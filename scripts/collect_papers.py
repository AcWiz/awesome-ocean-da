#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
论文搜集脚本 - 从 arXiv 搜集 AI+海洋数据同化相关论文

使用方法:
    python collect_papers.py [--max-results N] [--dry-run]

定时任务配置 (.github/workflows/collect.yml):
    每 5 分钟触发一次，每次最多搜集 3-5 篇新论文
"""

import argparse
import arxiv
import json
import logging
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional, Set

# 添加项目根目录到路径
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.search_strategy import (
    SEARCH_QUERIES,
    EXCLUDE_TERMS,
    ARXIV_CATEGORIES,
    METHOD_TAGS,
    APPLICATION_TAGS,
)
from scripts.paper_schema import PaperMetadata, extract_tags_from_text

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)


class PaperCollector:
    """论文搜集器"""

    COLLECTED_IDS_FILE = PROJECT_ROOT / ".collected_ids"
    PAPERS_DIR = PROJECT_ROOT / "papers"

    def __init__(self, max_results_per_query: int = 5):
        self.max_results_per_query = max_results_per_query
        self.collected_ids: Set[str] = set()
        self.newly_collected = []
        self._load_collected_ids()

    def _load_collected_ids(self):
        """加载已收集的论文 ID"""
        if self.COLLECTED_IDS_FILE.exists():
            try:
                with open(self.COLLECTED_IDS_FILE, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.collected_ids = set(data.get('collected', []))
                    logger.info(f"已加载 {len(self.collected_ids)} 篇已收集论文")
            except Exception as e:
                logger.warning(f"加载收集记录失败: {e}")

    def _save_collected_ids(self):
        """保存已收集的论文 ID"""
        data = {
            'collected': list(self.collected_ids),
            'last_run': datetime.now().isoformat(),
            'total_count': len(self.collected_ids),
        }
        try:
            with open(self.COLLECTED_IDS_FILE, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logger.info(f"已保存 {len(self.collected_ids)} 篇论文到收集记录")
        except Exception as e:
            logger.error(f"保存收集记录失败: {e}")

    def _is_relevant(self, title: str, abstract: str) -> bool:
        """检查论文是否与目标领域相关"""
        text = (title + " " + abstract).lower()

        # 排除不相关领域
        for term in EXCLUDE_TERMS:
            if term.lower() in text:
                return False

        # 必须包含海洋/数据同化相关词汇
        ocean_terms = ['ocean', 'sea', 'marine', 'sea surface', 'sst', 'ssh']
        da_terms = ['data assimilation', 'state estimation', 'reanalysis',
                    'kalman', 'variational', '4d-var', '4dvar', 'enkf']

        has_ocean = any(term in text for term in ocean_terms)
        has_da = any(term in text for term in da_terms)

        return has_ocean or has_da

    def _extract_tags(self, title: str, abstract: str) -> tuple:
        """提取方法和应用标签"""
        text = title + " " + abstract
        method_tags = extract_tags_from_text(text, METHOD_TAGS)
        application_tags = extract_tags_from_text(text, APPLICATION_TAGS)
        return method_tags, application_tags

    def _get_year_from_arxiv_id(self, arxiv_id: str) -> int:
        """从 arXiv ID 提取年份"""
        # 格式: YYMM.NNNNN 或 YYMM.NNNNNvV
        match = re.match(r'(\d{4})', arxiv_id)
        if match:
            yy = int(match.group(1)[:2])
            mm = int(match.group(1)[2:4])
            year = 2000 + yy if yy < 90 else 1900 + yy
            return year
        return datetime.now().year

    def _create_paper_dir(self, paper: PaperMetadata) -> Path:
        """创建论文目录"""
        year_dir = self.PAPERS_DIR / str(paper.year)
        year_dir.mkdir(parents=True, exist_ok=True)

        # 生成短名称
        short_name = paper.short_name
        paper_dir = year_dir / short_name

        # 如果目录已存在，添加数字后缀
        counter = 1
        while paper_dir.exists():
            paper_dir = year_dir / f"{short_name}_{counter}"
            counter += 1

        paper_dir.mkdir(parents=True, exist_ok=True)
        return paper_dir

    def _download_pdf(self, paper: PaperMetadata, save_dir: Path) -> Optional[Path]:
        """下载论文 PDF"""
        try:
            client = arxiv.Client()
            search = arxiv.Search(id_list=[paper.arxiv_id])
            results = list(client.results(search))

            if results:
                paper_pdf = results[0]
                pdf_path = save_dir / "paper.pdf"
                paper_pdf.download_pdf(dirpath=str(save_dir), filename="paper.pdf")
                logger.info(f"已下载 PDF: {pdf_path}")
                return pdf_path
        except Exception as e:
            logger.warning(f"下载 PDF 失败: {e}")
        return None

    def collect_from_arxiv(self, query: str, max_results: int = 5) -> list:
        """从 arXiv 搜集论文"""
        papers = []

        try:
            client = arxiv.Client(
                page_size=min(max_results, 100),
                delay_seconds=3.0,  # 避免过于频繁
            )

            search = arxiv.Search(
                query=query,
                max_results=max_results,
                sort_by=arxiv.SortCriterion.SubmittedDate,
                sort_order=arxiv.SortOrder.Descending,
            )

            logger.info(f"搜索: {query}")
            results = list(client.results(search))

            for result in results:
                arxiv_id = result.entry_id.split('/')[-1]

                # 去重检查
                if arxiv_id in self.collected_ids:
                    logger.debug(f"跳过已收集: {arxiv_id}")
                    continue

                # 提取信息
                title = result.title or "Untitled"
                abstract = result.summary or ""

                # 相关性检查
                if not self._is_relevant(title, abstract):
                    logger.debug(f"跳过不相关: {title[:50]}...")
                    continue

                # 提取标签
                method_tags, application_tags = self._extract_tags(title, abstract)

                # 如果没有匹配到任何标签，给一个默认标签
                if not method_tags and not application_tags:
                    method_tags = ["Deep-Learning"]

                paper = PaperMetadata(
                    title=title,
                    arxiv_id=arxiv_id,
                    authors=[str(a) for a in result.authors],
                    year=self._get_year_from_arxiv_id(arxiv_id),
                    source="arXiv",
                    abstract=abstract,
                    method_tags=method_tags,
                    application_tags=application_tags,
                    paper_url=result.entry_id,
                    pdf_url=result.pdf_url,
                )

                papers.append(paper)
                logger.info(f"找到论文: {title[:60]}...")

        except Exception as e:
            logger.error(f"搜索失败 '{query}': {e}")

        # 避免过于频繁
        time.sleep(2)
        return papers

    def save_paper(self, paper: PaperMetadata) -> bool:
        """保存论文到目录"""
        try:
            paper_dir = self._create_paper_dir(paper)

            # 写入 abstract.md
            abstract_path = paper_dir / "abstract.md"
            with open(abstract_path, 'w', encoding='utf-8') as f:
                f.write(paper.to_markdown())

            logger.info(f"已保存: {paper_dir}")
            return True

        except Exception as e:
            logger.error(f"保存论文失败: {e}")
            return False

    def run(self, dry_run: bool = False, max_per_query: int = 3) -> int:
        """运行搜集"""
        logger.info("=" * 60)
        logger.info("开始搜集 AI+海洋数据同化论文")
        logger.info("=" * 60)

        total_collected = 0

        for query in SEARCH_QUERIES:
            if total_collected >= self.max_results_per_query:
                logger.info(f"已达到本次搜集上限 ({self.max_results_per_query})")
                break

            papers = self.collect_from_arxiv(query, max_results=max_per_query)

            for paper in papers[:self.max_results_per_query - total_collected]:
                if dry_run:
                    logger.info(f"[DRY RUN] 将收集: {paper.title[:50]}...")
                else:
                    if self.save_paper(paper):
                        self.collected_ids.add(paper.arxiv_id)
                        self.newly_collected.append(paper)
                        total_collected += 1

            if total_collected >= self.max_results_per_query:
                break

        # 保存更新后的 ID 列表
        if not dry_run:
            self._save_collected_ids()

        logger.info("=" * 60)
        logger.info(f"本次搜集完成: {total_collected} 篇")
        logger.info(f"累计收集: {len(self.collected_ids)} 篇")
        logger.info("=" * 60)

        return total_collected


def main():
    parser = argparse.ArgumentParser(description="搜集 AI+海洋数据同化论文")
    parser.add_argument("--max-results", type=int, default=5,
                        help="本次最多搜集论文数 (默认: 5)")
    parser.add_argument("--max-per-query", type=int, default=3,
                        help="每个查询最多返回数 (默认: 3)")
    parser.add_argument("--dry-run", action="store_true",
                        help="仅测试，不实际保存")
    args = parser.parse_args()

    collector = PaperCollector(max_results_per_query=args.max_per_query)
    collected = collector.run(dry_run=args.dry_run, max_per_query=args.max_per_query)

    return 0 if collected >= 0 else 1


if __name__ == "__main__":
    sys.exit(main())

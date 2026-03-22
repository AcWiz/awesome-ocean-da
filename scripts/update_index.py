# -*- coding: utf-8 -*-
"""更新 Jekyll 索引文件"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent
PAPERS_DIR = PROJECT_ROOT / "papers"
OUTPUT_FILE = PROJECT_ROOT / "_data" / "papers.json"


def parse_abstract_md(file_path: Path) -> dict:
    """解析 abstract.md，提取 YAML front matter 和内容"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 提取 YAML front matter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            import yaml
            try:
                metadata = yaml.safe_load(parts[1]) or {}
                body = parts[2].strip()
                return metadata, body
            except:
                pass

    return {}, content


def _extract_preview(body: str) -> str:
    """从论文摘要/总结内容中提取预览文本。

    优先提取 TL;DR 部分（迁移后 summary.md 的第2节），否则取前200字。
    """
    import re
    lines = body.split('\n')
    for i, line in enumerate(lines):
        if 'TL;DR' in line or 'tl;dr' in line.lower():
            # 找到 TL;DR 行后，找下一段非空内容
            for j in range(i + 1, len(lines)):
                next_line = lines[j].strip()
                if next_line and not next_line.startswith('#'):
                    # 清理 Markdown 格式符号
                    preview = re.sub(r'[#*`]', '', next_line).strip()
                    return preview[:200]

    # 回退：找第一个非标题段落
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#') and len(line) > 20:
            preview = re.sub(r'[#*`]', '', line).strip()
            return preview[:200]

    # 最后回退：前200字
    preview = re.sub(r'[#*`]', '', body).strip()[:200]
    return preview


def scan_papers() -> list:
    """扫描所有论文目录"""
    papers = []

    for year_dir in sorted(PAPERS_DIR.iterdir(), reverse=True):
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue

        year = int(year_dir.name)

        for paper_dir in sorted(year_dir.iterdir()):
            if not paper_dir.is_dir():
                continue

            abstract_file = paper_dir / "abstract.md"
            if not abstract_file.exists():
                continue

            metadata, body = parse_abstract_md(abstract_file)

            paper_info = {
                'path': str(paper_dir.relative_to(PROJECT_ROOT)),
                'year': year,
                'title': metadata.get('title', paper_dir.name),
                'arxiv': metadata.get('arXiv', ''),
                'authors': metadata.get('authors', []),
                'source': metadata.get('source', 'arXiv'),
                'venue': metadata.get('venue', ''),
                'method_tags': metadata.get('method_tags', []),
                'application_tags': metadata.get('application_tags', []),
                'date_collected': metadata.get('date_collected', ''),
                'paper_url': metadata.get('paper_url', ''),
            }

            # 提取摘要预览：优先从 TL;DR 部分提取，否则取前200字
            abstract_preview = _extract_preview(body)
            paper_info['abstract_preview'] = abstract_preview

            papers.append(paper_info)

    return papers


def generate_statistics(papers: list) -> dict:
    """生成统计信息"""
    stats = {
        'total': len(papers),
        'by_year': {},
        'by_method': {},
        'by_application': {},
    }

    for paper in papers:
        # 按年份统计
        year = paper['year']
        stats['by_year'][year] = stats['by_year'].get(year, 0) + 1

        # 按方法统计
        for tag in paper['method_tags']:
            stats['by_method'][tag] = stats['by_method'].get(tag, 0) + 1

        # 按应用统计
        for tag in paper['application_tags']:
            stats['by_application'][tag] = stats['by_application'].get(tag, 0) + 1

    return stats


def update_index():
    """更新索引文件"""
    print("扫描论文目录...")
    papers = scan_papers()
    print(f"找到 {len(papers)} 篇论文")

    stats = generate_statistics(papers)

    # 确保输出目录存在
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    # 写入 JSON 索引
    data = {
        'papers': papers,
        'statistics': stats,
        'last_updated': datetime.now().isoformat(),
    }

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"索引已更新: {OUTPUT_FILE}")
    print(f"  - 总论文数: {stats['total']}")
    print(f"  - 年份分布: {stats['by_year']}")
    print(f"  - 方法分布: {list(stats['by_method'].keys())[:5]}...")
    print(f"  - 应用分布: {list(stats['by_application'].keys())[:5]}...")


if __name__ == "__main__":
    update_index()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
下载 arXiv 论文的 Abstract 和 Introduction 内容

Usage:
    python scripts/fetch_arxiv_content.py --dry-run --limit 3
    python scripts/fetch_arxiv_content.py --apply
    python scripts/fetch_arxiv_content.py --status
"""

import argparse
import logging
import sys
import time
from pathlib import Path
from typing import Optional, Tuple

import requests
from bs4 import BeautifulSoup
import yaml

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('workspace/logs/fetch_arxiv.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

# 路径配置
PAPERS_DIR = Path(__file__).parent.parent / "papers"
OUTPUT_DIR = Path(__file__).parent.parent / "papers"


def parse_abstract_md(abstract_md_path: Path) -> dict:
    """解析 abstract.md 的 YAML front matter"""
    try:
        with open(abstract_md_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 提取 YAML front matter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                yaml_content = parts[1]
                metadata = yaml.safe_load(yaml_content)
                return metadata or {}
    except Exception as e:
        logger.warning(f"解析 {abstract_md_path} 失败: {e}")
    return {}


def fetch_arxiv_content(arxiv_id: str, timeout: int = 30) -> Tuple[str, str]:
    """
    获取 arXiv 论文的 Abstract 和 Introduction

    优先尝试 HTML 格式（包含 Introduction），失败则回退到 abs 格式（仅 Abstract）

    Args:
        arxiv_id: arXiv ID (如 '2410.20072v2')
        timeout: 请求超时时间（秒）

    Returns:
        (abstract, introduction) 元组
    """
    # 清理 arXiv ID（移除版本号或 'v' 前缀）
    clean_id = arxiv_id.split('v')[0] if 'v' in arxiv_id else arxiv_id

    abstract = ""
    introduction = ""

    # 优先尝试 HTML 页面（包含 Introduction）
    html_url = f"https://arxiv.org/html/{clean_id}"
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        resp = requests.get(html_url, headers=headers, timeout=timeout)
        resp.raise_for_status()
        html = resp.text

        # 解析 HTML 格式
        soup = BeautifulSoup(html, 'html.parser')

        # 提取 Abstract
        abstract_elem = soup.find('div', class_='ltx_abstract')
        if abstract_elem:
            abstract_text = abstract_elem.get_text(strip=True)
            abstract = abstract_text.replace('Abstract', '', 1).strip()

        # 提取 Introduction
        intro_section = soup.find('section', id='S1') or soup.find('section', id='introduction')
        if intro_section:
            paragraphs = intro_section.find_all('div', class_='ltx_para')
            introduction = "\n\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
        else:
            # 备用：查找包含 "Introduction" 的 section
            for section in soup.find_all('section'):
                h2 = section.find('h2', class_='ltx_title')
                if h2 and 'introduction' in h2.get_text(strip=True).lower():
                    paragraphs = section.find_all('div', class_='ltx_para')
                    introduction = "\n\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
                    break

        logger.info(f"  HTML 格式获取成功: abstract({len(abstract)} chars), intro({len(introduction)} chars)")
        return abstract, introduction

    except requests.RequestException as e:
        logger.warning(f"  HTML 获取失败 ({html_url}): {e}")

    # 回退到 abs 页面（只有 Abstract）
    abs_url = f"https://arxiv.org/abs/{clean_id}"
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        resp = requests.get(abs_url, headers=headers, timeout=timeout)
        resp.raise_for_status()
        html = resp.text

        # 解析 abs 格式
        soup = BeautifulSoup(html, 'html.parser')

        # 方法1: 查找 blockquote (常包含摘要)
        blockquote = soup.find('blockquote')
        if blockquote:
            abstract = blockquote.get_text(strip=True)
            if abstract.startswith('Abstract'):
                abstract = abstract[8:].strip()

        # 方法2: 查找 meta tag
        if not abstract:
            meta = soup.find('meta', {'name': 'citation_abstract'})
            if meta and meta.get('content'):
                abstract = meta['content'].strip()

        # 方法3: 查找 og:description
        if not abstract:
            meta = soup.find('meta', {'property': 'og:description'})
            if meta and meta.get('content'):
                abstract = meta['content'].strip()

        if abstract:
            logger.info(f"  abs 页面获取成功: abstract({len(abstract)} chars)")
        return abstract, ""

    except requests.RequestException as e:
        logger.warning(f"  abs 页面获取失败 ({abs_url}): {e}")
        return "", ""


def save_arxiv_content(paper_dir: Path, abstract: str, introduction: str) -> bool:
    """
    保存 arXiv 内容到 arxiv_content.txt

    Args:
        paper_dir: 论文目录
        abstract: 摘要文本
        introduction: 引言文本

    Returns:
        是否成功保存
    """
    output_file = paper_dir / "arxiv_content.txt"

    content = f"""# arXiv Content
# 自动从 arXiv HTML 页面提取

## Abstract

{abstract}

## Introduction

{introduction}
"""

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        logger.error(f"保存 {output_file} 失败: {e}")
        return False


def process_paper(paper_dir: Path, dry_run: bool = False) -> dict:
    """
    处理单篇论文：下载并保存 arXiv 内容

    Args:
        paper_dir: 论文目录
        dry_run: 是否只预览不保存

    Returns:
        处理结果字典
    """
    abstract_md = paper_dir / "abstract.md"
    if not abstract_md.exists():
        return {"status": "skip", "reason": "no abstract.md"}

    # 解析 metadata
    metadata = parse_abstract_md(abstract_md)
    arxiv_id = metadata.get('arXiv', '')

    if not arxiv_id or arxiv_id.strip() == '':
        return {"status": "skip", "reason": "no arXiv ID", "paper": paper_dir.name}

    logger.info(f"处理论文: {paper_dir.name}, arXiv ID: {arxiv_id}")

    if dry_run:
        logger.info(f"[DRY RUN] 将会下载: {arxiv_id}")
        return {"status": "dry_run", "arxiv_id": arxiv_id, "paper": paper_dir.name}

    # 下载内容
    abstract, introduction = fetch_arxiv_content(arxiv_id)

    # 检查内容有效性
    if len(abstract) < 50:
        logger.warning(f"Abstract 太短 ({len(abstract)} chars): {paper_dir.name}")
        return {"status": "fail", "reason": "abstract too short", "arxiv_id": arxiv_id, "paper": paper_dir.name}

    # 保存
    if save_arxiv_content(paper_dir, abstract, introduction):
        return {
            "status": "success",
            "arxiv_id": arxiv_id,
            "paper": paper_dir.name,
            "abstract_len": len(abstract),
            "intro_len": len(introduction)
        }
    else:
        return {"status": "fail", "reason": "save failed", "arxiv_id": arxiv_id, "paper": paper_dir.name}


def find_all_paper_dirs() -> list:
    """查找所有论文目录"""
    paper_dirs = []
    if PAPERS_DIR.exists():
        for year_dir in sorted(PAPERS_DIR.iterdir()):
            if year_dir.is_dir() and year_dir.name.isdigit():
                for paper_dir in sorted(year_dir.iterdir()):
                    if paper_dir.is_dir():
                        paper_dirs.append(paper_dir)
    return paper_dirs


def main():
    parser = argparse.ArgumentParser(description="下载 arXiv 论文的 Abstract 和 Introduction")
    parser.add_argument("--dry-run", action="store_true", help="预览模式，不实际下载")
    parser.add_argument("--apply", action="store_true", help="正式执行下载")
    parser.add_argument("--limit", type=int, default=0, help="限制处理数量（0=全部）")
    parser.add_argument("--status", action="store_true", help="显示状态统计")
    parser.add_argument("--papers-dir", type=str, help="指定论文目录路径")

    args = parser.parse_args()

    global PAPERS_DIR
    if args.papers_dir:
        PAPERS_DIR = Path(args.papers_dir)

    # 状态模式
    if args.status:
        paper_dirs = find_all_paper_dirs()
        total = len(paper_dirs)
        with_id = 0
        without_id = 0
        has_content = 0

        for paper_dir in paper_dirs:
            abstract_md = paper_dir / "abstract.md"
            if abstract_md.exists():
                metadata = parse_abstract_md(abstract_md)
                arxiv_id = metadata.get('arXiv', '')
                if arxiv_id and arxiv_id.strip():
                    with_id += 1
                else:
                    without_id += 1

                # 检查是否已有 arxiv_content.txt
                if (paper_dir / "arxiv_content.txt").exists():
                    has_content += 1

        logger.info(f"=== 论文统计 ===")
        logger.info(f"总论文数: {total}")
        logger.info(f"有 arXiv ID: {with_id}")
        logger.info(f"无 arXiv ID: {without_id}")
        logger.info(f"已有 arxiv_content.txt: {has_content}")
        return

    # 确认模式
    if not args.dry_run and not args.apply:
        parser.print_help()
        logger.info("\n请使用 --dry-run 预览或 --apply 正式执行")
        return

    # 查找所有论文
    paper_dirs = find_all_paper_dirs()
    logger.info(f"找到 {len(paper_dirs)} 篇论文")

    # 统计
    results = {
        "total": 0,
        "dry_run": 0,
        "skip_no_id": 0,
        "skip_has_content": 0,
        "success": 0,
        "fail": 0
    }

    # 处理
    for i, paper_dir in enumerate(paper_dirs, 1):
        if args.limit > 0 and i > args.limit:
            break

        result = process_paper(paper_dir, dry_run=args.dry_run)
        results["total"] += 1

        if result["status"] == "dry_run":
            results["dry_run"] += 1
        elif result["status"] == "skip":
            if "no arXiv ID" in result.get("reason", ""):
                results["skip_no_id"] += 1
            else:
                results["skip_has_content"] += 1
        elif result["status"] == "success":
            results["success"] += 1
        elif result["status"] == "fail":
            results["fail"] += 1

        # 速率限制：每请求间隔 1 秒
        if args.apply and result["status"] not in ["skip", "dry_run"]:
            time.sleep(1.1)

    # 打印统计
    logger.info(f"\n=== 处理结果 ===")
    logger.info(f"总处理: {results['total']}")
    if args.dry_run:
        logger.info(f"预览模式: {results['dry_run']}")
    logger.info(f"无 arXiv ID: {results['skip_no_id']}")
    logger.info(f"成功: {results['success']}")
    logger.info(f"失败: {results['fail']}")


if __name__ == "__main__":
    main()

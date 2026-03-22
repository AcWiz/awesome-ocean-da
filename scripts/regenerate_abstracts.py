#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
使用 MiniMax-Text-01 生成新模板内容

基于下载的 arXiv 内容（Abstract + Introduction），使用 MiniMax API 生成结构化的论文分析模板

Usage:
    python scripts/regenerate_abstracts.py --dry-run --limit 3
    python scripts/regenerate_abstracts.py --apply --batch-size 10
"""

import argparse
import json
import logging
import os
import sys
import time
from pathlib import Path
from typing import Optional

import yaml

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('workspace/logs/regenerate_abstracts.log', encoding='utf-8')
    ]
)
logger = logging.getLogger(__name__)

# 路径配置
PAPERS_DIR = Path(__file__).parent.parent / "papers"

# MiniMax API 配置
MINIMAX_API_KEY = os.environ.get("MINIMAX_API_KEY", "")
MINIMAX_BASE_URL = "https://api.minimax.chat/v1/text/chatcompletion_pro"

# MiniMax Prompt 模板
PROMPT_TEMPLATE = """你是一个海洋科学和机器学习交叉领域的研究助手。请根据以下论文原文（标题 + 摘要 + 引言），按照新模板格式生成论文分析。

## 标题
{title}

## 摘要
{abstract}

## 引言
{introduction}

## 新模板格式要求

请按以下格式重写（使用中文）：

## TL;DR
一句话总结核心贡献（英文，50词以内）

## 研究问题
本文解决什么问题？研究动机和背景？

## 核心贡献
列出3-5个关键贡献点

## 方法详解
核心方法的技术描述

## 数学/物理建模
关键公式和物理意义（如果有）

## 实验分析
实验设置、结果、数据集

## 优缺点
客观评价

## 工程落地
实际应用场景

## Idea扩展
可借鉴到其他研究的想法

## BibTeX
根据论文信息生成标准格式引用
"""


def load_arxiv_content(paper_dir: Path) -> tuple:
    """加载 arXiv 内容"""
    content_file = paper_dir / "arxiv_content.txt"
    if not content_file.exists():
        return None, None

    with open(content_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 解析 Abstract 和 Introduction
    abstract = ""
    introduction = ""

    if "## Abstract" in content:
        parts = content.split("## Abstract")
        if len(parts) > 1:
            abstract_part = parts[1]
            if "## Introduction" in abstract_part:
                abstract = abstract_part.split("## Introduction")[0].strip()
            else:
                abstract = abstract_part.strip()

    if "## Introduction" in content:
        intro_part = content.split("## Introduction")[1]
        introduction = intro_part.strip()

    return abstract, introduction


def parse_abstract_md(abstract_md_path: Path) -> dict:
    """解析 abstract.md 的 YAML front matter"""
    try:
        with open(abstract_md_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                yaml_content = parts[1]
                metadata = yaml.safe_load(yaml_content)
                return metadata or {}
    except Exception as e:
        logger.warning(f"解析 {abstract_md_path} 失败: {e}")
    return {}


def call_minimax(prompt: str, model: str = "MiniMax-Text-01", timeout: int = 120) -> Optional[str]:
    """
    调用 MiniMax API

    Args:
        prompt: 提示词
        model: 模型名称
        timeout: 超时时间（秒）

    Returns:
        生成的文本，失败返回 None
    """
    if not MINIMAX_API_KEY:
        logger.error("MINIMAX_API_KEY 环境变量未设置")
        return None

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {MINIMAX_API_KEY}"
    }

    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 4096
    }

    try:
        import requests
        resp = requests.post(
            MINIMAX_BASE_URL,
            headers=headers,
            json=data,
            timeout=timeout
        )
        resp.raise_for_status()
        result = resp.json()

        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"]
        else:
            logger.error(f"API 返回格式异常: {result}")
            return None

    except Exception as e:
        logger.error(f"MiniMax API 调用失败: {e}")
        return None


def generate_template(title: str, abstract: str, introduction: str) -> Optional[str]:
    """
    使用 MiniMax 生成新模板

    Args:
        title: 论文标题
        abstract: 摘要
        introduction: 引言

    Returns:
        生成的模板内容
    """
    prompt = PROMPT_TEMPLATE.format(
        title=title,
        abstract=abstract[:3000] if abstract else "",  # 限制输入长度
        introduction=introduction[:5000] if introduction else ""  # 限制输入长度
    )

    return call_minimax(prompt)


def find_papers_to_process() -> list:
    """查找需要处理的论文"""
    papers = []

    if not PAPERS_DIR.exists():
        return papers

    for year_dir in sorted(PAPERS_DIR.iterdir()):
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue

        for paper_dir in sorted(year_dir.iterdir()):
            if not paper_dir.is_dir():
                continue

            abstract_md = paper_dir / "abstract.md"
            arxiv_content = paper_dir / "arxiv_content.txt"

            if not abstract_md.exists() or not arxiv_content.exists():
                continue

            # 检查是否已有新模板（通过检查是否有 TL;DR）
            with open(abstract_md, 'r', encoding='utf-8') as f:
                content = f.read()
                if "## TL;DR" in content or "## TL;DR" in content:
                    continue

            papers.append(paper_dir)

    return papers


def update_abstract_md(paper_dir: Path, metadata: dict, generated_content: str) -> bool:
    """
    更新 abstract.md 文件

    Args:
        paper_dir: 论文目录
        metadata: 元数据字典
        generated_content: 生成的内容

    Returns:
        是否成功
    """
    abstract_md = paper_dir / "abstract.md"

    # 构建新的 YAML front matter
    new_front_matter = f"""---
title: '{metadata.get('title', '')}'
arXiv: '{metadata.get('arXiv', '')}'
authors: {metadata.get('authors', [])}
year: {metadata.get('year', '')}
source: {metadata.get('source', 'arXiv')}
venue: {metadata.get('venue', 'arXiv')}
domain_tags: {metadata.get('domain_tags', [])}
ocean_vars: {metadata.get('ocean_vars', '')}
spatiotemporal_res: {metadata.get('spatiotemporal_res', 'Unknown')}
difficulty: '{metadata.get('difficulty', '★★★☆☆')}'
importance: '{metadata.get('importance', '★★★☆☆')}'
read_status: {metadata.get('read_status', 'skim')}
---

"""

    new_content = new_front_matter + generated_content

    try:
        with open(abstract_md, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    except Exception as e:
        logger.error(f"更新 {abstract_md} 失败: {e}")
        return False


def process_paper(paper_dir: Path, dry_run: bool = False) -> dict:
    """
    处理单篇论文

    Args:
        paper_dir: 论文目录
        dry_run: 是否只预览

    Returns:
        处理结果
    """
    abstract_md = paper_dir / "abstract.md"
    if not abstract_md.exists():
        return {"status": "skip", "reason": "no abstract.md"}

    # 加载 metadata
    metadata = parse_abstract_md(abstract_md)
    title = metadata.get('title', paper_dir.name)

    # 加载 arXiv 内容
    abstract, introduction = load_arxiv_content(paper_dir)

    if not abstract:
        return {"status": "skip", "reason": "no abstract content"}

    logger.info(f"处理论文: {paper_dir.name}")

    if dry_run:
        logger.info(f"[DRY RUN] 将会生成模板: {title[:50]}...")
        return {"status": "dry_run", "title": title, "paper": paper_dir.name}

    # 生成模板
    generated = generate_template(title, abstract, introduction)

    if not generated:
        return {"status": "fail", "reason": "MiniMax API failed", "paper": paper_dir.name}

    # 更新文件
    if update_abstract_md(paper_dir, metadata, generated):
        return {
            "status": "success",
            "title": title[:50],
            "paper": paper_dir.name
        }
    else:
        return {"status": "fail", "reason": "file update failed", "paper": paper_dir.name}


def main():
    parser = argparse.ArgumentParser(description="使用 MiniMax 生成新模板内容")
    parser.add_argument("--dry-run", action="store_true", help="预览模式，不实际调用 API")
    parser.add_argument("--apply", action="store_true", help="正式执行")
    parser.add_argument("--batch-size", type=int, default=10, help="每批处理数量")
    parser.add_argument("--limit", type=int, default=0, help="限制处理数量（0=全部）")
    parser.add_argument("--papers-dir", type=str, help="指定论文目录路径")

    args = parser.parse_args()

    global PAPERS_DIR
    if args.papers_dir:
        PAPERS_DIR = Path(args.papers_dir)

    if not args.dry_run and not args.apply:
        parser.print_help()
        logger.info("\n请使用 --dry-run 预览或 --apply 正式执行")
        return

    # 查找需要处理的论文
    papers = find_papers_to_process()
    logger.info(f"找到 {len(papers)} 篇论文需要处理")

    if args.limit > 0:
        papers = papers[:args.limit]
        logger.info(f"限制处理数量: {len(papers)}")

    if not papers:
        logger.info("没有需要处理的论文")
        return

    # 处理统计
    results = {
        "total": len(papers),
        "dry_run": 0,
        "success": 0,
        "fail": 0
    }

    # 分批处理
    for i, paper_dir in enumerate(papers, 1):
        logger.info(f"[{i}/{len(papers)}] 处理中...")

        result = process_paper(paper_dir, dry_run=args.dry_run)

        if result["status"] == "dry_run":
            results["dry_run"] += 1
        elif result["status"] == "success":
            results["success"] += 1
        elif result["status"] == "fail":
            results["fail"] += 1

        # 批次间暂停（避免 API 速率限制）
        if args.apply and result["status"] not in ["skip", "dry_run"]:
            time.sleep(2)  # 2 秒间隔

    # 打印统计
    logger.info(f"\n=== 处理结果 ===")
    logger.info(f"总处理: {results['total']}")
    if args.dry_run:
        logger.info(f"预览模式: {results['dry_run']}")
    logger.info(f"成功: {results['success']}")
    logger.info(f"失败: {results['fail']}")


if __name__ == "__main__":
    main()

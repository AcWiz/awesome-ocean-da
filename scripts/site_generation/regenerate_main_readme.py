# -*- coding: utf-8 -*-
"""从 papers.json 生成主页 README"""

import json
from pathlib import Path
from collections import defaultdict
import sys

PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from datetime import datetime, timedelta

from utils.normalizers import normalize_arxiv, normalize_tag
from utils.tag_config import TAG_CATEGORIES, get_canonical_tag
from site_generation.config import (
    ASSIMILATION_METHOD_KEYWORDS, ASSIMILATION_APP_KEYWORDS,
    FORECAST_METHOD_KEYWORDS, FORECAST_APP_KEYWORDS,
    ASSIMILATION_SUBTAGS, FORECAST_SUBTAGS,
    ASSIMILATION_SUBTAG_DESCS, FORECAST_SUBTAG_DESCS,
)

PAPERS_JSON = PROJECT_ROOT / "_data" / "papers.json"
README_FILE = PROJECT_ROOT / "README.md"


def is_recent_paper(paper, days=7) -> bool:
    """检查论文是否在过去N天内收集"""
    date_str = paper.get('date_collected', '')
    if not date_str:
        return False
    try:
        collected = datetime.strptime(date_str, "%Y-%m-%d")
        return collected >= datetime.now() - timedelta(days=days)
    except ValueError:
        return False


def generate_new_papers_section(papers):
    """生成'新'区域 - 过去7天收集的论文"""
    recent = [p for p in papers if is_recent_paper(p)]
    if not recent:
        return []

    lines = []
    lines.append("## 新")
    lines.append("")
    lines.append(f"> 最近一周收集的论文（共 {len(recent)} 篇）")
    lines.append("")
    lines.append("| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |")
    lines.append("|------|------|-------|------|------|------|")

    for paper in sorted(recent, key=lambda x: x.get('arxiv') or '', reverse=True):
        lines.append(generate_paper_row(paper))

    lines.append("")
    lines.append("---")
    lines.append("")

    return lines


def paper_matches_tag(paper, normalized_tag):
    """检查论文是否匹配给定标签"""
    for t in paper.get('method_tags', []) + paper.get('application_tags', []):
        if normalize_tag(t) == normalized_tag:
            return True
    return False


def get_venue_display(venue, source):
    """获取 venue 显示"""
    if venue and venue != '-':
        return venue
    if source == 'arXiv':
        return 'arXiv'
    return '-'


def format_tags_display(tags):
    """格式化标签为逗号分隔字符串"""
    if not tags:
        return '-'
    cleaned = [t.replace('_', '-') for t in tags]
    return ', '.join(cleaned)


PAPER_LIMIT = 6  # 主页每类最多显示6篇


def analyze_paper(paper):
    """一次性分析论文的分类和子分类，避免重复规范化标签

    Returns:
        tuple: (categories: set, subtag_results: list of (subtag_name, subtag_file), norm_method_tags: set, norm_app_tags: set)
    """
    norm_method_tags = {normalize_tag(t) for t in paper.get('method_tags', [])}
    norm_app_tags = {normalize_tag(t) for t in paper.get('application_tags', [])}
    all_tags = norm_method_tags | norm_app_tags

    categories = set()
    if (norm_method_tags & ASSIMILATION_METHOD_KEYWORDS) or \
       (norm_app_tags & ASSIMILATION_APP_KEYWORDS):
        categories.add('assimilation')
    if (norm_method_tags & FORECAST_METHOD_KEYWORDS) or \
       (norm_app_tags & FORECAST_APP_KEYWORDS):
        categories.add('forecast')

    subtag_results = []
    seen_subtags = set()
    for tag in all_tags:
        canonical = get_canonical_tag(tag)
        if canonical in ASSIMILATION_SUBTAGS:
            result = ASSIMILATION_SUBTAGS[canonical]
        elif canonical in FORECAST_SUBTAGS:
            result = FORECAST_SUBTAGS[canonical]
        else:
            continue
        if result not in seen_subtags:
            seen_subtags.add(result)
            subtag_results.append(result)

    return (categories, subtag_results, norm_method_tags, norm_app_tags)


def get_paper_subcategories(paper, category):
    """获取论文在指定类别下的子分类列表"""
    _, subtag_results, _, _ = analyze_paper(paper)
    target_subtags = ASSIMILATION_SUBTAGS if category == 'assimilation' else FORECAST_SUBTAGS
    return [s for s in subtag_results if s in target_subtags.values()]


def generate_paper_row(paper):
    """生成论文表格行（主页格式）

    主页格式: | 年份 | 论文 | Venue | 方法 | 应用 | 总结 |
    """
    arxiv = normalize_arxiv(paper.get('arxiv', ''))
    year = paper.get('year', '')
    folder = paper.get('path', '').replace('papers/', '')
    title = paper.get('title', '')
    venue = get_venue_display(paper.get('venue', ''), paper.get('source', 'arXiv'))
    method_tags = format_tags_display(paper.get('method_tags', []))
    app_tags = format_tags_display(paper.get('application_tags', []))

    # 构建论文链接（指向 arXiv）
    if arxiv:
        title_link = f"[{title}](https://arxiv.org/abs/{arxiv})"
    else:
        title_link = title

    # 构建总结链接（指向 summary.md）
    if arxiv:
        summary_link = f"[总结](./papers/{folder}/summary.md)"
    else:
        summary_link = "-"

    # 移除 arXiv 列（论文列已链接到 arXiv），添加总结列
    row = f"| {year} | {title_link} | {venue} | {method_tags} | {app_tags} | {summary_link} |"

    return row


def generate_category_section(category_name, category_file, papers, normalized_tag, method_desc=""):
    """生成单个分类部分"""
    # 过滤包含该标签的论文
    filtered = []
    for p in papers:
        if paper_matches_tag(p, normalized_tag):
            filtered.append(p)

    if not filtered:
        return []

    # 按年份分组
    by_year = defaultdict(list)
    for p in filtered:
        by_year[p['year']].append(p)

    lines = []
    lines.append(f"### {category_name}")
    if method_desc:
        lines.append(f"> {method_desc}")
    lines.append("")
    lines.append(f"| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |")
    lines.append("|------|------|-------|------|------|------|")

    # 只显示前几篇（主页只显示摘要）
    count = 0
    for year in sorted(by_year.keys(), reverse=True):
        for paper in sorted(by_year[year], key=lambda x: x.get('arxiv') or '', reverse=True):
            if count >= PAPER_LIMIT:
                break
            lines.append(generate_paper_row(paper))
            count += 1
        if count >= PAPER_LIMIT:
            break

    lines.append("")
    lines.append(f"[更多 {category_name} 论文 →](./papers/{category_file})")
    lines.append("")
    lines.append("---")
    lines.append("")

    return lines


def generate_dual_section(category, subtag_list, papers, subtag_descs=None):
    """生成数据同化或预报的子分区

    Args:
        category: 'assimilation' or 'forecast'
        subtag_list: list of (subtag_key, (subtag_name, subtag_file)) tuples
        papers: all papers
        subtag_descs: optional dict of subtag_key -> description
    """
    # subtag_name (display name) -> list of papers (deduplicated at assignment time)
    subtag_papers = defaultdict(list)

    for p in papers:
        categories, subtag_results, _, _ = analyze_paper(p)
        if category not in categories:
            continue
        # 获取该论文属于哪些子分类
        matched = get_paper_subcategories(p, category)
        for subtag_name, subtag_file in matched:
            # Deduplicate at assignment time by checking path
            if not any(pp['path'] == p['path'] for pp in subtag_papers[subtag_name]):
                subtag_papers[subtag_name].append(p)

    lines = []
    for subtag_key, (subtag_name, subtag_file) in subtag_list:
        if subtag_name not in subtag_papers or not subtag_papers[subtag_name]:
            continue

        filtered = subtag_papers[subtag_name]
        by_year = defaultdict(list)
        for p in filtered:
            by_year[p['year']].append(p)

        desc = subtag_descs.get(subtag_key, "") if subtag_descs else ""
        lines.append(f"### {subtag_name}")
        if desc:
            lines.append(f"> {desc}")
        lines.append("")
        lines.append(f"| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |")
        lines.append("|------|------|-------|------|------|------|")

        count = 0
        for year in sorted(by_year.keys(), reverse=True):
            for paper in sorted(by_year[year], key=lambda x: x.get('arxiv') or '', reverse=True):
                if count >= PAPER_LIMIT:
                    break
                lines.append(generate_paper_row(paper))
                count += 1
            if count >= PAPER_LIMIT:
                break

        lines.append("")
        lines.append(f"[更多 {subtag_name} 论文 →](./papers/{subtag_file})")
        lines.append("")
        lines.append("---")
        lines.append("")

    return lines


def generate_year_browse_section(papers):
    """生成按年份浏览部分"""
    by_year = defaultdict(list)
    for p in papers:
        by_year[p['year']].append(p)

    lines = []
    lines.append("## 按年份浏览")
    lines.append("")
    lines.append("| 年份 | 论文数 | 浏览 |")
    lines.append("|------|--------|------|")

    for year in sorted(by_year.keys(), reverse=True):
        count = len(by_year[year])
        lines.append(f"| {year} | {count} | [浏览](./papers/{year}/index.md) |")

    lines.append("")
    lines.append("---")
    lines.append("")

    return lines


def main():
    print("加载 papers.json...")

    if not PAPERS_JSON.exists():
        print(f"错误: {PAPERS_JSON} 不存在，请先运行 update_index.py")
        return

    with open(PAPERS_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    papers = data.get('papers', [])
    print(f"找到 {len(papers)} 篇论文")

    # 收集所有已生成的分类
    generated_categories = set()

    # 生成数据同化方法部分
    assim_lines = []
    assim_lines.append("## 数据同化方法")
    assim_lines.append("")
    assim_lines.append("（聚焦：状态估计、重建、同化）")
    assim_lines.append("")

    # Deduplicate subtag list by subtag_name to avoid duplicate sections
    # Structure: (subtag_key, (subtag_name, subtag_file))
    assim_subtags = [
        ('4d-var', ('4D-Var / EnKF', '4d-var.md')),
        ('koopman', ('Koopman 学习', 'koopman.md')),
        ('pinn', ('PINN (数据同化方向)', 'pinn.md')),
    ]
    assim_section = generate_dual_section('assimilation', assim_subtags, papers, ASSIMILATION_SUBTAG_DESCS)
    assim_lines.extend(assim_section)

    # 生成海洋预报方法部分
    forecast_lines = []
    forecast_lines.append("## 海洋预报方法")
    forecast_lines.append("")
    forecast_lines.append("（聚焦：未来状态预测）")
    forecast_lines.append("")

    # Structure: (subtag_key, (subtag_name, subtag_file))
    forecast_subtags = [
        ('fno', ('神经算子 (FNO)', 'neural-operator.md')),
        ('gnn', ('图神经网络 (GNN)', 'gnn.md')),
        ('transformer', ('Transformer / Attention', 'transformer.md')),
        ('lstm', ('LSTM', 'lstm.md')),
        ('forecasting', ('预报基础方法', 'forecasting.md')),
    ]
    forecast_section = generate_dual_section('forecast', forecast_subtags, papers, FORECAST_SUBTAG_DESCS)
    forecast_lines.extend(forecast_section)

    # 生成应用场景部分
    app_lines = []
    app_lines.append("## 应用场景")
    app_lines.append("")

    app_tags = [
        ("sst", "海表温度是海洋最重要的基础变量之一"),
        ("ssh", "海表高度反映海洋动力过程和环流结构"),
        ("enso", "ENSO 是最强的年际气候变化信号"),
        ("wave", "海浪对海洋工程和航行安全至关重要"),
        ("global-forecast", "全球海洋预报是气候预测的基础"),
    ]

    for tag, desc in app_tags:
        if tag in TAG_CATEGORIES:
            cat_name, cat_file = TAG_CATEGORIES[tag]
            lines = generate_category_section(cat_name, cat_file, papers, tag, desc)
            if lines:
                app_lines.extend(lines)
                generated_categories.add(cat_file)

    # 生成年份浏览部分
    year_lines = generate_year_browse_section(papers)

    # 组装完整 README
    total = len(papers)
    years = sorted(set(p['year'] for p in papers), reverse=True)
    latest_year = years[0] if years else 2026

    readme_lines = []
    readme_lines.append("# AI + 海洋数据同化论文库")
    readme_lines.append("")
    readme_lines.append("> 收录 AI/深度学习 + 海洋数据同化、预报相关的学术论文，持续更新。")
    readme_lines.append("")
    readme_lines.append(f"[![Papers](https://img.shields.io/badge/Papers-{total}-blue.svg)](#) ·")
    readme_lines.append(f"[![{latest_year}](https://img.shields.io/badge/{latest_year}-19-green.svg)](#papers-by-year) ·")
    readme_lines.append("[![Last Updated](https://img.shields.io/badge/Updated-2026--03--23-orange.svg)](#) ·")
    readme_lines.append("[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)")
    readme_lines.append("")
    readme_lines.append("---")
    readme_lines.append("")
    readme_lines.append("## 目录")
    readme_lines.append("")
    readme_lines.append("- [数据同化方法](#数据同化方法)")
    readme_lines.append("  - [4D-Var / EnKF](#4d-var--enkf)")
    readme_lines.append("  - [Koopman 学习](#koopman-学习)")
    readme_lines.append("  - [PINN (数据同化方向)](#pinn-数据同化方向)")
    readme_lines.append("- [海洋预报方法](#海洋预报方法)")
    readme_lines.append("  - [神经算子 (FNO)](#神经算子-fno)")
    readme_lines.append("  - [图神经网络 (GNN)](#图神经网络-gnn)")
    readme_lines.append("  - [Transformer / Attention](#transformer--attention)")
    readme_lines.append("  - [LSTM](#lstm)")
    readme_lines.append("  - [预报基础方法](#预报基础方法)")
    readme_lines.append("- [新](#新)")
    readme_lines.append("- [应用场景](#应用场景)")
    readme_lines.append("  - [海表温度 (SST)](#海表温度-sst)")
    readme_lines.append("  - [海表高度 (SSH)](#海表高度-ssh)")
    readme_lines.append("  - [ENSO 预测](#enso-预测)")
    readme_lines.append("  - [海浪预报](#海浪预报)")
    readme_lines.append("  - [全球预报](#全球预报)")
    readme_lines.append("- [按年份浏览](#papers-by-year)")
    readme_lines.append("- [如何贡献](./CONTRIBUTING.md)")
    readme_lines.append("")
    readme_lines.append("---")
    readme_lines.append("")

    readme_lines.extend(assim_lines)
    readme_lines.extend(forecast_lines)

    # 生成新论文区域
    new_lines = generate_new_papers_section(papers)
    readme_lines.extend(new_lines)

    readme_lines.extend(app_lines)
    readme_lines.extend(year_lines)

    # 贡献部分
    readme_lines.append("## 如何贡献")
    readme_lines.append("")
    readme_lines.append("欢迎提交 PR 或 Issue！详见 [贡献指南](./CONTRIBUTING.md)。")
    readme_lines.append("")

    # 写入文件
    content = '\n'.join(readme_lines)
    README_FILE.write_text(content, encoding='utf-8')
    print(f"生成: {README_FILE}")

    print("\n完成!")


if __name__ == "__main__":
    main()

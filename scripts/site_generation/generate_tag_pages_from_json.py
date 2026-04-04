# -*- coding: utf-8 -*-
"""从 papers.json 生成标签分类页面"""

import json
from pathlib import Path
from collections import defaultdict
import sys

PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from utils.normalizers import normalize_arxiv, normalize_tag
from utils.tag_config import TAG_CATEGORIES, TAG_ALIASES, get_canonical_tag

PAPERS_JSON = PROJECT_ROOT / "_data" / "papers.json"
PAPERS_DIR = PROJECT_ROOT / "papers"
OUTPUT_DIR = PAPERS_DIR


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


def paper_matches_tag(paper, normalized_tag):
    """检查论文是否匹配给定标签（规范化后，支持别名解析）"""
    for t in paper.get('method_tags', []) + paper.get('application_tags', []):
        tag = normalize_tag(t)
        # 解析别名到规范标签
        canonical = get_canonical_tag(tag)
        if canonical == normalized_tag:
            return True
    return False


def generate_paper_row(paper):
    """生成论文表格行

    统一格式: | 年份 | 论文 | arXiv | Venue | 方法标签 | 应用 | 总结 |
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

    # 构建 arXiv 链接
    if arxiv:
        arxiv_link = f"[{arxiv}](https://arxiv.org/abs/{arxiv})"
    else:
        arxiv_link = "ID 待查"

    # 构建总结链接（指向 abstract.md）
    # folder 格式是 "2022/2211.05904"，直接使用即可
    if arxiv:
        summary_link = f"[总结](./{folder}/abstract.md)"
    else:
        summary_link = "-"

    # 格式: | 年份 | 论文 | arXiv | Venue | 方法标签 | 应用 | 总结 |
    row = f"| {year} | {title_link} | {arxiv_link} | {venue} | {method_tags} | {app_tags} | {summary_link} |"

    return row


def generate_category_page(category_name, papers, normalized_tag):
    """生成单个分类页面"""
    # 过滤包含该标签的论文
    filtered = []
    for p in papers:
        if paper_matches_tag(p, normalized_tag):
            filtered.append(p)

    # 按年份分组
    by_year = defaultdict(list)
    for p in filtered:
        by_year[p['year']].append(p)

    lines = []
    lines.append(f"# {category_name} 论文列表")
    lines.append("")
    lines.append(f"> 收录 AI/深度学习 + {category_name} 相关论文，共 {len(filtered)} 篇。")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 生成表格（统一格式）
    lines.append("| 年份 | 论文 | arXiv | Venue | 方法标签 | 应用 | 总结 |")
    lines.append("|------|------|-------|-------|----------|------|------|")

    for year in sorted(by_year.keys(), reverse=True):
        for paper in sorted(by_year[year], key=lambda x: x.get('arxiv') or '', reverse=True):
            lines.append(generate_paper_row(paper))

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"*最后更新: 2026-03-23*")

    return '\n'.join(lines)


def generate_all_category_pages(papers):
    """生成所有分类页面"""
    # 收集所有唯一标签（规范化后，包含别名解析后的规范形式）
    all_normalized_tags = set()
    for p in papers:
        for t in p.get('method_tags', []) + p.get('application_tags', []):
            tag = normalize_tag(t)
            all_normalized_tags.add(tag)
            # 同时添加别名解析后的规范形式
            all_normalized_tags.add(get_canonical_tag(tag))

    # 生成每个标签对应的分类页面
    generated = set()
    for normalized_tag, (category_name, filename) in TAG_CATEGORIES.items():
        if normalized_tag not in all_normalized_tags:
            continue
        if filename in generated:
            continue

        content = generate_category_page(category_name, papers, normalized_tag)
        filepath = OUTPUT_DIR / filename
        filepath.write_text(content, encoding='utf-8')
        print(f"生成: {filepath}")
        generated.add(filename)


def main():
    print("加载 papers.json...")

    if not PAPERS_JSON.exists():
        print(f"错误: {PAPERS_JSON} 不存在，请先运行 update_index.py")
        return

    with open(PAPERS_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    papers = data.get('papers', [])
    print(f"找到 {len(papers)} 篇论文")

    print("\n生成分类页面...")
    generate_all_category_pages(papers)

    print("\n完成!")


if __name__ == "__main__":
    main()

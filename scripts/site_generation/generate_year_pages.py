# -*- coding: utf-8 -*-
"""为每个年份生成索引页面"""

import json
from pathlib import Path
from collections import defaultdict
import sys

PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from utils.normalizers import normalize_arxiv

PAPERS_JSON = PROJECT_ROOT / "_data" / "papers.json"
PAPERS_DIR = PROJECT_ROOT / "papers"


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


def generate_paper_row(paper):
    """生成论文表格行

    统一格式: | 年份 | 论文 | arXiv | Venue | 方法标签 | 应用 | 总结 |
    """
    arxiv = normalize_arxiv(paper.get('arxiv', ''))
    year = paper.get('year', '')
    folder = paper.get('path', '').replace('papers/', '')
    # folder 格式是 "2026/2603.16312"，提取最后的论文文件夹名
    folder_name = folder.split('/')[-1]
    title = paper.get('title', '')
    venue = get_venue_display(paper.get('venue', ''), paper.get('source', 'arXiv'))
    method_tags = format_tags_display(paper.get('method_tags', []))
    app_tags = format_tags_display(paper.get('application_tags', []))

    # 构建论文链接
    if arxiv:
        title_link = f"[{title}](https://arxiv.org/abs/{arxiv})"
    else:
        title_link = title

    # 构建 arXiv 链接
    if arxiv:
        arxiv_link = f"[{arxiv}](https://arxiv.org/abs/{arxiv})"
    else:
        arxiv_link = "ID 待查"

    # 构建总结链接（相对于年份 index 页）
    if arxiv:
        summary_link = f"[总结](./{folder_name}/summary.md)"
    else:
        summary_link = "-"

    row = f"| {year} | {title_link} | {arxiv_link} | {venue} | {method_tags} | {app_tags} | {summary_link} |"

    return row


def generate_year_page(year, papers):
    """生成单个年份页面"""
    year_papers = [p for p in papers if p.get('year') == year]

    lines = []
    lines.append(f"# {year} 年论文列表")
    lines.append("")
    lines.append(f"> 共收录 {len(year_papers)} 篇论文。")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("| 年份 | 论文 | arXiv | Venue | 方法标签 | 应用 | 总结 |")
    lines.append("|------|------|-------|-------|----------|------|------|")

    for paper in sorted(year_papers, key=lambda x: x.get('arxiv') or '', reverse=True):
        lines.append(generate_paper_row(paper))

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"*最后更新: 2026-03-23*")

    return '\n'.join(lines)


def generate_all_year_pages(papers):
    """生成所有年份页面"""
    years = set(p['year'] for p in papers)

    for year in sorted(years, reverse=True):
        content = generate_year_page(year, papers)
        year_dir = PAPERS_DIR / str(year)
        year_dir.mkdir(exist_ok=True)

        filepath = year_dir / "index.md"
        filepath.write_text(content, encoding='utf-8')
        print(f"生成: {filepath}")


def main():
    print("加载 papers.json...")

    if not PAPERS_JSON.exists():
        print(f"错误: {PAPERS_JSON} 不存在，请先运行 update_index.py")
        return

    with open(PAPERS_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    papers = data.get('papers', [])
    print(f"找到 {len(papers)} 篇论文")

    print("\n生成年份页面...")
    generate_all_year_pages(papers)

    print("\n完成!")


if __name__ == "__main__":
    main()

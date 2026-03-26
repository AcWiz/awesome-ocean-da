# -*- coding: utf-8 -*-
"""生成缺失 arXiv ID 的报告，用于手动补充"""

import json
import re
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from utils.normalizers import normalize_arxiv

PAPERS_JSON = PROJECT_ROOT / "_data" / "papers.json"
OUTPUT_FILE = PROJECT_ROOT / "_data" / "missing_arxiv_report.md"


def main():
    print("加载 papers.json...")

    if not PAPERS_JSON.exists():
        print(f"错误: {PAPERS_JSON} 不存在，请先运行 update_index.py")
        return

    with open(PAPERS_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    papers = data.get('papers', [])
    print(f"找到 {len(papers)} 篇论文")

    # 分类论文
    missing = []      # arXiv 为空
    invalid = []     # arXiv 格式无效
    valid = []       # arXiv 有效

    for paper in papers:
        arxiv_raw = paper.get('arxiv', '')
        arxiv_normalized = normalize_arxiv(arxiv_raw)

        entry = {
            'year': paper.get('year'),
            'folder': paper.get('path', '').replace('papers/', ''),
            'title': paper.get('title', '')[:60],
            'arxiv_raw': arxiv_raw,
            'arxiv_normalized': arxiv_normalized,
        }

        if not arxiv_raw:
            missing.append(entry)
        elif arxiv_normalized is None:
            invalid.append(entry)
        else:
            valid.append(entry)

    # 生成报告
    lines = []
    lines.append("# arXiv ID 补充报告")
    lines.append("")
    lines.append(f"生成时间: 2026-03-23")
    lines.append(f"")
    lines.append(f"## 统计")
    lines.append(f"- 总论文数: {len(papers)}")
    lines.append(f"- 有效 arXiv: {len(valid)}")
    lines.append(f"- 缺失 arXiv: {len(missing)}")
    lines.append(f"- 无效格式: {len(invalid)}")
    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## 缺失 arXiv ID（共 {len(missing)} 篇）")
    lines.append(f"")
    lines.append(f"| 年份 | 文件夹 | 论文标题 | 当前值 |")
    lines.append(f"|------|--------|----------|--------|")
    for p in sorted(missing, key=lambda x: (x['year'], x['folder'])):
        lines.append(f"| {p['year']} | {p['folder']} | {p['title']}... | {p['arxiv_raw'] or '(空)'} |")

    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## 无效格式 arXiv ID（共 {len(invalid)} 篇）")
    lines.append(f"")
    lines.append(f"| 年份 | 文件夹 | 论文标题 | 当前值 | 建议 |")
    lines.append(f"|------|--------|----------|--------|------|")
    for p in sorted(invalid, key=lambda x: (x['year'], x['folder'])):
        # 判断无效类型
        if 'XXXXX' in p['arxiv_raw']:
            suggestion = "补充正确 arXiv ID"
        elif 'v' in p['arxiv_raw'].lower() and '.v' not in p['arxiv_raw']:
            # 可能是版本号格式错误
            suggestion = "检查格式（如 2503_19160 → 2503.19160）"
        elif p['arxiv_raw'] in ['arXiv preprint', '暂无']:
            suggestion = "补充正确 arXiv ID"
        else:
            suggestion = "检查格式"
        lines.append(f"| {p['year']} | {p['folder']} | {p['title']}... | {p['arxiv_raw']} | {suggestion} |")

    lines.append(f"")
    lines.append(f"---")
    lines.append(f"")
    lines.append(f"## 补充说明")
    lines.append(f"")
    lines.append(f"1. 找到对应论文的 `abstract.md` 文件")
    lines.append(f"2. 修改 `arXiv:` 字段为正确的 arXiv ID")
    lines.append(f"3. 运行 `python scripts/site_generation/update_index.py` 更新索引")
    lines.append(f"4. 运行 `python scripts/repair/fix_arxiv_links.py` 修复格式")
    lines.append(f"5. 重新生成页面")

    content = '\n'.join(lines)
    OUTPUT_FILE.write_text(content, encoding='utf-8')
    print(f"\n报告已生成: {OUTPUT_FILE}")
    print(f"  - 缺失: {len(missing)} 篇")
    print(f"  - 无效: {len(invalid)} 篇")


if __name__ == "__main__":
    main()

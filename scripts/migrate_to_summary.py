#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将每篇论文的 abstract.md 替换为 summary.md 内容。
这样 Jekyll 生成的论文详情页将显示中文详细摘要。
"""

import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
PAPERS_DIR = PROJECT_ROOT / "papers"


def migrate_paper(paper_dir: Path) -> bool:
    """将 summary.md 内容复制到 abstract.md"""
    summary_file = paper_dir / "summary.md"
    abstract_file = paper_dir / "abstract.md"

    if not summary_file.exists():
        print(f"  [SKIP] {paper_dir.name}: 无 summary.md")
        return False

    if not abstract_file.exists():
        print(f"  [SKIP] {paper_dir.name}: 无 abstract.md")
        return False

    # 读取 summary.md 内容
    with open(summary_file, 'r', encoding='utf-8') as f:
        summary_content = f.read()

    # 备份原 abstract.md
    backup_file = abstract_file.with_suffix('.md.bak')
    with open(abstract_file, 'r', encoding='utf-8') as f:
        original_content = f.read()
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(original_content)

    # 用 summary.md 内容替换 abstract.md
    with open(abstract_file, 'w', encoding='utf-8') as f:
        f.write(summary_content)

    print(f"  [OK] {paper_dir.name}")
    return True


def main():
    """扫描所有论文目录并执行迁移"""
    paper_dirs = []

    for year_dir in sorted(PAPERS_DIR.iterdir(), reverse=True):
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue
        for paper_dir in sorted(year_dir.iterdir()):
            if paper_dir.is_dir():
                paper_dirs.append(paper_dir)

    print(f"找到 {len(paper_dirs)} 个论文目录")

    success = 0
    skipped = 0
    for paper_dir in paper_dirs:
        if migrate_paper(paper_dir):
            success += 1
        else:
            skipped += 1

    print(f"\n迁移完成: {success} 成功, {skipped} 跳过")
    print("原 abstract.md 已备份为 .bak 文件")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""修复所有文件中的 arXiv 链接格式"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
PAPERS_DIR = PROJECT_ROOT / "papers"


def fix_arxiv_links_in_file(file_path):
    """修复单个文件中的 arXiv 链接"""
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  错误: 无法读取 {file_path}")
        return 0

    original = content

    # 1. 修复 arXiv ID 格式（如 2409_05369 -> 2409.05369）
    # 在 frontmatter 中
    content = re.sub(r'arXiv:\s*"(\d{2,4})_(\d{5})"', r'arXiv: "\1.\2"', content)
    # 在链接中 https://arxiv.org/abs/2409_05369 -> https://arxiv.org/abs/2409.05369
    content = re.sub(r'https://arxiv\.org/abs/(\d{2,4})_(\d{5})', r'https://arxiv.org/abs/\1.\2', content)

    # 2. 修复带版本号的格式（如 2409.05369v1 -> 2409.05369）
    content = re.sub(r'(\d{2,4}\.\d{5})v\d+', r'\1', content)

    if content != original:
        file_path.write_text(content, encoding='utf-8')
        return 1
    return 0


def main():
    fixed_count = 0
    file_count = 0

    for year_dir in sorted(PAPERS_DIR.iterdir(), reverse=True):
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue

        for paper_dir in sorted(year_dir.iterdir()):
            if not paper_dir.is_dir():
                continue

            # 处理 abstract.md
            abstract_file = paper_dir / "abstract.md"
            if abstract_file.exists():
                file_count += 1
                if fix_arxiv_links_in_file(abstract_file):
                    print(f"修复: {abstract_file.relative_to(PROJECT_ROOT)}")
                    fixed_count += 1

            # 处理 summary.md
            summary_file = paper_dir / "summary.md"
            if summary_file.exists():
                file_count += 1
                if fix_arxiv_links_in_file(summary_file):
                    print(f"修复: {summary_file.relative_to(PROJECT_ROOT)}")
                    fixed_count += 1

    print(f"\n完成: 检查了 {file_count} 个文件，修复了 {fixed_count} 个文件")


if __name__ == "__main__":
    main()
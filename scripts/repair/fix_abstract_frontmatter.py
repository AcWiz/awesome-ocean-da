# -*- coding: utf-8 -*-
"""修复 abstract.md 中的 frontmatter 格式问题"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent
PAPERS_DIR = PROJECT_ROOT / "papers"


def fix_frontmatter(content):
    """修复 frontmatter 中的常见格式问题"""
    original = content

    # 1. 修复 arXiv 字段的双引号问题：arXiv: "XXXXX.XXXXX"" -> arXiv: "XXXXX.XXXXX"
    content = re.sub(r'arXiv:\s*"([^"]+)"', r'arXiv: "\1"', content)

    # 2. 修复 authors 字段的单引号双引号混合问题
    # 3. 移除 venue 字段的多余引号
    content = re.sub(r'venue:\s*""([^"]+)""', r'venue: "\1"', content)

    # 4. 统一 arXiv ID 格式（移除 v1, v2 等版本号）
    # arXiv: "2404.08522v1" -> arXiv: "2404.08522"
    def clean_arxiv(match):
        arxiv_id = match.group(1)
        # 移除版本号 v1, v2 等
        arxiv_clean = re.sub(r'v\d+$', '', arxiv_id)
        return f'arXiv: "{arxiv_clean}"'

    content = re.sub(r'arXiv:\s*"([^"]+)"', clean_arxiv, content)

    return content


def process_file(file_path, dry_run=False):
    """处理单个文件"""
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"  错误: 无法读取 {file_path}")
        return False

    # 检查是否需要修复
    if '""' in content or re.search(r'arXiv:.*v\d+"', content):
        fixed = fix_frontmatter(content)
        if fixed != content and not dry_run:
            file_path.write_text(fixed, encoding='utf-8')
            return True
        elif fixed != content and dry_run:
            print(f"  [DRY-RUN] 会修复: {file_path.relative_to(PROJECT_ROOT)}")
            return True
    return False


def main():
    import argparse
    parser = argparse.ArgumentParser(description='修复 abstract.md 中的 frontmatter 格式')
    parser.add_argument('--dry-run', action='store_true', help='预览修改但不实际写入')
    args = parser.parse_args()

    fixed_count = 0
    total_count = 0

    for year_dir in sorted(PAPERS_DIR.iterdir(), reverse=True):
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue

        for paper_dir in sorted(year_dir.iterdir()):
            if not paper_dir.is_dir():
                continue

            abstract_file = paper_dir / "abstract.md"
            if not abstract_file.exists():
                continue

            total_count += 1
            if process_file(abstract_file, dry_run=args.dry_run):
                print(f"{'[DRY-RUN] ' if args.dry_run else ''}修复: {abstract_file.relative_to(PROJECT_ROOT)}")
                fixed_count += 1

    print(f"\n完成: 检查了 {total_count} 个文件，{'会' if args.dry_run else '已'}修复 {fixed_count} 个")

if __name__ == "__main__":
    main()

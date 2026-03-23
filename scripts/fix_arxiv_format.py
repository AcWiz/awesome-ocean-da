# -*- coding: utf-8 -*-
"""修复 abstract.md 中的 arXiv ID 格式（如下划线转点号）"""

import re
import argparse
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
PAPERS_DIR = PROJECT_ROOT / "papers"


def normalize_arxiv_id(arxiv_raw):
    """规范化 arXiv ID，修复下划线等常见错误格式"""
    if not arxiv_raw or arxiv_raw in ['待补充', 'XXXXX', 'Not available', '', 'Not Available']:
        return arxiv_raw

    # 替换下划线为点（常见错误格式如 2503_19160 -> 2503.19160）
    arxiv = arxiv_raw.replace('_', '.')

    # 移除版本号如 v1, v2 等
    arxiv_clean = re.sub(r'v\d+$', '', arxiv).strip('.')

    # 检查是否是有效的 arXiv ID 格式（YYMM.NNNNN 或 YYYY.NNNNN）
    if re.match(r'^\d{2}\.\d{4,5}$', arxiv_clean):
        return arxiv_clean
    if re.match(r'^\d{4}\.\d{4,5}$', arxiv_clean):
        return arxiv_clean

    return arxiv_raw


def fix_file(file_path, dry_run=False):
    """修复单个文件的 arXiv ID 格式"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 匹配 arXiv: "XXXX_XXXXX" 或 arXiv: 'XXXX_XXXXX' 格式
    # 也处理 arXiv: XXXX_XXXXX 无引号格式
    pattern = r'(arXiv:\s*["\']?)(\d{2,4}_\d{4,5})(\1|[v\d]*)'

    def replace_arxiv(match):
        prefix = match.group(1)
        arxiv_id = match.group(2)
        suffix = match.group(3) if match.group(3) else ''
        fixed_id = normalize_arxiv_id(arxiv_id)
        if fixed_id != arxiv_id:
            return f'arXiv: "{fixed_id}"'
        return match.group(0)

    content = re.sub(pattern, replace_arxiv, content)

    if content != original and not dry_run:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return content != original


def main():
    parser = argparse.ArgumentParser(description='修复 abstract.md 中的 arXiv ID 格式')
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
            if fix_file(abstract_file, dry_run=args.dry_run):
                print(f"{'[DRY-RUN] Would fix' if args.dry_run else 'Fixed'}: {abstract_file.relative_to(PROJECT_ROOT)}")
                fixed_count += 1

    print(f"\n完成: 检查了 {total_count} 个文件，{'会' if args.dry_run else '已'}修复 {fixed_count} 个")


if __name__ == "__main__":
    main()
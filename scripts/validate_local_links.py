# -*- coding: utf-8 -*-
"""验证本地链接的有效性"""

import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
PAPERS_DIR = PROJECT_ROOT / "papers"


def extract_local_links(content, base_path=None):
    """从 Markdown 内容中提取本地链接"""
    # 匹配 [text](./path/to/file.md) 或 [text](../path/to/file.md) 格式
    # 捕获括号内的完整路径
    pattern = r'\[([^\]]+)\]\(([^\)]+\.md)\)'
    matches = re.findall(pattern, content)
    links = []
    for text, path in matches:
        links.append((text, path))
    return links


def resolve_link(base_path, link_path):
    """解析相对链接为绝对路径"""
    if link_path.startswith('./'):
        # 相对于 base_path
        return base_path.parent / link_path[2:]
    elif link_path.startswith('../'):
        # 向上跳转
        parts = link_path[3:].split('/')
        result = base_path.parent.parent
        for part in parts:
            result = result / part
        return result
    elif link_path.startswith('/'):
        # 绝对路径相对于 PROJECT_ROOT
        return PROJECT_ROOT / link_path[1:]
    return base_path.parent / link_path


def validate_file(file_path):
    """验证单个文件中的本地链接"""
    if not file_path.exists():
        return []

    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        return [(str(file_path), None, str(e))]

    links = extract_local_links(content)
    errors = []

    for text, link_path in links:
        resolved = resolve_link(file_path, link_path)
        if not resolved.exists():
            errors.append((str(file_path.relative_to(PROJECT_ROOT)), f"[{text}]({link_path})", "文件不存在"))

    return errors


def main():
    print("验证本地链接...")

    all_errors = []

    # 检查主页 README.md
    readme = PROJECT_ROOT / "README.md"
    if readme.exists():
        errors = validate_file(readme)
        all_errors.extend(errors)

    # 检查所有标签页
    for md_file in PAPERS_DIR.glob("*.md"):
        errors = validate_file(md_file)
        all_errors.extend(errors)

    # 检查所有年份目录下的 index.md
    for year_dir in PAPERS_DIR.iterdir():
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue
        index_file = year_dir / "index.md"
        if index_file.exists():
            errors = validate_file(index_file)
            all_errors.extend(errors)

        # 检查每篇论文的 summary.md 链接
        for paper_dir in year_dir.iterdir():
            if not paper_dir.is_dir():
                continue
            # 摘要中可能引用其他论文的链接
            abstract = paper_dir / "abstract.md"
            if abstract.exists():
                errors = validate_file(abstract)
                all_errors.extend(errors)

    if all_errors:
        print(f"\n发现 {len(all_errors)} 个错误:")
        for file, link, error in all_errors:
            print(f"  [{error}] {file}: {link}")
        return 1
    else:
        print("\n所有本地链接验证通过!")
        return 0


if __name__ == "__main__":
    exit(main())
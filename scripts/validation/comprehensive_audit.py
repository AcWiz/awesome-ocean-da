# -*- coding: utf-8 -*-
"""
全面审核脚本 - 验证论文库的所有信息正确性
"""

import json
import re
import urllib.request
import urllib.error
import random
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

PROJECT_ROOT = Path(__file__).parent.parent.parent
PAPERS_DIR = PROJECT_ROOT / "papers"
DATA_DIR = PROJECT_ROOT / "_data"


def check_arxiv_link(arxiv_id, timeout=5):
    """验证 arXiv 链接是否可访问"""
    if not arxiv_id:
        return False, "Empty ID"

    url = f"https://arxiv.org/abs/{arxiv_id}"
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0')
        with urllib.request.urlopen(req, timeout=timeout) as response:
            if response.status == 200:
                return True, "OK"
            return False, f"HTTP {response.status}"
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False, "404 Not Found"
        return False, f"HTTP {e.code}"
    except Exception as e:
        return False, str(e)[:30]


def audit_arxiv_format():
    """审核 arXiv ID 格式"""
    print("\n=== 1. 审核 arXiv ID 格式 ===")

    with open(DATA_DIR / "papers.json") as f:
        data = json.load(f)

    papers = data.get('papers', [])
    issues = []

    for p in papers:
        arxiv = p.get('arxiv', '')
        path = p.get('path', '')

        # 检查是否有下划线
        if '_' in arxiv:
            issues.append(f"  {path}: '{arxiv}' 包含下划线")

        # 检查是否有版本号
        if re.search(r'v\d+$', arxiv):
            issues.append(f"  {path}: '{arxiv}' 包含版本号")

        # 检查格式是否正确
        if arxiv and not re.match(r'^\d{2,4}\.\d{4,5}$', arxiv):
            if not issues or issues[-1] != f"  {path}: '{arxiv}' 格式错误":
                issues.append(f"  {path}: '{arxiv}' 格式错误")

    if issues:
        print(f"  发现 {len(issues)} 个格式问题:")
        for issue in issues[:10]:
            print(issue)
        return False
    else:
        print("  ✓ 所有 arXiv ID 格式正确")
        return True


def audit_arxiv_links_accessibility():
    """审核 arXiv 链接可访问性（抽样验证）"""
    print("\n=== 2. 审核 arXiv 链接可访问性 ===")

    with open(DATA_DIR / "papers.json") as f:
        data = json.load(f)

    papers = data.get('papers', [])

    # 抽样 20 篇进行验证
    sample = random.sample(papers, min(20, len(papers)))

    issues = []
    for p in sample:
        arxiv = p.get('arxiv', '')
        if arxiv:
            valid, msg = check_arxiv_link(arxiv)
            if not valid:
                issues.append(f"  {p['path']}: {arxiv} - {msg}")

    if issues:
        print(f"  发现 {len(issues)} 个链接问题:")
        for issue in issues:
            print(issue)
        return False
    else:
        print(f"  ✓ 抽样 {len(sample)} 篇论文的 arXiv 链接全部可访问")
        return True


def audit_file_links():
    """审核文件中引用的链接"""
    print("\n=== 3. 审核文件中的 arXiv 链接 ===")

    issues = []
    wrong_format_count = 0

    for year_dir in PAPERS_DIR.iterdir():
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue

        for paper_dir in year_dir.iterdir():
            if not paper_dir.is_dir():
                continue

            for md_file in ['abstract.md', 'summary.md']:
                file_path = paper_dir / md_file
                if not file_path.exists():
                    continue

                content = file_path.read_text(encoding='utf-8')

                # 检查链接格式
                links = re.findall(r'https://arxiv\.org/abs/\d{2,4}[_\d]+\.?\d*', content)
                for link in links:
                    if '_' in link or re.search(r'\d_\d', link):
                        issues.append(f"  {file_path.relative_to(PROJECT_ROOT)}: {link}")
                        wrong_format_count += 1

    if issues:
        print(f"  发现 {wrong_format_count} 个文件中的错误链接格式")
        for issue in issues[:10]:
            print(issue)
        return False
    else:
        print("  ✓ 所有文件中的 arXiv 链接格式正确")
        return True


def audit_summary_files():
    """审核 summary.md 文件内容"""
    print("\n=== 4. 审核 summary.md 文件内容 ===")

    total = 0
    empty = 0
    placeholder = 0

    issues = []

    for year_dir in PAPERS_DIR.iterdir():
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue

        for paper_dir in year_dir.iterdir():
            if not paper_dir.is_dir():
                continue

            summary_file = paper_dir / "summary.md"
            if not summary_file.exists():
                continue

            total += 1
            content = summary_file.read_text(encoding='utf-8')

            # 检查是否为空或占位符
            if len(content) < 100:
                empty += 1
                issues.append(f"  {paper_dir.relative_to(PROJECT_ROOT)}: 内容过短 ({len(content)} 字符)")

            # 检查占位符文本
            placeholders = ['暂无论文内容', '需要原文内容补充', '作者信息待补充', 'No content available']
            for ph in placeholders:
                if ph in content:
                    placeholder += 1
                    issues.append(f"  {paper_dir.relative_to(PROJECT_ROOT)}: 包含占位符")
                    break

    print(f"  总 summary 文件: {total}")
    print(f"  内容过短: {empty}")
    print(f"  包含占位符: {placeholder}")

    if issues:
        for issue in issues[:5]:
            print(issue)
        return False
    else:
        print("  ✓ 所有 summary.md 内容正常")
        return True


def audit_papers_json():
    """审核 papers.json 完整性"""
    print("\n=== 5. 审核 papers.json 完整性 ===")

    with open(DATA_DIR / "papers.json") as f:
        data = json.load(f)

    papers = data.get('papers', [])
    issues = []

    for p in papers:
        path = p.get('path', '')

        # 检查核心字段
        if not p.get('title'):
            issues.append(f"  {path}: 缺少 title")
        if not p.get('arxiv'):
            issues.append(f"  {path}: 缺少 arXiv")
        if not p.get('year'):
            issues.append(f"  {path}: 缺少 year")

        # 检查 arXiv 格式
        arxiv = p.get('arxiv', '')
        if arxiv and not re.match(r'^\d{2,4}\.\d{4,5}$', arxiv):
            issues.append(f"  {path}: arXiv 格式错误 '{arxiv}'")

    if issues:
        print(f"  发现 {len(issues)} 个问题:")
        for issue in issues[:10]:
            print(issue)
        return False
    else:
        print(f"  ✓ papers.json 中 {len(papers)} 篇论文核心字段完整")
        return True


def audit_consistency():
    """审核一致性问题"""
    print("\n=== 6. 审核数据一致性 ===")

    with open(DATA_DIR / "papers.json") as f:
        data = json.load(f)

    papers = data.get('papers', [])
    paper_map = {p['path']: p for p in papers}

    issues = []
    checked = 0

    for year_dir in PAPERS_DIR.iterdir():
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue

        for paper_dir in year_dir.iterdir():
            if not paper_dir.is_dir():
                continue

            rel_path = str(paper_dir.relative_to(PROJECT_ROOT))

            if rel_path not in paper_map:
                continue

            checked += 1
            p = paper_map[rel_path]

            # 检查 abstract.md 中的 arXiv 是否与 JSON 一致
            abstract_file = paper_dir / "abstract.md"
            if abstract_file.exists():
                content = abstract_file.read_text(encoding='utf-8')

                # 提取 frontmatter 中的 arXiv
                match = re.search(r'arXiv:\s*"([^"]+)"', content)
                if match:
                    file_arxiv = match.group(1)
                    json_arxiv = p.get('arxiv', '')

                    # 规范化比较
                    if file_arxiv.replace('_', '.') != json_arxiv.replace('_', '.'):
                        issues.append(f"  {rel_path}: frontmatter '{file_arxiv}' vs JSON '{json_arxiv}'")

    if issues:
        print(f"  发现 {len(issues)} 个一致性问题:")
        for issue in issues[:10]:
            print(issue)
        return False
    else:
        print(f"  ✓ 检查了 {checked} 篇论文，一致性正确")
        return True


def main():
    print("=" * 60)
    print("论文库全面审核")
    print("=" * 60)

    results = []

    results.append(("arXiv 格式", audit_arxiv_format()))
    results.append(("arXiv 可访问性", audit_arxiv_links_accessibility()))
    results.append(("文件链接格式", audit_file_links()))
    results.append(("Summary 内容", audit_summary_files()))
    results.append(("Papers JSON", audit_papers_json()))
    results.append(("数据一致性", audit_consistency()))

    print("\n" + "=" * 60)
    print("审核结果汇总")
    print("=" * 60)

    passed = sum(1 for _, r in results if r)
    total = len(results)

    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"  [{status}] {name}")

    print(f"\n通过: {passed}/{total}")

    if passed == total:
        print("\n✓ 所有审核通过！")
        return 0
    else:
        print("\n✗ 存在需要修复的问题")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())

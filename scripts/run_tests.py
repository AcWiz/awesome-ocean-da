# -*- coding: utf-8 -*-
"""
测试方案 - 验证论文库的完整性和正确性

运行方式:
    python scripts/run_tests.py           # 运行所有测试
    python scripts/run_tests.py --verbose # 详细输出
    python scripts/run_tests.py -t T1    # 只运行 T1 测试
"""

import json
import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict

PROJECT_ROOT = Path(__file__).parent.parent
PAPERS_DIR = PROJECT_ROOT / "papers"
DATA_DIR = PROJECT_ROOT / "_data"


class TestRunner:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.results = []
        self.passed = 0
        self.failed = 0

    def log(self, msg):
        if self.verbose:
            print(msg)

    def test(self, name, condition, error_msg=""):
        """执行单个测试"""
        result = {"name": name, "passed": condition, "error": error_msg}
        self.results.append(result)
        if condition:
            self.passed += 1
            status = "✓ PASS"
        else:
            self.failed += 1
            status = "✗ FAIL"

        print(f"  [{status}] {name}")
        if not condition and error_msg:
            print(f"         {error_msg}")
        return condition


def T1_arxiv_format_validation(runner):
    """T1: arXiv ID 格式验证"""
    print("\n=== T1: arXiv ID 格式验证 ===")

    with open(DATA_DIR / "papers.json") as f:
        data = json.load(f)

    papers = data.get('papers', [])
    invalid_count = 0
    invalid_examples = []

    for p in papers:
        arxiv = p.get('arxiv', '')
        # 检查格式：YYMM.NNNNN 或 YYYY.NNNNN
        if arxiv and not re.match(r'^\d{2,4}\.\d{4,5}$', arxiv):
            invalid_count += 1
            if len(invalid_examples) < 3:
                invalid_examples.append(f"  - {p['path']}: '{arxiv}'")

    runner.test(
        "所有论文arXiv ID格式正确",
        invalid_count == 0,
        f"{invalid_count} 篇论文格式错误\n" + "\n".join(invalid_examples)
    )

    # 检查无占位符
    placeholder_count = 0
    placeholders = []
    for p in papers:
        arxiv = p.get('arxiv', '')
        if arxiv in ['XXXXX', '待补充', 'Not Available', 'Not available', '', '暂无']:
            placeholder_count += 1
            if len(placeholders) < 3:
                placeholders.append(f"  - {p['path']}: '{arxiv}'")

    runner.test(
        "无占位符arXiv ID",
        placeholder_count == 0,
        f"{placeholder_count} 篇使用占位符\n" + "\n".join(placeholders)
    )

    return invalid_count == 0 and placeholder_count == 0


def T2_papers_json_integrity(runner):
    """T2: papers.json 完整性验证"""
    print("\n=== T2: papers.json 完整性验证 ===")

    with open(DATA_DIR / "papers.json") as f:
        data = json.load(f)

    papers = data.get('papers', [])

    runner.test(
        "papers.json 存在且可读",
        len(papers) > 0,
        f"论文数量: {len(papers)}"
    )

    # 检查必需字段（title, arxiv, year 是必须的，tags 可以为空列表）
    required_fields = ['path', 'year', 'title', 'arxiv']
    missing_field_count = 0
    for p in papers:
        for field in required_fields:
            if field not in p or not p[field]:
                missing_field_count += 1
                break

    runner.test(
        "所有论文包含核心字段",
        missing_field_count == 0,
        f"{missing_field_count} 篇论文缺少核心字段"
    )

    # 检查论文总数
    runner.test(
        "论文总数 >= 100",
        len(papers) >= 100,
        f"论文总数: {len(papers)}"
    )

    return len(papers) > 0 and missing_field_count == 0


def T3_arxiv_links_validity(runner):
    """T3: arXiv 链接有效性验证"""
    print("\n=== T3: arXiv 链接有效性验证 ===")

    import urllib.request
    import urllib.error

    with open(DATA_DIR / "papers.json") as f:
        data = json.load(f)

    papers = data.get('papers', [])

    # 抽样验证（前 10 篇）
    sample_size = min(10, len(papers))
    checked = 0
    failed = 0

    for p in papers[:sample_size]:
        arxiv = p.get('arxiv', '')
        if not arxiv:
            continue

        url = f"https://arxiv.org/abs/{arxiv}"
        try:
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0')
            with urllib.request.urlopen(req, timeout=10) as response:
                checked += 1
                if response.status != 200:
                    failed += 1
                    runner.log(f"  {arxiv}: HTTP {response.status}")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                failed += 1
                runner.log(f"  {arxiv}: 404 Not Found")
        except Exception as e:
            runner.log(f"  {arxiv}: {e}")

    runner.test(
        f"抽样 {checked} 篇arXiv链接可访问",
        failed == 0,
        f"{failed} 篇链接无效"
    )

    return failed == 0


def T4_tag_pages_format(runner):
    """T4: 标签页格式验证"""
    print("\n=== T4: 标签页格式验证 ===")

    tag_files = list(PAPERS_DIR.glob("*.md"))
    # 排除 README.md 和分类索引页（这些页面格式不同）
    tag_files = [f for f in tag_files if f.name not in ['README.md', 'CONTRIBUTING.md', 'by-method.md', 'by-application.md']]

    runner.test(
        "标签页数量 >= 5",
        len(tag_files) >= 5,
        f"找到 {len(tag_files)} 个标签页"
    )

    # 验证表头格式
    expected_header = "| 年份 | 论文 | arXiv | Venue | 方法标签 | 应用 | 总结 |"
    format_errors = []

    for tag_file in tag_files:
        content = tag_file.read_text(encoding='utf-8')
        if expected_header not in content:
            format_errors.append(f"  - {tag_file.name}: 表头格式不正确")

    runner.test(
        "所有标签页表头格式一致",
        len(format_errors) == 0,
        "\n".join(format_errors) if format_errors else ""
    )

    # 验证总结链接格式
    summary_link_pattern = re.compile(r'\[总结\]\(\./\d+/\d+\.\d+/summary\.md\)')
    link_errors = []

    for tag_file in tag_files:
        content = tag_file.read_text(encoding='utf-8')
        links = summary_link_pattern.findall(content)
        # 验证链接指向存在文件
        for link_match in re.finditer(summary_link_pattern, content):
            link = link_match.group(0)
            # 提取路径
            path_match = re.search(r'\./(\d+/\d+\.\d+/summary\.md)', link)
            if path_match:
                folder_path = PAPERS_DIR / path_match.group(1)
                if not folder_path.exists():
                    link_errors.append(f"  - {tag_file.name}: {link} 指向不存在")

    runner.test(
        "标签页总结链接指向存在文件",
        len(link_errors) == 0,
        "\n".join(link_errors[:5]) if link_errors else ""
    )

    return len(tag_files) >= 5 and len(format_errors) == 0 and len(link_errors) == 0


def T5_tag_pages_completeness(runner):
    """T5: 标签页论文完整性验证"""
    print("\n=== T5: 标签页论文完整性验证 ===")

    with open(DATA_DIR / "papers.json") as f:
        data = json.load(f)

    papers = data.get('papers', [])

    # 按标签统计论文数
    tag_counts = defaultdict(int)
    for p in papers:
        for tag in p.get('method_tags', []) + p.get('application_tags', []):
            tag_counts[tag.lower().replace('_', '-')] += 1

    # 检查主要标签（包括别名映射）
    main_tags_check = [
        ('pinn', ['pinn', 'physics-informed', 'physics-informed-neural-networks']),
        ('koopman', ['koopman', 'koopman-operator']),
        ('neural-operator', ['neural-operator', 'fno', 'fourier-neural-operator']),
        ('gnn', ['gnn', 'graph-neural-network']),
        ('sst', ['sst', 'sea-surface-temperature']),
        ('enso', ['enso']),
    ]

    missing_tags = []
    for main_tag, aliases in main_tags_check:
        found = any(tag_counts.get(a, 0) > 0 for a in aliases)
        if not found:
            missing_tags.append(main_tag)

    runner.test(
        "主要标签都有对应论文",
        len(missing_tags) == 0,
        f"缺失标签: {missing_tags}" if missing_tags else ""
    )

    # 验证标签页论文数 >= 1（基本完整性检查）
    tag_pages = ['pinn.md', 'koopman.md', 'gnn.md', 'neural-operator.md', 'sst.md', 'enso.md']

    empty_pages = []
    for filename in tag_pages:
        filepath = PAPERS_DIR / filename
        if filepath.exists():
            content = filepath.read_text(encoding='utf-8')
            # 统计论文行数（排除表头和分隔符）
            paper_rows = len([l for l in content.split('\n') if l.startswith('| 20')])
            if paper_rows == 0:
                empty_pages.append(filename)

    runner.test(
        "主要标签页都有论文",
        len(empty_pages) == 0,
        f"空标签页: {empty_pages}" if empty_pages else ""
    )

    return len(missing_tags) == 0 and len(empty_pages) == 0


def T6_year_pages_validity(runner):
    """T6: 年份页面有效性验证"""
    print("\n=== T6: 年份页面有效性验证 ===")

    year_dirs = [d for d in PAPERS_DIR.iterdir() if d.is_dir() and d.name.isdigit()]

    runner.test(
        "年份目录数量 >= 5",
        len(year_dirs) >= 5,
        f"找到 {len(year_dirs)} 个年份目录"
    )

    # 检查每个年份目录都有 index.md
    missing_index = []
    for year_dir in year_dirs:
        index_file = year_dir / "index.md"
        if not index_file.exists():
            missing_index.append(f"  - {year_dir.name}/index.md 不存在")

    runner.test(
        "所有年份目录都有 index.md",
        len(missing_index) == 0,
        "\n".join(missing_index) if missing_index else ""
    )

    # 验证 index.md 格式
    with open(DATA_DIR / "papers.json") as f:
        data = json.load(f)
    papers_by_year = defaultdict(list)
    for p in data.get('papers', []):
        papers_by_year[p['year']].append(p)

    format_errors = []
    for year_dir in year_dirs:
        year = int(year_dir.name)
        index_file = year_dir / "index.md"
        if index_file.exists():
            content = index_file.read_text(encoding='utf-8')
            # 统计论文行数
            paper_rows = len([l for l in content.split('\n') if l.startswith('| 20')])
            expected = len(papers_by_year.get(year, []))
            if paper_rows != expected:
                format_errors.append(f"  - {year}: 显示{paper_rows}篇, 期望{expected}篇")

    runner.test(
        "年份页论文数与实际匹配",
        len(format_errors) == 0,
        "\n".join(format_errors) if format_errors else ""
    )

    return len(year_dirs) >= 5 and len(missing_index) == 0 and len(format_errors) == 0


def T7_readme_validity(runner):
    """T7: README 有效性验证"""
    print("\n=== T7: README 有效性验证 ===")

    readme = PROJECT_ROOT / "README.md"

    runner.test(
        "README.md 存在",
        readme.exists(),
        ""
    )

    if not readme.exists():
        return False

    content = readme.read_text(encoding='utf-8')

    # 检查无占位符
    has_placeholder = 'XXXXX' in content or '待补充' in content
    runner.test(
        "README 无占位符",
        not has_placeholder,
        "发现占位符文本"
    )

    # 检查无直接指向年份文件夹的链接（不带文件名）
    # 正确: ./papers/2026/index.md, ./papers/2025/2510.17756/summary.md
    # 错误: ./papers/2026/ (直接指向年份文件夹，无文件名)
    # 匹配 ./papers/YEAR/ 后面不跟任何有效文件路径的
    year_folder_links = re.findall(r'\./papers/\d{4}/(?![0-9a-zA-Z])', content)
    runner.test(
        "README 无直接指向年份文件夹的链接（需跟文件名）",
        len(year_folder_links) == 0,
        f"发现 {len(year_folder_links)} 处无效年份文件夹链接"
    )

    # 验证"更多"链接存在
    more_links = re.findall(r'\[更多 .+? 论文 →\]\(\./papers/\w+\.md\)', content)
    runner.test(
        "README 包含'更多'链接",
        len(more_links) >= 5,
        f"找到 {len(more_links)} 个'更多'链接"
    )

    # 验证 arXiv 链接格式（在论文标题链接中）
    arxiv_links = re.findall(r'\[.+\]\(https://arxiv\.org/abs/\d{2,4}\.\d{4,5}\)', content)
    all_valid = all(re.match(r'\[.+\]\(https://arxiv\.org/abs/\d{2,4}\.\d{4,5}\)$', l) for l in arxiv_links)
    runner.test(
        "README 论文链接到arXiv正确",
        all_valid and len(arxiv_links) > 0,
        f"找到 {len(arxiv_links)} 个论文arXiv链接"
    )

    return not has_placeholder and len(year_folder_links) == 0 and len(more_links) >= 5


def T8_local_links_validation(runner):
    """T8: 本地链接完整性验证"""
    print("\n=== T8: 本地链接完整性验证 ===")

    # 验证 summary.md 文件存在性
    all_papers_have_summary = True
    missing_summaries = []

    for year_dir in PAPERS_DIR.iterdir():
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue
        for paper_dir in year_dir.iterdir():
            if not paper_dir.is_dir():
                continue
            summary_file = paper_dir / "summary.md"
            if not summary_file.exists():
                all_papers_have_summary = False
                if len(missing_summaries) < 5:
                    missing_summaries.append(f"  - {paper_dir.relative_to(PAPERS_DIR)}/summary.md 不存在")

    runner.test(
        "所有论文目录都有 summary.md",
        all_papers_have_summary,
        "\n".join(missing_summaries) if missing_summaries else f"共 {len(missing_summaries)} 篇缺失"
    )

    # 验证 abstract.md 存在
    all_papers_have_abstract = True
    missing_abstracts = []

    for year_dir in PAPERS_DIR.iterdir():
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue
        for paper_dir in year_dir.iterdir():
            if not paper_dir.is_dir():
                continue
            abstract_file = paper_dir / "abstract.md"
            if not abstract_file.exists():
                all_papers_have_abstract = False
                if len(missing_abstracts) < 5:
                    missing_abstracts.append(f"  - {paper_dir.relative_to(PAPERS_DIR)}/abstract.md 不存在")

    runner.test(
        "所有论文目录都有 abstract.md",
        all_papers_have_abstract,
        "\n".join(missing_abstracts) if missing_abstracts else f"共 {len(missing_abstracts)} 篇缺失"
    )

    return all_papers_have_summary and all_papers_have_abstract


def main():
    parser = argparse.ArgumentParser(description='论文库测试方案')
    parser.add_argument('--verbose', '-v', action='store_true', help='详细输出')
    parser.add_argument('-t', '--test', dest='test', help='只运行指定测试 (如 T1, T2)')
    args = parser.parse_args()

    runner = TestRunner(verbose=args.verbose)

    tests = [
        ("T1", T1_arxiv_format_validation),
        ("T2", T2_papers_json_integrity),
        ("T3", T3_arxiv_links_validity),
        ("T4", T4_tag_pages_format),
        ("T5", T5_tag_pages_completeness),
        ("T6", T6_year_pages_validity),
        ("T7", T7_readme_validity),
        ("T8", T8_local_links_validation),
    ]

    print("=" * 60)
    print("AI+海洋数据同化论文库 - 测试方案")
    print("=" * 60)

    if args.test:
        # 运行指定测试
        test_map = {t[0]: t[1] for t in tests}
        if args.test in test_map:
            test_map[args.test](runner)
        else:
            print(f"未知测试: {args.test}")
            print(f"可用测试: {', '.join(t[0] for t in tests)}")
            return 1
    else:
        # 运行所有测试
        for test_id, test_func in tests:
            test_func(runner)

    # 打印汇总
    print("\n" + "=" * 60)
    print(f"测试结果: {runner.passed} 通过, {runner.failed} 失败")
    print("=" * 60)

    return 0 if runner.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
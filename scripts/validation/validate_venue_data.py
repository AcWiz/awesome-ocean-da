# -*- coding: utf-8 -*-
"""验证 Venue 数据质量并生成报告

功能:
1. 扫描 papers.json，分析 venue 分布
2. 标记需要处理的论文:
   - PROPER: 有正式发表场所
   - TO_UPDATE: 仅 arXiv/预印本，可能有正式 venue
   - VAGUE: 模糊值需人工处理
3. 生成统计报告
"""

import json
from pathlib import Path
from collections import defaultdict

PROJECT_ROOT = Path(__file__).parent.parent.parent
PAPERS_DIR = PROJECT_ROOT / "papers"
DATA_FILE = PROJECT_ROOT / "_data" / "papers.json"


def classify_venue(venue):
    """分类 venue 类型

    Returns:
        'PROPER': 正式发表场所
        'TO_UPDATE': 仅 arXiv/预印本，需要查询
        'VAGUE': 模糊值，需人工处理
    """
    if not venue:
        return 'TO_UPDATE'

    venue_lower = venue.lower()

    # 明确是 arXiv 变体
    if venue in {'arXiv', 'arXiv preprint', 'arXiv preprint (stat.ME)'}:
        return 'TO_UPDATE'

    # N/A 占位符
    if venue == 'N/A - Preprint':
        return 'VAGUE'

    # 正式 venue 特征: 包含期刊名、会议名等
    proper_indicators = [
        'nature', 'science', 'cell', 'pnas', 'geophysical',
        'journal', 'transactions', 'letters', 'proceedings',
        'icml', 'neurips', 'iclr', 'aaai', 'ijcai', 'cvpr',
        'iccv', 'eccv', 'acl', 'emnlp', 'naacl', 'arxiv:',
        'ieee', 'acm', 'springer', 'wiley', 'elsevier',
        'monthly', 'quarterly', 'annual', 'review',
    ]

    for indicator in proper_indicators:
        if indicator in venue_lower:
            return 'PROPER'

    # 特定已知值
    if venue in {
        'CIKM', 'ICLR Workshop', 'ICLR 2026', 'ICLR 2021 Workshop on AI for Modeling Oceans and Climate Change',
        'Statistics and Computing', 'Technometrics', 'Physics of Fluids', 'Ocean Engineering',
        'IEEE Robotics and Automation Letters', 'IEEE Transactions on Signal Processing',
        'IEEE Transactions on Automatic Control / arXiv', 'Journal of Marine Systems',
        'Journal of Advances in Modeling Earth Systems (JAMES)', 'JGR', 'JGR: Machine Learning and Computation',
        'Monthly Weather Review'
    }:
        return 'PROPER'

    # 默认归类为需更新
    return 'TO_UPDATE'


def analyze_venue_distribution(papers):
    """分析 venue 分布"""
    stats = {
        'total': len(papers),
        'PROPER': [],
        'TO_UPDATE': [],
        'VAGUE': [],
    }

    venue_counts = defaultdict(int)
    year_counts = {}

    for paper in papers:
        venue = paper.get('venue', '')
        classification = classify_venue(venue)
        year = paper.get('year', 'unknown')

        stats[classification].append({
            'arxiv': paper.get('arxiv'),
            'title': paper.get('title', '')[:60],
            'venue': venue or '(empty)',
        })

        venue_counts[venue or '(empty)'] += 1

        if year not in year_counts:
            year_counts[year] = {'total': 0, 'proper': 0, 'to_update': 0, 'vague': 0, 'venues': defaultdict(int)}
        year_counts[year]['total'] += 1
        year_counts[year]['venues'][venue or '(empty)'] += 1
        if classification == 'PROPER':
            year_counts[year]['proper'] += 1
        elif classification == 'TO_UPDATE':
            year_counts[year]['to_update'] += 1
        else:
            year_counts[year]['vague'] += 1

    return stats, venue_counts, year_counts


def print_report(stats, venue_counts, year_counts):
    """打印验证报告"""
    print("=" * 70)
    print("Venue 数据验证报告")
    print("=" * 70)

    # 总体统计
    total = stats['total']
    proper_count = len(stats['PROPER'])
    to_update_count = len(stats['TO_UPDATE'])
    vague_count = len(stats['VAGUE'])

    print(f"\n📊 总体统计")
    print(f"  总论文数: {total}")
    print(f"  ✅ PROPER (正式 venue): {proper_count} ({100*proper_count/total:.1f}%)")
    print(f"  🔄 TO_UPDATE (需查询): {to_update_count} ({100*to_update_count/total:.1f}%)")
    print(f"  ⚠️  VAGUE (模糊值): {vague_count} ({100*vague_count/total:.1f}%)")

    proper_ratio = 100 * proper_count / total if total > 0 else 0
    target_ratio = 50.0

    print(f"\n📈 进度评估")
    if proper_ratio >= target_ratio:
        print(f"  🎉 PROPER 占比 {proper_ratio:.1f}% 已达到目标 {target_ratio}%!")
    else:
        print(f"  📍 PROPER 占比 {proper_ratio:.1f}%，目标 {target_ratio}%")
        print(f"  📝 需要将 {int((target_ratio * total - proper_count) / 100)} 篇更新为正式 venue")

    # 按年份分布
    print(f"\n📅 按年份分布")
    print(f"  {'年份':<8} {'总数':<6} {'PROPER':<8} {'TO_UPDATE':<12} {'VAGUE':<8}")
    print(f"  {'-'*45}")

    for year in sorted(year_counts.keys(), reverse=True):
        yc = year_counts[year]
        proper_pct = 100 * yc['proper'] / yc['total'] if yc['total'] > 0 else 0
        print(f"  {year:<8} {yc['total']:<6} {yc['proper']:<8} {yc['to_update']:<12} {yc['vague']:<8}")

    # Venue 分布详情
    print(f"\n📋 Venue 分布详情 (Top 20)")
    print(f"  {'Venue':<50} {'数量':<6}")
    print(f"  {'-'*58}")

    sorted_venues = sorted(venue_counts.items(), key=lambda x: -x[1])
    for venue, count in sorted_venues[:20]:
        classification = classify_venue(venue)
        indicator = {'PROPER': '✅', 'TO_UPDATE': '🔄', 'VAGUE': '⚠️'}[classification]
        print(f"  {indicator} {venue[:48]:<50} {count:<6}")

    # 需要处理的论文
    if stats['VAGUE']:
        print(f"\n⚠️  模糊值 (VAGUE) - 需要人工处理:")
        for paper in stats['VAGUE']:
            print(f"  - [{paper['arxiv']}] {paper['title']}... (venue: {paper['venue']})")

    if stats['TO_UPDATE']:
        print(f"\n🔄 需要查询 DOI 获取正式 venue (前 10 篇):")
        for paper in stats['TO_UPDATE'][:10]:
            print(f"  - [{paper['arxiv']}] {paper['title']}...")

        if len(stats['TO_UPDATE']) > 10:
            print(f"  ... 还有 {len(stats['TO_UPDATE']) - 10} 篇")

    print(f"\n" + "=" * 70)


def check_abstract_md_consistency(papers):
    """检查 abstract.md 与 papers.json 的 venue 一致性"""
    print(f"\n🔍 检查 abstract.md 与 papers.json 的一致性...")

    inconsistencies = []
    checked = 0

    for paper in papers:
        arxiv_id = paper.get('arxiv')
        json_venue = paper.get('venue', '')

        if not arxiv_id:
            continue

        # 查找 abstract.md
        found = False
        for year_dir in PAPERS_DIR.iterdir():
            if year_dir.is_dir() and year_dir.name.isdigit():
                abstract_file = year_dir / arxiv_id / "abstract.md"
                if abstract_file.exists():
                    found = True
                    checked += 1

                    content = abstract_file.read_text(encoding='utf-8')
                    # 简单提取 venue 行
                    import re
                    match = re.search(r'^venue:\s*"?([^"\n]+)"?', content, re.MULTILINE)
                    md_venue = match.group(1).strip() if match else ''

                    if md_venue != json_venue:
                        inconsistencies.append({
                            'arxiv': arxiv_id,
                            'json_venue': json_venue or '(empty)',
                            'md_venue': md_venue or '(empty)',
                        })
                    break

        if not found:
            inconsistencies.append({
                'arxiv': arxiv_id,
                'json_venue': json_venue or '(empty)',
                'md_venue': '(file not found)',
            })

    if inconsistencies:
        print(f"  ⚠️  发现 {len(inconsistencies)} 处不一致:")
        for inc in inconsistencies[:10]:
            print(f"    [{inc['arxiv']}] papers.json: {inc['json_venue']} | abstract.md: {inc['md_venue']}")
        if len(inconsistencies) > 10:
            print(f"    ... 还有 {len(inconsistencies) - 10} 处")
    else:
        print(f"  ✅ 所有 venue 一致 (检查了 {checked} 篇)")

    return len(inconsistencies)


def main():
    import argparse
    parser = argparse.ArgumentParser(description='验证 Venue 数据质量')
    parser.add_argument('--check-consistency', action='store_true', help='检查与 abstract.md 的一致性')
    args = parser.parse_args()

    # 读取 papers.json
    if not DATA_FILE.exists():
        print(f"[ERROR] 数据文件不存在: {DATA_FILE}")
        return

    data = json.loads(DATA_FILE.read_text(encoding='utf-8'))
    papers = data['papers']

    # 分析
    stats, venue_counts, year_counts = analyze_venue_distribution(papers)

    # 打印报告
    print_report(stats, venue_counts, year_counts)

    # 可选: 一致性检查
    if args.check_consistency:
        check_abstract_md_consistency(papers)

    # 验证标准检查
    print(f"\n📋 验证标准检查:")

    # 检查 1: 无 "N/A - Preprint"
    na_preprint = sum(1 for p in papers if p.get('venue') == 'N/A - Preprint')
    if na_preprint == 0:
        print(f"  ✅ 无 'N/A - Preprint' 占位符")
    else:
        print(f"  ⚠️  仍有 {na_preprint} 篇使用 'N/A - Preprint'")

    # 检查 2: arXiv 变体统一
    arxiv_variants = {'arXiv', 'arXiv preprint', 'arXiv preprint (stat.ME)'}
    variant_count = sum(1 for p in papers if p.get('venue') in arxiv_variants)
    if variant_count == 0:
        print(f"  ✅ arXiv 变体已统一 (无 'arXiv' 或 'arXiv preprint')")
    else:
        print(f"  ⚠️  仍有 {variant_count} 篇使用 arXiv 变体")

    # 检查 3: PROPER venue 占比
    proper_count = len(stats['PROPER'])
    proper_ratio = 100 * proper_count / len(papers) if papers else 0
    if proper_ratio > 50:
        print(f"  ✅ PROPER venue 占比 {proper_ratio:.1f}% > 50%")
    else:
        print(f"  ⚠️  PROPER venue 占比 {proper_ratio:.1f}% < 50%")

    print(f"\n" + "=" * 70)

if __name__ == "__main__":
    main()

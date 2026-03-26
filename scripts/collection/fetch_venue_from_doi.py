# -*- coding: utf-8 -*-
"""从 DOI 获取正式 venue 信息并更新论文元数据

流程:
1. 读取 papers.json 获取所有论文
2. 对每篇论文调用 arXiv API 获取 DOI
3. 用 DOI 调用 CrossRef API 获取 venue (container-title)
4. 更新 abstract.md 中的 venue 字段
5. 支持 --dry-run 预览模式
"""

import json
import re
import time
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent.parent
PAPERS_DIR = PROJECT_ROOT / "papers"
DATA_FILE = PROJECT_ROOT / "_data" / "papers.json"
STATE_FILE = PROJECT_ROOT / "_data" / "venue_fetch_state.json"

# API 限制
ARXIV_DELAY = 1.0  # 每秒 1 请求 (arXiv API)
CROSSREF_DELAY = 6.0  # 每分钟 10 次 = 每次 6 秒

# User-Agent for CrossRef API (必须提供)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; PaperVenueBot/1.0; mailto:research@example.com)"
}


def get_doi_from_arxiv(arxiv_id):
    """从 arXiv API 获取 DOI

    Args:
        arxiv_id: arXiv ID (如 "2404.05768")

    Returns:
        DOI 字符串或 None
    """
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=30) as response:
            if response.status == 200:
                content = response.read().decode('utf-8')
                # 解析 <arxiv:doi> 字段
                doi_match = re.search(r'<arxiv:doi>(.+?)</arxiv:doi>', content)
                if doi_match:
                    return doi_match.group(1).strip()
    except Exception as e:
        print(f"    [ERROR] arXiv API 错误: {e}")
    return None


def get_venue_from_crossref(doi):
    """从 CrossRef API 获取 venue (期刊名)

    Args:
        doi: DOI 字符串 (如 "10.1038/s41558-024-02052-5")

    Returns:
        venue 字符串或 None
    """
    # CrossRef URL encode DOI
    encoded_doi = urllib.parse.quote(doi, safe='')
    url = f"https://api.crossref.org/works/{encoded_doi}"

    try:
        req = urllib.request.Request(url)
        for key, value in HEADERS.items():
            req.add_header(key, value)

        with urllib.request.urlopen(req, timeout=30) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                message = data.get('message', {})

                # 优先使用 container-title (期刊全名)
                container_titles = message.get('container-title', [])
                if container_titles:
                    return container_titles[0]

                # 备用: title[0]
                titles = message.get('title', [])
                if titles:
                    return titles[0]
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"    [WARN] DOI 未在 CrossRef 找到: {doi}")
        else:
            print(f"    [ERROR] CrossRef HTTP 错误: {e.code}")
    except Exception as e:
        print(f"    [ERROR] CrossRef API 错误: {e}")

    return None


def parse_abstract_frontmatter(file_path):
    """解析 abstract.md 的 frontmatter

    Returns:
        (frontmatter dict, content start offset) 或 (None, None)
    """
    content = file_path.read_text(encoding='utf-8')

    # 查找 frontmatter 边界
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None, None

    frontmatter_text = match.group(1)
    lines = frontmatter_text.split('\n')
    frontmatter = {}

    for line in lines:
        if ':' in line:
            key, _, value = line.partition(':')
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if value:  # 忽略空值
                frontmatter[key] = value

    return frontmatter, match.end()


def update_venue_in_abstract(arxiv_id, new_venue, dry_run=True):
    """更新单篇论文的 venue

    Args:
        arxiv_id: arXiv ID
        new_venue: 新的 venue 值
        dry_run: 是否仅预览

    Returns:
        是否成功
    """
    # 查找论文目录
    paper_dir = None
    for year_dir in PAPERS_DIR.iterdir():
        if year_dir.is_dir() and year_dir.name.isdigit():
            for paper_subdir in year_dir.iterdir():
                if paper_subdir.is_dir() and paper_subdir.name == arxiv_id:
                    paper_dir = paper_subdir
                    break
            if paper_dir:
                break

    if not paper_dir:
        print(f"    [WARN] 未找到论文目录: {arxiv_id}")
        return False

    abstract_file = paper_dir / "abstract.md"
    if not abstract_file.exists():
        print(f"    [WARN] 未找到 abstract.md: {abstract_file}")
        return False

    content = abstract_file.read_text(encoding='utf-8')

    # 检查当前 venue
    frontmatter, offset = parse_abstract_frontmatter(abstract_file)
    if frontmatter and 'venue' in frontmatter:
        current_venue = frontmatter['venue']
        if current_venue == new_venue:
            print(f"    [SKIP] venue 已正确: {new_venue}")
            return False

    if dry_run:
        print(f"    [DRY-RUN] 更新 venue: {frontmatter.get('venue', 'N/A')} -> {new_venue}")
        return True

    # 执行更新
    # 替换 venue 行
    new_content = re.sub(
        r'^venue:.*$',
        f'venue: "{new_venue}"',
        content,
        flags=re.MULTILINE
    )

    # 如果没有 venue 行，在 source 行后添加
    if 'venue:' not in content and 'source:' in content:
        new_content = re.sub(
            r'^(source:.*)$',
            r'\1\nvenue: "{new_venue}"',
            content,
            flags=re.MULTILINE
        )

    abstract_file.write_text(new_content, encoding='utf-8')
    print(f"    [OK] 更新 venue: {new_venue}")
    return True


def process_paper(arxiv_id, dry_run=True):
    """处理单篇论文的 venue 更新

    Args:
        arxiv_id: arXiv ID
        dry_run: 是否仅预览

    Returns:
        (success, venue)
    """
    print(f"  处理 {arxiv_id}...")

    # Step 1: 获取 DOI
    doi = get_doi_from_arxiv(arxiv_id)
    if not doi:
        print(f"    [INFO] 无 DOI，使用 'arXiv'")
        return False, "arXiv"

    print(f"    [INFO] DOI: {doi}")
    time.sleep(ARXIV_DELAY)

    # Step 2: 获取 venue
    venue = get_venue_from_crossref(doi)
    if not venue:
        print(f"    [INFO] CrossRef 无 venue，使用 'arXiv'")
        time.sleep(CROSSREF_DELAY)
        return False, "arXiv"

    print(f"    [INFO] Venue: {venue}")
    time.sleep(CROSSREF_DELAY)

    # Step 3: 更新
    success = update_venue_in_abstract(arxiv_id, venue, dry_run=dry_run)
    return success, venue


def update_papers_json(arxiv_id, venue, dry_run=True):
    """更新 papers.json 中的 venue

    Args:
        arxiv_id: arXiv ID
        venue: 新的 venue
        dry_run: 是否仅预览

    Returns:
        是否成功
    """
    if not DATA_FILE.exists():
        return False

    data = json.loads(DATA_FILE.read_text(encoding='utf-8'))

    for paper in data['papers']:
        if paper.get('arxiv') == arxiv_id:
            if paper.get('venue') == venue:
                return False  # 无需更新

            if dry_run:
                print(f"    [DRY-RUN] 更新 papers.json: {paper.get('venue', 'N/A')} -> {venue}")
                return True

            paper['venue'] = venue
            DATA_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
            print(f"    [OK] 更新 papers.json venue: {venue}")
            return True

    return False


def load_processed_ids():
    """加载已处理的 arXiv ID 集合"""
    if not STATE_FILE.exists():
        return set()
    try:
        data = json.loads(STATE_FILE.read_text(encoding='utf-8'))
        return set(data.get('processed_ids', []))
    except (json.JSONDecodeError, IOError):
        return set()


def save_processed_ids(processed_ids, remaining_count):
    """保存已处理的 arXiv ID 集合"""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    state = {
        'processed_ids': list(processed_ids),
        'last_run': datetime.now().isoformat(),
        'remaining': remaining_count
    }
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')


def get_papers_to_process(papers, processed_ids, skip_arxiv=False):
    """获取待处理的论文列表"""
    arxiv_venues = {'arXiv', 'arXiv preprint', 'N/A - Preprint', 'arXiv preprint (stat.ME)'}
    papers_to_process = []

    for paper in papers:
        arxiv_id = paper.get('arxiv')
        if not arxiv_id:
            continue
        if arxiv_id in processed_ids:
            continue
        venue = paper.get('venue', '')
        if venue in arxiv_venues:
            papers_to_process.append(paper)
        elif skip_arxiv and venue not in {'arXiv', 'arXiv preprint', 'N/A - Preprint'}:
            pass
    return papers_to_process


def run_loop_mode(args, papers, processed_ids):
    """循环模式：持续处理直到所有论文完成"""
    print("=" * 60)
    print(f"Venue 更新工具 - 循环模式")
    print("=" * 60)
    print(f"总论文数: {len(papers)}")
    print(f"初始待处理: {len(papers) - len(processed_ids)}")
    print(f"批次大小: {args.limit if args.limit > 0 else '全部'}")
    print(f"间隔时间: {args.interval} 秒")
    if args.max_iterations > 0:
        print(f"最大迭代: {args.max_iterations}")
    print("=" * 60)
    print()

    iteration = 0
    total_success = 0
    total_arxiv_fallback = 0

    while True:
        iteration += 1
        papers_to_process = get_papers_to_process(papers, processed_ids, args.skip_arxiv)

        if not papers_to_process:
            print(f"\n🎉 所有论文处理完毕!")
            break

        print(f"\n--- 迭代 {iteration} (剩余 {len(papers_to_process)} 篇) ---")

        # 处理当前批次
        batch_size = args.limit if args.limit > 0 else len(papers_to_process)
        batch = papers_to_process[:batch_size]

        batch_success = 0
        batch_arxiv = 0

        for paper in batch:
            arxiv_id = paper.get('arxiv')
            if not arxiv_id:
                continue

            success, venue = process_paper(arxiv_id, dry_run=args.dry_run)
            update_papers_json(arxiv_id, venue, dry_run=args.dry_run)

            processed_ids.add(arxiv_id)

            if success:
                batch_success += 1
                total_success += 1
            if venue == "arXiv":
                batch_arxiv += 1
                total_arxiv_fallback += 1

        # 保存进度
        save_processed_ids(processed_ids, len(papers_to_process) - batch_size)

        print(f"  本批成功: {batch_success}, arXiv降级: {batch_arxiv}")
        print(f"  总进度: 已处理 {len(processed_ids)}/{len(papers)}")

        # 检查最大迭代
        if args.max_iterations > 0 and iteration >= args.max_iterations:
            print(f"\n⏹ 达到最大迭代次数 {args.max_iterations}")
            break

        # 继续等待下一批次
        if len(papers_to_process) > batch_size:
            print(f"  等待 {args.interval} 秒后继续...")
            time.sleep(args.interval)

    print()
    print("=" * 60)
    print(f"循环模式完成")
    print(f"总成功: {total_success}, arXiv降级: {total_arxiv_fallback}")
    print("=" * 60)


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='从 DOI 获取正式 venue 并更新论文元数据',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  python scripts/collection/fetch_venue_from_doi.py --dry-run
  python scripts/collection/fetch_venue_from_doi.py
  python scripts/collection/fetch_venue_from_doi.py --limit 5 --dry-run
  python scripts/collection/fetch_venue_from_doi.py --loop
  python scripts/collection/fetch_venue_from_doi.py --loop --limit 20 --interval 30
        '''
    )
    parser.add_argument('--dry-run', action='store_true', help='仅显示不更新')
    parser.add_argument('--limit', type=int, default=0, help='限制处理数量 (0=全部)')
    parser.add_argument('--skip-arxiv', action='store_true', help='跳过已有正式 venue 的论文')
    parser.add_argument('--loop', action='store_true', help='循环模式：持续查询直到所有论文处理完毕')
    parser.add_argument('--interval', type=int, default=60, help='批次间间隔秒数 (默认 60)')
    parser.add_argument('--max-iterations', type=int, default=0, help='最大迭代次数 (0=无限)')

    args = parser.parse_args()

    # 读取 papers.json
    if not DATA_FILE.exists():
        print(f"[ERROR] 数据文件不存在: {DATA_FILE}")
        return

    data = json.loads(DATA_FILE.read_text(encoding='utf-8'))
    papers = data['papers']

    # 循环模式
    if args.loop:
        processed_ids = load_processed_ids()
        run_loop_mode(args, papers, processed_ids)
        return

    # 普通模式
    print("=" * 60)
    print(f"Venue 更新工具")
    print("=" * 60)
    print(f"总论文数: {len(papers)}")
    print(f"模式: {'DRY-RUN (仅预览)' if args.dry_run else 'LIVE (执行更新)'}")
    if args.limit > 0:
        print(f"限制数量: {args.limit}")
    print("=" * 60)

    # 筛选需要处理的论文
    # 目标: venue 是 arXiv 变体或 N/A - Preprint
    arxiv_venues = {'arXiv', 'arXiv preprint', 'N/A - Preprint', 'arXiv preprint (stat.ME)'}
    papers_to_process = []

    for paper in papers:
        venue = paper.get('venue', '')
        if venue in arxiv_venues:
            papers_to_process.append(paper)
        elif args.skip_arxiv and venue not in {'arXiv', 'arXiv preprint', 'N/A - Preprint'}:
            # 已有正式 venue，跳过
            pass

    print(f"需要处理的论文: {len(papers_to_process)}")
    print()

    # 按年份分组
    by_year = {}
    for paper in papers_to_process:
        year = paper.get('year', 'unknown')
        if year not in by_year:
            by_year[year] = []
        by_year[year].append(paper)

    processed_count = 0

    for year in sorted(by_year.keys()):
        papers_in_year = by_year[year]
        print(f"[{year}] {len(papers_in_year)} 篇")

        for paper in papers_in_year:
            arxiv_id = paper.get('arxiv')
            if not arxiv_id:
                continue

            success, venue = process_paper(arxiv_id, dry_run=args.dry_run)
            update_papers_json(arxiv_id, venue, dry_run=args.dry_run)

            processed_count += 1
            if args.limit > 0 and processed_count >= args.limit:
                break

        if args.limit > 0 and processed_count >= args.limit:
            break

    print()
    print("=" * 60)
    print(f"完成")
    print("=" * 60)

if __name__ == "__main__":
    main()

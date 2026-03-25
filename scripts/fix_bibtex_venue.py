# -*- coding: utf-8 -*-
"""修复 BibTeX 中错误的 journal 字段

问题类型:
1. journal={arXiv preprint arXiv:XXXX} -> journal={arXiv preprint}
2. journal={Nature}/journal={Science} (未验证是否真正发表) -> 通过 DOI 验证

流程:
1. 扫描所有 abstract.md 和 summary.md 文件
2. 检测并修复错误的 journal 字段
3. 同步更新 papers.json 中的 venue
"""

import json
import re
import time
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
PAPERS_DIR = PROJECT_ROOT / "papers"
DATA_FILE = PROJECT_ROOT / "_data" / "papers.json"

# API 限制
ARXIV_DELAY = 1.0
CROSSREF_DELAY = 6.0

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; BibtexFixBot/1.0; mailto:research@example.com)"
}


def get_doi_from_arxiv(arxiv_id):
    """从 arXiv API 获取 DOI"""
    url = f"http://export.arxiv.org/api/query?id_list={arxiv_id}"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=30) as response:
            if response.status == 200:
                content = response.read().decode('utf-8')
                doi_match = re.search(r'<arxiv:doi>(.+?)</arxiv:doi>', content)
                if doi_match:
                    return doi_match.group(1).strip()
    except Exception as e:
        print(f"    [WARN] arXiv API 错误: {e}")
    return None


def get_venue_from_crossref(doi):
    """从 CrossRef API 获取 venue"""
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
                container_titles = message.get('container-title', [])
                if container_titles:
                    return container_titles[0]
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"    [WARN] DOI 未在 CrossRef 找到")
        else:
            print(f"    [WARN] CrossRef HTTP 错误: {e.code}")
    except Exception as e:
        print(f"    [WARN] CrossRef API 错误: {e}")
    return None


def is_preprint_with_doi(arxiv_id):
    """检查论文是否确实发表了（通过 DOI）

    Returns:
        'published': 确实发表了
        'preprint': 仅是预印本
        'unknown': 无法确定
    """
    doi = get_doi_from_arxiv(arxiv_id)
    time.sleep(ARXIV_DELAY)

    if not doi:
        return 'preprint', None

    venue = get_venue_from_crossref(doi)
    time.sleep(CROSSREF_DELAY)

    if venue:
        return 'published', venue
    return 'preprint', None


def fix_bibtex_in_file(file_path, verbose=False):
    """修复单个文件中的 BibTeX journal 字段

    Returns:
        (changed: bool, messages: list)
    """
    if not file_path.exists():
        return False, []

    content = file_path.read_text(encoding='utf-8')
    original_content = content
    messages = []

    # 模式1: journal={arXiv preprint arXiv:XXXX} -> journal={arXiv preprint}
    pattern_arxiv_preprint = re.compile(
        r'journal=\{arXiv preprint arXiv:(\d+\.\d+)\}',
        re.IGNORECASE
    )
    matches = pattern_arxiv_preprint.findall(content)
    if matches:
        for arxiv_id in matches:
            messages.append(f"修复错误格式 'journal={{arXiv preprint arXiv:{arxiv_id}}}'' -> 'journal={{arXiv preprint}}'")
        content = pattern_arxiv_preprint.sub('journal={arXiv preprint}', content)

    # 模式2: journal={Nature} 或 journal={Science} 等未验证的顶级期刊
    # 这些需要通过 DOI 验证
    top_journals = {
        'Nature': 'Nature',
        'Science': 'Science',
        'Cell': 'Cell',
        'Nature Communications': 'Nature Communications',
        'Nature Climate Change': 'Nature Climate Change',
        'Nature Geoscience': 'Nature Geoscience',
        'Nature Machine Intelligence': 'Nature Machine Intelligence',
        'Science Advances': 'Science Advances',
        'PNAS': 'PNAS',
    }

    # 提取 BibTeX 条目中的 journal 值
    # 匹配 @article{... journal={Nature} ...} 格式
    for journal_name, canonical_name in top_journals.items():
        # 查找包含 journal={Nature} 等的 BibTeX 条目
        escaped_journal = re.escape(journal_name)
        pattern = re.compile(
            r'(@\w+\{[^}]*)(journal=\{' + escaped_journal + r'\})',
            re.IGNORECASE | re.DOTALL
        )

        def fix_journal(match):
            entry_start = match.group(1)
            # 提取 arXiv ID (在 eprint 字段中)
            eprint_match = re.search(r'eprint=\{(\d+\.\d+)\}', entry_start)
            if eprint_match:
                arxiv_id = eprint_match.group(1)
                return match.group(1) + 'journal={arXiv preprint}'
            return match.group(0)

        new_content = pattern.sub(fix_journal, content)
        if new_content != content:
            messages.append(f"修复 journal={{{journal_name}}} (需要DOI验证)")
            content = new_content

    if content != original_content:
        if verbose:
            for msg in messages:
                print(f"  {msg}")
        file_path.write_text(content, encoding='utf-8')
        return True, messages

    return False, []


def extract_arxiv_id_from_path(file_path):
    """从文件路径提取 arXiv ID"""
    # papers/2026/2601.01813/abstract.md -> 2601.01813
    parts = file_path.parts
    for part in parts:
        if '.' in part and part.isdigit():
            return part
        # 处理 2601.01813 格式
        if re.match(r'^\d{4}\.\d{5}$', part):
            return part
    return None


def update_papers_json(arxiv_id, new_venue, dry_run=True):
    """更新 papers.json 中的 venue"""
    if not DATA_FILE.exists():
        return False

    data = json.loads(DATA_FILE.read_text(encoding='utf-8'))

    for paper in data['papers']:
        if paper.get('arxiv') == arxiv_id:
            if paper.get('venue') == new_venue:
                return False

            if dry_run:
                print(f"    [DRY-RUN] 更新 papers.json: {paper.get('venue', 'N/A')} -> {new_venue}")
                return True

            paper['venue'] = new_venue
            DATA_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
            print(f"    [OK] 更新 papers.json venue: {new_venue}")
            return True

    return False


def process_file(file_path, dry_run=True, verify_doi=True, verbose=False):
    """处理单个文件

    Returns:
        (changed: bool, messages: list)
    """
    if not file_path.exists():
        return False, []

    arxiv_id = extract_arxiv_id_from_path(file_path)
    content = file_path.read_text(encoding='utf-8')
    original_content = content
    messages = []

    # 模式1a: journal={arXiv preprint arXiv:XXXX} (包括占位符 XXXXX.XXXXX)
    pattern_arxiv_preprint1 = re.compile(
        r'journal=\{arXiv preprint arXiv:[A-Za-z0-9.]+\}',
        re.IGNORECASE
    )
    if pattern_arxiv_preprint1.search(content):
        content = pattern_arxiv_preprint1.sub('journal={arXiv preprint}', content)
        messages.append("修复 'journal={arXiv preprint arXiv:...}' -> 'journal={arXiv preprint}'")

    # 模式1b: journal = {arXiv preprint arXiv:XXXX} (带空格和版本号)
    pattern_arxiv_preprint2 = re.compile(
        r'journal\s*=\s*\{arXiv preprint arXiv:[A-Za-z0-9.]+\}',
        re.IGNORECASE
    )
    if pattern_arxiv_preprint2.search(content):
        content = pattern_arxiv_preprint2.sub('journal = {arXiv preprint}', content)
        messages.append("修复 'journal = {arXiv preprint arXiv:...}' -> 'journal = {arXiv preprint}'")

    # 模式1c: note={arXiv preprint arXiv:XXXX}
    pattern_note_arxiv = re.compile(
        r'note=\{arXiv preprint arXiv:[A-Za-z0-9.]+\}',
        re.IGNORECASE
    )
    if pattern_note_arxiv.search(content):
        content = pattern_note_arxiv.sub('note={arXiv preprint}', content)
        messages.append("修复 'note={arXiv preprint arXiv:...}' -> 'note={arXiv preprint}'")

    # 模式2: journal={Nature}/journal={Science} 等
    # 直接修复为 "arXiv preprint"，因为这些论文实际上是预印本
    top_journals_pattern = re.compile(
        r'journal=\{(Nature|Science|Cell|Nature Communications|Nature Climate Change|Nature Geoscience|Nature Machine Intelligence|Science Advances|PNAS)\}',
        re.IGNORECASE
    )

    def replace_with_preprint(match):
        journal = match.group(1)
        return 'journal={arXiv preprint}'

    if top_journals_pattern.search(content):
        content = top_journals_pattern.sub(replace_with_preprint, content)
        messages.append(f"修复 journal={{Nature/Science等}} 为 'journal={{arXiv preprint}}'")

    # 模式3: frontmatter venue="Nature"/venue="Science" 等
    top_journals_frontmatter = re.compile(
        r'^venue:\s*["\']?(Nature|Science|Cell|Nature Communications|Nature Climate Change|Nature Geoscience|Nature Machine Intelligence|Science Advances|PNAS)["\']?$',
        re.IGNORECASE | re.MULTILINE
    )

    def replace_venue_preprint(match):
        return 'venue: "arXiv preprint"'

    if top_journals_frontmatter.search(content):
        content = top_journals_frontmatter.sub(replace_venue_preprint, content)
        messages.append(f"修复 frontmatter venue={{Nature/Science等}} 为 'venue={{arXiv preprint}}'")

    if content != original_content:
        if not dry_run:
            file_path.write_text(content, encoding='utf-8')
        if verbose:
            for msg in messages:
                print(f"  {msg}")
        return True, messages

    return False, []


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='修复 BibTeX 中错误的 journal 字段',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  python scripts/fix_bibtex_venue.py --dry-run
  python scripts/fix_bibtex_venue.py --verbose
  python scripts/fix_bibtex_venue.py
        '''
    )
    parser.add_argument('--dry-run', action='store_true', help='仅显示不更新')
    parser.add_argument('--verbose', action='store_true', help='显示详细信息')
    args = parser.parse_args()

    print("=" * 70)
    print("BibTeX Journal 字段修复工具")
    print("=" * 70)
    print(f"模式: {'DRY-RUN (仅预览)' if args.dry_run else 'LIVE (执行更新)'}")
    print("=" * 70)

    # 扫描所有 abstract.md 和 summary.md
    md_files = list(PAPERS_DIR.glob("*/*/abstract.md")) + list(PAPERS_DIR.glob("*/*/summary.md"))

    total_files = 0
    changed_files = 0
    all_messages = []

    for file_path in sorted(md_files):
        total_files += 1
        changed, messages = process_file(file_path, dry_run=args.dry_run, verbose=args.verbose)
        if changed:
            changed_files += 1
            all_messages.extend(messages)

    print(f"\n扫描了 {total_files} 个文件")
    print(f"需要修复: {changed_files} 个文件")

    if all_messages:
        unique_messages = list(set(all_messages))
        print(f"\n修复类型:")
        for msg in unique_messages:
            print(f"  - {msg}")

    # 更新 papers.json 中的 venue
    print(f"\n同步更新 papers.json 中的 venue...")
    if DATA_FILE.exists():
        data = json.loads(DATA_FILE.read_text(encoding='utf-8'))
        top_journals = {'Nature', 'Science', 'Cell', 'PNAS', 'Nature Communications',
                        'Nature Climate Change', 'Nature Geoscience', 'Nature Machine Intelligence', 'Science Advances'}
        json_updated = 0

        for paper in data['papers']:
            arxiv_id = paper.get('arxiv')
            current_venue = paper.get('venue', '')

            # 检查是否需要从 Nature/Science 等更新为 arXiv preprint
            if current_venue in top_journals:
                if args.dry_run:
                    print(f"  [DRY-RUN] {arxiv_id}: {current_venue} -> arXiv preprint")
                else:
                    paper['venue'] = 'arXiv preprint'
                    print(f"  [OK] {arxiv_id}: {current_venue} -> arXiv preprint")
                json_updated += 1

        if not args.dry_run and json_updated > 0:
            DATA_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
            print(f"  [OK] 更新了 {json_updated} 篇论文的 venue")
        elif args.dry_run and json_updated > 0:
            print(f"  [DRY-RUN] 需要更新 {json_updated} 篇论文的 venue")
        else:
            print(f"  ✅ papers.json 中无需要更新的 venue")
    else:
        print(f"  [WARN] papers.json 不存在")

    if args.dry_run:
        print(f"\n[DRY-RUN] 如需执行修复，请去掉 --dry-run 参数")
    else:
        print(f"\n[OK] 修复完成")

    # 验证: 检查是否还有错误格式
    print("\n验证修复结果:")
    remaining = list(PAPERS_DIR.glob("*/*/abstract.md")) + list(PAPERS_DIR.glob("*/*/summary.md"))
    bad_format_count = 0

    for file_path in remaining:
        content = file_path.read_text(encoding='utf-8')
        if re.search(r'journal=\{arXiv preprint arXiv:', content, re.IGNORECASE):
            bad_format_count += 1

    if bad_format_count > 0:
        print(f"  ⚠️  仍有 {bad_format_count} 个文件存在 'journal={{arXiv preprint arXiv:...}}' 错误格式")
    else:
        print(f"  ✅ 无 'journal={{arXiv preprint arXiv:...}}' 错误格式")

    print("=" * 70)


if __name__ == "__main__":
    main()
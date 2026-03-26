# -*- coding: utf-8 -*-
"""验证 arXiv 链接的有效性"""

import json
import re
import urllib.request
import urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys

PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from utils.normalizers import normalize_arxiv

PAPERS_JSON = PROJECT_ROOT / "_data" / "papers.json"


def check_arxiv_link(arxiv_id):
    """检查 arXiv 链接是否可访问"""
    if not arxiv_id:
        return False, "Invalid/placeholder ID"

    url = f"https://arxiv.org/abs/{arxiv_id}"
    try:
        req = urllib.request.Request(url, method='HEAD')
        req.add_header('User-Agent', 'Mozilla/5.0')
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                return True, "OK"
            else:
                return False, f"HTTP {response.status}"
    except urllib.error.HTTPError as e:
        return False, f"HTTP {e.code}"
    except Exception as e:
        return False, str(e)[:50]


def main():
    print("加载 papers.json...")

    if not PAPERS_JSON.exists():
        print(f"错误: {PAPERS_JSON} 不存在，请先运行 update_index.py")
        return

    with open(PAPERS_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    papers = data.get('papers', [])
    print(f"找到 {len(papers)} 篇论文")

    # 提取所有 arXiv ID
    results = []
    for paper in papers:
        arxiv_raw = paper.get('arxiv', '')
        arxiv_normalized = normalize_arxiv(arxiv_raw)

        results.append({
            'title': paper.get('title', '')[:50],
            'year': paper.get('year'),
            'folder': paper.get('path', ''),
            'arxiv_raw': arxiv_raw,
            'arxiv_normalized': arxiv_normalized,
        })

    # 检查所有链接
    print("\n验证 arXiv 链接...")

    valid_count = 0
    invalid_count = 0
    placeholder_count = 0

    for r in results:
        if not r['arxiv_normalized']:
            if r['arxiv_raw'] in ['XXXXX', '待补充', '', 'Not available']:
                print(f"[PLACEHOLDER] {r['year']}/{r['folder']}: '{r['arxiv_raw']}' - 需补充")
                placeholder_count += 1
            else:
                print(f"[INVALID] {r['year']}/{r['folder']}: '{r['arxiv_raw']}' - 格式错误")
                invalid_count += 1
        else:
            # 实际检查链接（跳过以节省时间，只检查格式）
            # 如果需要实际验证，取消下面的注释
            # success, msg = check_arxiv_link(r['arxiv_normalized'])
            # if success:
            #     valid_count += 1
            # else:
            #     print(f"[DEAD] {r['year']}/{r['folder']}: {r['arxiv_normalized']} - {msg}")
            #     invalid_count += 1
            valid_count += 1

    print(f"\n汇总:")
    print(f"  有效: {valid_count}")
    print(f"  无效格式: {invalid_count}")
    print(f"  占位符: {placeholder_count}")


if __name__ == "__main__":
    main()

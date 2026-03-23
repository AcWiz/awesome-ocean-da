# -*- coding: utf-8 -*-
"""从 arXiv 获取论文元数据并更新 abstract.md"""

import re
import urllib.request
import urllib.error
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
PAPERS_DIR = PROJECT_ROOT / "papers"


def fetch_arxiv_page(arxiv_id):
    """获取 arXiv 页面内容"""
    url = f'https://arxiv.org/abs/{arxiv_id}'
    try:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (compatible; PaperBot/1.0)')
        with urllib.request.urlopen(req, timeout=15) as response:
            if response.status == 200:
                return response.read().decode('utf-8')
    except Exception as e:
        print(f"  获取失败: {e}")
    return None


def parse_arxiv_page(html_content):
    """解析 arXiv 页面提取元数据"""
    if not html_content:
        return None

    # 提取标题（新版 arXiv 格式）
    title_match = re.search(r'<h1 class="title mathjax">.*?:\s*(.+?)</h1>', html_content, re.DOTALL)
    if title_match:
        title = title_match.group(1).strip()
        # 移除可能残留的 HTML 标签
        title = re.sub(r'<[^>]+>', '', title)
    else:
        title = None

    # 提取作者
    authors_match = re.search(r'<div class="authors">.*?Authors:</span>(.+?)</div>', html_content, re.DOTALL)
    if authors_match:
        authors_html = authors_match.group(1)
        # 提取作者名
        author_names = re.findall(r'query=([^"]+)"[^>]*>([^<]+)', authors_html)
        authors = [name.strip() for _, name in author_names]
        if not authors:
            # 备用方式
            author_names = re.findall(r'>([^<]+)<', authors_html)
            authors = [a.strip() for a in author_names if a.strip() and not a.startswith('Languages')]
    else:
        authors = []

    # 提取摘要
    abstract_match = re.search(r'<blockquote class="abstract mathjax">.*?-\s*(.+?)</blockquote>', html_content, re.DOTALL)
    if abstract_match:
        abstract = abstract_match.group(1).strip()
        abstract = re.sub(r'<[^>]+>', '', abstract)
    else:
        abstract = None

    return {
        'title': title,
        'authors': authors,
        'abstract': abstract
    }


def update_abstract_md(file_path, arxiv_id, metadata):
    """更新 abstract.md 文件"""
    if not metadata:
        return False

    content = file_path.read_text(encoding='utf-8')

    # 检查是否是占位符文件（多种检测方式）
    placeholder_indicators = [
        '暂无论文内容',
        '由于未提供论文的具体内容',
        '需要原文内容补充',
        '需要原文内容才能生成摘要',
        '作者信息待补充',
        '提供的信息不完整',
        '无法生成准确的摘要',
        'No content available',
    ]

    # 如果 arXiv 字段是占位符，也需要更新
    arxiv_placeholder = [
        'Not Available',
        'Not available',
        '暂无',
        '待补充',
        'XXXXX',
    ]

    is_placeholder = any(indicator in content for indicator in placeholder_indicators)
    has_bad_arxiv = any(ap in content for ap in arxiv_placeholder)

    if not is_placeholder and not has_bad_arxiv:
        # 不是占位符文件，不需要更新
        return False

    # 构建新的 frontmatter
    title = metadata.get('title', file_path.parent.name)
    authors = metadata.get('authors', [])

    # 清理标题
    title = re.sub(r'\s+', ' ', title).strip() if title else file_path.parent.name

    # 生成新的 frontmatter
    new_frontmatter = f'''---
title: "{title}"
arXiv: "{arxiv_id}"
authors: {authors}
year: {file_path.parent.parent.name}
source: "arXiv"
venue: "arXiv"
method_tags: []
application_tags: []
---

# {title}

## 基本信息
- **论文链接**: https://arxiv.org/abs/{arxiv_id}
- **作者**: {', '.join(authors)}

## 摘要
{metadata.get('abstract', '暂无')}
'''

    file_path.write_text(new_frontmatter, encoding='utf-8')
    return True


def process_paper(arxiv_id, paper_dir):
    """处理单篇论文"""
    abstract_file = paper_dir / "abstract.md"
    if not abstract_file.exists():
        return False

    print(f"  获取 {arxiv_id}...")
    html = fetch_arxiv_page(arxiv_id)
    if not html:
        print(f"    获取页面失败")
        return False

    metadata = parse_arxiv_page(html)
    if not metadata:
        print(f"    解析页面失败")
        return False

    if update_abstract_md(abstract_file, arxiv_id, metadata):
        title = metadata.get('title', 'N/A') or 'N/A'
        print(f"    更新成功: {title[:50]}...")
        return True
    else:
        print(f"    无需更新（已有真实内容）")
        return False


def main():
    import argparse
    parser = argparse.ArgumentParser(description='从 arXiv 获取论文元数据')
    parser.add_argument('--dry-run', action='store_true', help='仅显示不更新')
    args = parser.parse_args()

    # 需要处理的 arXiv ID 列表
    arxiv_ids_to_fetch = [
        ('2024', '2409.03042'),  # Parameter Analysis
    ]

    print("开始获取 arXiv 论文元数据...")
    success_count = 0

    for year, arxiv_id in arxiv_ids_to_fetch:
        paper_dir = PAPERS_DIR / year / arxiv_id
        if paper_dir.exists():
            if process_paper(arxiv_id, paper_dir):
                success_count += 1
        else:
            print(f"  目录不存在: {paper_dir}")

    print(f"\n完成: 成功获取 {success_count} 篇论文")


if __name__ == "__main__":
    main()
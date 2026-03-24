# -*- coding: utf-8 -*-
"""生成标签分类页面和修复论文链接"""

import os
import sys
from pathlib import Path
from collections import defaultdict
import yaml
import re

PROJECT_ROOT = Path(__file__).parent.parent
PAPERS_DIR = PROJECT_ROOT / "papers"
CATEGORY_DIR = PAPERS_DIR


def normalize_arxiv(arxiv):
    """规范化 arXiv ID，移除无效字符，返回清理后的ID或None"""
    if not arxiv or arxiv in ['待补充', 'XXXXX', 'Not available', '', 'Not Available']:
        return None
    # 替换下划线为点（常见错误格式）
    arxiv = arxiv.replace('_', '.')
    # 移除 v1, v2 等版本号
    arxiv_clean = re.sub(r'v\d+$', '', arxiv).strip('.')
    # 如果看起来像有效的 arXiv ID（年月.数字），返回清理后的版本
    if re.match(r'^\d{2}\.\d{4,5}$', arxiv_clean):
        return arxiv_clean
    if re.match(r'^\d{4}\.\d{4,5}$', arxiv_clean):
        return arxiv_clean
    # 特殊处理带版本号的情况
    if re.match(r'^\d{2}\.\d{4,5}v\d+$', arxiv):
        return arxiv_clean
    if re.match(r'^\d{4}\.\d{4,5}v\d+$', arxiv):
        return arxiv_clean
    return None


def normalize_tag(tag):
    """规范化标签，移除下划线转为连字符，转小写用于匹配"""
    return tag.replace('_', '-').lower()


# 标签到分类名的映射（支持多种变体）
# key 是规范化后的标签名，value 是 (中文分类名, 文件名)
TAG_CATEGORIES = {
    # PINN
    "pinn": ("物理信息神经网络 (PINN)", "pinn.md"),
    "physics-informed-neural-network": ("物理信息神经网络 (PINN)", "pinn.md"),
    "physics-informed-neural-networks": ("物理信息神经网络 (PINN)", "pinn.md"),
    "physics-informed": ("物理信息神经网络 (PINN)", "pinn.md"),
    "physics-informed-ml": ("物理信息神经网络 (PINN)", "pinn.md"),
    # Koopman
    "koopman": ("Koopman 学习", "koopman.md"),
    "koopman-operator": ("Koopman 学习", "koopman.md"),
    "koopman-operator-theory": ("Koopman 学习", "koopman.md"),
    "koopman-learning": ("Koopman 学习", "koopman.md"),
    "koopman-autoencoder": ("Koopman 学习", "koopman.md"),
    # Neural Operator
    "neural-operator": ("神经算子 (Neural Operator)", "neural-operator.md"),
    "neural-operators": ("神经算子 (Neural Operator)", "neural-operator.md"),
    "neural-operator-learning": ("神经算子 (Neural Operator)", "neural-operator.md"),
    "fno": ("神经算子 (Neural Operator)", "neural-operator.md"),
    "fourier-neural-operator": ("神经算子 (Neural Operator)", "neural-operator.md"),
    "deeponet": ("神经算子 (Neural Operator)", "neural-operator.md"),
    # GNN
    "gnn": ("图神经网络 (GNN)", "gnn.md"),
    "graph-neural-network": ("图神经网络 (GNN)", "gnn.md"),
    "graph-neural-networks": ("图神经网络 (GNN)", "gnn.md"),
    "gcn": ("图神经网络 (GNN)", "gnn.md"),
    "gat": ("图神经网络 (GNN)", "gnn.md"),
    "graphsage": ("图神经网络 (GNN)", "gnn.md"),
    # 4D-Var / EnKF
    "4d-var": ("4D-Var / EnKF", "4d-var.md"),
    "enkf": ("4D-Var / EnKF", "4d-var.md"),
    "ensemble-kalman-filter": ("4D-Var / EnKF", "4d-var.md"),
    "variational-da": ("4D-Var / EnKF", "4d-var.md"),
    "variational-data-assimilation": ("4D-Var / EnKF", "4d-var.md"),
    # Transformer
    "transformer": ("Transformer / Attention", "transformer.md"),
    "transformers": ("Transformer / Attention", "transformer.md"),
    "attention": ("Transformer / Attention", "transformer.md"),
    # SST
    "sst": ("海表温度 (SST)", "sst.md"),
    "sst-forecasting": ("海表温度 (SST)", "sst.md"),
    "sea-surface-temperature": ("海表温度 (SST)", "sst.md"),
    # SSH
    "ssh": ("海表高度 (SSH)", "ssh.md"),
    "ssh-forecasting": ("海表高度 (SSH)", "ssh.md"),
    "sea-surface-height": ("海表高度 (SSH)", "ssh.md"),
    # ENSO
    "enso": ("ENSO 预测", "enso.md"),
    "enso-prediction": ("ENSO 预测", "enso.md"),
    "enso-forecast": ("ENSO 预测", "enso.md"),
    # Wave
    "wave": ("海浪预报", "wave.md"),
    "wave-forecasting": ("海浪预报", "wave.md"),
    "wave-prediction": ("海浪预报", "wave.md"),
    "ocean-wave": ("海浪预报", "wave.md"),
    "ocean-wave-forecasting": ("海浪预报", "wave.md"),
    # Global Forecast
    "global-forecast": ("全球预报", "global-forecast.md"),
    "global-forecasting": ("全球预报", "global-forecast.md"),
    "ocean-forecast": ("全球预报", "global-forecast.md"),
    "ocean-forecasting": ("全球预报", "global-forecast.md"),
    "global-ocean": ("全球预报", "global-forecast.md"),
    "global-ocean-modeling": ("全球预报", "global-forecast.md"),
}


def parse_abstract_md(file_path: Path) -> dict:
    """解析 abstract.md，提取 YAML front matter 和内容"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                metadata = yaml.safe_load(parts[1]) or {}
                body = parts[2].strip()
                return metadata, body
            except:
                pass

    return {}, content


def scan_papers():
    """扫描所有论文目录"""
    papers = []
    title_to_info = {}  # title -> {year, folder, arxiv, method_tags, application_tags, venue}

    for year_dir in sorted(PAPERS_DIR.iterdir(), reverse=True):
        if not year_dir.is_dir() or not year_dir.name.isdigit():
            continue

        year = int(year_dir.name)

        for paper_dir in sorted(year_dir.iterdir()):
            if not paper_dir.is_dir():
                continue

            abstract_file = paper_dir / "abstract.md"
            if not abstract_file.exists():
                continue

            metadata, body = parse_abstract_md(abstract_file)

            arxiv_raw = metadata.get('arXiv', '')
            title = metadata.get('title', paper_dir.name)

            # 清理 title
            title = re.sub(r'^#+\s*', '', title.split('\n')[0]) if '\n' in title else title
            title = title.strip('"').strip()

            # 规范化 arXiv ID
            arxiv = normalize_arxiv(arxiv_raw)

            paper_info = {
                'year': year,
                'folder': paper_dir.name,
                'arxiv_raw': arxiv_raw,
                'arxiv': arxiv,
                'title': title,
                'venue': metadata.get('venue', ''),
                'method_tags': metadata.get('method_tags', []),
                'application_tags': metadata.get('application_tags', []),
                'source': metadata.get('source', 'arXiv'),
            }

            papers.append(paper_info)
            title_to_info[title] = paper_info

    return papers, title_to_info


def get_venue_display(venue, source):
    """获取 venue 显示"""
    if venue and venue != '-':
        return venue
    if source == 'arXiv':
        return 'arXiv'
    return '-'


def format_tags_display(tags):
    """格式化标签为逗号分隔字符串（用于显示）"""
    if not tags:
        return '-'
    # 清理标签中的下划线
    cleaned = [t.replace('_', '-') for t in tags]
    return ', '.join(cleaned)


def paper_matches_tag(paper, normalized_tag):
    """检查论文是否匹配给定标签（规范化后）"""
    for t in paper.get('method_tags', []) + paper.get('application_tags', []):
        if normalize_tag(t) == normalized_tag:
            return True
    return False


def generate_paper_row(paper, include_summary=True):
    """生成论文表格行

    统一格式: | 年份 | 论文 | arXiv | Venue | 方法标签 | 应用 | 总结 |
    """
    arxiv = paper['arxiv']
    arxiv_raw = paper.get('arxiv_raw', '')
    year = paper['year']
    folder = paper['folder']
    title = paper['title']
    venue = get_venue_display(paper.get('venue', ''), paper.get('source', 'arXiv'))
    method_tags = format_tags_display(paper.get('method_tags', []))
    app_tags = format_tags_display(paper.get('application_tags', []))

    # 构建 arXiv 链接
    if arxiv:
        arxiv_link = f"[{arxiv}](https://arxiv.org/abs/{arxiv})"
    else:
        arxiv_link = "ID 待查"

    # 构建标题链接
    if arxiv:
        title_link = f"[{title}](https://arxiv.org/abs/{arxiv})"
    else:
        title_link = title

    # 格式: | 年份 | 论文 | arXiv | Venue | 方法标签 | 应用 | 总结 |
    row = f"| {year} | {title_link} | {arxiv_link} | {venue} | {method_tags} | {app_tags}"

    if include_summary:
        if arxiv:
            summary_link = f"[总结](./{year}/{folder}/summary.md)"
        else:
            summary_link = "-"
        row += f" | {summary_link}"

    return row


def generate_category_page(category_name, papers, normalized_tag):
    """生成单个分类页面"""
    # 过滤包含该标签的论文
    filtered = []
    for p in papers:
        if paper_matches_tag(p, normalized_tag):
            # 清理标签
            clean_method = [t.replace('_', '-') for t in p.get('method_tags', [])]
            clean_app = [t.replace('_', '-') for t in p.get('application_tags', [])]
            p = p.copy()
            p['method_tags'] = clean_method
            p['application_tags'] = clean_app
            filtered.append(p)

    # 按年份分组
    by_year = defaultdict(list)
    for p in filtered:
        by_year[p['year']].append(p)

    lines = []
    lines.append(f"# {category_name} 论文列表")
    lines.append("")
    lines.append(f"> 收录 AI/深度学习 + {category_name} 相关论文，共 {len(filtered)} 篇。")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 生成表格
    lines.append("| 年份 | 论文 | arXiv | Venue | 方法标签 | 应用 | 总结 |")
    lines.append("|------|-------|-------|------|----------|------|------|")

    for year in sorted(by_year.keys(), reverse=True):
        for paper in sorted(by_year[year], key=lambda x: x['arxiv'] or '', reverse=True):
            lines.append(generate_paper_row(paper))

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"*最后更新: 2026-03-23*")

    return '\n'.join(lines)


def generate_all_category_pages(papers):
    """生成所有分类页面"""
    # 收集所有唯一标签（规范化后）
    all_normalized_tags = set()
    for p in papers:
        for t in p.get('method_tags', []) + p.get('application_tags', []):
            all_normalized_tags.add(normalize_tag(t))

    # 生成每个标签对应的分类页面
    generated = set()
    for normalized_tag, (category_name, filename) in TAG_CATEGORIES.items():
        if normalized_tag not in all_normalized_tags:
            continue
        if filename in generated:
            continue

        content = generate_category_page(category_name, papers, normalized_tag)
        filepath = CATEGORY_DIR / filename
        filepath.write_text(content, encoding='utf-8')
        print(f"生成: {filepath}")
        generated.add(filename)


def generate_title_mapping_report(title_to_info):
    """生成标题到信息的映射报告，用于修复 papers/README.md"""
    print("\n=== 标题 -> 文件夹映射 ===")
    for title, info in sorted(title_to_info.items(), key=lambda x: (x[1]['year'], x[1]['folder'])):
        arxiv_display = info['arxiv'] or info['arxiv_raw'] or 'N/A'
        print(f"[{info['year']}] {info['folder']} | {arxiv_display} | {title[:50]}...")


def main():
    print("扫描论文目录...")
    papers, title_to_info = scan_papers()
    print(f"找到 {len(papers)} 篇论文")

    # 生成所有分类页面
    print("\n生成分类页面...")
    generate_all_category_pages(papers)

    # 生成标题映射报告
    generate_title_mapping_report(title_to_info)

    print("\n完成!")


if __name__ == "__main__":
    main()

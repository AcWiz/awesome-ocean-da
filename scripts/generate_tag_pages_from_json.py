# -*- coding: utf-8 -*-
"""从 papers.json 生成标签分类页面"""

import json
import re
from pathlib import Path
from collections import defaultdict

PROJECT_ROOT = Path(__file__).parent.parent
PAPERS_JSON = PROJECT_ROOT / "_data" / "papers.json"
PAPERS_DIR = PROJECT_ROOT / "papers"
OUTPUT_DIR = PAPERS_DIR


def normalize_arxiv(arxiv):
    """规范化 arXiv ID，移除无效字符，返回清理后的ID或None"""
    if not arxiv or arxiv in ['待补充', 'XXXXX', 'Not available', '', 'Not Available']:
        return None
    arxiv = arxiv.replace('_', '.')
    arxiv_clean = re.sub(r'v\d+$', '', arxiv).strip('.')
    if re.match(r'^\d{2}\.\d{4,5}$', arxiv_clean):
        return arxiv_clean
    if re.match(r'^\d{4}\.\d{4,5}$', arxiv_clean):
        return arxiv_clean
    if re.match(r'^\d{2}\.\d{4,5}v\d+$', arxiv):
        return arxiv_clean
    if re.match(r'^\d{4}\.\d{4,5}v\d+$', arxiv):
        return arxiv_clean
    return None


def normalize_tag(tag):
    """规范化标签，移除下划线转为连字符，转小写用于匹配"""
    return tag.replace('_', '-').lower()


# 标签别名映射（规范化后的别名 → 主标签）
# 用于处理 "Physics-Informed Neural Networks" → "pinn" 这类短语到缩写的映射
TAG_ALIASES = {
    # PINN 别名
    "physics-informed-neural-networks": "pinn",
    "physics-informed-neural-network": "pinn",
    "physics-informed": "pinn",
    "physics-informed-ml": "pinn",
    "physics-informed-neural-networks": "pinn",
    # Neural Operator 别名
    "fourier-neural-operator": "neural-operator",
    "deeponet": "neural-operator",
    "neural-operators": "neural-operator",
    # GNN 别名
    "graph-neural-networks": "gnn",
    "graph-neural-network": "gnn",
    # 4D-Var 别名
    "variational-da": "4d-var",
    "variational-data-assimilation": "4d-var",
    "ensemble-kalman-filter": "4d-var",
    # Koopman 别名
    "koopman-operator": "koopman",
    "koopman-operator-theory": "koopman",
    "koopman-learning": "koopman",
    "koopman-operator": "koopman",
    "koopman autoencoder": "koopman",
    "koopman learning": "koopman",
    "koopman operator": "koopman",
    "koopman-autoencoder": "koopman",
}


def get_canonical_tag(normalized_tag):
    """获取标签的规范形式（解析别名）"""
    return TAG_ALIASES.get(normalized_tag, normalized_tag)


# 标签到分类名的映射
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


def get_venue_display(venue, source):
    """获取 venue 显示"""
    if venue and venue != '-':
        return venue
    if source == 'arXiv':
        return 'arXiv'
    return '-'


def format_tags_display(tags):
    """格式化标签为逗号分隔字符串"""
    if not tags:
        return '-'
    cleaned = [t.replace('_', '-') for t in tags]
    return ', '.join(cleaned)


def paper_matches_tag(paper, normalized_tag):
    """检查论文是否匹配给定标签（规范化后，支持别名解析）"""
    for t in paper.get('method_tags', []) + paper.get('application_tags', []):
        tag = normalize_tag(t)
        # 解析别名到规范标签
        canonical = get_canonical_tag(tag)
        if canonical == normalized_tag:
            return True
    return False


def generate_paper_row(paper):
    """生成论文表格行

    统一格式: | 年份 | 论文 | arXiv | Venue | 方法标签 | 应用 | 总结 |
    """
    arxiv = normalize_arxiv(paper.get('arxiv', ''))
    year = paper.get('year', '')
    folder = paper.get('path', '').replace('papers/', '')
    title = paper.get('title', '')
    venue = get_venue_display(paper.get('venue', ''), paper.get('source', 'arXiv'))
    method_tags = format_tags_display(paper.get('method_tags', []))
    app_tags = format_tags_display(paper.get('application_tags', []))

    # 构建论文链接（指向 arXiv）
    if arxiv:
        title_link = f"[{title}](https://arxiv.org/abs/{arxiv})"
    else:
        title_link = title

    # 构建 arXiv 链接
    if arxiv:
        arxiv_link = f"[{arxiv}](https://arxiv.org/abs/{arxiv})"
    else:
        arxiv_link = "ID 待查"

    # 构建总结链接（指向 summary.md）
    # folder 格式是 "2022/2211.05904"，直接使用即可
    if arxiv:
        summary_link = f"[总结](./{folder}/summary.md)"
    else:
        summary_link = "-"

    # 格式: | 年份 | 论文 | arXiv | Venue | 方法标签 | 应用 | 总结 |
    row = f"| {year} | {title_link} | {arxiv_link} | {venue} | {method_tags} | {app_tags} | {summary_link} |"

    return row


def generate_category_page(category_name, papers, normalized_tag):
    """生成单个分类页面"""
    # 过滤包含该标签的论文
    filtered = []
    for p in papers:
        if paper_matches_tag(p, normalized_tag):
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

    # 生成表格（统一格式）
    lines.append("| 年份 | 论文 | arXiv | Venue | 方法标签 | 应用 | 总结 |")
    lines.append("|------|------|-------|-------|----------|------|------|")

    for year in sorted(by_year.keys(), reverse=True):
        for paper in sorted(by_year[year], key=lambda x: x.get('arxiv') or '', reverse=True):
            lines.append(generate_paper_row(paper))

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"*最后更新: 2026-03-23*")

    return '\n'.join(lines)


def generate_all_category_pages(papers):
    """生成所有分类页面"""
    # 收集所有唯一标签（规范化后，包含别名解析后的规范形式）
    all_normalized_tags = set()
    for p in papers:
        for t in p.get('method_tags', []) + p.get('application_tags', []):
            tag = normalize_tag(t)
            all_normalized_tags.add(tag)
            # 同时添加别名解析后的规范形式
            all_normalized_tags.add(get_canonical_tag(tag))

    # 生成每个标签对应的分类页面
    generated = set()
    for normalized_tag, (category_name, filename) in TAG_CATEGORIES.items():
        if normalized_tag not in all_normalized_tags:
            continue
        if filename in generated:
            continue

        content = generate_category_page(category_name, papers, normalized_tag)
        filepath = OUTPUT_DIR / filename
        filepath.write_text(content, encoding='utf-8')
        print(f"生成: {filepath}")
        generated.add(filename)


def main():
    print("加载 papers.json...")

    if not PAPERS_JSON.exists():
        print(f"错误: {PAPERS_JSON} 不存在，请先运行 update_index.py")
        return

    with open(PAPERS_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    papers = data.get('papers', [])
    print(f"找到 {len(papers)} 篇论文")

    print("\n生成分类页面...")
    generate_all_category_pages(papers)

    print("\n完成!")


if __name__ == "__main__":
    main()
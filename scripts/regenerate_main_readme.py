# -*- coding: utf-8 -*-
"""从 papers.json 生成主页 README"""

import json
import re
from pathlib import Path
from collections import defaultdict

PROJECT_ROOT = Path(__file__).parent.parent
PAPERS_JSON = PROJECT_ROOT / "_data" / "papers.json"
README_FILE = PROJECT_ROOT / "README.md"


def normalize_arxiv(arxiv):
    """规范化 arXiv ID"""
    if not arxiv or arxiv in ['待补充', 'XXXXX', 'Not available', '', 'Not Available']:
        return None
    arxiv = arxiv.replace('_', '.')
    arxiv_clean = re.sub(r'v\d+$', '', arxiv).strip('.')
    if re.match(r'^\d{2}\.\d{4,5}$', arxiv_clean):
        return arxiv_clean
    if re.match(r'^\d{4}\.\d{4,5}$', arxiv_clean):
        return arxiv_clean
    return None


def normalize_tag(tag):
    """规范化标签"""
    return tag.replace('_', '-').lower()


# 标签到分类信息的映射
TAG_CATEGORIES = {
    "pinn": ("物理信息神经网络 (PINN)", "pinn.md", "PINN"),
    "physics-informed-neural-network": ("物理信息神经网络 (PINN)", "pinn.md", "PINN"),
    "physics-informed-neural-networks": ("物理信息神经网络 (PINN)", "pinn.md", "PINN"),
    "physics-informed": ("物理信息神经网络 (PINN)", "pinn.md", "PINN"),
    "physics-informed-ml": ("物理信息神经网络 (PINN)", "pinn.md", "PINN"),
    "koopman": ("Koopman 学习", "koopman.md", "Koopman"),
    "koopman-operator": ("Koopman 学习", "koopman.md", "Koopman"),
    "koopman-operator-theory": ("Koopman 学习", "koopman.md", "Koopman"),
    "koopman-learning": ("Koopman 学习", "koopman.md", "Koopman"),
    "koopman-autoencoder": ("Koopman 学习", "koopman.md", "Koopman"),
    "neural-operator": ("神经算子 (Neural Operator)", "neural-operator.md", "Neural-Operator"),
    "neural-operators": ("神经算子 (Neural Operator)", "neural-operator.md", "Neural-Operator"),
    "neural-operator-learning": ("神经算子 (Neural Operator)", "neural-operator.md", "Neural-Operator"),
    "fno": ("神经算子 (Neural Operator)", "neural-operator.md", "FNO"),
    "fourier-neural-operator": ("神经算子 (Neural Operator)", "neural-operator.md", "FNO"),
    "deeponet": ("神经算子 (Neural Operator)", "neural-operator.md", "DeepONet"),
    "gnn": ("图神经网络 (GNN)", "gnn.md", "GNN"),
    "graph-neural-network": ("图神经网络 (GNN)", "gnn.md", "GNN"),
    "graph-neural-networks": ("图神经网络 (GNN)", "gnn.md", "GNN"),
    "gcn": ("图神经网络 (GNN)", "gnn.md", "GCN"),
    "gat": ("图神经网络 (GNN)", "gnn.md", "GAT"),
    "graphsage": ("图神经网络 (GNN)", "gnn.md", "GraphSAGE"),
    "4d-var": ("变分方法 (4D-Var / EnKF)", "4d-var.md", "4D-Var"),
    "enkf": ("变分方法 (4D-Var / EnKF)", "4d-var.md", "EnKF"),
    "ensemble-kalman-filter": ("变分方法 (4D-Var / EnKF)", "4d-var.md", "EnKF"),
    "variational-da": ("变分方法 (4D-Var / EnKF)", "4d-var.md", "4D-Var"),
    "variational-data-assimilation": ("变分方法 (4D-Var / EnKF)", "4d-var.md", "4D-Var"),
    "transformer": ("Transformer / Attention", "transformer.md", "Transformer"),
    "transformers": ("Transformer / Attention", "transformer.md", "Transformer"),
    "attention": ("Transformer / Attention", "transformer.md", "Attention"),
    "sst": ("海表温度 (SST)", "sst.md", "SST"),
    "sst-forecasting": ("海表温度 (SST)", "sst.md", "SST"),
    "sea-surface-temperature": ("海表温度 (SST)", "sst.md", "SST"),
    "ssh": ("海表高度 (SSH)", "ssh.md", "SSH"),
    "ssh-forecasting": ("海表高度 (SSH)", "ssh.md", "SSH"),
    "sea-surface-height": ("海表高度 (SSH)", "ssh.md", "SSH"),
    "enso": ("ENSO 预测", "enso.md", "ENSO"),
    "enso-prediction": ("ENSO 预测", "enso.md", "ENSO"),
    "enso-forecast": ("ENSO 预测", "enso.md", "ENSO"),
    "wave": ("海浪预报", "wave.md", "Wave"),
    "wave-forecasting": ("海浪预报", "wave.md", "Wave"),
    "wave-prediction": ("海浪预报", "wave.md", "Wave"),
    "ocean-wave": ("海浪预报", "wave.md", "Wave"),
    "ocean-wave-forecasting": ("海浪预报", "wave.md", "Wave"),
    "global-forecast": ("全球预报", "global-forecast.md", "Global"),
    "global-forecasting": ("全球预报", "global-forecast.md", "Global"),
    "ocean-forecast": ("全球预报", "global-forecast.md", "Ocean"),
    "ocean-forecasting": ("全球预报", "global-forecast.md", "Ocean"),
    "global-ocean": ("全球预报", "global-forecast.md", "Global"),
    "global-ocean-modeling": ("全球预报", "global-forecast.md", "Global"),
}


def paper_matches_tag(paper, normalized_tag):
    """检查论文是否匹配给定标签"""
    for t in paper.get('method_tags', []) + paper.get('application_tags', []):
        if normalize_tag(t) == normalized_tag:
            return True
    return False


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


def generate_paper_row(paper):
    """生成论文表格行（主页格式）

    主页格式: | 年份 | 论文 | Venue | 方法 | 应用 | 总结 |
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

    # 构建总结链接（指向 summary.md）
    if arxiv:
        summary_link = f"[总结](./papers/{folder}/summary.md)"
    else:
        summary_link = "-"

    # 移除 arXiv 列（论文列已链接到 arXiv），添加总结列
    row = f"| {year} | {title_link} | {venue} | {method_tags} | {app_tags} | {summary_link} |"

    return row


def generate_category_section(category_name, category_file, papers, normalized_tag, method_desc=""):
    """生成单个分类部分"""
    # 过滤包含该标签的论文
    filtered = []
    for p in papers:
        if paper_matches_tag(p, normalized_tag):
            filtered.append(p)

    if not filtered:
        return []

    # 按年份分组
    by_year = defaultdict(list)
    for p in filtered:
        by_year[p['year']].append(p)

    lines = []
    lines.append(f"### {category_name}")
    if method_desc:
        lines.append(f"> {method_desc}")
    lines.append("")
    lines.append(f"| 年份 | 论文 | Venue | 方法 | 应用 | 总结 |")
    lines.append("|------|------|-------|------|------|------|")

    # 只显示前几篇（主页只显示摘要）
    count = 0
    for year in sorted(by_year.keys(), reverse=True):
        for paper in sorted(by_year[year], key=lambda x: x.get('arxiv') or '', reverse=True):
            if count >= 6:  # 主页每类最多显示6篇
                break
            lines.append(generate_paper_row(paper))
            count += 1
        if count >= 6:
            break

    lines.append("")
    lines.append(f"[更多 {category_name} 论文 →](./papers/{category_file})")
    lines.append("")
    lines.append("---")
    lines.append("")

    return lines


def generate_year_browse_section(papers):
    """生成按年份浏览部分"""
    by_year = defaultdict(list)
    for p in papers:
        by_year[p['year']].append(p)

    lines = []
    lines.append("## 按年份浏览")
    lines.append("")
    lines.append("| 年份 | 论文数 | 浏览 |")
    lines.append("|------|--------|------|")

    for year in sorted(by_year.keys(), reverse=True):
        count = len(by_year[year])
        lines.append(f"| {year} | {count} | [浏览](./papers/{year}/index.md) |")

    lines.append("")
    lines.append("---")
    lines.append("")

    return lines


def main():
    print("加载 papers.json...")

    if not PAPERS_JSON.exists():
        print(f"错误: {PAPERS_JSON} 不存在，请先运行 update_index.py")
        return

    with open(PAPERS_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)

    papers = data.get('papers', [])
    print(f"找到 {len(papers)} 篇论文")

    # 收集所有已生成的分类
    generated_categories = set()

    # 生成核心方法部分
    method_lines = []
    method_lines.append("## 核心方法")
    method_lines.append("")

    method_tags = [
        ("pinn", "将物理约束嵌入神经网络 Loss，强制解满足物理定律"),
        ("koopman", "通过全局线性动力学近似捕捉非线性系统演化"),
        ("neural-operator", "学习解算子映射，无网格约束的偏微分方程求解"),
        ("gnn", "利用图结构建模海洋要素间的空间依赖关系"),
        ("4d-var", "变分数据同化方法，通过最小化目标函数估计最优状态"),
        ("transformer", "利用自注意力机制捕捉长距离依赖关系"),
    ]

    for tag, desc in method_tags:
        if tag in TAG_CATEGORIES:
            cat_name, cat_file, _ = TAG_CATEGORIES[tag]
            lines = generate_category_section(cat_name, cat_file, papers, tag, desc)
            if lines:
                method_lines.extend(lines)
                generated_categories.add(cat_file)

    # 生成应用场景部分
    app_lines = []
    app_lines.append("## 应用场景")
    app_lines.append("")

    app_tags = [
        ("sst", "海表温度是海洋最重要的基础变量之一"),
        ("ssh", "海表高度反映海洋动力过程和环流结构"),
        ("enso", "ENSO 是最强的年际气候变化信号"),
        ("wave", "海浪对海洋工程和航行安全至关重要"),
        ("global-forecast", "全球海洋预报是气候预测的基础"),
    ]

    for tag, desc in app_tags:
        if tag in TAG_CATEGORIES:
            cat_name, cat_file, _ = TAG_CATEGORIES[tag]
            lines = generate_category_section(cat_name, cat_file, papers, tag, desc)
            if lines:
                app_lines.extend(lines)
                generated_categories.add(cat_file)

    # 生成年份浏览部分
    year_lines = generate_year_browse_section(papers)

    # 组装完整 README
    total = len(papers)
    years = sorted(set(p['year'] for p in papers), reverse=True)
    latest_year = years[0] if years else 2026

    readme_lines = []
    readme_lines.append("# AI + 海洋数据同化论文库")
    readme_lines.append("")
    readme_lines.append("> 收录 AI/深度学习 + 海洋数据同化、预报相关的学术论文，持续更新。")
    readme_lines.append("")
    readme_lines.append(f"[![Papers](https://img.shields.io/badge/Papers-{total}-blue.svg)](#) ·")
    readme_lines.append(f"[![{latest_year}](https://img.shields.io/badge/{latest_year}-19-green.svg)](#papers-by-year) ·")
    readme_lines.append("[![Last Updated](https://img.shields.io/badge/Updated-2026--03--23-orange.svg)](#) ·")
    readme_lines.append("[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)")
    readme_lines.append("")
    readme_lines.append("---")
    readme_lines.append("")
    readme_lines.append("## 目录")
    readme_lines.append("")
    readme_lines.append("- [核心方法](#核心方法)")
    readme_lines.append("  - [物理信息神经网络 (PINN)](#物理信息神经网络-pinn)")
    readme_lines.append("  - [Koopman 学习](#koopman-学习)")
    readme_lines.append("  - [神经算子 (Neural Operator)](#神经算子-neural-operator)")
    readme_lines.append("  - [图神经网络 (GNN)](#图神经网络-gnn)")
    readme_lines.append("  - [变分方法 (4D-Var / EnKF)](#变分方法-4d-var--enkf)")
    readme_lines.append("  - [Transformer / Attention](#transformer--attention)")
    readme_lines.append("- [应用场景](#应用场景)")
    readme_lines.append("  - [海表温度 (SST)](#海表温度-sst)")
    readme_lines.append("  - [海表高度 (SSH)](#海表高度-ssh)")
    readme_lines.append("  - [ENSO 预测](#enso-预测)")
    readme_lines.append("  - [海浪预报](#海浪预报)")
    readme_lines.append("  - [全球预报](#全球预报)")
    readme_lines.append("- [按年份浏览](#papers-by-year)")
    readme_lines.append("- [如何贡献](./CONTRIBUTING.md)")
    readme_lines.append("")
    readme_lines.append("---")
    readme_lines.append("")

    readme_lines.extend(method_lines)
    readme_lines.extend(app_lines)
    readme_lines.extend(year_lines)

    # 贡献部分
    readme_lines.append("## 如何贡献")
    readme_lines.append("")
    readme_lines.append("欢迎提交 PR 或 Issue！详见 [贡献指南](./CONTRIBUTING.md)。")
    readme_lines.append("")

    # 写入文件
    content = '\n'.join(readme_lines)
    README_FILE.write_text(content, encoding='utf-8')
    print(f"生成: {README_FILE}")

    print("\n完成!")


if __name__ == "__main__":
    main()
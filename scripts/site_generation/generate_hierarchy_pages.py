# -*- coding: utf-8 -*-
"""从论文 abstract.md 生成分层分类页面 (by-method.md, by-application.md)

该脚本复用 scripts/site_generation/ 的现有基础设施:
- utils.normalizers: normalize_tag()
- utils.tag_config: TAG_ALIASES, get_canonical_tag()

在单次扫描中同时构建 method_index 和 application_index。
每篇论文可以出现在多个分类中（根据其标签）。
"""

import sys
import re
from pathlib import Path
from collections import defaultdict
from datetime import date

PROJECT_ROOT = Path(__file__).parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from utils.normalizers import normalize_tag
from utils.tag_config import TAG_ALIASES, get_canonical_tag

PAPERS_DIR = PROJECT_ROOT / "papers"
OUTPUT_METHOD = PAPERS_DIR / "by-method.md"
OUTPUT_APPLICATION = PAPERS_DIR / "by-application.md"

# ============================================================
# 层次化分类体系定义
# ============================================================

# 方法轴: 主分类 -> [子分类]
METHOD_HIERARCHY = {
    "PINN": [
        "physics-constrained", "wave-PINN", "ocean-circulation-PINN",
        "sea-ice-PINN", "advection-diffusion-PINN", "stratified-ocean-PINN"
    ],
    "Neural Operator": [
        "FNO", "PINO", "Kernel-Operator", "Mamba-Operator", "graph-neural-operator"
    ],
    "GNN": [
        "spherical-GNN", "mesh-GNN", "graph-dynamic", "graph-ensemble"
    ],
    "4D-Var/EnKF": [
        "variational", "ensemble-Kalman", "hybrid", "conjugate-gradient"
    ],
    "Transformer": [
        "vision-transformer", "state-space-model", "mixture-of-experts", "attention-mechanism"
    ],
    "Other": [
        "LSTM", "CNN", "U-Net", "diffusion-model", "generative-model"
    ],
}

# 应用轴: 主分类 -> [子分类]
APPLICATION_HIERARCHY = {
    "SST": [
        "global-SST", "regional-SST", "SST-anomaly", "PDO-mode", "upwelling-SST"
    ],
    "SSH": [
        "SSH-reconstruction", "eddy-detection", "sea-level-rise", "Gulf-Stream"
    ],
    "ENSO": [
        "NINO3.4", "El-Nino", "La-Nina", "ENSO-prediction"
    ],
    "海浪": [
        "wave-height", "wave-phase-resolved", "wave-spectrum", "wave-flume"
    ],
    "全球预报": [
        "global-ocean", "multi-variable", "benchmark", "ocean-circulation", "sea-ice"
    ],
    "海洋数据同化": [
        "ocean-da", "ocean-data-assimilation", "ocean-dynamics", "ocean-modeling"
    ],
}

# 原始标签 -> 方法主分类 的映射 (展开后的大映射)
METHOD_TAG_TO_CATEGORY = {
    # PINN - 包括各种变体
    "pinn": "PINN", "physics-informed-neural-network": "PINN",
    "physics-informed-neural-networks": "PINN", "physics-informed": "PINN",
    "physics-informed-ml": "PINN", "physics_informed": "PINN",
    "physics-informed-learning": "PINN",
    "physics-informed neural network": "PINN",
    "physics-informed neural networks": "PINN",
    # Neural Operator - 包括各种变体
    "neural-operator": "Neural Operator", "neural-operators": "Neural Operator",
    "fno": "Neural Operator", "fourier-neural-operator": "Neural Operator",
    "fourier_neural_operator": "Neural Operator", "deeponet": "Neural Operator",
    "deep_onet": "Neural Operator", "pino": "Neural Operator",
    "kernel-operator": "Neural Operator", "kernel_operator": "Neural Operator",
    "mamba-operator": "Neural Operator", "mamba_operator": "Neural Operator",
    "graph-neural-operator": "Neural Operator",
    "graph_neural_operator": "Neural Operator", "afno": "Neural Operator",
    "ffno": "Neural Operator", "fn": "Neural Operator",
    "neural operator": "Neural Operator",
    "graph neural network": "GNN",
    # GNN
    "neural-operator": "Neural Operator", "neural-operators": "Neural Operator",
    "fno": "Neural Operator", "fourier-neural-operator": "Neural Operator",
    "fourier_neural_operator": "Neural Operator", "deeponet": "Neural Operator",
    "deep_onet": "Neural Operator", "pino": "Neural Operator",
    "kernel-operator": "Neural Operator", "kernel_operator": "Neural Operator",
    "mamba-operator": "Neural Operator", "mamba_operator": "Neural Operator",
    "graph-neural-operator": "Neural Operator",
    "graph_neural_operator": "Neural Operator", "afno": "Neural Operator",
    "ffno": "Neural Operator", "fn": "Neural Operator",
    # GNN
    "gnn": "GNN", "graph-neural-network": "GNN", "graph-neural-networks": "GNN",
    "gcn": "GNN", "gat": "GNN", "graphsage": "GNN",
    "graph_network": "GNN", "graph_sage": "GNN",
    "spherical-gnn": "GNN", "spherical_gnn": "GNN",
    "mesh-gnn": "GNN", "mesh_gnn": "GNN",
    "graph-dynamic": "GNN", "graph-dynamics": "GNN",
    "graph-ensemble": "GNN",
    "hierarchical-gnn": "GNN", "hierarchical_graph": "GNN",
    # 4D-Var / EnKF
    "4d-var": "4D-Var/EnKF", "4dvar": "4D-Var/EnKF",
    "enkf": "4D-Var/EnKF", "ensemble-kalman-filter": "4D-Var/EnKF",
    "ensemble_kalman_filter": "4D-Var/EnKF",
    "variational-da": "4D-Var/EnKF", "variational-data-assimilation": "4D-Var/EnKF",
    "variational": "4D-Var/EnKF", "ensemble-kalman": "4D-Var/EnKF",
    "hybrid": "4D-Var/EnKF", "conjugate-gradient": "4D-Var/EnKF",
    "conjugate_gradient": "4D-Var/EnKF",
    "variational_inference": "4D-Var/EnKF",
    # Transformer
    "transformer": "Transformer", "transformers": "Transformer",
    "vision-transformer": "Transformer", "vit": "Transformer",
    "vision_transformer": "Transformer",
    "state-space-model": "Transformer", "state_space_model": "Transformer",
    "state-space-model": "Transformer", "mamba": "Transformer",
    "mixture-of-experts": "Transformer", "mixture_of_experts": "Transformer", "moe": "Transformer",
    "attention-mechanism": "Transformer", "attention": "Transformer",
    "attention_mechanism": "Transformer", "self-attention": "Transformer",
    "self_attention": "Transformer",
    # Other methods
    "lstm": "Other", "rnn": "Other", "gru": "Other",
    "bilstm": "Other", "bi_lstm": "Other",
    "cnn": "Other", "convolutional-neural-network": "Other",
    "convolutional_neural_network": "Other",
    "u-net": "Other", "u_net": "Other", "unet": "Other", "unet": "Other",
    "stu-net": "Other", "deeplabv3": "Other", "his-unet": "Other",
    "diffusion-model": "Other", "diffusion_models": "Other", "diffusion": "Other",
    "score-based": "Other", "score_based": "Other", "ddpm": "Other",
    "generative-model": "Other", "gan": "Other", "vae": "Other",
    "diffusion_model": "Other",
    "lstm": "Other", "rnn": "Other", "gru": "Other",
}

# 原始标签 -> 应用主分类 的映射 (展开后的大映射)
APPLICATION_TAG_TO_CATEGORY = {
    # SST
    "sst": "SST", "sst-forecasting": "SST", "sea-surface-temperature": "SST",
    "sea_surface_temperature": "SST",
    "global-sst": "SST", "regional-sst": "SST", "sst-anomaly": "SST",
    "pdo-mode": "SST", "pdo": "SST", "upwelling-sst": "SST",
    "sst_prediction": "SST", "sst_reconstruction": "SST",
    # SSH
    "ssh": "SSH", "ssh-forecasting": "SSH", "sea-surface-height": "SSH",
    "sea_surface_height": "SSH",
    "ssh-reconstruction": "SSH", "eddy-detection": "SSH",
    "sea-level-rise": "SSH", "gulf-stream": "SSH",
    "gulf_stream": "SSH", "sea_level_rise": "SSH",
    "sea_surface_elevation_prediction": "SSH",
    # ENSO
    "enso": "ENSO", "enso-prediction": "ENSO", "enso-forecast": "ENSO",
    "nino3.4": "ENSO", "nino": "ENSO", "el-nino": "ENSO", "el_nino": "ENSO",
    "la-nina": "ENSO", "la_nina": "ENSO",
    "enso_prediction": "ENSO", "enso_teleconnection": "ENSO",
    # 海浪
    "wave": "海浪", "wave-forecasting": "海浪", "wave-prediction": "海浪",
    "ocean-wave": "海浪", "ocean-wave-forecasting": "海浪",
    "wave-height": "海浪", "significant-wave-height": "海浪",
    "significant_wave_height": "海浪",
    "wave-phase-resolved": "海浪", "phase-resolved": "海浪",
    "wave_physics": "海浪", "phase_resolved": "海浪",
    "wave-spectrum": "海浪", "wave-flume": "海浪",
    "ocean_wave": "海浪", "wave_prediction": "海浪",
    "wave_propagation": "海浪", "wave_reconstruction": "海浪",
    # 全球预报
    "global-forecast": "全球预报", "global-forecasting": "全球预报",
    "ocean-forecast": "全球预报", "ocean-forecasting": "全球预报",
    "global-ocean": "全球预报", "global-ocean-modeling": "全球预报",
    "global_ocean": "全球预报", "global_ocean_modeling": "全球预报",
    "multi-variable": "全球预报", "multi_variable": "全球预报",
    "benchmark": "全球预报",
    "ocean-circulation": "全球预报", "ocean_circulation": "全球预报",
    "sea-ice": "全球预报", "sea_ice": "全球预报",
    "data-assimilation": "全球预报", "data_assimilation": "全球预报",
    "ocean_modeling": "全球预报",
    "ocean_dynamics": "全球预报",
    # 海洋数据同化
    "ocean-da": "海洋数据同化",
    "ocean-data-assimilation": "海洋数据同化",
    "ocean-dynamics": "海洋数据同化",
    "ocean-modeling": "海洋数据同化",
    "海洋数据同化": "海洋数据同化",
}


def parse_frontmatter(content: str) -> dict:
    """解析 markdown frontmatter"""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm


def get_tag_list(fm: dict, key: str) -> list:
    """从 frontmatter 获取标签列表"""
    val = fm.get(key, '')
    if not val or val == '[]':
        return []
    # 解析 Python 列表格式
    val = val.strip('[]')
    tags = []
    for t in val.split(','):
        t = t.strip().strip("'").strip('"').strip()
        if t:
            tags.append(t)
    return tags


def normalize_tag_flexible(tag: str) -> str:
    """更灵活的标签规范化 - 尝试多种规范化方式"""
    # 原始标签
    original = tag.strip()
    # 转换为小写
    nt = original.lower()
    # 替换下划线为连字符
    nt = nt.replace('_', '-')
    return nt


def scan_papers():
    """单次扫描所有论文，构建 method_index 和 application_index

    每篇论文会被添加到 ALL 匹配的分类中。
    """
    method_index = defaultdict(lambda: defaultdict(set))  # category -> subcategory -> papers (set)
    application_index = defaultdict(lambda: defaultdict(set))

    for year_dir in sorted(PAPERS_DIR.iterdir(), reverse=True):
        if not year_dir.is_dir() or not re.match(r'^\d{4}$', year_dir.name):
            continue
        year = year_dir.name
        for paper_dir in year_dir.iterdir():
            if not paper_dir.is_dir():
                continue
            abstract_path = paper_dir / "abstract.md"
            if not abstract_path.exists():
                continue

            content = abstract_path.read_text(encoding='utf-8')
            fm = parse_frontmatter(content)

            arxiv = fm.get('arXiv', '') or ''
            title = fm.get('title', '') or paper_dir.name
            venue = fm.get('venue', '') or '-'

            paper_key = f"{year}/{paper_dir.name}"
            paper = {
                'year': year,
                'title': title,
                'arxiv': arxiv,
                'venue': venue,
                'folder': paper_key,
                'key': paper_key  # 用于去重
            }

            # 处理方法标签 - 添加到所有匹配的分类
            method_tags = get_tag_list(fm, 'method_tags')
            matched_categories = set()
            for tag in method_tags:
                nt = normalize_tag_flexible(tag)
                # 尝试多种匹配方式
                cat = METHOD_TAG_TO_CATEGORY.get(nt, None)
                if cat:
                    matched_categories.add(cat)
                # 也尝试原始标签
                cat_orig = METHOD_TAG_TO_CATEGORY.get(tag, None)
                if cat_orig:
                    matched_categories.add(cat_orig)
                # 也尝试规范化后的原始形式
                nt_orig_style = nt.replace('-', '_')
                cat2 = METHOD_TAG_TO_CATEGORY.get(nt_orig_style, None)
                if cat2:
                    matched_categories.add(cat2)

            # 如果没有匹配到任何分类，归入 Other
            if not matched_categories:
                matched_categories.add("Other")

            for cat in matched_categories:
                method_index[cat][""].add(paper_key)

            # 处理应用标签
            app_tags = get_tag_list(fm, 'application_tags')
            matched_app_categories = set()
            for tag in app_tags:
                nt = normalize_tag_flexible(tag)
                cat = APPLICATION_TAG_TO_CATEGORY.get(nt, None)
                if cat:
                    matched_app_categories.add(cat)
                cat_orig = APPLICATION_TAG_TO_CATEGORY.get(tag, None)
                if cat_orig:
                    matched_app_categories.add(cat_orig)
                nt_orig_style = nt.replace('-', '_')
                cat2 = APPLICATION_TAG_TO_CATEGORY.get(nt_orig_style, None)
                if cat2:
                    matched_app_categories.add(cat2)

            # 如果没有匹配到任何分类，归入 全球预报
            if not matched_app_categories:
                matched_app_categories.add("全球预报")

            for cat in matched_app_categories:
                application_index[cat][""].add(paper_key)

    return method_index, application_index


def format_paper_row(paper: dict) -> str:
    """生成论文表格行"""
    arxiv = paper['arxiv']
    year = paper['year']
    title = paper['title']
    venue = paper['venue']

    if arxiv:
        title_link = f"[{title}](https://arxiv.org/abs/{arxiv})"
    else:
        title_link = title

    return f"| {year} | {title_link} | {venue} |"


def generate_by_method(method_index: dict) -> str:
    """生成 by-method.md"""
    lines = []
    lines.append("# 按方法分类索引")
    lines.append("")
    lines.append("> AI + 海洋数据同化论文库 · 方法轴分类")
    lines.append("")
    lines.append("---")

    # 按定义顺序输出主分类
    for category in METHOD_HIERARCHY:
        if category not in method_index:
            continue
        cat_papers = method_index[category]
        main_count = len(cat_papers.get("", set()))
        lines.append("")
        lines.append(f"## {category}")
        lines.append(f"> {main_count} 篇论文")
        lines.append("")
        lines.append("| 年份 | 论文 | Venue |")
        lines.append("|------|------|-------|")
        # 获取论文详情并排序
        for paper_key in sorted(cat_papers.get("", set()), key=lambda x: (-int(x.split('/')[0]), x.split('/')[1])):
            year, paper_dir = paper_key.split('/', 1)
            abstract_path = PAPERS_DIR / paper_key / "abstract.md"
            if abstract_path.exists():
                fm = parse_frontmatter(abstract_path.read_text(encoding='utf-8'))
                paper = {
                    'year': year,
                    'title': fm.get('title', paper_dir),
                    'arxiv': fm.get('arXiv', ''),
                    'venue': fm.get('venue', '-'),
                }
                lines.append(format_paper_row(paper))

        # 子分类
        for subcat in METHOD_HIERARCHY[category]:
            sub_papers = cat_papers.get(subcat, set())
            if sub_papers:
                lines.append("")
                lines.append(f"### {category} / {subcat}")
                lines.append(f"> {len(sub_papers)} 篇论文")
                lines.append("")
                lines.append("| 年份 | 论文 | Venue |")
                lines.append("|------|------|-------|")
                for paper_key in sorted(sub_papers, key=lambda x: (-int(x.split('/')[0]), x.split('/')[1])):
                    year, paper_dir = paper_key.split('/', 1)
                    abstract_path = PAPERS_DIR / paper_key / "abstract.md"
                    if abstract_path.exists():
                        fm = parse_frontmatter(abstract_path.read_text(encoding='utf-8'))
                        paper = {
                            'year': year,
                            'title': fm.get('title', paper_dir),
                            'arxiv': fm.get('arXiv', ''),
                            'venue': fm.get('venue', '-'),
                        }
                        lines.append(format_paper_row(paper))

    lines.append("")
    lines.append("---")
    lines.append(f"*最后更新: {date.today()}*")

    return '\n'.join(lines)


def generate_by_application(application_index: dict) -> str:
    """生成 by-application.md"""
    lines = []
    lines.append("# 按应用分类索引")
    lines.append("")
    lines.append("> AI + 海洋数据同化论文库 · 应用轴分类")
    lines.append("")
    lines.append("---")

    # 按定义顺序输出主分类
    for category in APPLICATION_HIERARCHY:
        if category not in application_index:
            continue
        cat_papers = application_index[category]
        main_count = len(cat_papers.get("", set()))
        lines.append("")
        lines.append(f"## {category}")
        lines.append(f"> {main_count} 篇论文")
        lines.append("")
        lines.append("| 年份 | 论文 | Venue |")
        lines.append("|------|------|-------|")
        for paper_key in sorted(cat_papers.get("", set()), key=lambda x: (-int(x.split('/')[0]), x.split('/')[1])):
            year, paper_dir = paper_key.split('/', 1)
            abstract_path = PAPERS_DIR / paper_key / "abstract.md"
            if abstract_path.exists():
                fm = parse_frontmatter(abstract_path.read_text(encoding='utf-8'))
                paper = {
                    'year': year,
                    'title': fm.get('title', paper_dir),
                    'arxiv': fm.get('arXiv', ''),
                    'venue': fm.get('venue', '-'),
                }
                lines.append(format_paper_row(paper))

        # 子分类
        for subcat in APPLICATION_HIERARCHY[category]:
            sub_papers = cat_papers.get(subcat, set())
            if sub_papers:
                lines.append("")
                lines.append(f"### {category} / {subcat}")
                lines.append(f"> {len(sub_papers)} 篇论文")
                lines.append("")
                lines.append("| 年份 | 论文 | Venue |")
                lines.append("|------|------|-------|")
                for paper_key in sorted(sub_papers, key=lambda x: (-int(x.split('/')[0]), x.split('/')[1])):
                    year, paper_dir = paper_key.split('/', 1)
                    abstract_path = PAPERS_DIR / paper_key / "abstract.md"
                    if abstract_path.exists():
                        fm = parse_frontmatter(abstract_path.read_text(encoding='utf-8'))
                        paper = {
                            'year': year,
                            'title': fm.get('title', paper_dir),
                            'arxiv': fm.get('arXiv', ''),
                            'venue': fm.get('venue', '-'),
                        }
                        lines.append(format_paper_row(paper))

    lines.append("")
    lines.append("---")
    lines.append(f"*最后更新: {date.today()}*")

    return '\n'.join(lines)


def main():
    print("扫描论文...")
    method_index, application_index = scan_papers()

    # 计算总论文数（去重）
    all_papers = set()
    for cat_papers in method_index.values():
        all_papers.update(cat_papers.get("", set()))

    print(f"发现 {len(all_papers)} 篇论文")

    print("生成 by-method.md...")
    content = generate_by_method(method_index)
    OUTPUT_METHOD.write_text(content, encoding='utf-8')
    print(f"  -> {OUTPUT_METHOD}")

    print("生成 by-application.md...")
    content = generate_by_application(application_index)
    OUTPUT_APPLICATION.write_text(content, encoding='utf-8')
    print(f"  -> {OUTPUT_APPLICATION}")

    print("完成!")


if __name__ == "__main__":
    main()

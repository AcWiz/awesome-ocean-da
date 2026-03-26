#!/usr/bin/env python3
"""
Translate method_tags and application_tags in README.md and papers/README.md
from English to Chinese, preserving professional terminology.
"""

import argparse
import re
import sys
from pathlib import Path

# Method tags translation map (English -> Chinese)
# Professional terms/abbreviations are NOT translated
METHOD_TAG_TRANSLATIONS = {
    "neural-network": "神经网络",
    "deep-learning": "深度学习",
    "machine-learning": "机器学习",
    "data-assimilation": "数据同化",
    "physics-informed": "物理约束",
    "physics-informed-neural-network": "物理约束神经网络",
    "uncertainty-quantification": "不确定性量化",
    "dynamical-system": "动力学系统",
    "dynamical-systems": "动力学系统",
    "spatio-temporal": "时空",
    "temporal-dispersion": "时间色散",
    "wave-physics": "波浪物理",
    "phase-resolved": "相位解析",
    "prediction": "预测",
    "forecasting": "预报",
    "ocean-modeling": "海洋建模",
    "atmospheric-modeling": "大气建模",
    "hierarchical-mesh": "分层网格",
    "autoregressive": "自回归",
    "multi-scale": "多尺度",
    "ensemble-learning": "集成学习",
    "ensemble-methods": "集成方法",
    "active-learning": "主动学习",
    "meta-learning": "元学习",
    "hyperparameter-optimization": "超参数优化",
    "bayesian-optimization": "贝叶斯优化",
    "graph-neural-network": "图神经网络",
    "neural-ode": "神经ODE",
    "conditional-mean-embedding": "条件均值嵌入",
    "inverse-hessian-approximation": "逆Hessian近似",
    "conjugate-gradient-method": "共轭梯度法",
    "kernel-methods": "核方法",
    "regularization": "正则化",
    "regularisation": "正则化",
    "state-estimation": "状态估计",
    "chaotic-systems": "混沌系统",
    "nonlinear": "非线性",
    "parameterization": "参数化",
    "super-resolution": "超分辨率",
    "eigenvalue-initialisation": "特征值初始化",
    "eigenvalue-initialization": "特征值初始化",
    "climate-forecast": "气候预报",
    "model-correction": "模型纠正",
    "spectral-analysis": "谱分析",
    "multi-agent-rl": "多智能体强化学习",
    "echo-state-network": "回声状态网络",
}

# Application tags translation map (English -> Chinese)
APPLICATION_TAG_TRANSLATIONS = {
    "ocean-forecasting": "海洋预报",
    "ocean-circulation": "海洋环流",
    "ocean-dynamics": "海洋动力学",
    "sea-surface-temperature": "海表温度",
    "sst-forecasting": "海表温度预报",
    "sea-level-prediction": "海平面预测",
    "sea-level": "海平面",
    "sea-ice": "海冰",
    "sea-ice-velocity": "海冰速度",
    "sea-ice-concentration": "海冰浓度",
    "arctic-ocean": "北冰洋",
    "ocean-pollutant": "海洋污染物",
    "advection-diffusion-equation": "平流扩散方程",
    "environmental-monitoring": "环境监测",
    "ocean-front": "海洋锋",
    "classification": "分类",
    "deep-ocean": "深海",
    "swot": "SWOT卫星",
    "argo": "ARGO浮标",
    "mesoscale": "中尺度",
    "ocean-waves": "海浪",
    "wave-prediction": "波浪预测",
    "wave-flume": "波流水槽",
    "nonlinear-waves": "非线性波",
    "ocean-reconstruction": "海洋重构",
    "gulf-of-mexico": "墨西哥湾",
    "satellite-altimetry": "卫星测高",
    "lagrangian-da": "拉格朗日数据同化",
    "sparse-observations": "稀疏观测",
    "canary-current": "加纳利流",
    "upwelling": "上升流",
    "regional-ocean": "区域海洋",
    "marine-ecosystem": "海洋生态系统",
    "baroclinic-wind-driven-ocean": "斜压风驱动海洋",
    "global-ocean": "全球海洋",
    "eddy": "涡旋",
    "ocean-state-prediction": "海洋状态预测",
    "mediterranean-sea": "地中海",
    "temperature": "温度",
    "salinity": "盐度",
    "currents": "海流",
    "flow-modeling": "流场建模",
    "robotics": "机器人",
    "active-sensing": "主动感知",
    "sant-estuarine-system": "圣埃斯皮里图河口系统",
    "variational-data-assimilation": "变分数据同化",
    "numerical-weather-prediction": "数值天气预报",
    "pde-constrained-optimization": "PDE约束优化",
    "weather-prediction": "天气预报",
    "climate-modeling": "气候建模",
    "geophysical-fluid-dynamics": "地球物理流体力学",
    "coastline-approximation": "海岸线近似",
    "jet-strengthening": "射流强化",
    "coastal-hypoxia-forecasting": "海岸缺氧预报",
    "environmental-ai": "环境AI",
    "submesoscale": "亚中尺度",
    "climate": "气候",
    "carbon-storage": "碳储存",
    "ocean-atmosphere": "海气耦合",
    "regional-forecast": "区域预报",
    "pacific": "太平洋",
    "weather": "天气",
    "global": "全球",
    "wave": "海浪",
    "global-forecast": "全球预报",
    "ocean-da": "海洋数据同化",
    "satellite-obs": "卫星观测",
    "ocean": "海洋",
    "underwater-acoustics": "水下声学",
    "pde": "偏微分方程",
    "ocean-observations": "海洋观测",
}


def translate_tag(tag, translation_map):
    """Translate a single tag using the translation map."""
    tag_lower = tag.lower().strip()
    if tag_lower in translation_map:
        return translation_map[tag_lower]
    return tag


def translate_tag_list(tag_string, translation_map):
    """Translate a comma-separated list of tags."""
    if not tag_string or tag_string.strip() == "":
        return tag_string

    tags = [t.strip() for t in tag_string.split(",")]
    translated_tags = []
    for tag in tags:
        if not tag:
            continue
        translated = translate_tag(tag, translation_map)
        translated_tags.append(translated)
    return ", ".join(translated_tags)


def is_separator_row(line):
    """Check if line is a markdown table separator row."""
    stripped = line.strip()
    if not (stripped.startswith("|") and stripped.endswith("|")):
        return False

    # Remove leading/trailing | and split
    inner = stripped[1:-1]
    cells = [c.strip() for c in inner.split("|")]

    # A separator row has cells that are either empty or contain only -, :, spaces
    for cell in cells:
        if cell and not re.match(r'^[-:\s]+$', cell):
            return False
    return True


def is_table_row(line):
    """Check if line is a markdown table data row (starts and ends with |)."""
    stripped = line.strip()
    return stripped.startswith("|") and stripped.endswith("|")


def translate_cell_tags(cell, translation_needed):
    """Translate tags in a cell if needed."""
    if not translation_needed:
        return cell

    # First translate method tags, then application tags
    translated = translate_tag_list(cell, METHOD_TAG_TRANSLATIONS)
    translated = translate_tag_list(translated, APPLICATION_TAG_TRANSLATIONS)
    return translated


def process_file(file_path, dry_run=False, verbose=False):
    """Process a single markdown file and translate tags in tables."""
    if verbose:
        print(f"Processing: {file_path}")

    content = file_path.read_text(encoding="utf-8")
    original_content = content

    lines = content.split("\n")
    new_lines = []

    for line in lines:
        # Keep separator rows as-is
        if is_separator_row(line):
            new_lines.append(line)
            continue

        # Only process lines that look like table rows
        if not is_table_row(line):
            new_lines.append(line)
            continue

        # Parse the table row
        stripped = line.strip()
        inner = stripped[1:-1]  # Remove leading | and trailing |
        cells = [c.strip() for c in inner.split("|")]

        # Check if any cell needs translation
        new_cells = []
        any_translated = False

        for cell in cells:
            # Check if this cell contains tags that need translation
            needs_trans = False
            cell_lower = cell.lower()
            for tag_map in [METHOD_TAG_TRANSLATIONS, APPLICATION_TAG_TRANSLATIONS]:
                for eng_tag in tag_map:
                    if eng_tag in cell_lower:
                        needs_trans = True
                        break
                if needs_trans:
                    break

            if needs_trans:
                translated = translate_cell_tags(cell, True)
                new_cells.append(translated)
                if translated != cell:
                    any_translated = True
            else:
                new_cells.append(cell)

        # Reconstruct the line
        leading_ws = len(line) - len(line.lstrip())
        trailing_ws = len(line) - len(line.rstrip())
        new_line = " " * leading_ws + "|" + "|".join(new_cells) + "|" + " " * trailing_ws

        if any_translated:
            if verbose:
                print(f"  Translated: {cells[:3]}...")
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    new_content = "\n".join(new_lines)

    if new_content != original_content:
        if dry_run:
            if verbose:
                print(f"  [DRY RUN] Would update: {file_path}")
        else:
            file_path.write_text(new_content, encoding="utf-8")
            if verbose:
                print(f"  [UPDATED]: {file_path}")
        return True
    else:
        if verbose:
            print(f"  [NO CHANGE]: {file_path}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Translate tags in README files")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    args = parser.parse_args()

    # Files to process
    base_path = Path(__file__).parent.parent.parent
    files_to_process = [
        base_path / "README.md",
        base_path / "papers" / "README.md",
    ]

    print(f"{'='*60}")
    print(f"Tag Translation Script")
    print(f"{'='*60}")
    if args.dry_run:
        print("Mode: DRY RUN (no changes will be written)")
    else:
        print("Mode: LIVE (changes will be written)")
    print(f"{'='*60}\n")

    total_changes = 0
    for file_path in files_to_process:
        if file_path.exists():
            changed = process_file(file_path, dry_run=args.dry_run, verbose=args.verbose)
            if changed:
                total_changes += 1
        else:
            if args.verbose:
                print(f"  [SKIP] File not found: {file_path}")

    print(f"\n{'='*60}")
    if args.dry_run:
        print(f"Dry run complete. {total_changes} file(s) would be modified.")
    else:
        print(f"Complete. {total_changes} file(s) modified.")
    print(f"{'='*60}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

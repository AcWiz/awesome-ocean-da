#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量迁移 abstract.md，添加 YAML front matter"""

import os
import re
import yaml
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent
PAPERS_DIR = PROJECT_ROOT / "papers"


# 预定义论文元数据（从现有 abstract.md 和目录结构提取）
PAPER_METADATA = {
    "2024/FuXi-DA": {
        "title": "FuXi-DA: A Generalized Deep Learning Data Assimilation Framework",
        "arXiv": "2404.08522",
        "authors": ["Xiaoze Xu", "Xiuyu Sun", "Wei Han", "Xiaohui Zhong", "Lei Chen", "Hao Li"],
        "method_tags": ["Deep-Learning", "Transformer"],
        "application_tags": ["Ocean-DA", "Global-Forecast"],
    },
    "2025/Tensor-Var": {
        "title": "Tensor-Var: Efficient Four-Dimensional Variational Data Assimilation",
        "arXiv": "2501.13312",
        "authors": ["Yiming Yang", "et al."],
        "method_tags": ["4D-Var", "Neural-Operator"],
        "application_tags": ["Ocean-DA", "Global-Forecast"],
    },
    "2025/Stratified_PINN_DA": {
        "title": "Stratified PINN for Deep Ocean Data Assimilation",
        "arXiv": "2503.19160",
        "authors": ["Limousin", "et al."],
        "method_tags": ["PINN"],
        "application_tags": ["Deep-Ocean"],
    },
    "2025/AI_GCS_DA": {
        "title": "AI for Geological Carbon Storage Data Assimilation",
        "arXiv": None,
        "authors": ["Seabra", "et al."],
        "method_tags": ["Deep-Learning"],
        "application_tags": ["Carbon-Storage"],
    },
    "2024/CGKN": {
        "title": "CGKN: Conditional Gaussian Koopman Network",
        "arXiv": "2410.20072",
        "authors": ["Chuanqi Chen", "et al."],
        "method_tags": ["Koopman", "Neural-Operator"],
        "application_tags": ["Ocean-DA"],
    },
    "2023/Echo_State_DA": {
        "title": "Echo State Network for Data Assimilation",
        "arXiv": "2304.00198",
        "authors": [],
        "method_tags": ["ESN"],
        "application_tags": ["Ocean-DA"],
    },
    "2024/Semilinear_Neural_Operators": {
        "title": "Semilinear Neural Operators for Ocean Forecasting",
        "arXiv": "2402.15656",
        "authors": ["Singh", "et al."],
        "method_tags": ["Neural-Operator"],
        "application_tags": ["Global-Forecast"],
    },
    "2025/Subregional_Ocean_Forecasting": {
        "title": "Subregional Ocean Forecasting with Deep Learning",
        "arXiv": "2505.24429",
        "authors": ["Cuervo-Londono", "et al."],
        "method_tags": ["Deep-Learning", "GNN"],
        "application_tags": ["Regional-Forecast"],
    },
    "2024/Tropical_Pacific_Ocean_DA": {
        "title": "Tropical Pacific Ocean Data Assimilation",
        "arXiv": "2406.07063",
        "authors": ["Meng", "et al."],
        "method_tags": ["EnKF"],
        "application_tags": ["Ocean-DA", "ENSO"],
    },
    "2023/Graph_SST_Forecast": {
        "title": "Graph Neural Network for SST Forecasting",
        "arXiv": "2305.09468",
        "authors": ["Ning", "et al."],
        "method_tags": ["GNN"],
        "application_tags": ["SST", "Global-Forecast"],
    },
    "2025/ORCAst": {
        "title": "ORCAst: Operational High-Resolution Current Forecasts",
        "arXiv": "2501.12054",
        "authors": ["Garcia", "et al."],
        "method_tags": ["Deep-Learning"],
        "application_tags": ["Global-Forecast", "Ocean-DA"],
    },
    "2025/NeuralOM": {
        "title": "NeuralOM: Neural Ocean Model for S2S Simulation",
        "arXiv": "2505.21020",
        "authors": ["Gao", "et al."],
        "method_tags": ["Neural-Operator"],
        "application_tags": ["Global-Forecast"],
    },
    "2025/Neural_Ocean_Forecasting": {
        "title": "Neural Ocean Forecasting",
        "arXiv": "2512.22152",
        "authors": [],
        "method_tags": ["Deep-Learning"],
        "application_tags": ["Global-Forecast"],
    },
    "2024/OceanCastNet_Wave_Forecasting": {
        "title": "OceanCastNet: Wave Forecasting Network",
        "arXiv": "2406.03848",
        "authors": [],
        "method_tags": ["Deep-Learning", "GNN"],
        "application_tags": ["Wave"],
    },
    "2024/koopman-based-deep-learning-nonlinear-system-estimation": {
        "title": "Koopman-based Deep Learning for Nonlinear System Estimation",
        "arXiv": "2405.00627",
        "authors": [],
        "method_tags": ["Koopman"],
        "application_tags": ["Ocean-DA"],
    },
    "2022/4D-SRDA": {
        "title": "4D-SRDA: Spatio-Temporal Super-Resolution Data Assimilation",
        "arXiv": "2212.03656",
        "authors": ["Yasuda", "et al."],
        "method_tags": ["4D-Var"],
        "application_tags": ["Ocean-DA", "Global-Forecast"],
    },
    "2022/Ocean_Observations_Expansion": {
        "title": "Ocean Observations Expansion with Deep Learning",
        "arXiv": "2206.01599",
        "authors": ["Muhamed", "et al."],
        "method_tags": ["Deep-Learning"],
        "application_tags": ["Ocean-DA"],
    },
    "2022/deep-learning-enhanced-ensemble-based-data-assimilation": {
        "title": "Deep Learning Enhanced Ensemble-based Data Assimilation",
        "arXiv": "2206.04811",
        "authors": [],
        "method_tags": ["EnKF", "Deep-Learning"],
        "application_tags": ["Ocean-DA"],
    },
    "2024/conditional-gaussian-ensemble-kalman-filtering": {
        "title": "Conditional Gaussian Ensemble Kalman Filtering",
        "arXiv": "2409.14300",
        "authors": [],
        "method_tags": ["EnKF"],
        "application_tags": ["Ocean-DA"],
    },
    "2024/validating-deep-learning-weather-forecast-models": {
        "title": "Validating Deep Learning Weather Forecast Models",
        "arXiv": "2404.17652",
        "authors": [],
        "method_tags": ["Deep-Learning"],
        "application_tags": ["Global-Forecast"],
    },
    "2024/neural-network-submesoscale-vertical-heat-flux": {
        "title": "Neural Network for Submesoscale Vertical Heat Flux",
        "arXiv": None,
        "authors": [],
        "method_tags": ["Deep-Learning", "Neural-Network"],
        "application_tags": ["Submesoscale"],
    },
    "2025/recursive-kalman-net": {
        "title": "Recursive Kalman Net",
        "arXiv": None,
        "authors": [],
        "method_tags": ["EnKF", "Deep-Learning"],
        "application_tags": ["Ocean-DA"],
    },
    "2025/deep-learning-subregional-ocean-forecasting-canary-current": {
        "title": "Deep Learning Subregional Ocean Forecasting: Canary Current",
        "arXiv": "2505.24429",
        "authors": [],
        "method_tags": ["Deep-Learning", "GNN"],
        "application_tags": ["Regional-Forecast"],
    },
    "2025/stratified-physics-informed-neural-network-data-assimilation": {
        "title": "Stratified Physics-Informed Neural Network Data Assimilation",
        "arXiv": "2503.19160",
        "authors": [],
        "method_tags": ["PINN"],
        "application_tags": ["Deep-Ocean", "Ocean-DA"],
    },
    "2024/Deep_Learning_Weather_Models_Subregional_Ocean_Forecasting": {
        "title": "Deep Learning Weather Models for Subregional Ocean Forecasting",
        "arXiv": None,
        "authors": [],
        "method_tags": ["Deep-Learning"],
        "application_tags": ["Regional-Forecast"],
    },
    "2024/Deep_Learning_Model_Correction_Dynamical_Systems": {
        "title": "Deep Learning Model Correction for Dynamical Systems",
        "arXiv": None,
        "authors": [],
        "method_tags": ["Deep-Learning", "Surrogate"],
        "application_tags": ["Global-Forecast"],
    },
    "2024/Deep_Learning_ENSO_Forecast": {
        "title": "Deep Learning for ENSO Forecast",
        "arXiv": None,
        "authors": [],
        "method_tags": ["Deep-Learning"],
        "application_tags": ["ENSO"],
    },
    "2024/DUNE_Climate_Forecasting": {
        "title": "DUNE: Deep Unstructured Neural Environment for Climate Forecasting",
        "arXiv": None,
        "authors": [],
        "method_tags": ["Deep-Learning"],
        "application_tags": ["Climate", "Global-Forecast"],
    },
    "2024/Deep_Koopman_Learning_Noisy_Data": {
        "title": "Deep Koopman Learning from Noisy Data",
        "arXiv": "2405.16649",
        "authors": [],
        "method_tags": ["Koopman"],
        "application_tags": ["Ocean-DA"],
    },
    "2022/Scientific_Machine_Learning_PINN": {
        "title": "Scientific Machine Learning and PINN",
        "arXiv": None,
        "authors": [],
        "method_tags": ["PINN"],
        "application_tags": ["Ocean-DA"],
    },
    "2022/Physics_Informed_Deep_Neural_Operator_Networks": {
        "title": "Physics-Informed Deep Neural Operator Networks",
        "arXiv": None,
        "authors": [],
        "method_tags": ["PINN", "Neural-Operator"],
        "application_tags": ["Ocean-DA"],
    },
    "2025/SamudrACE_Coupled_Climate_Modeling": {
        "title": "SamudrACE: Coupled Climate Modeling",
        "arXiv": None,
        "authors": [],
        "method_tags": ["Deep-Learning", "Hybrid"],
        "application_tags": ["Climate", "Global-Forecast"],
    },
    "2024/Continuous_Data_Assimilation_Turbulence_Models": {
        "title": "Continuous Data Assimilation for Turbulence Models",
        "arXiv": None,
        "authors": [],
        "method_tags": ["Deep-Learning"],
        "application_tags": ["Submesoscale", "Ocean-DA"],
    },
    "2024/LangYa_Cross_Spatiotemporal_Ocean_Forecasting": {
        "title": "LangYa: Cross-Spatiotemporal Ocean Forecasting",
        "arXiv": None,
        "authors": [],
        "method_tags": ["Deep-Learning", "Transformer"],
        "application_tags": ["Wave", "Global-Forecast"],
    },
    "2025/CTP_Hybrid_Ocean_Front_Forecasting": {
        "title": "CTP Hybrid Ocean Front Forecasting",
        "arXiv": None,
        "authors": [],
        "method_tags": ["Deep-Learning", "Hybrid"],
        "application_tags": ["Regional-Forecast"],
    },
    "2025/Enhanced_State_Estimation_Turbulent_Flows_DA_ML": {
        "title": "Enhanced State Estimation for Turbulent Flows with DA and ML",
        "arXiv": None,
        "authors": [],
        "method_tags": ["Deep-Learning", "EnKF"],
        "application_tags": ["Submesoscale", "Ocean-DA"],
    },
    "2024/Machine_Learning_Inverse_Problems_DA": {
        "title": "Machine Learning for Inverse Problems in Data Assimilation",
        "arXiv": None,
        "authors": [],
        "method_tags": ["Deep-Learning"],
        "application_tags": ["Ocean-DA"],
    },
    "2025/Neural_Network_Mesoscale_Eddies_Parameterization": {
        "title": "Neural Network for Mesoscale Eddies Parameterization",
        "arXiv": None,
        "authors": [],
        "method_tags": ["Deep-Learning", "Neural-Network"],
        "application_tags": ["Submesoscale"],
    },
    "2024/Randomized_PINN_Bayesian_DA": {
        "title": "Randomized PINN for Bayesian Data Assimilation",
        "arXiv": None,
        "authors": [],
        "method_tags": ["PINN", "Bayesian"],
        "application_tags": ["Ocean-DA"],
    },
    "2021/Sub-seasonal_Forecasting_Deep_Learning_Weather_Prediction": {
        "title": "Sub-seasonal Forecasting with Deep Learning Weather Prediction",
        "arXiv": None,
        "authors": [],
        "method_tags": ["Deep-Learning"],
        "application_tags": ["Global-Forecast", "Climate"],
    },
}


def get_year_from_path(path: str) -> int:
    """从路径提取年份"""
    match = re.search(r'(\d{4})', path)
    if match:
        return int(match.group(1))
    return datetime.now().year


def add_front_matter(content: str, metadata: dict) -> str:
    """添加 YAML front matter"""
    # 检查是否已有 front matter
    if content.startswith('---'):
        return content

    front_matter = {
        'title': metadata.get('title', 'Untitled'),
        'arXiv': metadata.get('arXiv'),
        'authors': metadata.get('authors', []),
        'year': metadata.get('year', get_year_from_path(metadata.get('path', ''))),
        'source': 'arXiv' if metadata.get('arXiv') else 'other',
        'method_tags': metadata.get('method_tags', []),
        'application_tags': metadata.get('application_tags', []),
        'date_collected': metadata.get('date_collected', datetime.now().strftime('%Y-%m-%d')),
    }

    # 移除 None 值
    front_matter = {k: v for k, v in front_matter.items() if v is not None}

    yaml_str = yaml.dump(front_matter, allow_unicode=True, default_flow_style=False, sort_keys=False)
    return f"---\n{yaml_str}---\n\n{content}"


def migrate_file(file_path: Path, metadata: dict) -> bool:
    """迁移单个文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查是否已有 front matter
        if content.startswith('---'):
            print(f"  跳过（已有 front matter）: {file_path.name}")
            return False

        # 添加 front matter
        metadata['path'] = str(file_path)
        metadata['year'] = metadata.get('year') or get_year_from_path(str(file_path))

        new_content = add_front_matter(content, metadata)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"  更新: {file_path.name}")
        return True

    except Exception as e:
        print(f"  错误: {file_path.name} - {e}")
        return False


def main():
    """批量迁移"""
    print("开始迁移 abstract.md 文件...")
    print("=" * 50)

    updated = 0
    skipped = 0

    for abstract_path in PAPERS_DIR.glob("**/abstract.md"):
        # 计算相对路径用于查找元数据
        rel_path = abstract_path.relative_to(PAPERS_DIR)
        rel_path_str = str(rel_path).replace('\\', '/')

        # 尝试匹配元数据
        metadata = None

        # 精确匹配
        if rel_path_str in PAPER_METADATA:
            metadata = PAPER_METADATA[rel_path_str]
        else:
            # 尝试年份+目录名匹配
            parts = rel_path_str.split('/')
            if len(parts) >= 2:
                key = f"{parts[0]}/{parts[1]}"
                if key in PAPER_METADATA:
                    metadata = PAPER_METADATA[key]

        if metadata:
            if migrate_file(abstract_path, metadata):
                updated += 1
            else:
                skipped += 1
        else:
            # 使用默认元数据
            default_metadata = {
                'title': rel_path.parent.name.replace('_', ' '),
                'year': get_year_from_path(rel_path_str),
                'method_tags': ['Deep-Learning'],
                'application_tags': ['Ocean-DA'],
            }
            if migrate_file(abstract_path, default_metadata):
                updated += 1
            else:
                skipped += 1

    print("=" * 50)
    print(f"迁移完成: {updated} 更新, {skipped} 跳过")


if __name__ == "__main__":
    main()

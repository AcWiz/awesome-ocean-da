# -*- coding: utf-8 -*-
"""标签配置和映射"""

# 标签别名映射（规范化后的别名 → 主标签）
TAG_ALIASES = {
    # PINN 别名
    "physics-informed-neural-networks": "pinn",
    "physics-informed-neural-network": "pinn",
    "physics-informed": "pinn",
    "physics-informed-ml": "pinn",
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
    "koopman-autoencoder": "koopman",
}


def get_canonical_tag(normalized_tag: str) -> str:
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
    # Ocean DA
    "ocean-da": ("海洋数据同化 (Ocean DA)", "ocean-da.md"),
    "ocean-data-assimilation": ("海洋数据同化 (Ocean DA)", "ocean-da.md"),
}

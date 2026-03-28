# -*- coding: utf-8 -*-
"""Classification configuration for dual-section structure: 数据同化 vs 预报"""

# Keywords for 数据同化 (Data Assimilation) category
ASSIMILATION_METHOD_KEYWORDS = {
    'data-assimilation', '4d-var', 'enkf', 'variational',
    'ensemble-kalman', 'kalman-filter', 'koopman', 'pinn'
}
ASSIMILATION_APP_KEYWORDS = {
    'data-assimilation', 'reconstruction', 'state-estimation'
}

# Keywords for 海洋预报 (Ocean Forecasting) category
FORECAST_METHOD_KEYWORDS = {
    'neural-operator', 'fno', 'gnn', 'transformer', 'lstm',
    'forecasting', 'prediction'
}
FORECAST_APP_KEYWORDS = {
    'forecasting', 'prediction', 'sst-forecasting'
}

# Sub-categories for 数据同化方法 section
ASSIMILATION_SUBTAGS = {
    '4d-var': ('4D-Var / EnKF', '4d-var.md'),
    'enkf': ('4D-Var / EnKF', '4d-var.md'),
    'variational': ('4D-Var / EnKF', '4d-var.md'),
    'ensemble-kalman': ('4D-Var / EnKF', '4d-var.md'),
    'kalman-filter': ('4D-Var / EnKF', '4d-var.md'),
    'koopman': ('Koopman 学习', 'koopman.md'),
    'pinn': ('PINN (数据同化方向)', 'pinn.md'),
    'physics-informed-neural-networks': ('PINN (数据同化方向)', 'pinn.md'),
    'physics-informed': ('PINN (数据同化方向)', 'pinn.md'),
}

# Sub-categories for 海洋预报方法 section
FORECAST_SUBTAGS = {
    'neural-operator': ('神经算子 (FNO)', 'neural-operator.md'),
    'fno': ('神经算子 (FNO)', 'neural-operator.md'),
    'fourier-neural-operator': ('神经算子 (FNO)', 'neural-operator.md'),
    'gnn': ('图神经网络 (GNN)', 'gnn.md'),
    'graph-neural-network': ('图神经网络 (GNN)', 'gnn.md'),
    'transformer': ('Transformer / Attention', 'transformer.md'),
    'lstm': ('LSTM', 'lstm.md'),
    'forecasting': ('预报基础方法', 'forecasting.md'),
    'prediction': ('预报基础方法', 'forecasting.md'),
}

ASSIMILATION_SUBTAG_DESCS = {
    '4d-var': '变分数据同化方法，通过最小化目标函数估计最优状态',
    'enkf': '集合卡尔曼滤波方法，通过集合采样估计状态均值和协方差',
    'variational': '变分数据同化方法，通过最小化目标函数估计最优状态',
    'ensemble-kalman': '集合卡尔曼滤波方法，通过集合采样估计状态均值和协方差',
    'kalman-filter': '卡尔曼滤波及其扩展方法，递归最优估计',
    'koopman': '通过全局线性动力学近似捕捉非线性系统演化',
    'pinn': '将物理约束嵌入神经网络 Loss，强制解满足物理定律（数据同化方向）',
    'physics-informed-neural-networks': '将物理约束嵌入神经网络 Loss，强制解满足物理定律（数据同化方向）',
    'physics-informed': '将物理约束嵌入神经网络 Loss，强制解满足物理定律（数据同化方向）',
}

FORECAST_SUBTAG_DESCS = {
    'neural-operator': '学习解算子映射，无网格约束的偏微分方程求解',
    'fno': '傅里叶神经算子，利用 FFT 加速卷积操作',
    'fourier-neural-operator': '傅里叶神经算子，利用 FFT 加速卷积操作',
    'gnn': '利用图结构建模海洋要素间的空间依赖关系',
    'graph-neural-network': '利用图结构建模海洋要素间的空间依赖关系',
    'transformer': '利用自注意力机制捕捉长距离依赖关系',
    'lstm': '长短期记忆网络，处理时序依赖关系',
    'forecasting': '时序预测与 forecasting 相关基础方法',
    'prediction': '时序预测与 prediction 相关基础方法',
}

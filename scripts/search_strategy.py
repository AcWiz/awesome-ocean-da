# -*- coding: utf-8 -*-
"""搜索策略配置 - AI+海洋数据同化论文搜集"""

from typing import List, Dict

# 方法类型标签及其对应关键词
METHOD_TAGS = {
    "PINN": ["physics-informed", "PINN", "physics constrained", "physics-constrained"],
    "Koopman": ["Koopman", "koopman"],
    "Neural-Operator": ["Fourier neural operator", "FNO", "neural operator", "CGKN", "operator learning"],
    "GNN": ["graph neural network", "GNN", "graph network", "graph convolution"],
    "Transformer": ["transformer", "attention", "attention mechanism", "self-attention"],
    "LSTM": ["LSTM", "long short-term"],
    "U-Net": ["U-Net", "u-net", "encoder-decoder"],
    "EnKF": ["Kalman filter", "ensemble Kalman", "EnKF", "ESMDA", "localization"],
    "4D-Var": ["4D-Var", "4DVar", "variational", "inverse", "minimization"],
    "ESN": ["echo state", "reservoir computing", "echo-state"],
    "CVAE": ["variational autoencoder", "VAE", "CVAE", "generative model"],
    "Surrogate": ["surrogate model", "emulator", "fast model"],
    "Hybrid": ["hybrid", "coupled", "data-driven"],
}

# 应用场景标签及其对应关键词
APPLICATION_TAGS = {
    "Global-Forecast": ["global ocean", "global forecast", "world ocean", "basin-scale"],
    "Regional-Forecast": ["regional ocean", "coastal", "regional forecast", "subregional"],
    "SST": ["sea surface temperature", "SST", "sea temperature"],
    "SSH": ["sea surface height", "SSH", "sea level"],
    "ENSO": ["ENSO", "El Nino", "La Nina", "El Niño", "Southern Oscillation"],
    "Deep-Ocean": ["deep ocean", "subsurface", "abyss", "deep-sea", "stratified"],
    "Wave": ["wave", "swell", "wave height", "ocean wave"],
    "Tidal": ["tidal", "tide", "harmonics"],
    "Submesoscale": ["submesoscale", "mesoscale", "eddy"],
    "Carbon-Storage": ["carbon storage", "carbon sequestration", "GCS", "geological carbon"],
    "Climate": ["climate", "climate model", "coupled model"],
    "Ocean-DA": ["data assimilation", "state estimation", "reanalysis"],
}

# arXiv 分类筛选
ARXIV_CATEGORIES = [
    "cs.LG",
    "physics.ao-ph",  # Atmospheric and Oceanic Physics
    "stat.ML",
    "math.DS",  # Dynamical Systems
]

# 搜索查询语句（arXiv API 格式）
SEARCH_QUERIES = [
    # 核心数据同化 + 深度学习
    'all:"data assimilation" AND all:"deep learning" AND all:"ocean"',
    'all:"data assimilation" AND all:"neural network" AND all:"ocean"',
    'all:"ocean" AND all:"state estimation" AND (all:"neural" OR all:"learning")',

    # PINN 应用
    'all:"PINN" AND all:"ocean"',
    'all:"physics-informed" AND all:"neural network" AND all:"ocean"',

    # Koopman 方法
    'all:"Koopman" AND all:"ocean"',
    'all:"Koopman" AND all:"data assimilation"',

    # 神经算子
    'all:"neural operator" AND all:"ocean"',
    'all:"Fourier neural operator" AND all:"ocean"',
    'all:"FNO" AND all:"ocean"',

    # 海面温度/高度预测
    'all:"sea surface temperature" AND all:"deep learning"',
    'all:"sea surface height" AND all:"neural network"',
    'all:"SST" AND all:"forecast" AND all:"learning"',

    # 海洋预报
    'all:"ocean forecast" AND all:"deep learning"',
    'all:"ocean prediction" AND all:"neural"',
    'all:"ocean modeling" AND all:"machine learning"',

    # 图神经网络
    'all:"graph neural network" AND all:"ocean"',
    'all:"GNN" AND all:"ocean"',

    # 海洋数据同化（通用）
    'all:"ocean data assimilation" AND all:"neural"',
    'all:"ensemble Kalman" AND all:"ocean"',
    'all:"4D-Var" AND all:"ocean"',

    # ENSO 预测
    'all:"ENSO" AND all:"deep learning"',
    'all:"El Nino" AND all:"neural network"',

    # 深海/次表层
    'all:"deep ocean" AND all:"neural"',
    'all:"subsurface" AND all:"data assimilation" AND all:"learning"',

    # 海洋模式/模拟
    'all:"ocean model" AND all:"learning"',
    'all:"numerical ocean" AND all:"neural network"',
]

# 排除关键词（减少噪声）
EXCLUDE_TERMS = [
    "radar",
    "acoustic",
    "acoustic wave",
    "fishing",
    "biology",
    "marine biology",
    "coral",
    "plankton",
    "whale",
    "fish species",
    "aquaculture",
    "sonar",
    "seismic",
    "underwater communication",
]

# 顶会/期刊来源配置
VENUE_SOURCES = {
    "NeurIPS": ["NeurIPS", "Neural Information Processing Systems"],
    "ICML": ["ICML", "International Conference on Machine Learning"],
    "ICLR": ["ICLR", "International Conference on Learning Representations"],
    "KDD": ["KDD", "Knowledge Discovery and Data Mining"],
    "Nature": ["Nature", "Nature Climate Change", "Nature Geoscience"],
    "Science": ["Science"],
    "GRL": ["Geophysical Research Letters", "GRL"],
    "JGR": ["Journal of Geophysical Research", "JGR"],
    "Ocean-Modelling": ["Ocean Modelling"],
    "JC": ["Journal of Climate"],
}

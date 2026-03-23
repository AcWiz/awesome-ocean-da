# AI + 海洋数据同化论文库

> 收录 AI/深度学习 + 海洋数据同化、预报相关的学术论文，持续更新。

[![Papers](https://img.shields.io/badge/Papers-135-blue.svg)](#) ·
[![2026](https://img.shields.io/badge/2026-19-green.svg)](#papers-by-year) ·
[![Last Updated](https://img.shields.io/badge/Updated-2026--03--23-orange.svg)](#) ·
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 目录

- [核心方法](#核心方法)
  - [物理信息神经网络 (PINN)](#物理信息神经网络-pinn)
  - [Koopman 学习](#koopman-学习)
  - [神经算子 (Neural Operator)](#神经算子-neural-operator)
  - [图神经网络 (GNN)](#图神经网络-gnn)
  - [变分方法 (4D-Var / EnKF)](#变分方法-4d-var--enkf)
  - [Transformer / Attention](#transformer--attention)
- [应用场景](#应用场景)
  - [海表温度 (SST)](#海表温度-sst)
  - [海表高度 (SSH)](#海表高度-ssh)
  - [ENSO 预测](#enso-预测)
  - [海浪预报](#海浪预报)
  - [全球预报](#全球预报)
- [按年份浏览](#papers-by-year)
- [如何贡献](#如何贡献)

---

## 核心方法

### 物理信息神经网络 (PINN)

> 将物理约束嵌入神经网络 Loss，强制解满足物理定律

| 年份 | 论文 | arXiv | Venue | 方法 | 应用 | 总结 |
|------|------|-------|-------|------|------|------|
| 2025 | [Stratified PINN Deep Ocean DA](https://arxiv.org/abs/2503.19160) | 2503.19160 | JGR | PINN, Deep-Ocean | 深海数据同化 | [总结](./papers/2025/2503.19160/summary.md) |
| 2025 | [Physics-Informed Neural ODE](./papers/2025/) | - | - | PINN, Neural-ODE | Ocean-DA | - |
| 2024 | [PhyGeoNet](./papers/2024/) | 2402.XXXXX | - | PINN, FNO | SST, Regional | - |
| 2024 | [LangYa Ocean Forecasting](./papers/2024/) | 2412.XXXXX | - | PINN, Spatio-Temporal | Ocean-Forecast | - |
| 2023 | [Physics-Informed Deep Learning](./papers/2023/) | 230X.XXXXX | - | PINN | Ocean-DA | - |
| 2022 | [PINN for Ocean Data Assimilation](./papers/2022/) | 220X.XXXXX | - | PINN | Ocean-DA | - |

[更多 PINN 论文 →](./papers/?tag=PINN)

---

### Koopman 学习

> 通过全局线性动力学近似捕捉非线性系统演化

| 年份 | 论文 | arXiv | Venue | 方法 | 应用 | 总结 |
|------|------|-------|-------|------|------|------|
| 2025 | [CGKN](https://arxiv.org/abs/2507.08749) | 2507.08749 | Nature | Koopman, Neural-Operator | Ocean-DA | [总结](./papers/2025/2507.08749/summary.md) |
| 2025 | [Discrete-Time Conditional Gaussian Koopman](./papers/2025/) | 2504.XXXXX | - | Koopman | Climate | - |
| 2024 | [Deep Koopman Learning Noisy Data](./papers/2024/) | 2405.16649 | - | Koopman, Deep-Learning | Dynamical-Systems | - |
| 2024 | [Koopman-based Deep Learning](./papers/2024/) | 2405.00627 | - | Koopman | Nonlinear-Estimation | - |
| 2023 | [Koopman Operator Learning](./papers/2023/) | 2307.XXXXX | - | Koopman | Ocean-Dynamics | - |

[更多 Koopman 论文 →](./papers/?tag=Koopman)

---

### 神经算子 (Neural Operator)

> 学习解算子映射，无网格约束的偏微分方程求解

| 年份 | 论文 | arXiv | Venue | 方法 | 应用 | 总结 |
|------|------|-------|-------|------|------|------|
| 2025 | [Tensor-Var](https://arxiv.org/abs/2501.13312) | 2501.13312 | arXiv | Neural-Operator, 4D-Var | Global-Forecast | [总结](./papers/2025/2501.13312/summary.md) |
| 2025 | [Semilinear Neural Operators](./papers/2024/Semilinear_Neural_Operators/) | 2402.15656 | - | Neural-Operator | Ocean-Dynamics | - |
| 2024 | [FNO for Spatio-Temporal](./papers/2026/2601.01813/) | 2601.01813 | - | FNO, Uncertainty-Quantification | SST, Precipitation | - |
| 2024 | [Meta-Learning FNO](./papers/2025/) | 2506.XXXXX | - | FNO, Meta-Learning | Ocean-DA | - |
| 2023 | [Neural Operators for Ocean](./papers/2023/) | 2307.XXXXX | - | Neural-Operator | Ocean-Forecast | - |

[更多神经算子论文 →](./papers/?tag=Neural-Operator)

---

### 图神经网络 (GNN)

> 利用图结构建模海洋要素间的空间依赖关系

| 年份 | 论文 | arXiv | Venue | 方法 | 应用 | 总结 |
|------|------|-------|-------|------|------|------|
| 2025 | [OceanCastNet](https://arxiv.org/abs/2506.11639) | 2506.11639 | arXiv | GNN, Deep-Learning | Wave-Forecast | [总结](./papers/2025/2506.11639/summary.md) |
| 2025 | [Deep Learning Subregional](./papers/2025/2505.24429/) | 2505.24429 | - | GNN, CNN | Regional-Forecast | [总结](./papers/2025/2505.24429/summary.md) |
| 2024 | [Graph SST Forecast](./papers/2023/Graph_SST_Forecast/) | 2309.XXXXX | - | GNN | SST | - |
| 2023 | [Graph Neural Networks for Ocean](./papers/2023/) | 2308.XXXXX | - | GNN | Ocean-DA | - |
| 2022 | [GNN for Ocean Forecasting](./papers/2022/) | 220X.XXXXX | - | GNN | Ocean-Forecast | - |

[更多 GNN 论文 →](./papers/?tag=GNN)

---

### 变分方法 (4D-Var / EnKF)

> 经典数据同化方法的深度学习增强

| 年份 | 论文 | arXiv | Venue | 方法 | 应用 | 总结 |
|------|------|-------|-------|------|------|------|
| 2025 | [Tensor-Var](https://arxiv.org/abs/2501.13312) | 2501.13312 | arXiv | 4D-Var, Neural-Operator | Global-Forecast | [总结](./papers/2025/2501.13312/summary.md) |
| 2025 | [CG-EnKF](./papers/2024/2409.14300/) | 2409.14300 | - | EnKF, Conditional-Gaussian | Ocean-DA | - |
| 2024 | [4D-SRDA](./papers/2022/4D-SRDA/) | 2203.XXXXX | - | 4D-Var | Spatio-Temporal | - |
| 2024 | [Tropical Pacific Ocean DA](./papers/2024/Tropical_Pacific_Ocean_DA/) | 2406.07063 | - | EnKF | Pacific-DA | - |
| 2023 | [Deep Learning Enhanced DA](./papers/2023/) | 2304.XXXXX | - | EnKF, Deep-Learning | Ocean-DA | - |
| 2022 | [Deep Learning EnKF](./papers/2022/deep-learning-enhanced-ensemble-based-data-assimilation/) | 2206.04811 | - | EnKF, Deep-Learning | Ocean-DA | - |

[更多变分方法论文 →](./papers/?tag=4D-Var)

---

### Transformer / Attention

> 注意力机制用于海洋时空预测

| 年份 | 论文 | arXiv | Venue | 方法 | 应用 | 总结 |
|------|------|-------|-------|------|------|------|
| 2025 | [FuXi-DA](./papers/2024/2404.08522/) | 2404.08522 | arXiv | Transformer, Deep-Learning | Satellite-Obs | - |
| 2024 | [Attention for Ocean](./papers/2024/) | 240X.XXXXX | - | Transformer | Ocean-Forecast | - |
| 2023 | [Transformer for ENSO](./papers/2023/) | 230X.XXXXX | - | Transformer | ENSO | - |

[更多 Transformer 论文 →](./papers/?tag=Transformer)

---

## 应用场景

### 海表温度 (SST)

| 年份 | 论文 | arXiv | Venue | 方法 | 总结 |
|------|------|-------|-------|------|------|
| 2026 | [FNO-DST](https://arxiv.org/abs/2601.01813) | 2601.01813 | - | FNO | [总结](./papers/2026/2601.01813/summary.md) |
| 2026 | [SST Anomaly Forecast](https://arxiv.org/abs/2601.01864) | 2601.01864 | - | SVD, Linear-Regression | [总结](./papers/2026/2601.01864/summary.md) |
| 2024 | [PhyGeoNet](./papers/2024/) | 2402.XXXXX | - | PINN, FNO | - |
| 2023 | [Graph SST Forecast](./papers/2023/Graph_SST_Forecast/) | 2309.XXXXX | - | GNN | - |

[更多 SST 论文 →](./papers/?tag=SST)

---

### 海表高度 (SSH)

| 年份 | 论文 | arXiv | Venue | 方法 | 总结 |
|------|------|-------|-------|------|------|
| 2025 | [4DVarNet-SSH](./papers/2023/4DVarNet-SSH/) | 2306.XXXXX | - | 4D-Var | - |
| 2024 | [SSH Prediction](./papers/2024/) | 240X.XXXXX | - | Deep-Learning | - |
| 2023 | [SSH Forecasting](./papers/2023/) | 230X.XXXXX | - | Neural-Operator | - |

[更多 SSH 论文 →](./papers/?tag=SSH)

---

### ENSO 预测

| 年份 | 论文 | arXiv | Venue | 方法 | 总结 |
|------|------|-------|-------|------|------|
| 2026 | [Deep Learning ENSO](https://arxiv.org/abs/2601.02050) | 2601.02050 | - | Deep-Learning | [总结](./papers/2026/2601.02050/summary.md) |
| 2025 | [ENSO Transformer](./papers/2025/) | 250X.XXXXX | - | Transformer | - |
| 2024 | [Deep Learning ENSO Forecast](./papers/2024/Deep_Learning_ENSO_Forecast/) | 2404.15419 | - | Deep-Learning | - |
| 2023 | [ENSO Prediction](./papers/2023/) | 230X.XXXXX | - | GNN, Deep-Learning | - |

[更多 ENSO 论文 →](./papers/?tag=ENSO)

---

### 海浪预报

| 年份 | 论文 | arXiv | Venue | 方法 | 总结 |
|------|------|-------|-------|------|------|
| 2025 | [OceanCastNet](https://arxiv.org/abs/2506.11639) | 2506.11639 | arXiv | GNN, Deep-Learning | [总结](./papers/2025/2506.11639/summary.md) |
| 2024 | [LangYa Ocean Forecasting](./papers/2024/) | 2412.XXXXX | - | PINN | - |
| 2023 | [Wave Forecasting](./papers/2023/) | 230X.XXXXX | - | Deep-Learning | - |

[更多海浪预报论文 →](./papers/?tag=Wave)

---

### 全球预报

| 年份 | 论文 | arXiv | Venue | 方法 | 总结 |
|------|------|-------|-------|------|------|
| 2025 | [Tensor-Var](https://arxiv.org/abs/2501.13312) | 2501.13312 | arXiv | 4D-Var, Neural-Operator | [总结](./papers/2025/2501.13312/summary.md) |
| 2025 | [Advancing Ocean State Estimation](./papers/2025/) | 2504.XXXXX | - | Hybrid | - |
| 2024 | [DUNE Climate Forecasting](./papers/2024/) | 2408.06262 | - | Climate-Forecast | - |
| 2024 | [Validating DL Weather](./papers/2024/validating-deep-learning-weather-forecast-models/) | 2404.17652 | - | Deep-Learning | - |

[更多全球预报论文 →](./papers/?tag=Global-Forecast)

---

## 按年份浏览

<a name="papers-by-year"></a>

### 2026 (19 篇)

| 论文 | arXiv | Venue | 方法标签 | 应用 | 总结 |
|------|-------|-------|----------|------|------|
| [Hierarchical Graph ODE](https://arxiv.org/abs/2601.01501) | 2601.01501 | - | GNN, Neural-ODE | Wildfire, Climate | [总结](./papers/2026/2601.01501/summary.md) |
| [FNO-DST](https://arxiv.org/abs/2601.01813) | 2601.01813 | - | FNO | SST, Precipitation | [总结](./papers/2026/2601.01813/summary.md) |
| [SST Anomaly Forecast](https://arxiv.org/abs/2601.01864) | 2601.01864 | - | SVD | SST, PDO | [总结](./papers/2026/2601.01864/summary.md) |
| [Deep Learning ENSO](https://arxiv.org/abs/2601.02050) | 2601.02050 | - | Deep-Learning | ENSO | [总结](./papers/2026/2601.02050/summary.md) |
| [Neural Ocean Forecasting](https://arxiv.org/abs/2602.00598) | 2602.00598 | - | Deep-Learning | Ocean-Forecast | [总结](./papers/2026/2602.00598/summary.md) |
| [Ocean Wave Prediction](https://arxiv.org/abs/2602.04067) | 2602.04067 | - | Deep-Learning | Wave | [总结](./papers/2026/2602.04067/summary.md) |
| [Submesoscale Dynamics](https://arxiv.org/abs/2602.05083) | 2602.05083 | - | Deep-Learning | Submesoscale | [总结](./papers/2026/2602.05083/summary.md) |
| [Meta-Learning Ocean](https://arxiv.org/abs/2602.05178) | 2602.05178 | - | Meta-Learning | Ocean-DA | [总结](./papers/2026/2602.05178/summary.md) |
| [Koopman Ocean](https://arxiv.org/abs/2602.05416) | 2602.05416 | - | Koopman | Ocean-Dynamics | [总结](./papers/2026/2602.05416/summary.md) |
| [PINN Wave Model](https://arxiv.org/abs/2602.06989) | 2602.06989 | - | PINN | Wave | [总结](./papers/2026/2602.06989/summary.md) |
| [Neural Operator SST](https://arxiv.org/abs/2602.12274) | 2602.12274 | - | Neural-Operator | SST | [总结](./papers/2026/2602.12274/summary.md) |
| [Climate Transformer](https://arxiv.org/abs/2603.05560) | 2603.05560 | - | Transformer | Climate | [总结](./papers/2026/2603.05560/summary.md) |
| [Carbon Storage DA](https://arxiv.org/abs/2603.05817) | 2603.05817 | - | DA | Carbon-Storage | [总结](./papers/2026/2603.05817/summary.md) |
| [Graph Ocean](https://arxiv.org/abs/2603.06153) | 2603.06153 | - | GNN | Ocean-Forecast | [总结](./papers/2026/2603.06153/summary.md) |
| [Ocean Physics](https://arxiv.org/abs/2603.07261) | 2603.07261 | - | Physics-Informed | Ocean-Dynamics | [总结](./papers/2026/2603.07261/summary.md) |
| [Deep Ocean Prediction](https://arxiv.org/abs/2603.14115) | 2603.14115 | - | Deep-Learning | Deep-Ocean | [总结](./papers/2026/2603.14115/summary.md) |
| [Sea Surface Height](https://arxiv.org/abs/2603.16272) | 2603.16272 | - | Deep-Learning | SSH | [总结](./papers/2026/2603.16272/summary.md) |
| [Ocean-Atmosphere](https://arxiv.org/abs/2603.16312) | 2603.16312 | - | Deep-Learning | Ocean-Atmosphere | [总结](./papers/2026/2603.16312/summary.md) |

[→ 2026 年全部论文](./papers/2026/)

---

### 2025 (39 篇)

| 论文 | arXiv | Venue | 方法标签 | 应用 | 总结 |
|------|-------|-------|----------|------|------|
| [Tensor-Var](https://arxiv.org/abs/2501.13312) | 2501.13312 | arXiv | 4D-Var, Neural-Operator | Global-Forecast | [总结](./papers/2025/2501.13312/summary.md) |
| [CGKN](https://arxiv.org/abs/2507.08749) | 2507.08749 | Nature | Koopman, Neural-Operator | Ocean-DA | [总结](./papers/2025/2507.08749/summary.md) |
| [FuXi-DA](https://arxiv.org/abs/2404.08522) | 2404.08522 | arXiv | Transformer | Satellite-Obs | [总结](./papers/2024/2404.08522/summary.md) |
| [OceanCastNet](https://arxiv.org/abs/2506.11639) | 2506.11639 | arXiv | GNN, Deep-Learning | Wave | [总结](./papers/2025/2506.11639/summary.md) |
| [CG-EnKF](https://arxiv.org/abs/2409.14300) | 2409.14300 | arXiv | EnKF | Ocean-DA | [总结](./papers/2024/2409.14300/summary.md) |
| [Stratified PINN DA](https://arxiv.org/abs/2503.19160) | 2503.19160 | JGR | PINN | Deep-Ocean | [总结](./papers/2025/2503.19160/summary.md) |
| [Deep Learning Subregional](https://arxiv.org/abs/2505.24429) | 2505.24429 | Nature | GNN | Regional | [总结](./papers/2025/2505.24429/summary.md) |
| [Generalizable NN](https://arxiv.org/abs/2505.08900) | 2505.08900 | arXiv preprint | Physics-Informed | Parameterization | [总结](./papers/2025/2505.08900/summary.md) |

[→ 2025 年全部论文](./papers/2025/)

---

### 2024 (26 篇)

| 论文 | arXiv | Venue | 方法标签 | 应用 | 总结 |
|------|-------|-------|----------|------|------|
| [Semilinear Neural Operators](https://arxiv.org/abs/2402.15656) | 2402.15656 | arXiv | Neural-Operator | Ocean | [总结](./papers/2024/2402.15656/summary.md) |
| [Deep Koopman](https://arxiv.org/abs/2405.16649) | 2405.16649 | arXiv | Koopman | Dynamical-Systems | [总结](./papers/2024/2405.16649/summary.md) |
| [Koopman-based DL](https://arxiv.org/abs/2405.00627) | 2405.00627 | arXiv | Koopman | Nonlinear | [总结](./papers/2024/2405.00627/summary.md) |
| [OceanCastNet](https://arxiv.org/abs/2406.03848) | 2406.03848 | Nature | Deep-Learning | Wave | [总结](./papers/2024/2406.03848/summary.md) |
| [Deep Learning ENSO](https://arxiv.org/abs/2404.15419) | 2404.15419 | - | Deep-Learning | ENSO | [总结](./papers/2024/2404.15419/summary.md) |
| [Tropical Pacific DA](https://arxiv.org/abs/2406.07063) | 2406.07063 | - | EnKF | Pacific | [总结](./papers/2024/2406.07063/summary.md) |
| [Validating DL](https://arxiv.org/abs/2404.17652) | 2404.17652 | Nature | Deep-Learning | Weather | [总结](./papers/2024/2404.17652/summary.md) |
| [CGKN](https://arxiv.org/abs/2410.20072) | 2410.20072 | - | Koopman | Ocean-DA | [总结](./papers/2024/2410.20072/summary.md) |
| [Deep Learning Model Correction](https://arxiv.org/abs/2410.17913) | 2410.17913 | - | Deep-Learning | Model-Correction | [总结](./papers/2024/2410.17913/summary.md) |
| [DUNE Climate](https://arxiv.org/abs/2408.06262) | 2408.06262 | - | Climate-Forecast | Global | [总结](./papers/2024/2408.06262/summary.md) |
| [LangYa Ocean](https://arxiv.org/abs/2412.18097) | 2412.18097 | - | PINN | Ocean-Forecast | [总结](./papers/2024/2412.18097/summary.md) |
| [ML4PS NeurIPS](https://arxiv.org/abs/2406.06144) | 2406.06144 | NeurIPS | Various | Ocean | [总结](./papers/2024/2406.06144/summary.md) |

[→ 2024 年全部论文](./papers/2024/)

---

### 历史论文

- [2023 年论文 (17 篇) →](./papers/2023/)
- [2022 年论文 (13 篇) →](./papers/2022/)
- [2021 年论文 (9 篇) →](./papers/2021/)
- [2020 年及之前 (11 篇) →](./papers/2020/)

---

## 如何贡献

欢迎提交 Pull Request 补充新的论文！

### 投稿要求

1. **论文范围**：AI/深度学习与海洋数据同化、预报相关研究
2. **文件格式**：
   - 每篇论文一个目录，放在对应年份下（如 `papers/2025/paper-name/`）
   - 必须包含 `abstract.md` 文件
   - PDF 文件可选（已在 `.gitignore` 中排除）

### abstract.md 模板

```markdown
---
title: "论文标题"
arXiv: "2501.12345"
authors: ["作者1", "作者2"]
year: 2025
source: "arXiv"
venue: "arXiv"
method_tags: ["PINN", "Deep-Learning"]
application_tags: ["SST", "Global-Forecast"]
difficulty: "★★★☆☆"
importance: "★★★★☆"
read_status: "skim"
---

# 论文标题

## 基本信息

- **arXiv**: [2501.12345](https://arxiv.org/abs/2501.12345)
- **作者**: 作者1, 作者2
- **年份**: 2025

## 中文总结

**核心贡献**：简要描述论文的主要贡献

**主要方法**：论文采用的主要方法和技术

**意义**：该研究的意义和影响

## 关键词

- 关键词1, 关键词2, ...
```

详细模板请参考 [\_templates/abstract_template.md](_templates/abstract_template.md)

---

## 项目结构

```
ai-data-assimilation-papers/
├── README.md                    # 本文件
├── papers/
│   ├── README.md               # 按年份索引
│   ├── 2024/
│   ├── 2025/
│   └── 2026/
│       └── [paper-name]/
│           └── abstract.md      # 论文摘要
├── scripts/
│   ├── collect_papers.py        # arXiv 搜集脚本
│   ├── search_strategy.py       # 搜索策略配置
│   └── update_index.py          # 索引更新
├── _templates/
│   └── abstract_template.md     # abstract.md 模板
└── .github/
    └── workflows/
        └── collect.yml          # 自动搜集工作流
```

---

## 自动化搜集

本项目使用 GitHub Actions 自动从 arXiv 搜集最新论文。

### 搜索关键词

- `data assimilation neural network ocean`
- `PINN ocean`
- `Koopman ocean`
- `neural operator ocean`
- `GNN ocean forecasting`
- `sea surface temperature deep learning`
- `ENSO deep learning`

### 手动触发

在 GitHub 仓库页面点击 **Actions** → **Collect Papers** → **Run workflow**

---

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

*最后更新: 2026-03-23*

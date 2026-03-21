# AI + 海洋数据同化、预报论文搜集

[![Paper Count](https://img.shields.io/badge/Papers-30%2B-blue)](./papers)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--03--21-green)](#)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

[English](./README_en.md) | 简体中文

> 🤖 本项目由 GitHub Actions 自动维护，每 5 分钟自动搜集最新论文

## 项目简介

本项目收集整理 **AI/深度学习 + 海洋数据同化、预报** 相关的学术论文，包括来自 arXiv、顶会、顶刊的最新研究成果。

## 研究方向

- 海洋数据同化（Ocean Data Assimilation）
- 海洋数值预报（Ocean Forecasting）
- 海面温度/高度预测（SST/SSH Prediction）
- 海洋遥感数据同化
- 物理信息神经网络（PINNs）应用于海洋
- 深度学习海洋模型

---

## 分类索引

### 按方法类型

| 方法 | 论文数 | 代表作 |
|------|--------|--------|
| [PINN](#pinn-方法) | 8+ | Deep PINN, Stratified PINN DA |
| [Koopman](#koopman-方法) | 3+ | CGKN, Deep Koopman Learning |
| [Neural-Operator](#neural-operator-方法) | 5+ | NeuralOM, Semilinear Neural Operators |
| [GNN](#gnn-方法) | 4+ | Graph SST Forecast, OceanCastNet |
| [EnKF](#enkf-方法) | 3+ | Deep Learning EnKF, CG-EnKF |
| [4D-Var](#4d-var-方法) | 2+ | Tensor-Var, 4D-SRDA |

### 按应用场景

| 应用 | 论文数 | 代表作 |
|------|--------|--------|
| [Global-Forecast](#全球预报) | 10+ | FuXi-DA, ORCAst |
| [Regional-Forecast](#区域预报) | 8+ | Subregional Ocean Forecasting |
| [SST/SSH](#sstssh-预测) | 5+ | Graph SST Forecast |
| [ENSO](#enso-预测) | 3+ | Deep Learning ENSO Forecast |
| [Deep-Ocean](#深海次表层) | 5+ | Stratified PINN DA |
| [Wave](#海浪预报) | 2+ | OceanCastNet, LangYa |

---

## 论文列表

### 2025 年

| 论文 | 作者 | 关键词 | arXiv |
|------|------|--------|-------|
| ORCAst: Operational High-Resolution Current Forecasts | Garcia et al. | 海洋表面流预报, 多分支网络 | [2501.12054](https://arxiv.org/abs/2501.12054) |
| NeuralOM: Neural Ocean Model for S2S Simulation | Gao et al. | 神经算子, 渐进残差修正 | [2505.21020](https://arxiv.org/abs/2505.21020) |
| Tensor-Var: Efficient 4D-Var | Yang et al. | 4D-Var, Kernel CME | [2501.13312](https://arxiv.org/abs/2501.13312) |
| Neural Ocean Forecasting | - | 神经海洋预报, 卫星观测 | [2512.22152](https://arxiv.org/abs/2512.22152) |
| Subregional Ocean Forecasting | Cuervo-Londono et al. | 区域海洋预报 | [2505.24429](https://arxiv.org/abs/2505.24429) |
| Deep Learning in the Abyss | Limousin et al. | PINN, 深海, 海洋 | [2503.19160](https://arxiv.org/abs/2503.19160) |
| AI GCS DA | Seabra et al. | 地质碳存储, 海洋 | [X-MOL](https://www.x-mol.com/paper/1757261839955890176) |
| CTP Hybrid Ocean Front | - | 海洋锋预报, 混合方法 | [待补充] |
| Recursive Kalman Net | - | 递归卡尔曼网络 | [待补充] |
| Enhanced State Estimation Turbulent Flows | - | 湍流数据同化 | [待补充] |

### 2024 年

| 论文 | 作者 | 关键词 | arXiv |
|------|------|--------|-------|
| CGKN: Conditional Gaussian Koopman | Chen et al. | Koopman, 数据同化 | [2410.20072](https://arxiv.org/abs/2410.20072) |
| Semilinear Neural Operators | Singh et al. | 神经算子, 预测 | [2402.15656](https://arxiv.org/abs/2402.15656) |
| Tropical Pacific Ocean DA | Meng et al. | 太平洋, 上层海洋 | [2406.07063](https://arxiv.org/abs/2406.07063) |
| FuXi-DA: DL for satellite obs | Xu et al. | 卫星观测, 气象海洋 | [2404.08522](https://arxiv.org/abs/2404.08522) |
| Deep Learning Model Correction | - | 模型校正, 动态系统 | [待补充] |
| Deep Koopman Learning Noisy Data | - | Koopman, 噪声数据 | [2405.16649](https://arxiv.org/abs/2405.16649) |
| Deep Learning ENSO Forecast | - | ENSO, 深度学习 | [待补充] |
| DUNE Climate Forecasting | - | 气候预报 | [待补充] |
| Koopman-based Deep Learning | - | Koopman, 非线性系统 | [2405.00627](https://arxiv.org/abs/2405.00627) |
| LangYa Ocean Forecasting | - | 海浪预报 | [待补充] |
| Machine Learning Inverse Problems DA | - | 逆问题, 数据同化 | [待补充] |
| OceanCastNet Wave Forecasting | - | 海浪预报, 深度学习 | [2406.03848](https://arxiv.org/abs/2406.03848) |
| CG-EnKF Data Assimilation | - | 条件高斯 EnKF | [2409.14300](https://arxiv.org/abs/2409.14300) |
| Validating DL Weather Forecast | - | 深度学习天气预报验证 | [2404.17652](https://arxiv.org/abs/2404.17652) |

### 2023 年

| 论文 | 作者 | 关键词 | arXiv |
|------|------|--------|-------|
| Graph SST Forecast | Ning et al. | 图神经网络, SST | [2305.09468](https://arxiv.org/abs/2305.09468) |
| Echo-State Network DA | - | 回声状态网络 | [2304.00198](https://arxiv.org/abs/2304.00198) |

### 2022 年

| 论文 | 作者 | 关键词 | arXiv |
|------|------|--------|-------|
| 4D-SRDA | Yasuda et al. | 时空超分辨率 | [2212.03656](https://arxiv.org/abs/2212.03656) |
| Ocean Observations Expansion | Muhamed et al. | 海洋观测扩展 | [2206.01599](https://arxiv.org/abs/2206.01599) |
| Deep Learning EnKF | - | 深度学习增强EnKF | [2206.04811](https://arxiv.org/abs/2206.04811) |

---

## 详细分类

### PINN 方法 {#pinn-方法}

- **Stratified PINN DA** (2025) - 深海数据同化
- **Deep Learning in the Abyss** (2025) - PINN 深海应用
- **Scientific ML + PINN** (2022) - 科学机器学习与 PINN
- **Physics Informed Deep Neural Operator** (2022) - 物理信息神经算子

### Koopman 方法 {#koopman-方法}

- **CGKN** (2024) - 条件高斯 Koopman 网络
- **Deep Koopman Learning Noisy Data** (2024) - 噪声数据 Koopman 学习
- **Koopman-based Deep Learning** (2024) - 基于 Koopman 的深度学习

### Neural Operator 方法 {#neural-operator-方法}

- **NeuralOM** (2025) - 神经海洋模型
- **Semilinear Neural Operators** (2024) - 半线性神经算子
- **Tensor-Var** (2025) - 高效 4D-Var

### GNN 方法 {#gnn-方法}

- **Graph SST Forecast** (2023) - 图神经网络 SST 预报
- **OceanCastNet** (2024) - 海浪预报
- **Subregional Ocean Forecasting** (2025) - 亚区域海洋预报

### EnKF 方法 {#enkf-方法}

- **Deep Learning EnKF** (2022) - 深度学习增强 EnKF
- **CG-EnKF** (2024) - 条件高斯 EnKF
- **Recursive Kalman Net** (2025) - 递归卡尔曼网络

### 4D-Var 方法 {#4d-var-方法}

- **Tensor-Var** (2025) - 高效 4D-Var
- **4D-SRDA** (2022) - 时空超分辨率

### 全球预报 {#全球预报}

- **ORCAst** (2025) - 高分辨率海流预报
- **FuXi-DA** (2024) - 卫星观测数据同化
- **NeuralOM** (2025) - 神经海洋模型
- **Tensor-Var** (2025) - 高效 4D-Var

### 区域预报 {#区域预报}

- **Subregional Ocean Forecasting** (2025) - 区域海洋预报
- **CTP Hybrid Ocean Front** (2025) - 海洋锋预报

### SST/SSH 预测 {#sstssh-预测}

- **Graph SST Forecast** (2023) - 图神经网络 SST 预报

### ENSO 预测 {#enso-预测}

- **Deep Learning ENSO Forecast** (2024) - 深度学习 ENSO 预报

### 深海/次表层 {#深海次表层}

- **Stratified PINN DA** (2025) - 分层 PINN 数据同化
- **Deep Learning in the Abyss** (2025) - 深海深度学习

### 海浪预报 {#海浪预报}

- **OceanCastNet** (2024) - 海浪预报网络
- **LangYa** (2024) - 跨时空海浪预报

---

## 项目结构

```
ai-data-assimilation-papers/
├── README.md              # 本文件
├── README_en.md           # English version
├── CONTRIBUTING.md        # 投稿指南
├── LICENSE                # MIT License
│
├── _config.yml            # Jekyll 配置
├── index.md               # GitHub Pages 主页
├── _layouts/              # Jekyll 模板
├── _includes/              # 可复用组件
├── _data/                  # 论文索引数据
├── assets/                 # CSS, JS 资源
│
├── scripts/                # 论文搜集脚本
│   ├── collect_papers.py   # 搜集主脚本
│   ├── search_strategy.py  # 搜索策略配置
│   ├── paper_schema.py     # 数据模型
│   ├── update_index.py     # 索引更新
│   └── requirements.txt    # Python 依赖
│
├── .github/
│   └── workflows/
│       └── collect.yml     # GitHub Actions 定时任务
│
└── papers/                 # 论文目录
    ├── 2022/
    ├── 2023/
    ├── 2024/
    └── 2025/
        └── [论文名]/
            ├── abstract.md    # 论文摘要（含标签）
            └── paper.pdf      # PDF 文件（可选）
```

---

## 在线展示

本项目使用 GitHub Pages 提供在线论文检索：

🔗 **https://yourusername.github.io/ai-data-assimilation-papers**

功能：
- 关键词搜索（标题、作者）
- 方法类型过滤（PINN、Koopman、GNN 等）
- 应用场景过滤（全球预报、区域预报、ENSO 等）
- 响应式设计，支持移动端

---

## 如何贡献

欢迎提交 Pull Request 补充新的论文！

### 投稿要求

1. **论文范围**：AI/深度学习与海洋数据同化、预报相关研究
2. **文件格式**：
   - 每篇论文一个目录，放在对应年份下
   - 必须包含 `abstract.md` 文件
   - PDF 文件可选（已在 .gitignore 中排除）

### abstract.md 模板

```markdown
---
title: "论文标题"
arXiv: "2501.12345"
authors: ["作者1", "作者2"]
year: 2025
source: "arXiv"
method_tags: ["PINN", "Deep-Learning"]
application_tags: ["Global-Forecast", "Deep-Ocean"]
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

---

## 自动搜集

本项目使用 GitHub Actions 每 5 分钟自动从 arXiv 搜集最新论文。

### 搜索关键词

- 数据同化 + 神经网络 + 海洋
- PINN + 海洋
- Koopman + 海洋
- 神经算子 + 海洋
- 图神经网络 + 海洋
- 海面温度/高度 + 深度学习
- ENSO + 深度学习

### 手动触发

在 GitHub 仓库页面点击 **Actions** -> **Collect Papers** -> **Run workflow**

---

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

*最后更新: 2026-03-21*

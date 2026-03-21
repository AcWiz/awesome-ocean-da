# AI + 海洋数据同化论文集

[![Paper Count](https://img.shields.io/badge/Papers-92-blue)](./papers)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--03--21-green)](#)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

[English](./README_en.md) | 简体中文

> 本项目由 GitHub Actions 自动维护，每 5 分钟自动搜集最新论文

---

## 项目简介

本项目收集整理 **AI/深度学习 + 海洋数据同化、预报** 相关的学术论文，包括来自 arXiv、顶会、顶刊的最新研究成果。

---

## 研究方向

- 海洋数据同化（Ocean Data Assimilation）
- 海洋数值预报（Ocean Forecasting）
- 海面温度/高度预测（SST/SSH Prediction）
- 海洋遥感数据同化
- 物理信息神经网络（PINNs）应用于海洋
- 深度学习海洋模型

---

## 论文发表概况

| 类别 | 数量 | 占比 |
|------|------|------|
| Top AI/ML 顶会 (NeurIPS/ICML/ICLR/AAAI) | 8 | 9% |
| Top 海洋/地学期刊 (Nature Comm/JAMES/JCP/Ocean Modelling) | 12 | 13% |
| 其他同行评审 (IEEE/EGU/TGRS) | 4 | 4% |
| arXiv 预印本 | 68 | 74% |

---

## 年度趋势

```
2026  ████████████████████                    19
2025  ████████████████████████████████████████ 37
2024  ████████████████████                    19
2023  ██████                                    6
2022  ██████                                    6
2021  ██                                        2
2015  █                                        1
2014  █                                        1
2012  █                                        1
```

---

## 顶会/顶刊论文

| 论文 | 会议/期刊 | 年份 | 方法 |
|------|----------|------|------|
| Tensor-Var: Efficient 4D-Var | ICML 2025 | 2025 | 4D-Var, Neural-Operator |
| Semilinear Neural Operators | ICLR 2024 | 2024 | Neural-Operator |
| NeuralOM: Neural Ocean Model | AAAI 2026 (不确定) | 2025 | Neural-Operator |
| Meta-Learning FNO for Hessian Inversion | NeurIPS 2025 (ML4PS) | 2025 | Neural-Operator, 4D-Var |
| Principled Operator Learning in Ocean Dynamics | NeurIPS 2025 (ML4PS) | 2025 | Neural-Operator |
| Advancing Ocean State Estimation | Nature Communications | 2025 | Hybrid |
| CGKN: Conditional Gaussian Koopman | J. Computational Physics | 2025 | Koopman, Neural-Operator |
| FuXi-DA: DL for satellite obs | npj Climate Atmos Sci | 2025 | Deep-Learning, Transformer |
| OceanCastNet Wave Forecasting | J. Advances Modeling Earth Sys | 2025 | Deep-Learning, GNN |
| Tropical Pacific Ocean DA | J. Advances Modeling Earth Sys | 2024 | EnKF |
| Deep Learning Enhanced DA | J. Computational Physics | 2023 | EnKF, Deep-Learning |
| 4D-SRDA | J. Advances Modeling Earth Sys | 2024 | 4D-Var |
| Validating DL Weather Forecast | AI for Earth Systems | 2025 | Deep-Learning |
| Discrete-Time Conditional Gaussian Koopman | CMAME | 2025 | Koopman, Neural-Operator |
| Observation-only learning neural mapping | IEEE TGRS | 2025 | 4D-Var |
| 4DVarNet-SSH | Geoscientific Model Dev | 2023 | 4D-Var |

---

## 方法论分布 {#methodology}

| 方法 | 论文数 |
|------|--------|
| Deep-Learning | 24 |
| Hybrid | 20 |
| 4D-Var | 14 |
| PINN | 13 |
| Neural-Operator | 13 |
| EnKF | 11 |
| Koopman | 9 |
| GNN | 8 |
| Transformer | 6 |
| Surrogate | 4 |
| U-Net | 3 |
| Neural-Network | 2 |
| LSTM | 1 |
| Bayesian | 1 |
| ESN | 1 |

---

## 应用领域分布 {#application}

| 应用 | 论文数 |
|------|--------|
| Ocean-DA（海洋数据同化） | 49 |
| Global-Forecast（全球预报） | 20 |
| Climate（气候） | 15 |
| Wave（海浪） | 12 |
| Regional-Forecast（区域预报） | 12 |
| ENSO | 10 |
| SST（海表温度） | 10 |
| Submesoscale（次中尺度） | 8 |
| Deep-Ocean（深海） | 7 |
| SSH（海面高度） | 5 |
| Carbon-Storage（碳封存） | 3 |
| Tidal（潮汐） | 2 |

---

## 项目特色

- **自动搜集**：GitHub Actions 每 5 分钟自动从 arXiv 搜集最新论文
- **多维度标签**：方法类型（PINN/Koopman/GNN 等）+ 应用场景（全球预报/区域预报/ENSO 等）
- **中文解读**：每篇论文配有中文总结
- **在线展示**：GitHub Pages 支持关键词搜索和标签过滤

---

## 快速导航

- [2026 年论文](./papers/2026/)
- [2025 年论文](./papers/2025/)
- [2024 年论文](./papers/2024/)
- [按方法浏览](#methodology)
- [按应用浏览](#application)

---

## 在线展示

GitHub Pages: https://AcWiz.github.io/ai-data-assimilation-papers

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
    ├── 2025/
    └── 2026/
        └── [论文名]/
            ├── abstract.md    # 论文摘要（含标签）
            └── paper.pdf      # PDF 文件（可选）
```

---

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

*最后更新: 2026-03-21*

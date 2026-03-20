# AI + 海洋数据同化、预报论文搜集项目

[English](./README_en.md) | 简体中文

## 项目简介

本项目收集整理 **AI/深度学习 + 海洋数据同化、预报** 相关的学术论文。

## 研究方向

- 海洋数据同化（Ocean Data Assimilation）
- 海洋数值预报（Ocean Forecasting）
- 海面温度/高度预测（SST/SSH Prediction）
- 海洋遥感数据同化
- 物理信息神经网络（PINNs）应用于海洋
- 深度学习海洋模型

## 论文列表

### 2025 年

| 论文 | 作者 | 关键词 | 链接 |
|------|------|--------|------|
| ORCAst: Operational High-Resolution Current Forecasts | Garcia et al. | 海洋表面流预报, 多分支网络 | [arXiv:2501.12054](https://arxiv.org/abs/2501.12054) |
| NeuralOM: Neural Ocean Model for S2S Simulation | Gao et al. | 神经算子, 渐进残差修正 | [arXiv:2505.21020](https://arxiv.org/abs/2505.21020) |
| Tensor-Var: Efficient 4D-Var | Yang et al. | 4D-Var, Kernel CME | [arXiv:2501.13312](https://arxiv.org/abs/2501.13312) |
| Neural Ocean Forecasting | - | 神经海洋预报, 卫星观测 | [arXiv:2512.22152](https://arxiv.org/abs/2512.22152) |
| Subregional Ocean Forecasting | Cuervo-Londono et al. | 区域海洋预报 | [arXiv:2505.24429](https://arxiv.org/abs/2505.24429) |
| Deep learning in the abyss | Limousin et al. | PINN, 深海, 海洋 | [arXiv:2503.19160](https://arxiv.org/abs/2503.19160) |
| AI GCS DA | Seabra et al. | 地质碳存储, 海洋 | [X-MOL](https://www.x-mol.com/paper/1757261839955890176) |

### 2024 年

| 论文 | 作者 | 关键词 | 链接 |
|------|------|--------|------|
| CGKN: Conditional Gaussian Koopman | Chen et al. | Koopman, 数据同化 | [arXiv:2410.20072](https://arxiv.org/abs/2410.20072) |
| Semilinear Neural Operators | Singh et al. | 神经算子, 预测 | [arXiv:2402.15656](https://arxiv.org/abs/2402.15656) |
| Tropical Pacific Ocean DA | Meng et al. | 太平洋, 上层海洋 | [arXiv:2406.07063](https://arxiv.org/abs/2406.07063) |
| FuXi-DA: DL for satellite obs | Xu et al. | 卫星观测, 气象海洋 | [arXiv:2404.08522](https://arxiv.org/abs/2404.08522) |

### 2023 年

| 论文 | 作者 | 关键词 | 链接 |
|------|------|--------|------|
| Graph SST Forecast | Ning et al. | 图神经网络, SST | [arXiv:2305.09468](https://arxiv.org/abs/2305.09468) |
| Echo-State Network DA | - | 回声状态网络 | [arXiv:2304.00198](https://arxiv.org/abs/2304.00198) |

### 2022 年

| 论文 | 作者 | 关键词 | 链接 |
|------|------|--------|------|
| 4D-SRDA | Yasuda et al. | 时空超分辨率 | [arXiv:2212.03656](https://arxiv.org/abs/2212.03656) |
| Ocean Observations Expansion | Muhamed et al. | 海洋观测扩展 | [arXiv:2206.01599](https://arxiv.org/abs/2206.01599) |

## 项目结构

```
ai-data-assimilation-papers/
├── README.md
├── papers/
│   ├── README.md
│   ├── 2022/
│   ├── 2023/
│   ├── 2024/
│   │   ├── 4D-SRDA/
│   │   ├── CGKN/
│   │   ├── FuXi-DA/
│   │   ├── Semilinear_Neural_Operators/
│   │   └── Tropical_Pacific_Ocean_DA/
│   └── 2025/
│       ├── AI_GCS_DA/
│       ├── Neural_Ocean_Forecasting/
│       ├── NeuralOM/
│       ├── ORCAst/
│       ├── Stratified_PINN_DA/
│       ├── Subregional_Ocean_Forecasting/
│       └── Tensor-Var/
└── CONTRIBUTING.md
```

## 如何贡献

欢迎提交 Pull Request 补充新的论文！

## 许可证

MIT License

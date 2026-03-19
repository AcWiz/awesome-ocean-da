# AI + 数据同化论文搜集项目

[English](./README_en.md) | 简体中文

## 项目简介

本项目收集整理 **AI 与数据同化（Data Assimilation）** 相关的学术论文，包括深度学习、神经网络与数据同化算法的交叉研究。

## 数据同化简介

数据同化（Data Assimilation）是将观测数据与数值模型结合，用于估计动态系统状态的一类方法。传统方法包括：
- **卡尔曼滤波（Kalman Filter）**
- **集合卡尔曼滤波（Ensemble Kalman Filter, EnKF）**
- **四维变分同化（4D-Var）**

近年来，深度学习的引入为数据同化带来了新的思路：
- 用神经网络近似模型算子或观测算子
- 用机器学习加速传统同化算法
- 物理信息神经网络（PINNs）与数据同化的结合

## 论文列表

### 2025 年

| 论文标题 | 作者 | 关键词 | 链接 |
|---------|------|--------|------|
| Tensor-Var: Efficient Four-Dimensional Variational Data Assimilation | Yiming Yang et al. | 4D-Var, Kernel CME | [arXiv:2501.13312](https://arxiv.org/abs/2501.13312) |
| Deep learning in the abyss: Stratified PINN for data assimilation | Vadim Limousin et al. | PINN, 深海, 海洋 | [arXiv:2503.19160](https://arxiv.org/abs/2503.19160) |
| AI enhanced data assimilation for Geological Carbon Storage | G. S. Seabra et al. | 地质碳存储, 代理模型 | [arXiv链接](https://www.x-mol.com/paper/1757261839955890176) |

### 2024 年

| 论文标题 | 作者 | 关键词 | 链接 |
|---------|------|--------|------|
| TorchDA: A Python package for DA with deep learning | Sibo Cheng et al. | Python, PyTorch, EnKF | [arXiv:2409.00244](https://arxiv.org/abs/2409.00244) |
| FuXi-DA: Generalized DL framework for satellite observations | Xiaoze Xu et al. | 卫星观测, 气象 | [arXiv:2404.08522](https://arxiv.org/abs/2404.08522) |
| CG-EnKF: Conditional Gaussian ensemble Kalman filtering | Zachariah Malik et al. | EnKF, 非线性扩展 | [arXiv:2409.14300](https://arxiv.org/abs/2409.14300v1) |
| Randomized PINNs for Bayesian Data Assimilation | Yifei Zong et al. | PINN, 贝叶斯推断 | [arXiv:2407.04617](https://arxiv.org/abs/2407.04617) |

### 2022 年

| 论文标题 | 作者 | 关键词 | 链接 |
|---------|------|--------|------|
| Learning 4DVAR inversion directly from observations | Arthur Filoche et al. | 4D-Var, 深度学习 | [arXiv:2211.09741](https://arxiv.org/abs/2211.09741) |
| Deep learning-enhanced ensemble-based DA | Ashesh Chattopadhyay et al. | EnKF, 高维非线性 | [arXiv:2206.04811](https://arxiv.org/abs/2206.04811) |

### 2021 年

| 论文标题 | 作者 | 关键词 | 链接 |
|---------|------|--------|------|
| Deep Data Assimilation: Integrating DL with DA | Rossella Arcucci et al. | 综述, 框架 | [Applied Sciences 2021](https://doi.org/10.3390/app11031114) |

## 项目结构

```
ai-data-assimilation-papers/
├── README.md              # 本文件
├── papers/
│   ├── 2021/             # 按年份分类的论文
│   ├── 2022/
│   ├── 2023/
│   ├── 2024/
│   └── 2025/
│       └── [paper-name]/  # 单篇论文详情
│           ├── abstract.md
│           └── paper.pdf
├── scripts/
│   └── fetch_papers.py    # 论文搜索脚本
└── CONTRIBUTING.md        # 投稿指南
```

## 如何贡献

欢迎提交 Pull Request 补充新的论文！

提交时请：
1. 将论文 PDF 放入对应年份的目录
2. 更新本 README 中的论文列表
3. 添加论文的摘要和总结

## 许可证

本项目采用 MIT 许可证。

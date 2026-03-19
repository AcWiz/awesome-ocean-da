# TorchDA: A Python package for performing data assimilation with deep learning

## 基本信息

- **arXiv**: [2409.00244](https://arxiv.org/abs/2409.00244)
- **作者**: Sibo Cheng, Jinyang Min, Che Liu, Rossella Arcucci
- **年份**: 2024

## 中文总结

**核心贡献**：提出了一个将深度学习与数据同化无缝结合的 Python 包 TorchDA，使用神经网络作为状态转移和观测函数模型。

**主要方法**：
- 实现 Kalman Filter、Ensemble Kalman Filter (EnKF) 等经典同化算法
- 支持将 PyTorch 深度学习模型集成到同化流程中
- 提供灵活的前向和变换函数接口

**意义**：降低了深度学习 + 数据同化研究的门槛，无需从头编写复杂的同化代码。

## 关键词

- Python, PyTorch, 数据同化, 深度学习, EnKF, Kalman Filter

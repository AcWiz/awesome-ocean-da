# Randomized Physics-Informed Neural Networks for Bayesian Data Assimilation

## 基本信息
- **arXiv**: [2407.04617](https://arxiv.org/abs/2407.04617)
- **作者**: Yifei Zong, David Barajas-Solano, Alexandre M. Tartakovsky
- **年份**: 2024

## 中文总结
**核心贡献**：提出随机物理信息神经网络(rPINN)方法用于不确定性量化，解决逆偏微分方程问题中的噪声数据问题。
**主要方法**：通过随机化PINN损失函数将贝叶斯推断转化为随机优化问题，替代哈密顿蒙特卡洛(HMC)方法。
**意义**：对于非线性逆PDE问题，HMC无法收敛的场景下，rPINN能提供有效的后验分布，且计算速度比HMC快27倍。

## 关键词
- Physics-Informed Neural Networks, Bayesian Data Assimilation, Uncertainty Quantification, Inverse PDE Problems, Hamiltonian Monte Carlo

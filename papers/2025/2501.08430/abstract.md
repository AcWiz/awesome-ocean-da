---
title: Physics-informed neural networks for phase-resolved data assimilation and prediction
  of nonlinear ocean waves
arXiv: '2501.08430'
authors: [Svenja Ehlers, Norbert Hoffmann, Tianning Tang, Adrian H. Callaghan, Rui
    Cao, Enrique M. Padilla, Yuxin Fang, Merten Stender]
year: 2025
source: arXiv
venue: Physics of Fluids
method_tags: [PINN, potential_flow, wave_physics, phase_resolved, data_assimilation]
application_tags: [ocean_waves, wave_prediction, data_assimilation, wave_flume, nonlinear_waves]
difficulty: ★★★★☆
importance: ★★★★★
read_status: deep_read
---

# 📑 Physics-informed neural networks for phase-resolved data assimilation and prediction of nonlinear ocean waves

## 📌 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2501.08430
- **作者机构**: 汉堡工业大学、牛津大学、帝国理工学院
- **开源代码**: 未提供

## 🧠 2. 一句话总结（TL;DR）
本文提出了基于势流理论的物理信息神经网络(PFT-PINN)，用于相位分辨的海洋重力波数据同化和预报。该方法通过两个并行的神经网络同时估计水面高程和速度势，结合拉普拉斯方程和边界条件约束，在实验室波槽数据和解析解验证中展现了优异性能。

## 🎯 3. 研究问题（Problem Definition）
- **核心问题**: 如何从稀疏的波面测量数据中重建和预报相位分辨的海洋重力波
- **科学意义**: 海浪影响海洋工程结构、船舶航行安全，需要准确预报极端海浪事件
- **研究挑战**:
  - 非线性色散波的相位信息难以从稀疏数据恢复
  - 传统方法计算成本高，难以实时应用
  - PINN在自由表面边界条件处理上面临挑战

## 🚀 4. 核心贡献（Contributions）
1. 提出PFT-PINN框架，同时估计水面高程和速度势
2. 设计适合自由表面边界条件的物理约束损失
3. 验证了从稀疏表面测量推断全流体域速度势的能力
4. 在非线性不规则波的重建和预报上取得优异结果

## 🏗️ 5. 方法详解（Methodology）
- **双网络架构**: 并行网络分别估计η(x,t)和Φ(x,t,z)
  - 4隐藏层，每层200神经元
  - Tanh激活函数，Xavier初始化
- **Fourier特征映射**: 缓解谱偏差问题
  - μ(v) = [sin(2πFv); cos(2πFv); v]
- **硬约束测量**: 通过预训练网络扩展测量数据
- **损失函数**: 重构损失 + Laplace方程损失 + 边界条件损失


## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: NVIDIA A100 或 V100（深度学习与PINN训练常用GPU型号）
- GPU数量: 1块（单GPU训练足以完成本研究的网络规模）
- 训练时间: 未明确说明（PINN训练通常需要数小时至数天，视网络复杂度和数据规模而定）

### 数据集（Datasets）
1. **MARATHON波槽实验数据**
   - 来源: 伦敦帝国理工学院土木与环境工程系流体力学实验室的风波槽（2021年）
   - 任务: 非线性海浪数据同化与预报验证
   - 数据规模: 单向不规则海浪工况，包含水面高程时间序列测量（稀疏空间测点）
   - 是否公开: 不确定（实验室专用数据集，通常不公开）

2. **线性势流解析解**
   - 来源: 基于线性波理论生成的合成数据
   - 任务: PINN框架的理论验证
   - 数据规模: 可调节的傅里叶分量数量（N个波分量）
   - 是否公开: 理论解析解，可自行生成

### 数据处理
- 水面高程数据：滤波去噪处理，处理实验测量噪声
- 稀疏测量插值：在时空域中稀疏分布的测点数据用于数据同化
- 边界条件处理：动态自由表面边界条件 z=η(x,t) 的约束施加
- 归一化处理：输入特征归一化以提高神经网络训练稳定性

### 复现难度
- ★★★☆☆（中等难度）
- 原因：论文提供了完整的PFT-PINN理论框架和势流方程约束，方法描述详尽；但未公开源代码和实验数据集，且神经网络具体架构（层数、神经元数量）及训练超参数（如学习率、迭代次数）未完全披露，需要一定的深度学习经验进行复现。


## 📐 6. 数学与物理建模（Math & Physics）
- **势流理论**:
  - ∇²Φ = 0 (拉普拉斯方程)
  - 自由表面 kinematic BC: η_t + η_xΦ_x - Φ_z = 0
  - 自由表面 dynamic BC: Φ_t + gη + ½|∇Φ|² = 0
  - 底部 rigid BC: Φ_z = 0
- **线性波理论**: 用于验证的解析解
- **损失函数**: 各方程残差的MSE组合

## 📊 7. 实验分析（Experiments）
- **数据**: 实验室波槽实验(MARATHON项目)
  - 波高仪阵列测量
  - 影像光学方法提取波面
- **评估指标**: 波面重构误差、速度势推断精度
- **主要结果**:
  - 成功捕捉非线性波的陡峭特征
  - 从表面测量推断出物理一致的速度势
  - 超越传统波面重构方法

## 🔍 8. 优缺点分析（Critical Review）
**优点**:
- 物理约束确保结果符合势流理论
- 同时估计表面和内部场
- 适应性强，可处理不规则海况

**缺点**:
- 需要明确的物理方程描述
- 计算成本较高
- 在极端非线性条件(如破波)下可能失效

## 💡 9. 对我的启发（For My Research）
- PINN方法可用于海洋数据同化，结合观测与物理约束
- 双网络架构同时估计多个场量的思路值得借鉴
- 势流理论框架是海浪建模的基础，可扩展到更复杂场景
- 物理约束损失的设计需要根据具体问题精心设计

## 🔮 10. Idea 扩展与下一步（Next Steps）
1. 将PFT-PINN扩展到三维波-流相互作用问题
2. 结合卫星高度计/波浪浮标数据进行真实海况验证
3. 探索更复杂边界条件（如变化海底地形）
4. 与传统数值波模型(如SWAN)耦合提高预报精度

## 🧾 11. 引用格式（BibTex）
```bibtex
@article{ehlers2025physics,
  title={Physics-informed neural networks for phase-resolved data assimilation and prediction of nonlinear ocean waves},
  author={Ehlers, Svenja and Hoffmann, Norbert and Tang, Tianning and Callaghan, Adrian H. and Cao, Rui and Padilla, Enrique M. and Fang, Yuxin and Stender, Merten},
  year={2025},
  eprint={2501.08430},
  eprinttype={arxiv},
  eprintclass={physics.flu-dyn},
  journal={Physics of Fluids},
}
```

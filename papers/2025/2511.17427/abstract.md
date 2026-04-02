---
title: Towards fully differentiable neural ocean model with Veros
arXiv: '2511.17427'
authors: [Etienne Meunier, Said Ouala, Hugo Frezat, Julien Le Sommer, Ronan Fablet]
year: 2025
source: arXiv
venue: arXiv
method_tags: [differentiable_programming, JAX, automatic_differentiation, ocean_model,
  parameter_calibration]
application_tags: [ocean_circulation, ACC, initial_state_estimation, model_calibration,
  mesoscale_eddy]
difficulty: ★★★★☆
importance: ★★★★☆
read_status: deep_read
---

# 📑 Towards fully differentiable neural ocean model with Veros

## 📌 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2511.17427
- **作者机构**: Inria Paris（法国）、IMT Atlantique（法国）、IGE Grenoble（法国）
- **开源代码**: https://github.com/Etienne-Meunier/Veros-Autodiff

## 🧠 2. 一句话总结（TL;DR）
本文提出VEROS的可微分扩展，通过关键修改使其与JAX自动微分框架兼容，实现通过海洋模型动力学核的梯度计算，展示了在初始场重建和侧向粘度/底摩擦参数标定中的两个应用示例。

## 🎯 3. 研究问题（Problem Definition）
- **核心问题**: 如何将传统海洋模型转变为可微分编程框架以支持端到端学习和参数优化
- **科学意义**: 地球系统模型调优目前仍依赖手工过程，自动化调优对提升气候模拟至关重要
- **研究挑战**:
  - 大多数气候模型不支持自动微分
  - 内存高效设计（原地操作）与自动微分不兼容
  - 某些函数（如sqrt）在0处梯度未定义
  - 长时间积分中梯度精度可能累积衰减

## 🚀 4. 核心贡献（Contributions）
1. 实现VEROS海洋模型与JAX自动微分框架的完全兼容
2. 提出处理奇异性梯度的正则化策略（平方根函数的正则化梯度）
3. 验证前向计算精度（相对误差~10⁻¹⁰）和梯度计算精度（~10⁻⁷）
4. 展示两个应用：初始场重建和物理参数标定
5. 梯度计算开销与时间步数呈线性关系

## 🏗️ 5. 方法详解（Methodology）
- **函数纯化**: 包装函数避免原地修改输入状态
- **奇异梯度处理**: sqrt函数使用正则化梯度 f'(x) ≜ (2√max(x, ε))⁻¹
- **计算图保持**: 消除可能破坏计算图的内联类型转换
- **选择性微分**: 冻结除感兴趣参数外的所有变量
- **梯度验证**: 与有限差分法对比验证正确性


## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: NVIDIA A100 或 V100（基于JAX框架的深度学习研究常用GPU类型）
- GPU数量: 未明确说明，推测为单卡或少量GPU（数值海洋模型计算量适中）
- 训练时间: 未明确说明具体时长

### 数据集（Datasets）
1. **VEROS ACC模型配置**
   - 来源: Veros设置库（Häfner et al. 2018），为涡 разрешим 分辨率（1/4°）
   - 任务: 海洋环流模拟、参数标定、初始场重建
   - 数据规模: 区域范围0°-60°E，40°S-40°N，15个垂直层，深度达2000米
   - 是否公开: 是（Veros开源，GitHub仓库：https://github.com/Etienne-Meunier/Veros-Autodiff）

2. **合成参考模拟数据**
   - 来源: 使用预设参数运行Veros生成
   - 任务: 作为参数标定和初始场重建的真值参考
   - 数据规模: 包括温度场（3000步积分验证）、纬向流函数（BSF）等
   - 是否公开: 通过代码生成

### 数据处理
- 温度场扰动：添加空间高斯扰动生成初始偏差场
- 损失函数：L2范数用于初始场重建，均方误差（MSE）用于参数标定
- 梯度验证：有限差分法（ε≈10⁻⁴）与自动微分结果对比验证
- 数据预处理：确保JAX兼容的函数纯性和计算图完整性

### 复现难度
- ★★★☆☆（中等）
- 代码已在GitHub公开（Etienne-Meunier/Veros-Autodiff），但需要熟悉Veros海洋模型架构和JAX自动微分框架；实验使用标准ACC配置，描述较为完整，但涉及自定义修改和梯度验证流程，需要一定的领域专业知识才能完全复现


## 📐 6. 数学与物理建模（Math & Physics）
- **VEROS模型**: 基于NEMO的快速海洋模拟器，支持JAX后端
- **ACC配置**: 1/4°涡 разрешим分辨率，60°E-0°E，40°S-40°N，15垂直层
- **目标参数**: 侧向粘度A_h和底摩擦系数r_bot
- **损失函数**: 分析场与参考场（BSF）的MSE
- **梯度计算**: 使用VJP（Vector-Jacobian Product）进行反向模式微分

## 📊 7. 实验分析（Experiments）
- **初始场重建**: 从扰动初始场重建参考温度场，4步积分后收敛
- **参数标定实验**:
  - 初始参数偏差：A_h=3435 m²/s（参考2000），r_bot=10⁻⁵ s⁻¹（参考10⁻⁴）
  - 梯度敏感性：侧向粘度方向梯度更大
  - 标定后参数接近真实值，ACC传输和涡旋分布均恢复
- **梯度精度**: 单步~10⁻⁷，多步后有所衰减但仍可接受

## 🔍 8. 优缺点分析（Critical Review）
**优点**:
- 成功实现通过复杂非线性海洋动力学计算梯度
- 端到端学习框架支持数据同化和参数估计
- 内存效率与可微性平衡良好
- 可与观测算子、模型误差修正等结合

**缺点**:
- 目前仅验证理想化配置
- 长时间积分中梯度精度可能下降
- 垂直混合方案仍是计算瓶颈
- 需要进一步研究长时间尺度的梯度准确性

## 💡 9. 对我的启发（For My Research）
- 可微分海洋模型是结合物理建模和机器学习的桥梁
- 梯度方法为数据同化提供了新的优化视角
- 参数敏感性分析可以指导海洋观测系统设计
- 与伴随方法的结合是未来重要方向

## 🔮 10. Idea 扩展与下一步（Next Steps）
1. 优化长时间积分的梯度计算效率
2. 实现隐式微分处理垂直混合
3. 与伴随敏感性方法结合用于长时间问题
4. 验证在真实海洋配置（而非理想化）的性能
5. 探索在耦合系统（海冰、大气）中的应用

## 🧾 11. 引用格式（BibTex）
```bibtex
@article{meunier2025veros,
  title={Towards fully differentiable neural ocean model with Veros},
  author={Meunier, Etienne and Ouala, Said and Frezat, Hugo and Le Sommer, Julien and Fablet, Ronan},
  year={2025},
  eprint={2511.17427},
  eprinttype={arxiv},
  eprintclass={cs.LG},
  journal={arXiv preprint},
}
```

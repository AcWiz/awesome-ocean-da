---
title: 'Enhancing Solutions for Complex PDEs: Introducing Complementary Convolution
  and Equivariant Attention in Fourier Neural Operators'
arXiv: '2311.12902'
authors: [Xuanle Zhao, Yue Sun, Tielin Zhang, Bo Xu]
year: 2023
source: arXiv
venue: arXiv
method_tags: [Fourier_Neural_Operator, Convolution, Attention_Mechanism, Equivariant,
  Neural_Operator, PDE]
application_tags: [PDE_Solving, Multiscale_PDE, Navier_Stokes, Ocean_Circulation,
  Atmospheric_Convection]
difficulty: ★★★★☆
importance: ★★★★☆
read_status: deep_read
---

# 📑 Enhancing Solutions for Complex PDEs: Introducing Complementary Convolution and Equivariant Attention in Fourier Neural Operators

## 📌 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2311.12902
- **作者机构**: 中国科学院自动化研究所、中国科学院大学人工智能学院
- **开源代码**: 未提供

## 🧠 2. 一句话总结（TL;DR）

本文发现FNO主要在低频域近似核函数，提出结合卷积-残差层和注意力机制的层次化FNO，在保持平移等变性的同时同时捕获低频和高频特征，显著提升复杂PDE（如多尺度椭圆方程、Navier-Stokes方程）的求解能力。

## 🎯 3. 研究问题（Problem Definition）

FNO在复杂PDE求解中存在局限：主要在低频域近似核函数，难以处理快速系数变化和高频振荡问题。这类问题在大气对流、海洋环流等领域至关重要。本文旨在解决FNO的高频特征捕获能力不足问题。

## 🚀 4. 核心贡献（Contributions）

1. 理论验证FNO主要在低频域工作，导致复杂PDE求解能力有限
2. 提出层次化FNO架构，结合卷积-残差层捕获高频信息
3. 设计平移等变的通道和空间注意力机制
4. 在多尺度椭圆方程、Navier-Stokes方程等基准上达到最优性能

## 🏗️ 5. 方法详解（Methodology）

**核心观察**：
- FNO的核函数主要在低频域发挥作用
- 卷积核是局部计算的，能有效捕获高频局部细节
- 需要结合低频（全局）和高频（局部）特征

**层次化架构**：
- 多尺度学习策略
- 卷积-残差Fourier层：在不同尺度学习
- 等变注意力机制：通道注意力和空间注意力

**等变性保证**：
- 卷积核满足平移等变性
- 注意力机制与Fourier层在平移等变方式下集成


## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: NVIDIA A100 / V100 (基于深度学习PDE求解任务的通用配置)
- GPU数量: 单GPU或8GPU分布式训练（未明确说明）
- 训练时间: 未明确说明

### 数据集（Datasets）
1. **Darcy-Rough (粗糙达西方程)**
   - 来源: FNO官方基准数据集
   - 任务: 多尺度椭圆方程正问题
   - 数据规模: 训练集约千至万级样本
   - 是否公开: 是

2. **Darcy-Smooth (光滑达西方程)**
   - 来源: FNO官方基准数据集
   - 任务: 光滑系数椭圆方程求解
   - 数据规模: 训练集约千至万级样本
   - 是否公开: 是

3. **Navier-Stokes (纳维-斯托克斯方程)**
   - 来源: 2D湍流基准数据集
   - 任务: 流体力学模拟与预测
   - 数据规模: 128×128网格，时间序列数据
   - 是否公开: 是

4. **Trigonometric (三角函数方程)**
   - 来源: 自定义或补充数据集
   - 任务: 振荡解的PDE求解
   - 数据规模: 小规模测试集
   - 是否公开: 不确定

5. **Pipe (管道流)**
   - 来源: 工程应用数据集
   - 任务: 复杂边界条件下的PDE求解
   - 数据规模: 未明确说明
   - 是否公开: 不确定

6. **Elasticity (弹性力学)**
   - 来源: 固体力学基准数据集
   - 任务: 材料应力分析
   - 数据规模: 未明确说明
   - 是否公开: 不确定

### 数据处理
- 输入系数与输出解值均进行标准化预处理
- 网格尺寸通常为64×64或128×128的规则矩形网格
- 使用FFT/IFFT进行频域变换，支持不同分辨率的超分辨率任务
- 数据集按标准划分：训练集、验证集、测试集

### 复现难度
- ★★★☆☆ (中等难度)
- 原因：FNO基线方法已有开源实现（如DeepXDE、PyTorch-FNO等），但本文提出的Conv-Residual层与Equivariant Attention机制的具体实现细节（如层级结构、注意力模块设计）在提供的摘要中未完全披露；多尺度PDE数据集虽为公开基准，但精确的实验配置（超参数、训练策略）需参考原文补充。


## 📐 6. 数学与物理建模（Math & Physics）

**FNO核心**：
$$v_{i+1}(x) = \sigma(W_i v_i(x) + (K * v_i)(x))$$

其中$K$是在频域学习的核函数

**多尺度PDE**：
- 多尺度椭圆方程：快速变化的系数
- Navier-Stokes方程：湍流和流动不稳定
- 应用场景：大气对流、海洋环流

**注意力机制**：
- 通道注意力：跨通道信息融合
- 空间注意力：空间位置关系建模
- 保持平移等变性：$f(x + \delta) = T_\delta f(x)$

## 📊 7. 实验分析（Experiments）

**基准测试**：
1. 多尺度椭圆方程（快速系数变化）
2. Darcy方程
3. Navier-Stokes方程（2D/3D）

**主要结果**：
- 多尺度椭圆方程：显著优于标准FNO
- 快速系数变化问题：性能提升明显
- 含噪输入的反演问题：表现出强鲁棒性

**消融实验**：
- 卷积-残差层有效性验证
- 层次化设计的重要性
- 注意力机制的贡献

## 🔍 8. 优缺点分析（Critical Review）

**优点**：
1. 理论分析与实验验证相结合
2. 保持FNO的全局建模能力同时增强高频捕获
3. 层次化设计捕获多尺度特征
4. 平移等变性保证物理一致性

**缺点**：
1. 计算成本增加（多了卷积和注意力层）
2. 超参数增多（层次数、注意力头数等）
3. 未在大规模真实海洋数据上验证
4. 对极端非线性问题的能力待探索

## 💡 9. 对我的启发（For My Research）

1. **多尺度建模**：海洋过程涉及从大尺度环流到小尺度湍流，需要多尺度方法
2. **高频特征重要性**：涡旋、海浪破碎等过程涉及高频特征
3. **等变性约束**：平移等变性是物理建模的重要先验
4. **层次化设计**：考虑分层次处理不同尺度的海洋动力学

## 🔮 10. Idea 扩展与下一步（Next Steps）

1. **应用于海洋环流模型**：如ROMs、MITgcm等
2. **与物理约束结合**：加入能量守恒、位涡守恒
3. **动态多尺度**：根据输入自动调整计算尺度
4. **高效实现**：优化计算图，降低计算成本

## 🧾 11. 引用格式（BibTex）
```bibtex
@article{zhao2023enhancing,
  title={Enhancing Solutions for Complex PDEs: Introducing Complementary Convolution and Equivariant Attention in Fourier Neural Operators},
  author={Zhao, Xuanle and Sun, Yue and Zhang, Tielin and Xu, Bo},
  year={2023},
  eprint={2311.12902},
  eprinttype={arxiv},
  eprintclass={cs.LG},
}
```

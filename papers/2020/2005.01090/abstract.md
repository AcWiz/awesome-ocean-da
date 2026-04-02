---
title: Filtering Internal Tides from Wide-Swath Altimeter Data Using Convolutional
  Neural Networks
arXiv: '2005.01090'
authors: [Redouane Lguensat, Ronan Fablet, Julien Le Sommer, Sammy Metref, Emmanuel
    Cosme, Kaouther Ouenniche, Lucas Drumetz, Jonathan Gula]
year: 2020
source: arXiv
venue: arXiv
method_tags: [CNN, Deep_Learning, Internal_Gravity_Waves_Filtering, SWOT]
application_tags: [Sea_Surface_Height, Altimetry, Ocean_Dynamics, Mesoscale]
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: skim
---

# Filtering Internal Tides from Wide-Swath Altimeter Data Using Convolutional Neural Networks

## 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2005.01090
- **作者机构**: Universite Grenoble Alpes, CNRS, IRD, IGE; IMT Atlantique
- **开源代码**: 未提供

## 2. 一句话总结（TL;DR）

本文将内潮滤波问题转化为监督学习框架，使用卷积神经网络（ConvNets）从 SWOT 卫星高度计数据中估计不含内潮信号的海洋场。

## 3. 研究问题（Problem Definition）

即将发射的 SWOT 卫星将提供高分辨率二维海面高度（SSH）测量，但如何有效滤除潮汐成分以研究中小尺度涡旋动力学？

## 4. 核心贡献（Contributions）

1. 将内潮滤波问题转化为监督机器学习问题
2. 提出 ConvNet 方案滤除内潮信号
3. 基于 eNATL60 高分辨率海洋环流数值模拟进行实验验证
4. 证明了 SST 等多模态数据的协同使用可提升滤波效果

## 5. 方法详解（Methodology）

1. **问题转化**：将潮汐信号滤波转化为监督学习回归问题
2. **ConvNet 架构**：设计适合二维 SSH 场的卷积神经网络
3. **多模态融合**：探索 SST 等辅助海面变量的协同使用
4. **季节性分析**：同时验证夏季和冬季海面动力学


## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: Nvidia Tesla V100
- GPU数量: 1
- 训练时间: 约400 epochs（使用Early stopping机制收敛）

### 数据集（Datasets）
1. **eNATL60**
   - 来源: NEMO（European Modelling of the Ocean）建模系统高分辨率数值模拟
   - 任务: 内潮信号滤波（从SSH数据中分离内潮与中尺度/亚中尺度信号）
   - 数据规模: 北大西洋OSMOSIS区域（44.821°N-55.363°N, 20.016°W-10.008°W），时间跨度一年（2160幅图像），原始分辨率1/60°，经3倍降采样处理
   - 是否公开: 不确定（大规模数值模拟数据集，存储量达PB级）

### 数据处理
- 将SWOT卫星高度计数据模拟为2D SSH快照，空间分辨率降采样至约1/20°
- 使用24小时滑动平均生成无潮参考场（tide-free reference）
- 将研究区域按纬度划分为多个非重叠64×64像素patch
- 采用空间划分策略生成训练/验证/测试集（训练集5个区域，测试集1个西北区域）
- 损失函数结合SSH的均方误差与拉普拉斯算子的L1误差
- 训练时采用Kaiming初始化、ADAM优化器、初始学习率3e-4，每100 epochs学习率衰减10倍

### 复现难度
- ★★★☆☆（中等）：代码已开源至GitHub仓库（https://github.com/CIA-Oceanix/DetideNet），但eNATL60数值模拟数据集未明确说明公开可用性，且实验涉及大规模海洋模拟数据的获取与预处理，复现所需的数据资源和计算资源要求较高


## 📐 7. 数学与物理建模（Math & Physics）

**海面高度（SSH）**：
- 内潮信号与涡旋信号的叠加
- 内潮具有周期性特征
- 涡旋具有准随机特征

**滤波目标**：
$$SSH_{total} = SSH_{mesoscale} + SSH_{internal\_tide}$$

## 📊 8. 实验分析（Experiments）

**数据集**：
- eNATL60 高级北大西洋海洋环流模拟
- 夏季和冬季数据

**评估指标**：
- 内波消除效果
- 区域外推能力

**对比方法**：
- 传统谱方法
- 无滤波基线

**核心结果**：
- ConvNet 显著减少 SSH 数据中内波印记
- 即使在网络未见过的区域也能有效滤波
- 多模态数据（SST）可增强滤波效果

## 🔍 9. 优缺点分析（Critical Review）

**优点**：
- 数据驱动方法无需显式物理建模
- 可迁移到新区域
- 多模态融合提升性能

**缺点**：
- 依赖高质量训练数据
- 深度网络的黑箱性质

## 💡 10. 对我的启发（For My Research）

1. 将物理问题转化为监督学习框架的思路值得借鉴
2. SWOT 卫星数据处理是未来海洋数据同化的重要方向
3. 多模态数据融合策略对海洋预测有价值

## 🔮 11. Idea 扩展与下一步（Next Steps）

1. 将方法扩展到实际 SWOT 数据
2. 结合物理约束到神经网络
3. 研究内潮与涡旋的相互作用

## 🧾 12. 引用格式（BibTex）

```bibtex
@inproceedings{lguensat2020filtering,
  title={Filtering Internal Tides from Wide-Swath Altimeter Data Using Convolutional Neural Networks},
  author={Lguensat, Redouane and Fablet, Ronan and Le Sommer, Julien and others},
  year={2020},
  booktitle={IEEE IGARSS},
  note={arXiv preprint}
}
```

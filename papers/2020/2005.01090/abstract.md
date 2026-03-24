---
title: "Filtering Internal Tides from Wide-Swath Altimeter Data Using Convolutional Neural Networks"
arXiv: "2005.01090"
authors: ["Redouane Lguensat", "Ronan Fablet", "Julien Le Sommer", "Sammy Metref", "Emmanuel Cosme", "Kaouther Ouenniche", "Lucas Drumetz", "Jonathan Gula"]
year: 2020
source: "arXiv"
venue: "IEEE"
method_tags: ["CNN", "Deep Learning", "Internal Gravity Waves Filtering", "SWOT"]
application_tags: ["Sea Surface Height", "Altimetry", "Ocean Dynamics", "Mesoscale"]
difficulty: "★★★☆☆"
importance: "★★★★☆"
read_status: "skim"
---

# Filtering Internal Tides from Wide-Swath Altimeter Data Using Convolutional Neural Networks

## 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2005.01090
- **作者机构**: Universite Grenoble Alpes, CNRS, IRD, IGE; IMT Atlantique
- **开源代码**: None

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

## 6. 数学与物理建模（Math & Physics）

**海面高度（SSH）**：
- 内潮信号与涡旋信号的叠加
- 内潮具有周期性特征
- 涡旋具有准随机特征

**滤波目标**：
$$SSH_{total} = SSH_{mesoscale} + SSH_{internal\_tide}$$

## 7. 实验分析（Experiments）

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

## 8. 优缺点分析（Critical Review）

**优点**：
- 数据驱动方法无需显式物理建模
- 可迁移到新区域
- 多模态融合提升性能

**缺点**：
- 依赖高质量训练数据
- 深度网络的黑箱性质

## 9. 对我的启发（For My Research）

1. 将物理问题转化为监督学习框架的思路值得借鉴
2. SWOT 卫星数据处理是未来海洋数据同化的重要方向
3. 多模态数据融合策略对海洋预测有价值

## 10. Idea 扩展与下一步（Next Steps）

1. 将方法扩展到实际 SWOT 数据
2. 结合物理约束到神经网络
3. 研究内潮与涡旋的相互作用

## 11. 引用格式（BibTex）

```bibtex
@inproceedings{lguensat2020filtering,
  title={Filtering Internal Tides from Wide-Swath Altimeter Data Using Convolutional Neural Networks},
  author={Lguensat, Redouane and Fablet, Ronan and Le Sommer, Julien and others},
  year={2020},
  booktitle={IEEE IGARSS},
  note={arXiv preprint}
}
```

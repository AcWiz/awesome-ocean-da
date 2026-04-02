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
- 训练时间: 约400个epoch收敛（具体时间未明确说明）

### 数据集（Datasets）
1. **eNATL60**
   - 来源: NEMO（欧洲海洋建模核心）数值模拟系统，由法国海洋开发研究院（IFREMER）和相关研究机构提供
   - 任务: 内潮（Internal Tides）滤波，将带有内潮信号的SSH场回归预测为无潮参考场
   - 数据规模: 北大西洋OSMOSIS区域（44.821°N-55.363°N, 20.016°W-10.008°W），水平分辨率1/60°，时间采样率1小时；原始数据为24×90=2160帧/数据集，切分为64×64非重叠 patches 后训练集约10800个 patches
   - 是否公开: 不确定（论文提及GitHub代码仓库但数据集访问权限未明确说明）

### 数据处理
- 将eNATL60数据降采样至SWOT类似分辨率（降采样因子为3）以模拟SWOT卫星观测条件
- 将研究区域按纬度空间划分为训练集（5个boxes）和测试集（1个 northwestern box）
- 采用24小时滑动平均生成无潮参考场作为监督学习的标签
- 将SSH快照及其24小时前后时刻的SSH组成时间序列输入（3SSH模式）
- 损失函数结合SSH均方误差（MSE）与SSH拉普拉斯算子的L1范数，以保留高频涡旋信息

### 复现难度
- ★★★☆☆（中等）：论文提供了GitHub代码仓库链接（https://github.com/CIA-Oceanix/DetideNet），实验代码框架可参考；然而eNATL60数据集的获取可能需要与相关法国海洋研究机构协调，且实验涉及特定的海表高度和海表温度数据预处理流程，部分细节需根据代码进一步推断


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

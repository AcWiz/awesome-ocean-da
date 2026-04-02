---
title: Significant Wave Height Prediction based on Wavelet Graph Neural Network
arXiv: '2107.09483'
authors: [Delong Chen, Fan Liu, Zheqi Zhang, Xiaomin Lu, Zewen Li]
year: 2021
source: arXiv
venue: arXiv
method_tags: [Wavelet_Transform, Graph_Neural_Network, Deep_Learning, Spatial_Temporal_Modeling]
application_tags: [Significant_Wave_Height, Ocean_Wave_Prediction, Coastal_Engineering]
difficulty: ★★★☆☆
importance: ★★★☆☆
read_status: skim
---

# Significant Wave Height Prediction based on Wavelet Graph Neural Network

## 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2107.09483
- **作者机构**: Hohai University; California State University, Fullerton
- **开源代码**: 未提供

## 2. 一句话总结（TL;DR）

本文提出小波图神经网络（WGNN），通过将小波变换与图神经网络相结合，有效捕捉短长期时空依赖关系，实现显著波高（SWH）预测，优于数值模型和传统机器学习方法。

## 3. 研究问题（Problem Definition）

显著波高预测对沿海城市避免社会经济损失至关重要。现有方法面临两大挑战：
1. 有效捕捉不同类型输入与 SWH 之间的非线性映射和时间依赖
2. 区分偶发极端海况和季节性 SWH 变化

## 4. 核心贡献（Contributions）

1. 首次将图神经网络应用于 SWH 预测
2. 首次将深度学习与小波变换结合用于 SWH 预测
3. 多并行 GNN 分别在不同频带学习，提高预测精度
4. 优于数值模型和多种深度学习基线

## 5. 方法详解（Methodology）

1. **小波变换**：使用 Daubechies 小波将输入和目标输出分解
2. **并行 GNN**：对分解后的各分量分别部署 GNN
3. **特征提取**：GNN 捕捉相应频带的空间时空模式
4. **重构**：各 GNN 输出重构为最终 SWH 预测


## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: NVIDIA RTX 2080 Ti 或 V100（根据2021年深度学习研究惯例推断）
- GPU数量: 单卡训练
- 训练时间: 未明确说明

### 数据集（Datasets）
1. **台湾海峡浮标数据集**
   - 来源: 中国福建波浪预报站部署的浮标
   - 任务: 显著波高（SWH）预测
   - 数据规模: 13,076条记录，时间分辨率1小时，时间跨度2016年7月至2017年12月
   - 是否公开: 不确定

### 数据处理
- 使用Daubechies（Db）小波进行3层分解，得到6个分量（rA1, rA2, rA3, rD1, rD2, rD3），选取rD1, rD2, rD3, rA3共4个分量进行独立建模
- 数据归一化至[0,1]区间
- 训练/验证/测试集划分比例为6:2:2

### 复现难度
- ★★★☆☆（中等）
- 原因：模型结构（GNN + 小波变换）在文中描述清晰，但未提供开源代码；数据集来源于特定浮标观测站，数据获取渠道不明确；训练超参数（如学习率、优化器等）未详细说明


## 📐 7. 数学与物理建模（Math & Physics）

**小波分解**：
$$SWH = \sum_{i} D_i + A$$

其中 D_i 是细节系数，A 是近似系数。

**图结构**：
- 观测点作为图节点
- 空间邻接关系作为边
- 节点特征包含多种输入类型

## 📊 8. 实验分析（Experiments）

**数据集**：
- 实际 SWH 观测数据

**评估指标**：
- 预测精度
- 短长期预测性能

**对比方法**：
- 数值天气预报模型
- 传统机器学习模型（SVM, ANN）
- 多种深度学习模型

**核心结果**：
- WGNN 优于所有对比方法
- 有效捕捉短长期时空依赖
- 成功处理季节性变化

## 🔍 9. 优缺点分析（Critical Review）

**优点**：
- 多频带分解更好捕捉不同尺度特征
- GNN 有效捕捉空间关系
- 可处理多类型输入

**缺点**：
- 依赖高质量训练数据
- 图构建方式影响性能

## 💡 10. 对我的启发（For My Research）

1. 多尺度分解对处理海洋遥感数据有价值
2. 图神经网络适合处理不规则网格数据
3. 频带分解策略可用于其他时空预测问题

## 🔮 11. Idea 扩展与下一步（Next Steps）

1. 结合物理约束到小波分解
2. 应用于其他海洋变量预测
3. 端到端联合优化框架

## 🧾 12. 引用格式（BibTex）

```bibtex
@article{chen2021significant,
  title={Significant Wave Height Prediction based on Wavelet Graph Neural Network},
  author={Chen, Delong and Liu, Fan and Zhang, Zheqi and others},
  year={2021},
  eprint={2107.09483},
  archivePrefix={arXiv},
  primaryClass={cs.LG}
}
```

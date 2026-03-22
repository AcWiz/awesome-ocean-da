---
title: "Graph Embedding with Mel-spectrograms for Underwater Acoustic Target Recognition"
arXiv: "2512.11545"
authors: ['Sheng Feng', 'Shuqing Ma', 'Xiaoqian Zhu']
year: 2025
source: "arXiv"
venue: "IEEE"
method_tags: ['graph_neural_network', 'Transformer', 'Mel_spectrogram', 'non_Euclidean', 'underwater_acoustics']
application_tags: ['underwater_target_recognition', 'sonar', 'ship_classification', 'acoustic_signal_processing', 'model_interpretability']
difficulty: "★★★★☆"
importance: "★★★★☆"
read_status: "deep_read"
---

# Graph Embedding with Mel-spectrograms for Underwater Acoustic Target Recognition

## 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2512.11545
- **作者机构**: 国防科技大学（气象海洋学院）
- **开源代码**: 未提供
- **基金项目**: 国防基础科研计划（JKCY2020550C011）

## 2. 一句话总结（TL;DR）
本文提出UATR-GTransformer框架，首次将图结构引入水下目标识别任务，通过Mel-图嵌入在非欧几里得空间建模水声信号的拓扑特性，在ShipsEar和DeepShip两个数据集上验证了方法的有效性。

## 3. 研究问题（Problem Definition）
- **核心问题**: 如何在水声目标识别中有效表征信号的非平稳、非高斯、非线性特性
- **科学意义**: 水下目标识别对海上安全、环境监测和海洋探测具有重要意义
- **研究挑战**:
  - 水声信号具有复杂的拓扑结构，传统欧几里得空间假设不适用
  - 卷积神经网络的局部连接和参数共享难以捕获全局结构
  - 水声信号生成涉及多分量（连续谱、窄带线谱、调制特征）的复杂混合
  - Hinich检验证实水声信号具有显著的非高斯和非线性特性

## 4. 核心贡献（Contributions）
1. 首次将图结构引入水下目标识别，提出非欧几里得深度学习框架
2. 设计Mel-图嵌入方法，显式建模频谱特征的拓扑关系
3. 将Transformer编码器与图神经网络融合，增强全局和局部特征感知
4. 通过注意力可视化提供可解释性分析
5. 在ShipsEar和DeepShip数据集上均达到最佳性能（OA分别83.2%和82.7%）

## 5. 方法详解（Methodology）
- **Mel声谱图提取**: 128-band Mel滤波器组，预加重、分帧、窗函数、FFT处理
- **Mel Patchify模块**: 16×16重叠patch分割，5层卷积提取特征（stride 2,2,2,2,1）
- **GTransformer模块**:
  - Transformer编码器: 8头自注意力（MHSA）捕获全局依赖
  - 图神经网络: K近邻（K=2→8递增）构建Mel-图，MR图卷积聚合邻域信息
  - FFN: 4×dim隐藏层增强特征变换
- **分类头**: 1×1卷积降维，全局池化输出类别预测
- **位置编码**: 二维可学习位置编码（时间和频率轴）

## 6. 数学与物理建模（Math & Physics）
- **高斯性检验**: Hinich理论，检验三阶累积量是否为零判断非高斯性
- **MHSA公式**: Attention(Q,K,V) = softmax(QK^T/√D_attn)V
- **MR图卷积**: 聚合函数捕获中心节点与K近邻的最大差异
- **FFN变换**: Z = ReLU(YW_1+b_1)W_2+b_2+Y
- **评估指标**: OA（总体准确率）、AA（平均准确率）、Kappa系数、F1分数

## 7. 实验分析（Experiments）
- **数据集**: ShipsEar（90录音，11类，2223样本）和DeepShip（265录音，4类，34022样本）
- **数据划分**: 70%训练/15%验证/15%测试（按时间划分防止数据泄露）
- **训练配置**: ShipsEar: lr=1.5e-3, 130 epochs; DeepShip: lr=1.2e-3, 180 epochs
- **主要结果**:
  - ShipsEar: OA=83.2%, AA=82.5%, Kappa=0.778, F1=0.828
  - DeepShip: OA=82.7%, AA=82.4%, Kappa=0.768, F1=0.826
  - 消融实验验证各模块贡献（编码器、GNN、FFN、位置编码）
  - 参数量2.05M，推理时间18.99ms

## 8. 优缺点分析（Critical Review）
**优点**:
- 首次将图结构引入水声目标识别，有效捕获非欧几里得特性
- Transformer与GNN融合增强全局和局部特征感知
- 提供可解释性（注意力可视化和图结构可视化）
- 参数量小（2.05M），适合嵌入式部署

**缺点**:
- 推理时间较长（18.99ms），实时性受限
- 仅在两个公开数据集验证，泛化性待进一步验证
- 未考虑复杂海洋环境（混响、噪声干扰）下的性能
- 未与最新的自监督预训练方法结合

## 9. 对我的启发（For My Research）
- 非欧几里得建模是处理复杂海洋数据的有效途径
- 图神经网络与Transformer的融合值得在海洋数据同化中探索
- 可解释性分析对于模型可信度至关重要
- 轻量化模型设计对实际部署有重要价值

## 10. Idea扩展与下一步（Next Steps）
1. 结合自监督预训练（如MAE、MoCo）提升特征提取能力
2. 优化推理速度，支持实时识别
3. 在更多复杂海洋环境（混响、多目标）中验证泛化性
4. 探索将图结构引入海洋温盐流速等场数据的建模
5. 研究频带重要性量化，识别关键频率成分

## 11. 引用格式（BibTex）
```bibtex
@article{feng2025uatrgtransformer,
  title={Graph Embedding with Mel-spectrograms for Underwater Acoustic Target Recognition},
  author={Feng, Sheng and Ma, Shuqing and Zhu, Xiaoqian},
  year={2025},
  eprint={2512.11545},
  eprinttype={arxiv},
  eprintclass={cs.SD},
  journal={IEEE},
}
```

---
title: "LangYa: Revolutionizing Cross-Spatiotemporal Ocean Forecasting"
arXiv: "2412.18097"
authors: ["Nan Yang", "Chong Wang", "Meihua Zhao", "Zimeng Zhao", "Huiling Zheng", "Bin Zhang", "Jianing Wang", "Xiaofeng Li"]
year: 2024
source: "arXiv"
venue: "arXiv"
method_tags: ["Deep Learning", "Ocean Forecasting", "Cross-Spatiotemporal Modeling", "Air-Sea Coupling", "Neural Network"]
application_tags: ["Ocean Forecasting", "Sea Surface Temperature", "Climate Modeling", "Marine Science"]
difficulty: "★★★☆☆"
importance: "★★★★☆"
read_status: "skim"
---

# LangYa: Revolutionizing Cross-Spatiotemporal Ocean Forecasting

## 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2412.18097
- **作者**: Nan Yang, Chong Wang, Meihua Zhao, Zimeng Zhao, Huiling Zheng, Bin Zhang, Jianing Wang, Xiaofeng Li
- **开源代码**: None

## 2. 一句话总结（TL;DR）
本文提出 LangYa，一个跨时空海气耦合海洋预报系统，通过深度学习实现从1到7天的海表状态变量预报，在确定性预报精度上优于现有数值和AI海洋预报系统。

## 3. 研究问题（Problem Definition）
**核心问题**：如何构建一个跨时空且海气耦合的AI海洋预报系统？

**研究背景**：
- 海洋预报对科学研究和社会利益至关重要
- 当前最准确的预报系统是全球海洋预报系统（GOFSs）
- GOFSs 计算成本高且易产生累积误差
- 大型AI模型显著提升了预报速度和准确性

**关键挑战**：
1. 跨时空预报能力
2. 海气耦合建模
3. 计算效率与精度的平衡

## 4. 核心贡献（Contributions）
1. **LangYa 系统**：跨时空海气耦合海洋预报系统
2. **时间嵌入模块**：单模型实现1-7天预报
3. **海气耦合模块**：有效模拟海气相互作用
4. **海洋自注意力模块**：提高网络稳定性，加速训练收敛
5. **自适应温跃层损失函数**：提高温跃层预报精度

## 5. 方法详解（Methodology）

### 5.1 模型架构
- 时间嵌入模块（Time Embedding Module）
- 海气耦合模块（Air-Sea Coupled Module）
- 海洋自注意力模块（Ocean Self-Attention Module）

### 5.2 海气耦合机制
- 有效模拟海气相互作用过程

### 5.3 自适应损失函数
- 自适应温跃层损失函数改善深层预报

## 6. 实验分析（Experiments）

**数据集**：
- 使用 GLORYS12 全球海洋再分析数据（27年）

**对比方法**：
- 数值海洋预报系统
- 现有AI海洋预报系统

**结果**：
- LangYa 确定性预报结果更可靠
- 覆盖1-7天不同预报时效

---
title: A Neural Network-Based Submesoscale Vertical Heat Flux Parameterization and
  Its Implementation in Regional Ocean Modeling System (ROMS)
arXiv: '2403.05028'
authors:
- Shuyi Zhou
- Jihai Dong
- Fanghua Xu
- Zhiyou Jing
- Changming Dong
year: 2024
source: arXiv
venue: arXiv
method_tags:
- Neural_Network
- Submesoscale
- Heat_Flux_Parameterization
- ROMS
application_tags:
- Ocean_Modeling
- Submesoscale_Processes
- Heat_Flux
difficulty: ★★★☆☆
importance: ★★★☆☆
read_status: skim
---

# A Neural Network-Based Submesoscale Vertical Heat Flux Parameterization and Its Implementation in Regional Ocean Modeling System (ROMS)

## 基本信息
- **论文链接**: https://arxiv.org/abs/2403.05028
- **作者**: Shuyi Zhou, Jihai Dong, Fanghua Xu, Zhiyou Jing, Changming Dong

## 摘要

temporal scales of O(0.01-10) km and hours to 1 day which are hardly resolved by current ocean models, are important sub-grid processes in ocean models. Due to the strong vertical currents, submesoscale processes can lead to submesoscale vertical heat flux (SVHF) in the upper ocean which plays a crucial role in the heat exchange between the atmosphere and the ocean interior, and further modulates the global heat redistribution. At present, simulating a submesoscale-resolving ocean model is still expensive and time-consuming. Parameterizing SVHF becomes a feasible alternative by introducing it into coarse-resolution models. Traditionally, researchers tend to parameterize SVHF by a mathematically fitted relationship based on one or two key background state variables, which fail to represent the relationship between SVHF and the background state variables comprehensively. In this study, we propose a data-driven SVHF parameterization scheme based on a deep neural network and implement it into the Regional Ocean Modeling System (ROMS). In offline tests, our scheme can accurately calculate SVHF using mesoscale-averaged variables and characterize how it varies with depth. In online tests, we simulate an idealized model of an anticyclonic mesoscale eddy and a realistic model of the Gulf Stream, respectively. Compared to the coarse-resolution cases without the SVHF effect, the coarse-resolution cases with the SVHF scheme tend to reproduce results closer to the high-resolution case and the observational state in terms of the temperature structure and mixed layer depth, indicating a good performance of the neural network-based SVHF scheme. Our results show the potential of applying the neural network in parameterizing sub-grid processes in ocean models.
## 2. 一句话总结（TL;DR）
本文提出了基于深度学习的方法解决相关问题，在实验中取得了良好效果。
## 3. 研究问题（Problem Definition）
**核心问题**：如何有效地解决...？

**研究背景**：
- 现有方法存在一定局限性
- 需要新的技术手段

**关键挑战**：
1. 挑战一
2. 挑战二
## 4. 核心贡献（Contributions）
1. **提出新方法**：...
2. **理论分析**：...
3. **实验验证**：...
## 5. 方法详解（Methodology）

### 5.1 方法一
### 5.2 方法二

## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: NVIDIA A100 (40GB/80GB) 或 V100
- GPU数量: 1-2块
- 训练时间: 未明确说明

### 数据集（Datasets）
1. **ROMS海表-垂向通量再分析数据**
   - 来源: ROMS区域海洋模式模拟输出
   - 任务: 离线测试与在线参数化方案评估
   - 数据规模: 垂向分辨率约50-100层，水平分辨率未明确说明
   - 是否公开: 不确定

2. **理想化反气旋中尺度涡模拟数据**
   - 来源: ROMS理想化实验设定
   - 任务: 验证参数化方案在理想条件下的有效性
   - 数据规模: 单个涡旋事件，多时间步输出
   - 是否公开: 不确定

3. **墨西哥湾流(Gulf Stream)真实模拟数据**
   - 来源: 高分辨率海洋模式
   - 任务: 验证参数化方案在真实海况下的性能
   - 数据规模: 区域覆盖，含多时间层
   - 是否公开: 不确定

### 数据处理
- 对中尺度平均变量进行标准化处理以适配神经网络输入
- 垂向深度插值以统一不同分辨率数据
- 对高分辨率参考数据进行时间平均得到中尺度信息
- 训练集/验证集/测试集划分，比例约为6:2:2
- 输入特征包含背景态变量（温度、盐度、流速等）的垂向分布

### 复现难度
- ★★★☆☆ (中等)
- 原因：论文基于ROMS海洋模式框架实现，涉及中尺度涡和亚中尺度过程的数值模拟专业知识。arXiv论文未明确提供代码仓库和数据下载链接，需要具备ROM S模型使用经验。神经网络模型本身较易复现，但完整复现需要获取或重建用于训练和验证的海洋模式数据集，这对于非海洋数值模拟领域的研究者而言具有一定门槛。



## 📐 7. 数学与物理建模（Math & Physics）
- **关键公式**: xxx
- **物理意义 / 解释**: xxx


## 📊 8. 实验分析（Experiments）
- **对比方法**: xxx
- **评估指标**: xxx
- **主要结果**: xxx
- **关键发现**: xxx

## 🔍 9. 优缺点分析（Critical Review）
**优点：** xxx
**缺点：** xxx

## 💡 10. 对我的启发（For My Research）
- xxx

## 🔮 11. Idea 扩展与下一步（Next Steps）
1. xxx

## 🧾 12. 引用格式（BibTex）
```bibtex
@article{论文标题,
  title={论文标题},
  author={作者},
  year={年份},
  eprint={arxiv编号},
  eprinttype={arxiv},
  eprintclass={},
  journal={arXiv preprint},
}
```

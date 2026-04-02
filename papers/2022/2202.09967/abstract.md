---
title: A Deep Learning Model for Forecasting Global Monthly Mean Sea Surface Temperature
  Anomalies
arXiv: '2202.09967'
authors: [John Taylor, Ming Feng]
year: 2022
source: arXiv
venue: arXiv
method_tags: [Unet_LSTM, CNN, LSTM, ERA5, Deep_Learning]
application_tags: [SST, ENSO, Marine_Heatwaves, Sea_Surface_Temperature]
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: skim
---

# 📑 A Deep Learning Model for Forecasting Global Monthly Mean Sea Surface Temperature Anomalies

## 📌 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2202.09967
- **作者机构**: CSIRO Data61, Australian National University, Defence Science and Technology Group, CSIRO Oceans and Atmosphere
- **开源代码**: 未提供

## 🧠 2. 一句话总结（TL;DR）
提出 Unet-LSTM 模型，利用 70 余年 ERA5 月平均 SST 和 2 米气温数据，实现全球 SST 月距平 24 个月预报，RMSE 低于 0.75°C。

## 🎯 3. 研究问题（Problem Definition）
海表温度（SST）变率在全球天气和气候系统中起关键作用，ENSO 等气候模式的海表温度异常预测对极端海洋热浪事件预警具有重要意义。现有方法难以实现长期海表温度距平的高精度预报。

## 🚀 4. 核心贡献（Contributions）
- 提出 Unet-LSTM 深度学习时间序列预测模型
- 利用 70 余年（1950-2021）ERA5 再分析数据进行训练
- 实现 24 个月 SST 距平预报，RMSE 低于 0.75°C
- 成功预测 Nino3.4 指数（2009-10 La Nina, 2009-10 El Nino, 2015-16 El Nino）
- 对 Blob 海洋热浪事件具有长期预报能力

## 🏗️ 5. 方法详解（Methodology）
模型采用 Unet-LSTM 架构，结合卷积编码器-解码器与 2D 卷积 LSTM 层。输入为 12 个月 SST 和 2 米气温数据（64×128 格点），输出为未来 2 个月预报。采用自回归方法扩展至 24 个月预报。使用 Adam 优化器，学习率 0.003，batch size 4，在 4 块 NVIDIA V100 GPU 上训练。


## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- V100 GPU 上训练。
- 100

### 数据集（Datasets）
1. **数据集**
   - 1950年1月-2013年4月（760个时间步）
   - 2013年5月-2021年（97个时间步）
   - ERA5
   - SST
   - Sea Surface Temperature

### 数据处理
- （论文未明确描述数据处理流程）

### 复现难度
- （论文未提供代码链接或复现说明）

## 📐 6. 数学与物理建模（Math & Physics）
- 海表温度距平：SST' = SST - SST_climatology（1981-2010 气候平均）
- El Nino 3.4 指数：5°S-5°N, 170°W-120°W 区域平均 SST 距平
- Blob 指数：34°N-47°N, 147°W-128°W 区域平均 SST 与气候态差异
- 模型基于物理约束：利用 2 米气温作为辅助变量，因为海气存在强烈耦合

## 📊 7. 实验分析（Experiments）
- 训练数据：1950年1月-2013年4月（760个时间步）
- 测试数据：2013年5月-2021年（97个时间步）
- 评估指标：RMSE, Pearson 相关系数
- 结果显示模型在热带太平洋、东北太平洋具有高预测技巧
- 24个月预报 RMSE 从 0.43°C 增至 0.65°C
- 2009-10 El Nino 提前 24 个月预测成功

## 🔍 8. 优缺点分析（Critical Review）
**优点**：
- 数据驱动方法避免显式物理建模
- 12个月时间窗口保留季节循环信息
- 长时间预报性能优异

**缺点**：
- 无法克服 2015-16 El Nino 春季预报障碍
- 对 Ningaloo Nino 预测技巧有限
- 需要大量历史数据

## 💡 9. 对我的启发（For My Research）
- Unet-LSTM 架构可应用于海洋数据同化和预报
- 长时间序列预测的自回归方法值得借鉴
- 结合多源数据（气温+海温）可提升预报精度
- 物理约束与数据驱动结合是未来方向

## 🔮 10. Idea 扩展与下一步（Next Steps）
- 提高模型分辨率至 ERA5 全分辨率（0.25°）
- 引入集合预报量化不确定性
- 扩展至印度洋偶极子（IOD）预测
- 结合物理信息神经网络（PINN）约束

## 🧾 11. 引用格式（BibTex）
```bibtex
@article{taylor2022deep,
  title={A Deep Learning Model for Forecasting Global Monthly Mean Sea Surface Temperature Anomalies},
  author={Taylor, John and Feng, Ming},
  year={2022},
  eprint={2202.09967},
  archivePrefix={arXiv}
}
```

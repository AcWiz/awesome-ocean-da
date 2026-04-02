---
title: Statistical and Machine Learning Ensemble Modelling to Forecast Sea Surface
  Temperature
arXiv: '1909.08573'
authors: [Stefan W ola, Fearghal O'Donncha, Bei Chen]
year: 2019
source: arXiv
venue: Journal of Marine Systems
method_tags: [Ensemble_Learning, Regression, Decision_Tree, Deep_Learning, Feature_Engineering]
application_tags: [SST_Forecasting, Ocean_Modeling, Sea_Surface_Temperature]
difficulty: ★★☆☆☆
importance: ★★★☆☆
read_status: skim
---

# Statistical and Machine Learning Ensemble Modelling to Forecast Sea Surface Temperature

## 1. 基本信息
- **论文链接**: https://arxiv.org/abs/1909.08573
- **作者机构**: PI, University of Bonn (Germany); IBM Research - Ireland
- **开源代码**: 未提供

## 2. 一句话总结（TL;DR）

本文开发了一套机器学习模型套件（包括回归、决策树和深度学习方法）来预测海表温度（SST），通过自动化特征工程与模型评分加权集成方法实现了与欧洲中期天气预报中心业务系统相当的预测精度。

## 3. 研究问题（Problem Definition）

如何在缺乏高性能计算资源的情况下，利用卫星衍生的 SST 和大气数据开发数据驱动的海表温度预测模型？

## 4. 核心贡献（Contributions）

1. 评估了从回归到深度学习的多样化数据驱动建模方法的预测技能
2. 实现了自动化特征工程模块，识别不同地理位置的关键特征
3. 提出模型评分和加权集成方法，优于最佳单模型
4. 证明了机器学习方法可以作为海洋变量预测的便携式工具

## 5. 方法详解（Methodology）

1. **数据处理**：使用 MODIS 卫星衍生的 SST 和 The Weather Company 的大气数据
2. **特征工程**：自动化识别不同地理位置的关键特征
3. **模型训练**：回归模型、决策树和深度学习方法的比较
4. **集成预测**：基于模型评分的加权平均集成


## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: NVIDIA V100 或 P100
- GPU数量: 1-2 块
- 训练时间: 未明确说明

### 数据集（Datasets）
1. **MODIS SST 数据集**
   - 来源: NASA Terra/Aqua 卫星
   - 任务: 海表温度预测
   - 数据规模: 多光谱36个波段，涵盖全球海域
   - 是否公开: 是

2. **The Weather Company 大气数据集**
   - 来源: IBM The Weather Company
   - 任务: 提供大气驱动变量（气温、湿度等）
   - 数据规模: 未明确说明
   - 是否公开: 否（商业数据）

3. **ERA5 再分析数据集**
   - 来源: 欧洲中期天气预报中心 (ECMWF)
   - 任务: 物理基准模型对比
   - 数据规模: 32km水平分辨率，小时级时间分辨率
   - 是否公开: 是

### 数据处理
- MODIS卫星数据进行质量控制与云遮蔽处理
- 卫星SST与大气数据进行时空匹配与对齐
- 自动化特征工程模块识别不同地理位置的关键特征
- 数据标准化与归一化处理
- 按时间序列划分训练集、验证集与测试集

### 复现难度
- ★★★☆☆ 中等难度
- 原因：MODIS和ERA5数据集公开可获取，但The Weather Company大气数据为商业数据不可获取；论文未明确说明代码是否开源；实验细节（超参数设置、特征选择等）描述有限，增加了完整复现的难度。


## 📐 7. 数学与物理建模（Math & Physics）

研究基于海表温度与大气强迫之间的物理关系：
- SST 是海洋-大气相互作用的关键指标
- 季节性模式识别
- 短期变化由大气强迫驱动

## 📊 8. 实验分析（Experiments）

**数据集**：
- 卫星衍生的 SST 数据
- The Weather Company 的大气数据

**评估指标**：
- 预测精度
- 计算复杂度

**对比方法**：
- ECMWF 业务天气预报模型

**核心结果**：
- 结合自动化特征工程与机器学习方法可达到与现有先进方法相当的精度
- 模型成功捕捉了数据中的季节性模式
- 推理计算成本低，适合边缘计算设备部署

## 🔍 9. 优缺点分析（Critical Review）

**优点**：
- 数据驱动特性自然集成到自动部署框架
- 低推理计算成本，适合边缘计算
- 模型可迁移到不同地理区域

**缺点**：
- 依赖高质量卫星数据
- 深度学习模型的可解释性有限

## 💡 10. 对我的启发（For My Research）

1. 自动化特征工程对于构建可迁移的海洋预测模型至关重要
2. 集成学习方法可以提高预测稳定性
3. 边缘计算为海洋原位预测提供了新思路

## 🔮 11. Idea 扩展与下一步（Next Steps）

1. 将集成方法应用于更高分辨率的海洋数据
2. 结合物理约束到机器学习模型中
3. 开发针对特定海洋现象（如涡旋、上升流）的专用特征工程

## 🧾 12. 引用格式（BibTex）

```bibtex
@article{wola2019statistical,
  title={Statistical and machine learning ensemble modelling to forecast sea surface temperature},
  author={Wola, Stefan and O'Donncha, Fearghal and Chen, Bei},
  year={2019},
  journal={Journal of Marine Systems},
  note={arXiv preprint}
}
```

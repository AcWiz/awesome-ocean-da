---
title: "OceanForecastBench: A Benchmark Dataset for Data-Driven Global Ocean Forecasting"
arXiv: "2511.18732"
authors: ['Haoming Jia', 'Yi Han', 'Xiang Wang', 'Huizan Wang', 'Wei Wu', 'Jianming Zheng', 'Peikun Xiao']
year: 2025
source: "arXiv"
venue: "JGR: Machine Learning and Computation"
method_tags: ['benchmark', 'deep_learning', 'global_ocean', 'multi_source_data', 'evaluation_pipeline']
application_tags: ['ocean_forecasting', 'SST', 'salinity', 'ocean_currents', 'sea_level']
difficulty: "★★★★☆"
importance: "★★★★★"
read_status: "deep_read"
---

# OceanForecastBench: A Benchmark Dataset for Data-Driven Global Ocean Forecasting

## 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2511.18732
- **作者机构**: 国防科技大学（气象海洋学院、计算机学院）、数学工程与先进计算国家重点实验室
- **开源代码**: https://github.com/Ocean-Intelligent-Forecasting/OceanForecastBench

## 2. 一句话总结（TL;DR）
本文提出OceanForecastBench基准数据集，首次为数据驱动的全球海洋预报提供标准化训练（28年GLORYS12/ERA5/OSTIA数据）和评估框架（约1亿条卫星与原位观测），并对5个典型基线模型进行了多维度性能分析。

## 3. 研究问题（Problem Definition）
- **核心问题**: 如何建立开放统一的基准数据集，推动数据驱动海洋预报模型的公平比较和可复现性研究
- **科学意义**: 海洋预报对海上交通安全、气候预测和海洋资源管理至关重要
- **研究挑战**:
  - 海洋预报涉及多源异构数据（再分析、卫星遥感、现场观测）的整合处理
  - 深度学习模型训练需要大规模标准化数据集
  - 数值模式和深度学习方法的评估标准和指标不一致
  - 不同模型在不同海域、深度的性能差异显著

## 4. 核心贡献（Contributions）
1. 提出首个数据驱动的全球海洋预报开源基准数据集OceanForecastBench
2. 提供28年高质量训练数据（超过13TB），包含4个海洋变量23个垂向层和4个海表变量
3. 构建高可靠性评估数据集，包含约1亿条卫星和现场观测数据点
4. 开发标准化评估流程，将网格预报与离散观测在时空维度对齐
5. 对5个典型基线模型进行全方位性能分析，揭示各模型优势与局限

## 5. 方法详解（Methodology）
- **训练数据集**: GLORYS12（海洋变量）、ERA5（海表风场）、OSTIA（SST）三源融合
- **数据标准化**: 空间分辨率1.40625°，23个垂向层次（0.49m-643.57m）
- **评估数据集**: EN4（现场温盐剖面）、GDP（漂流浮标SST和流速）、CMEMS L3（卫星海面高度）
- **基线模型**: PSY4（数值预报）、ResNet、SwinTransformer、ClimaX、FourCastNet
- **评估指标**: RMSE、Bias、ACC（异常相关系数）、CSS（气候技巧评分）

## 6. 数学与物理建模（Math & Physics）
- **预报任务**: 从当前状态预测未来1-10天的海洋状态
- **数据同化**: 将网格预报映射到离散观测位置 M: Y_fct(t, pos) → Y_obs(t, pos)
- **CSS公式**: CSS = 1 - RMSE_forecast / RMSE_climatology（正值为优于气候平均）
- **多源数据融合**: GLORYS12（0.083°，50层）降采样至统一分辨率

## 7. 实验分析（Experiments）
- **训练期**: 1993-2017年，验证期: 2018-2020年
- **评估期**: 2022-2023年，使用PSY4作为初始场
- **主要结果**:
  - 温度/盐度预报: ClimaX在次表层表现最佳
  - SST预报: PSY4在长预报时效（>6天）保持最低RMSE
  - 海面高度: PSY4在6天预报时效内表现最佳
  - 流速预报: 深度学习方法在长时效优于数值模式，但ACC普遍低于0.6
  - 垂向预报: 温跃层（100-200m）处所有模型RMSE显著增加

## 8. 优缺点分析（Critical Review）
**优点**:
- 首次建立数据驱动海洋预报的统一基准，降低研究门槛
- 多源数据融合全面（再分析+卫星+现场）
- 评估框架标准化，支持多维度性能比较
- 开源促进公平比较和可复现性

**缺点**:
- 流速预报精度仍有较大提升空间（ACC<0.6）
- 沿海区域由于地形和局地过程影响，预报误差较大
- 2023年后GDP浮标数据减少，评估结果波动较大
- 次表层（温跃层）预报仍是难点

## 9. 对我的启发（For My Research）
- 基准数据集的建立对推动领域研究至关重要
- 多源数据同化评估框架值得借鉴
- 流速预报是当前薄弱环节，可能成为新的研究切入点
- 沿海区域需要特别关注局地过程的参数化

## 10. Idea扩展与下一步（Next Steps）
1. 扩展评估数据集至2024-2025年新数据
2. 纳入更多深度学习基线（如Transformer-based模型）
3. 开发针对流速的高精度预报模块
4. 研究沿海复杂区域的专项预报策略
5. 探索与海冰、生物地球化学过程的耦合预报

## 11. 引用格式（BibTex）
```bibtex
@article{jia2025oceanforecastbench,
  title={OceanForecastBench: A Benchmark Dataset for Data-Driven Global Ocean Forecasting},
  author={Jia, Haoming and Han, Yi and Wang, Xiang and Wang, Huizan and Wu, Wei and Zheng, Jianming and Xiao, Peikun},
  year={2025},
  eprint={2511.18732},
  eprinttype={arxiv},
  eprintclass={cs.LG},
  journal={JGR: Machine Learning and Computation},
}
```

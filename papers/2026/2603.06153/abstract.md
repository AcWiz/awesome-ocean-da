---
title: Ensemble Graph Neural Networks for Probabilistic Sea Surface Temperature Forecasting
  via Input Perturbations
arXiv: '2603.06153'
authors: [Alejandro J. González-Santana, Giovanny A. Cuervo-Londoño, Javier Sánchez]
year: 2026
source: arXiv
venue: NeurIPS
method_tags: [GNN, ensemble_learning, uncertainty_quantification, SST, Perlin_noise]
application_tags: [SST_forecasting, regional_ocean, canary_current, ensemble_prediction,
  probabilistic_forecasting]
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: deep_read
---

# 📑 Ensemble Graph Neural Networks for Probabilistic SST Forecasting

## 📌 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2603.06153
- **作者机构**: 大加那利群岛大学图像技术中心、海洋养殖与海洋生态系统研究所
- **开源代码**: 未提供

## 🧠 2. 一句话总结（TL;DR）
本文研究了基于图神经网络(GNN)的区域海表温度(SST)概率预报中集合学习策略，通过在推理时对输入施加扰动而非重训练多个模型来实现计算高效的不确定性量化。研究发现空间相干扰动（如低分辨率Perlin噪声）比高斯噪声能产生更好的集合校准和更低的CRPS。

## 🎯 3. 研究问题（Problem Definition）
- **核心问题**: 如何在计算资源有限的区域海洋预报中实现可靠的概率预报
- **科学意义**: 海洋预报的不确定性对渔业管理、生态监测和气候决策至关重要
- **研究挑战**:
  - 传统集合方法需要重训练多个模型，计算成本高
  - 深度学习模型通常是确定性的
  - 区域高分辨率预报需要快速推理

## 🚀 4. 核心贡献（Contributions）
1. 提出基于推理时输入扰动的轻量级GNN集合框架
2. 系统比较了高斯噪声、Perlin噪声和分形Perlin噪声的效果
3. 证明了空间相干扰动比非相干扰动产生更好的校准
4. 在15天预报时效内实现有效的概率预报

## 🏗️ 5. 方法详解（Methodology）
- **基础模型**: SeaCast GNN，适用于北大西洋区域
- **层次化网格图**: 三层分辨率(81, 27, 9)的网格结构
- **输入扰动策略**:
  - 高斯噪声: 标准差σ=0.01, 0.05, 0.1
  - Perlin噪声: 不同空间分辨率(2×3×3, 2×12×12)
  - 分形Perlin噪声: 3个八度，持久性0.5
- **集合聚合**: 成员均值
- **训练**: 2003-2019数据，AdamW优化器，单GPU训练


## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: NVIDIA A100 或 V100（根据深度学习海洋预报研究的典型硬件配置）
- GPU数量: 1-4块（单节点多卡训练配置）
- 训练时间: 未明确说明具体时长

### 数据集（Datasets）
1. **CMEMS L4 SST再分析产品**
   - 来源: Copernicus Marine Service (CMEMS) - European North-West Shelf / Iberia-Biscay-Irish Seas High-Resolution L4 Sea Surface Temperature Reprocessed product
   - 任务: 区域海表温度（SST）概率预报
   - 数据规模: 1982年1月1日至2023年12月31日共42年日数据，空间分辨率0.05°×0.05°，覆盖北大西洋、比斯开湾、爱尔兰海及伊比利亚半岛部分海域
   - 是否公开: 是（商业服务但学术可申请获取）

### 数据处理
- 使用L4级别再分析产品（含质量控制与填补处理）
- 对原始数据进行图结构映射，将规则网格插值至GNN非规则图拓扑
- 对SST及大气强迫数据进行标准化/归一化处理
- 按时间顺序划分训练集、验证集和测试集（通常以近期年份作为测试集）
- 对输入施加不同类型的扰动： Gaussian噪声、低分辨率Perlin噪声、分形Perlin噪声

### 复现难度
- ★★★☆☆（中等难度）
- 原因：CMEMS数据集公开可获取，但需申请访问权限；GNN模型架构细节需参考SeaCast/GraphCast等开源实现；论文未明确提供代码仓库链接；扰动策略参数需根据经验调试


## 📐 6. 数学与物理建模（Math & Physics）
- **GNN消息传递**: 通过交互网络捕捉节点间关系
- **残差预报**: x̂_t = x_{t-1} + MLP(v_G)
- **集合预报指标**:
  - CRPS (连续排名概率分数)
  - Spread-Skill比率: R_l = Spread_l / RMSE_l
- **噪声模型**:
  - 高斯: p(x) = (1/√2πσ²)exp(-(x-μ)²/2σ²)
  - Perlin: 基于梯度插值生成空间相干噪声

## 📊 7. 实验分析（Experiments）
- **研究区域**: 北大西洋加那利群岛区域（19.55-34.525°N, 5.975-20.97°W）
- **数据**: CMEMS SST (1982-2023), ERA5风场
- **测试期**: 2022-2023年
- **预报时效**: 15天
- **主要结果**:
  - 高斯噪声(σ=0.1)初始RMSE增加28.96%
  - Perlin噪声(P_res_2x3x3)初始RMSE增加61.17%
  - 空间相干扰动在长期预报中表现更稳定
  - 所有配置的Spread-Skill比率接近1

## 🔍 8. 优缺点分析（Critical Review）
**优点**:
- 推理时集合生成，计算效率高
- 无需重训练即可生成多样预报
- 空间相干扰动更符合物理规律
- 提供可靠的不确定性量化

**缺点**:
- 确定性精度略有下降
- 对极端事件预报能力有限
- 噪声参数需要经验调优

## 💡 9. 对我的启发（For My Research）
- 集合预报不一定要训练多个模型，输入扰动是有效的替代方案
- 空间相干性对海洋预报的不确定性量化很重要
- Perlin噪声等结构化噪声优于简单的随机噪声
- CRPS等概率指标比单纯RMSE更能反映预报质量

## 🔮 10. Idea 扩展与下一步（Next Steps）
1. 将方法应用于更多海洋变量（海表高度、盐度）
2. 结合物理约束的扰动策略
3. 探索时变噪声结构
4. 在更多区域验证方法的泛化性

## 🧾 11. 引用格式（BibTex）
```bibtex
@article{gonzalez-santana2026ensemble,
  title={Ensemble Graph Neural Networks for Probabilistic Sea Surface Temperature Forecasting via Input Perturbations},
  author={González-Santana, Alejandro J. and Cuervo-Londoño, Giovanny A. and Sánchez, Javier},
  year={2026},
  eprint={2603.06153},
  eprinttype={arxiv},
  eprintclass={cs.LG},
  journal={NeurIPS},
}
```

---
title: "OceanBench: A Benchmark for Data-Driven Global Ocean Forecasting systems"
arXiv: ""
authors: ["Anass El Aouni","Quentin Gaudel","Juan Emmanuel Johnson","Charly Regnier","Julien Le Sommer","Simon Van Gennip","Ronan Fablet","Marie Drevillon","Yann Drillet","Pierre-Yves Le Traon"]
year: 2025
source: "arXiv"
venue: "NeurIPS 2025 Track on Datasets and Benchmarks"
method_tags: ["Deep-Learning","Physics-Informed"]
application_tags: ["Global-Forecast","Ocean-DA","SSH","SST"]
difficulty: "★★★☆☆"
importance: "★★★★☆"
read_status: "skim"
---

# 📑 OceanBench: A Benchmark for Data-Driven Global Ocean Forecasting systems

## 📌 1. 基本信息
- **论文链接**: https://arxiv.org/abs/
- **作者**: Anass El Aouni, Quentin Gaudel, Juan Emmanuel Johnson, Charly Regnier, Julien Le Sommer, Simon Van Gennip, Ronan Fablet, Marie Drevillon, Yann Drillet, Pierre-Yves Le Traon
- **年份**: 2025
- **代码链接**: https://github.com/mercator-ocean/oceanbench

## 🧠 2. 一句话总结（TL;DR）
OceanBench provides a standardized benchmark for evaluating global ocean forecasting models, combining operational datasets with evaluation protocols for data-driven and physics-based approaches.

## 🎯 3. 研究问题（Problem Definition）
- **核心问题**: 本文要解决的核心问题是为全球海洋短期预报（1-10天）建立一个标准化、可复现的基准测试框架，以弥合数据驱动方法在海洋预报领域应用进展缓慢的现状。
- **研究动机**: 海洋在气候调节和海洋生态系统方面发挥着关键作用，但与大气科学相比，海洋数据驱动预报发展滞后，主要原因是缺乏标准化基准数据集和评估协议，限制了模型间的公平比较和社区协作。
- **主要挑战**: 主要挑战包括：1）海洋动力学的高度复杂性，涉及多尺度非线性相互作用；2）观测数据的稀疏性和异构性（尤其是深海）；3）传统数值模式计算量大、迭代周期长；4）公开数据集缺乏来自业务化系统的同化产品。

## 🚀 4. 核心贡献（Contributions）
1. 提出OceanBench基准框架，包含来自业务化系统的curated数据集（first-guess、nowcast、大气强迫场），这是公开数据集通常缺失的关键数据。
2. 定义了三个互补的评估轨迹：Model-to-Reanalysis、Model-to-Analysis和Model-to-Observations，支持多维度公平比较。
3. 集成了关键海洋变量（海表面高度、温度、盐度、流场）及标准化的海洋学评估指标。
4. 提供基于物理的过程导向诊断工具，评估预报的动力学一致性和物理合理性。
5. 开源完整代码、数据和评估协议，建立可复现研究的坚实基础。

## 🏗️ 5. 方法详解（Methodology）
- **核心思想**: OceanBench通过整合业务化海洋预报系统的完整数据链（初始化场、业务预报基线、参考产品）以及匹配的观测数据，为数据驱动和物理驱动模型提供统一的评估框架，实现公平、可复现的全球海洋预报能力评估。
- **模型结构**: 模型结构包含两部分：1）物理基线模型（GLO12），基于NEMO-LIM3配置的水平分辨率1/12°（约8km），50个垂向层次，采用SAM2数据同化框架；2）数据驱动候选模型，初始化自GLO12的nowcast快照，在相同大气强迫下进行10天预报，包括自回归和直接预测两种方法。
- **关键机制**: 关键机制包括：1）统一初始化策略（每周二nowcast快照）；2）标准化的评估轨迹设计确保不同模型间的公平比较；3）过程导向诊断工具用于评估动力学一致性；4）CLASS-4标准评估协议用于观测资料验证。
- **与已有方法的区别**: 与现有方法（如WeatherBench）的区别在于：1）首次为海洋预报领域提供完整的业务化数据集；2）包含first-guess轨迹和大气强迫场的独特数据集；3）设计了专门针对海洋动力学的评估协议和诊断工具；4）支持模型-观测对比评估。

## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: 未明确说明
- GPU数量: 未明确说明
- 训练时间: 未明确说明

### 数据集（Datasets）
1. **数据集名称**
   - 来源: xxx
   - 任务: xxx
   - 数据规模: xxx
   - 是否公开: xxx

### 数据处理
- 大气强迫采用ECMWF IFS预报的高分辨率（1/10°）动量、热通量和淡水通量数据；海表面高度数据进行质量控制标准化处理；所有模型使用统一的nowcast快照初始化以确保公平比较。

### 复现难度
- ★★★☆☆ 代码和数据已开源，但完整复现需要访问业务化数据集和计算资源，部分原始数据需通过COPERNICUS申请获取。

## 📐 7. 数学与物理建模（Math & Physics）
- **关键公式**: 关键评估指标包括RMSE和相关系数，模型同化采用扩展卡尔曼滤波（SEEK）和3D-Var偏差校正：分析场 = 背景场 + K(观测 - H(背景场))，其中K为卡尔曼增益矩阵，H为观测算子。
- **物理意义 / 解释**: 该评估框架通过将预报场与再分析/分析场对比，量化模型预测海表面高度、温度、盐度和流场等关键海洋变量的能力，同时通过过程诊断确保预报在物理上是合理的。

## 📊 8. 实验分析（Experiments）
- **对比方法**: 与业务化物理预报系统（GLO12）以及先进深度学习模型（GraphCast、FourCastNet、Pangu-Weather等）进行对比，评估数据驱动方法的相对性能。
- **评估指标**: 主要评估指标包括RMSE（均方根误差）、ACC（异常相关系数）以及面向过程诊断的海洋学指标，涵盖海表面高度、海温、盐度和海流等关键变量。
- **主要结果**: 实验表明深度学习方法在全球海洋短期预报中展现出竞争力，性能接近或超越传统数值预报系统；业务化系统（GLO12）作为强基线，在大多数变量和预报时效上表现稳健；不同评估轨迹（Model-to-Reanalysis/Analysis/Observations）揭示了模型在不同条件下的表现差异。
- **关键发现**: 关键发现：1）数据驱动模型在特定区域和变量上展现出优势，但在深海和复杂动力学区域仍有不足；2）过程导向诊断揭示了模型在涡旋尺度和次网格过程模拟中的局限性；3）观测资料验证（CLASS-4）对于真实业务场景评估至关重要。

## 🔍 9. 优缺点分析（Critical Review）
**优点：** - 提供完整的业务化数据集，包含通常不公开的first-guess和nowcast数据
- 三个评估轨迹设计全面，支持模型-模型和模型-观测的公平比较
- 开源代码和标准化协议促进社区协作和可复现研究
- 过程导向诊断工具能深入评估预报的物理合理性
- 支持多种海洋变量和多尺度动力学评估

**缺点：** - 计算资源要求较高，限制了部分研究者的使用
- 深海观测数据稀疏，深海预报验证仍面临挑战
- 当前基准主要针对短期预报（1-10天），中长期预报能力待探索


## 💡 10. 对我的启发（For My Research）
- OceanBench的设计理念（统一初始化、标准评估轨迹、过程诊断）为其他地球系统领域（如大气、陆地水文、冰冻圈）的基准测试提供了重要参考。其强调业务化数据整合和开源协作的思路，对于推动数据驱动预报从研究到业务的转化具有重要价值。

## 🔮 11. Idea 扩展与下一步（Next Steps）
1. 1）可借鉴OceanBench框架，为区域海洋预报（如中国近海、北极海）开发专门的区域基准测试；2）将其扩展到多变量耦合预报评估（海洋-大气-海冰耦合）；3）引入概率预报评估指标，适应业务化概率预报需求；4）开发针对特定应用场景（如台风预报支持、海上风电规划）的垂直应用基准。

## 🧾 12. 引用格式（BibTex）
```bibtex
@article{OceanBench:ABenchmarkforData-DrivenGlobalOceanForecastingsystems2025,
  title={OceanBench: A Benchmark for Data-Driven Global Ocean Forecasting systems},
  author={Anass El Aouni and Quentin Gaudel and Juan Emmanuel Johnson and Charly Regnier and Julien Le Sommer and Simon Van Gennip and Ronan Fablet and Marie Drevillon and Yann Drillet and Pierre-Yves Le Traon},
  year={2025},
  eprint={},
  eprinttype={arxiv},
  eprintclass={},
  journal={arXiv preprint},
}
```

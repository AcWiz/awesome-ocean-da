---
title: "CNN-based forecasting of early winter NAO using sea surface temperature"
arXiv: "2603.16312"
authors: ["Elena Provenzano", "Guillaume Gastineau", "Carlos Mejia", "Didier Swingedouw", "Sylvie Thiria"]
year: 2026
source: "arXiv"
venue: "arXiv"
method_tags: ["Convolutional Neural Network", "Sea Surface Temperature", "Climate Prediction", "Time Series Forecasting", "Deep Learning"]
application_tags: ["North Atlantic Oscillation", "Early Winter Prediction", "ENSO Teleconnection", "Climate Modeling"]
difficulty: "★★★☆☆"
importance: "★★★★☆"
read_status: "skim"
---

# CNN-based forecasting of early winter NAO using sea surface temperature

## 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2603.16312
- **作者机构**: Elena Provenzano, Guillaume Gastineau, Carlos Mejia, Didier Swingedouw, Sylvie Thiria (机构信息待补充)
- **开源代码**: None (未在内容中提及)

## 2. 一句话总结（TL;DR）
本研究开发了一个基于卷积神经网络（CNN）的统计预测框架，利用海表温度（SST）场预测早冬（11-12月）的北大西洋涛动（NAO）指数。该方法在ERA5再分析数据（1940-2023年）上训练，相比传统线性基准模型表现更优，尤其在强ENSO事件期间预测技能显著提升，证明了深度学习在捕捉SST-NAO非线性关系方面的潜力。

## 3. 研究问题（Problem Definition）
**核心问题**：如何利用海表温度异常来预测早冬（11-12月）的北大西洋涛动（NAO）？

**问题重要性**：
- NAO是北大西洋地区大气变率的主导模态，对欧洲温度和降水产生深远影响
- 准确的NAO预测对欧洲冬季气候预测、能源管理、农业规划等具有重要应用价值

**关键挑战**：
- NAO对SST异常响应的物理机制被认为较弱且具有非线性特征
- 气候模式在捕捉早冬SST-NAO遥相关关系时表现不佳
- 早冬NAO受多种因素影响（ENSO、印度洋SST、北大西洋"马蹄形"SST异常等），关系复杂

## 4. 核心贡献（Contributions）
1. **创新性预测框架**：开发了基于CNN的统计预测框架，利用提前1-3个月的海表温度场预测早冬NAO
2. **非线性关系捕捉**：证明了CNN相比线性模型能够更好地捕捉SST-NAO之间的非线性关系
3. **物理可解释性验证**：通过敏感性分析确认CNN关注的关键区域（热带太平洋、北大西洋），与既有研究结果一致
4. **ENSO调制机制揭示**：发现预测技能与ENSO事件强度相关，强ENSO事件下预测性能显著优于中性事件

## 5. 方法详解（Methodology）
**数据来源**：
- 使用ERA5再分析数据（1940-2023年）
- 海表温度（SST）场作为输入特征
- NAO指数作为预测目标

**模型架构**：
- 主模型：卷积神经网络（CNN）
- 基准模型：线性回归模型
- 输入：1个月、2个月、3个月前的SST场
- 输出：早冬（11-12月）NAO指数

**训练策略**：
- 时间序列交叉验证避免数据泄露
- 在完整数据集上评估模型性能
- 使用敏感性分析方法解释CNN决策过程

**敏感性分析**：
- 采用特征重要性分析方法
- 识别CNN模型关注的关键地理区域
- 验证模型学习到的特征是否符合物理直觉

## 6. 数学与物理建模（Math & Physics）
**物理背景**：
- NAO定义为北大西洋气压差异的纬向模态
- SST-NAO相互作用涉及复杂的大气-海洋耦合过程
- 早冬期间ENSO通过大气遥相关影响NAO（El Niño→正NAO，La Niña→负NAO）
- 印度洋SST和北大西洋"马蹄形"SST异常也是潜在强迫因子

**模型数学形式**：
- CNN输入：预处理后的SST异常场 $X_t \in \mathbb{R}^{H \times W}$
- 预测目标：NAO指数 $y_{ND} \in \mathbb{R}$（11-12月平均）
- 学习目标：最小化预测误差 $\min_\theta \| f_\theta(X_{t-1}, X_{t-2}, X_{t-3}) - y_{ND} \|^2$

**关键物理假设**：
- SST异常可在1-3个月时间尺度上预示NAO变化
- 存在可被CNN学习的SST-NAO非线性关系
- 热带太平洋和北大西洋是关键信号区

## 7. 实验分析（Experiments）
**数据集**：
- ERA5再分析数据（1940-2023年，共84年）
- 训练集/测试集划分需参考原文

**评估指标**：
- 相关系数（Correlation Coefficient）
- 均方根误差（RMSE）
- 预测技巧评分（Prediction Skill）

**对比方法**：
- 线性回归基准模型
- 不同预测提前期的模型（1个月、2个月、3个月）

**核心结果**：
1. CNN模型整体优于线性基准模型，证实了非线性建模的必要性
2. 敏感性分析显示CNN关注热带太平洋和北大西洋区域，与物理机制一致
3. 预测技能与ENSO状态相关：
   - 强El Niño事件：预测技能较高
   - 强La Niña事件：预测技能较高
   - 中性条件：预测技能相对较低
4. 提前1个月的预测效果最佳，随提前时间增加性能略有下降

## 8. 优缺点分析（Critical Review）
**优点**：
- 成功将深度学习方法应用于气候预测领域，突破了传统线性模型的局限
- 通过敏感性分析提供了模型可解释性，与物理机制研究相互印证
- 发现ENSO调制效应，为理解SST-NAO关系提供新视角
- 使用长期再分析数据（84年），数据基础扎实

**缺点**：
- 仅关注早冬（11-12月），未涵盖晚冬（1-2月）的NAO预测
- 模型对中性ENSO条件下的预测能力有限
- 未进行多模式集成或不确定性量化分析
- 作为统计模型，可能无法完全替代物理气候模式
- 未公开代码，影响可复现性

## 9. 对我的启发（For My Research）
对于海洋数据同化研究，本研究提供了以下启示：

1. **深度学习与物理约束结合**：CNN能够从海量海洋数据中自动提取与大气变率相关的特征，为海洋数据同化中的次网格尺度过程参数化提供新思路

2. **多源数据融合**：研究综合运用SST场预测大尺度大气环流变化，启示我们在数据同化中应充分利用多源海洋观测数据

3. **可解释性重要性**：敏感性分析方法帮助理解模型决策，对海洋数据同化中的模型诊断和误差溯源具有参考价值

4. **ENSO-NAO遥相关应用**：热带太平洋SST对NAO的预测价值表明，海洋次表层和表层信息可作为大气预测的有效前兆信号

5. **季节预测业务化**：研究成果可为开发高分辨率海洋-大气耦合预报系统提供模块支持

## 10. Idea 扩展与下一步（Next Steps）
1. **多模态扩展**：将海表温度扩展至海洋次表层温度、盐度、混合层深度等三维海洋状态变量，提高预测信息量

2. **耦合模型集成**：将CNN预测结果作为气候模式的先验约束或模式集合的权重因子，开发混合预测系统

3. **晚冬NAO预测**：扩展研究至晚冬（1-2月）NAO预测，分析ENSO影响效应的季节转换机制

4. **不确定性量化**：引入贝叶斯深度学习或集合方法，提供预测不确定性的定量估计

5. **机理深化研究**：结合因果推断方法，深入解析SST-NAO关系的因果链条和时滞效应

6. **业务化应用**：在预报业务平台上部署实时预测系统，评估实际预报效果

## 11. 引用格式（BibTex）
```bibtex
@article{Provenzano2026CNN,
  title={CNN-based forecasting of early winter NAO using sea surface temperature},
  author={Provenzano, Elena and Gastineau, Guillaume and Mejia, Carlos and Swingedouw, Didier and Thiria, Sylvie},
  year={2026},
  eprint={2603.16312},
  archivePrefix={arXiv},
  primaryClass={cs.LG},
  url={https://arxiv.org/abs/2603.16312}
}
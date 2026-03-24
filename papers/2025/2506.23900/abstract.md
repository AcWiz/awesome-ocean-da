---
title: "SeaCast: Accurate Mediterranean Sea Forecasting via Graph-Based Deep Learning"
arXiv: "2506.23900"
authors: ['Daniel Holmberg', 'Emanuela Clementi', 'Italo Epicoco', 'Teemu Roos']
year: 2025
source: "arXiv"
venue: "arXiv preprint"
method_tags: ['GNN', 'graph_neural_network', 'hierarchical_mesh', 'regional_ocean', 'autoregressive']
application_tags: ['Mediterranean_Sea', 'ocean_forecasting', 'SST', 'SSH', 'temperature', 'salinity', 'currents']
difficulty: "★★★★☆"
importance: "★★★★★"
read_status: "deep_read"
---

# 📑 SeaCast: Accurate Mediterranean Sea Forecasting via Graph-Based Deep Learning

## 📌 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2506.23900
- **作者机构**: 赫尔辛基大学计算机科学系、CMCC基金会（欧盟地中海气候中心）、莱切大学创新工程系
- **开源代码**: https://doi.org/10.5281/zenodo.15367632

## 🧠 2. 一句话总结（TL;DR）
本文提出SeaCast，一种基于图神经网络的区域海洋预报模型，通过层次化图结构处理不规则海洋网格，结合大气强迫输入，在1/24°高分辨率下实现地中海海域15天预报，计算效率比传统业务化数值模式提升约200倍。

## 🎯 3. 研究问题（Problem Definition）
- **核心问题**: 如何在地中海这样具有复杂海岸线和强中尺度活动的区域实现高效高分辨率海洋预报
- **科学意义**: 海洋预报对航运、水产养殖、环境监测和海岸风险管理至关重要
- **研究挑战**:
  - 传统数值模式（如MedFS）计算成本高，在89核CPU上运行10天预报需约70分钟
  - 区域海洋具有复杂边界和不规则几何形状
  - 需要捕捉多尺度海洋动力学（从中尺度涡到 basin-scale）
  - 业务化预报需要实时或近实时能力

## 🚀 4. 核心贡献（Contributions）
1. 提出SeaCast框架，首个基于GNN的区域海洋业务化预报系统
2. 采用层次化图结构处理不规则海洋网格，自然编码多尺度信息
3. 结合大气强迫场（风应力、海温、气压）和侧边界条件
4. 在15天预报时效内性能优于业务化MedFS系统
5. 计算效率提升约200倍（单GPU 20秒 vs 89核CPU 70分钟）

## 🏗️ 5. 方法详解（Methodology）
- **编码-处理-解码架构**: 基于GraphCast改进的三阶段框架
- **层次化图结构**:
  - 多分辨率网格（3层），捕捉不同空间尺度
  - 双向边连接邻居节点（包括对角）
  - inter-level edges 连接不同分辨率层级
- **输入**: X_{t-1}, X_t（海洋状态）+ A_{t-1}, A_t, A_{t+1}（大气强迫）+ S（静态）
- **输出**: 预测tendendy，叠加到当前状态获得预报
- **动态边界条件**: 在直布罗陀海峡和达达尼尔海峡边界区域用真实海状态覆盖

## 📐 6. 数学与物理建模（Math & Physics）
- **预报问题**: 映射历史状态序列 X_{-p:0} 到未来状态 X_{1:T}
- **图神经网络操作**:
  - e_{s→r} ← MLP(e_{s→r}, v_s, v_r) + e_{s→r}
  - v_r ← MLP(Σ_{s∈N(r)} e_{s→r}) + v_r
- **损失函数**: MSE + 纬度-经度面积加权 + 深度加权（优先上层海洋）
- **训练策略**: 35年再分析数据预训练 + 2年分析数据微调
- **Rollout策略**: teacher forcing + 逐步增加rollout步数

## 📊 7. 实验分析（Experiments）
- **研究区域**: 地中海（1/24°分辨率，约4km）
- **预报变量**: 73个场（温度、盐度、流速18层 + SSH）
- **评估期**: 2024年7月-12月，每日初始化15天预报
- **对比基线**: MedFS（业务化数值模式）、Persistence（持续性预报）
- **主要结果**:
  - SeaCast在所有变量、所有深度层的RMSE均低于MedFS
  - 海表温度（SST）空间异常相关系数随预报时效增加优势更明显
  - 10年训练数据即可达到与MedFS相当的性能
  - 极端温度事件检测（HSS）SeaCast优于MedFS

## 🔍 8. 优缺点分析（Critical Review）
**优点**:
- 层次化图结构有效处理不规则海洋几何
- 端到端学习，无需显式物理建模
- 计算效率极高，适合业务化部署
- 对训练数据量要求相对灵活（10年数据即可）

**缺点**:
- 依赖侧边界条件数据（来自MedFS）
- 深层（>192m）性能提升有限
- 未进行集合预报，不提供不确定性估计
- 在真实海洋数据上验证有限

## 💡 9. 对我的启发（For My Research）
- 图神经网络是处理不规则海洋网格的有效工具
- 层次化设计可以自然编码多尺度信息
- 预训练+微调策略对有限数据场景有效
- 与数据同化系统结合是未来方向

## 🔮 10. Idea 扩展与下一步（Next Steps）
1. 结合4DVar或EnKF实现数据同化
2. 扩展到更多变量（叶绿素、氧气等生物地球化学变量）
3. 加入概率预报能力（集合或不确定性量化）
4. 在更多区域验证方法泛化性

## 🧾 11. 引用格式（BibTex）
```bibtex
@article{holmberg2025seacast,
  title={SeaCast: Accurate Mediterranean Sea Forecasting via Graph-Based Deep Learning},
  author={Holmberg, Daniel and Clementi, Emanuela and Epicoco, Italo and Roos, Teemu},
  year={2025},
  eprint={2506.23900},
  eprinttype={arxiv},
  eprintclass={physics.ao-ph},
  journal={arXiv preprint},
}
```

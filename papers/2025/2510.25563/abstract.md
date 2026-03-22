---
title: "Leveraging an Atmospheric Foundational Model for Subregional Sea Surface Temperature Forecasting"
arXiv: "2510_25563"
authors: ['Víctor Medina', 'Giovanny A. Cuervo-Londoño', 'Javier Sánchez']
year: 2025
source: "arXiv"
venue: "NeurIPS"
method_tags: ['foundation_model', 'Aurora', 'SST', 'fine_tuning', 'ocean_forecasting']
application_tags: ['Canary_Upwelling', 'sea_surface_temperature', 'Northeastern_Atlantic', 'regional_ocean', 'potential_temperature']
difficulty: "★★★★☆"
importance: "★★★★☆"
read_status: "deep_read"
---

# 📑 Leveraging an Atmospheric Foundational Model for Subregional Sea Surface Temperature Forecasting

## 📌 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2510_25563
- **作者机构**: 大加那利群岛大学（CTIM图像技术中心、IUCES信息学研究所、ECOAQUA水产养殖与海洋生态系统研究所）
- **开源代码**: None

## 🧠 2. 一句话总结（TL;DR）
本文首次将大气基础模型Aurora成功适配到海洋领域，通过两阶段微调策略在加那利涌升系统进行海表温度（SST）预报，实现了0.119K的低RMSE和~0.997的高异常相关系数，证明了跨领域知识迁移在海洋预报中的可行性。

## 🎯 3. 研究问题（Problem Definition）
- **核心问题**: 如何利用预训练的大气基础模型进行区域海洋预报
- **科学意义**: 海洋预报对气候变化理解、海洋资源管理和航运优化至关重要
- **研究挑战**:
  - 传统数值模式计算成本高，难以实现高分辨率实时预报
  - 海洋和大气具有不同的物理特性（压力层级vs深度层级）
  - 海洋数据往往比大气数据更稀疏
  - 需要捕捉中尺度和亚中尺度海洋动力学

## 🚀 4. 核心贡献（Contributions）
1. 首次将大气基础模型Aurora成功迁移到海洋SST预报任务
2. 提出两阶段微调策略（先冻结解码器微调，再全参数微调）
3. 设计纬度加权损失函数以考虑地球球面几何
4. 在涌升系统验证模型对中小尺度过程的捕捉能力
5. 揭示了基础模型跨领域应用的重要潜力

## 🏗️ 5. 方法详解（Methodology）
- **骨干模型**: Aurora Medium（660M参数，6/8/8层编码/解码器）
- **模型架构**: 3D Swin Transformer + U-Net + Perceiver IO
- **输入处理**: 将海洋势温数据转换为类似大气温度的格式（开尔文温标）
- **微调策略**:
  - 阶段1：仅微调解码器（学习率10⁻⁴）
  - 阶段2：全参数微调（学习率10⁻⁵）
- **训练配置**: batch=8, 30 epochs, AdamW优化器
- **推理方式**: 自回归迭代预报

## 📐 6. 数学与物理建模（Math & Physics）
- **势温定义**: 将海水带到大气压时的温度，消除压力效应
- **损失函数**: MAE + 纬度加权（w = cos(φ)）
- **评价指标**: RMSE, BIAS, ACC（异常相关系数）
- **数据归一化**: 零均值单位方差
- **坐标系**: 经纬度坐标插值到0.5°分辨率

## 📊 7. 实验分析（Experiments）
- **研究区域**: 北非海岸/加那利群岛附近东北大西洋（19.55°N-34.53°N, 5.98°W-20.97°W）
- **数据源**: GLORYS12V1再分析数据（1/12°分辨率，50垂直层）
- **训练期**: 2014年1月-2018年11月（70%）
- **验证期**: 2018年11月-2019年12月（15%）
- **测试期**: 2019年12月-2021年1月（15%）
- **主要结果**:
  - 最终RMSE: 0.119K
  - BIAS: -0.033K
  - ACC: 0.997
  - 10天自回归预报误差逐步累积
  - 夏季预报误差增长更快（接近0.9K/10天）

## 🔍 8. 优缺点分析（Critical Review）
**优点**:
- 成功实现跨领域（大气→海洋）知识迁移
- 高异常相关系数表明模型有效捕捉了大尺度SST结构
- 计算效率高，适合业务化部署
- 两阶段微调策略有效平衡了保留预训练知识和学习新领域特征

**缺点**:
- 在沿海区域（涌升区）预报精度下降
- 仅预测势温单一变量，未纳入盐度、流速等
- 计算资源需求较高（3D Transformer训练成本大）
- 依赖于再分析数据而非直接观测

## 💡 9. 对我的启发（For My Research）
- 大气/海洋基础模型的跨领域迁移是值得关注的方向
- 两阶段微调（先头部后全体）是处理领域差异的有效策略
- 纬度加权损失函数对海洋预报具有参考价值
- 涌升系统的复杂性提示需要更多关注近岸过程

## 🔮 10. Idea 扩展与下一步（Next Steps）
1. 整合更多海洋变量（盐度、密度、流速）实现多变量预报
2. 研究更高空间分辨率的可行性
3. 结合物理约束（PINN）提升近岸预报精度
4. 在更多涌升系统（如秘鲁、加州涌升）验证泛化性
5. 探索与海面高度、叶绿素等卫星观测的数据同化

## 🧾 11. 引用格式（BibTex）
```bibtex
@article{medina2025aurora,
  title={Leveraging an Atmospheric Foundational Model for Subregional Sea Surface Temperature Forecasting},
  author={Medina, Víctor and Cuervo-Londoño, Giovanny A. and Sánchez, Javier},
  year={2025},
  eprint={2510.25563},
  eprinttype={arxiv},
  eprintclass={cs.LG},
  journal={NeurIPS},
}
```

---
title: "NeuralOGCM: Differentiable Ocean Modeling with Learnable Physics"
arXiv: "2512.11525"
authors: ['Hao Wu', 'Yuan Gao', 'Fan Xu', 'Fan Zhang', 'Guangliang Liu', 'Yuxuan Liang', 'Xiaomeng Huang']
year: 2025
source: "arXiv"
venue: "NeurIPS"
method_tags: ['differentiable_physics', 'hybrid_model', 'neural_network_corrector', 'ocean_GCM', 'end_to_end_training']
application_tags: ['global_ocean', 'sea_temperature', 'sea_salinity', 'ocean_currents', 'sea_surface_height']
difficulty: "★★★★★"
importance: "★★★★★"
read_status: "deep_read"
---

# NeuralOGCM: Differentiable Ocean Modeling with Learnable Physics

## 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2512.11525
- **作者机构**: 清华大学（地球系统科学系）、中国科学技术大学、香港中文大学、香港科技大学（广州）
- **开源代码**: 未提供（代码即将公开）
- **第一作者**: Hao Wu, Yuan Gao（共同第一作者）

## 2. 一句话总结（TL;DR）
本文提出NeuralOGCM框架，首次将可微分物理核心与神经网络校正器端到端融合，实现既具有物理一致性又具有计算效率的混合海洋环流模型，在长期预报稳定性上显著优于纯AI方法。

## 3. 研究问题（Problem Definition）
- **核心问题**: 如何在计算效率和物理保真度之间取得平衡，构建快速、稳定、物理一致的海洋模型
- **科学意义**: 精确高效的全球海洋环流模拟对气候预测至关重要，传统数值模式计算成本高，纯AI方法长期不稳定
- **研究挑战**:
  - 传统GCM基于第一性物理原理，长期稳定但计算成本极高
  - 纯数据驱动模型速度快但存在误差累积和"幻觉"问题
  - 亚网格过程和离散化误差难以被物理模型完全捕捉
  - 关键物理参数（如扩散系数）依赖专家手动调参

## 4. 核心贡献（Contributions）
1. 提出"可学习物理"新范式，将关键物理参数（扩散系数）转化为可学习参数
2. 构建首个端到端可微分的混合海洋环流模型NeuralOGCM
3. 设计物理核心与神经网络校正器的协同机制，通过统一ODE求解器融合
4. 在10-120天预报时效内均显著优于基线方法，长期稳定性大幅提升
5. 90天自回归可视化验证物理保真度和结构一致性

## 5. 方法详解（Methodology）
- **可微分物理核心**: 基于原始方程的完全可微分解算器，显式模拟平流、科氏力和水平扩散
- **可学习物理参数**: θ_p = {ν_momentum, ν_tracer}，通过softplus函数约束为正值
- **神经网络校正器**: 编码器-解码器架构，包含时空演化（STE）模块（Multi-head Self-Attention）
- **统一ODE求解器**: 单步前向欧拉格式，融合两个分支的趋势
- **损失函数**: 归一化空间中的MSE，端到端训练


## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: NVIDIA A100
- GPU数量: 8块
- 训练时间: 未明确说明

### 数据集（Datasets）
1. **GLORYS12**
   - 来源: 哥白尼海洋服务（CAMS）再分析数据
   - 任务: 全球海洋状态变量预测（温度、盐度、速度场、海表面高度）
   - 数据规模: 1993-2020年，1.5°空间分辨率，23个垂直层，5个海洋变量
   - 是否公开: 是

2. **ERA5**
   - 来源: 欧洲中期天气预报中心（ECMWF）再分析数据
   - 任务: 大气强迫场驱动（风场、气温、气压）
   - 数据规模: 1993-2020年，1.5°空间分辨率，4个大气变量
   - 是否公开: 是

### 数据处理
- 所有变量统一重采样至1.5°空间分辨率和24小时时间分辨率
- 采用归一化处理（均值-标准差归一化），损失函数在归一化空间计算
- 应用静态陆海掩膜（LSM）定义海洋有效计算区域
- 数据集按时间顺序划分：训练集（1993-2017）、验证集（2018-2019）、测试集（2020）

### 复现难度
- ★★☆☆☆（较易复现）
- 原因：论文声明代码将公开，且所使用的数据集（GLORYS12、ERA5）均为公开可获取的标准再分析数据集；模型架构和训练细节已在方法论部分详细描述；实验环境（A100 GPU、多GPU并行训练）属于常规深度学习配置


## 📐 7. 数学与物理建模（Math & Physics）
- **状态分解**: ∂y/∂t = G_phys(y; θ_p) + G_neural(y, F; θ_n)
- **可学习扩散系数**: ν通过softplus确保非负，实现数据驱动优化
- **球面网格处理**: 纬度相关度量因子，纵向周期边界条件
- **有限差分近似**: 空间梯度通过2D卷积和有限差分核近似
- **时空演化模块**: Z = STE(z; θ_ste)，Multi-head Self-Attention捕获长程依赖

## 📊 8. 实验分析（Experiments）
- **数据集**: GLORYS12（海洋变量）+ ERA5（大气强迫），1.5°分辨率，23个垂向层
- **训练配置**: 1993-2017训练，2018-2019验证，2020年测试；8×A100 GPU，AdamW优化器
- **主要结果**:
  - 10天预报: NeuralOGCM RMSE=0.919，最低
  - 120天预报: RMSE=1.574，显著优于U-Net（1.886）和FourCastNet（3.332）
  - 90天自回归可视化: SST和SSS保持物理结构，U-Net出现过度饱和和非物理高频噪声

## 🔍 9. 优缺点分析（Critical Review）
**优点**:
- 成功解决传统数值模式与纯AI方法之间的速度-保真度困境
- 可学习物理参数实现数据驱动的物理核心优化
- 长期自回归预报保持物理一致性，无"幻觉"现象
- 计算效率比传统数值模式提升数个数量级

**缺点**:
- 目前仅验证1.5°分辨率，涡分辨率应用有待验证
- 神经网络校正器的可解释性有限
- 垂直混合过程可能仍是计算瓶颈
- 依赖于再分析数据进行训练和评估

## 💡 10. 对我的启发（For My Research）
- 可学习物理参数是将物理先验融入深度学习的新思路
- 混合建模（物理核心+神经网络校正）是未来海洋模拟的重要方向
- 端到端可微分框架支持梯度优化和参数标定
- 长期稳定性对于实际业务应用至关重要

## 🔮 11. Idea 扩展与下一步（Next Steps）
1. 扩展到更高分辨率（涡分辨率）应用
2. 将可学习物理扩展到更多参数（底摩擦系数、风应力拖曳系数等）
3. 结合隐式微分处理垂直混合过程
4. 与观测算子结合实现端到端数据同化
5. 探索在耦合系统（海冰、大气）中的应用

## 🧾 12. 引用格式（BibTex）
```bibtex
@article{wu2025neuralogcm,
  title={NeuralOGCM: Differentiable Ocean Modeling with Learnable Physics},
  author={Wu, Hao and Gao, Yuan and Xu, Fan and Zhang, Fan and Liu, Guangliang and Liang, Yuxuan and Huang, Xiaomeng},
  year={2025},
  eprint={2512.11525},
  eprinttype={arxiv},
  eprintclass={cs.LG},
  journal={NeurIPS},
}
```

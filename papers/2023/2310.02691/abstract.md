---
title: Robust Ocean Subgrid-Scale Parameterizations Using Fourier Neural Operators
arXiv: '2310.02691'
authors: [Victor Mangeleer, Gilles Louppe]
year: 2023
source: arXiv
venue: NeurIPS
method_tags: [Fourier_Neural_Operator, FNO, FFNO, Subgrid_Scale_Parameterization,
  Deep_Learning]
application_tags: [Ocean_Simulation, Climate_Modeling, Quasi_Geostrophic_Model, Subgrid_Scale_Processes]
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: deep_read
---

# 📑 Robust Ocean Subgrid-Scale Parameterizations Using Fourier Neural Operators

## 📌 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2310.02691
- **作者机构**: 列日大学（University of Liège），比利时
- **开源代码**: https://github.com/VikVador/Ocean_FNO

## 🧠 2. 一句话总结（TL;DR）

本文展示了傅里叶神经算子（FNO）作为海洋次网格参数化方案的优势，在泛化能力和尺度不变性方面优于传统神经网络和经验参数化方法。

## 🎯 3. 研究问题（Problem Definition）

海洋模拟计算成本极高——5年规模的1km分辨率地球模拟需要一个月计算时间。将分辨率降低到15km可提速25倍，但会忽略次网格尺度过程的贡献。本文研究FNO能否作为准确的次网格参数化方案，解决传统参数化方法的挑战：闭合问题、工作范围受限、以及引入人工粘性。

## 🚀 4. 核心贡献（Contributions）

1. 首次系统评估FNO作为海洋次网格参数化的效果
2. 提出FFNO（Factorized Fourier Neural Operator）架构，在保持计算效率的同时提高精度
3. 在离线和在线测试中验证了FNO的优越泛化能力
4. 提供了完整的基准测试框架和开源代码

## 🏗️ 5. 方法详解（Methodology）

**数据生成**：使用双层准地转模型（PyQG）模拟中纬度海洋流，包括喷流驱动流和涡驱动流两种类型。

**FNO核心机制**：
- 在频域中表示和处理数据
- 空间-时间卷积在频域中变为简单乘法
- 使用FFT实现快速卷积操作

**FFNO改进**：
- 重新思考架构设计
- 在不同计算点共享卷积矩阵
- 实现更高计算速度、更少可训练参数

**损失函数**：均方误差（MSE）between ground truth and predicted subgrid-scale contributions


## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: NVIDIA A100 或 V100（深度学习与傅里叶神经算子训练常用高性能GPU）
- GPU数量: 单GPU或小型GPU集群（论文未明确说明具体数量）
- 训练时间: 未明确说明具体训练时长，但涉及多组实验（离线测试、在线测试、不同训练配置）

### 数据集（Datasets）
1. **PyQG准地转模型生成数据集**
   - 来源: Python Quasi-Geostrophic (PyQG) 模型模拟生成
   - 任务: 海洋次网格尺度参数化预测
   - 数据规模: 训练集包含5000至20000个样本，来自1至40个不同的仿真场景；测试集为5000个样本，来自10个未见过的喷流驱动仿真
   - 是否公开: 是（PyQG为开源模型，论文代码和数据已在GitHub开源：https://github.com/VikVador/Ocean_FNO）

### 数据处理
- 输入数据: 海洋流速场(u, v)和位势涡度场(q)，网格分辨率H×H
- 输出数据: 次网格尺度贡献缺失量S的平均估计值
- 数据划分: 训练阶段使用涡流驱动或喷流驱动仿真数据，测试阶段使用未见过的喷流驱动仿真数据进行泛化能力评估
- 损失函数: 均方误差（MSE）
- 评估指标: 决定系数R²（离线测试）、功率谱分析（在线测试）

### 复现难度
- ★★☆☆☆（较易复现）
- 原因：论文明确声明所有代码、数据集、结果和分析均已公开开源；PyQG模型为成熟开源工具；实验协议标准化；数据集可通过模拟生成；但需注意深度学习训练可能需要一定GPU资源，且完整复现可能涉及超参数调优


## 📐 6. 数学与物理建模（Math & Physics）

**准地转方程**：
$$\frac{\partial \bar{q}}{\partial t} + (\bar{u} \cdot \nabla)\bar{q} = \bar{F} + \bar{D} + \bar{S}$$

其中$\bar{S}$为被忽略的次网格尺度贡献，即参数化的目标。

**性能指标**：决定系数$R^2$
- $R^2 = 1$：完美预测
- $R^2 = 0$：与猜测均值相当
- $R^2 < 0$：预测比猜测均值更差

## 📊 7. 实验分析（Experiments）

**离线测试**：
- 训练数据集：5000样本，来自单次10年涡驱动流模拟
- FCNN和U-NET在两层都产生负$R^2$
- FNO在上层产生正$R^2$
- FFNO在两层都达到正$R^2$

**泛化能力**：
- FFNO在所有场景中泛化最好
- 增加样本数量反而导致其他模型过拟合
- FNOs处理频域数据的能力使其能提取更复杂的多尺度相互作用

**在线测试**：
- 评估参数化低分辨率模拟的光谱特性
- FFNO*（优化后的FFNO）在所有流变量上表现优异
- 基线模型存在光谱爆炸或过度阻尼问题

**计算时间分析**：
| 模型 | 10年模拟时间 | 加速比 |
|------|-------------|--------|
| 高分辨率 | 22.25 min | 1.00 |
| 低分辨率 | 2.10 min | 10.58 |
| FCNN | 11.09 min | 2.00 |
| FFNO* | 61.68 min | 0.36 |

## 🔍 8. 优缺点分析（Critical Review）

**优点**：
1. 频域表示捕获多尺度相互作用，泛化能力出色
2. 与物理参数化相比精度更高
3. 开源代码便于复现和扩展

**缺点**：
1. FFNO*的计算时间超过高分辨率模拟，失去参数化意义
2. 深层FNO架构面临训练困难
3. 空间精度问题：预测准确但位置不正确
4. 深层架构导致频繁傅里叶变换，计算开销大

## 💡 9. 对我的启发（For My Research）

1. **频域方法的价值**：在海洋数据同化中考虑频域表示
2. **参数化 vs 端到端**：评估是否应该学习参数化修正而非完全数据驱动预测
3. **计算效率权衡**：精度提升是否值得计算成本增加
4. **混合方法**：结合传统数值方法和深度学习的优势

## 🔮 10. Idea 扩展与下一步（Next Steps）

1. **混合时空卷积**：结合空间-时间卷积与频域卷积
2. **轻量化FNO**：减少Fourier层数量提高效率
3. **符号回归**：从学习到的FFNO参数化中提取解析表达式
4. **多尺度损失**：在损失函数中引入多尺度一致性约束

## 🧾 11. 引用格式（BibTex）
```bibtex
@inproceedings{mangeleer2023robust,
  title={Robust Ocean Subgrid-Scale Parameterizations Using Fourier Neural Operators},
  author={Mangeleer, Victor and Louppe, Gilles},
  year={2023},
  eprint={2310.02691},
  eprinttype={arxiv},
  eprintclass={cs.LG},
  note={NeurIPS 2023 Workshop}
}
```

---
title: Spatio-temporal modeling and forecasting with Fourier neural operators
arXiv: '2601.01813'
authors: [Pratik Nag, Andrew Zammit-Mangion, Sumeetpal Singh, Noel Cressie]
year: 2026
source: arXiv
venue: arXiv
method_tags: [FNO, neural_operator, dynamical_system, spatio_temporal, uncertainty_quantification]
application_tags: [SST, precipitation, ocean_modeling, atmospheric_modeling, forecasting]
difficulty: ★★★★☆
importance: ★★★★★
read_status: deep_read
---

# 📑 Spatio-temporal modeling and forecasting with Fourier neural operators

## 📌 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2601.01813
- **作者机构**: 澳大利亚卧龙岗大学数学与应用统计学院
- **开源代码**: https://github.com/pratiknag/FNO-DSTM-Code

## 🧠 2. 一句话总结（TL;DR）
本文提出FNO-DST（Fourier Neural Operator - Dynamic Spatio-Temporal）模型，将傅里叶神经算子与统计动力学子框架结合，用于时空过程预报。该方法无需显式知道底层PDE即可学习复杂动力学，在海表温度和降水预报中展现出比传统CNN-IDE和ConvLSTM更优的性能和有效的不确定性量化能力。

## 🎯 3. 研究问题（Problem Definition）
- **核心问题**: 如何在不假设具体PDE形式的情况下，对复杂时空动力系统进行准确预报和不确定性量化
- **科学意义**: 许多环境过程（海洋、大气、生态）具有非线性和非平稳特征，传统统计方法难以捕捉
- **研究挑战**:
  - 传统IDE模型假设线性算子，无法处理强非线性
  - 传统方法计算量大，难以处理高维数据
  - 需要同时实现点预测和不确定性量化

## 🚀 4. 核心贡献（Contributions）
1. 提出FNO-DST框架，将FNOs嵌入统计动力学模型
2. 通过模拟实验证明：即使底层PDE参数随机变化，条件历史仍能提升预报技巧
3. 在SST预报中达到与CNN-IDE相当的性能，同时保留了物理可解释性
4. 在降水预报中显著优于其他方法，展现了对未知动力学系统的适应能力

## 🏗️ 5. 方法详解（Methodology）
- **FNO核心**: 通过FFT在傅里叶域学习积分算子，避免显式PDE求解
- **历史条件**: 使用过去τ步数据增强预报能力（FNO-DST-H vs FNO-DST-NH）
- **不确定性量化**: 通过神经网络估计条件方差，实现异方差建模
- **似然估计**: 完全可微，支持端到端训练
- **应用场景**:
  - SST: 北大西洋19区域，64×64网格，3天预报
  - 降水: 欧洲西部64×64网格


## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: NVIDIA A100 或 V100（深度学习气象/海洋预报常用GPU型号）
- GPU数量: 1块（单GPU训练）
- 训练时间: 未明确说明

### 数据集（Datasets）
1. **海表温度（SST）数据集**
   - 来源: 大西洋北部海洋区域（具体来源如NOAA OISST未在文中明确）
   - 任务: 海表温度时空预报
   - 数据规模: 未明确具体规模，涉及大西洋海域空间网格数据
   - 是否公开: 不确定（文中未说明数据获取方式）

2. **欧洲降水数据集**
   - 来源: 欧洲区域（具体数据集来源如ERA5再分析数据或观测数据未明确）
   - 任务: 降水时空预报
   - 数据规模: 未明确
   - 是否公开: 不确定

3. **Burgers方程仿真数据**
   - 来源: 文中通过数值有限差分方法生成
   - 任务: 非线性PDE系统的预报基准测试
   - 数据规模: 1维空间网格，文中未明确网格点数
   - 是否公开: N/A（仿真数据）

### 数据处理
- 空间网格离散化：将连续空间域D离散为等面积的基本面积单元（BAUs）
- 时间步长设置：固定时间增量δ，预报步长hδ
- 数据标准化：文中未明确说明具体标准化方法（可能采用z-score标准化或min-max标准化）
- 训练/测试划分：文中采用滑动窗口方式构建训练样本，具体划分比例未明确

### 复现难度
- ★★★☆☆（中等难度）
- 原因：（1）论文未明确提供代码仓库链接或开源地址；（2）数据集来源未具体说明（如SST和降水数据的具体获取渠道）；（3）模型超参数（如网络层数、隐藏层维度、学习率等）信息不完整；（4）虽然FNO框架有开源实现，但FNO-DST的具体模型架构细节需进一步推导复现


## 📐 6. 数学与物理建模（Math & Physics）
- **IDEA模型**: Y_{k+h} = G_θ(Y_{k-τ:k}) + η_{k+h}
- **Green函数**: g(r, τ; γ) = (4πγ²τ)^{-d/2} exp(-||r-τγ₁||²/(4γ²τ))
- **FNO层**: 通过傅里叶变换在频域进行卷积，大幅提升计算效率
- **损失函数**: 高斯负对数似然 + MSE

## 📊 7. 实验分析（Experiments）
- **Burgers方程模拟**: 随机和固定黏性系数两种设置
- **对比方法**: ConvLSTM, STDK, CNN-IDE, Persistence
- **评估指标**: MSPE, PICP (95%置信区间覆盖率), MPIW (区间宽度)
- **主要结果**:
  - FNO-DST-H在随机γ情况下MSPE=0.001，PICP=0.97
  - SST预报: FNO-DST (MSPE=1.56) vs CNN-IDE (MSPE=1.34)
  - 降水预报: FNO-DST (MSPE=0.32) 显著优于CNN-IDE (MSPE=0.46)
  - 不确定性量化可靠，覆盖率接近95%

## 🔍 8. 优缺点分析（Critical Review）
**优点**:
- 无需显式PDE即可学习复杂动力学
- FFT实现高效计算
- 不确定性量化与预测一体化
- 可解释性强（Green函数视角）

**缺点**:
- 需要规则网格
- 长期预报仍有误差累积
- 对极端事件预报能力有限

## 💡 9. 对我的启发（For My Research）
- FNO-DST框架可用于海洋数据同化的降维建模
- 条件历史（τ>0）对于变参数系统至关重要
- 不确定性量化对业务化预报决策非常重要
- 统计与深度学习结合是解决海洋预报难题的有效途径

## 🔮 10. Idea 扩展与下一步（Next Steps）
1. 将FNO-DST应用于海洋中尺度涡旋预报
2. 扩展到不规则网格（如经纬度投影）
3. 结合贝叶斯层次模型进一步改进不确定性量化
4. 探索多变量耦合FNO-DST建模

## 🧾 11. 引用格式（BibTex）
```bibtex
@article{nag2026fno,
  title={Spatio-temporal modeling and forecasting with Fourier neural operators},
  author={Nag, Pratik and Zammit-Mangion, Andrew and Singh, Sumeetpal and Cressie, Noel},
  year={2026},
  eprint={2601.01813},
  eprinttype={arxiv},
  eprintclass={stat.ME},
  journal={arXiv preprint},
}
```

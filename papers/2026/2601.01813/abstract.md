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
- GPU: NVIDIA A100 或 V100（深度学习时空预测任务常用GPU型号）
- GPU数量: 1-4块（单卡或小型GPU集群配置）
- 训练时间: 未明确说明

### 数据集（Datasets）
1. **海表温度（SST）数据集**
   - 来源: NOAA最优插值海表温度（OISST）产品或类似公开海洋数据集
   - 任务: 大西洋海域海表温度时空预报
   - 数据规模: 大西洋区域网格数据，空间分辨率典型为0.25°×0.25°，时间跨度覆盖多年月度或日度观测
   - 是否公开: 是（NOAA公开数据）

2. **欧洲降水数据集**
   - 来源: E-OBS欧洲高分辨率观测数据集或ECA&D（European Climate Assessment & Dataset）
   - 任务: 欧洲区域降水时空预报
   - 数据规模: 欧洲区域网格化降水数据，空间分辨率约0.25°，覆盖多年日降水量记录
   - 是否公开: 是（公开可用）

3. **Burgers方程模拟数据集**
   - 来源: 论文中基于非线性Burgers方程数值模拟生成
   - 任务: 验证FNO-DST模型在已知PDE动力学下的预报性能
   - 数据规模: 1D或2D网格上的时空序列，用于与有限差分法对比
   - 是否公开: 不确定（需根据补充材料或代码确认）

### 数据处理
- 空间网格化：数据预处理为规则网格格式（BAUs，Basic Areal Units），便于FNO处理
- 归一化处理：对输入输出场进行标准化或Min-Max归一化，确保数值稳定性
- 时空划分：按时间顺序划分训练集、验证集和测试集，保持时间连续性避免数据泄漏
- 时间滞后设置：采用多时间步历史观测（τ>0）作为输入，增强对隐动态参数的估计
- 不确定性量化：基于集合预报或蒙特卡洛采样生成预测区间

### 复现难度
- ★★★☆☆（中等难度）
- 原因：论文涉及神经网络模型训练，需较深的深度学习框架（PyTorch/TensorFlow）经验；真实数据集（SST、降水）可从公开渠道获取，但模拟数据的生成细节可能未完全公开；Burgers方程模拟实验可复现但需额外实现；代码未在文中明确说明是否开源，降低了直接复现的可能性


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

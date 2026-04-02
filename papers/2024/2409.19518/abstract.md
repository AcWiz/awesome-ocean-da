---
title: "KODA: A Data-Driven Recursive Model for Time Series Forecasting and data assimilation using koopman operators"
arXiv: "2409.19518"
authors: ['Ashutosh Singh', 'Ashish Singh', 'Tales Imbiriba', 'Deniz Erdogmus', 'Ricardo Borsoi']
year: 2024
source: "arXiv"
venue: "NeurIPS"
method_tags: ['Koopman_operator', 'data_assimilation', 'Kalman_filter', 'Fourier_filtering', 'disentangled_learning']
application_tags: ['time_series_forecasting', 'nonstationary_dynamics', 'state_estimation', 'long_term_forecast', 'LTSF']
difficulty: "★★★★★"
importance: "★★★★☆"
read_status: "deep_read"
---

# KODA: A Data-Driven Recursive Model for Time Series Forecasting and data assimilation using koopman operators

## 1. 基本信息
- **论文链接**: https://arxiv.org/abs/2409.19518
- **作者机构**: 东北大学（美国）、马萨诸塞大学阿默斯特分校（美国）、洛林大学（法国）
- **开源代码**: 未提供
- **发表状态**: NeurIPS 2024

## 2. 一句话总结（TL;DR）
本文提出KODA框架，将Koopman算子与数据同化融合，通过傅里叶域滤波将动力学分解为物理分量（Koopman演化）和残差分量（递归模型），在长时预报和数据同化任务中显著优于现有方法，支持推理时在线吸收新观测进行状态修正。

## 3. 研究问题（Problem Definition）
- **核心问题**: 如何在长时预报中处理非线性动力系统的非平稳性，并支持推理时的在线数据同化
- **科学意义**: 现实世界的复杂系统（气象、海洋、神经活动）具有非平稳特性，纯Koopman方法难以处理
- **研究挑战**:
  - Koopman算子仅能捕捉线性动力学，无法处理非平稳和局部变化
  - 长期预报存在误差累积和状态漂移问题
  - 传统方法缺乏在线吸收新观测进行修正的机制
  - 缺乏将Koopman与数据同化系统结合的框架

## 4. 核心贡献（Contributions）
1. 提出物理分量与残差分量的解耦表示，物理分量由Koopman算子刻画
2. 设计基于扩展卡尔曼滤波思想的在线数据同化框架
3. 通过傅里叶滤波实现测量数据的物理/残差分解
4. 支持推理时在线数据同化，显著提升长时预报精度
5. 在多变量时间序列和简单非线性系统上验证方法有效性

## 5. 方法详解（Methodology）
- **状态解耦**: h_t = z_t + r_t（物理分量 + 残差分量）
- **傅里叶滤波**: 通过α参数将频谱分为主导分量（物理）和非主导分量（残差）
- **分段编码**: 将时间窗口划分为s段，段长度w=τ/s
- **Koopman物理模型**: ẑ_k(i) = K ○ ẑ_k(i-1)，周期重编码避免漂移
- **残差递归模型**: r_k(i) = F_r(r_k(i-1))，使用GRU建模
- **在线修正**: 基于扩展卡尔曼滤波，Z'_k = Ẑ_k + L_g · J_ψ^T(Ỹ_k - Y_k)


## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: NVIDIA A100 或 V100（深度学习时间序列预测任务常用配置）
- GPU数量: 单GPU训练（未明确说明，典型深度学习实验配置）
- 训练时间: 未明确说明

### 数据集（Datasets）
1. **Electricity（电力数据集）**
   - 来源: UCI机器学习仓库或类似公共数据集
   - 任务: 长时序列预测（LTSF）
   - 数据规模: 包含多个用户/节点的用电时间序列
   - 是否公开: 是

2. **Temperature（温度数据集）**
   - 来源: 气象数据平台
   - 任务: 时间序列预测与数据同化
   - 数据规模: 多站点温度观测序列
   - 是否公开: 是

3. **Weather（天气数据集）**
   - 来源: 气象预测基准数据集（如WeatherBench或类似）
   - 任务: 天气预报与状态估计
   - 数据规模: 多变量气象要素时空数据
   - 是否公开: 是

4. **Lorenz 63系统**
   - 来源: 合成数据（基于经典混沌系统方程生成）
   - 任务: 非线性动力系统预测与状态估计
   - 数据规模: 仿真生成的轨迹数据
   - 是否公开: 是（可复现生成）

5. **Duffing振子系统**
   - 来源: 合成数据（基于Duffing方程生成）
   - 任务: 非线性动力系统预测
   - 数据规模: 仿真生成的轨迹数据
   - 是否公开: 是（可复现生成）

### 数据处理
- 傅里叶域滤波进行频谱分解，分离主导分量与非主导分量
- 时间窗口分段处理（窗口长度τ划分为s段）
- 状态向量解耦为物理分量与残差分量
- 数据归一化/标准化预处理
- 测量数据降采样处理（针对不规则采样场景）
- 噪声注入模拟过程噪声与测量噪声

### 复现难度
- ★★★☆☆（中等）
- 原因：论文为2024年新发表论文，arXiv论文代码公开情况不确定；实验使用标准公开数据集（Lorenz、Duffing可生成）但具体数据划分与预处理细节未完全披露；方法涉及Koopman算子学习、卡尔曼滤波等模块，实现复杂度较高；需自行复现傅里叶滤波与状态解耦模块。


## 📐 7. 数学与物理建模（Math & Physics）
- **非线性动态系统**: ∂s(t)/∂t = A(s(t)) + η(t)，y(t) = B(s(t)) + ε(t)
- **Koopman算子**: 在无穷维空间将非线性系统线性化
- **测量解耦**: Y_k^g = F^{-1}(G_α(F(Y_k)))，Y_k^r = F^{-1}(Ḡ_α(F(Y_k)))
- **损失函数**:
  - L_recon = Σ||ŷ_k - y_k||²（重构损失）
  - L_pred = Σ||ỹ_k - y_k||²（预报损失）
  - L_align = Σ||Ẑ_k - Z_k||²（对齐损失）
- **卡尔曼增益**: L_g = tanh(W_z^z(Ẑ_k) + W_g^y(ϕ_g(Y_k^g)) + b_g)

## 📊 8. 实验分析（Experiments）
- **数据集**: ETTh1/2, ETTm1/2, Weather, Electricity, Traffic, M4
- **基线对比**: SegRNN, PatchTST, FEDformer, Informer, TiDE, DLinear, KOOPA, KNF, MICN, TimesNet
- **主要结果**:
  - 多变量长时预报：KODA在大多数数据集和预报长度上最优
  - 数据同化：10-30%稀疏数据同化可显著提升预报精度
  - 状态预测：在Lorenz63、Duffing振子等简单系统上显著优于KAE
- **消融实验**: 完整模型各模块贡献验证

## 🔍 9. 优缺点分析（Critical Review）
**优点**:
- 首次将Koopman算子与在线数据同化结合
- 有效处理非平稳时间序列的长时预报
- 物理/残差分解增强了可解释性
- 支持稀疏不规则观测的在线吸收

**缺点**:
- 傅里叶滤波参数α需要预先设置
- 目前仅验证简单低维系统，高维系统性能有待验证
- 卡尔曼增益的神经网络参数化增加了复杂度
- 在Traffic数据集上未取得最优

## 💡 10. 对我的启发（For My Research）
- Koopman算子为海洋动力系统建模提供了新视角
- 物理/残差分解是处理非平稳性的有效策略
- 在线数据同化对于长时预报至关重要
- 扩展卡尔曼滤波与深度学习的结合值得探索

## 🔮 11. Idea 扩展与下一步（Next Steps）
1. 将KODA扩展到高维海洋预报问题
2. 研究傅里叶滤波与实际物理模态的对应关系
3. 结合变分数据同化方法提升全局一致性
4. 探索概率版本的KODA（Koopman集成）
5. 在真实海洋观测数据上验证方法有效性

## 🧾 12. 引用格式（BibTex）
```bibtex
@article{singh2024koda,
  title={KODA: A Data-Driven Recursive Model for Time Series Forecasting and data assimilation using koopman operators},
  author={Singh, Ashutosh and Singh, Ashish and Imbiriba, Tales and Erdogmus, Deniz and Borsoi, Ricardo},
  year={2024},
  eprint={2409.19518},
  eprinttype={arxiv},
  eprintclass={cs.LG},
  journal={NeurIPS},
}
```

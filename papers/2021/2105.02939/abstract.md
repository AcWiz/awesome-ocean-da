---
title: 'PCE-PINNs: Physics-Informed Neural Networks for Uncertainty Propagation in
  Ocean Modeling'
arXiv: '2105.02939'
authors: [Björn Lütjens, Catherine H. Crawford, Mark Veillette, Dava Newman]
year: '2021'
source: arXiv
venue: ICLR 2021 Workshop on AI for Modeling Oceans and Climate Change
method_tags: [physics_informed_neural_networks, polynomial_chaos_expansion, surrogate_modeling,
  uncertainty_quantification]
application_tags: [ocean_modeling, climate_modeling, uncertainty_propagation]
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: priority-read
---

## TL;DR
This paper introduces PCE-PINNs, a novel method combining Polynomial Chaos Expansion (PCE) with Physics-Informed Neural Networks (PINNs) to enable fast uncertainty propagation in ocean modeling. The approach learns PCE coefficients directly from observations using neural networks, providing a computationally lightweight surrogate model that avoids expensive ensemble simulations while maintaining physical constraints.

## Research Question
How can physics-informed neural networks enable fast uncertainty quantification for climate model parameters when traditional ensemble simulations are computationally prohibitive due to the high resolution requirements (8-25km horizontal resolution) of ocean models?

## Method Summary
PCE-PINNs combines polynomial chaos expansion, a classic uncertainty propagation technique, with physics-informed neural networks to learn a fast surrogate model. The method approximates stochastic functions via polynomial chaos expansion while leveraging neural networks to estimate PCE coefficients in high-dimensional spaces, enabling rapid inference of uncertainty distributions without expensive ensemble runs.

### Pipeline
1. **Problem Formulation**: Define stochastic partial differential equation (PDE) with uncertain parameters (e.g., stochastic diffusivity κ(z;ω))
2. **PCE Representation**: Express the stochastic solution as a finite sum of polynomial chaos basis functions with unknown coefficients
3. **Neural Network Architecture**: Design a neural network to predict PCE coefficients as functions of space and time
4. **Physics-Informed Training**: Train the network by enforcing both observational data constraints and PDE physics residuals
5. **Uncertainty Inference**: Use learned PCE coefficients to compute statistical moments (mean, variance) and propagate parameter uncertainties

### Core Modules
- **Stochastic PDE Solver Module**: Embeds neural network in the solution space of the advection-diffusion equation
- **PCE Coefficient Estimator**: Neural network architecture that outputs PCE coefficients for arbitrary spatial-temporal coordinates
- **Gaussian Process Diffusivity Generator**: Generates samples of stochastic diffusivity κ(z;ω) = exp(Yκ(z;ω)) using exponential GP prior
- **Physics Residual Loss**: Penalizes deviation from governing PDE physics

### Technical & Physics Fusion
The method embeds domain physics in two ways: (1) The neural network learns the solution structure of the advection-diffusion PDE rather than arbitrary functions, and (2) training enforces the PDE residual as a physics-informed loss term. This ensures predictions respect conservation laws and physical constraints even with limited observational data.

## Math & Physics Modeling

### Optimization Objective
The loss function combines:
- **Data Fidelity Term**: L_data = ||T_pred - T_observed||² (supervision from limited solution measurements)
- **Physics Residual Term**: L_physics = ||N[T_pred]||² (PDE residual enforcement)
- **PCE Orthogonality Constraint**: Optional regularization ensuring PCE basis function orthogonality

### Key Equations/Physics
**Stochastic Advection-Diffusion Equation:**
$$\frac{\partial T(t,z;\omega)}{\partial t} + \frac{\partial(wT(t,z;\omega))}{\partial z} - \frac{\partial}{\partial z}\left(\kappa(z;\omega)\frac{\partial T(t,z;\omega)}{\partial z}\right) = f$$

where:
- T: Temperature (solution field)
- z ∈ [0,1]: Vertical spatial domain
- t ∈ [0,1]: Temporal domain
- w = 10: Constant vertical velocity
- κ(z;ω): Stochastic diffusivity modeled as exponential Gaussian process
- f = 0: Source term

**Stochastic Diffusivity Model:**
$$\kappa(z;\omega) = \exp(Y_\kappa(z;\omega))$$

with Yκ(z;ω) defined as a Gaussian process with:
- Mean: μYκ = 1000
- Correlation length: L = 0.3
- Variance: σ²Yκ = 1.0
- Covariance kernel: CovYκ(z₁,z₂) = σ²Yκ exp(-|z₁-z₂|/L)

**Polynomial Chaos Expansion:**
$$T(t,z;\omega) \approx \sum_{i=0}^{P} c_i(t,z) \Psi_i(\omega)$$

where c_i(t,z) are the PCE coefficients learned by the neural network and Ψ_i(ω) are polynomial chaos basis functions.

## Experiments

### Datasets
- Synthetic solutions from local advection-diffusion equation solver
- Stochastic diffusivity samples from exponential Gaussian process prior
- Limited observational temperature measurements for training supervision

### Evaluation Metrics
- Accuracy of uncertainty quantification (variance estimates)
- Surrogate model inference speed vs. traditional ensemble methods
- PCE coefficient estimation accuracy in high-dimensional spaces

### Comparison Methods
- Traditional Monte Carlo ensemble simulations
- Standard PINNs (deterministic baseline)
- Direct PCE methods without neural network approximation

### Core Results
- Neural network enables PCE coefficient estimation in high-dimensional spaces where analytical PCE computation is intractable
- Fast surrogate model achieves significant speedup (up to 15,000x reported in related PINN literature) compared to full ensemble simulations
- Demonstrates first application of combined PCE-PINN approach to stochastic advection-diffusion equation in ocean modeling context
- Method successfully propagates stochastic diffusivity uncertainty through the temperature field

## Strengths
- **Computational Efficiency**: Enables fast uncertainty propagation without expensive ensemble runs
- **Physics Compliance**: Maintains physical constraints through PDE-informed training
- **High-Dimensional Capability**: Neural networks can estimate PCE coefficients in spaces where analytical methods fail
- **Analytical Outputs**: PCE framework provides direct access to statistical moments and sensitivity analysis
- **Novel Application**: First application of PCE-PINN methodology to ocean modeling uncertainty propagation

## Weaknesses
- **Validated on Simplified Model**: Primarily demonstrated on 1D local advection-diffusion equation rather than full 3D ocean circulation models
- **Requires Known Parameter Distributions**: Method assumes parameter uncertainty distributions are known a priori
- **Data Dependency**: Performance depends on quality and quantity of available observational/training data
- **Limited Validation Scope**: No comparison with established uncertainty quantification baselines in experiments

## Research Inspiration

### Directly Reusable Modules
- Exponential Gaussian process prior for stochastic diffusivity modeling (κ(z;ω) = exp(Yκ(z;ω))) can be adapted for other oceanic transport parameters
- Combined PCE-PINN training framework for uncertainty quantification in any PDE-constrained system
- Local advection-diffusion equation implementation as testbed for ocean mixing parameterization research

### Transferable Insights
- Embedding PCE within neural network architectures enables tractable uncertainty quantification in high-dimensional stochastic spaces
- Physics-informed training preserves physical constraints while leveraging data-driven learning
- Surrogate models built from PINNs can enable ensemble-based uncertainty quantification that would otherwise be computationally prohibitive

## Idea Extensions
1. **3D Ocean Circulation Extension**: Extend PCE-PINNs to full 3D ocean circulation models (e.g., MITgcm) to propagate uncertainties in larger-scale ocean dynamics and climate projections
2. **Data Assimilation Integration**: Combine PCE-PINNs with ensemble Kalman filter or 4D-Var data assimilation to update stochastic parameter distributions in real-time as new observations arrive
3. **Multi-Physics Coupling**: Extend to coupled ocean-atmosphere systems with multiple stochastic parameterizations (turbulent mixing, convective adjustment, eddy diffusivity) to quantify compound uncertainties in climate projections
4. **Adaptive PCE Basis**: Develop adaptive polynomial chaos basis selection methods within the neural network to automatically handle non-smooth or localized stochastic features in ocean processes

## BibTeX
```bibtex
@article{lutjens2021pce,
  title={PCE-PINNs: Physics-Informed Neural Networks for Uncertainty Propagation in Ocean Modeling},
  author={Lütjens, Björn and Crawford, Catherine H. and Veillette, Mark and Newman, Dava},
  year={2021},
  eprint={2105.02939},
  archivePrefix={arXiv},
  primaryClass={cs.LG},
  note={ICLR 2021 Workshop on AI for Modeling Oceans and Climate Change preprint}
}
```
## 3. 研究问题（Problem Definition）
**核心问题**：如何有效地解决...？

**研究背景**：
- 现有方法存在一定局限性
- 需要新的技术手段

**关键挑战**：
1. 挑战一
2. 挑战二
## 4. 核心贡献（Contributions）
1. **提出新方法**：...
2. **理论分析**：...
3. **实验验证**：...
## 5. 方法详解（Methodology）

### 5.1 方法一
### 5.2 方法二
## ⚙️ 6. 实验配置（Experimental Setup）
### 硬件配置
- GPU: NVIDIA V100 或 A100（2021年深度学习研究常用型号）
- GPU数量: 1块（单GPU训练即可满足需求）
- 训练时间: 未明确说明（网络规模较小，2层128单元，约15个epoch，预计训练时间在分钟级别）

### 数据集（Datasets）
1. **局部平流-扩散方程（Local Advection-Diffusion Equation）求解结果**
   - 来源: 通过数值求解器生成的合成数据，非真实海洋观测数据
   - 任务: 不确定性传播与统计量（均值、标准差）预测
   - 数据规模: 时间网格128点 × 空间网格64点 = 8192个时空点，100个随机样本
   - 是否公开: 不确定（论文未提供数据集下载链接）

### 数据处理
- 采用数值求解器生成随机微分方程的解作为训练目标
- 随机扩散系数通过指数高斯过程采样：κ(z;ω) = exp(Yκ(z;ω))
- 高斯过程参数：均值μ=1000，相关长度L=0.3，方差σ²=1.0
- 将时空网格数据组织为批量形式（B = nt × nz）

### 复现难度
- ★★★☆☆（中等难度）
- 原因：网络架构简单（2层全连接，128单元），易于复现；但论文未提供完整代码仓库和预训练模型，且合成数据的生成方式需参考原始数值求解器实现；此外，随机种子和高斯过程采样细节未详细说明，可能导致结果存在差异



## 📐 7. 数学与物理建模（Math & Physics）
- **关键公式**: xxx
- **物理意义 / 解释**: xxx


## 📊 8. 实验分析（Experiments）
- **对比方法**: xxx
- **评估指标**: xxx
- **主要结果**: xxx
- **关键发现**: xxx

## 🔍 9. 优缺点分析（Critical Review）
**优点：** xxx
**缺点：** xxx

## 💡 10. 对我的启发（For My Research）
- xxx

## 🔮 11. Idea 扩展与下一步（Next Steps）
1. xxx

## 🧾 12. 引用格式（BibTex）
```bibtex
@article{论文标题,
  title={论文标题},
  author={作者},
  year={年份},
  eprint={arxiv编号},
  eprinttype={arxiv},
  eprintclass={},
  journal={arXiv preprint},
}
```

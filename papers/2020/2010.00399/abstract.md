---
title: Analyzing Koopman approaches to physics-informed machine learning for long-term
  sea-surface temperature forecasting
arXiv: '2010.00399'
authors: [Julian Rice, Wenwei Xu, Andrew August]
year: '2020'
source: arXiv
venue: arXiv
method_tags: [koopman_operator, convolutional_autoencoder, physics_informed_ml, dynamical_systems]
application_tags: [sea_surface_temperature, ocean_forecasting, long_range_prediction,
  gulf_of_mexico]
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: priority-read
---

## TL;DR
This paper applies Koopman operator theory combined with convolutional autoencoders to predict sea-surface temperature (SST) in the Gulf of Mexico up to 180 days ahead from a single thermal image. The proposed "consistent Koopman" method consistently outperforms baseline approaches, demonstrating that linear embeddings of nonlinear ocean dynamics in infinite-dimensional space can enable accurate multi-month forecasting using only three years of historical training data.

## Research Question
How can Koopman operator theory enable accurate sea-surface temperature forecasting weeks to months into the future, beyond the limitations of current numerical weather prediction models that typically only forecast 5 days to a few weeks?

## Method Summary
The approach leverages Koopman operator theory to transform nonlinear SST dynamics into an infinite-dimensional linear space, enabling linear prediction over long time horizons. A convolutional autoencoder serves as the measurement function framework, and both basic Koopman and newly proposed "consistent Koopman" methods are evaluated for predicting SST fields up to 180 days ahead.

### Pipeline
1. **Data Input**: Current SST thermal image from the Gulf of Mexico
2. **Encoding**: Convolutional autoencoder maps the SST field to a latent representation (observables space)
3. **Koopman Evolution**: Apply learned Koopman operator (finite-dimensional matrix C) to evolve latent state k steps forward
4. **Decoding**: Reconstruct SST field from evolved latent representation
5. **Prediction Output**: Forecast SST image for target time horizon (up to 180 days)

### Core Modules
- **Convolutional Autoencoder**: Encoder-decoder architecture for learning measurement functions and their inverses (φ and φ⁻¹)
- **Koopman Operator Module**: Finite-dimensional matrix approximation C = φ ∘ K_φ ∘ φ⁻¹ of the infinite-dimensional Koopman operator
- **Consistent Koopman Variant**: Enhanced method ensuring consistency between encoding and prediction dynamics
- **Prediction Head**: Multi-step forecasting via C^k matrix powers

### Technical & Physics Fusion
- **Physics-Informed Constraint**: Network architectures explicitly constructed to satisfy Koopman operator properties (linear evolution of observables)
- **Dynamical Systems Framework**: Incorporates time-invariant system assumptions common to oceanographic flows
- **General Physical Prior**: Uses general dynamical systems physics rather than specific ocean PDEs, allowing transferability across domains
- **Interpretability**: Eigenvalues of C provide insight into system stability and dominant modal structures

## Math & Physics Modeling

### Optimization Objective
- Minimize reconstruction error in both encoder and decoder
- Ensure learned Koopman operator C produces physically consistent multi-step predictions
- Consistent Koopman adds constraints ensuring temporal consistency across prediction steps

### Key Equations/Physics
- **State Evolution**: z_{t+1} = φ(z_t) (discrete-time dynamical system)
- **Observable Mapping**: y_t = f(z_t) (measurement function)
- **Koopman Operator**: K_φ f(x) = f ∘ φ(x) (linear operator on observables)
- **Finite-Dimensional Approximation**: C = φ ∘ K_φ ∘ φ⁻¹
- **k-Step Prediction**: y_{t+k} = φ⁻¹ ∘ C^k ∘ φ(y_t)
- **Physical Context**: Loop Current dynamics and eddy shedding with 9-12 month propagation timescales

## Experiments

### Datasets
- Gulf of Mexico sea-surface temperature imagery
- Three years of historical training data
- 180-day prediction horizon evaluation

### Evaluation Metrics
- Forecast accuracy at various lead times (14, 30, 60, 90, 180 days)
- Comparison against persistence baselines
- Ability to capture Loop Current and eddy shedding dynamics

### Comparison Methods
- Persistence baseline (current state equals future state)
- Basic Koopman with convolutional autoencoder
- Consistent Koopman variant
- State-of-the-art numerical prediction systems (NOAA RTOFS)

### Core Results
- Koopman-based methods consistently outperform all baselines across prediction horizons
- Accurate SST prediction achievable up to 180 days (6 months) ahead
- Successfully captures Loop Current intrusions and warm eddy shedding events
- Consistent Koopman method provides improvements over basic Koopman approach
- Single present thermal image suffices; no requirement for extensive initial/boundary conditions

## Strengths
- Demonstrates unprecedented 180-day SST forecasting capability, far exceeding numerical model limits
- Elegant physics-informed framework with theoretical guarantees via Koopman operator properties
- Computational efficiency compared to numerical ocean models
- Interpretable latent space through dynamical systems lens
- No requirement for complex initial/boundary conditions
- Consistent Koopman variant provides principled improvement to basic approach

## Weaknesses
- Validated primarily for Gulf of Mexico region; generalizability to other ocean basins uncertain
- Performance depends on quality and length of training data availability
- May struggle with extreme events not well represented in training period
- Lacks integration with existing numerical weather prediction frameworks
- No explicit handling of atmospheric forcing or interannual variability
- Theoretical framework assumes time-invariant dynamics which may not hold for climate-scale changes

## Research Inspiration

### Directly Reusable Modules
- **Consistent Koopman Layer**: Can be adapted for other dynamical systems problems requiring temporal consistency
- **Convolutional Autoencoder + Koopman Architecture**: General framework for spatio-temporal forecasting problems
- **Multi-step Prediction via Matrix Powers**: Reusable technique for linear evolution in latent space

### Transferable Insights
- Koopman operator theory provides principled physics-informed inductive bias for time-series forecasting
- Linear evolution in latent space can capture complex nonlinear dynamics when properly constructed
- Single-image initialization for long-range forecasting is feasible for systems with strong coherent structures
- Consistency constraints between encoding and evolution improve prediction quality
- The 9-12 month eddy shedding timescale provides natural predictability boundary for Gulf of Mexico SST

## Idea Extensions
1. **Multi-basin Extension**: Apply framework to other ocean basins (e.g., Gulf Stream, El Niño regions) to test generalizability of Koopman-based forecasting
2. **NWP Integration**: Assimilate Koopman-based predictions into numerical weather prediction models as improved initial conditions or bias correction
3. **Climate-Scale Application**: Extend from seasonal (180-day) to interannual (multi-year) forecasting by incorporating climate mode indicators as additional observables
4. **Multi-variable Prediction**: Include additional ocean variables (sea surface height, salinity, chlorophyll) to capture coupled dynamics
5. **Adaptive Koopman**: Develop online learning approaches to adapt the Koopman operator as new data arrives, handling non-stationarity

## BibTeX
```bibtex
@article{rice2020koopman,
  title={Analyzing Koopman approaches to physics-informed machine learning for long-term sea-surface temperature forecasting},
  author={Rice, Julian and Xu, Wenwei and August, Andrew},
  year={2020},
  eprint={2010.00399},
  archivePrefix={arXiv},
  primaryClass={physics.geo-ph},
  note={arXiv preprint}
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
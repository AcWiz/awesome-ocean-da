---
title: CT-KAE: Continuous-Time Koopman Autoencoder for Efficient and Stable Ocean State Forecasting
arXiv: 2603.05560
authors:
- Rares Grozavescu
- Pengyu Zhang
- Mark Girolami
- Etienne Meunier
year: 2026
source: arXiv
venue: ICLR 2026
difficulty: ★★★★☆
importance: ★★★★☆
read_status: deep_read
method_tags:
- Koopman_Operator
- autoencoder
- continuous_time
- QG_model
- ocean_dynamics
application_tags:
- ocean_forecasting
- quasi_geostrophic
- chaotic_flows
- long_horizon
- surrogate_modeling
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# SSTODE: Ocean-Atmosphere Physics-Informed Neural ODEs for Sea Surface Temperature Prediction

## TL;DR
SSTODE uses physics-informed neural ODEs with advection-diffusion dynamics and energy exchanges integrator for interpretable global and regional SST prediction.

## Research Question
How can physics-informed neural ODEs capture ocean-atmosphere interactions for accurate and physically consistent sea surface temperature prediction?

## Main Contributions
1. Derives ODEs from fluid transport principles incorporating advection and diffusion for ocean spatiotemporal dynamics
2. Introduces Energy Exchanges Integrator (EEI) accounting for external forcing factors (SW, LW, SHF, LHF)
3. Recovers latent velocity field through variational optimization for explicit governing of SST temporal dynamics

## Method
SSTODE uses physics-informed Neural Ordinary Differential Equations framework. The model incorporates advection-diffusion dynamics derived from fluid transport principles. Variational optimization recovers latent velocity field. The Energy Exchanges Integrator encodes ocean heat budget equations for external forcing. The framework achieves state-of-the-art performance in global and regional SST forecasting benchmarks while maintaining physical consistency and interpretability.

## Datasets
- Global and regional SST forecasting benchmarks
- Sea surface temperature observations with ocean-atmosphere interaction data

## Core Results
- Achieves state-of-the-art performance in global SST forecasting
- Demonstrates interpretability of advection dynamics, thermal diffusion patterns, and diurnal cycles
- Physically consistent predictions validated across multiple regions

## Limitations
- Requires accurate velocity field recovery for optimal performance
- Performance depends on quality of forcing data
- May need adaptation for extreme events

## Research Gaps
- Extension to longer lead times and climate scale predictions
- Integration with coupled ocean-atmosphere models
- Application to sea ice and other ocean variables
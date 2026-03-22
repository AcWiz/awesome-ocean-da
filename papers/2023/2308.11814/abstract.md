---
title: Evaluation of Deep Neural Operator Models toward Ocean Forecasting
arXiv: 2308.11814
authors:
- Ellery Rajagopal
- Anantha N. S. Babu
- Tony Ryu
- Patrick J. Haley Jr.
- Chris Mirabito
- Pierre F. J. Lermusiaux
year: 2023
source: arXiv
venue: arXiv
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: deep_read
method_tags:
- DeepONet
- Fourier_Neural_Operator
- FourCastNet
- Latent_DeepONet
- Neural_Operator
application_tags:
- Ocean_Forecasting
- Ocean_Circulation
- Fluid_Dynamics
- Middle_Atlantic_Bight
- Massachusetts_Bay
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Evaluation of Deep Neural Operator Models toward Ocean Forecasting

## TL;DR
Deep neural operator models (DeepONet, FNO, FourCastNet, Latent DeepONet) demonstrate capability for ocean surface circulation forecasting in the Middle Atlantic Bight and Massachusetts Bay.

## Research Question
Can deep neural operator models effectively reproduce and predict realistic ocean dynamics, including periodic eddy shedding and surface circulation in real ocean regions?

## Main Contributions
1. Evaluates multiple neural operator architectures (DeepONet, FNO, FourCastNet, Latent DeepONet) for ocean forecasting applications
2. Demonstrates trained models can predict idealized periodic eddy shedding in 2D flow past a cylinder
3. Shows preliminary skill in predicting ocean surface circulation features in Middle Atlantic Bight and Massachusetts Bay from data-assimilative simulations

## Method
Deep neural operator models are trained on high-resolution data-assimilative simulations to learn mappings between infinite-dimensional function spaces. The study uses Fourier Neural Operators (FNOs) with Vision Transformers (FourCastNet) and Latent DeepONet architectures, trained on ocean state variables to predict forward time evolution without requiring governing equations or adjoint methods.

## Datasets
- 2D flow past a cylinder benchmark simulation for idealized fluid dynamics
- MITgcm ocean model simulations for Middle Atlantic Bight and Massachusetts Bay
- High-resolution data-assimilative simulations developed for real sea experiments

## Core Results
- Neural operator models successfully predict periodic eddy shedding in idealized 2D cylinder flow
- Preliminary ocean forecasting shows skill in capturing several surface circulation features
- Models demonstrate reduced computational cost during inference compared to traditional methods

## Limitations
- Preliminary ocean application study with limited validation on real observational data
- Performance heavily depends on discretization choices and training data quality
- Discretization invariance benefits may not fully apply to irregular ocean measurement grids

## Research Gaps
- Validation against actual ocean observations rather than model-derived training data
- Extension to three-dimensional ocean dynamics and longer prediction horizons
- Integration with physics-based constraints for improved dynamical consistency
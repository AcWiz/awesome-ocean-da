---
title: On the Choice of Training Data for Machine Learning of Geostrophic Mesoscale Turbulence
arXiv: 2307.00734
authors:
- F. E. Yan
- J. Mak
- Y. Wang
year: 2023
source: arXiv
venue: Journal of Advances in Modeling Earth Systems (JAMES)
difficulty: ★★★★☆
importance: ★★★★☆
read_status: deep_read
method_tags:
- CNN
- Eddy_Mean_Interaction
- Geostrophic_Turbulence
- Training_Data_Choice
- Robustness
application_tags:
- Ocean_Mesoscale
- Eddy_Parameterization
- QG_Turbulence
- Ocean_Modeling
- Rotational_Fluxes
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# On the Choice of Training Data for Machine Learning of Geostrophic Mesoscale Turbulence

## TL;DR
Training CNNs on eddy force function (filtered eddy fluxes) yields more robust models than training on divergence of eddy fluxes for ocean turbulence parameterization.

## Research Question
How does the choice of training data affect CNN model skill and robustness when learning eddy-mean interaction in geostrophic ocean turbulence?

## Main Contributions
1. Demonstrates that training data choice significantly impacts ML model performance for ocean turbulence
2. Proposes eddy force function as optimal training target that filters dynamically inert rotational fluxes
3. Shows models trained on filtered fluxes are more robust to noise than those trained on divergence

## Method
CNN trained on three output targets: divergence of eddy PV flux (standard), full eddy PV flux, and filtered eddy PV flux via eddy force function. Quasi-geostrophic double gyre configuration with time-averaged Reynolds decomposition. 20-member ensemble for statistical robustness. Noise injection experiments to test robustness.

## Datasets
- QG double gyre model (qgm2) with pseudo-spectral method
- 512x512 horizontal grid, 7.5km resolution
- Three-layer configuration with Rossby deformation radii 32.2km and 18.9km
- 20,000 day spinup + 5,000 day integration for time averages
- Finite element mesh for eddy force function computation via FEniCS

## Core Results
- Models trained on filtered fluxes (-gradient of eddy force function) outperform those trained on full eddy fluxes
- Comparable or better performance vs models trained on divergence of eddy fluxes
- Filtered flux models show 10x smaller rotational component contamination
- Significantly more robust to noise: divergence-trained models degrade rapidly with noise while filtered models remain stable
- L2 and Sobolev semi-norm (H^-1/2) metrics evaluated

## Limitations
- Time-averaging limitation for data availability
- Single QG double gyre configuration (may not generalize to other flows)
- Eddy buoyancy flux exception: divergence training slightly better when flux already smooth
- Theoretical gains may not matter if only seeking "working" model

## Research Gaps
- Extension to spatial averaging (vs time averaging) for eddy decomposition
- Online vs offline learning for parameterization
- Generalization to eddy-resolving global ocean simulations
- Multiple input choices and biased sampling strategies
- Information content quantification in training data

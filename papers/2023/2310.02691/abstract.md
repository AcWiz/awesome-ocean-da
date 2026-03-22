---
title: Robust Ocean Subgrid-Scale Parameterizations Using Fourier Neural Operators
arXiv: 2310.02691
authors:
- Victor Mangeleer
- Gilles Louppe
year: 2023
source: arXiv
venue: NeurIPS
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: deep_read
method_tags:
- Fourier_Neural_Operator
- FNO
- FFNO
- Subgrid_Scale_Parameterization
- Deep_Learning
application_tags:
- Ocean_Simulation
- Climate_Modeling
- Quasi-Geostrophic_Model
- Subgrid_Scale_Processes
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Robust Ocean Subgrid-Scale Parameterizations Using Fourier Neural Operators

## TL;DR
Fourier Neural Operators provide accurate and generalizable parameterizations for ocean subgrid-scale processes, outperforming empirical approaches.

## Research Question
How can Fourier Neural Operators develop accurate and generalizable parameterizations for computationally expensive ocean subgrid-scale processes?

## Main Contributions
1. Develops FNO-based parameterizations for ocean subgrid-scale processes
2. Demonstrates improved accuracy and generalizability compared to empirical parameterizations
3. Analyzes advantages and limitations of neural networks operating in frequency domain

## Method
Fourier Neural Operators learn subgrid-scale contributions from high-resolution simulation data. Parameterizations approximate missing subgrid-scale terms in low-resolution simulations. Model compared against FCNN, U-Net, and empirical approaches (Smagorinsky, Backscattering, Biharmonic, symbolic regression). Evaluated on quasi-geostrophic two-layer ocean model with jet-driven and eddy-driven flows.

## Datasets
- Two-layer quasi-geostrophic model (PyQG) simulations
- Jet-driven and eddy-driven flow regimes

## Core Results
- FNO-based parameterizations show improved accuracy
- Better generalization across different flow regimes
- Competitive with symbolic regression-based approaches

## Limitations
- Validated on idealized quasi-geostrophic model
- Performance depends on training data diversity
- May require retraining for different ocean regions

## Research Gaps
- Application to real ocean simulations
- Integration with global climate models
- Extension to 3D ocean dynamics
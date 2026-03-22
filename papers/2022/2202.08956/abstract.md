---
title: GNN-Surrogate: A Hierarchical and Adaptive Graph Neural Network for Parameter Space Exploration of Unstructured-Mesh Ocean Simulations
arXiv: 2202.08956v2
authors:
- Neng Shi
- Jiayi Xu
- Skylar W. Wurster
- Hanqi Guo
- Jonathan Woodring
- Luke P. Van Roekel
- Han-Wei Shen
year: 2022
source: arXiv
venue: arXiv preprint
difficulty: ★★★★☆
importance: ★★★★☆
read_status: skim
method_tags:
- Graph Neural Network
- Surrogate Model
- Unstructured Mesh
- Hierarchical Graph
application_tags:
- MPAS-Ocean
- Parameter Space Exploration
- Ocean Climate Simulation
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# GNN-Surrogate: Hierarchical and Adaptive Graph Neural Network for Parameter Space Exploration of Unstructured-Mesh Ocean Simulations

## TL;DR
GNN-Surrogate uses graph neural networks on hierarchical unstructured meshes to predict MPAS-Ocean simulation outputs from input parameters.

## Research Question
How can graph neural networks efficiently predict ocean simulation outputs on unstructured meshes for parameter space exploration without running expensive simulations?

## Main Contributions
1. Proposes GNN-Surrogate for learning parameter-to-simulation-output mapping on unstructured grids
2. Introduces hierarchical graph construction and adaptive resolution for GPU memory efficiency
3. Demonstrates 50x computational speedup (2s vs 50min) with good accuracy for MPAS-Ocean ensemble visualization

## Method
Hierarchical graphs built from MPAS-Ocean unstructured Voronoi meshes via graph coarsening. Edge-weighted graph construction captures horizontal/vertical connectivity and geographic directional relationships (6 directions). Graph hierarchy cutting based on region sensitivity analysis to reduce computation. Adaptive resolution training data generation. Upsampling-convolution generator architecture with graph convolution and upsampling operators. L1 loss training with spectral normalization and mixed precision.

## Datasets
- MPAS-Ocean model simulations (EC60to30 resolution, 235,160 Voronoi cells per layer)
- 4 parameters studied: wind stress amplitude (BwsA), Gent-McWilliams eddy parameterization (GM), bulk Richardson number (CbrN), horizontal viscosity (HV)
- 100 ensemble members: 70 training, 30 testing
- 15-model-day simulations

## Core Results
- GNN-Surrogate achieves PSNR=50.7dB globally, 39.5dB in ROI (eastern equatorial Pacific cold tongue)
- Outperforms IDW and RBF interpolation methods in data-level, geometry-level, and image-level evaluations
- 2-second inference vs 50-minute full simulation on supercomputer
- Successfully captures sensitivity ranking: BwsA > CrbN > GM > HV
- Effective parameter space exploration for wind stress effects on ocean temperature

## Limitations
- 36-hour offline training time
- Fixed reference selection for sensitivity estimation may not represent all parameter space regions
- Single ocean model (MPAS-Ocean) validation
- Does not support time-varying data directly

## Research Gaps
- Multi-GPU training acceleration
- Neural network-based super-resolution for adaptive-to-full resolution conversion
- Extension to 4D convolutions for time-varying simulations
- Generalization to other unstructured-mesh ocean/climate models
- Kriging-based interpolation comparison

---
title: AI-GOMS: Large AI-Driven Global Ocean Modeling System
arXiv: 2308.03152
authors:
- Wei Xiong
- Yanfei Xiang
- Hao Wu
- Shuyi Zhou
- Yuze Sun
- Muyuan Ma
- Xiaomeng Huang
year: 2023
source: arXiv
venue: arXiv
difficulty: ★★★★★
importance: ★★★★★
read_status: deep_read
method_tags:
- Masked_Autoencoder
- Fourier_Based
- Backbone_Downstream
- Global_Ocean_Modeling
- Deep_Learning
application_tags:
- Global_Ocean_Modeling
- Ocean_Prediction
- Mesoscale_Eddies
- Ocean_Variables
- Earth_System
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# AI-GOMS: Large AI-Driven Global Ocean Modeling System

## TL;DR
AI-GOMS uses Fourier-based masked autoencoder backbone with downstream fine-tuning modules for 30-day global ocean prediction at 1/4 degree resolution.

## Research Question
How can a large AI model achieve accurate and efficient global ocean daily prediction across multiple variables, depths, and downstream tasks?

## Main Contributions
1. Proposes AI-GOMS with backbone-downstream paradigm for transferrable ocean modeling
2. Achieves best performance for all 5 ocean variables (T, S, U, V, SSH) at 15 depth layers over 30 days
3. Demonstrates mesoscale eddy simulation in Kuroshio at 1/12 degree via downscaling module

## Method
Backbone: Fourier-based masked autoencoder (AFNO) with asymmetric encoder-decoder structure. Random mask strategy for multi-scale learning. 16 encoder layers, 8 decoder layers, patch embedding (8x8 patches). Supports 2D/3D/sparse input. Autoregressive daily prediction. Downstream modules: regional downscaling (3x super-resolution), wave decoding, biochemistry coupling.

## Datasets
- HYCOM global reanalysis (1/12 degree, 41 vertical layers, 3-hourly, 1994-2015)
- Training: 2000-2010, Validation: 2011, Test: 2012
- 15 depth layers: 0-500m
- ERA5 atmospheric forcing, ETOPO bathymetry
- NASA ocean biochemistry for coupling module

## Core Results
- Outperforms FourCastNet on all variables in ACC and RMSE
- 30-day prediction at 1/4 degree with 15 depth layers
- Downscaling: 1/4 to 1/12 degree for Kuroshio (ACC>0.6 for 7-day velocity and SSH)
- Wave decoding: 30-day significant wave height prediction
- Biochemistry coupling: 8 variables including chlorophyll, nitrate, mixed layer depth
- 34.2 hours training on 4x16 A100 GPUs

## Limitations
- Still limited to 1/4 degree resolution (not eddy-resolving globally)
- Single backbone model without online data assimilation
- Fixed 15 vertical layers may miss deep ocean dynamics
- Transfer learning benefits not fully quantified
- Computational requirements for training still significant

## Research Gaps
- Native sparse data assimilation at model level
- More transfer learning techniques for reduced fine-tuning cost
- Extension to sub-monthly and seasonal timescales
- Integration with operational ocean forecasting systems
- Global eddy-resolving predictions (below 1/12 degree)

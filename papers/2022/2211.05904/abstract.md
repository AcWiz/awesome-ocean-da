---
title: 4DVarNet-SSH: End-to-End Learning of Variational Interpolation Schemes for Nadir and Wide-Swath Satellite Altimetry
arXiv: 2211.05904
authors:
- Maxime Beauchamp
- Quentin Febvre
- Hugo Georgenthum
- Ronan Fablet
year: 2022
source: arXiv
venue: N/A - Preprint
difficulty: ★★★★☆
importance: ★★★★★
read_status: skim
method_tags:
- 4DVarNet
- Deep Learning
- SSH
- Satellite Altimetry
- SWOT
application_tags:
- Sea Surface Height
- Gulf Stream
- OSMOSIS
- NATL60
- DUACS
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# 4DVarNet-SSH: End-to-End Learning of Variational Interpolation Schemes for Nadir and Wide-Swath Satellite Altimetry

## TL;DR
4DVarNet-SSH combines deep learning with variational data assimilation for sea surface height interpolation from sparse satellite altimetry, outperforming operational DUACS OI.

## Research Question
How can neural networks learn optimal space-time interpolation of sparse satellite altimeter data to reconstruct mesoscale sea surface dynamics?

## Main Contributions
1. Proposes end-to-end neural architecture for SSH interpolation using 4DVarNet variational DA framework
2. Demonstrates 30-60% relative improvement over operational DUACS optimal interpolation
3. Achieves resolved scales below 70km and 7 days with nadir+SWOT configuration

## Method
4DVarNet framework with trainable LSTM-based gradient solver. Augmented state formulation: x = (SSH, dx1, dx2) where dx represents anomaly from large-scale OI field. Multiscale decomposition separates large-scale (DUACS OI) from anomaly. Prior operator F uses two-scale residual architecture with bilinear units. 5 gradient iterations. Loss combines reconstruction and gradient losses with temporal weighting.

## Datasets
- NATL60 NEMO model simulation (1/60 degree resolution, ~7km effective)
- OSSE with pseudo-nadir altimetry (4 missions: TOPEX/Poseidon, Geosat, Jason-1, Envisat)
- SWOT wide-swath pseudo observations
- Regions: GULFSTREAM (10x10 deg), OSMOSIS (8x10 deg), cNATL (20x40 deg)
- Training: Feb-Sep 2013; Test: Oct-Dec 2012

## Core Results
- GULFSTREAM: mRMSE=0.94cm, resolved scales 0.83 deg/8 days (nadir), 0.62 deg/5.29 days (nadir+SWOT)
- OSMOSIS: mRMSE=0.80-0.87cm, resolved scales 1.18 deg/14.5 days (nadir), 0.35 deg/6.84 days (nadir+SWOT)
- 20-60% relative improvement over DUACS OI depending on region and configuration
- Ensemble UQ via multiple training runs: ensemble std correlates with error (R2=0.86)

## Limitations
- OSSE framework (synthetic observations) - real data performance待验证
- Error-free SWOT assumption - real SWOT errors not considered
- Regional-scale training limits global applicability
- 4-8 hour training time per configuration

## Research Gaps
- Application to real SWOT and nadir altimetry observations
- Basin-scale and global-scale training
- Integration of attention mechanisms for space-time variability
- Multi-swot configurations optimization
- Generalization to other ocean parameters (SST, salinity)

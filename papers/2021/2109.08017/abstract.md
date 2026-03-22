---
title: Super-resolution data assimilation
arXiv: 2109.08017v1
authors: Sébastien Barthélémy; Julien Brajard; Laurent Bertino; François Counillon
year: 2021
source: arXiv
venue: arXiv
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: read
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Super-resolution data assimilation

## TL;DR
Super-resolution data assimilation (SRDA) uses neural networks to emulate high-resolution fields from low-resolution forecasts, reducing errors by 40% with only 55% computational cost increase.

## Research Question
How can the computational cost of high-resolution data assimilation be reduced while maintaining accuracy by leveraging super-resolution techniques?

## Main Contributions
1. Proposes SRDA algorithm combining low-resolution forecast integration with neural network high-resolution emulation
2. Demonstrates 40% error reduction with only 55% computational cost increase compared to low-resolution ensemble Kalman filter
3. Shows NN ability to anticipate systematic differences between low and high resolution model dynamics

## Method
SRDA performs forecast steps using a computationally cheap low-resolution model, then uses a trained neural network to map low-resolution forecasts to high-resolution fields for assimilation with high-resolution observations. The ensemble Kalman filter analysis is computed in high-resolution space. The neural network learns to correct systematic differences in eddy propagation speeds between resolutions.

## Datasets
- Quasi-geostrophic model representing simplified surface ocean dynamics
- Synthetic observations at high resolution
- Model resolutions up to 4 times lower than reference high-resolution configuration

## Core Results
- Error reduction of 40% compared to low-resolution data assimilation
- Performance close to high-resolution system (16% larger error vs 92% larger for LR-EnKF)
- Computational cost increase of only 55% above LR data assimilation system

## Limitations
- Relies on accurate neural network emulation of high-resolution dynamics
- Performance depends on similarity between training and operational conditions
- Validated on simplified quasi-geostrophic model; needs validation on more realistic ocean models

## Research Gaps
- Application to realistic ocean models with full physics and bathymetry
- Integration with operational forecasting systems
- Development of adaptive neural network training for non-stationary dynamics
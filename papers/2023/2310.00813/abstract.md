---
title: OceanNet: A Principled Neural Operator-Based Digital Twin for Regional Oceans
arXiv: 2310.00813
authors:
- Ashesh Chattopadhyay
- Michael Gray
- Tianning Wu
- Anna B. Lowe
- Ruoying He
year: 2023
source: arXiv
venue: arXiv
difficulty: ★★★★☆
importance: ★★★★★
read_status: deep_read
method_tags:
- Fourier_Neural_Operator
- Digital_Twin
- Spectral_Regularizer
- PEC_Scheme
- Neural_Operator
application_tags:
- Ocean_Forecasting
- Sea_Surface_Height
- Gulf_Stream
- Loop_Current
- Regional_Ocean_Modeling
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# OceanNet: A Principled Neural Operator-Based Digital Twin for Regional Oceans

## TL;DR
OceanNet achieves 500,000x computation reduction compared to dynamical ocean models using Fourier neural operator with predictor-evaluator-corrector integration.

## Research Question
How can neural operators create stable and accurate digital twins for regional ocean modeling with complex bathymetry and western boundary currents?

## Main Contributions
1. Proposes OceanNet using Fourier neural operator with PEC integration scheme to mitigate autoregressive error growth
2. Spectral regularizer counteracts spectral bias at smaller scales for turbulent flows
3. Demonstrates competitive forecast skill compared to state-of-the-art dynamical ocean model with 500,000x computation reduction

## Method
OceanNet uses Fourier neural operator architecture with predictor-evaluate-correct (PEC) integration scheme. Spectral regularizer addresses spectral bias that causes instability in long-term integration. Model trained on historical SSH data from northwest Atlantic Ocean reanalysis. Applied to Gulf Stream and Loop Current eddy prediction in northwest Atlantic Ocean.

## Datasets
- Northwest Atlantic Ocean sea surface height (SSH) reanalysis data
- Gulf Stream and Loop Current regions

## Core Results
- Competitive forecast skill compared to dynamical ocean model
- 500,000x computation reduction compared to numerical simulation
- Long-term stability demonstrated for seasonal prediction

## Limitations
- Validated primarily on SSH prediction
- Performance depends on training data quality and length
- Regional application; generalizability to global ocean requires further study

## Research Gaps
- Extension to subsurface ocean variables
- Integration with data assimilation for improved initial conditions
- Application to other ocean basins and phenomena
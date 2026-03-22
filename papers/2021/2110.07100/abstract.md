---
title: Digital Twin Earth - Coasts: Developing a Fast and Physics-Informed Surrogate Model for Coastal Floods via Neural Operators
arXiv: 2110.07100v1
authors:
- Peishi Jiang
- Nis Meinert
- Helga Jordão
- Constantin Weisser
- Simon Holgate
- Alexander Lavin
- Björn Lütjens
- Dava Newman
- Haruko Wainwright
- Catherine Walker
- Patrick Barnard
year: 2021
source: arXiv
venue: arXiv preprint
difficulty: ★★★★★
importance: ★★★★★
read_status: skim
method_tags:
- Fourier Neural Operator
- Physics-Informed ML
- Surrogate Modeling
- Digital Twin
application_tags:
- Coastal Floods
- Sea Surface Height
- NEMO
- Coastal Dynamics
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Digital Twin Earth - Coasts: Developing a Fast and Physics-Informed Surrogate Model for Coastal Floods via Neural Operators

## TL;DR
CoastalTwin platform achieves 45x speedup over NEMO using FNO surrogate for coastal flood prediction with accurate SSH emulation.

## Research Question
How can neural operators create fast and accurate surrogates for coastal ocean models to enable efficient risk estimation and decision-making?

## Main Contributions
1. Develops first coastal digital twin using FNO surrogate for NEMO ocean model
2. Achieves 45x acceleration over NEMO simulation while maintaining accuracy
3. Delivers open-source CoastalTwin platform for extensible coastal modeling

## Method
Fourier Neural Operator surrogate built on NEMO (Nucleus for European Modelling of the Ocean) simulations. FNO learns multivariate dynamics including sea surface height from atmospheric forcings. Platform designed in end-to-end modular way for easy extensions. Validated on northwestern Europe coastal region with 7km resolution.

## Datasets
- NEMO simulations for northwestern Europe (7km resolution, 520x292 grids)
- Atmospheric forcings: MSLP, U10, V10 wind components
- 2020 simulation data at 5-minute intervals

## Core Results
- Upwards of 45x acceleration over NEMO simulation
- Accurate SSH prediction in most regions
- Open-source platform enables extensions to other simulations

## Limitations
- Validated primarily on northwestern Europe
- Land boundary masking impacts training
- Performance may vary for extreme events

## Research Gaps
- Extension to global coastlines
- Integration with real-time data assimilation
- Application to coastal flood prediction under sea level rise
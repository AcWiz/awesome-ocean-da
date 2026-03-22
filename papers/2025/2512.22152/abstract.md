---
title: Neural ocean forecasting from sparse satellite-derived observations: a case-study for SSH dynamics and altimetry data
arXiv: 2512.22152
authors:
- Daria Botvynko
- Pierre Haslee
- Lucile Gaultier
- Bertrand Chapron
- Clément de Boyer Montégut
- Anass El Aouni
- Julien Le Sommer
- Ronan Fablet
year: 2025
source: arXiv
venue: Nature
difficulty: ★★★★☆
importance: ★★★★★
read_status: deep_read
method_tags:
- U-Net
- 4DVarNet
- satellite_altimetry
- SSH_forecasting
- end_to_end_learning
application_tags:
- sea_surface_height
- ocean_circulation
- nadir_altimeters
- GLO12
- ocean_forecasting
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Neural Ocean Forecasting from Sparse Satellite-Derived Observations: A Case-Study for SSH Dynamics and Altimetry Data

## TL;DR
End-to-end neural forecasting with 4DVarNet outperforms operational Mercator Ocean GLO12 system for SLA prediction from sparse satellite altimetry.

## Research Question
How can end-to-end neural networks forecast ocean sea level anomaly from sparse satellite observations without relying on physics-based data assimilation?

## Main Contributions
1. Proposes end-to-end neural forecasting from sparse satellite altimetry to full-field SLA prediction
2. Demonstrates 4DVarNet achieves best performance, outperforming GLO12 and other neural emulators
3. Establishes standardized benchmark within OceanBench initiative for reproducible neural ocean forecasting

## Method
Sequence-to-sequence mapping from 14-day sparse SLA snapshots to 7-day future full-field SLA. Two architectures: U-Net and 4DVarNet. OSSE-based training with synthetic nadir sampling patterns applied to GLORYS12 reanalysis. 4DVarNet combines state/MSE loss, gradient loss, and variational regularization. Evaluated globally against SARAL/AltiKa and drifter observations.

## Datasets
- GLORYS12 ocean reanalysis (1/4 degree, daily SLA, 2010-2019 training)
- Real satellite altimetry from near-real-time CMEMS product
- SARAL/AltiKa for SLA validation
- Drifter observations for surface current validation

## Core Results
- 4DVarNet: nRMSE improvement of -1.35% (offshore high variability) to 8.85% (coastal) vs GLO12 at lead time 0
- 4DVarNet maintains positive gains relative to DUACS at lead times 3 and 5
- U-Net shows competitive performance but loses energy at longer leads
- Significant improvements at small scales (65-500km) in offshore regions
- Both neural models outperform GLO12 baseline across all metrics

## Limitations
- 7-day forecast horizon may not capture longer-term ocean dynamics
- Single variable focus (SLA) limits operational applicability
- Training on synthetic nadir patterns may not fully represent real observation gaps
- Uncertainty quantification not addressed

## Research Gaps
- Multi-variable forecasting (SST, salinity, currents)
- Integration with real observation training schemes
- Uncertainty quantification via generative approaches
- Extension to coastal and high-latitude regions

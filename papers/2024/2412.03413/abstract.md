---
title: Deep Learning for Sea Surface Temperature Reconstruction under Cloud Occlusion
arXiv: 2412.03413
authors:
- Andrea Aspertia
- Ali Aydogdub
- Angelo Grecoa
- Fabio Merizzia
- Pietro Miragliob
- Beniamino Tartufolici
- Alessandro Testaa
- Nadia Pinardic
- Paolo Oddob
year: 2024
source: arXiv
venue: Elsevier
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: deep_read
method_tags:
- U-Net
- Vision_Transformer
- DINCAE
- CNN
application_tags:
- SST_reconstruction
- cloud_filling
- satellite_Ocean
- MODIS
- oceanography
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Deep Learning for Sea Surface Temperature Reconstruction under Cloud Occlusion

## TL;DR
U-Net64 with 4-day temporal input achieves 50% lower RMSE than DINCAE and L4 operational products for cloud-occluded SST reconstruction.

## Research Question
How can deep learning models reconstruct sea surface temperature data under cloud occlusion while preserving fine-scale features and avoiding smoothing artifacts?

## Main Contributions
1. Proposes U-Net64 architecture with 4-day temporal input achieving 0.30 RMSE, 50% lower than DINCAE
2. Demonstrates deep learning significantly outperforms optimal interpolation and L4 statistical products for cloud filling
3. Validates model transferability from MODIS-AQUA training to Copernicus L3S operational products

## Method
U-Net with [64,128,256,512] channel configuration and residual blocks. Input: 4 consecutive days of MODIS-AQUA nighttime SST with artificial cloud masks. Unbiased seasonal climatology subtraction for anomaly learning. Generator-based training with configurable cloud occlusion (40% average). AdamW optimizer, early stopping, learning rate reduction. 128x128 spatial splitting into quadrants improves performance.

## Datasets
- MODIS-AQUA L3 SST (4km resolution, nighttime, 2002-2023)
- MODIS-TERRA for validation
- Italian Seas region (35-46N, 7-18E)
- Copernicus L3S operational product for transfer testing

## Core Results
- U-Net64 RMSE: 0.30°C (vs DINCAE 0.54°C) - 44% improvement
- U-Net64 with 128x128 quadrants: 0.28°C average RMSE
- L4 comparison: U-Net64 error 0.04°C vs L4 error 0.14°C
- Performance degrades linearly with cloud coverage (~0.005°C per 1% increase)
- Best reconstruction: Adriatic Sea (RMSE 0.283°C); most challenging: Ionian Sea (0.314°C)

## Limitations
- Regional focus (Italian Seas) limits global applicability
- Nighttime-only training may not capture diurnal cycle
- Diffusion models failed to achieve competitive performance
- Performance degrades in coastal zones with complex topography
- 256x256 model underperforms split quadrants approach

## Research Gaps
- Extension to full Mediterranean Sea
- Integration of microwave measurements for all-weather coverage
- Multi-sensor fusion with VIIRS and other satellites
- Physics-informed constraints for dynamical consistency
- Real-time operational implementation

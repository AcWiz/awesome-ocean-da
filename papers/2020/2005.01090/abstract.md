---
title: Filtering Internal Tides from Wide-Swath Altimeter Data Using Convolutional Neural Networks
arXiv: 2005.01090v1
authors:
- Redouane Lguensat
- Ronan Fablet
- Julien Le Sommer
- Sammy Metref
- Emmanuel Cosme
- Kaouther Ouenniche
- Lucas Drumetz
- Jonathan Gula
year: 2020
source: arXiv
venue: IEEE
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: skim
method_tags:
- CNN
- Deep Learning
- Internal Gravity Waves Filtering
- SWOT
application_tags:
- Sea Surface Height
- Altimetry
- Ocean Dynamics
- Mesoscale
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Filtering Internal Tides from Wide-Swath Altimeter Data Using Convolutional Neural Networks

## TL;DR
ConvNet filters internal gravity waves from SWOT SSH measurements, achieving effective tide removal on par with 24h averaging.

## Research Question
How can deep learning filter internal tide signals from SWOT satellite altimetry measurements to recover mesoscale and submesoscale ocean dynamics?

## Main Contributions
1. Proposes ConvNet-based filtering method to separate internal tides from non-tidal SSH signals for SWOT mission
2. Demonstrates effective filtering for both summer and winter sea surface dynamics using eNATL60 simulations
3. Shows multi-modal approach combining SSH and SST improves filtering performance

## Method
Convolutional Neural Networks (ResNet architecture) trained on high-resolution eNATL60 North Atlantic simulations. Network takes SSH snapshots (single or temporal sequences) as input and outputs filtered tide-free SSH. Loss function combines MSE on SSH and absolute error on Laplacian. Three input variants: SSH only, 3 temporal SSH snapshots, or 3SSH combined with SST.

## Datasets
- eNATL60 NEMO model simulation (1/60° resolution, hourly output)
- OSMOSIS region (44.8°N-55.4°N, 20°W-10°W)
- Summer (JAS) and winter (JFM) datasets
- 24h-averaged SSH as reference tide-free state

## Core Results
- ConvNet significantly outperforms linear 5x5 filtering baseline
- Multi-temporal SSH (3SSH) outperforms single snapshot approach
- Adding SST provides marginal improvement over 3SSH
- Effective filtering in both seen and unseen geographic regions

## Limitations
- Validated on simulation data only, not real SWOT observations
- Spatial splitting for train/test may not capture all regional variations
- Performance decreases in winter due to intensified non-wave processes

## Research Gaps
- Application to real SWOT satellite data
- Integration with other noise sources (instrument noise, orbit errors)
- Extension to submesoscale filtering

---
title: Deep learning in the abyss: a stratified Physics Informed Neural Network for data assimilation
arXiv: 2503.19160
authors:
- Vadim Limousin
- Nelly Pustelnik
- Bruno Deremble
- Antoine Venaille
year: 2025
source: arXiv
venue: JGR (Journal of Geophysical Research)
difficulty: ★★★★☆
importance: ★★★★★
read_status: deep_read
method_tags:
- PINN
- SIREN
- data_assimilation
- quasi_geostrophic
- stratified_ocean
application_tags:
- deep_ocean
- SWOT
- ARGO
- ocean_circulation
- mesoscale
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Deep learning in the abyss: A stratified Physics Informed Neural Network for data assimilation

## TL;DR
StrAss-PINN uses multi-layer Physics-Informed Neural Networks with SIREN architecture to reconstruct deep ocean flows from surface SWOT-like and sparse ARGO-like observations.

## Research Question
How can deep ocean currents be reconstructed from sparse interior data when surface observations are available but interior measurements are extremely limited?

## Main Contributions
1. Proposes StrAss-PINN (Stratified Assimilation PINNs) with separate networks for each ocean layer that interact during training
2. Successfully reconstructs ocean mesoscale features including vortex rings, eastward jets, and Rossby waves using SIREN architecture
3. Demonstrates proof of concept for deep flow reconstruction from surface SSH and sparse ARGO float observations

## Method
StrAss-PINN assigns a separate neural network to each layer of a three-layer quasi-geostrophic ocean model. Using SIREN architecture (multilayer perceptron with sine activation functions), the network takes spatiotemporal coordinates as input and predicts velocity fields. Training combines observational data with dynamical priors enforced at multiple collocation points, propagating information between vertical layers.

## Datasets
- Three-layer quasi-geostrophic model for synthetic ocean dynamics
- SWOT-like pseudo-observations of sea surface height (surface layer)
- ARGO-like pseudo-observations for interior and deep layer measurements

## Core Results
- Strong ability to resolve key ocean mesoscale features including vortex rings and eastward jets
- Successfully reconstructs flows in both interior and surface layers from limited measurements
- Demonstrates capability to infer deep ocean dynamics from surface-intensified and sparse subsurface data

## Limitations
- Proof of concept using simplified three-layer quasi-geostrophic model; not yet applied to real observational data
- No direct comparison with traditional assimilation techniques (4DVAR, EnKF) provided
- Performance on multiscale chaotic flows requires further investigation

## Research Gaps
- Application to real-world observational data including actual SWOT satellite and ARGO float measurements
- Extension to more realistic and higher-resolution ocean models
- Comparative evaluation against established data assimilation methods
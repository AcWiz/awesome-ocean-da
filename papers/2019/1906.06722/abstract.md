---
title: A Fast Tunable Blurring Algorithm for Scattered Data
arXiv: 1906.06722v2
authors:
- Gregor Robinson
- Ian Grooms
year: 2019
source: arXiv
venue: arXiv preprint
difficulty: ★★★☆☆
importance: ★★★★☆
read_status: skim
method_tags:
- Multiresolution Gaussian
- RBF Interpolation
- Fractional Laplacian
- Scale Separation
application_tags:
- Data Assimilation
- Ocean Modeling
- Particle Filtering
- Signal Processing
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# A Fast Tunable Blurring Algorithm for Scattered Data

## TL;DR
Linear-time blurring algorithm with tunable spectrum enables scale separation for scattered geophysical data, with applications to data assimilation and ocean eddy analysis.

## Research Question
How can small-scale content be attenuated in data measured at scattered locations in spatially extended domains of arbitrary dimension?

## Main Contributions
1. Proposes blurring algorithm with linear time complexity for scattered data in arbitrary dimensions
2. Generalizes conventional blurring algorithms to data at non-uniform locations
3. Enables scale separation for scattered oceanographic float measurements and improves particle filter performance for data assimilation

## Method
The algorithm forms a Gaussian interpolant of scattered input data, then convolves with a multiresolution Gaussian approximation of the Green's function to a differential operator with tunable spectrum. The fractional bound-state Helmholtz operator has eigenvalues that can be tuned via length scale and power parameters. The method is equivalent to solving a positive definite self-adjoint elliptic PDE.

## Datasets
- Scattered oceanographic float measurements (for scale decomposition example)
- Meteorological observations (for particle filtering application)

## Core Results
- Linear time complexity achieved
- Tunable spectral response enables problem-specific scale separation
- Successfully decomposes scattered data into large-scale and small-scale components

## Limitations
- Requires appropriate kernel selection for specific applications
- Performance depends on choice of tuning parameters

## Research Gaps
- Application to operational ocean data assimilation systems
- Integration with ensemble filtering methods for real-time forecasting
- Extension to time-varying dynamical systems
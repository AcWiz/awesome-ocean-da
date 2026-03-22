---
title: Computer Model Calibration Using the Ensemble Kalman Filter
arXiv: 1204.3547
authors:
- Dave Higdon
- Matt Pratola
- Jim Gattiker
- Earl Lawrence
- Charles Jackson
- Michael Tobis
- Salman Habib
- Katrin Heitmann
- Steve Price
year: 2012
source: arXiv
venue: Technometrics
difficulty: ★★★★☆
importance: ★★★★★
read_status: deep_read
method_tags:
- EnKF
- Computer Model Calibration
- Gaussian Process Emulator
- Bayesian Inference
application_tags:
- Cosmology
- Climate Modeling
- Ice Sheet Modeling
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Computer Model Calibration Using the Ensemble Kalman Filter

## TL;DR
EnKF applied to computer model calibration problems, combining observational data with computationally expensive forward models for Bayesian parameter estimation.

## Research Question
How can the Ensemble Kalman Filter be adapted for computer model calibration where the goal is estimating static model parameters using physical observations combined with computational models?

## Main Contributions
1. Shows EnKF implicitly uses linear regression-based emulator, enabling handling of large ensembles and high-dimensional input/output spaces
2. Demonstrates EnKF calibration on cosmological parameters (LCDM model) and Community Atmosphere Model (CAM 3.1)
3. Uses EnKF for optimal experimental design in ice sheet measurement placement

## Method
Two EnKF variants for static calibration: Gaussian representation (multivariate normal approximation) and ensemble representation (sample-based). Both use ensemble of forward model runs to estimate prior covariance. Includes two-stage approach for improved linear approximation. Applications to cosmology (5 LCDM parameters, 128 simulations), climate (15 CAM parameters, 1400 runs), and ice sheet modeling (optimal measurement locations).

## Datasets
- Sloan Digital Sky Survey (SDSS) galaxy observations
- N-body cosmological simulations (LCDM)
- Community Atmosphere Model CAM 3.1 (15 parameters)
- Community ice sheet model (CISM) idealized setup

## Core Results
- Posterior distributions similar to GP emulator-based methods but with lighter computational requirements
- EnKF can handle ensemble sizes larger than practical for MCMC
- D-optimal design for ice sheet measurements finds informative locations

## Limitations
- Implicit linear emulator may truncate posterior tails
- Prior specification and covariance estimation critical
- Limited to problems where ensemble size can capture parameter space

## Research Gaps
- Integration with gradient-based optimization for high-dimensional problems
- Adaptive covariance estimation strategies
- Comparison with MCMC for exact Bayesian inference

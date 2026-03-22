---
title: Automated Identification of Metamorphic Test Scenarios for an Ocean-Modeling Application
arXiv: 2009.01554v1
authors:
- Dilip J. Hiremath
- Martin Claus
- Wilhelm Hasselbring
- Willi Rath
year: 2020
source: arXiv
venue: arXiv preprint
difficulty: ★★★☆☆
importance: ★★☆☆☆
read_status: skim
method_tags:
- Metamorphic Testing
- Machine Learning
- Ocean Modeling
- Software Testing
application_tags:
- Ocean Model Validation
- Software Testing
- Metamorphic Relations
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Automated Identification of Metamorphic Test Scenarios for an Ocean-Modeling Application

## TL;DR
ML-based metamorphic testing identifies relations (g, h) for ocean model validation where test oracles are unavailable.

## Research Question
How can machine learning automate the discovery of metamorphic test relations for validating ocean-modeling software without test oracles?

## Main Contributions
1. Proposes ML-based approach to automatically identify metamorphic relations (g, h) where f(g(X)) = h(f(X))
2. Cost function penalizes identity map solutions while rewarding metamorphic transformations
3. Demonstrates automated test generation for ocean kinetic energy calculation application

## Method
ML algorithms minimize custom cost function to find affine transformation g. Cost function rewards metamorphic behavior (f(g(X)) close to f(X)) while penalizing g being identity map. Iterative orthogonalization identifies multiple independent metamorphic relations. Constrains h to identity map for initial problem simplification.

## Datasets
- Kinetic energy calculation from sea level ssh fields (QG double gyre-style ocean model)
- Two software implementations (one respecting cyclic boundary, one not)
- Finite difference discretization for numerical implementation
- Artifact available on Binder for reproducibility

## Core Results
- Successfully identified multiple metamorphic relations from physical symmetries
- Detected implementation bug in non-cyclic-boundary version
- Method generalizes to find orthogonal metamorphic relations iteratively
- Physical symmetries (sign changes, scaling, transposition, translation) recoverable as metamorphic relations

## Limitations
- Restricted to h being identity map (general h not explored)
- g limited to affine transformations (non-linear g not considered)
- Single ocean-modeling application demonstrated
- Monte Carlo optimization may converge to local minima

## Research Gaps
- Relaxing h identity constraint for broader metamorphic relation discovery
- Non-linear metamorphic transformations beyond affine
- Transfer of discovered relations across different ocean modeling applications
- Integration with continuous integration testing pipelines

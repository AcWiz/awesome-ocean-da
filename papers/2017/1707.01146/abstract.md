---
title: Data-driven discovery of Koopman eigenfunctions for control
arXiv: 1707.01146
authors:
- Eurika Kaiser
- J. Nathan Kutz
- Steven L. Brunton
year: 2017
source: arXiv
venue: IEEE Transactions on Automatic Control / arXiv
difficulty: ★★★★★
importance: ★★★★★
read_status: deep_read
method_tags:
- Koopman Operator
- DMD
- EDMD
- System Identification
- Optimal Control
application_tags:
- Nonlinear Control
- Hamiltonian Systems
- Ocean Double-Gyre
- Dynamical Systems
ocean_vars: Unknown
spatiotemporal_res: Unknown
---
# Data-driven Discovery of Koopman Eigenfunctions for Control

## TL;DR
KRONIC framework validates Koopman eigenfunctions and constructs reduced-order models in intrinsic coordinates for nonlinear system control.

## Research Question
How can Koopman eigenfunctions be validated and used to construct improved reduced-order models for nonlinear system control?

## Main Contributions
1. Illustrates fundamental closure issue in finite-dimensional Koopman approximations and proposes validation approach
2. Demonstrates that lightly damped eigenfunctions can be faithfully extracted from EDMD for control applications
3. Proposes KRONIC (Koopman Reduced Order Nonlinear Identification and Control) architecture for control in eigenfunction coordinates

## Method
The method first validates eigenfunctions by checking their Koopman-invariant properties, then constructs reduced-order models in these validated coordinates. Eigenfunctions are approximated using data-driven regression and power series expansions based on the PDE governing the infinitesimal generator. Control is formulated directly in intrinsic Koopman coordinates, where dynamics are linear by design.

## Datasets
- Nonlinear system with known linear embedding
- Hamiltonian systems
- High-dimensional double-gyre model for ocean mixing

## Core Results
- Improved predictive power through Koopman-invariant subspace construction
- Validated eigenfunctions enable reliable reduced-order control
- Demonstrates control in intrinsic coordinates for various dynamical systems

## Limitations
- Requires sufficiently rich data for accurate eigenfunction identification
- Performance depends on eigenfunction validation quality
- Computational cost increases with system dimensionality

## Research Gaps
- Application to real ocean control problems
- Extension to partial observations
- Integration with machine learning for eigenfunction discovery
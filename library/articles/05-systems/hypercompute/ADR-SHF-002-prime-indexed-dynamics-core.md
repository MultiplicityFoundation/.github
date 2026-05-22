---
title: 'ADR-SHF-002: Prime-Indexed Dynamics Core'
slug: adr-shf-002-prime-indexed-dynamics-core
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 05-systems/hypercompute/ADR-SHF-002-prime-indexed-dynamics-core.md
  last_synced: '2026-03-20T17:17:17.976209Z'
---

# ADR-SHF-002: Prime-Indexed Dynamics Core

> **Status**: Proposed  
> **Date**: 2026-03-13  
> **Authors**: Phase Mirror Research/Tooling Team  
> **Related Sources**: [Semantic_Hypercomputational_Field.json](./Semantic_Hypercomputational_Field.json), [Hypercomputational_Number_Field.json](./Hypercomputational_Number_Field.json)

---

## Problem Statement

Multiple dynamic equations are presented without a minimal executable core, making comparative validation difficult.

## Decision

Define a minimal prime-indexed dynamics core as the baseline executable model for simulation and testing.

## Decision Details

1. Select a minimal equation set required for baseline evolution and stability checks.
2. Specify parameter ranges and assumptions as explicit constraints.
3. Require deterministic numerical integration settings and seed policy.

## Consequences

### Positive

- Establishes a single baseline for experiments.
- Improves reproducibility and comparison quality.

### Negative

- Reduces immediate flexibility for exploratory variants.

## Alternatives Considered

### Alternative A

Run all published equations in parallel as first-class baselines.

Rejection reason: too costly and too ambiguous for acceptance gating.

### Alternative B

Defer baseline selection until hardware prototyping.

Rejection reason: delays software validation and evidence quality.

## Acceptance Criteria

- [ ] Baseline equation set is documented with symbol references to ADR-SHF-001.
- [ ] Fixed-seed simulation reproduces same metrics across two environments.
- [ ] Parameter constraint violations fail with explicit diagnostics.

## Evidence Artifacts

- Baseline simulator spec.
- Reproducibility logs and metric snapshots.

## Open Questions

- Which baseline metrics are mandatory: convergence, stability margin, or attractor consistency?

## References

- [ADR-SHF-001](./ADR-SHF-001-semantic-ontology-and-sheaf-contract.md)
- [ADR Plan](./ADR-PLAN-Semantic-Hypercomputational-Number-Field.md)

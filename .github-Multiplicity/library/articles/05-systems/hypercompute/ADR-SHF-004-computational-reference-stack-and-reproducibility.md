---
title: 'ADR-SHF-004: Computational Reference Stack and Reproducibility'
slug: adr-shf-004-computational-reference-stack-and-reproducibility
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 05-systems/hypercompute/ADR-SHF-004-computational-reference-stack-and-reproducibility.md
  last_synced: '2026-03-20T17:17:17.962431Z'
---

# ADR-SHF-004: Computational Reference Stack and Reproducibility

> **Status**: Proposed  
> **Date**: 2026-03-13  
> **Authors**: Phase Mirror Research/Tooling Team  
> **Related Sources**: [Hypercomputational_Number_Field.json](./Hypercomputational_Number_Field.json), [Semantic_Hypercomputational_Field.json](./Semantic_Hypercomputational_Field.json)

---

## Problem Statement

Claims span multiple toolchains and runtimes, but there is no standardized reference stack for reproducible execution.

## Decision

Adopt a reference computational stack and mandatory reproducibility manifest for ADR-SHF experiments.

## Decision Details

1. Define approved runtime matrix (language versions, core libraries, environment metadata).
2. Require fixed seeds, deterministic flags, and artifact hashing.
3. Require one-command rerun instructions for baseline experiments.

## Consequences

### Positive

- Improves auditability of computational claims.
- Reduces "works on my machine" drift.

### Negative

- Adds setup overhead for exploratory notebooks.

## Alternatives Considered

### Alternative A

Allow per-experiment environment flexibility without standard manifest.

Rejection reason: weak reproducibility.

### Alternative B

Standardize only at publication time.

Rejection reason: too late to catch drift during development.

## Acceptance Criteria

- [ ] Reference stack document exists in docs/hypercompute.
- [ ] Reproducibility manifest exists for each accepted experiment.
- [ ] Clean-environment rerun reproduces baseline metrics within declared tolerance.

## Evidence Artifacts

- Environment lock files or manifests.
- Reproducibility run logs.

## Open Questions

- What tolerance policy is acceptable for floating-point variance across hardware?

## References

- [ADR-SHF-002](./ADR-SHF-002-prime-indexed-dynamics-core.md)
- [ADR Plan](./ADR-PLAN-Semantic-Hypercomputational-Number-Field.md)

---
title: 'ADR-SHF-001: Semantic Ontology and Sheaf Contract'
slug: adr-shf-001-semantic-ontology-and-sheaf-contract
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 05-systems/hypercompute/ADR-SHF-001-semantic-ontology-and-sheaf-contract.md
  last_synced: '2026-03-20T17:17:17.937566Z'
---

# ADR-SHF-001: Semantic Ontology and Sheaf Contract

> **Status**: Proposed  
> **Date**: 2026-03-13  
> **Authors**: Phase Mirror Research/Tooling Team  
> **Related Sources**: [Semantic_Hypercomputational_Field.json](./Semantic_Hypercomputational_Field.json), [Hypercomputational_Number_Field.json](./Hypercomputational_Number_Field.json)

---

## Problem Statement

Key terms are used across documents with shifting meanings, making implementation inconsistent and validation ambiguous.

## Decision

Define a canonical ontology and sheaf-language contract used by all subsequent ADR-SHF files.

## Decision Details

1. Canonical symbol registry must exist for core terms and operators.
2. Each symbol must include type, domain, units (if applicable), and allowed aliases.
3. Terms marked speculative must be explicitly tagged and separated from operational terms.

## Consequences

### Positive

- Reduces semantic drift.
- Enables deterministic interpretation in code and tests.

### Negative

- Requires upfront editorial harmonization across existing documents.

## Alternatives Considered

### Alternative A

Keep freeform terminology and reconcile during implementation.

Rejection reason: expensive and error-prone at validation time.

### Alternative B

Use only informal glossary prose.

Rejection reason: not machine-actionable.

## Acceptance Criteria

- [ ] Canonical glossary file published in docs/hypercompute.
- [ ] Every downstream ADR references glossary identifiers.
- [ ] Ambiguous terms have deprecation notes or aliases.

## Evidence Artifacts

- `glossary.schema.json` and `glossary.v1.json`.
- Glossary changelog.
- Cross-reference report from ADR-SHF-002..006.

## Open Questions

- Which symbols require dimensional units vs pure symbolic domain tags?

## References

- [ADR Plan](./ADR-PLAN-Semantic-Hypercomputational-Number-Field.md)
- [Glossary Schema](./glossary.schema.json)
- [Glossary Draft v1](./glossary.v1.json)

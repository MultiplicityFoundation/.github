---
title: SHF Gate Report Template (ADR-SHF-005)
slug: shf-gate-report-template-adr-shf-005
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 05-systems/hypercompute/gate-report-template.md
  last_synced: '2026-03-20T17:17:17.947529Z'
---

# SHF Gate Report Template (ADR-SHF-005)

Use this template to produce acceptance-ready gate reports for Semantic Hypercomputational ADR decisions.

## Report Metadata

- Report ID: `SHF-GATE-YYYYMMDD-<slug>`
- ADR Scope: `ADR-SHF-00X`
- Reviewer(s):
- Date:
- Source docs in scope:

## Gate Context

- Gate Name: `Definition Freeze | Dynamics Baseline | Semantic Validator | Reproducibility | Evidence Integrity | Responsible Hardware Translation`
- Trigger reason:
- Decision deadline:

## Tier Checklist (ADR-SHF-005)

### Tier S: Semantic Consistency and Contract Conformance

- [ ] Ontology terms resolve to glossary identifiers.
- [ ] Schema/contract validation passes for all scope artifacts.
- [ ] Morphism/transition rules produce no unresolved semantic violations.

Evidence links:
-

### Tier N: Numerical Determinism and Stability

- [ ] Fixed-seed runs reproduce baseline metrics.
- [ ] Stability tests pass declared thresholds.
- [ ] Numerical violations are classified and triaged.

Evidence links:
-

### Tier E: Empirical and Replication Evidence

- [ ] Comparative benchmark artifacts are present.
- [ ] External rerun or independent replication status is declared.
- [ ] Variance and limitations are documented.

Evidence links:
-

## Claim Mapping Table

| Claim ID | Source | Required Tiers | Evidence IDs | Status (`tested | partially tested | open`) | Notes |
|---|---|---|---|---|---|
| SHF-C001 | | S | | | |
| SHF-C002 | | S,N | | | |

## Test and Artifact Index

| Evidence ID | Type (`log | metric | report | schema | benchmark`) | Path | Repro command | Hash/Version |
|---|---|---|---|---|
| E-001 | | | | |
| E-002 | | | | |

## Validation Outcomes

- Total claims evaluated:
- Claims `tested`:
- Claims `partially tested`:
- Claims `open`:
- Blocking failures:

## Risks and Exceptions

- Risk items:
- Exception requests:
- Expiration date for exceptions:

## Gate Decision

- Decision: `PASS | HOLD | FAIL`
- Rationale:
- Required follow-up actions:

## Sign-Off

- Technical reviewer:
- Governance reviewer:
- Date:

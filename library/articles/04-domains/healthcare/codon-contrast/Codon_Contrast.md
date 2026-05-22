---
slug: codon-contrast
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 04-domains/healthcare/codon-contrast/Codon_Contrast.md
  last_synced: '2026-03-20T17:17:18.822270Z'
---

Codon-Contrast: Deterministic Codon Diffs with Walsh–Hadamard
         Biophysical Contrasts and Fast Flow Metrics
                                               Your Name

                                          December 18, 2025


                                                Abstract
         This report specifies and validates a production-ready framework for exact codon-level
     differencing and biologically interpretable contrast features. Sequences are encoded under
     a fixed lexicographic mapping over {A, C, G, T }3 with frame = 0 and strand normalized to
     “+”. Edits are sparse substitutions with optional positions; content deltas are captured as a
     64-dimensional integer vector ∆h. Biophysical structure is summarized via a 6-bit mapping
     [GC1, P U R1, GC2, P U R2, GC3, P U R3] and an in-place length-64 Walsh–Hadamard transform
     after a fixed bit-order permutation; coefficients are L1 -normalized to yield scale-free contrasts
     (GC1, PUR1, GC2, PUR2, GC3, PUR3 and selected interactions). Substitution flows are
     quantified by transition ratio (A↔G, C↔T), GC bias per move, wobble-transition fraction, and
     flow entropy.
         Correctness is validated by FWHT orthonormality, permutation round-trip, single-coefficient
     dominance, and an integration test (AAA→ACA and AAC→ACC) that yields GC2 = +0.125
     with other contrasts ≈ 0 and flow metrics transition_ratio = 0, wobble = 0, GC_bias = 1.0,
     entropy = ln 2. Performance on commodity Linux: FWHT ≈ 165 µs per call; fast flow analysis
     ≈ 3.2 ms per 10k substitutions (∼ 10× speedup vs. naive). The implementation exposes a
     compact API, JSON-safe serialization, and CI-stable tests.
         Limits: not a fitness model; codon table, frame, and strand must be fixed; indels are slated
     for a normalized extension; real-dataset predictive lift over GC3-only is UNPROVEN pending
     benchmarking with ≥ 5% absolute accuracy gain as the Go/No-Go gate.

Keywords: codon diffs; Walsh–Hadamard transform; GC bias; transitions/transversions; prove-
nance; ∆h.




                                                     1

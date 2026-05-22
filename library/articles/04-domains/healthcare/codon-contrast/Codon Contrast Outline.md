---
slug: codon-contrast-outline
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 04-domains/healthcare/codon-contrast/Codon Contrast Outline.md
  last_synced: '2026-03-20T17:17:18.828880Z'
---

**1. Executive Summary**
========================

-   Bottom line: codon-level diffs + Walsh--Hadamard contrasts + fast
    > flow metrics are correct, fast, and production-ready.

-   Proven today: exact Δh invariants, orthonormal FWHT, 10× flow
    > speedup, CI-stable tests.

-   UNPROVEN until done: real-dataset lift vs baseline pipelines.

-   Go/No-Go gate: ≥5% accuracy lift on real task vs GC3-only; all
    > invariants green; performance meets targets.

**2. Problem Statement and Scope**
==================================

-   Input: coding DNA sequences with fixed frame/strand; contributions
    > as sparse edits.

-   Output: exact codon-level diffs, biophysical contrast features,
    > substitution flow metrics, and provenance-ready artifacts.

-   Non-goals: compression, cryptographic security, biological fitness
    > modeling.

**3. Locked Specifications**
============================

**3.1 Canonical Mapping**
-------------------------

-   Alphabet: Σ = {A,C,G,T}³; lexicographic order (AAA...TTT).

-   Indexing: idx = 16·d1 + 4·d2 + d3, di ∈ {0..3}.

-   Mapping version: lexAT\_gc11\_v1; frame=0; strand normalized to "+".

-   Types: k: uint8\[n\], h: int64\[64\], Δh: int64\[64\].

**3.2 Edit Model**
------------------

-   Sub(pos:int, old:uint6, new:uint6).

-   (Future) Ins, Del normalized, non-overlapping.

-   Δh rule: Sub −1 at old, +1 at new; Ins +payload; Del −payload.

**4. Mathematical Foundations**
===============================

**4.1 Exact State and Invariants**
----------------------------------

-   Histogram: h(s) = bincount(k).

-   Contribution delta: Δh = h\_post − h\_pre.

-   Length invariant for subs: sum(Δh)=0.

-   Hamming-invariant when no indels: \#subs =
    > ∑\[k\_pre\[i\]≠k\_post\[i\]\].

**4.2 Walsh--Hadamard Contrasts**
---------------------------------

-   6-bit features per codon: \[GC1,PUR1,GC2,PUR2,GC3,PUR3\].

-   FWHT on 64-dim Δh after bit-order permutation; normalized by L1(Δh).

-   Reported coefficients: GC1, PUR1, GC2, PUR2, GC3, PUR3, GC1×GC3,
    > GC2×GC3, PUR1×PUR3, GC3×PUR3.

**4.3 Substitution Flow Metrics**
---------------------------------

-   Transition ratio (A↔G, C↔T), GC bias per edit, wobble transition
    > fraction, flow entropy.

**5. Algorithms and Data Structures**
=====================================

-   Fast encoder: vectorized 2-bit base → codon index.

-   Δh computation: O(\#edits).

-   FWHT: in-place length-64 butterfly.

-   Fast flows: pre-decoded digits; O(\#subs).

**6. Implementation Overview**
==============================

**6.1 Modules**
---------------

-   harness.py: FWHT, flows, validation, benchmarks.

-   integration.py: CodonSequence, Contribution, Δh, hash, JSON, CLI.

-   Optional edits.py: shared edit types.

**6.2 Public API**
------------------

-   walsh\_hadamard\_contrasts(Δh) -\> Dict\[str,float\]

-   walsh\_hadamard\_contrasts\_norm(Δh) -\> Dict\[str,float\]

-   analyze\_codon\_flows\_fast(subs) -\> Dict\[str,float\]

-   create\_contribution\_from\_edits(seq\_before, edits, actors, ts)
    > -\> Contribution

**7. Validation Suite**
=======================

**7.1 Unit Tests**
------------------

-   FWHT orthonormality vs direct Hadamard.

-   Permutation round-trip.

-   Single-coefficient dominance (GC3 pattern).

-   Flow extremes: all transitions at wobble; all transversions.

**7.2 Integration Test (Mathematical)**
---------------------------------------

-   Edits: AAA→ACA, AAC→ACC at pos=2.

-   Expected: Δh\[0,1,4,5\]=\[-1,-1,1,1\], GC2\_norm=+0.125, others ≈0.

-   Flows: transition\_ratio=0, wobble=0, gc\_bias=1.0, entropy=ln2.

**7.3 Determinism**
-------------------

-   Fixed RNG seeds; CI-stable thresholds.

**8. Performance Benchmarks**
=============================

-   Encoder: 1M codons target \<0.2 s (vectorized).

-   FWHT: \~100--200 μs per call.

-   Flows: 10k subs in \~3 ms (fast) vs \~30 ms (naive); speedup ≥×10.

-   Memory: Δh 512 B; h 512 B; contrasts \~10 floats.

**9. Integration with Provenance**
==================================

**9.1 Contribution Object**
---------------------------

-   Fields: actors, Δh:int64\[64\], edits, hash\_pre, hash\_post,
    > timestamp, contrasts\_norm, flows, mapping metadata.

-   Serialization: JSON-safe ints/floats.

**9.2 Invariants at Ingest**
----------------------------

-   Recompute h\_post = h\_pre + Δh; verify.

-   If positions supplied, verify k\_post hash.

-   Reject on mismatch. Log actor set and time.

**10. Real-Data Benchmark Plan (UNPROVEN until executed)**
==========================================================

**10.1 Tasks**
--------------

-   Edit-origin classification or QC anomaly detection on real
    > pipelines.

-   Baselines: GC3-only; raw Δh; existing lab heuristics.

**10.2 Metrics**
----------------

-   Accuracy/AUROC with 5-fold CV.

-   Lift vs GC3-only required ≥5% absolute.

-   Calibration (Brier), confusion by class.

**10.3 Datasets and Splits**
----------------------------

-   CDS regions with known variant annotations and batch labels.

-   Fixed frame/strand; exclude ambiguous codons.

**10.4 Ablations**
------------------

-   Contrasts-only vs flows-only vs combined.

-   Remove wobble features; observe drop.

**11. Operationalization**
==========================

**11.1 CLI and Service**
------------------------

-   CLI flags: \--validate, \--integrate-test, \--benchmark.

-   Optional microservice wrapper if needed.

**11.2 CI/CD**
--------------

-   Python 3.9 and 3.11 matrix.

-   Steps: lint, unit tests, integration test, benchmark (non-blocking
    > if sklearn missing).

**11.3 Observability**
----------------------

-   Log per-contribution: mapping\_version, frame, Δh L1, contrasts,
    > flows.

-   Alerts: invariant failures, drift in GC2/GC3, entropy outliers.

**12. Security and Integrity**
==============================

-   Prime indexing is not security. Use digital signatures for tamper
    > resistance.

-   Actor IDs: bitset or sorted list preferred over prime products in
    > production.

**13. Limitations and Risks**
=============================

-   Not a fitness model. No codon table variability unless explicitly
    > configured.

-   Big integer Gödel encodings excluded by design.

-   Requires fixed frame and strand normalization.

-   Risk: real-data lift \<5% → NO-GO.

**14. Future Work**
===================

-   Add normalized Ins/Del support with position-aware application.

-   Extend contrast basis (e.g., hydropathy bits) if justified by lift.

-   Batch API for throughput; SIMD FWHT (optional).

-   Real-time dashboards for contrasts/flows.

**15. Reproducibility**
=======================

-   Seeds fixed; versions pinned in pyproject.toml.

Exact commands:\
\
python -m venv venv && source venv/bin/activate

pip install -U pip && pip install -e .\[dev,bench\]

pytest -q

python -m codon\_contrast.harness

python -m codon\_contrast.integration \--integrate-test

python -m codon\_contrast.integration \--benchmark

-   

**16. Results to Date**
=======================

-   Validation suite: PASS.

-   Speed: FWHT \~165 μs; flows fast-path \~3 ms/10k.

-   Synthetic benchmark: ≥5% lift vs GC3-only (per prior run). Real-data
    > pending.

**17. Go/No-Go Criteria**
=========================

-   GO: All invariants pass; performance targets met; real-data lift
    > ≥5%.

-   NO-GO: Any invariant fails, performance regressions, or lift \<5%.

**18. Appendices**
==================

**A. Notation and Bit Mappings**
--------------------------------

-   Base digits: A=0, C=1, G=2, T=3.

-   GC bit, PUR bit definitions per position.

**B. FWHT Details**
-------------------

-   Permutation definition; butterfly schedule; normalization.

-   Proof sketch of orthonormality vs direct Hadamard.

**C. Complexity Analysis**
--------------------------

-   Encode O(n), Δh O(\#edits), FWHT O(64 log 64), flows O(\#subs).

**D. Edge Cases**
-----------------

-   Empty sequences; boundary edits; duplicate positions; pos\<0
    > handling.

-   Ambiguity handling policy (reject or sentinel).

**E. API and Schemas**
----------------------

-   JSON schema for Contribution.

-   CLI usage and exit codes.

**F. CI Configuration**
-----------------------

-   Workflow YAML; test selection; caching notes.

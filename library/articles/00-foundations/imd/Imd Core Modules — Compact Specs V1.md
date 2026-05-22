---
slug: imd-core-modules-compact-specs-v1
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "00-foundations/imd/Imd Core Modules \u2014 Compact Specs V1.md"
  last_synced: '2026-03-20T17:17:22.412980Z'
---

IMD Core Modules — Compact Specs v1.0
Compact, implementation-ready specs for the remaining IMD engines. Conforms to global contracts in
“IMD Engines — Contracts v1.1”.




Langlands Prism (Integration Layer)
Purpose: Bind safety (ACE) and structure (PETC) to learning and control; orchestrate routing, budgets, and
certification flow.
I/O: (xt , ϕt , mt , Mt∧ , policyt ) → (At , bt , smax , rt ) .
Hooks: reads Archivum sector weights M ∧ (T , p) ; compiles policy to CSL; forwards smax from PQH/ST
proxies.
Contracts: pipeline invariants (deterministic order; idempotent on identical inputs); budget conservation;
route stability under small changes.
Certificates: KKT for ACE step; ledger conservation; commutation of route+projection on active set.
Tests: replay determinism; budget and route monotonicity under policy homotopy.




Moonshine Operator (Speculative→Certified Controller)
Purpose: Zeta/automorphic-weighted controller with spectral certificates; pairs with SCN block.
I/O: features ϕt and weights wt → control signal ut ∈ Rk .
Hooks: consumes Ramanujan bounds and gap Δt from PQH; passes slope caps to ACE; logs to Archivum.
Contracts: bounded gain schedule; budgeted scalarization; unitary or orthogonal mixing in SCN.
Certificates: Ramanujan proxy; small-gain ∥G∥∞ ∥K∥∞ < 1 ; Lipschitz envelope LSCN = 1 .
Tests: step/impulse robustness; margin retention under noise; zero-overspend.




SPASC (Prime-Structured Attention + Certificates)
Purpose: Masked attention with prime structure and spectral certificates (slope, gap).
I/O: (ϕt , mt ) → at , masks mt+1 updated by Ihara sieve and ST/Frobenius diagnostics.
Hooks: consumes ST deviation bands and Ihara gaps; exports SlopeUB and mask to ACE/PETC.
Contracts: prime-typed masking; monotone SlopeUB tightening until stop; unitary internal blocks when
certified.
Certificates: Sato–Tate deviation DT within band; Cheeger-type gap bound; Lipschitz from block spectra.
Tests: mask monotonicity; correlation of proxy gaps with SCN eigen-gaps; halt on no-improvement.




                                                     1
PIRTM (Runtime / State Backbone)
Purpose: State update and online checks; substrate for Watchdog/OMEGA.
I/O: Tt+1 = F + KTt ; exposes ∥Tt+1 − Tt ∥2 , spectra, and counters.
Hooks: emits features for risk Rt ; writes state hashes to Archivum.
Contracts: bounded update per tick; versioned ops; deterministic RNG.
Certificates: contraction or bounded growth under configured norms; ledger match.
Tests: perturbation injections; replay equality; latency within budget.




Automorphic Learning (∞/CSL Training Spec)
Purpose: Training regime embedding invariances, prereg, and certified projection.
I/O: losses (task + invariance + prereg) → updates; ACE projection in-loop.
Hooks: uses CSL compiler; exports KKT witnesses; aligns with Prism routing.
Contracts: convex projection step; explicit tolerance τ ; stable learning-rate schedule.
Certificates: KKT satisfaction; Lipschitz envelope on updates; budget adherence.
Tests: certificate pass-rate ≥ 99% ; no-flap under policy changes.




Alpha Function (Unified Special-Function Kernel)
Purpose: Provide certified special-function transforms aligned with PQH/ACE/PETC.
I/O: inputs z , primes p → kernel features α(z; p) in normalized units.
Hooks: feeds PETC and PQH; exports numerical stability flags to Prism.
Contracts: bounded conditioning; unit-consistent outputs; deterministic eval.
Certificates: interval error bounds; monotonicity or convexity where specified.
Tests: stress on extreme z, p ; reproducible to machine epsilon.




ACE/SCN (Arithmetic Spectral Control Network)
Purpose: Exact Hecke operators + Spectral Control Network with unitary blocks; Weyl-based gap
certificates.
I/O: (ϕt , wt ) → ut .
Hooks: uses PQH eigen-structure; enforced by ACE slope cap; audited by Archivum.
Contracts: unitary cores; bounded slope; certified composition with Moonshine.
Certificates: Weyl-gap lower bound; small-gain closure.
Tests: frequency response bounded; certification completeness.




                                                       2
PGM–MPS (Multiplicity Backbone)
Purpose: Multiplicity functor and sector weights for routing and stability.
                                                                     ^ (T , p) .
I/O: maps operators to integer ledgers and normalized sector weights M
                                            ^ for routing; ACE gates by sector.
Hooks: Archivum writes ledgers; Prism reads M
                           ^ = 1 ; integer integrity.
Contracts: conservation ∑p M
Certificates: stability gates per sector; ledger proofs.
Tests: conservation invariant; adversarial ledger edits rejected.




Π‑kernel (Factorized Projector Kernel)
Purpose: Per-atom proximal projector with SlopeUB aggregation; stabilizes attention and control.
I/O: atoms {ai } → proximal updates; aggregated projector Π .
Hooks: used by PQH and ACE; exports SlopeUB to SPASC/Prism.
Contracts: monotone objective decrease; one-step nonexpansiveness.
Certificates: Lyapunov descent; small-gain compatibility.
Tests: per-iteration decrease; rollback safe when tolerance violated.



Status: Aligned with global contracts; ready to integrate into builds and tests.




                                                       3

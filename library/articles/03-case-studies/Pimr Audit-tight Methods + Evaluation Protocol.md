---
slug: pimr-audit-tight-methods-evaluation-protocol
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Pimr Audit-tight Methods + Evaluation Protocol.md
  last_synced: '2026-03-20T17:17:20.758517Z'
---

PIMR Audit-Tight Methods + Evaluation Protocol
This document formalizes the latest protocol developments for Prime-Indexed Multi-Resolution (PIMR)
architectures in NLP long-context settings. It is written as an audit-ready specification (not a results
section). Any later empirical claims must comply with denominators, masking rules, and acceptance tests
defined below.




0. Scope and positioning
     • Goal: Isolate whether prime arithmetic content (beyond multiscale mixing) improves stability and
       out-of-distribution (OOD) performance.
     • Non-goal: Claiming literal Langlands correspondences or physics validation. Any speculative
       extensions remain quarantined until core acceptance tests pass.
     • Primary endpoints: (i) instability rate and (ii) OOD performance.




1. Model instantiation (operators, weights, cost)

1.1 Backbone and state

Let Xt ∈ RL×d be the hidden sequence state (length L, width d) at recursion/refinement step t. A PIMR
block is applied T refinement steps per forward pass (or unrolled across segments for streaming).


1.2 Indexed operator family {Ap } with deterministic span ladder

Let m denote the target number of indexed operators (e.g., m ∈ {16, 32, 64}). Let P≤P = {p1 < ⋯ <
pm } be the first m primes (equivalently P = pm ). Report m and P .

Define a deterministic span ladder covering [smin , smax ]:

                                                       (0)
                       ρ = (smax /smin )1/(m−1) ,     sk = min(smax , ⌊smin ρk−1 ⌋) .

Enforce strictly increasing spans:


                                     sk = min(smax , max(sk , sk−1 + 1)) for k ≥ 2.
                           (0)                                (0)
                    s1 = s1 ,

Define span-associated operator Apk (typed, implementable):


                                 Apk (X) = LN(X + Attnsk (X)) + MLP(⋅),

where Attnsk is causal attention restricted to the last sk tokens.




                                                      1
Span diagnostics (mandatory): - Distinct-span fraction: ∣{sk }∣/m. - Saturation incidence: #{k : sk =
smax }.

1.3 Weights and optional top-K gating

Simplex-constrained weights:

                                        exp(−β ϕ(p; θ))
                           wp (θ) =                        ,    wp ≥ 0, ∑ wp = 1.
                                      ∑q≤P exp(−β ϕ(q; θ))                  p

If top-K gating is used, define selected set S and report: - K , selection rule, and excluded mass 1 −
∑p∈S wp .

1.4 Computational cost reporting

Cost scales with m (or K if gated). Report m, P , effective K , and excluded mass.




2. Controlled score families (numerical safety) — 3×2 factorial
A factorial design tests: score family (3 levels) × curvature regularization (on/off).


2.1 Score-family factor (3 levels)

Use n as the label input to ϕ(⋅) (either primes pk or B3 composites ck ).


      • S1 Linear log-label: ϕ(n) = a log n + b (learn a, b).


      • S2 Euler-motif label score: ϕ(n) = clip(−ℜ log(1 − αn−s ), [ℓ, u]), with constraints ∣α∣ < 1,
          ℜ(s) > 0, and u ≥ 10.

      • S3 Null (frozen noise): Sample ϕk iid
                                          ∼ Uniform[−1, 1] once per run (seeded + logged) and freeze
          for the entire training/evaluation.


Clipping bounds [ℓ, u] and temperature β must be declared.


2.2 Curvature-regularization factor (2 levels)

Optional curvature penalty on ordered weights wk :

                                                m−1
                                           λ ∑ (wk+1 − 2wk + wk−1 )2 .
                                                k=2

Declare λ (including λ = 0 for off).




                                                       2
2.3 Factorial attribution (analysis plan)

Primary endpoints are analyzed via a two-factor model with interaction: - main effects: score family,
curvature regularization - interaction: score family × regularization


Secondary metrics are analyzed under FDR control.




3. Stability: enforcement + metrics

3.1 Enforcement mechanism (choose ≥1)

     • E1: spectral normalization on linear projections
     • E2: Jacobian penalty (e.g., Hutchinson trace estimator)
     • E3: contractive blocks when available

3.2 Jacobian spectral proxy (standardized)

Report Jacobian spectral proxy summaries:


                                            L = ∥∇X F(X)∥2

estimated via one-step power iteration on minibatches. Report median and 95th percentile across
batches.


3.3 Hard instability events (primary stability metric)

Record an instability event if any occurs: 1. NaN/Inf in activations or loss 2. Hidden-state norm blowup:
∥Xt ∥2 > τX 3. Loss blowup: loss > τℓ or spike > τΔ

Report rates: - events per 10k training updates - events per 1k eval tokens


3.4 Soft update magnitude (anti-overcontraction)

                                                  ∥Xt+1 − Xt ∥2
                                        U = E[                  ].
                                                   ∥Xt ∥2 + ϵ



4. Baselines and ablations
     • B0: unconstrained recursion (no mixture)
     • B1: dyadic spans (2k )
     • B2: random spans (fixed per run)

4.1 B3 (strong, distribution-matched composites)

Replace primes {pk } with distinct composite integers {ck } such that ordered logs match log ck ≈ log pk .




                                                      3
Deterministic construction: - For each k , choose ck as the nearest composite integer to pk (search
±1, ±2, …; break ties by choosing the smaller). - Enforce distinctness by skipping composites already
used. - Use the same span ladder {sk } indexed by k , identical architecture/params, and the same score-
family formulas with n = p replaced by n = c.


B3 diagnostics (mandatory): - maxk ∣ log ck − log pk ∣ - mean ∣ log ck − log pk ∣


Optional parity control: repeat B3 with nearest odd composite via the same outward-search rule restricted
to odd composites.


4.2 B4 (uniform weights)

Identical to PIMR (same A, spans, enforcement), but fix wk ≡ 1/m.




5. Tasks, metrics, and acceptance tests

5.1 Tasks

     • SYN-MS (synthetic, prime-neutral): specified in Appendix A
     • REAL-LC: declare dataset/version + preprocessing; include an OOD split protocol

5.2 Metrics

Primary endpoints: 1. instability rate (Section 3.3) 2. OOD performance (task-specific)


Secondary: - in-distribution performance - U (Section 3.4) - Jacobian proxy (Section 3.2) - interpretability:
Jaccard top-K , Spearman(full w ), EMD(sorted w )


5.3 Acceptance tests (pass/fail)

     • AT1 (stability): PIMR vs B3 improves instability by ≥ abs a OR rel r , while maintaining U ≥ Umin
       and performance degradation ≤ δ .
     • AT2 (OOD): OOD effect ≥ d0 and ≥ 1 SE vs B1/B2/B3/B4, without worse instability.
     • AT3 (signature): cross-seed Jaccard ≥ J0 , Spearman ≥ ρ0 , EMD ≤ w0 ; cross-task Spearman ≥ ρtask .

Cross-task definition: reproducibility is computed on the ordered weight vector (wk )m
                                                                                     k=1 with matched m
and identical span-ladder construction across tasks.


5.4 Multiplicity and endpoint policy

     • Holm–Bonferroni for primary comparisons (PIMR vs B3 and vs B4 on primary endpoints)
     • FDR for secondary analyses




                                                       4
6. Reporting, masking, and power/SESOI

6.1 Minimum denominators

      • ≥ 10 independent seeds per condition per task
      • Mask claims if completed seeds < 8

6.2 Required logs

      • m, P , span ladder {sk } + diagnostics (distinct-span fraction, saturation incidence)
      • if gated: K , excluded mass
      • full wk distributions (not just top-K )
      • compute budget (tokens, wall-clock, FLOPs estimate), hardware
      • stability enforcement choice(s) and Jacobian proxy summaries
      • B3 composite diagnostics (mean/max log mismatch)

6.3 SESOI and power reporting (audit defense)

Pre-register smallest effect sizes of interest (SESOI) for AT1/AT2 and report achieved CI widths; report per-
factor effect sizes for factorial main effects and interaction.




7. Speculative extensions quarantine
All physics-facing or “cosmic” extensions are confined to a Non-validated Speculation appendix and are
gated on passing AT1–AT3.




Appendix A: SYN-MS Generator Spec (Prime-
Neutral)
Generate sequences of length L ∼ 104 –105 . Vocabulary: keys Ki , values Vi , delimiters, brackets.


      • Choose segment lengths from scale set S (geometric: 64, 128, 256, …; no primes).
      • Within each segment: 1) introduce key–value pairs, 2) query keys after variable delays, 3) embed
        nested bracket constraints for long-range consistency.
      • OOD split: increase delays/nesting and shift the tail of S .
      • Splits: 80/10/10; declare generator seed + parameters.

Metrics: retrieval accuracy + bracket validity (+ perplexity if LM).




                                                         5
Appendix B: Fastest path to validation (high-signal
causal test)
1) SYN-MS first: run the 3×2 factorial PIMR conditions and compare against B3(composites) and
B4(uniform) (optionally B0). 2) If Euler beats composite-matched B3 on primary endpoints, proceed to
REAL-LC; otherwise reframe to “multiscale mixtures” and quarantine arithmetic claims. 3) REAL-LC: evaluate
OOD robustness and cross-task signature (AT3) under identical m and span-ladder construction.




                                                    6

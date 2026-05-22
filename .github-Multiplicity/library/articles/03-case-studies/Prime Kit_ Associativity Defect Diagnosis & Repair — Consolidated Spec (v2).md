---
slug: prime-kit-associativity-defect-diagnosis-repair-consolidated-spec-v2
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "03-case-studies/Prime Kit_ Associativity Defect Diagnosis & Repair \u2014\
    \ Consolidated Spec (v2).md"
  last_synced: '2026-03-20T17:17:20.618326Z'
---

PrimeKit: Associativity Defect Diagnosis & Repair
— Consolidated Spec (v2)
This document compiles the developments from PrimeKit v0 → v0.1 → v2 into a single, falsifiable, runnable
research/engineering spec.




1. Philosophy in one line
Learn a prime basis and lawful composition operators; measure associativity defects; apply minimal,
costed augmentations that improve ternary generalization and reduce defect significance—or else
report a menu-relative closure defect as a scientific result.


Key slogans:


     • Lawful composition: operators are admissible by design + enforced by tests.
     • Closure diagnostics: associator is the diagnostic; repair actions are constrained and falsifiable.
     • Irreducibility is okay: “persistent associator under the menu” is evidence, not failure.




2. System overview
PrimeKit is organized into four interacting layers:


2.1 Representation layer (Prime Dictionary Learner)

     • Learn a parts-based, nonnegative basis P ∈ Rm×K
                                                   ≥0  and sparse activations a(x) ∈ RK
                                                                                      ≥0 .
     • Enforce identifiability and stability via gauge fixing:
     • column normalization of P
     • deterministic column ordering (e.g., by explained mass)
     • sparsity penalties on a
     • carrier / “no-new-direction” checks
     • extra_prime knob: increment K only when defects demand it and it passes costed veto.

2.2 Composition layer (Prime-space Composition Operators)

Provide a library of admissible operators ⊗α : Z × Z → Z (where Z is the latent cone or its extension).


Baseline operator families:


     • LRS (linear receptor sum): u ⊗ v = s(u + v)
     • DN (divisive normalization): u ⊗ v = 1+γ(u+v)
                                              u+v
                                                     (coordinatewise)
     • operator_mixing: convex mixtures of admissible operators




                                                         1
Admissibility gates (configurable):


      • cone-closure (if operating in a cone)
      • continuity + empirical Lipschitz/contractivity bounds
      • optional: endpoint identity, monotonicity (domain-specific)

2.3 Diagnostics layer (Associator Spectroscopy)

      • Evaluate associativity on ternaries by measuring the associator.
      • Quantify defect geometry (low-rank / high-rank / spiky structure).
      • Calibrate noise and produce a significance statistic and/or p-value.

2.4 Repair layer (Augmentation Controller)

      • A controller proposes a discrete set of augmentations, evaluates them against a veto rule, and
        commits only the best candidate.
      • Augmentations are explicitly costed (MDL-ish bits, degrees of freedom, and/or runtime cost).

Augmentation menu (canonical):


      • operator_mixing
      • context_1d (state/context-dependent operator parameters)
      • sparse_interaction (bounded bilinear/sparse correction)
      • extra_prime (increase K )
      • netting toggle (group-completion / extended cone)




3. Core diagnostic object: the associator defect tensor

3.1 Associator on ternaries

Given latent states ui , vj , wk ∈ Z , a readout R : Z → Y , and a metric d on Y :


$$ A_{ijk} = d\big(R((u_i \otimes v_j) \otimes w_k),\; R(u_i \otimes (v_j \otimes w_k))\big). $$


3.2 Repeats and heteroscedasticity

PrimeKit v2 promotes repeat-aware defects:

                  (r)
      • collect Aijk for repeats r = 1..R
                                ˉijk and variance σ
      • compute per-triple mean A                   2
                                                  ^ijk

This separates:


      • within-triple measurement/realization noise
      • across-triple structural variation
      • across-seed/training stochasticity (optional replicate mode)




                                                         2
3.3 James–Stein shrinkage for variance stabilization (v2)

Per-entry variance estimates can be noisy for small R. We shrink:


$$ \tilde\sigma^2_{ijk} = (1-\lambda)\hat\sigma^2_{ijk} + \lambda\, \sigma^2_{\text{pooled}}. $$


3.4 Weighted global test statistic (v2)

Use inverse-variance weighting:


$$ S = \frac{\sum_{ijk} w_{ijk}\, \bar A_{ijk}}{\sqrt{\sum_{ijk} w_{ijk}}}, \quad w_{ijk} = \frac{1}
{\tilde\sigma^2_{ijk}+\epsilon}. $$


This is a “global defect” statistic with good power when defects are diffuse.


3.5 Defect geometry summaries

   ˉ, compute:
On A


     • Frobenius norm ∥Aˉ∥F
                        ˉ∣/(E∣Aˉ∣ + ϵ)
     • spike score max ∣A
                                                         ˉ ∈ RI×(JK)
     • low-rank energy profile via SVD on the flattening A
                                  ˉ − Aˉr ∥2 /∥Aˉ∥2 ≤ η
     • rank-hat: smallest r s.t. ∥A        F      F




4. Empirical null: wild bootstrap for S (v2)
Analytic nulls are fragile under heteroscedasticity and dependence.


Wild bootstrap procedure:

               ˉ and residuals e(r) = A(r) − Aˉ.
    1. Compute A
    2. Sample Rademacher signs sr ∈ {−1, +1}.
                           ˉ∗ = 1 ∑ sr e(r) (centered at 0).
    3. Form bootstrap mean A    R  r
                                          ~2.
                        ˉ∗ using the same σ
    4. Compute S ∗ from A
    5. p-value (upper tail): p = Pr(S ∗ ≥ Sobs ) with add-one smoothing.

Interpretation:


     • If p is small, observed defect is unlikely under “noise-only” residual structure.
     • This supports menu-relative defect claims with fewer distributional assumptions.




                                                       3
5. Repair ladder: from geometry to candidate generation
PrimeKit’s stance:


      • Geometry should inform which candidates to consider, not dictate a rigid order.
      • Selection should be optimization-based over actual measured improvements.

Geometry-informed heuristics for proposing candidates:


      • Low-rank defect → propose operator_mixing, then context_1d
      • High-rank residual → include extra_prime early
      • Spiky / structured defects → propose sparse_interaction
      • Domain licenses cancellation → propose netting toggle

But: all candidates (and some short combos) are evaluated and scored.




6. Controller: optimization-based selection with rollback (v2)

6.1 Proposal interface

A proposal is a callable that:


     1. modifies model state (operator/dictionary/augment params)
     2. trains briefly and evaluates
     3. returns improvements (ΔL, ΔS), cost, and a checkpoint token

6.2 Compound score + costs

PrimeKit v2 uses a normalized tradeoff score:


$$ \text{score} = \alpha\frac{\Delta L}{\delta_L} + (1-\alpha)\frac{\Delta S}{\delta_S} - \gamma\,\text{cost}. $$


Acceptance:


      • default: require ΔL ≥ 0 and ΔS ≥ 0
      • optional early-training grace: allow one step with strong ΔS even if ΔL is small

Rollback discipline:


      • Evaluate all candidates from the same baseline snapshot.
      • Commit only the best candidate by restoring its returned checkpoint token.




                                                        4
6.3 Composing augmentations

CandidateFactory can propose short combos (length 2) with joint cost:


      • operator_mixing + sparse_interaction
      • context_1d + sparse_interaction
      • mixing + context (if lawful)




7. “Law cards” and LCC join (conceptual integration)
PrimeKit is designed to plug into a Law-Card / LCC (Lawful Closure Composition) stack:


      • A law card specifies admissible composition along certain subspaces/aspects.
      • A join (⋈ₖ) composes states only when permitted by the law card.
      • Closure diagnostics test whether a macro operation exists that makes Φ sufficient for bracketing.

Even if a full LCC join engine isn’t implemented in v2 scaffolding, the interface is respected:


      • composition operators are modular
      • closure tests are attached to admissibility + associator outcomes




8. CI and invariants: executable philosophy
Make conceptual constraints enforceable:


8.1 Always-on (typical)

      • cone closure (for nonnegative latent cones)
      • empirical Lipschitz/contractivity bounds
      • deterministic gauge fixing checks (dictionary normalization and ordering)

8.2 Profiled (domain-dependent)

      • endpoint identity u ⊗ 0 ≈ u
      • monotonicity under coordinate order

8.3 Statistical calibration checks
                            ~ 2 under resampling
      • repeat stability of σ
      • bootstrap null sanity: p-values roughly uniform on associative synthetic data




                                                        5
9. Benchmarks and validation plan

9.1 Synthetic benchmarks (minimum viable)

Four generators:


    1. associative (noise-only)
    2. low-rank non-associativity
    3. high-rank non-associativity
    4. spiky non-associativity

Expected controller behavior:


     • associative → stop
     • low-rank → mixing/context wins on score-per-cost
     • high-rank → extra_prime (or combo including it) wins
     • spiky → sparse_interaction wins

9.2 Real-data workflow

    1. train representation + binary composition
    2. evaluate ternary associator with repeats
    3. calibrate significance using repeat-aware variance + bootstrap
    4. run controller; commit minimal augmentations only if they improve ternary generalization and
       reduce defect
    5. if persistent: report menu-relative defect (rank profile + p-values)

Deliverables:


     • closure certificates Δ ≤ ϵ
     • augmentation bits/complexity
     • law-card sparsity and stability




10. Implementation artifacts produced so far

PrimeKit v0

     • Minimal lawful operators (LRS/DN), associator, basic controller, CI tests.

PrimeKit v0.1

     • Controller evaluates all candidates (no rigid priority queue)
     • compound normalized score (tradeoff between ΔL and ΔS )
     • law profiles: optional endpoint identity and monotonicity checks




                                                       6
PrimeKit v2 scaffolding

      • heteroscedastic defect denoising + James–Stein variance shrinkage
      • inverse-variance weighted S
      • wild bootstrap null + p-value
      • candidate factory with combo proposals
      • controller with rollback + commit tokens

Local artifacts:


      • primekit_v0.zip
      • primekit_v0_1.zip
      • primekit_v2_scaffold.zip




11. What to do next (v2.1 suggestions)
High-leverage improvements:


     1. Add max-type / BH-FDR tests for localized defects (complements global weighted-S).
     2. Use studentized bootstrap for better calibration under heteroscedasticity.
     3. Make cost multi-objective: (MDL bits, parameters, runtime latency).
     4. Add a “law-card harness” to automatically test operator admissibility under domain profiles.




External references (selected)
Associativity, associators, and composition

      • Saunders Mac Lane, Categories for the Working Mathematician, 2nd ed., 1998. (Associators, monoidal
        categories.)
      • J. D. Stasheff, “Homotopy associativity of H-spaces,” Transactions of the AMS, 1963. (Associahedra /
        associativity structure.)

Nonnegative / parts-based representations

      • D. D. Lee and H. S. Seung, “Learning the parts of objects by non-negative matrix factorization,”
        Nature, 1999.
      • P. O. Hoyer, “Non-negative matrix factorization with sparseness constraints,” JMLR, 2004.
      • D. Donoho and V. Stodden, “When does non-negative matrix factorization give a correct
        decomposition into parts?” 2004. (Identifiability conditions.)

Divisive normalization

      • D. J. Heeger, “Normalization of cell responses in cat striate cortex,” Visual Neuroscience, 1992.




                                                        7
     • M. Carandini and D. J. Heeger, “Normalization as a canonical neural computation,” Nature Reviews
       Neuroscience, 2012.

Statistical calibration and bootstrap

     • B. Efron and R. Tibshirani, An Introduction to the Bootstrap, 1993.
     • C. F. J. Wu, “Jackknife, bootstrap and other resampling methods in regression analysis,” Annals of
       Statistics, 1986. (Wild/bootstrap ideas.)
     • E. Mammen, “Bootstrap and wild bootstrap for high dimensional linear models,” 1993. (Wild
       bootstrap foundations.)

Shrinkage estimation

     • W. James and C. Stein, “Estimation with quadratic loss,” Proceedings of the Fourth Berkeley Symposium,
       1961. (James–Stein shrinkage.)

Multiple testing control

     • Y. Benjamini and Y. Hochberg, “Controlling the false discovery rate,” JRSS-B, 1995.

MDL and information bottleneck

     • J. Rissanen, “Modeling by shortest data description,” Automatica, 1978. (MDL principle.)
     • N. Tishby, F. C. Pereira, and W. Bialek, “The information bottleneck method,” 1999.

Low-rank approximation and stability

     • C. Eckart and G. Young, “The approximation of one matrix by another of lower rank,” Psychometrika,
       1936.
     • P. H. Schönemann, “A generalized solution of the orthogonal Procrustes problem,” 1966. (Dictionary
       alignment diagnostics.)

Contractive mappings

     • S. Banach, “Sur les opérations dans les ensembles abstraits…” 1922. (Contraction mapping principle;
       useful as a theoretical lens for admissible operators.)

Citizen Gardens © 2025 CC-NC-ND 4.0




                                                      8

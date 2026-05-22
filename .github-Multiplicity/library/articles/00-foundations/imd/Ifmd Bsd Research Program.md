---
slug: ifmd-bsd-research-program
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 00-foundations/imd/Ifmd Bsd Research Program.md
  last_synced: '2026-03-20T17:17:22.229619Z'
---

IFMD Research Program for the Birch–Swinnerton-
Dyer (BSD) Problem
0) Mission & Outcomes
Mission. Build a certified, reproducible pipeline that (i) computes lawful local/global invariants of elliptic
curves, (ii) estimates analytic rank and key BSD quantities with numerical guarantees, and (iii) tests
prime‑structured learning ideas without violating standard number‑theoretic definitions.


Primary outcomes (12–16 weeks). - A small, audited library ifmd-bsd with three layers: data → estimators
→ certificates. - Benchmarks on 1,000–10,000 curves comparing (a) analytic rank estimates, (b) Sato–Tate
conformity of normalized traces, (c) Tamagawa & conductor checks. - A preregistered evaluation report with
pass/fail gates and failure analyses.




1) Scientific Objectives & Hypotheses
    1. Rank estimation (H1): A transparent, prime‑feature estimator can predict the analytic rank class
       r ∈ {0, 1, ≥ 2} with >90% accuracy on held‑out curves, while never changing definitions of ap ,
       L(E, s) , or local factors.
    2. Sato–Tate profiling (H2): For non‑CM curves, the empirical distribution of ap /   p matches Sato–Tate
       within a stated Wasserstein bound after ACE stabilization.
    3. Numerical certification (H3): A projection‑first operator (ACE) yields interval‑validated evaluations
       of L(E, 1) and L(r) (E, 1) that are reproducible across machines.




2) IFMD Architecture Mapping
     • ACE=CSP (Safety): Projection‑first numerical operators; enforce Lipschitz < 1 via spectral radius
       bounds; use interval/ball arithmetic for certified values.
     • PETC=TPC (Structure): Lawful per‑prime features: ap = p + 1 − #E(Fp ) , reduction types,
       Tamagawa cp , local root numbers; never encode ap as prime powers.
     • PGF=PGM (Learning): Lightweight estimators (logistic, isotonic regression, small decision trees) that
       map PETC features to rank class; no deep nets in baseline.
     • Langlands Prism (Integration): Interface aggregating local data → global invariants (conductor,
       sign, functional equation) with clear provenance.
     • Moonshine Operator (Spec→Cert): Sandbox for speculative heuristics (e.g., feature transforms)
       that must pass ACE gates to influence outputs.
     • SPASC (Modeling): Prime‑attention map for analysis only (feature importance, saliency); never used
       to redefine arithmetic objects.
     • Low‑Complexity Attractor: Simple constants/priors (e.g., parity, conductor size) used as stabilizers
       in training/selection.




                                                      1
3) Work Packages (WPs)

WP0. Reproducibility & Data Ops (Week 1–2)

    • Tasks:
    • Create ifmd-bsd repo; lock Python env; enable deterministic BLAS; add arb /interval backend or
      mpmath +interval wrapper.
    • Data schema for curves: minimal model, conductor, j‑invariant, CM flag, known rank (if available),
      Tamagawa factors, torsion.
    • Acceptance: make test runs in <5 min on 100 curves; seed‑fixed outputs identical across Linux/
     Mac.

WP1. Lawful Local Features (Week 1–4)

    • Tasks:
    • Implement point_count(E, p) and ap(E, p) = p + 1 − N_p for good primes; reduction
      type + Tamagawa at bad primes.
    • Normalize traces tp = ap/√p ; assemble per‑prime feature vectors up to bound p ≤ P_max .
    • Acceptance: Matches independent references on a 200‑curve audit set; Hasse bound checks ∣ap ∣ ≤
     2√p auto‑verified; bad‑prime handling unit‑tested.

WP2. Global Invariants & L‑function (Week 3–6)

    • Tasks:
    • Implement/consolidate: conductor, sign (root number), functional equation scaffolding.
    • Numerical evaluation near s = 1 : modular‑symbol or approximate functional equation path;
     support L(E, 1) , L(k) (E, 1) for k = 0, 1, 2 .
    • Acceptance: Reproduces tabulated values within stated intervals; includes interval certificates
      (radius < 10−8 baseline).

WP3. Estimators (PGF/PGM) (Week 5–8)

    • Tasks:
    • Baseline classifier r^ ∈ {0, 1, ≥ 2} using PETC features: parity, small‑prime traces, conductor size,
      torsion hints.
    • Calibrate with isotonic regression; report well‑calibrated probabilities.
    • Acceptance: >90% accuracy on held‑out with honest CIs; ablations show which prime features
      matter.

WP4. ACE Certification (Week 6–9)

    • Tasks:
    • Define operator T for numerical continuation/Newton near s = 1 ; compute spectral norm estimate
      via power iteration.
    • Projection: If ρ(T ) > γ < 1 not met, shrink step or widen intervals; log certificate (rho_est,
     gamma, pass) .
    • Acceptance: No divergence in 10k evals; certificates attached to each L or L′ query.




                                                       2
WP5. SPASC Analysis & Moonshine Sandbox (Week 8–11)

      • Tasks:
      • Investigate speculative transforms of PETC features (e.g., short Dirichlet‑convolution windows).
      • Promote only if (i) improves validation metrics and (ii) passes ACE and ablation stability.
      • Acceptance: At least one promoted transform with documented gain and proof it preserves
        arithmetic definitions.

WP6. Evaluation & Report (Week 10–16)

      • Tasks:
      • Pre‑registered tests: rank confusion matrix; Sato–Tate distance; conductor/Tamagawa checks;
        timing/complexity.
      • Failure taxonomy and fixes; release v1.0 dataset + code + report.
      • Acceptance: Report with all figures, tables, and replication script; archive on a persistent DOI.




4) Metrics & Gates
      • Rank Class Accuracy: overall and by conductor deciles; calibration curves; parity consistency rate.
      • Sato–Tate Distance: Wasserstein/KS between empirical ap / p and ST law for non‑CM curves.
      • Certification Coverage: fraction of L and L′ evaluations with valid ACE certificates.
      • Numerical Stability: max interval radius; failure/timeout rates.

Hard gates (must pass): 1. All local data satisfy Hasse bounds and correct bad‑prime factors. 2. No code
path redefines ap or violates standard L -factor definitions. 3. ACE certificate attached to every reported L
or derivative value.




5) Data, Software & Reproducibility
      • Data: Minimal models; conductor/Tamagawa; known CM flag; prime features up to P_max
        (configurable).
      • Stack: Python; exact/integer arithmetic via gmpy2 ; high‑precision/interval via mpmath + interval
       wrapper or arb ; optional C++ kernels later.
      • Artifacts:
      • /data/curves.parquet (curve‑level); /data/prime_features.parquet (long table:
       curve×prime).
      • /models/ (pickled estimators + calibration); /certs/ (JSON with ACE logs and intervals).
      • Repro: Makefile , lockfile, seeds; continuous benchmarks on a fixed instance.




6) Risk & Mitigation
      • R1: Numerical fragility near s = 1 . Mitigation: ball arithmetic, ACE projection, redundancy via two
       independent evaluators.




                                                       3
      • R2: Data leakage between train/test (curves with near‑duplicate invariants). Mitigation: split by
        conductor ranges and isogeny classes.
      • R3: Overfitting speculative features. Mitigation: Moonshine sandbox with promotion only after
        preregistered tests.




7) Deliverables & Timeline (Gantt‑style, weeks)
      • W1–2: WP0 kickoff, schema, smoke tests.
      • W1–4: WP1 local features (rolling audits weekly).
      • W3–6: WP2 global invariants & L‑eval.
      • W5–8: WP3 estimators + calibration.
      • W6–9: WP4 ACE certification.
      • W8–11: WP5 SPASC/Moonshine experiments.
      • W10–16: WP6 evaluation, write‑up, release.




8) Minimal Working Example (MWE)
For clarity only; production code will be modular.



  # Pseudocode sketch — lawful a_p and simple rank classifier
  from fractions import Fraction
  from math import isqrt, sqrt

  def point_count(E, p):
      # E: tuple (a1,a2,a3,a4,a6) minimal model, good prime p only
      a1,a2,a3,a4,a6 = E
      N = 1 # point at infinity
      for x in range(p):
          # y^2 + a1*x*y + a3*y = x^3 + a2*x*x + a4*x + a6 (mod p)
          rhs = (x**3 + a2*x*x + a4*x + a6) % p
            # Count solutions y to y^2 + (a1*x + a3)*y - rhs ≡ 0 (mod p)
            # Solve quadratic in y over F_p by discriminant test
            b = (a1*x + a3) % p
            D = (b*b + 4*rhs) % p
            # Legendre symbol via Euler criterion (p odd here)
            if D == 0:
                 N += 1
            else:
                 ls = pow(D, (p-1)//2, p)
                 if ls == 1:
                     N += 2
        return N




                                                       4
  def ap(E, p):
      Np = point_count(E, p)
      return p + 1 - Np

  # Features for primes up to P_max


  def features(E, primes):
      vec = []
      for p in primes:
           a = ap(E, p)
           assert abs(a) <= 2*int(sqrt(p)) + 1              # Hasse sanity (loose)
           vec.append((p, a / sqrt(p)))
       return vec




9) Authorship, Roles, & Review
     • PI: Oversees arithmetic correctness and evaluation design.
     • Numerics Lead: ACE/intervals, performance.
     • Data Lead: Curves/feature pipeline, audits.
     • ML Lead: Estimators, calibration, SPASC analyses.
     • Repro Lead: CI, packaging, artifact publication.




10) Pre‑registration Checklist (to file before WP3)
     • Train/test split policy (by conductor & isogeny class), metrics, gates.
     • What counts as promotion from Moonshine sandbox to certified stack.
     • Fixed compute budget and termination criteria for all experiments.




Closing Note

This program preserves strict arithmetic correctness while giving room to explore prime‑structured
learning. All speculative ideas must pass ACE gates and cannot redefine standard objects. The result is a
BSD‑aligned, certifiable research pipeline ready for real benchmarks.




                                                     5

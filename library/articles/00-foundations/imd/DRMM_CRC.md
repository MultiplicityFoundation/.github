---
slug: drmm-crc
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 00-foundations/imd/DRMM_CRC.md
  last_synced: '2026-03-20T17:17:22.258906Z'
---

                          DRMM × CSC:
 Certified Spectral Control of Prime-Scripted Operators (Finite-P )

                        Dr. Ryan Van Gelder, Luis Morató de Dalmases,
                                      Tyler Van Osdol

                                              October 1, 2025


Motivation & Long-Term Vision
We aim to develop a certifiable control theory for prime-scripted spectral operators that (i) produces
verifiable, finite-dimensional results now; (ii) scales to structurally faithful surrogates of operators
from analytic number theory (Hecke/trace, automorphic Laplacians, moonshine blocks); and (iii)
yields lawfulness-aware design principles—prime gating and recursion budgets—that survive model
variation. Success is not a theorem like RH; it is a reliable pipeline that (1) constructs operators
with arithmetic provenance, (2) moves specific gaps/slopes under explicit budgets, and (3) quantifies
when DRMM-style constraints do or do not confer real robustness beyond ordinary regularization.
                                                  Abstract
         We present a finite-P , certified control scheme for prime-scripted operators that constrains
      the Certified Spectral Control (CSC) design by DRMM (Dynamic Recursive Meta-Mathematics)
      lawfulness budgets and introduces a small-gain DRMM recursion. The plant is UP (ω) =
      XP + C(ω; w) on ℓ2 (P), where XP encodes arithmetic symmetry and C(ω; w) is a Bohr–prime
      multiplier driven by weights w. We provide convex design surrogates (gap lower bound; slope
      upper bound), a pinning & slope-control theorem with explicit constants, a lawful-controller
      program, a minimal P =5 sanity check with verification & falsifiability, and a bounded recursion
      with a small-gain certificate. We claim finite-P certified control and a clear scaling path—not
      asymptotic problem resolution.


1     Plant, Sector, and Design Objectives
Indexing and space.        Let P = {p1 , . . . , pP } be the first P primes and work on H = ℓ2 (P).

Plant.   The controlled operator is
                        UP (ω) = XP + C(ω; w),              C(ω; w) =         wp Bp (ω),                   (1)
                                                                        X

                                                                        p∈P

with XP self-adjoint, each channel Bp (ω) self-adjoint, and w ∈ RP the controller. Assume uniform
bounds ∥Bp (ω)∥ ≤ bp and ∥∂ω Bp (ω)∥ ≤ b′p , so

                                 |wp | bp =: ∥w∥1,b ,                             |wp | b′p =: ∥w∥1,b′ .   (2)
                            X                                             X
             ∥C(ω; w)∥ ≤                                ∥∂ω C(ω; w)∥ ≤
                             p                                                p


1.1   Lawful sector (DRMM) — constraints with motivation
We constrain design and evolution to a lawful subset Hlawful ⊆ H via three budgets.

                                                        1
(a) Prime gating (Λm ): scale separation by prime size. For α in a small grid A (e.g.,
{0.5, 0.7, 1.0, 1.3}) and κ ∈ R, penalize deviations from a power-law template
                                  (α)
                                RΛ (w, κ) =                wp − κp−α ≤ τ.                            (3)
                                                 X

                                                 p∈P

We keep convexity by optimizing (w, κ) for each fixed α ∈ A and selecting α by validation.

(b) Ξ-budget: memory/recursion gain. A recursion operator Ξ (introduced in Section 6)
satisfies ∥Ξ∥ ≤ β. The pilot uses β = 0; later, β > 0 is certified by a small-gain margin.

(c) Commutator stability (M ): channel geometry control.                       Bound non-abelian channel
interference by
                                   ∥[Bp , Bq ]∥ ≤ γ,                                                 (4)
                                 X

                                           p<q

implemented via epigraph variables θpq ≥ ∥[Bp , Bq ]∥ with            p<q θpq ≤ γ (convex).
                                                                  P


Design surrogates. Let λ1 (ω) ≤ · · · ≤ λP (ω) be the eigenvalues of UP (ω). If XP has a simple
eigenvalue λk separated by δS > 0, Weyl’s inequality yields the gap lower bound

                                        gapk (w) := δS − 2∥w∥1,b ,                                   (5)

and differentiability of Bp yields the slope upper bound

                                             dλk
                                                 ≤ ∥w∥1,b′ .                                         (6)
                                             dω

2     Pilot Theorem: Pinning, Gap, Slope, and Subspace Control
Assumptions A. (i) XP self-adjoint with a simple λk such that min(λk+1 −λk , λk −λk−1 ) ≥ δS > 0.
(ii) ∥C(ω; w)∥ ≤ r < δS /2 for all ω. (iii) ∂ω C exists with ∥∂ω C∥ ≤ s.

Theorem 1 (Pinning & Slope Control). Under Assumptions A:

    (i) Pinning & gap: For all ω, there is a simple eigenvalue λk (ω) with |λk (ω) − λk | ≤ r and
        gapk (ω) ≥ δS − 2r.

 (ii) Slope: With a smooth eigen-branch, |dλk /dω| ≤ s.

(iii) Subspace stability: If Pk and Pk (ω) denote the rank-1 spectral projectors at λk and λk (ω),
                                             r
      then (Davis–Kahan) ∥Pk (ω) − Pk ∥ ≤        .
                                          δS − r
Corollary 2 (Certified design via convex surrogates). If ∥w∥1,b ≤ r < δS /2 and ∥w∥1,b′ ≤ s, any
optimizer of the controller program in Section C certifies the above bounds; a single eigentracking
sweep verifies realized values.




                                                       2
3     Controller: Convex Program with Lawfulness Budgets
Maximizing gapk (w) is equivalent to minimizing ∥w∥1,b subject to budgets:

                          min     ∥w∥1,b
                          w,κ

                           s.t.   ∥w∥1,b ≤ r,     ∥w∥1,b′ ≤ s,                                   (7)
                                                (α)
                                  ∃ α ∈ A : RΛ (w, κ) ≤ τ,
                                                      θpq ≤ γ, θpq ≥ ∥[Bp , Bq ]∥,
                                                X
                                  ∥Ξ∥ ≤ β,
                                                p<q

                                  w ∈ RP , κ ∈ R.

Solver: projected/proximal gradient for each fixed α ∈ A; select α by validation (e.g., realized gap
at matched budgets). Warm start wp = κp−α .


4     Verification & Falsifiability
Eigensolver. One Lanczos sweep across a grid Ω = {ωj } around the design point; use Woodbury
updates when channels are low rank.


                         Table 1: Certified vs. realized metrics at ωj ∈ Ω.

                ωj   gapk (w) (cert)       gapk (ωj ) (real)   s (cap)    |∆λk /∆ω| (real)
                ω1          ...                  ...              ...            ...
                ω2          ...                  ...              ...            ...

Certified vs realized table.

Null controls. Generate N null controllers wnull by (i) shuffling prime lags in Bp , or (ii) random-
izing signs, while matching ∥w∥1,b and RΛ . Plot a histogram of gap improvements and report a
p-value for our controller relative to nulls.


5     Zeroth-Order Sanity Check (P=5) & Scaling Plan
Index set.   P = {2, 3, 5, 7, 11}.

5.1   Base-operator menus (choose one per run)
(H) Hecke-trace truncation (Automorphic-DRMM). XP = q≤Q ρq Tq restricted to ℓ2 (P)
                                                                             P

with symmetrized Hecke-like Tq . Why: arithmetic symmetry; δS measurable and tunable via ρq .

(E) Explicit-formula surrogate (pair-correlation toy). (XP )ij = ψ(log pi ) + ψ(log pj ) −
ψ(log(pi pj )) − µ with smooth ψ. Why: mimics explicit-formula interactions while remaining
bounded/symmetric.



                                                        3
(M) Moonshine block (modular moment matrix). XP = Π⊤ M (τ0 )Π, where M (τ0 ) is a small
covariance of modular coefficients; Π projects to prime indices. Why: direct modular provenance.

House rule.      Justify the chosen XP in two sentences and publish δS .

5.2    Channels and bounds
Rank-1 Bohr–prime multipliers

                       Bp (ω) = up (ω)up (ω)⊤ ,          up (ω)i = cos ω log(ppi + ℓ) ,                (8)
                                                                                      


so ∥Bp ∥ ≤ 1 and ∥∂ω Bp ∥ ≤ b′p (explicit from up ).

5.3    Protocol & outputs
(i) Solve (7) with published (r, s, τ, β, γ, α). (ii) Verify by Lanczos across Ω. (iii) Report: confidence-
band plot and the certified vs. realized table; include null-control histogram and p-value.

5.4    Scaling targets & complexity
Targets: P = 5 (sanity), P = 23 (∼9×), P = 97 (∼19×). Controller: proximal methods with
O(P ) primitives/step (empirically tens of iterations). Eigensweep: Lanczos O(P · m) matvecs
(tens–low hundreds of Krylov steps for P ≤ 100). Success at scale: certified bands remain binding
(non-vacuous) and realized improvements beat nulls for P ∈ {23, 97}.


6     Pilot-Plus: Bounded DRMM Recursion with Small-Gain Cer-
      tificate
Introduce a recursion on Tt :

                       Tt+1 = Tt + ε         Λm Ξ Mp (Tt ),         T0 = XP + C(ω; w),                 (9)
                                       X

                                       p∈P

with ∥Ξ∥ ≤ β and mixer Mp chosen to reduce channel conflict.

Default mixer. Let up denote the channel vector underlying Bp = up u⊤
                                                                    p . Define a Householder
                          ⊤
                      up up
reflector Up := I − 2        and set
                      ∥up ∥2

                            Mp (T ) := Up T Up⊤ − T,             ∥Mp (T )∥ ≤ 2∥T ∥.                   (10)

With mp := 2∥Tt ∥, define the one-step recursion gain

                                              η := ε         Λm β mp .                                (11)
                                                       X

                                                       p∈P

Proposition 3 (Spectral drift control). Suppose Eq. (7) yields margin δS − 2r > 0 and η < δS /8.
Then
                                            η
             ∥Pk (Tt+1 ) − Pk (Tt )∥ ≤             ,  gapk (Tt+1 ) ≥ δS − 2r − 2η.
                                       δS − 2r − η
Over T steps, pinning persists provided T η < δS /4 (triangle inequality/telescoping).

                                                         4
Reporting. Publish (ε, β, Λm ), per-step projector drift, cumulative drift over T , and realized gap
floors vs. certified margins.


7     Reproducibility Checklist & Hyperparameter Protocol
Checklist. Publish P , choice of XP , channel definitions, and (ϕ, µ) or (ρq , Q) as applicable; list
(r, s, τ, β, γ, α); fix seeds; release solver and verification scripts.

7.1   Setting (r, s, τ, β, γ) from data
 1. r = θ δS with θ ∈ [0.2, 0.4]; publish (δS , θ).

 2. s: compute b′p analytically; enforce ∥w∥1,b′ ≤ s with target s ≤ 0.1 δS .

 3. τ : for each α ∈ A, fit κ by least-absolute-deviation; set τ = η          −α with η ∈ {0.02, 0.05}.
                                                                       P
                                                                         pp

 4. β: start at 0; for recursion, choose β so that η < δS /8.

 5. γ: measure     p<q ∥[Bp , Bq ]∥ on the uncontrolled system; set γ to its 25th percentile (conservative
                 P

    geometry).


8     Extension Tracks (Problem-Themed Variants)
Automorphic-DRMM: XP = q≤Q ρq Tq ; test with/without (Λm , Ξ, M ) at matched ∥w∥1,b ,
                                     P

compare realized gap floors and recursion drift. Moonshine-DRMM: modular linear ties among
wp (e.g., by residue classes); test variance reduction of realized slopes without hurting certified
floors. Ablation: remove each budget in turn at fixed ∥w∥1,b and measure whether certification
bands become vacuous or realized performance degrades.


9     What We Claim (and What We Don’t)
We claim certified, finite-P control of targeted eigen-gaps and slopes under explicit operator-norm
budgets and DRMM-lawfulness penalties, plus a scaling study to P ∈ {23, 97}. We do not claim
asymptotic (P → ∞) behavior or resolution of deep conjectures. The contribution is a falsifiable,
reproducible pipeline with ablations demonstrating when DRMM-style constraints provide genuine
advantage.


A     Mini-Glossary
Plant / Controller
     XP is the system; C(ω; w) is the designed control.

Bohr–prime multiplier
    Rank-1/low-rank channel keyed by a prime-phase vector up (ω).

Woodbury updates
   Fast rank-r inverse/solve updates used during verification.




                                                      5
Small-gain
    Recursion gain η kept strictly within the spectral separation margin.

Davis–Kahan / Weyl
    Eigen-projection and eigenvalue perturbation bounds controlling drift and separation.


B     Certified Spectral Control
The interplay between arithmetic structure and spectral phenomena has long been anticipated in
number theory and physics. Here we present a minimal, reproducible framework to control such
spectra with certificates using convex optimization.
    Directly optimizing spectral quantities depending on full eigendecompositions is nonconvex
and costly. We therefore design convex surrogates that bound gaps and slopes from below/above,
enabling tractable controller design with rigorous guarantees.
    Contributions. (i) A plant/controller framework for prime-scripted operators; (ii) certified
                     (LB)  (UB)
convex objectives Jgap , Jslope ; (iii) a pilot pinning
slope theorem for bounded drives; (iv) a P =5 case study showing certified gap modulation and null
controls.
    Outline. Section B.1 defines the plant. Section B.2 proves the pilot theorem. Section C presents
the convex programs. Section D shows P =5 results. Section E discusses scope and limitations.

B.1    Model (Plant): Prime-Scripted Operator
Let PP = {p ∈ P : p ≤ P } and consider UP (ω) = XP + C(ω) acting on ℓ2 (PP ).
Definition 4 (Prime block). For parameters Φ > 0, σ > 0, define
                                                            p                 2
                                                                                   
          (XP )pp = p−1/2 ,    (XP )pq = Φ Re ζ 21 + i log      exp − (log(p/q))
                                                                          2σ 2
                                                                                     ,   p ̸= q.
                                                             q

Definition 5 (Bohr–prime drive). Given weights w ∈ R|PP | , define m(ω; w) = p≤P wp e−iω log p
                                                                                         P

and C(ω; w) by (Cf
                d )(ω) = m(ω; w)fb(ω). We control w under budgets ∥w∥1 ≤ W , ∥w∥2 ≤ W2 .

Remark 6 (Operator norm). We use the operator norm ∥·∥ for Weyl/Kato bounds; Hilbert–Schmidt
norms enter only in optional factorization/regularization.

B.2    Pilot Theorem: Pinning and Slope Bounds
Let S be a set of simple eigenvalues of XP with minimal gap δS > 0 from the rest of the spectrum.
Theorem 7 (Pilot pinning
slope). If C ∈ C 1 (Ω; B) with supω∈Ω ∥C(ω)∥ < δS /2, then for each λi ∈ S there exists a unique C 1
branch λi (ω) such that

                sup λi (ω) − λi ≤ sup ∥C(ω)∥ ,       sup ∂ω λi (ω) ≤ sup ∥∂ω C(ω)∥ .
               ω∈Ω                ω∈Ω                ω∈Ω                ω∈Ω

Moreover, the Riesz projection onto the band S is well-defined for all ω, and the Davis–Kahan
principal angle between invariant subspaces at 0 and ω is at most 2∥C∥/δS .
Sketch. Analytic perturbation for simple eigenvalues (Kato) and Weyl inequality yield the bounds;
subspace stability follows from Davis–Kahan.

                                                 6
Figure 1: Eigenvalue trajectories before (baseline) and after optimization (w∗ ); highlighted target
gap.


                   Figure 2: Optimized prime-lag weights w∗ under ℓ1 /ℓ2 budgets.


C     Controller: Convex Design with Certificates
We design w using convex surrogates that bound the realized objectives.

C.1      Certified lower bound on a target gap
      (0)
Let ∆i      denote gaps of XP on an index set I. Define
                                                 n                              o
                                                         (0)
                           (LB)
                          Jgap  (w) := min max 0, ∆i − 2 sup ∥C(ω; w)∥ .
                                        i∈I                       ω∈Ω

                                                                              (LB)
Since supω ∥C(ω; w)∥ ≤ ∥w∥1 for the multiplier class, maximizing Jgap under ℓ1 /ℓ2 budgets is
convex.

C.2      Certified upper bound on total slope
                                 Z
                  (UB)
                 Jslope (w) :=                             with                     |wp | log p.
                               X                                              X
                                     ∥∂ω C(ω; w)∥ dω,              ∥∂ω C∥ ≤
                               i∈I Ω                                          p≤P

This yields a convex penalty that discourages excessive sensitivity.

C.3      Convex program

                                                         (UB)
                              max        (LB)
                                        Jgap  (w) − λ Jslope (w)
                             w∈R|PP |
                                 s.t.   ∥w∥1 ≤ W, ∥w∥2 ≤ W2 , w ∈ Wphys .

Here Wphys encodes platform constraints (bandwidth, symmetry).


D     Numerical Case Study: P = 5
Setup. P5 = {2, 3, 5, 7, 11}; choose (Φ, σ); budgets (W, W2 ). Target a specific internal gap among
the ordered eigenvalues of XP .

Optimization. Solve the convex program for w∗ (projected gradient, coordinate descent). Report
 (LB)           (UB)
Jgap (w∗ ) and Jslope (w∗ ).

Verification. Perform one eigentracking sweep to compute the realized gap and compare against
the certificate.




                                                     7
                                     Certified LB       Realized      Null (shuffled lags)
                                       (LB)
                   Target gap size    Jgap (w∗ )        ∆realized              ∆null

                   Table 2: Certificate vs. realized gap and null-control outcome.

       Table 3: Prime vs. shuffled delays at P =5. Shuffled entries are means over 64 seeds.

 W     Prime gap    Shuffled gap (mean)       Gap adv.%      Prime corr.         Shuffled corr. (mean)   Corr. adv.%
 0.5     1.411              1.428               +1.2                0.712                  0.409           +74.1
 1.0     1.328              1.349               +1.5                0.712                  0.344           +107.3
 2.0     1.166              1.192               +2.3                0.712                  0.335           +112.6
 4.0     0.798              0.729               −8.6                0.712                  0.360           +97.8


E      Discussion and Outlook
We emphasized methodology: certified convex design and a pilot theorem ensuring spectral stability.
Future work adds state-dependent rank-1 mixing, soft lawfulness penalties, and scaling to larger P
and phase-diagram studies.


Reproducibility
Code and data to be released at: https://example.org/prime-spectral-control.


Acknowledgments

A      Notes on Norm Bounds and Multipliers
Derive supω ∥C(ω; w)∥ ≤ ∥w∥1 and supω ∥∂ω C∥ ≤             p |wp | log p for the convolution multiplier on
                                                        P

L2 .


B      Implementation Details
Optimization uses projected gradient with adaptive step sizes; eigentracking uses Lanczos with
warm starts; crossing detection via sign changes in discrete gap derivatives.


Mathematical Appendix: Explicit Proofs and Operator-Norm Bounds

A      Fourier–Multiplier Bounds for the Temporal Sieve
[Operator norm of C(ω; w)] Let C(ω; w) act on L2 (Rt ) as the Fourier multiplier with symbol
m(ω; w) = p≤P wp e−iω log p . Then for all ω,
          P


                       ∥C(ω; w)∥L2 →L2 = ∥m(·; w)∥L∞ (R) ≤                |wp | = ∥w∥1 .
                                                                    X

                                                                    p≤P




                                                    8
Proof. C is unitary-conjugate to multiplication by m in the frequency domain: Cf
                                                                              d (ω) = m(ω; w)fb(ω).
For multiplication on L2 , the operator norm equals the L∞ norm of the symbol. Since |e−iω log p | = 1,
|m(ω; w)| ≤ p |wp | for all ω, proving the bound.
             P


   [Derivative bound] Assuming w is independent of ω, the weak derivative ∂ω C exists as a
multiplier with symbol ∂ω m(ω; w) = −i p≤P wp (log p)e−iω log p and
                                      P


                        ∥∂ω C(ω; w)∥L2 →L2 = ∥∂ω m(·; w)∥L∞ ≤            |wp | log p.
                                                                    X

                                                                   p≤P

Proof. Differentiate the symbol termwise; take L∞ as in Section A.


B     Pilot Pinning and Slope: Full Proof
We restate Theorem 7 and give a complete argument.
    [Pilot pinning & slope, restated] Let XP be self-adjoint on ℓ2 (PP ) with a set S of simple eigenvalues
{λi }i∈S separated from (XP ) \ S by δS > 0. Let C ∈ C 1 (Ω; B) and supω∈Ω ∥C(ω)∥ < δS /2. For
each i ∈ S there exists a unique C 1 eigenbranch λi (ω) of UP (ω) = XP + C(ω) such that

                 sup |λi (ω) − λi | ≤ sup ∥C(ω)∥,        sup ∂ω λi (ω) ≤ sup ∥∂ω C(ω)∥.
                 ω∈Ω                   ω                 ω∈Ω                ω

Moreover the Riesz spectral projection onto S is well-defined for all ω, and the principal angle Θ(ω)
between the invariant subspaces at 0 and ω satisfies sin Θ(ω) ≤ 2∥C∥/δS .

Proof. Existence and uniqueness of branches. By Kato’s analytic perturbation theory for isolated
simple eigenvalues, if ∥C(ω)∥ < δS /2, each λi extends to a unique C 1 branch (indeed analytic in ω
if C is analytic), remaining isolated from the rest of the spectrum.
     Eigenvalue displacement. For each fixed ω, Weyl’s inequality gives |λi (ω) − λi | ≤ ∥C(ω)∥. Taking
supω yields the first bound.
     Slope bound. Differentiate the eigenvalue equation (XP + C(ω))ui (ω) = λi (ω)ui (ω); taking
inner product with ui (ω) and using ∥ui (ω)∥ = 1 yields the Hellmann–Feynman identity ∂ω λi (ω) =
⟨ui (ω), (∂ω C(ω))ui (ω)⟩, hence |∂ω λi (ω)| ≤ ∥∂ω C(ω)∥.
     Subspace stability. Let E(ω) = C(ω) and PS (0), PS (ω) be the Riesz projections onto the bands
at 0, ω. By the Davis–Kahan sinΘ theorem, ∥ sin Θ(ω)∥ ≤ ∥E(ω)∥/dist(S, (XP ) \ S). Since the
minimal gap is δS and we assumed supω ∥E(ω)∥ < δS /2, the claimed bound with factor 2 follows
from standard norm inequalities for projectors.


C     Relative Perturbation Determinants for Sums Across Tensor
      Factors
Definition 8 (Relative perturbation determinant). Let A0 be a closed operator with nonempty
resolvent set; assume K(z) := (A − A0 )(A0 − z)−1 ∈ S2 (Hilbert–Schmidt) for some z. The
2-determinant is
                                                                                       
                 D(z; A|A0 ) := det2 I + K(z) := exp tr log(I + K(z)) − K(z) .
                                                 


It is analytic in z and encodes the discrete spectral shift of A relative to A0 .



                                                     9
Theorem 9 (Factorization up to an entire, nonvanishing prefactor). Let A0 = XP ⊗ ⊗ on ℓ2 (PP ) ⊗
L2 (R) ⊗ Cd . Let
                                  A = A0 + ⊗C⊗     +⊗ ⊗ Ξ.
                                             | {z } | {z }
                                                :=B1     :=B2

Assume that for some z in the resolvent of A0 , Kj (z) := Bj (A0 − z)−1 ∈ S2 (j = 1, 2). Then

                       D(z; A|A0 ) = G(z) det2 (I + K1 (z)) det2 (I + K2 (z)),

where G is entire and nonvanishing.

Sketch. Use the identity (I + K1 + K2 ) = (I + K1 )(I + (I + K1 )−1 K2 ) and the multiplicativity of
det2 up to an analytic, nonzero prefactor that compensates for the tr(K) terms in the definition
of det2 . Since K1 , K2 ∈ S2 , the cross-term (I + K1 )−1 K2 ∈ S2 , and the product formula holds
with G(z) = exp − tr(K1 K2 ) + · · · given by an absolutely convergent series (Plemelj–Smithies).
                                     

Analyticity and nonvanishing follow from standard arguments in trace-ideal determinant theory.

Remark 10. The naive factorization det2 (I −(A0 +B1 +B2 )) = det2 (I −(A0 +B1 )) det2 (I −(A0 +B2 ))
is false in general; Theorem 9 is the correct relative statement.


D     Rank-k Updates, Woodbury, and Eigenvalue Perturbations
[Woodbury for resolvents] Let A = A0 + U V ∗ with U, V : Ck → H and z ∈ ρ(A0 ). Then

          (A − z)−1 = (A0 − z)−1 − (A0 − z)−1 U (Ik + V ∗ (A0 − z)−1 U )−1 V ∗ (A0 − z)−1 .

Proof. Standard Woodbury identity; verify by multiplication.

Proposition 11 (Hoffman–Wielandt/Weyl bounds). Let A be normal and E be a perturbation.
Then
             dist2 ((A + E), (A)) ≤ ∥E∥HS , dist∞ ((A + E), (A)) ≤ ∥E∥.

Proof. Classical inequalities (Hoffman–Wielandt for normal matrices; Weyl for general).


E    Bounds for the State-Dependent Coupling
Recall K(ω) = Re m(ω) (XP Pv + Pv XP ) + Im m(ω) (XP J − JXP ).
   [Operator norms] For any projector Pv and bounded J,

∥K(ω)∥ ≤ | Re m(ω)| ∥XP Pv +Pv XP ∥+| Im m(ω)| ∥[XP , J]∥ ≤ 2| Re m(ω)| ∥XP ∥+2| Im m(ω)| ∥XP ∥ ∥J∥.

Proof. ∥XP Pv + Pv XP ∥ ≤ ∥XP Pv ∥ + ∥Pv XP ∥ ≤ 2∥XP ∥ since ∥Pv ∥ = 1. For the commutator,
∥[XP , J]∥ ≤ ∥XP J∥ + ∥JXP ∥ ≤ 2∥XP ∥ ∥J∥.

Corollary 12 (Smallness condition). If ε supω ∥K(ω)∥ < δS /2, the band S remains isolated for the
active model UP (ω) = XP + C(ω) + εK(ω) and the pilot theorem applies with C ⇝ C + εK.




                                                 10
F      Validity of Certified Surrogates
                                                                              (0)
Proposition 13 (Gap lower bound surrogate). Let ∆i                                  be the i-th internal gap of XP . For
E(ω) = C(ω; w) + εK(ω),
                                   (0)                                                  (0)
                 ∆i (ω) ≥ ∆i − 2∥E(ω)∥                  ⇒         min ∆i (ω) ≥ ∆i − 2 sup ∥E(ω)∥.
                                                                  ω∈Ω                               ω∈Ω

        (LB)
Thus Jgap is a rigorous certificate.
Proof. Apply Weyl’s inequality to the two neighboring eigenvalues defining the gap.

Proposition 14 (Slope upper bound surrogate). For any differentiable branch λi (ω), |∂ω λi (ω)| ≤
∥∂ω E(ω)∥. Hence            Z                     Z
                                              |∂ω λi (ω)| dω ≤
                                    X                               X
                                                                              ∥∂ω E(ω)∥ dω,
                                    i∈I   Ω                         i∈I   Ω

               (UB)
justifying Jslope .
Proof. Hellmann–Feynman as in the pilot theorem, then integrate and sum.


G      Soft Lawfulness and Subspace Stability
Proposition 15 (Davis–Kahan with lawfulness penalty). Let Slaw be the Riesz subspace for the
“lawful band” of XP . Suppose the controller enforces budgets W, W2 and taper (Φ, σ) so that
supω ∥E(ω)∥ ≤ εE and the minimal band gap inside XP satisfies δS > 2εE . Then the invariant
subspace for UP (ω) over the same index set obeys
                                                                εE     2εE
                                              sin Θ(ω) ≤             ≤     .
                                                             δS − εE    δS
Proof. Davis–Kahan in the version for two self-adjoint operators with separated spectra (triangle
inequality on gaps).


H      Two-Level Avoided Crossing Model and Arithmetic Fingerprints
Consider a pair of modes (ψi , ψj ) near resonance; project UP (ω) onto span{ψi , ψj }:
                      (0)
                                                    !
                  λi + δi (ω)    Γij (ω)
    Heff (ω) =                 (0)        ,              Γij (ω) ≈ ε Im m(ω) ⟨ψi , [XP , J]ψj ⟩ + ⟨ψi , C(ω)ψj ⟩.
                    Γij (ω)   λj + δj (ω)
The minimal gap is
                                                                        (0)                   (0)
                            gapmin = 2 min |Γij (ω)|     when        λi + δi (ω) = λj + δj (ω).
                                          ω

If C is diagonal-dominant in the XP -basis, the dominant off-diagonal comes from the commutator
term and
                        gapmin ≈ 2 | Im m(ωmin )|                 ψi (p) ψj (q) Xpq Jqq − Jpp Xpq ,
                                                           X                                              

                                                           p̸=q
                                                                                                                   2   2
which is sparse in (p, q) due to the structure of Xpq . Since Xpq ∝ Re ζ(1/2+i log(p/q)) e−(log(p/q)) /(2σ ) ,
the leading channels (p, q) imprint an arithmetic fingerprint on the crossing.

                                                              11
I     Complexity Summary for the Plant–Controller Loop
    • Controller step (convex). Projection and gradient for w ∈ R|PP | under ℓ1 /ℓ2 budgets: O(P )
      per iteration; evaluation of ∥C∥ and ∥∂ω C∥ uses Section A.

    • Verification step. Lanczos eigentracking across a grid |Ω|: O(|Ω| P 2 ) matvecs with warm
      starts; with rank-k update, Woodbury reduces per-ω work by a low-rank solve O(k 3 ) plus
      O(kP ) matvecs.
                      (LB)       (UB)
    • Certificates. Jgap and Jslope are computed without diagonalization; the realized spectrum is
      computed once per design.


J      Notation and Trace-Ideal Conventions
∥ · ∥ denotes the operator norm unless explicitly marked ∥ · ∥HS . S2 is the Hilbert–Schmidt class; det2
is the Carleman–Fredholm determinant. Davis–Kahan bounds are stated for orthogonal projectors
with the principal-angle norm.


References
 [1] Ryan O. Van Gelder. Dynamic recursive meta-mathematics. Citizen Gardens – The Foundation
     of Multiplicity, Preprint, 2024.

 [2] Ryan O. Van Gelder. The universal multiplicity constant (λm ): Prime-indexed recursive tensor
     mathematics. Citizen Gardens - The Foundation of Multiplicity, 2024. Preprint - PrimeAI
     Enhanced Template.

 [3] Tyler Van Osdol. Dynamic recursive operator. Citizen Gardens – The Foundation of Multiplicity,
     Preprint, 2025.

 [4] Luis Morató de Dalmases. Universal spectral operator. Indepedent Research Initiative, 2025.

 [5] Tosio Kato. Perturbation Theory for Linear Operators. Springer, Berlin, classics in mathematics
     edition, 1995.

 [6] Rajendra Bhatia. Matrix Analysis. Springer, New York, 1997.

 [7] G. W. Stewart and Ji guang Sun. Matrix Perturbation Theory. Academic Press, San Diego,
     1990.

 [8] Chandler Davis and William M. Kahan. The rotation of eigenvectors by a perturbation. III.
     SIAM Journal on Numerical Analysis, 7(1):1–46, 1970.

 [9] Gene H. Golub and Charles F. Van Loan. Matrix Computations. Johns Hopkins University
     Press, Baltimore, 4 edition, 2013.

[10] Lloyd N. Trefethen and David Bau III. Numerical Linear Algebra. SIAM, Philadelphia, 1997.

[11] Cornelius Lanczos. An iteration method for the solution of the eigenvalue problem of linear
     differential and integral operators. Journal of Research of the National Bureau of Standards,
     45:255–282, 1950.


                                                  12
[12] Harold V. Henderson and Shayle R. Searle. On deriving the inverse of a sum of matrices. SIAM
     Review, 23(1):53–60, 1981. Woodbury matrix identity.

[13] Charles A. Desoer and Mathukumalli Vidyasagar. Feedback Systems: Input-Output Properties.
     Academic Press, New York, 1975.

[14] Kemin Zhou, John C. Doyle, and Keith Glover. Robust and Optimal Control. Prentice Hall,
     Upper Saddle River, NJ, 1996.

[15] Stephen Boyd and Lieven Vandenberghe. Convex Optimization. Cambridge University Press,
     Cambridge, 2004.

[16] Neal Parikh and Stephen Boyd. Proximal algorithms. Foundations and Trends in Optimization,
     1(3):127–239, 2014.

[17] Amir Beck and Marc Teboulle. A fast iterative shrinkage-thresholding algorithm for linear
     inverse problems. SIAM Journal on Imaging Sciences, 2(1):183–202, 2009.

[18] Semyon A. Gershgorin. über die abgrenzung der eigenwerte einer matrix. Izvestiya Akademii
     Nauk SSSR, Ser. Fiz.-Mat., 6:749–754, 1931.

[19] Franz Rellich. Perturbation Theory of Eigenvalue Problems. Gordon and Breach, New York,
     1969.

[20] Henryk Iwaniec and Emmanuel Kowalski. Analytic Number Theory, volume 53 of Colloquium
     Publications. American Mathematical Society, Providence, RI, 2004.

[21] Henryk Iwaniec. Spectral Methods of Automorphic Forms. American Mathematical Society,
     Providence, RI, 2 edition, 2002.

[22] Jean-Pierre Serre. A Course in Arithmetic. Springer, New York, 1973.

[23] Hugh L. Montgomery. The pair correlation of zeros of the zeta function. Analytic Number
     Theory, Proc. Sympos. Pure Math., 24:181–193, 1973.

[24] Andrew M. Odlyzko. On the distribution of spacings between zeros of the zeta function.
     Mathematics of Computation, 48(177):273–308, 1987.

[25] Nicholas M. Katz and Peter Sarnak. Random Matrices, Frobenius Eigenvalues, and Monodromy,
     volume 45 of Colloquium Publications. American Mathematical Society, Providence, RI, 1999.

[26] John H. Conway and Simon P. Norton. Monstrous moonshine. Bull. London Math. Soc.,
     11(3):308–339, 1979.

[27] Richard E. Borcherds. Monstrous moonshine and monstrous lie superalgebras. Inventiones
     Mathematicae, 109(2):405–444, 1992.

[28] Richard E. Borcherds. Automorphic forms on Os+2,2 and infinite products. Inventiones
     Mathematicae, 120:161–213, 1998.

[29] Robert P. Langlands. Problems in the theory of automorphic forms. In Lectures in Modern
     Analysis and Applications, III, volume 170 of Lecture Notes in Mathematics, pages 18–61.
     Springer, 1970.


                                               13
[30] Alston S. Householder. Unitary triangularization of a nonsymmetric matrix. Journal of the
     ACM, 5(4):339–342, 1958.

[31] Bradley Efron and Robert Tibshirani. An Introduction to the Bootstrap. Chapman & Hall/CRC,
     New York, 1993.

[32] Hermann Weyl. Das asymptotische verteilungsgesetz der eigenwerte linearer partieller differen-
     tialgleichungen. Mathematische Annalen, 71:441–479, 1912.

[33] Rajendra Bhatia. Positive Definite Matrices. Princeton University Press, Princeton, 2013.

[34] Tosio Kato. On the differentiability of eigenvalues and eigenvectors. Proceedings of the Japan
     Academy, 26:1–7, 1950. See also Kato’s monograph for full development.




                                                14

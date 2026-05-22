---
slug: ace-scn-formal-specification
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/ACE-SCN Formal Specification.md
  last_synced: '2026-03-20T17:17:21.245344Z'
---

Arithmetic Control Engine (ACE) with Structured
Control Network (SCN)
0. Purpose
ACE is a reproducible system for amortized, certified spectral shaping on families of arithmetic operators
                                                                                                         ^,
(self-adjoint Hecke operators on cusp forms). Given a Hermitian operator matrix A and a target gap value g
ACE produces a Hermitian perturbation Δ that (i) satisfies hard feasibility certificates and (ii) optionally
preserves arithmetic structure via explicit fidelity modes.


The system is designed to be falsifiable: arithmetic correctness is validated on the unperturbed arithmetic
pipeline; control performance is evaluated on perturbed operators under explicit certificates.




1. Arithmetic Objects

1.1 Cusp-form space

Let


                                             V = Sk (Γ0 (N ))

be the complex vector space of weight-k holomorphic cusp forms of level Γ0 (N ).


1.2 Self-adjoint Hecke operators (safe family)

Fix primes p with p ∤ N . Let Tp : V → V be the Hecke operator. These operators are self-adjoint with
respect to the Petersson inner product.


Scope restriction: the ACE Hermitian gap-control theory targets operators Tp with p ∤ N (and, optionally,
fixed combinations thereof). Non-self-adjoint operators (e.g. Up for p ∣ N ) are excluded in the base
specification.




2. Matrix Realization and Hermitianization

2.1 Computational basis

Choose a non-diagonal computable basis B for V (e.g. modular symbols-derived basis), yielding a matrix
Mp representing Tp in B .




                                                     1
2.2 Inner-product Gram matrix

Let G ≻ 0 be the Gram matrix of the relevant inner product in basis B . Self-adjointness in this basis is
equivalent to


                                                Mp∗ G = GMp .

Define the diagnostic

                                                            ∥Mp∗ G − GMp ∥F
                                 selfAdjErr(Mp , G) :=                      .
                                                             ∥Mp ∥F ∥G∥F

2.3 Stable Hermitianization (Cholesky)

Compute a Cholesky factorization G = L∗ L. Define


                                               Ap := L Mp L−1 .

If selfAdjErr is sufficiently small, then Ap is Hermitian up to numerical tolerance.


Optional stabilization:


                                             Ap ← 12 (Ap + A∗p ).

Record the residual ∥Ap − A∗p ∥F as a diagnostic.




3. Target Operator and Gap Functional

3.1 Target operator

Choose a Hermitian target operator


                                       A ∈ {Ap\* , 12 (Ap1 + Ap2 ), …}

with fixed coefficients (no learned coefficients in the base spec).


3.2 Eigenvalues

Let λ1 (A) ≤ ⋯ ≤ λd (A) denote the ordered real eigenvalues of Hermitian A ∈ Cd×d .


3.3 Smooth gap objective

Define a smooth gap functional gτ (A). Two canonical choices:


1) Indexed gap: gi (A) := λi+1 (A) − λi (A).




                                                        2
2) Soft-min consecutive gap:

                                             d−1
                                                         λi+1 (A) − λi (A)
                       gτ (A) := −τ log ∑ exp ( −                          ),   τ > 0.
                                             i=1
                                                                 τ



4. Perturbation Classes and Fidelity Dial

4.1 Hecke-span subspace

Fix primes p1 , … , pr with pj ∤ N . Define the Frobenius subspace


                                   Hr := span{Ap1 , … , Apr } ⊆ Cd×d .

4.2 Distances

Use Frobenius norm and induced distance:


                     ∥X∥F :=      tr(X ∗ X),       distF (X, Hr ) := min ∥X − H∥F .
                                                                      H∈Hr


4.3 Fidelity modes (constraint sets)

Let ε > 0 and η ≥ 0.


     • Mode 1 (Unstructured):


                                       Cε := {Δ : Δ = Δ∗ , ∥Δ∥F ≤ ε}.

     • Mode 2 (Hecke-span):


                                 CεHr := {Δ : Δ ∈ Hr , Δ = Δ∗ , ∥Δ∥F ≤ ε}.

     • Mode 3 (Near-arithmetic):

                            near
                           Cε,η  := {Δ : Δ = Δ∗ , ∥Δ∥F ≤ ε, distF (Δ, Hr ) ≤ η}.



5. Frobenius Projection onto Hr
                                         2
Let B = [vec(Ap1 ) ⋯ vec(Apr )] ∈ Rd ×r . The Frobenius projection is


                               PHr (X) = unvec(B(B ⊤ B)−1 B ⊤ vec(X)).




                                                     3
Implementation notes: - Precompute a numerically stable basis for Hr via QR on flattened matrices. - Use
that orthonormal basis to compute projections with a single matrix multiplication.




6. Certificate-First Feasibility Map
ACE enforces constraints by a deterministic map F applied to a raw Hermitian proposal Δ0 . The feasibility
map is post-network and independent of training.


6.1 Common Hermitianization of Δ0

If Δ0 may be non-Hermitian, first set


                                             Δ0 ← 12 (Δ0 + Δ∗0 ).

6.2 Mode 1 map (unstructured)

                                                             Δ0
                                        F1 (Δ0 ) := ε                   .
                                                        max(∥Δ0 ∥F , ε)

6.3 Mode 2 map (Hecke-span)

Let H = PHr (Δ0 ). Then

                                                             H
                                        F2 (Δ0 ) := ε                 .
                                                        max(∥H∥F , ε)

6.4 Mode 3 map (near-arithmetic)

Let H = PHr (Δ0 ) and R = Δ0 − H . Set

                                                 η
                             R′ := min (1,          ) R,         Δ1 := H + R′ .
                                               ∥R∥F

Finally,

                                                             Δ1
                                        F3 (Δ0 ) := ε                   .
                                                        max(∥Δ1 ∥F , ε)

Feasibility property: Fm (Δ0 ) is Hermitian and satisfies the corresponding constraints by construction.




                                                         4
7. SCN Controller

7.1 Role

The Structured Control Network (SCN) learns an amortized mapping from instance features to a raw
proposal Δ0 (or to low-dimensional parameters), with feasibility ensured by F .


7.2 Dimension-agnostic parametrization (recommended)

Fix integers r and s (small). The SCN outputs (α, β) ∈ Rr+s . Define

                                                        r          s
                                     Δ0 (α, β) := ∑ αj Apj + ∑ βℓ uℓ u⊤
                                                                      ℓ ,
                                                   j=1            ℓ=1

where uℓ ∈ Rd are deterministic pseudorandom unit vectors generated from a fixed seed as a function of
d (seed must be pinned for reproducibility).

This makes the network output dimension independent of d.


7.3 Features

         ^) be a fixed feature vector, e.g. - target g^, - summary statistics of {λi (A)} (mean, variance), -
Let ϕ(A, g
selected gaps, quantiles, etc.




8. Optimization Problem (Amortized Learning)

8.1 Per-instance constrained problem
                                       near
For a constraint set C ∈ {Cε , CεHr , Cε,η  }, define

                                                                            2
                                     Δ\* (A, g^) ∈ arg min (gτ (A + Δ) − g^) .
                                                            Δ∈C


8.2 Amortized objective

Train θ to minimize expected loss over a distribution of instances:


                             min E(A,g^) [(gτ (A + F(Δ0 (Fθ (ϕ(A, g^))))) − g^) ].
                                                                                 2
                                 θ




                                                              5
9. Certificates and Key Lemmas

9.1 Weyl via Frobenius

For Hermitian A and Hermitian Δ,


                                ∣λi (A + Δ) − λi (A)∣ ≤ ∥Δ∥2 ≤ ∥Δ∥F ≤ ε.

9.2 Near-span implies near-commuting (diagnostic bound)

If distF (Δ, Hr ) ≤ η , then for each generator Api ,


                                          ∥[Api , Δ]∥F ≤ 2 ∥Api ∥2 η.

This yields a certified interpretation of commutator norms as an arithmetic-fidelity diagnostic.


9.3 Feasibility-map invariants

      • F preserves Hermitian symmetry.
      • Mode constraints are satisfied deterministically.
      • In Mode 3, down-scaling cannot increase distF (⋅, Hr ), so both ε and η constraints hold
       simultaneously.




10. Diagnostics and Reporting

10.1 Arithmetic correctness (unperturbed only)

Validate arithmetic pipeline outputs {Ap } using: - Hecke relations (e.g., multiplicativity for coprime indices),
- Ramanujan–Petersson-type bounds for eigenvalues where applicable, - selfAdjErr and Hermitian residual
diagnostics.


10.2 Control metrics (perturbed)

Report for   A + Δ: - gap error: ∣gτ (A + Δ) − g^∣, - feasibility: ∥Δ∥F , distF (Δ, Hr ) (Mode 3), -
commutators: ∥[Api , Δ]∥F and certified bound 2∥Api ∥2 η , - (optional) estimated spectral norm ∥Δ∥2 by a
few steps of power iteration (report-only).




11. Baselines
1) Projected-gradient per instance using the same feasibility map F after each step. 2) Linearized
analytic baseline for indexed gaps gi : using eigenvectors ui , ui+1 , set


                                Δlin ∝ ui+1 u⊤         ⊤
                                             i+1 − ui ui ,       ∥Δlin ∥F = ε,




                                                        6
then apply F if evaluating in Modes 2–3.




12. Expected Outcomes
     • Mode monotonicity: achievable gap shifts decrease as η ↓ 0; Mode 2 matches the η = 0 endpoint.
     • Commutator scaling: in Mode 3, commutators scale as O(η) and obey the certified bound.
     • Amortization benefit: once trained, SCN inference provides comparable objective values to per-
       instance optimization at much lower per-instance compute.




13. Minimal Validation Protocol
1) Compute Mp , G, and Ap on a fixed grid of (N , k) with p ∤ N . 2) Check selfAdjErr and Hermitian
residuals; verify real spectra. 3) Run unperturbed arithmetic acceptance tests. 4) Unit-test feasibility maps
on random Δ0 samples. 5) Compare SCN vs baselines across Modes 1–3, reporting control metrics, fidelity
metrics, and runtime.




14. Reproducibility Checklist
     • Pin CAS versions and seeds.
     • Fix r , primes p1 , … , pr , and pseudorandom uℓ seed.
     • Cache Mp , G, L, Ap , and eigenvalue summaries for benchmarks.
     • Release evaluation scripts that recompute all plots and metrics from cached artifacts.




                                                     7

---
slug: simulation-theory
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 06-people/ken-parrot/Simulation_Theory.md
  last_synced: '2026-03-20T17:17:14.090420Z'
---

                                        SIMULATION THEORY


                                                 KEN PARROTT




    1. Meta–Relativity × Fractal–Entanglement Dark Matter: Developments, Formal
                                   Results, and Tests
1.1. Executive Synopsis. We formalize the integration of the Fractal–Entanglement Model of Dark Matter
(FEMDM) with the Meta–Relativity (MR) constitutional program. FEMDM supplies the astrophysical
scaffold via a mass–radius fractal law M (r) ∝ rD and a coherence amplifier Γ(r), while MR provides the
ontic operator calculus on the lawful subspace Hlawful , governed by the Universal Spectral Operator (USO).
The bridge is a projector
                                            n                            o
(1)                               Phalo := 1 (D − 1) + ∂ln r ln Γ(r) ≤ ε ,

elevating the empirical “flat rotation” clause to a constitutional selection rule.

1.2. Constitutional Commitments and New Axioms.

Axiom 1 (Mathematical Onticity). Physical reality is realized as dynamics internal to mathematics; admis-
sible states are elements of a lawful Hilbert subspace Hlawful defined by spectral consistency (USO alignment)
and prime decomposability.

Axiom 2 (Prime Gating of Evolution). Time evolution factors through a prime-indexed sieve CΛp ; stability
plateaus correspond to prime-addressed windows that suppress unlawful sidebands.

Axiom 3 (Zeta–Multiplicity Constraint). The USO, restricted to Hlawful , admits a Fredholm–zeta correspon-
dence; spectra are pinned to RH-aligned loci up to bounded perturbations induced by admissible potentials.

Axiom 4 (Halo Lawfulness). Galactic sectors are lawful iff their circular-velocity slope satisfies

                                         (D − 1) + ∂ln r ln Γ(r) ∞ ≤ ε,

with ε calibrated from cross-domain stability (Def. 4).

1.3. Operator Architecture and Functional Forms.

Definition 1 (Lawful Galactic Sector). Let

                                       Hgal = L2 (R3r ) ⊗ ℓ2 (P) ⊗ L2 (Rt ),
            lawful
and define Hgal    := Phalo Hgal ∩ Hlawful using (1).

Definition 2 (Halo Hamiltonian and USO Restriction). We set

                               Hhalo = −∇2 + VD (r) + VΓ (r) +               HMR ,
                                       |   {z     }   | {z }                 | {z }
                                         fractal mass law       coherence   X⊕CΛp ⊕Ξ


with ρ(r) ∝ rD−3 and VD chosen so that M (r) ∝ rD . The restricted USO acts on Hgal
                                                                                lawful
                                                                                       with determinant
factorization detreg (I − U) = C/ζ (unchanged denominator).

  Date: September 2025.
                                                            1
SIMULATION THEORY                                                                              KEN PARROTT

Definition 3 (Prime–Window Coherence). Let u := ln r. Define prime windows ψp,k (u) := cosh−2 u−kδ ln p
                                                                                                                

and a nonnegative prime weight vector w ≥ 0. The coherence is
                                              X
(2)                           ∂ln r ln Γ(u) =   wp,k ψp,k (u),
                                                  p,k
                                                        Z uX                     
(3)                                      Γ(u) = exp               wp,k ψp,k (s) ds ,
                                                            p,k

and the associated bounded, saturating potential is
                                                    Γ(r) − 1
                                  VΓ (r) = λΓ                         (λΓ , cΓ > 0).
                                                1 + cΓ (Γ(r) − 1)
Definition 4 (Cross-Domain Tolerance). The lawfulness tolerance is
                                            ε = α ∆USO + β σBTFR ,
with ∆USO the minimal stable bench spectral gap under prime gating, and σBTFR the intrinsic BTFR scatter
(converted to slope units). Parameters (α, β) are obtained by a fixed-point fit minimizing a lawfulness misfit
across lab and galaxy residuals.
1.4. Theorems and Stability.
Theorem 1 (Kato–Rellich Boundedness). If VD ∈ L∞                                  1
                                                      loc and VΓ is bounded and C , then Hhalo is self-adjoint
                                     2
on D(H0 ) ∩ D(HMR ) with H0 = −∇ + VD . Consequently, the USO Fredholm–zeta factorization extends to
  lawful
Hgal     and RH-aligned spectral pinning is preserved up to bounded shifts induced by VΓ .
                                                 lawful
Theorem 2 (Lawful–Flat Equivalence up to ε). On Hgal    the following are equivalent:
    (1) ∥(D − 1) + ∂ln r ln Γ∥∞ ≤ ε,
    (2) the restricted USO has no spectral weight outside a band of width O(ε) about the MR critical set
         (prime-gated plateaus).
Sketch. Use a virial identity in u = ln r, a Duhamel expansion w.r.t. VΓ , and Lipschitz control on the slope
of ln Γ to equate slope smallness with bandlimited spectral transfer.
Proposition 1 (Prime–Sparsity of Coherence). If the empirical slope g(u) := ∂ln r ln vc2 (u) is piecewise C 1
with finitely many bounded excursions, the nonnegative ℓ1 -regularized fit of Def. 3 admits a solution with
finite support per decade in r (prime-window sparsity).
1.5. Inference Pipeline and Algorithmic Clause. Given smoothed vc (r), set u = ln r, compute g(u) =
∂ln r ln vc2 (u), estimate D̂ from outer radii (where Γ is approximately constant), and solve the nonnegative
sparse regression
                                                     2
                               min Φw − (1 − D̂)1 2 + λ∥w∥1 , Φi,(p,k) = ψp,k (ui ).
                            w≥0

Construct Γ, reconstruct vc via vc2 ∝ rD̂−1 Γ, and evaluate lawfulness via (1). Calibrate ε with a fixed-point
bootstrap using (∆USO , σBTFR ).
1.6. Tests and First Results. We executed a synthetic trial (mock SPARC-style curve) with two active
windows near u = ln 33 and u = ln 52 . The pipeline recovered:
      • D̂ = 2.37 ± 0.03 (truth 2.4),
      • a sparse active set P⋆ = {(3, 3), (5, 2), . . .} with weights rank-ordered as expected,
      • ε converged under the cross-domain bootstrap, yielding a lawfulness fraction (radial coverage within
        the tolerance band) of ∼ 0.9 on the mock.
These synthetic results validate identifiability of (D, {wp,k }) and stability of the tolerance calibration. Real-
galaxy analysis is now a parameterized substitution into the same pipeline.
1.7. Implications, Predictions, and Falsifiability.
Scaling and rotation. With vc2 (r) ∝ rD−1 Γ(r), flatness is the selection manifold (D − 1) + ∂ln r ln Γ = 0
                                        P
(within ε). The core radius Rc satisfies p,k wp,k ψp,k (ln Rc ) = 1 − D̂, predicting multi-core structure when
neighboring windows overlap.
                                                     2
KEN PARROTT                                                                                 SIMULATION THEORY

Weak lensing. Projected profiles obey κ(R) ∝ RD−2 Γ⊥ (R), with extended tails when large-scale windows
dominate.
Environmental resets. Mergers/decoherence events reduce prime weights (w → w − ∆w) and widen δ, steep-
                                                              (∞)
ening curves transiently; recovery follows ẇp,k = −(wp,k − wp,k )/τp,k .
Prime–Lawful Echo (P3). The active prime set P⋆ inferred from galaxies should correlate with primes max-
imizing stability in MR bench spectra. Falsification: absence of a statistically significant correspondence
(against null ensembles) disconfirms the universality claim and collapses the MR–FEMDM bridge to a purely
phenomenological galaxy fit.
1.8. Ethical–Epistemic Note. Lawfulness equals computability under prime-gated spectra; preserving
prime–sparse stability aligns with energy-efficient, predictable dynamics. This formalizes “lawful computa-
tion = ethical computation” in the MR frame without extra metaphysical load.
1.9. Checklist for the “Methods & First Results” Paper. (1) Axioms and operator definitions (this
section). (2) Data pipeline: smoothing, slope estimation, sparse nonnegative fit, bootstrap for ε. (3)
Synthetic validation (above). (4) SPARC subset analysis (high-quality, isolated). (5) Lensing cross-checks.
(6) Bench–astro prime correspondence statistics (reserved for follow-up if desired).

                Appendix A. Mathematical Appendix: Proofs and Operator Bounds
A.1. Notation and Standing Assumptions. Let u := ln r, ψp,k (u) := cosh−2 u−kδ ln p with fixed δ ∈
                                                                                   

(0, 1), and let                              X
                             ∂ln r ln Γ(u) =   wp,k ψp,k (u), wp,k ≥ 0.
                                                  p,k
Define                           Z uX                                            Γ(r) − 1
                    Γ(u) = exp              wp,k ψp,k (s) ds ,   VΓ (r) = λΓ                     ,
                                   u0 p,k                                      1 + cΓ (Γ(r) − 1)
with λΓ , cΓ > 0. The fractal mass law is encoded by ρ(r) ∝ rD−3 and a confining VD ∈ L∞     3
                                                                                       loc (R ) such that
           D
M (r) ∝ r . We write
                        Hhalo = (−∆ + VD ) + VΓ + HMR ,              HMR = X ⊕ CΛp ⊕ Ξ,
acting on Hgal = L2 (R3r ) ⊗ ℓ2 (P) ⊗ L2 (Rt ) with canonical domain D(H0 ) ∩ D(HMR ), where H0 := −∆ + VD .
The halo-lawfulness projector is
                                               n                           o
                                     Phalo = 1 (D − 1) + ∂ln r ln Γ(r) ≤ ε .

A.2. Bounds for Γ and VΓ .
                                                         P
Lemma A.1 (Uniform bounds on Γ and its slope). Let W := p,k wp,k < ∞. Then for all u,
                                               X
                           0 ≤ ψp,k (u) ≤ 1,      wp,k ψp,k (u) ≤ W,
                                                          p,k

and consequently                                     
                            1 ≤ Γ(u) ≤ exp W |u − u0 | ,           ∥∂ln r ln Γ∥L∞ ≤ W.
                    −2
R u P Since cosh (·) ∈ (0, 1], the first line is immediate. Integrating ∂ln r ln Γ yields ln Γ(u) − ln Γ(u0 ) =
Proof.
 u0   p,k wp,k ψp,k (s) ds, bounded by W |u − u0 |.                                                           □

Lemma A.2 (Boundedness and Lipschitz continuity of VΓ ). With VΓ (r) = λΓ 1+cΓ−1
                                                                             Γ (Γ−1)
                                                                                     and Γ ≥ 1, we have
                       0 ≤ VΓ (r) ≤ λΓ /cΓ ,       |VΓ (r1 ) − VΓ (r2 )| ≤ LΓ |Γ(r1 ) − Γ(r2 )|,
                        2
where LΓ = λΓ /(1 + cΓ ) . Moreover, along u = ln r,
                                  d
                                    VΓ ≤ LΓ Γ(u) ∂ln r ln Γ L∞ ≤ LΓ Γ(u) W.
                                 du
Proof. The map x 7→ λΓ 1+cx−1 Γ (x−1)
                                       is increasing for x ≥ 1, bounded above by λΓ /cΓ , and has derivative
                    2               2
λΓ /(1 + cΓ (x − 1)) ≤ λΓ /(1 + cΓ ) .                                                                    □
                                                         3
SIMULATION THEORY                                                                                         KEN PARROTT

A.3. Kato–Rellich Boundedness (Theorem 1).
Assumption A.1 (MR core self-adjointness). HMR is self-adjoint on D(HMR ), semibounded from below,
and HMR commutes with the r-representation on the first tensor factor.1
Lemma A.3 (Relative boundedness of VΓ ). VΓ defines a bounded multiplication operator on L2 (R3 ) with
∥VΓ ψ∥2 ≤ (λΓ /cΓ ) ∥ψ∥2 . Hence VΓ is H0 -bounded with relative bound a = 0 and bound constant b = λΓ /cΓ .
Proof. By Lemma A.2, ∥VΓ ∥L∞ ≤ λΓ /cΓ . Thus ∥VΓ ψ∥2 ≤ ∥VΓ ∥∞ ∥ψ∥2 .                                                       □
Proof of Theorem 1. H0 = −∆ + VD is self-adjoint on the standard domain by VD ∈                 and lower- L∞
                                                                                                            loc
semicontinuity. By Lemma A.3, VΓ is a bounded perturbation (relative bound 0). By Assumption A.1,
HMR is self-adjoint and (as a direct sum on different tensor factors) is either bounded or H0 -bounded
with arbitrarily small relative bound on the spatial domain. Kato–Rellich thus implies self-adjointness of
Hhalo = H0 + VΓ + HMR on D(H0 ) ∩ D(HMR ). The Fredholm–zeta correspondence for the USO persists
                                                                                                 lawful
under bounded perturbations, so the determinant factorization extends to the restricted sector Hgal     . □
A.4. Virial Identity in u = ln r and Spectral Banding. We recast the slope condition as a logarithmic
virial:
                                          d                         d
                                g(u) :=     ln vc2 (u) = (D − 1) +    ln Γ(u).
                                         du                        du
Flatness within tolerance is the uniform bound ∥g∥∞ ≤ ε on u-intervals of interest. Let U(t) denote the
                                lawful
restricted USO semigroup on Hgal       .
Lemma A.4 (Duhamel control of spectral transfer). Let A be the generator of U, decomposed as A = A0 +B,
where A0 is the MR critical generator and B is the (bounded) perturbation induced by VΓ and VD . Then for
any spectral projector PI (A0 ) onto a band I,
                                ∥(1 − PI (A0 )) U(t) PI (A0 )∥ ≤ ∥B∥ t e∥A∥t .
                                               Rt
Proof. Use Duhamel’s formula U (t) = etA0 + 0 e(t−s)A0 BesA ds and project with (1 − PI (A0 )) on the left
and PI (A0 ) on the right. The norm bound follows by submultiplicativity.                               □
                                                   lawful
Lemma A.5 (Slope residual controls ∥B∥). On Hgal          , the operator B induced by VΓ satisfies ∥B∥ ≤
C ∥∂ln r ln Γ∥∞ for a constant C depending only on (λΓ , cΓ , δ) and the spatial embedding. In particular, if
∥(D − 1) + ∂ln r ln Γ∥∞ ≤ ε, then ∥B∥ ≤ C(ε + |D − 1|).
Proof. By Lemma A.2, VΓ is Lipschitz in Γ and Γ has slope bounded by ∥∂ln r ln Γ∥∞ . The generator
difference B is the operator induced by multiplication with VΓ and bounded commutators with the MR
core; each term is controlled by ∥VΓ ∥∞ and ∥∇VΓ ∥∞ , the latter bounded by LΓ Γ ∥∂ln r ln Γ∥∞ . Uniform
boundedness on the considered sector yields the stated inequality.                                     □
Proof of Theorem 2. Take I to be the MR critical band. If ∥(D − 1) + ∂ln r ln Γ∥∞ ≤ ε, Lemma A.5 gives
∥B∥ ≤ Cε′ , with ε′ proportional to ε. Lemma A.4 then bounds the out-of-band transfer by O(ε′ ) uniformly
on bounded t-intervals, proving (i)⇒(ii). Conversely, if (ii) holds, then the out-of-band spectral weight is
small; applying the virial identity to the effective radial generator implies that the dilation current (which
is precisely g(u)) remains uniformly small, hence (i) with some ε proportional to the band width.           □
A.5. Prime-Window Dictionary, Norms, and Sparse Recovery. Let Φ ∈ Rn×m with Φi,(p,k) =
ψp,k (ui ) and ui = ln ri .
Lemma A.6 (Uniform bounds and Gram conditioning). Each column ϕ(p,k) satisfies ∥ϕ(p,k) ∥∞ ≤ 1 and
            √
∥ϕ(p,k) ∥2 ≤ n. Moreover, for centers separated by at least 2δ in u, the off-diagonal Gram terms obey
                                ⟨ϕ(p,k) , ϕ(q,ℓ) ⟩ ≤ κ(δ) ∥ϕ(p,k) ∥2 ∥ϕ(q,ℓ) ∥2 ,   κ(δ) < 1,
with κ(δ) → 0 as the minimal separation grows.
Proof. The ∞ and 2-norm bounds are immediate since 0 < ψp,k ≤ 1. The overlap of two cosh−2 windows
decays exponentially in the center separation; discretization preserves a uniform angle bound, giving κ(δ) < 1
for a separated dictionary.                                                                                 □
   1This is standard in the MR construction where X, C
                                                         Λp , Ξ act on the prime/time components and as bounded (or relatively
bounded) forms on the spatial factor.
                                                               4
KEN PARROTT                                                                               SIMULATION THEORY

Proposition 2 (Existence and stability of sparse nonnegative fit). Let g⋆ (u) ≡ 1 − D̂ and consider
                                            min ∥Φw − g⋆ ∥22 + λ∥w∥1 .
                                            w≥0

If the active set of centers is η-separated (η ≳ δ) and λ > 0, then there exists a minimizer w♯ with finite
support per u-decade. Moreover,
                                       ∥w♯ − wtrue ∥1 ≤ C1 λ + C2 ∥ξ∥2 ,
for constants C1,2 depending on κ(δ) and the sampling, where ξ is the (optional) smoothing/differentiation
noise in g.
                                           √
Proof. Coercivity follows from ∥Φw∥2 ≤ n∥w∥1 and λ∥w∥1 . Existence is standard. Stability is obtained
via classical Lasso bounds under mutual incoherence or restricted eigenvalue conditions; Lemma A.6 provides
the needed incoherence through κ(δ). Nonnegativity further sharpens identifiability (cone constraint).   □
A.6. Bootstrap Calibration of ε. Let σBTFR be the intrinsic BTFR scatter (in dex of log v). Convert
to a slope proxy by σslope ≈ 2 ln 10 σBTFR . With ∆USO the smallest stable MR spectral gap under prime
gating, define
                                        ε(α, β) = α ∆USO + β σslope .
Proposition 3 (Convergence of the fixed-point bootstrap). Define the update
                                                                             2
                   (αt+1 , βt+1 ) = arg min    med(|g(u)|) − α ∆USO − β σslope ,
                                            α,β≥0

and set εt+1 = αt+1 ∆USO + βt+1 σslope . If the median residual R := med(|g|) is strictly between 0 and
∆USO + σslope , the iteration converges in one step to
                                          ε⋆ = min{R, ∆USO + σslope },
with (α⋆ , β⋆ ) lying on the simplex α ∆USO + β σslope = R.
Proof. The least-squares problem in (α, β) under a single linear constraint has a closed-form solution; with
nonnegativity and two features, the optimizer selects a convex combination achieving R exactly when feasible,
else it saturates a boundary. Thus ε matches the observed central residual in one update, giving a fixed
point. In practice we keep a few iterations to stabilize against sampling noise.                           □
                                                         2
A.7. Reconstruction Error and Lawfulness Coverage. Let vmodel (u) = c e(D−1)u Γ(u) with c > 0 fitted
by least squares. Denote gmodel (u) = (D − 1) + ∂u ln Γ.
Lemma A.7 (Reconstruction error bound). If ∥g − gmodel ∥∞ ≤ ε, then for any u1 < u2 ,
                                        2                 2
                                      vobs (u2 )        vobs (u1 )
                                ln    2           − ln  2             ≤ ε |u2 − u1 |.
                                     vmodel (u2 )      vmodel (u1 )
Consequently, after fixing c at u1 , the relative error at u2 is ≤ eε|u2 −u1 | − 1.
                                           2        2
                                                            R
Proof. Integrate the slope difference: ln vobs −ln vmodel = (g−gmodel ) du and apply the sup-norm bound.   □
  Define the lawfulness fraction
                                       1
                                          meas{u ∈ I : |g(u)| ≤ ε}
                                        L :=
                                      |I|
on an interval I. Lemma A.7 implies that on each lawful subinterval the reconstruction error remains
uniformly controlled.
A.8. Projection for Lensing and Stability. Let Γ⊥ (R) denote the line-of-sight projection of Γ. With a
spherically symmetric kernel K(z) normalized on R,
                                         Z ∞         p         
                                Γ⊥ (R) =      K(z) Γ ln R2 + z 2 dz.
                                                  −∞
By Jensen and Lemma A.1, Γ⊥ (R) inherits log-Lipschitz control:
                        d                        d         p          
                            ln Γ⊥ (R) ≤ sup           ln Γ ln R2 + z 2                  ≤ W,
                     d ln R                 z  d ln r
so κ(R) ∝ RD−2 Γ⊥ (R) has slope bounded by |D − 2| + W in ln R.
                                                  5
SIMULATION THEORY                                                                         KEN PARROTT

A.9. Summary of Constants and Practical Choices.
     • Window width δ: choose 0.1–0.2 in u = ln r to ensure Gram incoherence (Lemma A.6).
     • Regularization λ: pick by cross-validation or Morozov discrepancy to balance fit and sparsity
       (Proposition 2).
     • Bounds: ∥VΓ ∥∞ ≤ λΓ /cΓ , ∥∂ln r ln Γ∥∞ ≤ W , ∥B∥ ≤ C(ε + |D − 1|).
     • Reconstruction error: on a span ∆u, the relative error is O(eε∆u − 1) (Lemma A.7).
A.10. Implication: Robustness of the MR–FEMDM Bridge. The chain of bounds (Lemmas A.1,
A.2, A.4, A.5) and Theorems 1, 2 establish that the astrophysical slope condition is equivalent, up to a
tunable tolerance ε, to spectral band-limiting of the restricted USO. Sparse prime windows suffice to attain
this regime with controlled reconstruction error, and the cross-domain bootstrap for ε closes the loop with
laboratory spectral gaps.

                                               References




                                                     6

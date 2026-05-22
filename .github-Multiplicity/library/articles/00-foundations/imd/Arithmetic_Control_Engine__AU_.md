---
slug: arithmetic-control-engine-au
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 00-foundations/imd/Arithmetic_Control_Engine__AU_.md
  last_synced: '2026-03-20T17:17:22.480649Z'
---

           Integrating the Arithmetic Control Engine (ACE) with the
                                  AU–Triad:
           Measure, Compare, Equalize for Certified Spectral Control



                                                          Abstract
              We formalize how to integrate the Arithmetic Control Engine (ACE) into the AU–Triad
          pipeline. ACE supplies exact arithmetic operators (Hecke Tn on Sk (Γ0 (N ))), a unitary-constrained
          Spectral Control Network (SCN), and a Weyl-inequality certificate for gap control. The AU–
          Triad supplies system-level gates: Measure spectral/arithmetical invariants, Compare against
          theorem-backed tests and envelopes, then Equalize via certified updates (projection-first) with
          audit logs. The result is a reproducible, math-first loop that blends arithmetic structure with
          certified optimization.


1        Arithmetic layer (ACE) and spectral state
1.1        Arithmetic operators
Fix even k ≥ 2 and level N ≥ 1. Let Sk (Γ0 (N )) denote cusp forms of weight k and level N .
For n ∈ N, the Hecke operator Tn acts linearly on Sk (Γ0 (N )). In particular, if (m, n) = 1, then
Tm Tn = Tmn (Dirichlet-convolution law for general m, n).1 Let Mn be a matrix representation of
Tn in a chosen basis; ACE computes these exactly via a CAS.

1.2        Spectral features and gaps
Let A ∈ Cd×d be a normal/Hermitian operator representing the current spectral state (e.g., a Hecke
matrix, its symmetrization, or a learned graph operator). Let λ1 ≤ · · · ≤ λd be eigenvalues and
define the spectral gap                                     
                                  g(A) := min λi+1 − λi .
                                                         1≤i≤d−1

A target ĝ > 0 is provided by design or downstream objectives.

1.3        Spectral Control Network (SCN)
The SCN maps state features ϕ(A, ĝ) to a control vector w that parameterizes a perturbation ∆(w)
with an explicit norm budget. A stability-preserving internal transform uses a skew-symmetric
parameter S = −S ⊤ and U = exp(S), so that ∥xU ∥2 = ∥x∥2 for all x (unitary/orthogonal block).
The SCN loss tracks the target gap and penalizes budget violations:
                                               2
                   L(θ) = g(A + ∆(wθ )) − ĝ + λ max{0, ∥∆(wθ )∥2 − ε}2 .
    1
        RP bound: for normalized eigenforms f , |ap (f )| ≤ 2p(k−1)/2 for primes p ∤ N .




                                                               1
2    AU–Triad mapping
We integrate ACE into the AU–Triad (Measure–Compare–Equalize) as follows.

Measure
    • Arithmetic invariants: multiplicativity residuals ρm,n := ∥Mm Mn − Mmn ∥ for (m, n) = 1;
      RP residuals maxp |ap | − 2p(k−1)/2 + .
                                         

    • Spectral statistics: g(A), min λ, max λ, mean(λ), std(λ), and nearest-neighbor spacings.
    • Distributional diagnostics (optional): KS/CvM comparisons of empirical spectra to a
      reference law (e.g., Wigner-like surrogates) with predeclared thresholds/CIs.

Compare
    • Theorem-backed checks: require ρm,n ≤ εalg and RP residual = 0 within tolerance.
    • Envelope checks: budget ∥∆∥2 ≤ ε; Lipschitz/softmax envelopes (when present) SlopeUB ≤
      τslope .
    • Gap targets: compare g(A) to ĝ; define acceptable band |g(A) − ĝ| ≤ δg (predeclared).

Equalize
Produce a certified update via SCN → projection → apply:
                          A+ = A + ∆⋆ ,       ∆⋆ ∈ arg min       ∆ − ∆(w) .
                                                       ∥∆∥2 ≤ε

By Weyl’s inequality (see Prop. 3), the spectral gap obeys |g(A+ ) − g(A)| ≤ 2ε, which yields a
simple, auditable acceptance rule.


3    Certificates
[Unitary block is norm-preserving] Let S = −S ⊤ and U = exp(S). Then U ⊤ U = I and for all x,
∥xU ∥2 = ∥x∥2 .
   [Weyl gap certificate] If A is Hermitian and ∥∆∥2 ≤ ε, then for all i, |λi (A + ∆) − λi (A)| ≤ ε
and thus
                                     |g(A + ∆) − g(A)| ≤ 2 ε.
   [Weighted-ℓ1 projection with KKT certificate P (optional)] Given     weights ωk > 0 and budget
                              m                                      ⋆
T > 0, the projection of v ∈ R onto Ω = {x : k ωk |xk | ≤ T } is xk = sign(vk ) max{|vk | − τ ωk , 0}
with τ ≥ 0 chosen so that the constraint is tight when active. Feasibility, complementary slackness,
and a dual lower bound provide an auditable optimality certificate.


4    Integration objective
Define a composite training objective (if learning is active)
                        2                                            X                    X                        2
J = g(A + ∆(w)) − ĝ + λ∆ max{0, ∥∆(w)∥2 − ε}2 + λalg                        ρ2m,n + λRP           |ap | − 2p(k−1)/2 + .
      |       {z         }      |           {z          }                                      p
                                          budget                  (m,n)=1
           gap tracking                                           |     {z      }          |             {z          }
                                                                  multiplicativity                   RP bounds


                                                   2
5    Pass/fail gate and audit record
Fix thresholds (εalg , ε, τslope , δg ) and CI parameters for distributional tests. A step passes iff all
hold:         
                ρ       ≤ εalg ∀(m, n) = 1,          max(|ap | − 2p(k−1)/2 )+ = 0,
               m,n
              
                                                      p
                                           +
               ∥∆∥2 ≤ ε,              |g(A ) − g(A)| ≤ 2ε,     |g(A+ ) − ĝ| ≤ δg ,
              
                (optional) KS/CvM within preregistered bands; SlopeUB ≤ τslope .
              

Audit tuple (per step):

           g(A), g(A+ ), ∥∆∥2 , 2ε, {ρm,n }(m,n)=1 , max(|ap | − 2p(k−1)/2 )+ , KS, SlopeUB .
                                                                                           
                                                       p


6    Algorithm (AU–Triad ⊕ ACE)

Algorithm 1 One certified integration step
 1: Inputs: operator A; target gap ĝ; budget ε; arithmetic set N ; thresholds.
 2: Measure:
       (a) Compute g(A), summary stats; (b) for (m, n) = 1, form Mm , Mn , Mmn , record ρm,n ;
       (c) RP residuals from eigenvalues {ap }.
 3: Compare: check algebraic tests and envelopes vs. thresholds.
 4: Equalize (proposal): w ← SCN(ϕ(A, ĝ)), form ∆(w).
 5: Projection/envelope: ∆⋆ ← arg min∥∆∥2 ≤ε ∥∆ − ∆(w)∥ (or weighted-ℓ1 variant).
 6: Apply: A+ ← A + ∆⋆ .
 7: Certificate: verify |g(A+ ) − g(A)| ≤ 2ε; re-check algebraic tests; log audit tuple.
 8: if all gates pass then
 9:     accept A ← A+ ;
10: else
11:     rollback and (optionally) shrink ε or retrain SCN.
12: end if


7    Remarks and options
    • Which A? For pure arithmetic checks, take A = Mn or a block of {Mp }. For learned systems
      (e.g., graph/attention operators), use the system operator and keep arithmetic residuals as
      side-constraints/features.

    • Distributional checks: Use KS/CvM with bootstrap CIs as diagnostics; preregister pass
      bands and seeds.

    • AU–Triad compatibility: The gap certificate plays the role of a simple Lyapunov-style
      bound; the projection-first step matches the Triad’s certificate-before-actuation philosophy
      and standard logging (Measure stats, Compare gates, Equalize update).




                                                   3

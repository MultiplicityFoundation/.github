---
slug: sapgc-formalization-final-pgf-consistent-umc-rewrite
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Sapgc Formalization (final Pgf-consistent Umc Rewrite).md
  last_synced: '2026-03-20T17:17:20.392931Z'
---

Scale‑Adaptive Prime‑Graded Feedback Controller
(SAPGC)
This document formalizes the exact final SAPGC form: a PGF‑consistent prime‑graded structural layer, a
raw → certified gain pipeline, and a typed physics interface. It is designed to be a drop‑in replacement for
the 3‑page UMC equations (2)–(7) while preserving meaning and eliminating tensor/scalar and dimensional
inconsistencies.




0. Notation and typing
     • P: the set of primes.
     • PN ⊂ P: a finite prime set (cutoff model). (Infinite‑prime extensions require boundedness
       conditions stated below.)
     • X : a real Banach space with norm ∥ ⋅ ∥. When Rayleigh quotients are used, assume X is a real
       Hilbert space with inner product ⟨⋅, ⋅⟩ and induced norm.
     • B(X): bounded linear operators on X .

Type convention (core separation‑of‑concerns):


     • Structural prime content lives in operators/projectors {Pp } and their prime‑weighted combination
       S ∈ B(X).
     • The deployed gain Λm is always a real scalar: Λm ∈ R.




1. Structural layer: prime‑graded operator

Definition 1.1 (Prime projectors)

Let {Pp }p∈PN ⊂ B(X) be bounded projectors. Typical cases:


     • Orthogonal resolution (Hilbert): Pp = Pp∗ = Pp2 and Pp Pq = 0 for p  q . =
     • Non‑orthogonal / non‑normal case: Pp need only be bounded projectors; extra conservatism
       enters via ∥S∥.

Assume ∥Pp ∥ ≤ 1 for simplicity (can be relaxed).


Definition 1.2 (Prime weights)

Choose exponents αp ∈ R and define weights


                                                wp := pαp .




                                                     1
Definition 1.3 (Prime‑graded structural operator)

Define


                                        S := ∑ wp Pp ∈ B(X).
                                              p∈PN

Because PN is finite, S is bounded.


Remark 1.4 (Infinite‑prime boundedness)

If one extends to infinite P∞ ⊂ P, a sufficient condition for boundedness is


                                               sup pαp < ∞,
                                               p∈P∞

which (for unbounded primes) forces lim supp→∞ αp ≤ 0 unless one renormalizes or truncates.




2. Dynamics layer: affine prime‑graded recursion

Definition 2.1 (State, forcing, update)

Let Tt ∈ X be the prime‑sector state at discrete time t ∈ N. Let F ∈ X be a fixed forcing term.


Define the update map


                                   Tt+1 = Φt (Tt ) := Λm (Tt ) S Tt + F .

Here Λm (⋅) is the deployed gain, defined by the raw → certified pipeline in §3.




3. Gain layer: raw → certified pipeline
SAPGC separates meaningful/raw proposals for Λm from a certifier that guarantees contraction.


3.1 Raw gain proposals (meaning layer)

You may choose one or more raw proposals Λm . Two canonical families:


(A) Invariant / prime‑harmonic family (finite primes)

Let M (T , p) ≥ 0 be a multiplicity/measurement functional (user‑defined). Fix α ∈ R. Define

                                                                       −1
                                    m (T ) := ( ∑ M (T , p) p ) ,
                                   Λinv                      −α

                                                  p∈PN




                                                      2
provided the denominator is positive.


A special “universal target” ignores state dependence:

                                                                        −1
                                             Λ⋆m := ( ∑ p−α ) .
                                                        p∈PN


(B) Prime‑harmonic / phase‑transition modulation family

Let τ be a phase variable (or a function of energy E ). Choose coefficients ai , primes pi ∈ PN , and ωi :=
log pi . Define


                                  m (τ ) := Λ0 exp( − ∑ pi ai sin(ωi τ )).
                                 Λph
                                                                i


3.2 Certified fences (safety layer)

Fix a contraction margin γ ∈ (0, 1). Define the global fence

                                                                     γ
                                                Λglob (γ) :=            .
                                                                    ∥S∥

When X is Hilbert, define the Rayleigh quotient (directional average)

                                                 ⟨T , Ssym T ⟩
                                      r(T ) :=                 ,            T  0,        =
                                                    ∥T ∥2

where

                                                         1
                                               Ssym :=     (S + S ∗ )
                                                         2
is used to handle non‑normal S . (If S is already self‑adjoint, take Ssym = S .)


Define the local fence

                                                                      γ
                                              Λloc (T ; γ) :=             ,
                                                                    r(T )

when r(T ) > 0. (If r(T ) ≤ 0, skip the local gate and fall back to the global fence.)


3.3 Scale‑adaptive schedule for γ

Let E : X → (0, ∞) be an “energy” functional. Define a clipped schedule

                                                                      γ0
                                γ(E) := clip[γmin ,γmax ] (                      ),
                                                              1 + log(1 + E/E0 )

with parameters




                                                          3
                               0 < γmin < γmax < 1,        γ0 > 0, E0 > 0.

3.4 The raw → certified deployed gain (the SAPGC line)

Let Λm be any raw proposal (possibly state‑dependent).


Deployed gain (raw → certified):


                     Λm (T ) := min {Λglob (γ(E(T ))), Λloc (T ; γ(E(T ))), Λm (T )}.


Operationally:


1) compute Λm (T ) (meaning), 2) compute global and local safe fences (safety), 3) deploy the minimum.


This guarantees safety regardless of the raw proposal.




4. Core stability results

Theorem 4.1 (One‑step contractivity)

Assume Λm (T ) ≤ Λglob (γ) for some γ ∈ (0, 1). Then for all U , V ∈ X ,


                                     ∥Φ(U ) − Φ(V )∥ ≤ γ ∥U − V ∥.

Proof: ∥Φ(U ) − Φ(V )∥ = ∥Λm S(U − V )∥ ≤ ∥Λm S∥ ∥U − V ∥ ≤ γ ∥U − V ∥.


Corollary 4.2 (Hybrid safety)

Because Λm (T ) is defined as the minimum including Λglob , it always satisfies ∥Λm (T )S∥ ≤ γ(E(T )) ≤
γmax < 1.

Theorem 4.3 (Uniform geometric bound)

If γ(E(Tt )) ≤ γmax < 1 for all t, then

                                               ′
                                     ∥Tt+k − Tt+k      k
                                                  ∥ ≤ γmax ∥Tt − Tt′ ∥.

Remark 4.4 (Fixed point when Λm is constant)

If Λm is held constant with ∥Λm S∥ < 1, then I − Λm S is invertible and


                                          T∞ = (I − Λm S)−1 F

is the unique fixed point.



                                                     4
When Λm (T ) varies with T , one typically proves convergence by showing the map remains contractive
and/or by bounding the product ∏t γ(E(Tt )).




5. PGF‑consistent rewrite of UMC equations (2)–(7)
This section gives the surgical replacement of the UMC excerpt’s equations (2)–(7) into SAPGC form.


(2′) Prime‑graded structural operator and recursion (typed)

                               S := ∑ pαp Pp ,        Tt+1 = Λm (Tt ) S Tt + F .
                                    p∈PN


(2″) Raw → certified gain line (explicit)

Pick any raw proposal Λm (e.g. Λinv   ph
                                m or Λm ).



                   Λm (T ) := min { γ(E(T )) γ(E(T ))
                                      ∥S∥ ,    r(T ) , Λm (T )},         0 < γ(E(T )) < 1.


(3′) Einstein equation uses Λphys , not Λm

Define a physical cosmological scalar via one scale μ2 (units L−2 ):


                                      Λphys (x) := Λ0 + μ2 Λm (T (x)).

Then the typed gravitational equation is

                                                           matter    PGF
                               Gμν + Λphys (x) gμν = 8πG (Tμν     + Tμν  ).


(4′) Prime‑sector stress tensor defined via an action (conservation‑friendly)

Choose a covariant prime‑sector Lagrangian density LPGF (model‑dependent) and define


                                                2   δ
                                   PGF
                                  Tμν  := −              ∫ d4 x −g LPGF .
                                                −g δg μν


(5′)–(7′) Gravitational‑wave equation and dispersion (dimensionally correct)

If one retains the UMC‑style modification as a mass‑like term, write


                              (□ − m2eff (x)) hμν = 0,       m2eff (x) := Λphys (x).

For plane waves h ∼ eik⋅x :




                                                         5
                                  η αβ kα kβ = m2eff ,       ω 2 − ∥k ∥2 = m2eff .

Consequently, for m2eff > 0, group speed is subluminal.




6. Optional: SdS interface for UMC (8)–(10) (typed, first‑order)
If desired, use Λphys in the Schwarzschild–de Sitter lapse

                                              rs   Λphys 2                  2GM
                                f (r) = 1 −      −      r ,          rs =       .
                                              r     3                        c2
Small‑Λphys rs2 black‑hole horizon:

                                               1
                                      rh = rs + Λphys rs3 + O(Λ2phys rs5 ).
                                               3
Hawking temperature (first order):

                                        ℏc3       4
                             TH =             (1 − Λphys rs2 + O(Λ2phys rs4 )).
                                      8πGM kB     3



7. Implementation checklist (minimal, unambiguous)
1) Choose PN (finite primes), αp , projectors Pp , build S . 2) Choose energy functional E(T ). 3) Choose raw
gain Λm . 4) Compute γ(E(T )) and fences Λglob , Λloc (if available). 5) Deploy Λm (T ) =
min{Λglob , Λloc , Λm }. 6) Update Tt+1 = Λm (Tt )STt + F . 7) (Optional physics) map Λm → Λphys and
couple into GR/GW equations.




8. What SAPGC does and does not claim
SAPGC guarantees: stability of the prime‑graded recursion under the certified fences (contractivity).


SAPGC does not imply by itself: any specific cosmological observation, GW anomaly, BH shift, or gauge
unification—those require additional modeling choices in LPGF , E(T ), Λm , and the map to Λphys .




                                                         6

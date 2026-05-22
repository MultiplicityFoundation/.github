---
slug: cmfc-definition-theorem-ready-rewrite-of-equations-1-5
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "03-case-studies/Cmfc Definition (theorem-ready Rewrite Of Equations (1)\u2013\
    (5)).md"
  last_synced: '2026-03-20T17:17:21.498188Z'
---

Coupled Multiplicity Floer Complex (CMFC)
This section rewrites the proposal’s equations (1)–(5) into a single, coordinate-free Floer-type definition that
supports a well-posed chain complex.


0. Starting point: equations (1)–(5) as given
We begin from the five expressions in the note:


    1. Extended operator

                                             ∂u
                                F (u) =         + J∇H(u) + ∑ Tij ⋅ ∇Φ(u) + ξ(t).                            (1)
                                             ∂t            i,j


    2. Tensor/TQFT-style observable


                                           Ψ(u) = ∑ Tij (ui ⊗ uj ) ei(θi −θj ) .                            (2)
                                                     i,j


    3. Euler characteristic refinement (as written)


                                χ(M ) = ∫ (Rμνρσ Rμνρσ − 4Rμν Rμν + R2 ) d4 x.                              (3)
                                              M


    4. Hybrid quantum–classical correction term

                                       ∂u
                             F (u) =      + J∇H(u) + ∑ γmn um un cos(θm − θn ).                             (4)
                                       ∂t            m,n


    5. Adaptive/learning feedback functional

                                       N
                             L(t) = ∑ ∇H(ui ) ⋅ cos(ωi t + ϕi ) ⋅ F (t) ⋅ (1 + εi (t)).                     (5)
                                       i=1


The goal is to reinterpret these in a standard Floer analytic framework (elliptic PDE on R × S 1 ) while
preserving the intended ingredients: multiplicity, tensor-network couplings, stochastic feedback, and prime-
based encoding.




1. Geometric setup and hypotheses
Let (M , ω) be a symplectic manifold. Fix one of the following standard settings (either is sufficient):




                                                           1
(A) Exact/convex-at-infinity setting

      • ω = dλ is exact and M is convex at infinity (or geometrically bounded, as needed for Floer
        compactness).
      • Hamiltonians are chosen admissibly at infinity (e.g. linear or compactly supported) so that Floer
       trajectories have compactness.

(B) Closed monotone setting

      • M is closed and monotone: there exists κ > 0 such that c1 (TM ) = κ [ω] on π2 (M ).
      • Choose Novikov coefficients if needed to control bubbling.

Fix: - A smooth 1-periodic Hamiltonian Ht : M → R, t ∈ S 1 . - A smooth 1-periodic family of ω -compatible
almost complex structures Jt .


Multiplicity level

Fix an integer N ≥ 1. We work on the product symplectic manifold


                                  (M N , ω ⊕N )    with          ω ⊕N = ω ⊕ ⋯ ⊕ ω.

Write points as x = (x1 , … , xN ) ∈ M N , and maps as u = (u1 , … , uN ).


Coefficient ring and “prime encoding”

Let Λ be a Novikov-type coefficient ring appropriate to the setting (e.g. Z2 -Novikov in the monotone case;
Z2 in simple exact cases). Define the prime-extended ring

                                              R := Λ[p±1       ±1
                                                      1 , … , pN ],

where p1 , … , pN are formal prime generators. These variables record multiplicity/filtration data (they are
not a literal identification of trajectories with primes).


Tensor coefficients Tij

Let


                                          T = (Tij )1≤i,j≤N ∈ MatN (R)

(or MatN (R) if one wants algebraic weights as well). Analytically, taking Tij ∈ R is the cleanest choice;
algebraic prime weights can be handled separately via R.




2. Interaction potential Φ and the mode-coupling term
To interpret ∑i,j Tij ⋅ ∇Φ(u) in (1) in a coordinate-free way, we fold it into a single smooth coupling
Hamiltonian/potential on M N .




                                                             2
Pairwise coupling potential

Choose smooth 1-periodic functions


                                          ϕij,t : M × M → R,           t ∈ S1.

Define the tensor-weighted coupling potential

                                                        N
                                          Φt (x) := ∑ Tij ϕij,t (xi , xj ).
                                                      i,j=1

Assume Φt and its derivatives satisfy the standard growth/boundedness conditions required for Floer
compactness in your chosen setting.


Self-interaction (replacement for “ηu2 ”)

The term “ηu2 ” is not coordinate-free for manifold-valued u. Replace it by a smooth self-potential: - choose
V : M → R smooth, - choose η ∈ R, and add

                                                         N
                                             Φt (x) = η ∑ V (xi ).
                                              self

                                                        i=1


Mode-coupling (incorporating equation (4))

To absorb the ∑m,n γmn um un cos(θm − θn ) term into the same framework, choose: - smooth “mode
functions” am : M → R for m = 1, … , M0 , - phases θm ∈ R/2πZ, - coefficients γmn ∈ R (or R).


Define

                                     M0           N                   N
                   Φ   mode
                              (x) := ∑ γmn ( ∑ am (x ))( ∑ an (xj )) cos(θm − θn ).
                                                                  i

                                    m,n=1         i=1                 j=1

This is a coordinate-free analogue of (4): it is a smooth scalar function on M N built from “mode amplitudes”
am .

Total coupling

Define the total multiplicity coupling Hamiltonian


                                    Kt (x) := Φt (x) + Φself
                                                        t (x) + Φ
                                                                  mode
                                                                       (x).




                                                              3
3. The CMFC Floer operator (single consistent replacement for (1)
and (4))
Let Ht⊕N (x) := ∑i=1 Ht (xi ). Let XH ⊕N and XKt denote the Hamiltonian vector fields on (M N , ω ⊕N ).
                    N
                                       t



Deterministic perturbation term ξ(t)

To keep the Floer equation as a (perturbed) gradient-flow equation of an action functional, assume the
perturbation is Hamiltonian: - choose a smooth 1-periodic perturbation Gt : M N → R, - set ξt := XGt .


(If you truly want stochastic forcing, treat Gt as a random process and interpret the resulting equation as
an SPDE; that is a separate analytic package and is not required for the basic CMFC definition.)


CMFC operator on the Floer cylinder

Define the Coupled Multiplicity Floer operator


                     FCMFC (u) := ∂s u + Jt (u)(∂t u − XHt⊕N (u) − XKt (u) − ξt (u))

for maps u : R × S 1 → M N .


This is the Floer-elliptic replacement of (1): the term J∇H is realized as J(⋅)(−XH ) via the standard
identity between gradient and Hamiltonian vector fields under the metric g(⋅, ⋅) = ω(⋅, J⋅), and the “Tij ⋅
∇Φ” contribution is encoded by the scalar coupling Kt built from Tij and ϕij,t .



4. CMFC chain complex

Generators

Assume the 1-periodic orbits of the coupled Hamiltonian


                                           Ht := Ht⊕N + Kt + Gt

are nondegenerate. Let P(H ) denote the set of its 1-periodic orbits in M N .


Define the chain module


                                      CF∗ (H , J; R) := ⨁ R ⋅ x
                                                          x∈P(H )

graded by the usual Conley–Zehnder/Maslov index on M N (with standard conventions depending on
coefficients/orientations).




                                                      4
Prime weights

Fix homomorphisms


                              λi : π2 (M N , x− , x+ ) → Z,             i = 1, … , N ,

which encode the chosen “multiplicity data” (examples: component-wise symplectic area filtrations,
intersection counts with chosen cycles, or interaction/event counts defined by a geometric rule). For a Floer
trajectory class [u], define the prime monomial

                                                        N
                                          w([u]) := ∏ pi i
                                                              λ ([u])
                                                                        ∈ R.
                                                       i=1


Differential

Let M0 (x− , x+ ) denote the moduli space of solutions u of FCMFC (u) = 0 with Fredholm index 1, modulo
R-translation in s, connecting x− to x+ .

Define


                           ∂ x− :=     ∑             ∑            #M0 ([u]) w([u]) x+ .
                                     x+ ∈P(H ) [u]∈M0 (x− ,x+ )

(Here #M0 ([u]) is the signed count when orientations are available; otherwise use Z2 -counts.)


Well-definedness assumption

Assume the usual Floer analytic package holds for (M N , ω ⊕N ) with (Ht , Jt ): - compactness up to breaking
(and bubbling control in the monotone/Novikov setting), - transversality/regularity (e.g. by generic choices
or abstract perturbations).


Then the standard boundary-of-1-manifold argument implies


                                                      ∂ 2 = 0,

and we define the CMFC homology

                         HF∗CMFC (M ; N , T , Φ, γ; R) := H∗ (CF∗ (H , J; R), ∂).



5. Tensor observable Ψ (equation (2) as a derived functional)
Equation (2) is interpreted as an auxiliary observable extracted from Floer data, not as part of the PDE
definition.




                                                          5
Fix a finite-dimensional complex vector space V and a rule that associates to each loop x(t) ∈ M N a
vector U (x) ∈ V , together with components ui in a chosen basis and phases θi . (For numerical work, U
can come from a feature map, Fourier expansion in a chart, or a spectral truncation.)


Define


                              Ψ(x) := ∑ Tij (ui (x) ⊗ uj (x)) ei(θi −θj ) ∈ V ⊗ V .
                                         i,j

One may then define correlators/invariants by pushing Ψ through counts over moduli spaces (e.g.
summing Ψ(x+ ) weighted by Floer trajectory counts). This is compatible with CMFC provided Ψ depends
only on the asymptotics (or is otherwise controlled).




6. Euler characteristic refinement (equation (3) made precise)
If M is a closed oriented Riemannian 4-manifold, the Chern–Gauss–Bonnet theorem gives

                                           1
                              χ(M ) =         ∫ (∣Riem∣2 − 4∣Ric∣2 + R2 ) dvol.
                                         32π 2 M
In CMFC, χ(M ) can be used as: - a scalar parameter weighting observables (e.g. rescaling correlators), or -
an additional grading/filtration constant in the coefficient system.


It is not needed for ∂ 2 = 0; it is an optional refinement layer.




7. Adaptive feedback / learning (equation (5) as parameter
evolution)
Equation (5) is most naturally interpreted as defining a control law that evolves the Floer data
(Tij , γmn , ϕij,t , Gt ) over an external time τ (training time), while Floer theory runs on (s, t) ∈ R × S 1 .

Feedback-driven family of CMFC data

Let


                                         Dτ := (Ht , Jt , T τ , γ τ , ϕτij,t , Gτt )

be a piecewise-smooth family in τ , where the update rule is derived from the scalar functional

                                    N
                        L (t) = ∑ ∇H(uτi ) ⋅ cos(ωi t + ϕi ) ⋅ F τ (t) ⋅ (1 + ετi (t)).
                          τ

                                   i=1

Assume τ ↦ D τ stays within the admissible class for Floer theory and avoids degeneracies except at
isolated continuation events.




                                                             6
Continuation principle

Under standard hypotheses, a homotopy τ ∈ [0, 1] yields continuation maps


                                 Φ0→1 : HF∗CMFC (D0 ) → HF∗CMFC (D1 ),

which are isomorphisms when D τ is a regular admissible homotopy.


This is the mathematically clean way to incorporate “adaptive learning” into Floer-style invariants: learning
updates produce a path of CMFC complexes, related by continuation.




8. Summary (single consistent CMFC definition)
CMFC is the Floer homology of the coupled Hamiltonian system on M N defined by: - baseline Hamiltonian
Ht⊕N , - tensor-weighted coupling potential Φt built from Tij and kernels ϕij,t , - optional self and mode-
coupling corrections (absorbing the intent of (4)), - Hamiltonian perturbation Gt representing deterministic
noise ξ(t), - prime-extended coefficients R encoding multiplicity filtrations.


The resulting operator is the elliptic Floer operator FCMFC on R × S 1 , and the differential counts its rigid
solutions with prime weights.




                                                      7

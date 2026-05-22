---
slug: aspectual-counting-axioms-theorems-dynamics-and-random-aspects-canvas-edition
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "03-case-studies/Aspectual Counting \u2014 Axioms, Theorems, Dynamics, And\
    \ Random Aspects (canvas Edition).md"
  last_synced: '2026-03-20T17:17:20.612012Z'
---

Aspectual Counting — Axioms, Theorems,
Dynamics, and Random Aspects
Arithmetic Metaphysics — canvas packet




0) Core data and notation (ACA)
Let E be a set of tokens. An aspect α on E is an equivalence relation ≈α . Write Uα := E/ ≈α and πα :
E → Uα for the quotient map.

For finite X ⊆ E , the aspectual count is


                                         a(X, α) := ∣πα [X]∣ ∈ N.

An α-automorphism is a function t : E → E such that x ≈α y            ⟺ t(x) ≈α t(y) and the induced tˉ :
Uα → Uα , tˉ([x]) = [t(x)], is bijective. The set of these forms a group Autα (E).

Refinement. For aspects α, β , define β ⪯ α iff ≈β ⊆≈α (β is finer than α). Then there is a canonical
surjection τβ→α : Uβ ↠ Uα with πα = τβ→α ∘ πβ .


Meet/Join of aspects. α ∧ β has relation ≈α ∩ ≈β (finest common refinement). α ∨ β is the equivalence
closure of ≈α ∪ ≈β (coarsest common coarsening).




1) Axioms and basic theorems

Axiom A (Counting-by-quotient)

For all finite X ⊆ E , a(X, α) = ∣πα [X]∣.


Axiom B (Aspect symmetry)

If t ∈ Autα (E), then a(t[X], α) = a(X, α) for all finite X ⊆ E .


Lemma 1 (Aspectual symmetry invariance). Follows immediately from Axiom B / bijectivity of tˉ:


                              πα [t[X]] = tˉ[πα [X]] ⇒ ∣πα [t[X]]∣ = ∣πα [X]∣.

Axiom C (Refinement)

If β ⪯ α, then τβ→α exists as above.




                                                     1
Lemma 2 (Refinement monotonicity). If β ⪯ α, then for finite X ,


                                            a(X, β) ≥ a(X, α).

Proof. τβ→α (πβ [X]) = πα [X] and surjections do not increase cardinality.


Union identity (overlap penalty). With Oα (X, Y ) := {u ∈ Uα : u ∩ X  ∅ &
                                                                         = u ∩ Y  ∅}=
                                                                                     ,


                            a(X ∪ Y , α) = a(X, α) + a(Y , α) − ∣Oα (X, Y )∣.

Bounds via meet/join. For all finite X :


         a(X, α ∧ β) ≥ max{a(X, α), a(X, β)},               a(X, α ∨ β) ≤ min{a(X, α), a(X, β)}.

Extremes. Identity aspect id: x ≈id y      ⟺ x = y ⇒ a(X, id) = ∣X∣. Chaotic aspect ⊤: all tokens
equivalent ⇒ a(X, ⊤) = 1X       . =∅



2) Measure-valued aspectual counting (infinite sets)
Let (E, Σ) be measurable. Equip Uα with the quotient σ -algebra Σα = {S ⊆ Uα : πα−1 (S) ∈ Σ}.


2.1 Pure unit-count on the quotient

Counting measure να on (Uα , Σα ):


                                   a∞ (X, α) := να (πα [X]) ∈ N ∪ {∞}.

Invariance and refinement monotonicity carry over verbatim.


2.2 Hit measure relative to a base measure

Given σ -finite μ on E , push forward: μα = (πα )∗ μ. Define


   a^{\mathrm{hit}}_\mu(X,\alpha):=\mu_\alpha(\pi_\alpha[X])=\mu\big(\text{KATEX51-saturation of }X\big).
If t is α-automorphic and μ-preserving, invariance holds. If β ⪯ α and quotient measures are consistent
(μα = (τβ→α )∗ μβ ), then refinement monotonicity holds.


2.3 Fiberwise valuations via disintegration

When μ disintegrates along πα , μ = ∫ μu dμα (u). For monotone φ : [0, ∞) → [0, ∞) with φ(0) = 0,
define


                                     Aα,φ (X) := ∫      φ(μu (X)) dηα (u),
                                                   Uα




                                                        2
with ηα = μα (mass-weighted) or να (unit-weighted). Special cases recover hit-counts and total mass.




3) Dynamic aspects (time/context index)
Let (C, ≤) index contexts. A dynamic aspect family is c ↦ αc . Two regimes:


(Refining over time) If c1 ≤ c2 ⇒ αc2 ⪯ αc1 , then for any X , a∞ (X, αc ) is nondecreasing in c.


(Coarsening over time) If c1 ≤ c2 ⇒ αc1 ⪯ αc2 , then a∞ (X, αc ) is nonincreasing.


For finite E , if only finitely many merges/splits occur on compact intervals, c ↦ a(X, αc ) is piecewise-
constant (càdlàg). Dynamic symmetries tc ∈ Autαc (E) give pointwise invariance.




4) Categorical wrapper (initiality of the quotient)
Let Quot(E) have objects quotients π : E → U and morphisms h : Uα → Uβ with h ∘ πα = πβ (so β
coarsens α).


Define Invα : objects (V , f ) with x ≈α y ⇒ f (x) = f (y); morphisms m : (V , f ) → (W , g) satisfying
g = m ∘ f.

Theorem (Initiality). (Uα , πα ) is initial in Invα . For any (V , f ) there is a unique fˉ : Uα → V with f = fˉ ∘
πα .

Meets/joins as limits/colimits. α ∧ β is the pullback partition; α ∨ β the pushout (equivalence closure of
the union).




5) Random aspects (distributions over partitions)
A random aspect is a random equivalence relation (partition) Π on E . For finite E and X ⊆ E , let


                                  KX := ∣{blocks of Π that intersect X}∣.

5.1 Paintbox (Kingman) representation

If assignments are i.i.d. from a probability vector (pi )i≥1 plus dust mass p0 ∈ [0, 1] (each dust draw forms a
fresh singleton), then for ∣X∣ = m:


                                   E[KX ] = m p0 + ∑ (1 − (1 − pi )m ).
                                                        i≥1




                                                        3
For the purely atomic case (p0 = 0),

     Var(KX ) = ∑ (1 − (1 − pi )m )(1 − pi )m + 2 ∑ ((1 − pi − pj )m − (1 − pi )m (1 − pj )m ).
                       i≥1                                  i<j

(For p0 > 0, the same covariance structure applies among atoms; dust contributes an additional binomial
component whose moments can be added via the law of total variance.)


5.2 Ewens/CRP (θ > 0)

For the Ewens sampling formula (Chinese Restaurant Process with concentration θ ), the number of blocks
                                                                             m
among m draws has the independent Bernoulli representation Km = ∑i=1 Bi with P(Bi = 1) = θ/(θ +
i − 1). Hence

                             m                                    m
                               θ                                        θ          θ
                E[Km ] = ∑         ,            Var(Km ) = ∑                (1 −       ),
                         i=1
                             θ+i−1                                i=1
                                                                      θ+i−1      θ+i−1

with asymptotics E[Km ] ∼ θ log m, Var(Km ) ∼ θ log m.


(These formulas give the expected/typical aspectual count when the aspect itself is random and exchangeable.)




6) Tiny gallery of examples

(a) Cells on R

Aspect αcell : x ≈ y    ⟺ ⌊x⌋ = ⌊y⌋. For X = [0, 2.3):


             a∞ (X, αcell ) = 3,    ahit
                                     Leb (X, αcell ) = 3,    ∫ μu (X) dμα (u) = Leb(X) = 2.3.


(b) Graph-connected components

Let E be vertices of a graph G. Aspect αconn : vertices equivalent iff connected in G. For X ⊆ V , a(X,
\alpha_\text{conn}}) counts the number of connected components touched by X . Refinement monotonicity
matches the effect of splitting/merging components.


(c) Time-varying partitions (households)

Tokens are persons; αt groups co-residents at time t. Mergers/splits of households make t ↦ a(X, αt )
piecewise-constant; refining vs coarsening regimes model gaining vs losing information.




7) References (selected)
      • S. Mac Lane, Categories for the Working Mathematician, 2nd ed., Springer, 1998.




                                                       4
   • V. I. Bogachev, Measure Theory, Vol. I–II, Springer, 2007. (quotients, disintegration)
   • G. B. Folland, Real Analysis: Modern Techniques and Their Applications, 2nd ed., Wiley, 1999. (quotient
     σ -algebras, pushforward)
   • J. F. C. Kingman, “The Representation of Partition Structures,” J. London Math. Soc. (2) 18 (1978), 374–
     380. (paintbox)
   • J. Pitman, Combinatorial Stochastic Processes, Springer LNM 1875, 2006. (Ewens, exchangeable
     partitions)
   • O. Kallenberg, Foundations of Modern Probability, 2nd ed., Springer, 2002. (regular conditional
     probabilities, disintegration)
   • L. Lovász, Large Networks and Graph Limits, AMS, 2012. (graph components as partitions)




Notes

   • All proofs are short and rely on quotients/partitions and functorial pushforwards. Random-aspect
     formulas are standard in occupancy/paintbox representations. For dust-bearing models,
     expectations decompose neatly (each dust draw creates a singleton block); variances can be
     combined via the law of total variance.




                                                     5

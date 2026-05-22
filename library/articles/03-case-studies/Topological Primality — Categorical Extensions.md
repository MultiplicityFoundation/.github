---
slug: topological-primality-categorical-extensions
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "03-case-studies/Topological Primality \u2014 Categorical Extensions.md"
  last_synced: '2026-03-20T17:17:21.715321Z'
---

Topological Primality — Categorical Extensions
(Formal Canvas)
0. Goal
Formalize “Topological Primality” by encoding prime-factor structure of N+ as categorical/topos-theoretic
geometry. The guiding principle is:


        Arithmetic locality = prime-factor constraints.


We replace point-set topology on integers with a site built from divisibility, then define sheaves,
(co)homology-like invariants, and categorical “retractions” expressing prime-set structure.




1. Divisibility category (the base site)
       • Objects: positive integers n ∈ N+ .
       • Morphisms: a unique arrow m → n iff m ∣ n.

Equivalently, Div is the poset (N+ , ∣) viewed as a category.


1.2 Principal up-sets

For n ∈ N+ , define the principal upset


$$ \uparrow n:={m\in\mathbb N^+: n\mid m}. $$


These are the categorical avatars of “basic opens”: they encode all integers satisfying at least the prime-
valuation constraints of n.




2. Prime-valuation geometry

2.1 Valuation vector embedding

Let vp (n) denote the exponent of prime p in n. Define


$$ \nu:\mathbb N^+\to\bigoplus_{p\in\mathbb P}\mathbb N,\qquad \nu(n)=(v_p(n))_p. $$


Then


$$ m\mid n\iff v_p(m)\le v_p(n)\ \forall p. $$




                                                      1
Thus Div is equivalent to the finite-support product poset ⨁p N with coordinatewise order.


2.2 Prime-support regions (multiplicity-aware)

For finite S ⊂ P and multi-index k = (kp )p∈S ∈ NS , define


$$ U_S^{\mathbf k}:={n\in\mathbb N^+:\forall p\in S,\ v_p(n)\ge k_p}. $$


Each USk is an upset in (N+ , ∣), hence corresponds to a sieve on Div.




3. Grothendieck topologies (prime local generation)

3.1 Coverage by unions of principal up-sets

A family {ni → n}i is a cover of n if


$$ \uparrow n\;=\;\bigcup_i \uparrow n_i. $$


Equivalently: for every m with n ∣ m, there exists i such that ni ∣ m.


This defines a Grothendieck topology J∪ on Div (posetal “union coverage”).


3.2 Prime-generated refinement (optional)

To enforce explicit prime locality, restrict to covers where each ni refines n by controlled prime-power
increments, e.g.


$$ n_i=n\cdot \prod_{p\in S_i} p^{t_{i,p}}, $$


for finite Si and exponents ti,p ≥ 0. Call the resulting topology Jprime .




4. Sheaves and “prime cohomology”

4.1 Presheaves

A presheaf of sets/abelian groups is a functor


$$ \mathcal F:\mathbf{Div}^{op}\to\mathbf{Set}\ \text{or}\ \mathbf{Ab}. $$


      • F(n) is the data visible at “resolution” n.
      • If m ∣ n, the unique arrow m → n induces a restriction F(n) → F(m).




                                                        2
4.2 Sheaves

A presheaf F is a sheaf (for Jprime ) if for every covering family {ni → n}:


      • sections over n are determined uniquely by compatible sections over each ni ,
      • with compatibility enforced on overlaps (via pullbacks in the poset, typically lcms).

4.3 Global sections and derived invariants

Global sections are


$$ \Gamma(\mathcal F)=\mathcal F(1), $$


since 1 ∣ n for all n so 1 is terminal in Div.


Define “prime cohomology” as derived functors in the topos


$$ H^i(\mathbf{Div},J_{\mathrm{prime}};\mathcal F):=R^i\Gamma(\mathcal F). $$


         Note: Because Div is filtered, many constant-coefficient cohomologies may vanish in
         degrees > 0. Prime-sensitive variants below address this.




5. Prime-set deformation retracts as adjunctions/(co)monads

5.1 Squarefree coreflection via radical

Define the radical (squarefree part)


$$ \mathrm{rad}(n)=\prod_{p\mid n}p. $$


Let Sqf ⊂ Div be the full subcategory of squarefree integers.


There is an inclusion i : Sqf ↪ Div and a functor


$$ \mathrm{rad}:\mathbf{Div}\to\mathbf{Sqf} $$


with rad(n) ∣ n. This yields an idempotent closure/interior operator on the poset, categorically expressible
as an idempotent (co)monad (variance depending).


Interpretation: “retracting” integers to their prime-sets is better behaved via Sqf than via P alone.


5.2 Support functor to finite prime sets

Define




                                                        3
$$ \mathrm{Supp}(n)={p\in\mathbb P: p\mid n}\in\mathbf{FinSet}. $$


Then Supp(mn) = Supp(m) ∪ Supp(n). This is a monoid map into (Pfin (P), ∪).




6. Non-Archimedean enrichment (optional)

6.1 Support-distance and multiplicity-distance

Examples of prime-sensitive pseudometrics:


      • Support overlap metric

$$ d_{\cap}(m,n)=\frac{1}{1+|\mathrm{Supp}(m)\cap\mathrm{Supp}(n)|}. $$


      • Multiplicity ultrametric-like form (heuristic)

$$ d_{\nu}(m,n)=\prod_{p\in\mathbb P} p^{-|v_p(m)-v_p(n)|}. $$


These can be used to enrich Div or to define enriched sheaves / continuity constraints.




7. Avoiding triviality: prime-sensitive invariants

7.1 Truncated sites

Define subsites to prevent global filtering from collapsing invariants:

                            (≤N )
      • Prime cutoff: Div           : objects with primes ≤ N .
                                (≤K)
      • Valuation bound: Div            : objects with ∑p vp (n) ≤ K .
      • Fixed support: DivS : primes restricted to a finite set S .

Study cohomology on these finite/controlled sites and then pass to limits as N → ∞, etc.


7.2 Equivariant / action-based constructions

Let (N+ , ⋅) act on Div by endofunctors


$$ T_k(n)=kn. $$


This induces an action on Sh(Div, Jprime ). Prime-sensitive invariants may be defined via fixed points or
derived limits, e.g.


$$ \Gamma(\mathcal F)^{\mathbb N^+},\qquad \mathrm{holim}_{k}\,\Gamma(T_k^*\mathcal F). $$




                                                           4
8. Predictions / expected outcomes
   1. Squarefree reduction is canonical: Sqf behaves as a coreflective “prime-set skeleton,” allowing
     functorial projection rad without arbitrary choices.
                                                                         (≤N )
   2. Truncation reveals structure: cohomological invariants on Div              should show growth patterns
     reflecting prime distribution in [2, N ].
   3. Equivariant invariants detect primes: invariants built from the action of Tp (prime multiplication)
     should separate prime-power strata from mixed composites.




9. Fast validation program (minimal)
   1. Choose a Grothendieck topology J∪ or Jprime and characterize sheaves via gluing along lcms.
                                                                                  (≤N )
   2. Compute cohomology for a small library of coefficient sheaves on Div                for N = 2, 3, 5, 7.
   3. Test filtered-triviality: check whether constant sheaves have vanishing higher cohomology; if so,
      pivot to truncated/equivariant invariants.
   4. Implement toy computations: build the Čech complex for covers generated by prime-power
      refinements and measure nontriviality.




10. Next formal tasks
    • (A) Pick a canonical prime-generated Grothendieck topology J_prime and prove the Grothendieck
      axioms.
    • (B) Describe points of the topos Sh(Div, J_prime) (i.e., geometric morphisms from Set).
    • (C) Define a prime-sensitive coefficient system F (e.g., valuation-weighted or Mobius-twisted) and
      compute low-degree invariants.




11. References (selected)

Topos theory, sites, and sheaves

    • M. Artin, A. Grothendieck, and J.-L. Verdier (eds.). Theorie des Topos et Cohomologie Etale des Schemas
      (SGA 4), Lecture Notes in Mathematics, Springer, 1972.
    • M. Kashiwara and P. Schapira. Categories and Sheaves, Grundlehren der mathematischen
      Wissenschaften 332, Springer, 2006.
    • S. Mac Lane. Categories for the Working Mathematician (2nd ed.), Graduate Texts in Mathematics 5,
      Springer, 1998.
    • S. Mac Lane and I. Moerdijk. Sheaves in Geometry and Logic: A First Introduction to Topos Theory,
      Springer, 1994.
    • P. T. Johnstone. Sketches of an Elephant: A Topos Theory Compendium, Vol. 1, Oxford Logic Guides,
      Oxford University Press, 2002.




                                                     5
Posets, Alexandroff spaces, and finite-space homotopy

     • M. C. McCord. “Singular homology groups and homotopy groups of finite topological spaces,” Duke
       Mathematical Journal 33(3), 465–474, 1966.
     • J. A. Barmak. Algebraic Topology of Finite Topological Spaces and Applications, Lecture Notes in
       Mathematics 2032, Springer, 2011.

Filtered categories and contractibility

     • D. Quillen. “Higher algebraic K-theory I,” in Algebraic K-Theory I: Higher K-Theories, Lecture Notes in
       Mathematics 341, Springer, 1973. (Includes the fact that filtered categories have contractible
       classifying space.)

Enrichment and Lawvere-style metrics

     • G. M. Kelly. Basic Concepts of Enriched Category Theory, London Mathematical Society Lecture Note
       Series 64, Cambridge University Press, 1982.
     • F. W. Lawvere. “Metric spaces, generalized logic, and closed categories,” Rendiconti del Seminario
       Matematico e Fisico di Milano 43, 135–166, 1973.

Non-Archimedean / ultrametric background

     • F. Q. Gouvea. p-adic Numbers: An Introduction (2nd ed.), Universitext, Springer, 1997.
     • W. H. Schikhof. Ultrametric Calculus: An Introduction to p-adic Analysis, Cambridge Studies in Advanced
       Mathematics 4, Cambridge University Press, 1984.

Arithmetic-geometry interface around the multiplicative monoid of positive integers

     • A. Connes and C. Consani. “The Arithmetic Site,” Comptes Rendus Mathematique 352(12), 971–975,
       2014. (See also the 2014 arXiv preprint with the same title.)

Classical scheme-theoretic background (comparison target)

     • R. Hartshorne. Algebraic Geometry, Graduate Texts in Mathematics 52, Springer, 1977.

Absolute / F1 / monoid-scheme context (optional comparison)

     • A. Deitmar. “Schemes over F1,” arXiv\:math/0404185 (versions through 2005).

Citizen Gardens © 2025 CC-NC-ND 4.0




                                                       6

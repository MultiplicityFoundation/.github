---
slug: where-do-negatives-come-from-operational-closure-completion-and-baselines
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "03-case-studies/Where Do Negatives Come From_ \u2014 Operational Closure,\
    \ Completion, And Baselines.md"
  last_synced: '2026-03-20T17:17:21.006927Z'
---

Where Do Negatives Come From?
Operational Closure, Group Completion, and Baselines

Abstract

Negative quantities are philosophically puzzling: they are indispensable in science and accounting, yet often
seem metaphysically suspicious as “less-than-nothing.” This puzzle dissolves when we shift attention from
ontology to practice. A negative is not an entity but a functional role within a typed operational system
that supports netting to a privileged neutral state. Formally, genuine negatives occur exactly when a
system’s states form (or are canonically extended to) an abelian group under its composition rule, so that
each state x has an inverse −x with x + (−x) = 0. This framework explains both the presence and the
emergence of negatives: some domains contain inverses intrinsically (displacements, charge), while others
acquire them when practices introduce deficits or obligations, modeled by Grothendieck group
completion (e.g., inventory with backorders; double-entry bookkeeping). Baseline-relativity is captured by
torsor structure, where inverses live in differences rather than absolute states. We distinguish directed
deficits from mere absences and derive testable predictions about sign reasoning under different framings.


Keywords: negative numbers; abelian groups; Grothendieck group; group completion; torsors; affine
space; measurement scales; accounting; cognition.




1. The problem
Negatives often invite a pseudo-problem: do negative numbers (or “negative quantities”) exist, or are they
merely absences? The everyday use of debt, elevation below sea level, electric charge, and displacement
suggests that “negative” is not simple nonexistence. But metaphysical reification (“negative being”) can
obscure more than it clarifies.


Thesis (quietist/pragmatist): “Existence” is the wrong predicate. The right question is structural and
operational:


       Does this practice support cancellation (netting) to a privileged neutral state?


If yes, then “−x” is as real—i.e., as rule-governed and inference-supporting—as “+x” within that practice.




2. The insight: operational closure under inversion
A minus sign on a page does not guarantee a genuine negative. Genuine negatives belong to systems
where practitioners can offset states to reach a neutral.




                                                     1
2.1 The netting test

A domain instantiates directed negatives exactly when it supports a robust “offset” rule:


      • For a state x, there is an opposed state −x
      • Composing them yields neutrality: x ⊕ (−x) = 0
      • Offsetting behaves consistently (associativity/commutativity in the relevant practice)

This is the operational signature of additive inverses.




3. Formal core

3.1 Typed operational systems

A typed operational system is a triple


$$ \mathcal S_T = (S_T,\; \oplus,\; 0) $$


where:


      • ST is the set of admissible states of type T
      • ⊕ is a (practice-defined) composition rule
      • 0 is a privileged neutral (baseline) state

         Typing matters: cancellation only makes sense within the same type (−$5 cancels +$5, not
         +5 apples).

3.2 Genuine negatives (ideal case): abelian groups

ST supports genuine negatives iff (ST , ⊕, 0) is an abelian group.

Equivalently, for every x ∈ ST there exists −x ∈ ST such that:


$$ x \oplus (-x) = 0. $$


Define subtraction as addition with inverse: x ⊖ y := x ⊕ (−y).


Interpretation: “Directedness” is not metaphysical force; it is the operational fact that states come with
systematic counter-states enabling netting.


3.3 Relativity case: torsors (differences are invertible)

Many “absolute” state spaces have no canonical origin. What is operationally well-defined are differences.




                                                          2
A set A is a torsor over a group (G, +, 0) if G acts freely and transitively on A. Intuitively: a torsor is a
“group that forgot its identity element.”


      • Absolute positions form a torsor A over the displacement group G ≅ (Rn , +)
      • For a, b ∈ A, the “difference” b − a ∈ G is defined and is invertible
      • Choosing a baseline a0 ∈ A coordinatizes points by a ↦ (a − a0 ) ∈ G

Moral: coordinate negatives (e.g., “left of the origin”) are baseline artifacts; inversional negatives live in the
difference group.


3.4 Emergence case: monoids and Grothendieck completion

Some practices begin with a commutative monoid (M , ⊕, 0) (no inverses): cash-only tallies, inventories
without backorders, counts of resources.


When the practice introduces obligations/deficits/backorders, it effectively extends M to a group: the
Grothendieck group completion G(M ).


      • Elements of G(M ) behave like formal differences (often written [a, b])
      • They enforce [a, b] + [c, d] = [a ⊕ c, b ⊕ d]
      • [a, b] = 0 iff a = b (in cancellative settings)

Interpretive gloss: negative inventory is the internalization of “would need to be supplied” into the state
space.


Lemma (injectivity criterion; proof sketch)

If M is cancellative and commutative, the natural map M → G(M ) is injective. (Cancellation prevents
different “positive” states from collapsing under completion.)




4. Algebraic taxonomy of domains (Table 1)

                                                                            Where
  Domain                  “States”     Composition        Structure                            Minus means…
                                                                            inverses live?

                                                                                               not defined in-
  Cash-only tally         N            +                  Monoid            nowhere
                                                                                               domain

  Double-entry net                                                                             inverse /
                          Z            +                  Abelian group     in states
  balance                                                                                      cancellation

  Inventory (no
                          N            +                  Monoid            nowhere            not licensed
  backorders)

  Inventory (with         G(N) ≅                          Group             in completed       engineered
                                       +
  backorders)             Z                               completion        states             inverse




                                                          3
                                                                             Where
  Domain                 “States”      Composition       Structure                              Minus means…
                                                                             inverses live?

                                       (no canonical     Torsor over                            coordinate
  Absolute position      A                                                   in differences
                                       +)                (Rn , +)                               choice

                                                                                                inverse /
  Displacement           Rn            +                 Abelian group       in states
                                                                                                cancellation




5. Paradigm cases

5.1 Debt and credit (the canonical netting practice)

Model net balance as x ∈ (Z, +) or (R, +). A +5 credit and −5 debt satisfy:


$$ (+5)+(-5)=0. $$


Multi-agent transfer naturally yields invariants: (xA , xB ) ↦ (xA − 5, xB + 5) preserves xA + xB in a
closed system.


5.2 Inventory and backorders (emergence via completion)

      • Without backorders: inventory is a monoid (N, +)
      • Allowing backorders adds deficits, producing a group-like bookkeeping domain isomorphic to Z

This is a clean illustration that negatives can be engineered into a practice when netting is operationally
required.


5.3 Displacement vs absolute position (torsor vs group)

      • Absolute positions (without a distinguished origin) form a torsor A
      • Displacements form a group (Rn , +)
      • “Negative position” is not intrinsic; it arises only after choosing coordinates (a baseline point + axis)




6. Demarcation from mere absence
“Mere absences” (e.g., “the absence of unicorns”) typically fail the netting test:


      • no agreed composition ⊕
      • no privileged neutral 0
      • no operationally meaningful inverse −x

By contrast, directed deficits (debt, backorders, charges) are embedded in systems with explicit netting
rules, conservation constraints, and normative or interactional governance.




                                                        4
7. Not every minus sign indicates a genuine negative
(measurement sidebar)
Many measurement systems are affine (interval scales): the zero point is conventional, and meaningful
structure lives in differences.


      • Celsius readings allow negatives because the origin is chosen by convention.
      • What is operationally stable is the temperature difference ΔT , which supports additive inverses in
       (R, +).

This aligns with measurement theory: interval scales are invariant under positive affine transformations
x ↦ ax + b (Stevens).

Moral: genuine inversional negativity belongs to the operational algebra of the relevant quantity (often
differences), not to the glyph “−.”




8. Philosophical payoff: dissolving “Do negatives exist?”
This framework resolves a longstanding pseudo-problem.


      • Asking whether “−x exists” abstracts away from the practice that gives “−x” content.
      • Within a practice whose state space is (or is completed to) a group, “−x” is a legitimate,
       indispensable role.

       Negatives are not discovered in the world; they are engineered into practices that
       require netting.


This is quietist about metaphysical “negative being,” but not deflationary about mathematics: it explains
why negatives are indispensable, stable, and transferable across domains—because many practices share
the same algebraic requirements.




9. Predictions and validation

9.1 Conceptual audit (fast)

Survey domains and classify them as group / torsor / monoid / completion, recording:


      • states, composition, baseline, inverse availability
      • whether “minus” is inversional (group) or coordinate/affine (torsor chart)




                                                       5
9.2 Formal validation (fast)

Prove representation results of the form:


     • If a practice supports netting with associativity/commutativity and inverses, it is modeled by an
       abelian group.
     • If a practice is monoidal but cancellative, group completion is canonical and explains deficit-states.
     • If a practice admits only differences, torsor structure captures baseline relativity.

9.3 Cognitive prediction (cheap experiment)

People should reason more accurately and quickly about negatives when framed in netting practices (debt/
credit, displacement) than when framed as bare symbol manipulation or “mere absence.”


A simple design:


     • Same algebraic task (e.g., solve x − 5 = 2)
     • Framed as: (A) debt, (B) displacement, (C) pure symbols, (D) “absence/hole” metaphor
     • Measure accuracy, time, and systematic sign errors




10. Optional enrichments (when you do get vectors)
Vector spaces (or ordered groups, cones, etc.) are enrichments, not the foundation.


     • If the domain supports meaningful scalar action (e.g., “triple the debt”), then the abelian group
       becomes a Z-module (often extendable to R-vector space for continuous quantities).
     • If the domain supports a partial order (e.g., ‘at least as good as’), you may add ordered-group
       structure.

These additions are domain-dependent; the core litmus test remains operational inversion (or its canonical
emergence via completion).




References (selected)
Operational negatives, history, and interpretation

     • Mumford, D. (2010). What’s so baffling about negative numbers? — a cross-cultural comparison. In
       Studies in the History of Indian Mathematics (pp. 113–143). Springer.
     • Shutler, P. M. E. (2017). A symbolical approach to negative numbers. The Mathematics Enthusiast, 14(1),
       207–240.

Cognition and learning of negative numbers

     • Kilhamn, C. (2011). Making Sense of Negative Numbers (Doctoral thesis). University of Gothenburg.




                                                       6
     • Young, L. K., & Booth, J. L. (2015). Student magnitude knowledge of negative numbers. Journal of
       Numerical Cognition, 1(1), 38–55. https://doi.org/10.5964/jnc.v1i1.7
     • Vlassis, J. (2022). The role of algebraic thinking in dealing with negative numbers. ZDM – Mathematics
       Education, 54(6), 1243–1255. https://doi.org/10.1007/s11858-022-01402-1

Measurement theory and affine scales

     • Stevens, S. S. (1946). On the theory of scales of measurement. Science, 103(2684), 677–680. https://
       doi.org/10.1126/science.103.2684.677
     • Krantz, D. H., Luce, R. D., Suppes, P., & Tversky, A. (1971). Foundations of Measurement, Vol. I: Additive
       and Polynomial Representations. Academic Press.

Group completion / Grothendieck construction

     • Weibel, C. A. (2013). The K-book: An introduction to algebraic K-theory. American Mathematical Society
       (Graduate Studies in Mathematics).
     • nLab authors. (2023). Grothendieck group of a commutative monoid. nLab.

Torsors and affine spaces

     • Riehl, E. (2016). Category Theory in Context. Dover (freely available draft editions circulate online).
     • Serre, J.-P. (1997). Galois Cohomology (English translation; original French 1964). Springer.
     • Vistoli, A. (2005). Grothendieck topologies, fibered categories, and descent theory. In Fantechi et al.
       (Eds.), Fundamental Algebraic Geometry (AMS).
     • Skorobogatov, A. (2001). Torsors and Rational Points. Cambridge University Press.

Accounting and the emergence of netting practices

     • Pacioli, L. (1494). Summa de arithmetica, geometria, proportioni et proportionalita. Venice: Paganino
       Paganini.
     • Sangster, A. (2016). The genesis of double entry bookkeeping. The Accounting Review, 91(1), 299–315.
       https://doi.org/10.2308/accr-51115
     • Mattessich, R. (2005). A concise history of analytical accounting: examining the use of mathematical
       notions in our discipline. De Computis (Spanish Journal of Accounting History), 2, 123–167.



Citizen Gardens © 2025 CC-NC-ND 4.0




                                                        7

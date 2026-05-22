---
slug: multiplicity-theory-v0
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Multiplicity Theory V0.md
  last_synced: '2026-03-20T17:17:21.453358Z'
---

Multiplicity Theory v0.2: A Self-Correcting
Functorial Framework
Abstract
We formalize Multiplicity as a functorial, semiring-valued invariant on a symmetric monoidal (∞, 1)-
category endowed with descent and a domain-specific self-correction operator. The framework recovers
classical algebraic–geometric multiplicities, extends to spectral and network settings, and provides stability
windows under perturbations.




1. Core Formalization
1.1 Minimal Object & Target
Let: - (C, ⊕, ⊗) be a symmetric monoidal (∞, 1)-category with a Grothendieck topology J . - Rig be the 2-
category of commutative semirings and semiring functors. - Mult : (C, ⊕, ⊗) → (Rig, +, ⋅) be a lax
symmetric monoidal functor, with base-change natural in objects. Write m(X) ∈ MX for its value.


1.2 Axioms (Essential)
A1 (Functoriality): Mult(g ∘ f ) = Mult(g) ∘ Mult(f ).


A2 (Semiring Additivity/Multiplicativity):


                   m(X ⊕ Y ) = m(X) + m(Y ),              m(X ⊗ Y ) = m(X) ⋅ m(Y ).

A3 (Descent): Mult is a J -sheaf of semirings (Čech descent holds for admissible covers).


A4 (Invariance): Preserved under relevant equivalences (isomorphism, derived, Morita, homotopy).


A5 (Normalization): Restricts to classical multiplicities on canonical subcategories (Hilbert–Samuel/J, Serre/
derived intersection, tropical stable intersections, spectral degeneracy, microstate count in statistical
mechanics).


A6 (Derived Additivity): For nontransverse intersections/gluing, A2 holds after derived correction (Tor/Ext
terms or obstruction-theoretic defects).


A7 (Self-Correction): There exists a domain-specific update operator U and a metric d with contractivity:


                              d(mt+1 , m⋆ ) ≤ κ d(mt , m⋆ ),       0 ≤ κ < 1.



                                                      1
1.3 Exclusion Principle
An admissible Mult must be: 1. Integer-valued on compact discrete presentations. 2. Localizable
(computable from a cover with descent). 3. Stable under the domain’s equivalence notion.


This excludes Shannon/von Neumann entropy as a universal substitute (they generally fail (1) and/or (3)
across categories).




2. Self-Correction: Operators & Stability Windows
We detail objects, multiplicity, update law, and stability for three anchor domains.


2.1 Quantum/Spectral (Q)
     • Object: Self-adjoint H with spectral projectors {Pλ }.
     • Multiplicity: m(H) = {(λ, rank Pλ )} or cluster-multiplicity after gap-based clustering.
     • Update: H ↦ H + E (bounded Hermitian perturbation) or CPTP channel E .
     • Stability (Davis–Kahan): If ∥E∥ < 12 gap, then projector angles satisfy

                                                                ∥E∥
                                            sin Θ(P , P ′ ) ≤       =: κ < 1,
                                                                gap
       and the cluster multiplicity is locally constant.

Metric choice: principal-angle metric on invariant subspaces; cluster stability judged by rank constancy
within the gap window.


2.2 Algebraic/AG (A)
     • Object: Noetherian local pair (R, m; I) (or maps X → Y ).
     • Multiplicity: Hilbert–Samuel eI (M ); derived intersection multiplicity via ∑(−1)i length Tori .
     • Update: Deformation to the normal cone; flat base change.
     • Stability: Upper semicontinuity of e in flat families ⇒ et+1 ≤ et for flattening updates (one-sided
       contraction in the partial order).

Metric choice: partial order ≥ on multiplicities; optionally ∣et+1 − e⋆ ∣ in regimes where equality is
expected.


2.3 Graphs/Networks (G)
     • Object: Finite graph G on n vertices.
     • Multiplicity: Coefficient vector a(G) = (a0 , … , am ) of the reliability polynomial RG (p) =
       ∑k ak pk (1 − p)m−k .
     • Update: Deletion–contraction recursion: RG = pRG/e + (1 − p)RG∖e ; edit operators add/delete
       edges.



                                                           2
      • Stability: Coefficients obey submodularity; under ≤ r edge edits,

                                           ∥a(G) − a(G′ )∥1 ≤ c r nO(1) .

Metric choice: ℓ1 distance on coefficient vectors; log-summaries for robustness proxies.




3. Universal Constructions
Multiplicity Sheaf. A presheaf M : O(X)op → Rig that satisfies descent, gluing local multiplicities into
m(X).

Multiplicity Monad. A monad T : C → C encoding branching/superposition; the Kleisli category composes
multiplicity-bearing processes, compatible with A2 and A3.




4. Explicit Examples & Counterexamples
    1. Monomial Ideals (toy algebraic backend): in k[x, y] at m = (x, y), I = (xa , y b ) has m =
       em (R/I) = ab. Verifies A2 across random (a, b).
    2. Derived Additivity Toy: C1 : y − x2 , C2 : y intersect nontransversely at 0. Naive additivity fails; Tor-
       corrected multiplicity satisfies A6.
    3. Spectral Robustness: H0 = diag(0, 0, Δ) with perturbation εE . The 0-eigenspace multiplicity is
       stable for ε < Δ/2 and changes at gap closure.
    4. Graph Non-Entropy Witness: Two 8-vertex graphs with the same degree sequence yield distinct
       reliability coefficients; m distinguishes them while degree-entropy does not.




5. Micro-Theorems (Targets)
Thm 1 (Descent). If X = U ∪ V is a J -cover with derived-transverse U ∩ V , then


                                  m(X) = m(U ) + m(V ) − m(U ∩ V ).

Thm 2 (Monoidal). For independent systems X, Y , m(X ⊗ Y ) = m(X) ⋅ m(Y ).


Thm 3 (Spectral Stability Window). Let H have a spectral cluster separated by gap g . If ∥E∥ < g/2,
cluster multiplicity is invariant and projector distance contracts by factor ∥E∥/g .


Prop 4 (Graph Lipschitz). If G′ differs by ≤ r edge edits, then ∥a(G) − a(G′ )∥1 ≤ c r nO(1) .


Prop 5 (Upper Semicontinuity). In flat families, Hilbert–Samuel multiplicity is upper semicontinuous;
flattening updates are contractive in the partial order ≥.




                                                       3
6. API Skeleton (Language-Agnostic)

  class Mult[Value: Semiring]:
      value: Value
      def op_sum(a: "Mult", b: "Mult") -> "Mult": ...
      def op_prod(a: "Mult", b: "Mult") -> "Mult": ...
      def transport(self, f: Morphism) -> "Mult": ... # functorial transport

  interface Backend[X, Value: Semiring]:
      def compute(x: X) -> Mult[Value]
      def local(self, U: CoverOpen[X]) -> Mult[Value]                   # optional, for sheaf
  gluing

  namespace backends:
      algebraic: Backend[(R, m; I), N]
      tropical: Backend[TropicalCycle, N]
      spectral: Backend[Matrix | Hamiltonian, N]
      graphs:   Backend[Graph, PolyRing]

  module update:
        def spectral_step(H: Matrix, E: Matrix) -> Mult[N]: ...
        def deform_step(instance, deformation) -> Mult[N]: ...
        def graph_step(G: Graph, edit) -> Mult[PolyRing]: ...




7. Experiments & Datasets (Week‑1 Plan)
Algebraic: Grid (a, b) ∈ {2..8}2 for I = (xa , y b ); verify A2/A3; random deformations y b ↦ y b + xc .
Spectral: Random Hermitian 3 × 3 and 6 × 6 with planted gaps; sweep ∥E∥ to map stability windows.
Graphs: ER(n, p) and BA(n, m) with n = 50..300; correlate percolation threshold with (i) degree entropy, (ii)
algebraic connectivity, (iii) log of reliability coefficients.


Success criteria: Axioms hold on toy cases; one domain where m predicts behavior that entropy/rank miss;
reproducible notebooks demonstrate stability.




8. Deliverables & Links
Paper skeleton (LaTeX):
- multiplicity_v0_2.tex




                                                            4
Code scaffold ( multiplicity_core ):
- README.md
- pyproject.toml
- src/multiplicity_core
- tests


Demos (Jupyter):
- spectral_stability.ipynb
- graph_reliability_vs_robustness.ipynb




9. Roadmap (Next 2–3 Weeks)
     1. Prove Thm 1–3 on restricted settings; add counterexamples clarifying A6 necessity.
     2. Implement transport along morphisms (functoriality) for each backend.
     3. Add tropical backend (stable intersections).
     4. Integrate spectral gap detection and explicit Davis–Kahan bounds visualization.
     5. Prepare preprint with toy benchmarks and public repo.




10. Open Problems & Extensions
      • Characterize the broadest class of semirings M admitting A1–A7 simultaneously.
      • Relate Mult to K -theory / λ-rings; identify when m refines ranks/Chern characters.
      • Extend to probabilistic sheaves and Wasserstein contractivity for stochastic updates.
      • Noncommutative geometry: Morita-invariant multiplicities beyond classical spectral degeneracy.
      • Data-driven multiplicities: learnable base-change functors respecting A1–A4.




                                                     5

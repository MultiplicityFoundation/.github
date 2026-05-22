---
slug: exotic-spheres-multiplicity-topology-prime-indexed-cobordism-invariants
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "03-case-studies/Exotic Spheres & Multiplicity Topology \u2014 Prime-indexed\
    \ Cobordism Invariants.md"
  last_synced: '2026-03-20T17:17:20.840212Z'
---

Exotic Spheres & Multiplicity Topology
0. Executive idea
We construct prime-indexed cobordism invariants for exotic spheres by translating surgery/handle data
into recursive multiplicity matrices and then extracting prime-tier spectral signatures using multiplicity-
style projectors. The guiding principle is:


         Smooth structure obstructions (exoticness) should appear as prime-layered defects in a
         canonical multiplicity carrier, stable under cobordism moves.


This document organizes the proposal as a mathematical program and a fast validation plan.




1. Background: exotic spheres as smooth obstructions
A smooth exotic sphere is a manifold homeomorphic but not diffeomorphic to the standard sphere. In high
dimensions ( n ≥ 5), exotic spheres are classified via surgery theory, stable homotopy, and bordism-type
invariants (e.g., Kervaire–Milnor groups, Eells–Kuiper invariants in dimension 7, and refinements in modern
classifications).


Multiplicity Theory angle: treat primes as identity/eigenmode labels; “multiplicity” encodes recursion
depth/interaction thickness. The topological/smooth structure becomes a structured carrier that can be
decomposed into prime tiers.




2. Goal

2.1 Prime-indexed cobordism invariants

Given a smooth homotopy sphere Σn , produce a family of invariants


$$ {\mathfrak I_{p^r}(\Sigma)}_{p\ \text{prime},\ r\ge 1} $$


that:


        • is invariant under bordism / surgery moves after canonicalization,
        • is sensitive to smooth structure (so it can distinguish exotic spheres), and
        • is computable from presentations (plumbing graphs / Kirby diagrams / handle decompositions).

2.2 Physical implication

Use the prime spectrum {Ipr } to define weights/phases for a sum over smooth structures in quantum
gravity, and to refine string topology operations by prime-tier projections.




                                                      1
3. The multiplicity bordism picture (high-level)
We model the bordism category as acting on multiplicity carriers:


     • Objects: n-manifolds (e.g., Σn )
     • Morphisms: bordisms W : Σ0 ⇝ Σ1
     • Functorial target: a prime-graded algebra/category of multiplicity carriers

3.1 Multiplicity carrier

For each Σ choose presentation data (surgery or handles) and build:


     • a hypergraph (or graph) H(Σ) = (V , E, ι)
     • a matrix/operator MΣ built recursively from attaching/intersection/linking/framing data

The carrier is (H(Σ), MΣ ).




4. Construction: recursive multiplicity matrix from surgery/handle
data

4.1 Input formats

Any of the following can serve as the input presentation P(Σ):


     • Kirby diagram: framed link in S 3
     • Plumbing graph (common for 7-spheres and Brieskorn-type constructions)
     • Morse handle decomposition

4.2 Data extraction

From P(Σ), extract a bilinear kernel K capturing smooth-sensitive structure:


     • intersection form / linking matrix (depending on dimension and encoding)
     • framing defects
     • characteristic class refinements (spin/pontryagin corrections)
     • optionally spectral/eta-type corrections for smooth sensitivity

4.3 Prime labeling and recursion depth

Assign to each generator/handle/node v ∈ V :


     • prime label p(v)
     • multiplicity exponent μ(v) ∈ N (recursion depth / interaction thickness)




                                                      2
A deterministic choice (for reproducibility): order nodes by some canonical rule and map them to the first
∣V ∣ primes; μ(v) can be derived from local graph depth or from handle index stratification.

4.4 Matrix definition

Define


$$ M_{\Sigma}(i,j) := p(v_i)^{\mu(v_i)}\, p(v_j)^{\mu(v_j)}\, K(i,j). $$


Interpretation:


      • K(i, j) encodes topological attachment;
      • prime-powers encode “identity + depth”;
      • the product encodes coupling strength across nodes.

4.5 Recursion rule (optional but powerful)

Introduce a recursion operator R that updates μ (and possibly K ) under moves, e.g.


$$ \mu_{t+1}(v) = f\big(\mu_t(v),\ {\mu_t(u): u\sim v},\ \text{handle move type}\big). $$


This makes the invariant dynamic but still reducible to a canonical normal form.




5. Prime-tier projectors and invariants

5.1 Prime-tier projector

For each prime power pr , define an idempotent projector Πpr acting on matrices/operators so that Πpr M
keeps only the pr -tier information.


(Implementation idea: reduce matrix entries to p-adic valuation layers, or filter by prime divisibility
structure, or use operator-algebraic projections.)


5.2 Spectral packages (families of invariants)

Define prime-indexed signatures using any combination of:


      • traces of powers: $$ \mathfrak I^{\mathrm{tr}}{p^r}(\Sigma) := \big{\mathrm{Tr}((\Pi $$}
        M_{\Sigma})^k)\big}_{k=1}^{K
      • determinant/zeta forms: $$ \mathfrak I^{\det}{p^r}(\Sigma;s) := \det(I-s\,\Pi) $$}M_{\Sigma
      • eigenvalue multiplicity spectra: $$ \mathfrak I^{\mathrm{spec}}{p^r}(\Sigma) := \mathrm{Spec}(\Pi. $
        $}M_{\Sigma})\ \text{(as multiset)

These are intended to form a stable “prime fingerprint” of smooth structure.




                                                            3
6. Cobordism invariance strategy: canonicalization (“gauge fixing”)
The central technical problem is presentation dependence: different Kirby/handle presentations represent
the same manifold.


6.1 Move invariance via normal forms

Define a canonicalization procedure N such that:


     • if P and P ′ differ by Kirby/handle moves, then $$ \mathcal N(M_{\Sigma}(\mathcal P)) = \mathcal
       N(M_{\Sigma}(\mathcal P')) $$

6.2 What canonicalization might look like

     • reduce by elementary transformations encoding handle slides (row/column operations)
     • eliminate canceling handle pairs (block reduction)
     • normalize framings / blowups (stabilization moves)
     • choose a canonical prime labeling up to symmetries (graph automorphisms)

In practice: treat moves as an action of a generated equivalence relation on M , and reduce to a canonical
representative.




7. Exotic sphere sensitivity: where smoothness enters
To distinguish exotic spheres, K must incorporate smooth-sensitive refinements.


Candidate sources of smooth sensitivity:


     • Eells–Kuiper-type invariants in dimension 7 (and generalizations)
     • eta invariants / APS boundary correction terms
     • stable framing defects and the J -homomorphism context
     • refined characteristic class data (spin/pontryagin corrections)

The matrix framework does not replace these; it reorganizes them into a prime-tier spectral signal.




8. Implications for quantum gravity

8.1 Sum over smooth structures

If a fixed topological manifold admits multiple smoothings, define a “smoothness sector” partition
contribution


$$ Z_{\mathrm{smooth}}(M) := \sum_{\sigma\in \mathrm{Smooth}(M)} \exp\big(i\,S_{\mathrm{mult}}
(\sigma)\big) $$




                                                      4
where Smult is built from prime-tier invariants:


$$ S_{\mathrm{mult}}(\sigma) = \sum_{p,r} w_{p^r}\,\Phi\big(\mathfrak I_{p^r}(\sigma)\big) $$


for suitable weights wpr and phase map Φ.


Expected outcome: coherent clustering or cancellation across smooth sectors due to prime-tier resonance.


8.2 Noncommutative/operator viewpoint

Prime-tier operators naturally resemble noncommutative observables; canonicalization resembles gauge
reduction. This aligns well with approaches that link exotic smoothness to operator-algebraic structures.




9. Implications for string topology
String topology builds algebraic operations on H∗ (LM ) (free loop space). The proposal:


     • enrich operations by prime-tier projectors Πpr
     • interpret loop concatenation/splitting as interactions whose channels are filtered by prime structure

Potential deliverable: a prime-decomposed BV algebra on loop homology, where exotic smooth structure
modifies the prime spectrum of operations.




10. Concrete predictions (testable)
    1. Dimension 7 clustering: Milnor 7-spheres should split into distinguishable clusters by {Ipr },
       reflecting prime-primary components implicit in the classification groups.
    2. Move stability: applying Kirby/handle moves to the same sphere should leave Ipr unchanged after
       canonicalization.
    3. Smooth sensitivity: at least one small-prime tier (often p = 2 or 7 in 7D contexts) should
       systematically detect changes invisible to purely homotopy-level invariants.
    4. Physics signature: in a toy path-integral weighting, prime tiers may produce structured interference
       (selection of “dominant smoothings”).




11. Fastest path to validation (MVE)

Step A — choose a small battleground

Use 7-dimensional exotic spheres presented by explicit plumbing/link data.




                                                     5
Step B — implement pipeline

   1. Parse a presentation P(Σ) (plumbing graph or Kirby diagram).
   2. Build K (linking/intersection/framing form + smooth refinements).
   3. Assign primes p(v) and compute μ(v).
   4. Construct MΣ .
   5. Apply Πpr for a few tiers and compute Ipr .

Step C — invariance checks

    • apply known Kirby moves / handle slides / blowups
    • confirm invariants are stable after canonicalization

Step D — exotic discrimination

    • compare two non-diffeomorphic spheres with known classification differences
    • check whether prime spectra separate them




12. Reference map

12.1 Internal Multiplicity documents (project context)

    • Multiplicity Operator Calculus (MOC)
    • Polymorphic Multiplicity Matrices
    • Multiplicity Theory V0

12.2 Exotic spheres, surgery, invariants:

    • M. A. Kervaire & J. W. Milnor, “Groups of Homotopy Spheres: I”, Annals of Mathematics 77 (1963),
      504–537.
    • J. Eells Jr. & N. H. Kuiper, “An invariant for certain smooth manifolds”, Annali di Matematica Pura ed
      Applicata 60 (1962), 93–110. DOI: 10.1007/BF02412768.
    • D. Crowley, “The classification of 2-connected 7-manifolds” (and published version in Proceedings
      of the London Mathematical Society). arXiv:1406.2226.
    • E. V. Brieskorn, “Examples of singular normal complex spaces which are topological manifolds”,
      PNAS 55 (1966), 1395–1397. DOI: 10.1073/pnas.55.6.1395.
    • B. Martelli, “A finite set of local moves for Kirby calculus” (2011). arXiv:1102.1288.
    • M. F. Atiyah, V. K. Patodi, I. M. Singer, “Spectral asymmetry and Riemannian geometry I”, Math.
      Proc. Cambridge Philos. Soc. 77 (1975).
    • M. A. Hill, M. J. Hopkins, D. C. Ravenel, “A solution to the Arf–Kervaire invariant problem”
      (background/outline).

12.3 String topology

    • M. Chas & D. Sullivan, “String Topology” (1999). arXiv\:math/9911159.
    • D. Sullivan, “String topology: background and present state” (survey).




                                                     6
12.4 Exotic smoothness & quantum gravity

     • T. Asselmeyer-Maluga, “Smooth quantum gravity: Exotic smoothness and Quantum gravity”
       (2016). arXiv:1601.06436.
     • T. Asselmeyer-Maluga & J. Król, “Exotic Smoothness and Quantum Gravity II: exotic ********R4
      ********, singularities and cosmology” (2011). arXiv:1112.4882.



Citizen Gardens © 2025 CC-NC-ND 4.0




                                                  7

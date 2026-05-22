---
slug: aspectual-counting-framework
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Aspectual_Counting_Framework.md
  last_synced: '2026-03-20T17:17:20.358947Z'
---

             Aspectual Counting Framework (ACF):
 Aspects, Contexts, Bridges, and Higher-Order Conflict Geometry
                                           Ryan O. Van Gelder

                                            December 29, 2025


                                                  Abstract
         The Aspectual Counting Framework (ACF) formalizes the idea that numerical answers de-
      pend on the aspect under which we count. An aspect fixes (i) admissible units, (ii) invariances,
      and (iii) permissible inferences within and across aspects via explicit bridges. This article devel-
      ops ACF from a set-based quotient model through a functorial formulation, introduces contexts
      as a semilattice of practices, defines a bridge-selection principle as a prioritized satisfiable-
      subset problem, and analyzes the resulting conflict geometry via graphs, hypergraphs, Helly-
      type conditions, and a k-shadow hierarchy. We provide a concrete inconsistency theorem for
      Ship-of-Theseus-style paradoxes (as a non-existence of a global identity equivalence satisfying
      incompatible bridges), show how selection reduces to maximum-weight independent set (graph
      case) or its hypergraph analogue (higher-order case), define a practical Helly order induced by
      weights, give local dominance and antidominance criteria, and present a sound hypergraph-
      native certification procedure with a provable runtime-bounded local candidate generator. The
      only heuristic component is which candidate sets are tested; every certified constraint is sound.


Contents
1 Motivation: aspectual answers and Theseus                                                                  2

2 ACF-1: units as quotients and invariance                                                                   3
  2.1 Situations and aspects (quotient form) . . . . . . . . . . . . . . . . . . . . . . . . . .             3
  2.2 Invariance by construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           3
  2.3 Locality and additivity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          3

3 ACF-2: functorial aspects, contexts, and bridges                                                           3
  3.1 Aspects as functors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          3
  3.2 Contexts as admissibility constraints . . . . . . . . . . . . . . . . . . . . . . . . . . .            4
  3.3 Refinement as natural surjection . . . . . . . . . . . . . . . . . . . . . . . . . . . . .             4
  3.4 Bridges as natural relations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           4

4 Ship of Theseus as non-existence of a global identity                                                      4
  4.1 A minimal inconsistency model . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .              4

5 ACF-3: contexts as a semilattice and bridge selection                                                      4
  5.1 Contexts as a join-semilattice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .           4
  5.2 #-strict contexts and satisfiability . . . . . . . . . . . . . . . . . . . . . . . . . . . .           5
  5.3 Prioritized satisfiable-subset selection . . . . . . . . . . . . . . . . . . . . . . . . . . .         5


                                                       1
6 Conflict geometry: from graphs to hypergraphs                                                         5
  6.1 Monotonicity and minimal unsatisfiable sets . . . . . . . . . . . . . . . . . . . . . . .         5
  6.2 Graph reduction axiom (BW2 / MUS2) . . . . . . . . . . . . . . . . . . . . . . . . .              5
  6.3 Conflict hypergraph (general case) . . . . . . . . . . . . . . . . . . . . . . . . . . . .        5
  6.4 Reduction to (hyper)graph independent set . . . . . . . . . . . . . . . . . . . . . . .           5

7 Helly-type characterization and the k-shadow hierarchy                                                6
  7.1 Helly number of satisfiability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      6
  7.2 k-shadow approximation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        6

8 Practical Helly order and early exactness under weights                                               6
  8.1 Practical Helly order . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     6

9 Local dominance: sufficient conditions for early exactness                                            7
  9.1 Hypergraph-native dominance (MUS-incidence) . . . . . . . . . . . . . . . . . . . . .             7
  9.2 Graph-approx dominance (2-section neighborhood) . . . . . . . . . . . . . . . . . . .             7

10 Dual local lower bounds: antidomination structures                                                   7
   10.1 Local forcing of vertices (graph setting) . . . . . . . . . . . . . . . . . . . . . . . . .     7
   10.2 Weakened packing via an auxiliary graph and matching . . . . . . . . . . . . . . . .            7

11 Hypergraph-native certified unavoidable constraints and r-uniform packing                            8
   11.1 Certified unavoidable tail-hyperedges . . . . . . . . . . . . . . . . . . . . . . . . . . .     8
   11.2 Standard local bound: LP relaxation . . . . . . . . . . . . . . . . . . . . . . . . . . .       8
   11.3 Auxiliary hypergraph and fractional matching lower bound . . . . . . . . . . . . . .            8

12 Algorithm specification and soundness guarantees                                                     8
   12.1 ACF certification procedure (compact) . . . . . . . . . . . . . . . . . . . . . . . . . .       8
   12.2 Soundness theorem (certified vs heuristic) . . . . . . . . . . . . . . . . . . . . . . . .      9

13 A minimal local candidate generator with runtime bound                                               9
   13.1 MUS co-incidence neighborhood generator (MCN) . . . . . . . . . . . . . . . . . . .             9

14 Empirical and computational predictions                                                             10
   14.1 Graph vs hypergraph as a testable hypothesis . . . . . . . . . . . . . . . . . . . . . .       10
   14.2 k-shadow saturation and order of interaction . . . . . . . . . . . . . . . . . . . . . .       10
   14.3 Default parameter heuristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   10

15 Conclusion and open directions                                                                      10


1    Motivation: aspectual answers and Theseus
In counting disputes (Ship of Theseus, restored artifacts, legal identity, software versions), parties
often share all base-level facts yet disagree numerically. ACF posits: such disagreements frequently
arise from unlicensed cross-aspect inference. One can count planks, ship-continuants, replacement
events, legal registrations, functional roles, etc.; these are different invariants of the same underlying
situation.




                                                    2
2      ACF-1: units as quotients and invariance
2.1     Situations and aspects (quotient form)
Let E be a domain of items (tokens, time-slices, events, etc.). Let Obj be a class of situations X
with carriers |X| ⊆ E.
Definition 2.1 (Aspect as unitization). An aspect α assigns to each X ∈ Obj:
    (i) a selection Sα (X) ⊆ |X| (eligible candidates),

 (ii) an equivalence relation ∼α,X on Sα (X) (when candidates count as the same unit).
Define the set of α-units Uα (X) := Sα (X)/ ∼α,X .
Definition 2.2 (Aspectual count). If Uα (X) is finite, define

                                        a(X, α) := |Uα (X)| ∈ N.

2.2     Invariance by construction
Definition 2.3 (α-preserving bijection). A bijection f : |X| → |Y | is α-preserving if
    (i) x ∈ Sα (X) ⇐⇒ f (x) ∈ Sα (Y ),

 (ii) x ∼α,X x′ ⇐⇒ f (x) ∼α,Y f (x′ ).
Theorem 2.1 (Invariance). If f is α-preserving, then a(X, α) = a(Y, α).

2.3     Locality and additivity
Axiom 2.1 (Restriction coherence). If Y ⊆ |X| and X ↾ Y is defined, then Sα (X ↾ Y ) = Sα (X) ∩ Y
and ∼α,X↾Y is the restriction of ∼α,X .
Definition 2.4 (α-separation). If a disjoint sum X ⊔ Y is defined, say X ⊥α Y if Uα (X ⊔ Y ) ∼
                                                                                             =
Uα (X) ⊔ Uα (Y ).
Axiom 2.2 (Conditional additivity). If X ⊥α Y then a(X ⊔ Y, α) = a(X, α) + a(Y, α).
Remark 2.1. Continuant aspects often violate additivity over temporal concatenation: two history
segments each contain one continuant, yet their concatenation also contains one.


3      ACF-2: functorial aspects, contexts, and bridges
3.1     Aspects as functors
Let O be a category of situations (objects are situations, morphisms are structure-preserving maps;
isomorphisms are renamings).
Definition 3.1 (Aspect functor). An aspect is a functor Uα : O → FinSet. Define a(X, α) :=
|Uα (X)| when finite.
Theorem 3.1 (Functorial invariance). If g : X ∼
                                              = Y in O, then Uα (g) : Uα (X) ∼
                                                                             = Uα (Y ) and
a(X, α) = a(Y, α).
Remark 3.1. The quotient model of Definition 2.1 is recovered by taking Uα (X) = Sα (X)/ ∼α,X .

                                                    3
3.2   Contexts as admissibility constraints
A key philosophical point is that admissibility depends on what a practice can talk about.

Definition 3.2 (Context-indexed situation categories). A context c supplies a category Oc of
situations described in a language/signature Lc , and a forgetful/translation functor Fc : O → Oc .

Definition 3.3 (Context-admissible aspect). An aspect is admissible in context c if there exists a
functor U α,c : Oc → FinSet such that Uα ∼
                                         = U α,c ◦ Fc .

3.3   Refinement as natural surjection
Definition 3.4 (Refinement). An aspect β refines α (write β ⪰ α) if there exists a natural
transformation ρ : Uβ ⇒ Uα such that each component ρX : Uβ (X) ↠ Uα (X) is surjective.

Proposition 3.1 (Monotonicity under refinement). If β ⪰ α and both counts are finite, then
a(X, β) ≥ a(X, α).

3.4   Bridges as natural relations
Definition 3.5 (Bridge as natural relation). Fix a context c. A bridge τ : Uα ⇝ Uβ is a natural
family of relations τX ⊆ Uα (X) × Uβ (X).

Remark 3.2. Bridges are often partial, context-dependent, and relational rather than functional.
ACF enforces: no bridge, no transfer.


4     Ship of Theseus as non-existence of a global identity
4.1   A minimal inconsistency model
Let S = {s0 , s1 , s2 } be three ship-slices: original at t0 , maintained at t1 , reassembled at t1 . Let
# ⊆ S 2 encode co-present distinctness: s1 #s2 . Let C (continuity) relate s0 to s1 , and M (material
provenance) relate s0 to s2 .

Theorem 4.1 (Theseus inconsistency theorem). There is no equivalence relation ∼ on S such that:
(i) C(x, y) ⇒ x ∼ y, (ii) M (x, y) ⇒ x ∼ y, (iii) x#y ⇒ ¬(x ∼ y).

Proof. From (i) and C(s0 , s1 ), s0 ∼ s1 . From (ii) and M (s0 , s2 ), s0 ∼ s2 . Transitivity yields
s1 ∼ s2 , contradicting (iii) since s1 #s2 .

Remark 4.1. The “paradox” is the implicit demand that one identity relation satisfy incompatible
bridge-induced constraints.


5     ACF-3: contexts as a semilattice and bridge selection
5.1   Contexts as a join-semilattice
Definition 5.1 (Context semilattice). Let (C, ≤) be a poset of contexts. Assume a join operation
c ∨ d (least context extending both). Intuitively: c ∨ d combines practices, constraints, and bridge
libraries.



                                                   4
5.2   #-strict contexts and satisfiability
Fix c ∈ C. Let Bc be available bridge schemata. Each schema b ∈ Bc induces for each situation X
a required-identification relation Rb,c (X) on candidate slices Sc (X).
    Define forced identity for Γ ⊆ Bc on X by
                                                    [            
                                   ≡Γ,c (X) := EqCl      Rb,c (X) .
                                                         b∈Γ

Let #c (X) ⊆ Sc (X)2 be co-presence distinctness.
Definition 5.2 (#-strictness and satisfiability). Context c is #-strict if co-presence distinctness
is non-negotiable. A set Γ ⊆ Bc is satisfiable in c if for all X,
                                          ≡Γ,c (X) ∩ #c (X) = ∅.

5.3   Prioritized satisfiable-subset selection
Let ⪯c be a priority preorder on Bc , inducing levels L1 , . . . , LK (highest to lowest). Encode lexico-
graphic priorities by weights w(b) = M K−i for b ∈ Li , M > |Bc |.
Definition 5.3 (Selection problem). Choose Γ⊆Bc maximizing b∈Γ w(b) subject to Γ satisfiable.
                                                                      P


6     Conflict geometry: from graphs to hypergraphs
6.1   Monotonicity and minimal unsatisfiable sets
Lemma 6.1 (Monotonicity). If Γ ⊆ ∆ and Unsat(Γ) then Unsat(∆).
Definition 6.1 (Minimal unsatisfiable sets (MUS)). A set M ⊆ Bc is a MUS if Unsat(M ) and
every proper subset is satisfiable. Let Mc denote the family of all MUS.
Lemma 6.2 (MUS basis). Unsat(Γ) iff ∃M ∈ Mc with M ⊆ Γ.

6.2   Graph reduction axiom (BW2 / MUS2)
Axiom 6.1 (MUS2). All minimal unsatisfiable sets have size 2: ∀M ∈ Mc , |M | = 2.
    Under MUS2, satisfiable sets are exactly independent sets in a graph.

6.3   Conflict hypergraph (general case)
Definition 6.2 (Conflict hypergraph). Define Hc = (Vc , Ec ) with Vc = Bc and Ec = Mc . A bridge
set Γ is satisfiable iff it contains no hyperedge: ∀e ∈ Ec , e ̸⊆ Γ.

6.4   Reduction to (hyper)graph independent set
Proposition 6.1 (Optimization form). Bridge selection is equivalent to:
                           nX                                      o
                      max       w(b) : Γ ⊆ Bc , ∀M ∈ Mc , Γ ̸⊇ M .
                                   b∈Γ

As an ILP:
                      X                    X
                max       w(b)xb   s.t.         xb ≤ |M | − 1 (∀M ∈ Mc ), xb ∈ {0, 1}.
                      b                   b∈M


                                                     5
7     Helly-type characterization and the k-shadow hierarchy
7.1    Helly number of satisfiability
Definition 7.1 (Helly number). Let h(c) := max{|M | : M ∈ Mc } ∈ N ∪ {∞}.

Theorem 7.1 (Helly/MUS equivalence). For k ≥ 2, the following are equivalent: (i) every MUS
has size ≤ k; (ii) satisfiability is k-Helly (if all subsets of size ≤ k are satisfiable then the whole set
is satisfiable); (iii) Unsat(Γ) ⇒ ∃∆ ⊆ Γ with |∆| ≤ k and Unsat(∆).

Corollary 7.1 (Graph reduction). The conflict hypergraph reduces to a graph iff h(c) = 2 (equiv-
alently MUS2).

7.2    k-shadow approximation
Definition 7.2 (k-shadow of MUS family). For a MUS M and k ≥ 2, define
                       (
                        {S ⊆ M : |S| = k}, |M | > k,             [
            ∂k (M ) :=                                ∂k Mc :=        ∂k (M ).
                        {M },              |M | ≤ k.           M ∈M               c


Define the k-shadow approximation hypergraph H (k) = (Bc , ∂k Mc ).

Proposition 7.1 (Equivalent per-MUS cap). Γ is feasible in H (k) iff for all M ∈ Mc ,

                                    |Γ ∩ M | ≤ min(k − 1, |M | − 1).

Theorem 7.2 (Monotone interpolation). Let OP Tk be the maximum weight over Feask (the feasible
sets of H (k) ), and OP T⋆ the true optimum. Then

                              OP T2 ≤ OP T3 ≤ · · · ≤ OP Th(c) = OP T⋆ .


8     Practical Helly order and early exactness under weights
8.1    Practical Helly order
Definition 8.1 (Practical Helly order). Define

                                hw (c) := min{k ≥ 2 : OP Tk = OP T⋆ }.

Definition 8.2 (MUS-load). For Γ ⊆ Bc , define load(Γ) := maxM ∈Mc |Γ ∩ M |. Let

                                  L:=min{load(Γ):Γ∈arg max∆∈Feas⋆ w(∆)}.

Theorem 8.1 (Exactness criterion via optimal-load). For k ≥ 2,

                                   OP Tk = OP T⋆        ⇐⇒    k ≥ L+1.

Consequently hw (c) = L+1 and 2 ≤ hw (c) ≤ h(c).




                                                    6
9      Local dominance: sufficient conditions for early exactness
9.1    Hypergraph-native dominance (MUS-incidence)
Let M(b) := {M ∈ Mc : b ∈ M }.

Definition 9.1 (Incidence dominance). Define d ⪰ b if w(d) ≥ w(b) and M(d) ⊆ M(b).

Lemma 9.1 (Safe swap). If d ⪰ b and Γ is satisfiable with b ∈ Γ, then (Γ \ {b}) ∪ {d} is satisfiable
and has weight no smaller.

Definition 9.2 (k-tail). For each MUS M , let T opk−1 (M ) be the S min(k − 1, |M |) highest-weight
elements of M . Define T ailk (M ) := M \ T opk−1 (M ) and T ailk := M T ailk (M ).

Assumption 9.1 (Local dominance condition DC(k)). For every b ∈ T ailk , there exists d ̸= b
with d ⪰ b.

Theorem 9.1 (Local dominance implies hw (c) ≤ k). If DC(k) holds in a #-strict context, then
OP Tk = OP T⋆ , hence hw (c) ≤ k.

9.2    Graph-approx dominance (2-section neighborhood)
Define the 2-section graph G2sec on Bc where {u, v} is an edge iff they co-occur in some MUS. Let
N [b] denote closed neighborhood in G2sec .

Definition 9.3 (Graph dominance). d ⪰G b if w(d) ≥ w(b) and N [d] ⊆ N [b].

Assumption 9.2 (Graph dominance condition DCG (k)). For every b ∈ T ailk , there exists d ̸= b
with d ⪰G b.

Theorem 9.2 (Tail elimination for MWIS on G2sec ). If DCG (k) holds, then G2sec has a maximum-
weight independent set that avoids T ailk .


10      Dual local lower bounds: antidomination structures
10.1    Local forcing of vertices (graph setting)
Let G be a weighted graph. For b ∈ V (G), let U B(b) be any upper bound on the maximum weight
of an independent set in G[N (b) \ {b}].

Lemma 10.1 (Local forcing). If w(b) > U B(b), then every MWIS contains b.

10.2    Weakened packing via an auxiliary graph and matching
Fix k and tail set T = T ailk in G2sec . For u, v ∈ T nonadjacent, let Z(u, v) = N [u] ∪ N [v]. If
w(u) + w(v) exceeds an upper bound on the best independent-set weight within Z(u, v) \ {u, v},
then every MWIS must include at least one of {u, v}.
    Define an auxiliary graph Ak on vertex set T , with edge {u, v} if the above certificate holds.
Then any MWIS must hit each edge of a matching; hence matching size lower-bounds unavoidable
tails.

Theorem 10.1 (Matching lower bound). Let µk be the maximum matching size in Ak . Then every
MWIS I satisfies |I ∩T ailk |≥µk .

                                                 7
11     Hypergraph-native certified unavoidable constraints and r-uniform
       packing
11.1    Certified unavoidable tail-hyperedges
Fix tail level k and choose Q ⊆ T ailk with |Q| = r.
   Define
                                                    [
M(Q) := {M ∈ Mc : M ∩Q ̸= ∅},           Z(Q) :=                    (M \Q),   MZ (Q) := {M ∈ Mc : M ⊆ Z(Q)}.
                                                        M ∈M(Q)


11.2    Standard local bound: LP relaxation
Definition 11.1 (Local LP upper bound). Define U BLP (Q) as the optimum of
                                X
                          max       w(b)xb
                                      b∈Z(Q)
                                      X
                               s.t.         xb ≤ |M | − 1      (∀M ∈ MZ (Q)),
                                      b∈M
                                      0 ≤ xb ≤ 1     (∀b ∈ Z(Q)).

Definition 11.2 (Certified unavoidable set). Assuming Q itself contains no MUS (i.e. ∀M ∈
Mc , M ⊈ Q), call Q certified unavoidable if

                                               w(Q) > U BLP (Q).

Theorem 11.1 (Unavoidability soundness). If Q is certified unavoidable, then every maximum-
weight feasible selection Γ intersects Q.

11.3    Auxiliary hypergraph and fractional matching lower bound
Let Ek,r be the family of certified unavoidable r-sets. Define Ak,r = (T ailk , Ek,r ).

Theorem 11.2 (Fractional matching tail lower bound). Let νf (Ak,r ) be the fractional matching
number of Ak,r . Then for every optimal selection Γ,

                                         |Γ∩T ailk |≥τ (Ak,r )≥νf (Ak,r ),

where τ is the transversal number.

Remark 11.1. For r = 2, this recovers the graph/matching bound in polynomial time. For r ≥ 3,
integral hypergraph matching is hard in general, but νf remains polynomial via LP.


12     Algorithm specification and soundness guarantees
12.1    ACF certification procedure (compact)
Inputs. B, weights w, MUS family Mc , tailrule T ailk , target (k, r) values, and a candidate
generator producing finite families Qk,r ⊆ T ail
                                             r
                                                k
                                                  .



                                                        8
Outputs.      Certified families Ek,r ⊆ Qk,r , auxiliary hypergraphs Ak,r , and lower bounds Lk,r :=
νf (Ak,r ).

Certification. For each Q ∈ Qk,r : (i) discard if it contains a MUS; (ii) compute Z(Q) and
MZ (Q); (iii) solve the local LP to get U BLP (Q); (iv) if w(Q) > U BLP (Q), add Q to Ek,r .

Bounding.         Compute νf (Ak,r ) via the fractional matching LP.

12.2    Soundness theorem (certified vs heuristic)
Theorem 12.1 (Procedure soundness). Fix a #-strict context with MUS family Mc and weights
w. Run the certification procedure with any candidate sets Qk,r (possibly generated heuristically).
Then:
                                                                                           ∩Q̸=∅
  (i) Every certified Q ∈ Ek,r is a valid unavoidable constraint: ∀Γ∈OPT, Γ                        .

 (ii) Consequently every optimum hits every hyperedge in Ak,r .
                                                                      ∩T ailk |≥Lk,r
(iii) The computed bound Lk,r = νf (Ak,r ) satisfies ∀Γ∈OPT, |Γ                        .

 (iv) The only heuristic element is coverage: failing to test some Q can miss constraints (false
      negatives), but the procedure cannot certify a false unavoidable constraint (no false positives),
      assuming LPs are solved correctly.


13     A minimal local candidate generator with runtime bound
13.1    MUS co-incidence neighborhood generator (MCN)
Fix k and T = T ailk .

Co-incidence graph. Build   P Ck = (T, Ek ) with edge {u, v} iff ∃M ∈ Mc such that {u, v} ⊆ M .
This can be built in time O( M ∈Mc |M ∩ T |2 ).

Caps. Choose a neighborhood cap s ∈ N and radius ℓ ∈ {1, 2}. For each t ∈ T , let N (ℓ) (t) be its
ℓ-hop neighborhood in Ck . Define Ns (t) as the top min(s, |N (ℓ) (t)|) vertices in N (ℓ) (t) by weight.

Star enumeration.           For each target size r and each t ∈ T , generate candidates

                               Qk,r (t) := {{t} ∪ S : S ⊆ Ns (t), |S| = r − 1}.
              S
Let Qk,r =        t∈T Qk,r (t) (deduplicated).

Proposition 13.1 (Generator runtime bound). For fixed k, the MCN generator runs in
                                            !                   !
                            X                          X s 
                                          2
                       O         |M ∩ T |     + O |T |
                                                           r−1
                                   M ∈Mc                        r∈R

time (plus linear hashing for deduplication).
Remark 13.1. Soundness remains unconditional (Theorem 12.1); the generator only affects com-
pleteness.

                                                      9
14     Empirical and computational predictions
14.1    Graph vs hypergraph as a testable hypothesis
The MUS size profile pk = |{M ∈M  c :|M |=k}|
                                 |Mc |        and Helly number h(c) quantify higher-order conflict.
Domains with h(c) = 2 are effectively pairwise; domains with frequent |M | ≥ 3 support “all pairs
ok, some triples forbidden” phenomena.

14.2    k-shadow saturation and order of interaction
Compute OP Tk (or bounds thereof) across k to estimate hw (c). Compute certified lower bounds
on unavoidable tails via Lk,r ; growth of Lk,r with r indicates higher-order interaction beyond pairs.

14.3    Default parameter heuristics
Typical regimes suggest starting with r ∈ {2, 3} and modest neighborhood caps (e.g. s ≈ 15) with
ℓ = 1, escalating to ℓ = 2 when MUS are larger or co-incidence neighborhoods are sparse.


15     Conclusion and open directions
ACF transforms counting/identity disputes into explicit choices of (i) aspects, (ii) contexts, and (iii)
bridges. The resulting selection problem has a rich geometry: graph-like under MUS2, hypergraph-
like otherwise, with Helly numbers measuring interaction order. The k-shadow hierarchy interpo-
lates between pairwise approximations and true constraints, while hw (c) captures the effective order
needed under a weight regime. Local dominance and certified unavoidability procedures yield fast,
interpretable sufficient conditions and lower bounds. Future work includes: learning Mc from data,
context morphisms and joins as empirical shifts, and characterizing when higher-order structure is
necessary for stable disagreement.


References
 [1] Saunders Mac Lane. Categories for the Working Mathematician, volume 5 of Graduate Texts
     in Mathematics. Springer, New York, 2 edition, 1998.
 [2] Steve Awodey. Category Theory, volume 49 of Oxford Logic Guides. Oxford University Press,
     Oxford, 2 edition, 2010.
 [3] Tom Leinster. Basic Category Theory, volume 72 of London Mathematical Society Student
     Texts. Cambridge University Press, Cambridge, 2014.
 [4] Francis Borceux. Handbook of Categorical Algebra 1: Basic Category Theory. Cambridge
     University Press, Cambridge, 1994.
 [5] Francis Borceux. Handbook of Categorical Algebra 2: Categories and Structures. Cambridge
     University Press, Cambridge, 1994.
 [6] Francis Borceux. Handbook of Categorical Algebra 3: Sheaf Theory. Cambridge University
     Press, Cambridge, 1994.
 [7] Peter J. Freyd and Andre Scedrov. Categories, Allegories, volume 39 of North-Holland Math-
     ematical Library. North-Holland, Amsterdam, 1990.

                                                  10
 [8] Bart Jacobs. Categorical Logic and Type Theory, volume 141 of Studies in Logic and the
     Foundations of Mathematics. Elsevier, Amsterdam, 1999.

 [9] F. William Lawvere and Stephen H. Schanuel. Conceptual Mathematics: A First Introduction
     to Categories. Cambridge University Press, Cambridge, 2 edition, 2009.

[10] Claude Berge. Graphs and Hypergraphs. North-Holland, Amsterdam, 1973.

[11] Alain Bretto. Hypergraph Theory: An Introduction. Springer, Cham, 2013.

[12] Jack Edmonds. Paths, trees, and flowers. Canadian Journal of Mathematics, 17:449–467, 1965.

[13] László Lovász and Michael D. Plummer. Matching Theory, volume 121 of North-Holland
     Mathematics Studies. North-Holland, Amsterdam, 1986.

[14] Alexander Schrijver. Combinatorial Optimization: Polyhedra and Efficiency. Springer, Berlin,
     2003.

[15] George L. Nemhauser and Laurence A. Wolsey. Integer and Combinatorial Optimization.
     Wiley, New York, 1988.

[16] Richard M. Karp. Reducibility among combinatorial problems. In Raymond E. Miller and
     James W. Thatcher, editors, Complexity of Computer Computations, pages 85–103. Plenum
     Press, New York, 1972.

[17] Michael R. Garey and David S. Johnson. Computers and Intractability: A Guide to the Theory
     of NP-Completeness. W. H. Freeman, San Francisco, 1979.

[18] Christos H. Papadimitriou. Computational Complexity. Addison-Wesley, Reading, MA, 1994.

[19] Eduard Helly. Über mengen konvexer körper mit gemeinschaftlichen punkten. Jahresbericht
     der Deutschen Mathematiker-Vereinigung, 32:175–176, 1923.

[20] Ludwig Danzer, Branko Grünbaum, and Victor Klee. Helly’s theorem and its relatives. In
     Convexity, volume 7 of Proceedings of Symposia in Pure Mathematics, pages 101–180. American
     Mathematical Society, Providence, RI, 1963.

[21] Raymond Reiter. A theory of diagnosis from first principles. Artificial Intelligence, 32(1):57–95,
     1987.

[22] Johan de Kleer and Brian C. Williams. Diagnosing multiple faults. Artificial Intelligence,
     32(1):97–130, 1987.

[23] Mark H. Liffiton and Karem A. Sakallah. Algorithms for computing minimal unsatisfiable
     subsets of constraints. Journal of Automated Reasoning, 40(1):1–33, 2008.

[24] Raymond Reiter. A logic for default reasoning. Artificial Intelligence, 13(1–2):81–132, 1980.

[25] Gerhard Brewka. Adding priorities and specificity to default logic. In Logics in Artificial
     Intelligence (JELIA ’94), volume 838 of Lecture Notes in Computer Science, pages 247–260,
     Berlin, 1994. Springer.

[26] Peter Simons. Parts: A Study in Ontology. Clarendon Press, Oxford, 1987.



                                                  11
[27] David Wiggins. Sameness and Substance Renewed. Cambridge University Press, Cambridge,
     2001.

[28] Saul A. Kripke. Naming and Necessity. Harvard University Press, Cambridge, MA, 1980.

[29] David Lewis. Survival and identity. Philosophical Papers, 1:55–77, 1983. Essay originally
     published 1976; reprinted in Philosophical Papers, Vol. 1.

[30] Plutarch. Theseus. In Parallel Lives. Many editions; cite the edition used, 0. Classical source
     of the Ship of Theseus motif; specify translator/edition in final bibliography.

[31] Thomas Hobbes. De Corpore. Various editions, 1655. Contains the discussion Of Identity and
     Difference; specify edition/translator used.

[32] Achille C. Varzi. Mereology. The Stanford Encyclopedia of Philosophy, 2023. Edward N. Zalta
     (ed.); cite with URL and access date in final manuscript.

[33] Harold Noonan and Ben Curtis. Personal identity. The Stanford Encyclopedia of Philosophy,
     2024. Edward N. Zalta (ed.); cite with URL and access date in final manuscript.




                                                12

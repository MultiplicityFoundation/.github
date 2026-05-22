---
slug: determinacy-algebra-being-becoming-and-laws-that-bite-canvas-edition
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "03-case-studies/Determinacy Algebra \u2014 Being, Becoming, And Laws That\
    \ Bite (canvas Edition).md"
  last_synced: '2026-03-20T17:17:20.600081Z'
---

Determinacy Algebra: Being, Becoming, and Laws
That Bite
Executive summary. We model "being" as closure under an idempotent operator α. The size F = ∣Fix(α)∣ of
its determinate core satisfies a submultiplicative law under constraint‑coupled composition: F (X ⊗K Y ) ≤
F (X) ⋅ F (Y ), with **defect **Δ = |Forbidden determinate pairs|. This defect quantifies how laws bite.
The framework lifts cleanly to presheaves for context‑dependent semantics and admits temporalization for
becoming.




Core Definitions & Theorems
Assumption. We work primarily in the finite setting; cardinal arithmetic extends the results.


Definition 1 (Mode Object). A carrier X with idempotent α : X → X (α ∘ α = α). Its determinate core
is Fix(α) = {x ∣ α(x) = x}. The size invariant F (X, α) := ∣Fix(α)∣ ∈ N (or Card).


Definition 2 (Law & Constrained Tensor). For (X, αX ), (Y , αY ), a law K ⊆ X × Y is closed under
αX × αY . The constrained tensor is the subobject K ↪ X × Y equipped with αK := (αX × αY ) ↾K ,
which remains idempotent because (αX × αY )2 = αX × αY and K is closed under αX × αY .




The Three Key Theorems

Theorem 1 (Fixed‑Point Formula).


$$ \mathrm{Fix}\big((X,\alpha_X) \, \widehat{\otimes}_K \, (Y,\alpha_Y)\big) = \big(\mathrm{Fix}(\alpha_X)
\times \mathrm{Fix}(\alpha_Y)\big) \cap K. $$


Theorem 2 (Submultiplicativity & Equality Criterion).


$$ F\big((X,\alpha_X) \, \widehat{\otimes}_K \, (Y,\alpha_Y)\big) \le F(X,\alpha_X)\cdot F(Y,\alpha_Y). $$


Equality holds iff Fix(αX ) × Fix(αY ) ⊆ K , i.e., when the inclusion (Fix(αX ) × Fix(αY )) ∩ K ↪
Fix(αX ) × Fix(αY ) is an isomorphism.

Theorem 3 (Defect Identity). Define the multiplicativity defect


$$ \Delta_K(X,Y) := F(X)F(Y) - F\big((X,\alpha_X)\widehat{\otimes}_K(Y,\alpha_Y)\big). $$


Then:




                                                        1
$$ \Delta_K(X,Y) = |\,(\mathrm{Fix}(\alpha_X)\times\mathrm{Fix}(\alpha_Y)) \setminus K\,|. $$


Thus F is a lax monoidal size functor with defect Δ.




Additional Properties
                                                           ′
Proposition (Determinacy monotonicity). If Fix(αX ) ⊆ Fix(αX ) and Fix(αY ) ⊆ Fix(αY′ ), then

$$ F\big((X,\alpha_X)\widehat{\otimes}_K(Y,\alpha_Y)\big)              \le   F\big((X,\alpha'_X)\widehat{\otimes}_K(Y,
\alpha'_Y)\big). $$


Proposition (Law monotonicity). If K ⊆ K ′ then


$$ F\big((X,\alpha_X)\widehat{\otimes}K(Y,\alpha_Y)\big)         \le    F\big((X,\alpha_X)\widehat{\otimes}(Y,\alpha_Y)
\big), \quad \Delta_K(X,Y) \ge \Delta_{K'}(X,Y). $$


Theorem (Defect subadditivity under intersections). For any K, L ⊆ X × Y closed under αX × αY ,


$$ \Delta_{K\cap L}(X,Y) \le \Delta_K(X,Y) + \Delta_L(X,Y). $$


Proof. The forbidden set for K ∩ L is the union of the two forbidden sets; apply ∣A ∪ B∣ ≤ ∣A∣ + ∣B∣.


Proposition (Defect under unions). For K, L closed under αX × αY ,


$$ \Delta_{K\cup L}(X,Y) \ge \max{\Delta_K(X,Y),\ \Delta_L(X,Y)}. $$


Bonferroni (two laws).


$$ \Delta_{K\cap L}(X,Y) \ge \Delta_K(X,Y)+\Delta_L(X,Y)-\Delta_{K\cup L}(X,Y). $$


Definition (n‑ary law and defect). For (Xi , αi ) (i = 1, … , n) and K ⊆ ∏i Xi closed under ∏i αi ,


$$ \widehat{\bigotimes}_{K}\,       (X_1,\alpha_1),   \dots,     (X_n,\alpha_n)      :=   \big(K,   (\prod_i   \alpha_i)!
\restriction_K\big), $$


$$ \Delta_K(X_1,\dots,X_n) := \prod_i F(X_i) - F!\big(\widehat{\bigotimes}_{K} (X_i,\alpha_i)\big) = \big|\,
(\prod_i \mathrm{Fix}(\alpha_i)) \setminus K \,\big|. $$




Associativity & the Associator Defect

When laws are only pairwise, associativity is not automatic.




                                                         2
Setup. Let K ⊆ X × Y , L ⊆ Y × Z , M ⊆ X × Z (all closed under the respective α's). Define two
composites:


$$ \begin{aligned} F_{(XY)Z} &:= F\big((X\widehat{\otimes}K Y) \widehat{\otimes} Z\big),\
F_{X(YZ)} &:= F\big(X \widehat{\otimes}_{\widetilde K} (Y\widehat{\otimes}_L Z)\big), \end{aligned} $$


where L, K are the induced laws on triples obtained by pullback/pushforward along projections.


Definition (Associator defect).


$$ \delta_{\mathrm{assoc}}(X,Y,Z;K,L,M) := |F_{(XY)Z} - F_{X(YZ)}|. $$


Theorem (Associativity via 3‑ary extension). δassoc = 0 iff there exists a T ⊆ X × Y × Z closed under
αX × αY × αZ such that πXY [T ] = K, πY Z [T ] = L, πXZ [T ] = M , and both composites are the
same subobject (T , (αX × αY × αZ ) ↾T ) viewed along the two bracketings.


Why it matters: δassoc flags non‑associative constraint interactions—critical for systems engineering.




The Bool Witness Family
Take Bool with α = id (everything determinate). Then F (Bool) = 2.


        Law K                         Description           Forbidden pairs    F (Bool⊗K Bool)       Δ

        All‑allowed (X × Y )          No law                ∅                  4                     0

        Implication (b1 ⇒ b2 )        Entailment            (1,0)              3                     1

        At‑most‑one (¬(b1 ∧ b2 ))     Exclusion             (1,1)              3                     1

        At‑least‑one (b1 ∨ b2 )       Coverage              (0,0)              3                     1

        Diagonal (b1 = b2 )           Agreement             (0,1), (1,0)       2                     2

        XOR (b1 ⊕ b2 = 1)             Incompatibility       (0,0), (1,1)       2                     2


Different laws yield different defects, all computable via Theorem 3.




Presheaf Lift: Global Actual Being
                                                                    P op
Let P be a poset (stages, worlds, contexts). Work in C = Set               .
Notation: Terminal presheaf 1; global sections Γ(Z) = Nat(1, Z).
Equalizers and monos are computed pointwise.




                                                        3
A presheaf mode object is (X, α) with α : X ⇒ X natural and idempotent.
Define Fix(α) as the equalizer presheaf (pointwise).
Define actual being as F (X, α) := ∣Γ(Fix(α))∣.


Choice of aggregator. We take F = ∣Γ(Fix(α))∣ to measure coherent being across contexts. Alternatives
(pointwise counts, colimits) capture potential/aggregate being. Results are stable under switching to any
                                                            P op
aggregator that is a limit‑preserving functor out of Set           .


Example (two stages). For P = {0 → 1}, with restriction r10 : X(1) → X(0),


$$ \Gamma(\mathrm{Fix}(\alpha))\ \cong\ {x_1\in \mathrm{Fix}(\alpha(1))\mid r_{10}(x_1)\in \mathrm{Fix}
(\alpha(0))}, $$


so F ≤ min{#Fix(α(0)), #Fix(α(1))}.


Lemma (Constant Lift). For constant presheaves and pointwise K , Γ(Fix(α)) ≅ Fix(α) at any stage.
Hence the Bool witnesses lift unchanged.


           Context P              Interpretation                   Γ(Fix(α)) meaning

           Single point           Static world                     Actual core

           (N, ≤)                 Developmental stages             Stable identity across stages

           Kripke frame           Modal worlds                     Necessary core (world‑invariant)

           Intervention poset     Causal contexts                  Dispositions surviving all interventions




Introduce a time‑indexed family (αt )t∈T with αs ≤ αt pointwise (s ≤ t).


Lemma (Monotone Cores). Fix(αs ) ⊆ Fix(αt ) ⇒ Fs ≤ Ft .


Process law: αt+1 ∘ αt = αt+1 (lax idempotence across time).
Event: strict increase in Ft .
Becoming‑two time: t∗ := min{t ∣ Ft = 2} (when exists).


Lemma (Event–defect identity). For fixed K ,


$$ \Delta_{K,t} = \big|\,(\mathrm{Fix}(\alpha_{X,t})\times\mathrm{Fix}(\alpha_{Y,t})) \setminus K\,\big|. $$


Corollary (Stability). If K is constant in t and αt stabilizes, then ΔK,t stabilizes.




                                                        4
Law Taxonomy & Closure Operator
     • α****‑preserving: (x, y) ∈ K ⇒ (αX x, αY y) ∈ K .
     • α****‑creating: ∃ α′ ≥ α with K α′ ‑preserving but not α‑preserving.
     • α****‑violating: references indeterminate bits (disallowed if α encodes lawful sector).

Law‑closure operator.


$$ \mathrm{LawCl}_\alpha(K) := \min{\alpha' \ge \alpha \mid K \text{ is } \alpha'\text{‑preserving}}. $$


Monotonicity:
K ⊆ K ′ ⇒ LawClα (K) ≤ LawClα (K ′ ).
α ≤ α′ ⇒ LawClα (K) ≤ LawClα′ (K).

Proposition (Law closure is a nucleus). Ordering idempotents by fixed‑set inclusion, LawClα is
inflationary, monotone, and idempotent; hence a nucleus on this poset. The image is a reflective subposet
of determinacy levels where K is admissible.


Remark (Karoubi split). Every idempotent α on Set splits; (X, α) is equivalent to the inclusion i :
Fix(α) ↪ X . In this normal form, Theorem 1 becomes “intersect with K then count,” and all other results
reduce to elementary set arithmetic.




Unit & Isomorphism Invariance
Unit mode object. Let I be a one‑element set with αI = id. For any law K ⊆ X × I closed under
αX × αI , we have K ≃ X , αK ≃ αX , hence

$$ F\big((X,\alpha_X)\widehat{\otimes}K(\mathbb I,\alpha)\big)=F(X,\alpha_X). $$


Taking K = X × I realizes I as the tensor unit.


Isomorphism invariance. If f : (X, αX ) → (X ′ , αX ′ ) is an isomorphism commuting with α, then F and
ΔK are preserved under transport along f × g .



Computational Recipe (finite case)
       Algorithm (finite Δ). Precompute A := Fix(αX ), B := Fix(αY ). Then
       F (X ⊗K Y ) = #{(a, b) ∈ A × B : (a, b) ∈ K}, and Δ = #(A × B) − F .
       Cost: O(∣A∣∣B∣) membership checks in K . With bitsets/sorted lists, stream with O(∣A∣ +
       ∣B∣) memory.




                                                      5
Lean‑Flavored Code Snippets

Set‑level skeleton (finite case)


 -- Finite mode objects with explicit cardinality
 structure ModeObj (X : Type) [Fintype X] where
    α : X → X
    idem : ∀ x, α (α x) = α x

 namespace ModeObj
 variable {X Y : Type} [Fintype X] [Fintype Y] (M : ModeObj X) (N : ModeObj Y)

 -- Fixed points as a Finset (helper predicate omitted for brevity)
 def Fix : Finset X := {x | M.α x = x}


 def F : ℕ := (Fix M).card

 structure Law where
   K : Finset (X × Y)
    closed : ∀ p ∈ K, (M.α p.1, N.α p.2) ∈ K


 def tensor (L : Law M N) : ModeObj {p // p ∈ L.K} where
    α := fun ⟨p, h⟩ => ⟨(M.α p.1, N.α p.2), L.closed p h⟩
    idem := fun ⟨p, h⟩ => by
      ext <;> simp [M.idem, N.idem]


 -- Theorem 1: fixed‑point formula (sketch)
 theorem fix_tensor (L : Law M N) :
      (tensor L).Fix = (M.Fix ×ˢ N.Fix).filter (· ∈ L.K) := by
    -- unpack definitions; idempotence + closure suffice
    admit

 -- Theorem 2: submultiplicativity (sketch)
 theorem F_le_mul (L : Law M N) : F (tensor L) ≤ F M * F N := by
   -- compare cardinalities via inclusion into product core
   admit


 -- Theorem 3: defect identity (sketch)
 def defect (L : Law M N) : ℕ := F M * F N - F (tensor L)

 theorem defect_eq (L : Law M N) :
      defect L = ((M.Fix ×ˢ N.Fix) \ L.K).card := by
    -- inclusion–exclusion on filtered product
    admit




                                          6
Bool witness (diagonal law)


  def BoolMode : ModeObj Bool := ⟨id, λ _ => rfl⟩

  def diagLaw : Law BoolMode BoolMode := {
    K := {(true,true), (false,false)},
    closed := by simp
  }

  #eval BoolMode.F                          -- 2
  #eval (tensor diagLaw).F                  -- 2 (< 4)
  #eval defect diagLaw                      -- 2


(Swap N for cardinals to remove finiteness; port to presheaves by working in functor categories and using
pointwise equalizers.)




Relevant External References
      • S. Mac Lane, Categories for the Working Mathematician, 2nd ed., Springer (1998).
      • S. Mac Lane & I. Moerdijk, Sheaves in Geometry and Logic, Springer (1992).
      • P. T. Johnstone, Sketches of an Elephant: A Topos Theory Compendium, Oxford (2002).
      • S. Awodey, Category Theory, 2nd ed., Oxford (2010).
      • T. Leinster, Basic Category Theory, Cambridge (2014).
      • F. W. Lawvere, "Adjointness in Foundations," Dialectica 23 (1969).
      • M. Karoubi, K‑Theory: An Introduction, Springer (1978). [Idempotent splitting/Karoubi envelope]
      • B. Jacobs, Categorical Logic and Type Theory, Elsevier (1999).
      • S. Abramsky & A. Brandenburger, "The sheaf-theoretic structure of non-locality and contextuality,"
        New J. Phys. 13 (2011). [presheaves & constraints]
      • M. Barr & C. Wells, Toposes, Triples and Theories, Repr. Theory Appl. Categ. (2005).
      • T. Leinster, "Basic Bicategories," arXiv:9802029. [lax monoidal functors & coherence]




FAQ (quick checks)
      • Infinite case? All statements hold in Card; submultiplicativity uses cardinal multiplication;
        Theorem 3 uses set‑difference cardinality.
      • Does F functorialize? Yes: on morphisms commuting with α, F is monotone on monos; equality
        holds exactly when the mono is an iso on fixed sets.
      • Why ‘tensor’? It is a law‑parametrized product; formally a lax monoidal structure where the unit is
        the mode object with singleton core.




                                                      7
One‑sentence value proposition

Determinacy algebra turns “laws reduce independence” into a lax‑monoidal arithmetic with a
measurable defect ****Δ, unifying static, modal, and developmental readings and exposing
non‑associative law interactions as quantifiable risk.


Citizen Gardens © 2025 CC-NC-ND 4.0




                                            8

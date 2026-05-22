---
slug: petc-drmm-csc
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 00-foundations/imd/PETC_DRMM_CSC.md
  last_synced: '2026-03-20T17:17:22.364982Z'
---

  Prime-Encoded Tensor Calculus
Formal Foundations, Functorial Multiplicity, and ACE-Certification


                                Dr. Ryan Van Gelder


                       A Community Research Initiative

                                  Citizen Gardens

                     Institute for Mathematical Discovery


                                      October 2025




  We develop a certified mathematical framework where prime factorization provides a
  canonical encoding of tensor structure. Objects are prime signatures — finitely supported
  integer labelings of the set of primes — equipped with a strict symmetric monoidal
  structure (tensor = pointwise addition, unit = 0, dual = negation). A central multiplicity
  functor M : Sig → Q× maps signatures to units of the rationals by M(e) = p pep ,
                                                                                        Q
  thereby transporting tensor to multiplication and duals to inversion. We formalize the key
  laws (M(0) = 1, M(e+f ) = M(e) M(f ), M(−e) = M(e)−1 ) and show prime-conservation
  for morphisms in the discrete categorical model. This yields algebraic certificates for tensor
  product and contraction that are independent of floating-point numerics and integrate
  seamlessly with an ACE control loop for stability-aware contraction planning.
Contents
1 Introduction                                                                                    2

2 Prime Signatures and Monoidal Structure                                                        2

3 Multiplicity Functor to Q×                                                                      2

4 Categorical Semantics and Conservation                                                          3

5 Computational Semantics: Axis-Typed Tensors                                                     3

6 Prime-Encoded Tensor Calculus × Certified Spectral Control (CSC/DRMM)                           3
  6.1 Plant, channels, and weights . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    4
  6.2 Certified objectives: gap lower bound and slope upper bound . . . . . . . . . . .           4
  6.3 Lawfulness budgets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    4
  6.4 Optimization program (CSC controller) . . . . . . . . . . . . . . . . . . . . . . .         4
  6.5 PETC invariants and composition theorem . . . . . . . . . . . . . . . . . . . . .           5
  6.6 Small-gain recursion and ACE loop . . . . . . . . . . . . . . . . . . . . . . . . . .       5
  6.7 Prime-gating invariant Λm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     5

7 ACE Integration: Stability-Aware, Certified Contractions                                        6

8 Mechanization Summary (Lean)                                                                   6

9 Scope, Limitations, and Extensions                                                              6

A Lean Snippets                                                                                   7

B Python Signatures and Certificates                                                              7

C Prime Signatures and Monoidal/Dual Structure                                                   9

D Multiplicity Functor to Q×                                                                      9

E Categorical Semantics and Conservation                                                         10

F Lean Formalization (Core Snippets)                                                             10

G Computational Semantics: Axis-Typed Tensors                                                    12

H ACE/CSC Integration (Interface Sketch)                                                         14

I   Reproducibility and Build                                                                    14

J Why Prime Signatures? Structural Linearization                                                 14

K Empirical Validation Plan                                                                      15
  K.1 Kernel Dispatch Safety . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   15
  K.2 Blocked Contraction Validity . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     15
  K.3 CSC Certificate Tightening . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     15

L References                                                                                     15




                                                1
1    Introduction
Prime factorization is canonical, global, and choice-free. We leverage this to encode the structural
“type” of tensor axes and to define a multiplicative invariant that certifies the correctness of
tensor operations. The resulting framework—Prime-Encoded Tensor Calculus (PETC)—unifies:
• a free abelian structure of signatures on primes,

• a monoidal/dual semantics (tensor/dual ↔ add/negate exponents),

• a functorial multiplicity invariant into Q× (group of rational units), and

• certified computation: tensor product and contraction preserve the invariant and hence cannot
  create or destroy “prime mass”.
We also outline an ACE-integrated control loop that uses these algebraic guarantees as hard
constraints while learning numerically stable contraction orderings.

Contributions. (1) A strict symmetric monoidal skeleton on prime signatures with duals; (2)
a monoidal functor M : Sig → Q× proving conservation laws; (3) a computational semantics
that lifts signatures to axis-typed tensors; (4) certified operations and property-based testing;
(5) an integration plan with ACE for stability-aware, safety-preserving tensor contraction.


2    Prime Signatures and Monoidal Structure
Let P denote the set of natural primes. We write e = (ep )p∈P ∈ Z(P) for a finitely supported
integer labeling of primes.
Definition 2.1 (Prime signatures). The set of prime signatures is

                       Sig := {e : P → Z : e has finite support} ∼
                                                                 = Z(P) .

The support is supp(e) := {p ∈ P : ep ̸= 0}.
Definition 2.2 (Monoidal and dual structure). Define tensor by pointwise addition (e ⊗ f )p :=
ep + fp , the unit by 0, and the dual by e∨ := −e. Thus (Sig, ⊗, 0, (·)∨ ) is a strict symmetric
monoidal skeleton with duals.


3    Multiplicity Functor to Q×
Definition 3.1 (Multiplicity). Define M : Sig → Q× by
                                               Y
                                   M(e) :=          p ep .
                                                 p∈supp(e)

Because supp(e) is finite, this product is well-defined. Negative exponents are interpreted via
pep = 1/p−ep .
Theorem 3.2 (Monoidality and duality). For all e, f ∈ Sig:

                M(0) = 1,       M(e + f ) = M(e) M(f ),        M(−e) = M(e)−1 .

Proof. Immediate from unique factorization and the laws of exponents. Finite support ensures
all products are finite.

Remark 3.3 (Valuations). The coordinate ep coincides with the p-adic valuation vp (M(e)).
Thus e 7→ M(e) packages the family of valuations (vp )p into a single multiplicative invariant.

                                                 2
Unsigned size (optional). Define |M|(e) := p p|ep | ∈ Q≥0 . Then |M|(e+f ) = |M|(e) |M|(f ),
                                             Q
but |M|(−e) = |M|(e), so |M| ignores variance (duals) and is not a duality-preserving functor.


4    Categorical Semantics and Conservation
To obtain lightweight, fully certified laws, we view signatures as objects of the discrete category
Disc(Sig): morphisms are equalities.

Proposition 4.1 (Prime conservation in the discrete model). Any isomorphism e ∼
                                                                              = f in
Disc(Sig) satisfies M(e) = M(f ).

Proof. In Disc(Sig), isomorphisms are equalities; apply Theorem D.2.

Remark 4.2 (Compact-closed perspective). Object-level duals e∨ = −e admit evaluation/co-
evaluation maps e∨ ⊗ e → 0 and 0 → e ⊗ e∨ given by the definitional equalities (−e) + e = 0 and
0 = e + (−e). Passing through M, evaluation corresponds to multiplication by M(−e) M(e) = 1.


5    Computational Semantics: Axis-Typed Tensors
EachQtensor axis of integer length n > 0 carries a signature given by its prime factorization
n = pvp (n) . A tensor with axes (ni ) and variances σi ∈ {+1, −1} has global signature
                                        X
                             sig(T ) =     σi e(i) , e(i)
                                                      p := vp (ni ).
                                          i


Certified operations.

• Tensor product (Kronecker). Concatenates axes; globally, signatures add: sig(A ⊗ B) =
  sig(A) + sig(B).

• Contraction (Einstein). Removes one +1 axis and one −1 axis with matching signatures
  (same prime profile). Globally, the signature is unchanged: sig(contract(A, B)) = sig(A) +
  sig(B), because the contracted pair contributes +e + (−e) = 0.

Certificates.   Define the (algebraic) certificate

C⊗ : (A, B, C) 7→ [sig(C) = sig(A)+sig(B)],          C⟨·,·⟩ : (A, B, C) 7→ [sig(C) = sig(A)+sig(B)].

Both certificates imply M(sig(C)) = M(sig(A)) M(sig(B)) by Theorem D.2.

Example 5.1 (Matrix multiplication). A ∈ Rm×n (variance [−1, +1]), B ∈ Rn×p (variance
[−1, +1]). Contract the shared n-axis to obtain C ∈ Rm×p . The global signature obeys
sig(C) = sig(A) + sig(B); the contracted pair contributes 0.


6   Prime-Encoded Tensor Calculus × Certified Spectral Control
    (CSC/DRMM)
This section couples the structural guarantees of PETC with certified spectral control (CSC)
in the DRMM style. PETC enforces type safety (no creation of prime content) through the
multiplicity functor M : Sig → Q× . CSC enforces spectral safety (gap preservation and slope
control) for parameterized operators.




                                                3
6.1   Plant, channels, and weights
Let Ω be a compact frequency/parameter domain and fix a target spectral band S of a nominal
operator X(ω) with frequency gap δS (ω) > 0 for all ω ∈ Ω. We consider a controlled operator
                                                              X
               U (ω; w) = X(ω) + C(ω; w),          C(ω; w) =      wp Bp (ω),
                                                                       p∈P

where {Bp (ω)} are prime-indexed channels and w = (wp )p∈P are real weights. We assume
ω 7→ Bp (ω) is norm-differentiable with known bounds

                        ∥Bp (ω)∥ ≤ bp ,       ∥∂ω Bp (ω)∥ ≤ Lp ,       ∀ω ∈ Ω.

6.2   Certified objectives: gap lower bound and slope upper bound
The spectral gap of U (ω; w) over the band S obeys the Weyl-type lower bound
                                                                    X           
           GapLB (w) inf δS (ω) − 2 ∥C(ω; w)∥ ≥ inf δS (ω) − 2           |wp | bp .                         (1)
                        ω∈Ω                                ω∈Ω
                                                                                  p

Similarly, eigenvalue slopes satisfy a Hellmann–Feynman/Davis–Kahan-style bound
                                                                      X
           SlopeUB (w) sup max ∂ω λk (U (ω; w)) ≤ sup ∥∂ω C(ω; w)∥ ≤      |wp | Lp .                        (2)
                        ω∈Ω λk ∈S                        ω∈Ω                          p

These two certified surrogates are computable from (bp , Lp ) and enter the control program below.

6.3   Lawfulness budgets
We constrain the controller using three budgets that encode structural lawfulness:

1. Prime-gated ℓ1 norm: ∥w∥1,b := p bp |wp | ≤ τ . (Optionally fit a prior |wp | ≈ κp−α and
                                       P
   penalize deviations.)

2. Recursion gain: a model gain ∥Ξ∥ ≤ β used in small-gain updates (see §6.6).
                        P
3. Commutator budget:      p<q ∥[Bp (ω), Bq (ω)]∥ ≤ γ uniformly in ω.


6.4   Optimization program (CSC controller)
Given a trade-off parameter λ > 0, solve:

                 max J(w) = GapLB (w) − λ SlopeUB (w)
                w∈RP
                  s.t. ∥w∥1,b ≤ τ,         Λm (w; α) ≤ τΛ ,        ∥Ξ∥ ≤ β,                                 (3)
                       X
                          θpq ≤ γ,        ∥[Bp (ω), Bq (ω)]∥ ≤ θpq     ∀ ω ∈ Ω, p < q.
                       p<q
                                                                   P                  P
Using (1)–(2), a convex surrogate objective is inf ω δS (ω) − 2      p bp |wp | − λ       p Lp |wp |, optimized
under the additional convex constraint Λm (w; α) ≤ τΛ .




                                                   4
6.5   PETC invariants and composition theorem
PETC tracks
        Q σpa global prime signature σ ∈ Sig for each tensor object. The multiplicity functor
M(σ) = p ∈ Q is monoidal and dual-compatible: M(σ + σ ′ ) = M(σ)M(σ ′ ), M(−σ) =
                  ×

M(σ)−1 . Contractions remove one +σ and one −σ axis, leaving the global signature (and thus
M) unchanged.

Theorem 6.1 (PETC × CSC soundness). Consider a contraction plan whose tensor operations
pass the PETC certificates (signature equalities) and a weight vector w feasible for (3). If
GapLB (w) > 0, then:

  (i) Structural correctness: global prime signatures (and hence M) are conserved along the
      entire plan.

  (ii) Spectral safety: the target band S remains isolated for all ω ∈ Ω; in particular, every
       eigenvalue branch in S is Lipschitz with slope bounded by SlopeUB (w).

Proof. (i) follows from monoidality and dual-compatibility of M, together with the definition
of contraction as canceling matched ±σ axes. (ii) follows by Weyl-type gap perturbation with
bound (1) and a standard eigen-slope estimate bounded by (2).

6.6   Small-gain recursion and ACE loop
Let Tt denote the active operator and suppose the controller supplies an increment ∆C(·; w(t) ).
A one-step small-gain update is

                      Tt+1 (ω) = Tt (ω) + ε Ξ ∆C(ω; w(t) ),       0 < ε ≪ 1.

If ∥Ξ∥ ∥∆C∥ ≤ η and η < 12 inf ω δS (ω), then the gap remains positive by the same bound as in
(1). This yields an ACE loop:

1. Generate candidate contraction orders; filter by PETC certificates.

2. Solve (3) for w; reject if GapLB (w) ≤ 0.

3. Apply a small-gain step; verify with eigentracking; learn stability features for the next
   iteration.

Remark (Unsigned size). The map |M|(σ) = p|σp | ∈ Q≥0 is a monoidal size that ignores
                                                     Q
dual signs; it is useful for coarse resource accounting but is not dual-compatible.

6.7   Prime-gating invariant Λm
We encode a scale-invariant prior that controller weights follow a prime-indexed power law. Let
ap (α) := p−α for fixed α ≥ 0 and channel weights w = (wp )p∈P . Define the weighted ℓ1 deviation
                                              X
                             Λm (w; α) := inf     bp wp − κ ap (α) .                           (4)
                                           κ≥0
                                                 p∈P

Properties.

            P Λm (· ; α) is convex since it is the infimum, over κ ≥ 0, of convex functions
1. Convexity.
   (w, κ) 7→ p bp |wp − κap (α)|.

2. Scale-insensitivity. Λm (w; α) = 0 iff w lies on the ray {κ a(α) : κ ≥ 0}.



                                                  5
3. Stability under small updates. For any increment ∆w,
                                                                            X
            Λm (w + ∆w; α) ≤ Λm (w; α) + ∥∆w∥1,b ,      where ∥∆w∥1,b :=          bp |∆wp |.
                                                                              p


We enforce a lawfulness band by requiring Λm (w; α) ≤ τΛ . This
                                                            P preserves a tempered spectrum
of active channels and complements the budgets ∥w∥1,b and p<q ∥[Bp , Bq ]∥.


7    ACE Integration: Stability-Aware, Certified Contractions
We integrate the algebraic layer with an ACE control loop:

1. Candidates. Generate contraction plans (which axes to contract, in which order).

2. Hard constraints. Filter plans by certificates C⊗ , C⟨·,·⟩ ; reject any plan violating signature
   equalities.

3. Stability scoring. A learned oracle predicts instability based on signature features (cancel-
   lation depth, prime residuals, entropy, spread).

4. Execute learn. Execute the best certified plan, measure stability, and update the oracle
   (bandit/Thompson or small MLP).

This yields a self-correcting loop: algebraic invariants enforce correctness, while ACE optimizes
performance.


8    Mechanization Summary (Lean)
We formalized the following in Lean (mathlib):

• Sig = P →fin Z via finitely supported functions.

• M : Sig → Q× with proofs of M(0) = 1, M(e + f ) = M(e) M(f ), M(−e) = M(e)−1 .

• Discrete symmetric monoidal packaging (tensor = addition; dual = negation).

• Prime conservation: isomorphisms (equalities) preserve M.

A compact-closed upgrade (cups/caps, yanking) can be added; M then becomes a strong
monoidal functor into the one-object monoidal category (Q× , ·, 1).


9    Scope, Limitations, and Extensions
Scope. The framework certifies structural correctness (no creation/destruction of prime content)
independent of numeric values.
    Limitations. Current formalization uses the discrete category; full compact-closed coherence
is future work. Factorization cost is mitigated by maintaining signatures symbolically.
    Extensions. Replace P by prime ideals of a Dedekind domain; treat    Qsignatures as gradings
of tensor categories; connect to Hecke-operator factorization Tn ∼   = p Tpvp (n) for algebraic
validation.




                                                6
A    Lean Snippets

import   Mathlib
import   Mathlib / Data / Finsupp
import   Mathlib / Data / Nat / Prime
import   Mathlib / Algebra / GroupPower
import   Mathlib / CategoryTheory / Category / Discrete

-- primes as indices
def PrimeNat := { p : Nat // Nat . Prime p }
-- signatures
def Sig := PrimeNat         Int

namespace Sig
noncomputable def qUnit ( p : PrimeNat ) :           :=
  Units . mk0 ( p .1 :   ) ( by exact_mod_cast Nat . cast_ne_zero . mpr ( Nat .
     ne_of_gt p .2. pos ) )

noncomputable def multiplicity ( s : Sig ) :                :=
  s . support . prod ( fun p = > ( qUnit p ) ^ ( s p ) )

@ [ simp ] lemma multi plicit y_zero : multiplicity (0 : Sig ) = (1 :                )
     := by
    simp [ multiplicity ]

lemma multiplicity_add ( a b : Sig ) :
  multiplicity ( a + b ) = multiplicity a * multiplicity b := by
  -- proof uses support union + zpow_add + prod_mul_distrib
  admit

lemma multiplicity_neg ( a : Sig ) : multiplicity ( - a ) = ( multiplicity a )
         := by
  -- proof uses support equality + zpow_neg + prod_inv_distrib
  admit
end Sig



B    Python Signatures and Certificates

from fractions import Fraction

def multiplicity_Qx ( sig : dict [ int , int ]) -> Fraction :
    num , den = 1 , 1
    for p , e in sig . items () :
         if e >= 0: num *= p ** e
         else :       den *= p ** ( - e )
    return Fraction ( num , den )

def conservation_ok ( inputs : list [ dict [ int , int ]] , out : dict [ int , int ]) ->
    bool :
    m_in = Fraction (1 ,1)
    for s in inputs : m_in *= multiplicity_Qx ( s )
    return m_in == multiplicity_Qx ( out )


Acknowledgments. We thank the ACE architecture for providing the control scaffolding and
the multiplicity validation pipeline. [11pt]article

                                            7
    [a4paper,margin=1in]geometry [T1]fontenc [utf8]inputenc amsmath,amssymb,amsfonts,amsthm,mathtools
microtype enumitem xcolor hyperref [nameinlink,capitalise]cleveref tikz listings
    Theorem[section] [theorem]Proposition [theorem]Lemma [theorem]Corollary [theorem]Definition
[theorem]Example [theorem]Remark




                                            8
    Prime-Encoded Tensor Calculus with Certified Multiplicity:
      Formal Foundations, Code, and ACE/CSC Integration



                                            Abstract
        We present a certified framework where prime factorization encodes tensor structure.
     Objects are prime signatures—finitely supported integer labelings of primes—equipped
     with a strict symmetric monoidal structure (tensor = pointwise addition,    unit = 0, dual
     = negation). A multiplicity functor M : Sig → Q× sends e 7→ p pep , transporting
                                                                          Q
     tensor to multiplication and duals to inversion. We formalize the core laws (M(0) = 1,
     M(e + f ) = M(e) M(f ), M(−e) = M(e)−1 ), package signatures as a discrete symmetric
     monoidal category so prime conservation is immediate, and lift the semantics to axis-typed
     tensors with runtime certificates. We include Lean and Python snippets and outline an ACE
     control loop with a CSC layer for spectral safety.


Contents

C    Prime Signatures and Monoidal/Dual Structure
Let P be the set of natural primes. A prime signature is a finitely supported map e : P → Z,
written e = (ep )p with support supp(e) := {p ∈ P : ep ̸= 0}. The set

                       Sig := Z(P) ∼
                                   = {e : P → Z : e has finite support}

forms the free abelian group on P.

Definition C.1 (Monoidal and dual structure). Define tensor by (e ⊗ f )p := ep + fp , the unit
by 0, and the dual by e∨ := −e. Thus (Sig, ⊗, 0, (·)∨ ) is a strict symmetric monoidal skeleton
with duals.


D     Multiplicity Functor to Q×
Definition D.1 (Signed multiplicity). Define M : Sig → Q× by M(e) := p∈supp(e) p ep ,
                                                                               Q
interpreting negative exponents as reciprocals. Finite support makes the product finite.

Theorem D.2 (Monoidality and duality). For all e, f ∈ Sig: M(0) = 1, M(e+f ) = M(e) M(f ),
M(−e) = M(e)−1 .

Proof sketch. Immediate from unique factorization and exponent laws; finite support ensures
well-defined products.

Remark D.3 (Valuations). Each coordinate ep is the p-adic valuation vp (M(e)). The functor
M packages the family (vp )p into a single multiplicative invariant.

                                               |ep | ∈ Q
                                        Q
Optional unsigned size. |M|(e) :=         pp            ≥0 is monoidal (ignores duals): |M|(e + f ) =
|M|(e) |M|(f ) and |M|(−e) = |M|(e).


                                                  9
E    Categorical Semantics and Conservation
We view signatures as objects of the discrete category Disc(Sig): morphisms are equalities.
Proposition E.1 (Prime conservation). Any isomorphism e ∼
                                                        = f in Disc(Sig) satisfies M(e) =
M(f ).
Proof. Isomorphisms are equalities in Disc(Sig); apply Theorem D.2.

Remark E.2 (Compact-closed perspective). Object-level duals e∨ = −e admit evaluation/co-
evaluation maps e∨ ⊗ e → 0 and 0 → e ⊗ e∨ given by the equalities (−e) + e = 0 and 0 = e + (−e).
Under M, evaluation multiplies by M(−e) M(e) = 1.


F    Lean Formalization (Core Snippets)
The following Lean (mathlib) snippets capture the formal laws with ASCII-only identifiers for
portability.
import Mathlib
import Mathlib/Data/Finsupp
import Mathlib/Data/Nat/Prime
import Mathlib/Algebra/GroupPower
import Mathlib/CategoryTheory/Category/Discrete
import Mathlib/CategoryTheory/Monoidal/Basic

open scoped BigOperators
open Finsupp

/-- primes as indices -/
def PrimeNat := {p : Nat // Nat.Prime p}

/-- prime signatures: finitely-supported integer exponents over primes -/
abbrev Sig := PrimeNat Int

namespace Sig

/-- embed a prime into Units Rat -/
noncomputable def qUnit (p : PrimeNat) : Units Rat :=
by
  refine Units.mk0 (p.1 : Rat) ?_
  exact_mod_cast (Nat.cast_ne_zero.mpr (Nat.ne_of_gt p.2.pos))

/-- multiplicity: finite product of prime-units to integer exponents -/
noncomputable def multiplicity (s : Sig) : Units Rat :=
by
  classical
  exact s.support.prod (fun p => (qUnit p) ^ (s p))

@[simp] lemma multiplicity_zero : multiplicity (0 : Sig) = (1 : Units Rat) := by
  classical
  simp [multiplicity]

lemma multiplicity_add (a b : Sig) :
    multiplicity (a + b) = multiplicity a * multiplicity b := by
  classical
  let S := a.support b.support
  have hA : multiplicity a = S.prod (fun p => (qUnit p) ^ (a p)) := by
    refine Finset.prod_subset ?subset ?fill rfl


                                              10
    exact Finset.subset_union_left
    intro p hpS hpA; have : a p = 0 := by simpa [mem_support_iff] using hpA
     simpa [multiplicity, this]
 have hB : multiplicity b = S.prod (fun p => (qUnit p) ^ (b p)) := by
   refine Finset.prod_subset ?subset ?fill rfl
    exact Finset.subset_union_right
    intro p hpS hpB; have : b p = 0 := by simpa [mem_support_iff] using hpB
     simpa [multiplicity, this]
 have hAB : multiplicity (a + b) = S.prod (fun p => (qUnit p) ^ (a p + b p)) := by
   have hsub : (a + b).support S := by
     intro p hp; have : a p + b p 0 := by simpa [mem_support_iff] using hp
     by_cases ha : a p = 0
      have hb : b p 0 := by
         have : b p = 0 False := by intro hb0; simpa [ha, hb0] using this
         simpa using this
       exact Finset.mem_union.mpr (Or.inr (by simpa [mem_support_iff] using hb))
      exact Finset.mem_union.mpr (Or.inl (by simpa [mem_support_iff] using ha))
   have hfill : p S, p (a + b).support (qUnit p) ^ (a p + b p) = (1 : Units Rat)
       := by
     intro p _ hpAB; have : a p + b p = 0 := by simpa [mem_support_iff] using hpAB
     simpa [this]
   have := Finset.prod_subset hsub hfill
   simpa [multiplicity]
 calc
   multiplicity (a + b)
       = S.prod (fun p => (qUnit p) ^ (a p + b p)) := hAB
   _ = S.prod (fun p => (qUnit p) ^ (a p) * (qUnit p) ^ (b p)) := by
         refine Finset.prod_congr rfl ?_; intro p _; simpa using
           (Units.zpow_add (qUnit p) (a p) (b p))
   _ = (S.prod (fun p => (qUnit p) ^ (a p))) * (S.prod (fun p => (qUnit p) ^ (b p)))
       := by
         simpa [Finset.prod_mul_distrib]
   _ = multiplicity a * multiplicity b := by simpa [hA, hB]

lemma multiplicity_neg (a : Sig) : multiplicity (-a) = (multiplicity a) := by
  classical
  have hS : (-a).support = a.support := by
    ext p; simp [mem_support_iff]
  calc
    multiplicity (-a)
        = a.support.prod (fun p => (qUnit p) ^ (-(a p))) := by simpa [multiplicity, hS]
    _ = a.support.prod (fun p => ((qUnit p) ^ (a p))) := by
          refine Finset.prod_congr rfl ?_; intro p _; simpa using
            (Units.zpow_neg (qUnit p) (a p))
    _ = (a.support.prod (fun p => (qUnit p) ^ (a p))) := by
          simpa using (Finset.prod_inv_distrib _ _)
    _ = (multiplicity a) := by simp [multiplicity]

end Sig

open CategoryTheory
abbrev PSig := Discrete Sig

instance : MonoidalCategory (PSig) where
  tensorObj X Y := X.as + Y.as
  tensorHom := by intro X X’ Y Y’ f g; cases f; cases g; exact rfl
  tensorUnit := 0
  associator X Y Z := rfl


                                          11
  leftUnitor X := rfl
  rightUnitor X := rfl

/-- conservation is immediate in the discrete setting -/
lemma prime_conservation {A B : Sig}
    (f : (Discrete.mk A) (Discrete.mk B)) : Sig.multiplicity A = Sig.multiplicity B
        := by
  cases f; simp



G     Computational Semantics: Axis-Typed Tensors
Each axis of integer length n > 0 carries a signature via prime factorization n = pvp (n) . A tensor
                                                                                 Q
                                                                                   (i)
with axes (ni ) and variances σi ∈ {+1, −1} has global signature i σi e(i) with ep = vp (ni ).
                                                                     P


Certified operations. Tensor product concatenates axes and adds signatures. Contraction
removes a matched +1 axis with a matched −1 axis with equal signatures; globally, the signature
is unchanged (+e + (−e) = 0 inside the sum).
from __future__ import annotations
from dataclasses import dataclass, field
from collections import Counter
from typing import Dict, List
import functools
from fractions import Fraction
import numpy as np

@functools.lru_cache(maxsize=None)
def factorint_cached(n: int):
    if n <= 0: raise ValueError("n␣must␣be␣positive")
    f, d, m = {}, 2, n
    while d*d <= m:
        while m % d == 0:
            f[d] = f.get(d, 0) + 1
            m //= d
        d += 1 if d == 2 else 2
    if m > 1: f[m] = f.get(m, 0) + 1
    return tuple(sorted(f.items()))

Signature = Counter # prime -> integer exponent (allow negatives)

def sig_add(a: Signature, b: Signature) -> Signature:
    out = a.copy()
    for p, e in b.items():
        out[p] += e
        if out[p] == 0: del out[p]
    return out

def multiplicity_Qx(a: Signature) -> Fraction:
    num, den = 1, 1
    for p, e in a.items():
        if e >= 0: num *= p**e
        else: den *= p**(-e)
    return Fraction(num, den)

@dataclass(frozen=True)
class Axis:


                                                12
   length: int
   signature: Signature = field(init=False)
   def __post_init__(self):
       fac = factorint_cached(self.length)
       object.__setattr__(self, "signature", Signature(dict(fac)))

@dataclass
class PETensor:
    data: np.ndarray
    axes: List[Axis]
    variance: List[int] # +1 (covariant), -1 (contravariant)
    def __post_init__(self):
        if self.data.ndim != len(self.axes) or len(self.axes) != len(self.variance):
            raise ValueError("axes/variance␣must␣match␣rank")
        for ax, n in zip(self.axes, self.data.shape):
            if ax.length != n:
                raise ValueError("Axis␣length␣mismatch")
    @property
    def signature(self) -> Signature:
        sig = Signature()
        for ax, s in zip(self.axes, self.variance):
            sig = sig_add(sig, Signature({p: s*e for p, e in ax.signature.items()}))
        return sig

def can_contract_axes(axA: Axis, axB: Axis) -> bool:
    return (axA.signature == axB.signature) and (axA.length == axB.length)

def tensor_product(A: PETensor, B: PETensor) -> PETensor:
    data = np.kron(A.data, B.data)
    return PETensor(data, A.axes + B.axes, A.variance + B.variance)

def contract(A: PETensor, B: PETensor, a_axis: int, b_axis: int) -> PETensor:
    if A.variance[a_axis] == B.variance[b_axis]:
        raise ValueError("Contraction␣requires␣opposite␣variances")
    if not can_contract_axes(A.axes[a_axis], B.axes[b_axis]):
        raise ValueError("Axis␣signatures/dimensions␣differ")
    data = np.tensordot(A.data, B.data, axes=([a_axis], [b_axis]))
    axes = [ax for i, ax in enumerate(A.axes) if i != a_axis] + \
           [ax for j, ax in enumerate(B.axes) if j != b_axis]
    variance = [v for i, v in enumerate(A.variance) if i != a_axis] + \
               [v for j, v in enumerate(B.variance) if j != b_axis]
    return PETensor(data, axes, variance)

# Certificates
from dataclasses import dataclass
@dataclass
class OpCertificate:
    ok: bool; msg: str; input_sigs: List[Signature]; output_sig: Signature

def validate_tensor_product(A: PETensor, B: PETensor, C: PETensor) -> OpCertificate:
    s = sig_add(A.signature, B.signature)
    ok = (C.signature == s) and (C.data.shape == np.kron(A.data, B.data).shape)
    return OpCertificate(ok, "tensor_product" if ok else "tensor_product␣violated", [A.
        signature, B.signature], C.signature)

def validate_contraction(A: PETensor, B: PETensor, C: PETensor) -> OpCertificate:
    s = sig_add(A.signature, B.signature)
    ok = (C.signature == s)


                                          13
    return OpCertificate(ok, "contraction" if ok else "contraction␣violated", [A.
        signature, B.signature], C.signature)

def conservation_ok(inputs: List[PETensor], out: PETensor) -> bool:
    m = Fraction(1,1)
    for T in inputs: m *= multiplicity_Qx(T.signature)
    return m == multiplicity_Qx(out.signature)


Example G.1 (Matrix multiplication). A ∈ Rm×n (variance [−1, +1]), B ∈ Rn×p (variance
[−1, +1]). Contract the shared n-axis to obtain C ∈ Rm×p . The global signature obeys
sig(C) = sig(A) + sig(B); the contracted pair contributes 0.


H     ACE/CSC Integration (Interface Sketch)
We treat PETC and CSC as orthogonal certifications: PETC enforces structural invariants
(prime conservation), while CSC enforces spectral budgets (gap/slope/gain/commutators). The
ACE loop searches contraction orderings under PETC hard constraints and CSC soft/hard
constraints.
class CSCertifiedObjectives:
    def __init__(self, delta_S: float, primes: list[int], omega_range: tuple[float,
        float]):
        self.delta_S = delta_S; self.primes = primes
        self.omega_range = omega_range
    def gap_lower_bound(self, w):
        C_sup = float(np.sum(np.abs(w)))
        return max(0.0, self.delta_S - 2.0*C_sup)
    def slope_upper_bound(self, w):
        slope = float(np.sum(np.abs(w)*np.log(self.primes)))
        return (self.omega_range[1]-self.omega_range[0]) * slope

class CertifiedACE:
    def __init__(self, objectives: CSCertifiedObjectives):
        self.obj = objectives
    def execute_plan(self, A, B, plan):
        # 1) PETC check
        cert = validate_contraction(A, B, plan.result)
        if not cert.ok: raise ValueError("PETC␣violated")
        # 2) CSC check (pre/post)
        J_gap = self.obj.gap_lower_bound(plan.weights)
        if J_gap <= 0: raise ValueError("CSC␣gap␣failed")
        return plan.result



I   Reproducibility and Build
Provide a repository with: (i) Lean project containing Section F code; (ii) Python module
containing Section G code and tests; (iii) this LaTeX source.


J    Why Prime Signatures? Structural Linearization
Traditional dimension checking relies on multiplicative Diophantine constraints: given axis
lengths n1 , . . . , nk , we verify equalities like n1 n2 = n3 n4 . Prime signatures linearize these



                                                14
                  (i)
constraints: for ep = vp (ni ), the same condition becomes

                                   e(1)  (2)  (3)  (4)
                                    p + ep = ep + ep        ∀p ∈ P,

turning multiplicative reasoning into integer-linear constraints. This enables:

    • SMT/ILP compatibility: Linear constraints are directly solvable.

    • Dual-awareness: Contravariance becomes native negation e 7→ −e.

    • Blocked-kernel dispatch: Conditions like “contains 2k block” become v2 (n) ≥ k.

    • Lattice operations: gcd /lcm become coordinatewise min / max.

While integers and nonnegative signatures carry equivalent information, signatures make the
algebraic structure additive, linear, and dual-aware—precisely what formal verification and
static planning require.


K     Empirical Validation Plan
We validate PETC through three concrete test cases demonstrating advantages over integer-only
tracking.

K.1    Kernel Dispatch Safety
Using axis signatures, we implement static dispatch rules such as

                               use radix2 fft(n) ⇐⇒ v2 (n) ≥ k.

PETC verifies these conditions at compile-time, whereas integer-only approaches either factor at
runtime or risk misdispatch.

K.2    Blocked Contraction Validity
We construct networks where dimensions match numerically (e.g. 12 = 12) but require specific
blocked structure (e.g. 3 × 4 vs. 2 × 6). PETC rejects ill-typed contractions that pass integer-level
checks but fail at runtime.

K.3    CSC Certificate Tightening
When PETC proves operator block-diagonality across prime sectors, spectral certificates tighten
from sums to extrema:
                                                 X
             ∥C(ω; w)∥ ≤ max |wp | ∥Bp (ω)∥ (vs.     |wp | ∥Bp (ω)∥ in general).
                               p
                                                        p

This demonstrates how structural typing enables stronger numerical guarantees.


L     References

References
 [1] Saunders Mac Lane. Categories for the Working Mathematician, volume 5 of Graduate
     Texts in Mathematics. Springer, 2 edition, 1998.


                                                 15
 [2] G. M. Kelly and M. L. Laplaza. Coherence for compact closed categories. Journal of Pure
     and Applied Algebra, 19:193–213, 1980.

 [3] Peter Selinger. A survey of graphical languages for monoidal categories. In Bob Coecke,
     editor, New Structures for Physics, volume 813 of Lecture Notes in Physics, pages 289–355.
     Springer, 2011.

 [4] Tosio Kato. Perturbation Theory for Linear Operators. Classics in Mathematics. Springer,
     2 edition, 1995.

 [5] Chandler Davis and W. M. Kahan. The rotation of eigenvectors by a perturbation. iii.
     SIAM Journal on Numerical Analysis, 7(1):1–46, 1970.

 [6] Roger A. Horn and Charles R. Johnson. Matrix Analysis. Cambridge University Press, 2
     edition, 2013.

 [7] Rajendra Bhatia. Matrix Analysis, volume 169 of Graduate Texts in Mathematics. Springer,
     1997.

 [8] Lloyd N. Trefethen and Mark Embree. Spectra and Pseudospectra: The Behavior of
     Nonnormal Matrices and Operators. Princeton University Press, 2005.

 [9] Richard P. Feynman. Forces in molecules. Physical Review, 56:340–343, 1939.

[10] Hans Hellmann. Einführung in die Quantenchemie. Franz Deuticke, Leipzig, 1937.

[11] Cornelius Lanczos. An iteration method for the solution of the eigenvalue problem of linear
     differential and integral operators. Journal of Research of the National Bureau of Standards,
     45(4):255–282, 1950.

[12] Max A. Woodbury. Inverting modified matrices. Technical Report Memo. Rep. 42, Statistical
     Research Group, Princeton University, 1950.

[13] James W. Cooley and John W. Tukey. An algorithm for the machine calculation of complex
     fourier series. Mathematics of Computation, 19(90):297–301, 1965.

[14] Charles M. Rader. Discrete fourier transforms when the number of data samples is prime.
     Proceedings of the IEEE, 56(6):1107–1108, 1968.

[15] Charles F. Van Loan. The ubiquitous kronecker product. Journal of Computational and
     Applied Mathematics, 123(1–2):85–100, 2000.

[16] Ivan V. Oseledets. Tensor-train decomposition. SIAM Journal on Scientific Computing,
     33(5):2295–2317, 2011.

[17] Román Orús. A practical introduction to tensor networks: Matrix product states and
     projected entangled pair states. Annals of Physics, 349:117–158, 2014.

[18] G. H. Hardy and E. M. Wright. An Introduction to the Theory of Numbers. Oxford
     University Press, 6 edition, 2008.

[19] Jürgen Neukirch. Algebraic Number Theory. Springer, 1999.

[20] M. F. Atiyah and I. G. Macdonald. Introduction to Commutative Algebra. Addison-Wesley,
     1969.

[21] Jean-Pierre Serre. A Course in Arithmetic, volume 7 of Graduate Texts in Mathematics.
     Springer, 1973.

                                               16
[22] Jean-Pierre Serre. Linear Representations of Finite Groups, volume 42 of Graduate Texts
     in Mathematics. Springer, 1977.

[23] William Fulton and Joe Harris. Representation Theory: A First Course, volume 129 of
     Graduate Texts in Mathematics. Springer, 1991.

[24] Leonardo de Moura, Soonho Kong, Jeremy Avigad, Floris van Doorn, and Jakob von Raumer.
     The lean theorem prover (system description). In Automated Deduction – CADE-25, volume
     9195 of Lecture Notes in Computer Science, pages 378–388. Springer, 2015.

[25] The mathlib Community. The lean mathematical library. In Proceedings of the 9th ACM
     SIGPLAN International Conference on Certified Programs and Proofs (CPP 2020), pages
     367–381, 2020.

[26] Leonardo de Moura and Nikolaj Bjørner. Z3: An efficient smt solver. In Tools and Algorithms
     for the Construction and Analysis of Systems (TACAS 2008), volume 4963 of Lecture Notes
     in Computer Science, pages 337–340. Springer, 2008.

[27] Gurobi Optimization, LLC. Gurobi Optimizer Reference Manual, 2024.




                                              17

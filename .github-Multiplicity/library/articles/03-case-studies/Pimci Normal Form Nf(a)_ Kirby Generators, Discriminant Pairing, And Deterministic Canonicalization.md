---
slug: pimci-normal-form-nf-a-kirby-generators-discriminant-pairing-and-deterministic-canonicalization
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Pimci Normal Form Nf(a)_ Kirby Generators, Discriminant Pairing,
    And Deterministic Canonicalization.md
  last_synced: '2026-03-20T17:17:20.396179Z'
---

PIMCI Normal Form NF (A): Kirby Generators,
Discriminant Pairing, and Deterministic
Canonicalization
This document formalizes:


    1. Kirby generators as explicit matrix actions on a symmetric integral matrix A.
    2. The stable Kirby invariant (G(A), λA ) where G(A) = Zn /AZn and λA is the induced Q/Z-
       valued pairing.
    3. A deterministic normal form map NF such that for any Kirby word W ,

                                             NF (W [A]) = NF (A).

    4. An implementable pseudocode pipeline:

                  SNF → pairing matrix → p-primary split → canonical block reduction.

    5. An explicit block library for odd primes p and for p = 2 (finite abelian p-groups with nondegenerate
       symmetric pairings into Q/Z).

       Scope: This is a stable Kirby normal form for the discriminant pairing. For unimodular A
       (∣ det A∣ = 1), G(A) = 0 and the output is trivial; exotic-sphere sensitivity typically enters
       through an additional smooth channel κ (not expanded here).




1. Kirby generators as matrix actions
Let A ∈ Mn (Z) be symmetric.


(G0) Relabeling

For a permutation matrix P ,


                                               A ↦ P T AP .

(G1) Handle slide i ← i ± j

Let Eij have a single 1 at (i, j). For σ ∈ {+1, −1}, define


                                        U := I + σEij ∈ GLn (Z).

Then

                                               A ↦ U T AU .



                                                      1
                        =′ik = aik + σajk and symmetry gives a′ki similarly. - a′ii = aii + 2σaij + ajj . -
Entrywise: - For k  i: a
Other entries unchanged.


(G2) Stabilization

For ε ∈ {+1, −1},


                                                     A ↦ A ⊕ [ε].

A Kirby word W is any composition of these operations.




2. The invariant: discriminant group and linking pairing
Assume det(A)  0 (nondegenerate
                       =         over Q). Define


                                                 G(A) := Zn /AZn .

This is finite of order ∣ det(A)∣.


Define the induced symmetric pairing


                          λA : G(A) × G(A) → Q/Z,                 ˉ, yˉ) := xT A−1 y mod 1.
                                                              λA (x

Why Kirby moves preserve (G, λ)

      • Slides / relabeling: A′ = U T AU with unimodular U gives an induced isomorphism x
                                                                                        ˉ ↦ U −1 x
          preserving λ.
      • Stabilization: [±1] is unimodular so contributes a trivial discriminant summand.

Thus the isomorphism class of (G(A), λA ) is invariant under all Kirby words.




3. Definition of the normal form map NF

          Definition (stable Kirby normal form). NF (A) is a canonical encoding of the isomorphism
          class of the finite pairing (G(A), λA ).


Then for any Kirby word W :


                                              NF (W [A]) = NF (A).

To implement NF , we produce a deterministic decomposition of (G(A), λA ) into canonical prime-power
blocks.




                                                          2
4. Implementation pipeline overview
Input: symmetric integer matrix A with det(A)  0.             =

Output: a structured object


                                     NF (A) = { N Fp (A) : p ∣ det(A) }

where each N Fp is a list of canonical p-primary pairing blocks.


Pipeline: 1. Compute Smith normal form (SNF) of A. 2. Compute an explicit pairing matrix for λA on a
canonical SNF-derived basis. 3. Split into p-primary components. 4. For each p, perform canonical block
reduction using the block library.




5. Step 1: Smith normal form (SNF)
Compute unimodular S, V ∈ GLn (Z) such that


                                SAV = D = diag(d1 , … , dn ),           di ∣ di+1 .

Then

                                            G(A) ≅ ⨁ Z/di Z.
                                                      i:di    =1

The list (di ) is canonical.


Let I be the index set of nontrivial invariants {i : di > 1} and define


                                      DI := diag(di )i∈I ,         m := ∣I∣.

We will represent elements of G(A) by coordinate vectors u ∈ Zm modulo DI .




6. Step 2: pairing matrix in SNF coordinates
We need a matrix P ∈ Mm (Q/Z) such that for u, v ∈ Zm ,


                                          λ(u, v) = uT P v mod 1.

Constructing P

From SAV = D , note A = S −1 DV −1 , hence


                                               A−1 = V D−1 S.



                                                       3
Therefore for lifts x, y ∈ Zn ,

                                           ˉ, yˉ) = xT V D−1 Sy mod 1.
                                       λA (x

Restrict to the components in I : let πI project to those indices. Define

                                       P := πI (V T A−1 V )πIT mod 1.

Implementation-friendly version (avoids explicit A−1 ):

                                     P = πI (V T V D−1 SV )πIT mod 1.

In practice, compute over rationals with exact arithmetic and then reduce each entry to [0, 1) ⊂ Q
representing its class mod 1.


       Sanity: P is symmetric in Q/Z.




7. Step 3: p-primary split
For each prime p ∣ det(A): - Decompose each di into di = ∏p pei,p . - The p-primary subgroup is


                                            Gp ≅     ⨁ Z/pei,p Z.
                                                   i∈I:ei,p >0

- Restrict the pairing matrix P to the coordinates with ei,p > 0 and then project values to the p-primary
torsion of Q/Z, i.e. reduce denominators to powers of p.


Concretely, for an entry r ∈ Q/Z represented by a/b in lowest terms: - Keep only the p-power part: write
b = pt b′ with gcd(b′ , p) = 1. - Replace a/b by a(b′ )−1 /pt mod 1, where (b′ )−1 is inverse mod pt .

This yields a pairing λp on Gp .




8. Step 4: canonical block reduction
We now reduce (Gp , λp ) to a canonical direct sum of standard blocks.


8.1 Odd prime block library (p odd)

Every nondegenerate symmetric pairing on a finite abelian p-group decomposes as an orthogonal direct
sum of cyclic blocks:


      • Cyclic block C(pk , ϵ):

                                                   (Z/pk Z, ⟨ϵ/pk ⟩),

       meaning in the generator basis g ,




                                                         4
                                               λ(g, g) = ϵ/pk mod 1,

       where ϵ ∈ (Z/pk Z)× .

For odd p, ϵ is classified up to multiplication by a square; there are exactly two square-classes in (Z/pk Z)× :
residue and nonresidue.


Canonical choice of ϵ: - Let ηp be the smallest positive integer that is a quadratic nonresidue mod p (and
hence mod pk by Hensel lifting for odd p). - Represent the two classes by ϵ = 1 and ϵ = ηp .


So the odd-prime library is


                                  Bpodd = { C(pk , 1), C(pk , ηp ) : k ≥ 1 }.

8.2 The p = 2 block library

For 2-primary groups, one needs both 1-dimensional and certain 2-dimensional indecomposables.


Use the following standard blocks.


(A) 1D cyclic blocks (diagonal types)

     • A(2k , ϵ):

                                                  (Z/2k Z, ⟨ϵ/2k ⟩)

       where ϵ is odd.

Canonical representatives for ϵ modulo squares in (Z/2k )× can be taken as: - for k = 1: only ϵ ≡ 1 (since
Z/2^\times) is trivial) - for k = 2: ϵ ∈ {1, 3} - for k ≥ 3: ϵ ∈ {1, 3, 5, 7} (these represent the four square-
classes of odd units mod 2k ).


So include


A2,k = {{A(2, 1)}        k = 1 {A(4, 1), A(4, 3)} k = 2 {A(2k , 1), A(2k , 3), A(2k , 5), A(2k , 7)}    k ≥ 3.

(B) 2D “hyperbolic” blocks

     • H(2k ): group (Z/2k )2 with Gram matrix

                                          1 0      1
                                            (       )       (entries in Q/Z).
                                          2k 1     0

(C) 2D “twisted hyperbolic” blocks

     • T (2k ): group (Z/2k )2 with Gram matrix




                                                        5
                                                       1 2    1
                                                         (     ).
                                                       2k 1   2

Thus the 2-adic library is


                                    B2 = ⋃ (A2,k ∪ {H(2k ), T (2k )}).
                                          k≥1


       Note: This library is standard for nondegenerate symmetric bilinear pairings on 2-groups; the
       diagonal-only family is not sufficient in general, hence H and T .




9. Deterministic canonical block reduction algorithm
We now give implementable pseudocode that takes: - {ei } generators with orders pki , - a pairing matrix
Pp ∈ Mm (Q/Z) whose entries have denominators powers of p,

and returns a canonical multiset of blocks from Bp .


9.1 Helper operations

      • order(i) : returns pki .
      • val_p(x) : p-adic valuation of a rational number represented as a/pt (so val_p(a/p^t) = -t if
       p ∤ a).
      • reduce_mod_1(q) : reduce rational to [0, 1).
      • Basis change by unimodular matrix over Z respecting the abelian invariants: use elementary
       column/row operations corresponding to changing generators.

9.2 Odd p: diagonalization into cyclic blocks

For odd p, we can deterministically diagonalize.


Pseudocode (odd prime reduction):



  function CanonicalBlocksOddP(p, orders[k1..km], P):
       blocks = []
       # Work from largest exponent down for determinism
       while m > 0:
           # Choose pivot generator i deterministically:
           # 1) max order, 2) smallest index among ties
           i = argmax_i(orders[i])
           k = log_p(orders[i])

          # Find j such that pairing with i has minimal p-valuation (strongest
  coupling)
          # Prefer diagonal if nonzero.




                                                        6
        if P[i,i] != 0:
            j = i
        else:
            j = argmin_j(val_p(P[i,j])) over j with P[i,j] != 0


        # If j != i, change basis to make diagonal pivot nonzero (odd p allows
this)
        if j != i:
            # Replace generator i by i + t*j to make P[i,i] nonzero
            # Choose smallest t in {0..p-1} that works.
            for t in 0..p-1:
                if P[i,i] + 2*t*P[i,j] + t*t*P[j,j] != 0:
                    apply basis change: e_i <- e_i + t*e_j
                    update P accordingly
                    break

        # Now diagonal entry P[i,i] is nonzero: it defines a cyclic block
        # Normalize to epsilon/p^k
        q = P[i,i] # element of Q/Z with denom p^k'
        # Reduce q to form a/p^k (k determined by order), ensure gcd(a,p)=1
        a, kk = normalize_to_unit_over_p(q) # q = a/p^kk with p∤a
        # For a generator of order p^k, enforce kk == k by rescaling generator
if needed
        # (Implement by splitting off smaller-order components first.)

        # Determine square-class of a mod p:
        if is_quadratic_residue_mod_p(a, p):
            eps = 1
        else:
            eps = eta_p(p) # smallest nonresidue mod p

        blocks.append( C(p^k, eps) )


        # Orthogonalize: kill row/col i against all others
        for r != i:
            # choose u to eliminate P[r,i] using diagonal pivot P[i,i]
            u = P[r,i] / P[i,i] (computed in Z/p^k)
            apply basis change: e_r <- e_r - u*e_i
            update P

        # Remove i from the system
        delete row/col i from P
        delete orders[i]
        m = m - 1

   # Sort blocks canonically by (k, eps) then return
   return sort(blocks)




                                       7
9.3 p = 2: reduction with 1D and 2D blocks

For 2, diagonalization may fail; we extract either a 1D diagonal block, or a 2D H or T block.


Deterministic extraction strategy: 1. Work by largest order first. 2. Prefer extracting a 1D block when you
can find an element with λ(x, x)  0. 3. Otherwise
                                           =       extract a 2D block from a pair with λ(x, y) having
maximal 2-adic denominator.


Pseudocode (2-adic reduction):



  function CanonicalBlocks2(orders[2^k1..2^km], P):
      blocks = []
      while m > 0:
          i = argmax_i(orders[i])
          k = log2(orders[i])

          if P[i,i] != 0:
              # 1D extraction
              q = P[i,i] # in Q/Z with denom 2^t
              eps = canonical_odd_unit_class(q, k)                 # maps to {1} or {1,3} or
  {1,3,5,7}
              blocks.append( A(2^k, eps) )

                  # Orthogonalize against others using pivot
                  for r != i:
                      u = solve_for_u_to_kill(P[r,i], P[i,i], 2^k)
                      e_r <- e_r - u*e_i
                      update P

                  delete i
                  continue

            # If diagonal is zero, try to form 2D block with some j
            # Choose j that maximizes denominator (i.e., minimizes valuation) of
  P[i,j]
            j = argmin_j(val2(P[i,j])) over j with P[i,j] != 0


          # Now classify the 2D form on span{i,j}
          # We have Gram matrix [[0, b],[b, c]] (after possible basis tweaks),
  with b != 0.
          # Make b = 1/2^k via scaling within allowed generator changes.
          normalize_pair(i, j) # deterministic basis changes to standardize
  cross-term

            # Decide whether this is H(2^k) or T(2^k)
            if can_make_diagonals_zero():




                                                      8
                blocks.append( H(2^k) )
            else:
                blocks.append( T(2^k) )

            # Orthogonalize remaining generators against span{i,j}
            for r not in {i,j}:
                eliminate_pairings_with_span(r, i, j)

            delete i and j


       return sort(blocks)


Notes for implementers (2-adic details): - canonical_odd_unit_class(q,k) : - write q = a/2t with
odd a. Reduce to modulus 2k and map a into the canonical representative set: - k = 1: {1} - k = 2: {1,3} -
k ≥ 3: {1,3,5,7} - normalize_pair(i,j) and can_make_diagonals_zero() are standard 2-adic basis
adjustments on the 2D span; implement deterministically by trying a fixed ordered list of substitutions (e.g.,
ei ← ei + tej for t ∈ {0, 1}, then ej ← ej + tei , etc.) and selecting the first that matches the target
pattern.




10. Full pseudocode for NF (A)

  function NF(A):
      assert A is symmetric integer matrix
      assert det(A) != 0

       # Step 1: SNF
       S, D, V = SmithNormalForm(A)           # S*A*V = D diag(d1..dn)
       I = [i : D[i,i] > 1]
       d = [D[i,i] for i in I]

       if len(I) == 0:
           return {} # unimodular: trivial discriminant

       # Step 2: pairing matrix in SNF coords
       # Use A^{-1} = V * D^{-1} * S
       # Compute B = V^T * A^{-1} * V = V^T * V * D^{-1} * S * V
       B = transpose(V) * V * inverse_diag(D) * S * V # exact rationals
       P = restrict(B, I, I) # m x m rational matrix
       P = entrywise_reduce_mod_1(P)

       # Step 3: p-primary split
       primes = prime_factors(abs(det(A)))
       NF_out = {}

       for p in sorted(primes):



                                                      9
            # indices in I whose invariant factor has p-power
            Ip = [t in 1..m such that v_p(d[t]) > 0]
            if Ip empty:
                continue


            orders = [p^{v_p(d[t])} for t in Ip]
            Pp = restrict(P, Ip, Ip)
            Pp = project_pairing_to_p_primary(Pp, p)


            # Step 4: canonical block reduction
            if p != 2:
                blocks = CanonicalBlocksOddP(p, orders, Pp)
            else:
                blocks = CanonicalBlocks2(orders, Pp)

            NF_out[p] = blocks

       return NF_out


Output format suggestion: for each primep, return a list like - odd p: [(k, eps_tag,
multiplicity), ...] where eps_tag ∈ {res, nonres} - p = 2: [(type, k, params,
multiplicity), ...] where type ∈ {A,H,T} and params is the canonical ϵ if type A.




11. Determinism rules (to guarantee identical output)
Whenever there is a choice: 1. Prefer largest-order generators first. 2. Break ties by smallest index. 3. For
basis changes, try coefficients in a fixed ordered set (odd p: t = 0..p − 1; p = 2: t ∈ {0, 1}) and take the
first that achieves the target. 4. Sort blocks canonically at the end by a fixed key: - odd p: sort by
(k, eps_tag) - p = 2: sort by (type_order, k, params) with A < H < T .

These rules ensure NF is a deterministic function, not just an isomorphism class.




12. Invariance theorem (the guarantee)
Theorem. Let ∼ be the equivalence relation generated by Kirby generators (G0–G2). If A ∼ A′ , then
NF (A) = NF (A′ ).

Reason. Each generator preserves the isomorphism class of (G(A), λA ). The pipeline computes a
canonical representative of that isomorphism class, hence is invariant under any Kirby word.




                                                     10
13. Practical caution for exotic spheres
If ∣ det A∣ = 1, the discriminant pairing is trivial and NF (A) will be empty.


For exotic-sphere detection you typically extend the carrier with a smooth refinement channel κ (e.g.,
Pontryagin/characteristic correction). Then define


                     N Fsmooth (A, κ) := (NF (A), NF (κ in matching prime tiers)).

This document provides the stable Kirby normal form part (NF (A)).




                                                      11

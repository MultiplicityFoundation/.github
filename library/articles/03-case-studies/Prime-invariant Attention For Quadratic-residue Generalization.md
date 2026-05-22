---
slug: prime-invariant-attention-for-quadratic-residue-generalization
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Prime-invariant Attention For Quadratic-residue Generalization.md
  last_synced: '2026-03-20T17:17:20.604686Z'
---

Final Project Report: Prime‑Invariant Attention for
Quadratic‑Residue Generalization
Executive summary
This project implements and validates a prime-conditioned, symmetry-regularized attention model
designed to learn algebraic properties over the multiplicative group F∗p and generalize out-of-distribution
(OOD) to unseen primes. The final system combines:


       • A ratio-based quadratic-residue attention mask (structural inductive bias).
       • A multiplicative permutation group action over residue indices (correct symmetry).
       • An invariance regularizer applied to pre-mask attention logits (clean separation of symmetry
         from task constraints).
       • A pair-query head that is exactly symmetric under swapping the queried pair.
       • A train/val/test split by primes with validation-based λ selection and paired statistical testing.

The final setup is engineered to avoid earlier confounds (ill-posed ratio queries, label/mask equivalences,
asymmetry bugs, device/dtype hazards, and test-set hyperparameter leakage).




Scientific goal and hypothesis

Goal

Learn an algebraic predicate over pairs (i, j) ∈ F∗p × F∗p from training primes and generalize to unseen
primes.


Core hypothesis

Adding (1) structure-aware masking and (2) correct symmetry regularization improves OOD
generalization more than: - no structure (baseline), - mask alone, - invariance alone, - or invariance under an
intentionally wrong symmetry.




Final task definition

Input

For each prime p, a sequence of tokens in canonical order: - tokens = [1,2,...,p-1] (length n = p −
1)

A query is a pair of positions (i, j) (indices into the token sequence).




                                                       1
Label (final choice)

A symmetric and multiplicatively invariant binary label:


                         label(i, j) = 1{ i2 + j 2 is a quadratic residue mod p }.

Why this label: - Symmetric under swap: i2 + j 2 = j 2 + i2 . - Invariant under multiplicative action: for
a ∈ F∗p ,

                                        (ai)2 + (aj)2 = a2 (i2 + j 2 ),

and a2 is always a quadratic residue, so the quadratic-residue status is unchanged.


Prime choice rationale

Primes are chosen with p ≡ 3 (mod 4) (e.g., 7, 11, 19, 23, 31, 43) so that i2 + j 2 ≡ 0 (mod p) has no
nontrivial solutions with i, j  0. This
                                     = removes a special-case label corner and yields a cleaner binary
predicate.




Structural mask (attention constraint)
A ratio-based quadratic-residue mask constrains which keys each query can attend to:


                            M (i, j) = 1{ i ⋅ j −1 is a quadratic residue mod p }.

Implementation: - Precompute the QR set using Euler’s criterion. - Construct mask_bias[i,j] = 0 if
allowed, else -inf . - Apply mask bias after computing base logits.


Important: The mask is a bias/constraint; it is not the label. The final label is different (sum-of-squares QR),
eliminating mask–label equivalence.




Symmetry and group actions

Correct symmetry: multiplicative action

The multiplicative group F∗p acts on residues by multiplication. This induces a permutation of indices in the
canonical token ordering.


For a multiplier a, indices are permuted by applying a−1 to preserve the canonical order mapping: - Build
inverse permutation     inv_perm     such that residue r ↦ a−1 r maps to the corresponding 0-indexed
position.




                                                       2
Wrong symmetry controls

To falsify “any invariance helps,” we include: - Shift action: cyclic index shifts modulo n = p − 1. - Random
action: fixed random permutations; store inverse permutations for correct conjugation behavior.


Device-cached permutations

All inverse permutations are: - precomputed on CPU, - cached per-device on first use to avoid repeated
 .to(device) overhead.




Model architecture

Encoder: Fourier features over residue values

Each token value i ∈ {1..p − 1} is embedded using Fourier features of t = i/p and log p, then projected
to d_model .


Attention block: shared single head

SharedPrimeAttentionHead          computes: -   base_logits = QK^T / sqrt(d_head)               (pre-mask) -
logits = base_logits + mask_bias (optional) - attention = softmax(logits) - output =
W_o(attention V)


Key design choice: invariance regularization is applied to base_logits, not masked logits.


Pair head: symmetric classifier

The pair-query head consumes the two contextual hidden states hi and hj and outputs class logits.


To guarantee swap symmetry: - Use only symmetric features: - hi + hj - hi ⊙ hj - ∣hi − hj ∣


Then apply an MLP to predict {0, 1}.




Regularizers

Invariance loss (symmetry regularization)

Given base logits L ∈ Rn×n and a set of group actions g , enforce:


                                         Linv = Eg ∥L − g ⋅ L∥2 .




                                                     3
Implementation details: - Conjugate logits by inverse permutations on both axes. - Average across the
configured action set. - (Recommended) normalize by n2 via mean over the last two dims to make λ
comparable across primes.


Stability loss

The project includes an optional attention-entropy stability loss, but the final experiments keep
 use_stability=False to isolate the effect of mask + invariance.




Dataset generation and balancing

Balanced sampling (train/val)

For each prime: - Sample random distinct pairs (i, j). - Compute the label. - If balancing is enabled, accept
examples until reaching ~50/50 per class. - Increase max_attempts_factor to avoid premature failure.


Natural sampling (test)

Test sets use balance_classes=False to evaluate under the natural distribution.


Reporting

The dataset prints per-prime class counts (and warns if balancing cannot be achieved within attempt limits).




Training protocol

Prime-homogeneous batching

A PrimeHomogeneousSampler forms batches where all samples share the same prime p. This ensures: -
consistent sequence length n = p − 1, - a single shared mask per batch, - coherent invariance action per
batch.


Hyperparameter selection (no test leakage)

      • Sweep λinv ∈ {0.01, 0.1, 1.0}.
      • Select the best λ using validation primes only.
      • Report test accuracy on unseen primes using the selected λ.

(Optionally: select λ per-seed for strict paired testing; both approaches avoid using test labels for tuning.)




                                                       4
Experiment matrix
Each condition is run with multiple random seeds.


    1. baseline: no mask, no invariance
    2. mask_only: mask only
    3. invariance_only: invariance only (correct symmetry)
    4. full: mask + invariance (correct symmetry)
    5. wrong_symmetry_shift: mask + invariance under shift actions
    6. wrong_symmetry_random: mask + invariance under random permutations

Primary comparisons: - full vs baseline - full vs wrong_symmetry_random




Sanity checks (final)

1) Swap symmetry (end-to-end)

     • Compute predictions for (i, j) and (j, i).
     • Verify max absolute logit difference is < 10−6 .

2) Mask invariance under multiplicative action

     • Permute the mask using each multiplier action.
     • Verify exact equality up to numerical tolerance.

3) Invariance loss is nontrivial

     • Compute invariance loss on random logits.
     • Expect a clearly positive value (unless identity-only actions).

These sanity checks are run early (first seed / first lambda) to catch implementation regressions.




Statistical testing
Given paired seeds across conditions, use exact sign-flip (paired permutation) tests: - Compute per-seed
test accuracies for two conditions. - Compute differences and enumerate all sign flips (for n = 5, only 32
combinations). - Report one-sided p-values for improvement.


Success criteria (typical): - full beats baseline with p < 0.05 and meaningful effect size. - full beats
wrong_symmetry_random with p < 0.05 and meaningful effect size.




                                                        5
Reproducibility checklist
     • Fixed seed handling for each lambda evaluation.
     • Deterministic group actions (including random permutation actions) via fixed generator seeds.
     • Device-cached permutations and dtype-safe masks.
     • Prime-homogeneous batching.
     • Validation-based lambda selection.




Known limitations and recommended last-mile improvements
    1. Invariance loss scaling: use mean over n × n rather than sum for better cross-prime comparability.
    2. Empty-action edge case: ensure invariance loss returns logits.new_zeros(()) if action list is
       empty.
    3. Balanced sampling robustness: if balancing repeatedly fails for a prime, fall back to weighted CE
       (optional) or increase attempts.
    4. Per-seed lambda selection: improves strictness of paired tests (still no test leakage).




Final deliverable
The final codebase implements a complete, self-contained experimental pipeline: - dataset generation with
balanced train/val and natural test, - model with symmetry-aligned pair head, - multiplicative invariance
regularization and wrong-symmetry controls, - comprehensive sanity checks, - validation-based tuning, -
paired statistical evaluation.


This provides a decisive, well-controlled test of whether algebraic structure + correct symmetry
regularization improves OOD generalization to unseen primes.




                                                      6

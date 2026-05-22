---
slug: qpf-lab-associator-spectroscopy-final-engineering-spec
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "03-case-studies/Qpf Lab \u2014 Associator Spectroscopy (final Engineering\
    \ Spec).md"
  last_synced: '2026-03-20T17:17:20.382052Z'
---

QPF Lab — Associator Spectroscopy (Final
Engineering Spec)
Purpose. QPF is a falsifiable discovery procedure for perceptual composition. It learns (i) a minimal set of
nonnegative perceptual “primes” and (ii) a lawful composition operator that predicts human judgments on
mixtures. The associator is treated as a structural anomaly detector: persistent non-associativity is used to
discover missing latent macrostates (e.g., context/adaptation), or else to certify irreducible non-associativity
under a fixed class of lawful augmentations.




1. Goals and falsifiable hypotheses

Goal

Discover a low-rank, interpretable percept basis and an admissible percept-composition law that predict
out-of-sample responses to binary and ternary mixtures, while separating stimulus mixing from percept
mixing.


Core hypotheses

       • H1 (Low-rank + lawful beats unconstrained): A low-dimensional prime basis with a lawful
         composition operator predicts held-out judgments (especially ternary mixes) better than
         unconstrained baselines at matched complexity.
       • H2 (Netting selectivity): Where cancellation is behaviorally licensed, extending the state to a group-
         complete form improves predictive evidence; otherwise it does not.
       • H3 (Closure defect): Most measured non-associativity across triple mixes is a closure defect that
         collapses after adding a minimal latent macrostate (often context/adaptation).




2. Mathematical foundation (Option A: latent-space order +
extended cone)

2.1 Spaces

       • Stimulus space: S ⊆ RC
                              ≥0 (C stimulus channels).
       • Latent percept space: Z = Rm
                                    ≥0 with cone K = Z and partial order z ⪰ z
                                                                               ′
                                                                                        ⟺ z − z′ ∈ K .

2.2 Prime dictionary (nonnegative factorization)

       • Representation: $$ z = P a,\quad P \in \mathbb{R}^{m\times K}{\ge 0},\ a \in \mathbb{R}^K. $$}\
         \text{(sparse)
       • Practical parameterization: P = softplus(P_raw) and a = softplus(a_raw) .




                                                       1
Scale/identifiability anchors (required):


      • Column-normalize dictionary (e.g., L1): ∑i Pik = 1 for each prime k .
      • Normalize magnitude weights (e.g., ∥w∥1 = 1).

2.3 Magnitude and aspects

      • Magnitude functional: J(z) = w ⊤ z , with w ∈ Rm
                                                       ≥0 .
                                      ℓ z , with uℓ ∈ R≥0 .
      • Aspect intensities: Iℓ (z) = u⊤                m


Immediate consequences:


      • Monotonicity is structural if the operator preserves the cone order.
      • Contractivity is meaningful and compatible with nonnegativity.

2.4 Netting-enabled aspects (extended cone)

For aspects where cancellation is behaviorally licensed, represent signed percepts as differences of
positives:


$$ (z^+, z^-) \in K \times K,\quad z_{net} = z^+ - z^-. $$


Use magnitude on the extended state:


$$ J(z^+,z^-) = w^\top(z^+ + z^-) $$


so cancellation cannot be gamed via large opposing components.




3. Percept composition operators (lawful by construction)
All operators take an explicit mix proportion α ∈ [0, 1]:


$$ \otimes_\alpha: Z\times Z \to Z. $$


3.1 LRS (Linear receptor-sum surrogate)

$$ \mathrm{LRS}_\alpha(z_1,z_2) = \alpha z_1 + (1-\alpha) z_2. $$


Guarantees: cone-preserving, order-preserving, and J -contractive.


3.2 DN (Divisive normalization) — two variants

Variant A: Coordinatewise DN (recommended for v1.0)

$$ \mathrm{DN}^{coord}_\alpha(z_1,z_2) = \frac{n}{1+\sigma + \gamma n},\quad n=\alpha z_1+(1-
\alpha)z_2,\ \sigma,\gamma\ge 0. $$



                                                         2
Guarantees: cone-preserving, order-preserving, and J -contractive.


Variant B: Global DN (optional menu item)

$$ \mathrm{DN}^{global}_\alpha(z_1,z_2) = \frac{n}{1+\sigma + \gamma\,J(n)},\quad n=\alpha z_1+(1-
\alpha)z_2. $$


Guarantees: cone-preserving and         J -contractive due to denominator ≥ 1. Not guaranteed order-
preserving under the cone order; treat monotonicity as a diagnostic/penalty when using this operator.




4. Context / adaptation macrostate (Patch A: fixed dimensionality)

4.1 Scalar context state

Project stimulus to a nonnegative scalar signal:


$$ \xi(s) = q^\top s,\quad q\ge 0. $$


Exponential smoothing update:


$$ h_{t+1} = \lambda h_t + (1-\lambda)\,\xi(s_t),\quad \lambda\in[0,1]. $$


4.2 Context injection (cone-lawful)

        • Additive: zt = P at + vht , with v ≥ 0.
        • Divisive (often more realistic): zt = (P at )/(1 + ηht ), with η ≥ 0.

Note on suppressive adaptation

If adaptation must subtract directionally, implement it in the extended cone (signed) state, or as
multiplicative gain control (divisive), not as subtraction in Z .




5. Carrier invariance (correct invariants)
A strict identity element for all α  1 is
                                        = generally incompatible with convex-mixture operators. QPF v1.0
uses:


    1. Endpoint identity:


    2. ⊗α=1 (z1 , z2 ) = z1


    3. ⊗α=0 (z1 , z2 ) = z2




                                                        3
     4. Carrier “no-new-direction” invariance: Let the carrier encode to z0 ≈ 0. Then


$$ \otimes_\alpha(z,z_0) \approx \kappa(\alpha,z)\,z,\quad \kappa\ge 0. $$


Implementation check: high cosine similarity between normalized z and ⊗α (z, z0 ).




6. Associator spectroscopy (discovery loop)

6.1 Associator definition

For triples (z1 , z2 , z3 ) and mix proportions (α, β):


$$ A = d\Big(R(\otimes_\beta(\otimes_\alpha(z_1,z_2),z_3)),\ R(\otimes_\alpha(z_1,\otimes_\beta(z_2,z_3)))
\Big) $$


      • Observable distance d (v1.0): L2 difference in predicted aspect means plus triangle-test cross-
       entropy.

6.2 Noise-calibrated signal

Estimate associator noise floor σA via repeats / bootstrap.


$$ S(M) = \frac{\mathbb{E}[A]}{\widehat{\sigma}_A} $$


Stop when S(M ) ≤ τ (e.g., τ = 1.1).


6.3 Minimal augmentation menu (cone-lawful)

Each augmentation must preserve cone structure by construction.


      • context_1d : add h with positive projection q and injection v (additive or divisive).
      • extra_prime : increase K → K + 1 (nonnegative new column and activation).
      • subject_slope : subject-specific positive scaling on uℓ or on readout gains.
      • operator_mixing : convex mix of LRS and DN, β ∈ [0, 1].
      • sparse_interaction : safe, bounded, nonnegative interaction term (typically with additional
       normalization to avoid blow-up).

6.4 Selection criterion (“no free wins”)

Adopt an augmentation only if:


      • held-out ternary ELPD improves (veto otherwise),
      • associator signal S decreases meaningfully,
      • complexity-adjusted score improves:




                                                          4
$$ \Delta\mathrm{Score} = \Delta\mathrm{ELPD}_{ternary} - \lambda\,\Delta\mathrm{Complexity} -
\gamma\,\Delta S $$


If no augmentation improves score, declare irreducible non-associativity under the menu (scientific
result).




7. Training objective (v1.0)
Let data include ratings y and triangle outcomes t.


Likelihood:


     • Ratings: Gaussian or ordinal-logit (depending on scale).
     • Triangle test: multinomial / logistic.

Regularization / priors (implemented as penalties):


     • Sparsity on a: L1 or structured sparse gates.
     • Carrier-null penalty: encourage zcarrier ≈ 0.
     • Optional continuity penalty: Lipschitz surrogate on readouts.
     • Monotonicity penalty: only required if using DN_global or other non-monotone operators.




8. Unit-test invariants (run during training)
Hard asserts for LRS and DN_coord ; diagnostics (soft checks) for DN_global .


    1. Cone closure: ⊗α (z1 , z2 ) ∈ K .
    2. Endpoint identity: ⊗1 (z1 , z2 ) = z1 , ⊗0 (z1 , z2 ) = z2 .
    3. J-contractivity: J(⊗α (z1 , z2 )) ≤ max(J(z1 ), J(z2 )).
    4. Carrier no-new-direction: cosine similarity between normalized z and ⊗α (z, z0 ) near 1.
    5. Order preservation (when guaranteed): if z1′ ⪰ z1 , then I(⊗α (z1′ , z2 )) ≥ I(⊗α (z1 , z2 )).




9. Implementation plan (week 1–2)

Week 1

     • Implement QPFBase : softplus constraints, column normalization for P , normalized w , positive
        U .
     • Implement LRS and DN_coord (plus optional DN_global ).
     • Implement associator() and noise-floor bootstrap.
     • Add carrier-null penalty and L1 sparsity on a .
     • Add invariant tests to CI / training loop.




                                                          5
Week 2

      • Implement context_1d augmentation wrapper (projection q , state h, injection).
      • Implement scoring + veto rule (ternary ELPD must not degrade).
      • Add associator heatmaps and “associator spectroscopy” iteration driver.




10. Minimal dataset schema (starter)
      • subjects: subject_id , demographics, session info
      • stimuli: stimulus_id , component_vector (length C), intensity_level , carrier_id
      • trials: trial_id , subject_id , task_type {rating, triangle, similarity},
        (s_a_id,s_b_id,alpha) and optional (s_c_id,beta) ; presentation order; timestamp
      • responses: ratings per aspect; triangle choice/correct; similarity score/choice
      • aspects: aspect_id , scale spec, netting_allowed flag




External references (selected)
Divisive normalization / canonical computations


     1. Heeger, D. J. (1992). Normalization of cell responses in cat striate cortex. Visual Neuroscience.
     2. Carandini, M., & Heeger, D. J. (2012). Normalization as a canonical neural computation. Nature Reviews
        Neuroscience.
     3. Reynolds, J. H., & Heeger, D. J. (2009). The normalization model of attention. Neuron.

Nonnegativity, sparse representations, parts-based bases 4. Lee, D. D., & Seung, H. S. (1999). Learning
the parts of objects by non-negative matrix factorization. Nature. 5. Olshausen, B. A., & Field, D. J. (1996).
Emergence of simple-cell receptive field properties by learning a sparse code for natural images. Nature.


Bayesian model checking, predictive validation, and model comparison 6. Gelman, A., Meng, X.-L., &
Stern, H. S. (1996). Posterior predictive assessment of model fitness via realized discrepancies. Statistica Sinica. 7.
Vehtari, A., Gelman, A., & Gabry, J. (2017). Practical Bayesian model evaluation using leave-one-out cross-
validation and WAIC. Statistics and Computing.


Bayesian experimental design / active information acquisition 8. Chaloner, K., & Verdinelli, I. (1995).
Bayesian experimental design: A review. Statistical Science.


Adaptation / context as a latent macrostate 9. Webster, M. A. (2011). Adaptation and visual coding. Journal
of Vision.


Associativity and functional-equation constraints 10. Aczél, J. (1966). Lectures on Functional Equations and
Their Applications. Academic Press.




                                                          6
Group completion / algebraic foundations (for netting toggle) 11. Mac Lane, S. (1998). Categories for the
Working Mathematician (2nd ed.). Springer. (Background on Grothendieck group completion of commutative
monoids.)


Citizen Gardens © 2025 CC-NC-ND 4.0




                                                   7

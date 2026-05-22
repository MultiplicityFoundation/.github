---
slug: qpf-methods-protocol-gallows-proof-v1
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Qpf Methods Protocol (gallows-proof, V1.md
  last_synced: '2026-03-20T17:17:20.965664Z'
---

Qualitative Prime Factorization (QPF)
Gallows-Proof Methods Protocol (v1.0)

Purpose

QPF is a falsifiable methodology for discovering empirical qualitative generators (“primes”)—minimal sets of
perceptual qualities that, together with a biologically admissible composition operator, best predict and
compress perceptual data from mixture stimuli. QPF treats “primeness” as model- and constraint-relative,
and operationalizes emergence via predictive generalization + complexity penalties.




1. Formal Setup
1.1 Data
Let the dataset be


$$ D={(s_i,r_i)}_{i=1}^N, $$


where stimuli si ∈ RC
                    ≥0 are concentration vectors over C compounds and responses ri include any subset
of:

                               (c)
      • Continuous ratings yi        ∈R
                         (o)
      • Ordinal ratings yi ∈ {1, … , K}
                                 (d)
      • Discrimination outcomes yi ∈ {0, 1} (e.g., triangle tests)
      • Similarity judgments zab ∈ [0, 1] or forced-choice comparisons


1.2 Two-Layer Structure
We separate stimulus composition from percept composition.


Stimulus layer

      • Stimulus space: S = RC
                             ≥0
      • Physical mixture operator (example for solutions): $$ s\otimes_S t := \lambda s + (1-\lambda)t,\qquad
        \lambda\in[0,1]. $$
      • Carrier (identity stimulus): 1S := 0 (base matrix/solvent; domain-specific).




                                                      1
Percept layer

We represent percepts through a latent coordinate z and a representation map R that yields an
observable percept object μ ∈ P .


      • Latent percept coordinate: z ∈ Rm (e.g., descriptor logits, intensity coordinates, or a learned
        embedding).
      • Representation map R:
      • Option A (Simplex): μ = R(z) = softmax(z) ∈ Δm−1
      • Option B (Gaussian): μ = R(z, Σ) = N (z, Σ)

Define the percept mapping (learned):


$$ (z_i,\Sigma_i)\sim F_{\phi}(s_i),\qquad \mu_i := R(z_i,\Sigma_i). $$


(For simplex, Σi is omitted.)


Induced percept composition

Percept composition is defined in latent space via ⊗z (family-dependent) and then mapped to μ:


$$ z_{a\otimes b} := z_a\otimes_z z_b\quad \Rightarrow \quad \mu_{a\otimes b}:=R(z_{a\otimes b},
\Sigma_{a\otimes b}). $$


Neutral percept: 1P := R(0, Σ0 ) (or softmax(0) for simplex).



A candidate percept composition operator ⊗P (implemented via ⊗z and R) is admissible if it satisfies the
following (interpreted in the chosen representation):


2.1 Continuity
For all ϵ > 0 there exists δ > 0 such that


$$ d(\mu_a,\mu_a')<\delta\ \Rightarrow\ d(\mu_a\otimes\mu_b,\mu_a'\otimes\mu_b)<\epsilon. $$


2.2 Monotonicity (on designated intensity functionals)
Choose intensity functionals Iℓ (μ) (e.g., sweetness, bitterness), typically linear in latent space (e.g.,
Iℓ (μ) = wℓ⊤ z ). Require:

$$ I_\ell(\mu_a)\le I_\ell(\mu_b)\ \Rightarrow\ I_\ell(\mu_a\otimes\mu_c)\le I_\ell(\mu_b\otimes\mu_c) $$


for relevant ℓ.




                                                        2
2.3 Contractivity (intensity magnitude)
Let J(μ) be an overall intensity magnitude (e.g., ∥z∥2 ). Require:


$$ J(\mu_{a\otimes b})\le \max{J(\mu_a),J(\mu_b)}. $$


(This allows nonlinear interactions in shape/direction while preventing runaway “super-intensity.”)


2.4 Approximate associativity
$$ d\big((a\otimes b)\otimes c,\ a\otimes(b\otimes c)\big)<\epsilon. $$


2.5 Carrier invariance
$$ \mathbf 1_P\otimes\mu=\mu\otimes\mathbf 1_P=\mu. $$


2.6 Enforcement as priors/penalties
Admissibility is imposed via constrained parameters and/or soft penalties:


$$ p(\theta)\propto \exp\Big(-\sum_k \lambda_k\,\mathrm{violation}_k(\theta)\Big). $$




3. Computability Layer (Type-2 Effectivity /
Computable Analysis)
3.1 Assumptions
     • Law class L = {L1 , L2 , … } computably enumerable.
     • Weights π(Li ) uniformly lower semicomputable with ∑i π(Li ) ≤ 1.
     • Point probabilities (i, n) ↦ PLi (N = n) uniformly computable as reals.


3.2 Core results

Theorem 3.2.1 (Effectivity of count mixtures)

$$ \lambda_N(n):=\sum_{i=1}^{\infty}\pi(L_i)\,\mathbb P_{L_i}(N=n) $$


is a lower semicomputable semimeasure.


Corollary 3.2.2 (Unattainability)

Any q that is not a lower semicomputable semimeasure cannot equal λN under the above assumptions.



                                                        3
Theorem 3.2.3 (Universality)

Every lower semicomputable semimeasure is attainable in some computable setup (allowing degenerate
laws).


3.3 Structural restriction: convolution closure
Assume:


       1. (W , ⊗) is a commutative monoid (disjoint-union semantics).
       2. Additivity: N (w ⊗ w ′ ) = N (w) + N (w ′ ).
       3. Independent composition: for independent w, w ′ ∼ L, the composed world has law L⊗2 .
       4. Closure under k -fold replication.

Then for each L, the count distribution pL = (N )∗ PL satisfies


$$ p_L^{(k)}=p_L^{*k}\quad \forall k\in\mathbb N. $$


Hence mixtures λN = ∑L π(L)pL lie in the convex hull of a convolution-closed family.


3.4 Tail bound theorem (explicit tail hypotheses)
If subsystem count S and per-subsystem maximum E have exponential tails and Nmax ≤ ηE with η ≤ S ,
then


$$ \Pr(N_{\max}\ge n)\le C\exp(-\alpha\sqrt n) $$


for some C, α > 0 determined by those tail constants and the η -mixing.




4.1 Canonical gustatory pathway scaffold
       1. Receptor binding (example Hill form): Rc (s) = K s+s
                                                            c
                                                             c   c



       2. Early population drive: xn = ∑c wnc Rc (s) + ϵn


       3. Divisive normalization (canonical sensory computation):


$$ y_m=\frac{\sum_n v_{mn}x_n^+}{\sigma_m+\sum_k\alpha_{mk}x_k^+} $$


       1. Percept readout (example logits): z = β ⊤ y and μ = R(z).

Let λ ∈ [0, 1] be the physical mixture weight.




                                                         4
Family 1: LRS (Linear receptor-sum surrogate)

$$ z_{a\otimes b}=\lambda z_a+(1-\lambda)z_b. $$


Constraints: nonnegative tuning where appropriate (domain-justified).


Family 2: DN (Divisive normalization)

$$ z_{a\otimes b}=\frac{\lambda z_a+(1-\lambda)z_b}{\sigma+\lambda|z_a|_1+(1-\lambda)|z_b|_1},\qquad
\sigma>0. $$


Family 3: LB (Logistic binding / sparse interactions)

$$ z_{a\otimes b}=\lambda z_a+(1-\lambda)z_b+\rho\,(z_a\odot z_b),\qquad \rho\ \text{sparse and
bounded}. $$


Then μa⊗b = softmax(za⊗b ) (simplex) or N (za⊗b , Σa⊗b ) (Gaussian).




5. Statistical Model (Likelihoods + Mixture-
Consistency Penalty)
5.1 Measurement likelihoods
Let μi be the percept object for stimulus si .


Continuous ratings

$$ y_i^{(c)}\sim \mathcal N\big(I_c(\mu_i),\sigma_c^2\big). $$


Ordinal ratings (probit)

$$ \Pr(y_i^{(o)}\le k)=\Phi\left(\frac{\tau_k-I_o(\mu_i)}{\sigma_o}\right),\quad \tau_1<\cdots<\tau_{K-1}. $$


Triangle discrimination

For pair (a, b):


$$        \Pr(\mathrm{correct})=\gamma+(1-\gamma)\,\Phi\big(\beta\,d(\mu_a,\mu_b)-\alpha\big),\quad
\gamma=1/3. $$




                                                       5
Similarity judgments

Use a bounded likelihood (recommended):


     • Beta regression: zab ∼ Beta(κm, κ(1 − m)), with m = exp(−λs d(μa , μb )2 ).


5.2 Mixture-consistency penalty (soft constraint)
For mixture-structured trials (i, j) ∈ M, impose:


$$ \log p(D\mid\cdot)\leftarrow \log p(D\mid\cdot) -\eta\sum_{(i,j)\in\mathcal M}\max{0,\mathrm{Div}
(\mu_{i\otimes j}|\mu_i\otimes\mu_j)-\epsilon}, $$


where Div is KL (simplex) or W2 (Gaussian) and the hinge avoids over-penalizing already-consistent fits.


5.3 Participant random effects
For participant u:


$$ \phi_u\sim\mathcal N(\bar\phi,\Sigma_\phi),\qquad \theta_u\sim\mathcal N(\bar\theta,\Sigma_\theta). $
$




6. Model Comparison and Prime Inference (Anti-
Gaming)
6.1 Clustered cross-validation
Primary generalization target is novel mixtures.


     • Ratings: leave-one-stimulus-out (clustered by stimulus)
     • Discrimination: leave-one-pair-out
     • Pointwise PSIS-LOO reported only as sensitivity analysis

For model families M1 , … , MJ :


     • Compute clustered ELPD (LOO/CV) and its SE.
     • Prefer Ma over Mb if ΔELPDab > 2 ⋅ SE(Δ).
     • Otherwise use stacking/model averaging.


6.3 Stacking weights (model averaging)
Compute stacking weights wj to maximize expected log score of the mixture predictive distribution.




                                                     6
6.4 Generator (prime) inference
QPF supports two complementary inference modes.


Mode A (Primary): Bayesian inclusion (spike-and-slab)

Introduce inclusion indicators γq ∈ {0, 1} with spike-and-slab priors, and infer


$$ P(q\in G\mid D,M_j)=\mathbb E[\gamma_q\mid D,M_j]. $$


Define stacking-weighted robust probability:


$$ P_{\mathrm{robust}}(q)=\sum_{j=1}^J w_j\,P(q\in G\mid D,M_j). $$


Mode B (Secondary check): MDL / nested CV compression

Perform nested CV once per model family (not per posterior draw):


$$ \mathrm{Score}(G)=\mathrm{NLL}_{\mathrm{outerCV}}(G)+\lambda_1|G|+\lambda_2|\theta|_0. $$


Use the Bayes-inclusion ranking to define a manageable candidate pool (e.g., top k qualities), then search
over subsets.


6.5 Structure-preserving permutation null
To test MDL-prime claims:


     • Permute labels within concentration strata.
     • Permute edge labels on the mixture-design graph.
     • Preserve adjacency/mixture structure.


6.6 Prime definitions
     • Bayes-prime: P (q ∈ G ∣ D) > 0.95 (within a family)
     • Robust-prime: Probust (q) > 0.90 (stacking-weighted)
     • MDL-prime: ΔScoreq exceeds the 95th percentile of the structure-preserving null




7. Algorithm 1 (Complete QPF Pipeline)
    1. Specify ⊗-families {LRS, DN, LB} with admissibility constraints.
    2. For each family Mj : fit the hierarchical model to D , including mixture-consistency penalty.
    3. Compute clustered CV/ELPD and SE for each Mj ; compute stacking weights wj .
    4. For each Mj : infer inclusion probabilities P (q ∈ G ∣ D, Mj ) (spike-and-slab).




                                                      7
   5. Compute Probust (q) = ∑j wj P (q ∈ G ∣ D, Mj ).
   6. Run structure-preserving permutations; compute MDL-prime checks via nested CV.
   7. Report: winning ⊗ family (or model-averaged results), robust primes, model-dependent primes, and
      all failure diagnostics.




8. Falsifiable Predictions
8.1 Basic tastes (within canonical physiology-constrained families)
    • {sweet, sour, salty, bitter} should have high Probust (> 0.9).
    • umami should require its own generator (often > 0.8).


8.2 Bittersweet emergence
    • “bittersweet” should be generator-worthy primarily under DN/LB and primarily when discrimination/
      similarity data are included.


8.3 Category boundary
    • Extending QPF to taste + trigeminal (astringent/metallic/pungent) should fail unless ⊗ is expanded
      to cross-modal interactions or the generator set includes cross-modal primitives.




9. Success / Failure Criteria
Supported if
   1. One ⊗ family dominates (stacking weight > 0.7) or stacking delivers stable predictions.
   2. Robust primes are consistent across participants (e.g., ICC > 0.7).
   3. Held-out discrimination performance is high (e.g., >75% or meaningfully above a baseline model).
   4. Compression ratio < 0.5 (generators fewer than half of qualities).


Falsified if
   1. Models are indistinguishable (stacking weights \~ uniform) and model averaging yields no stable
      prime structure.
   2. No quality achieves robust-prime status.
   3. Predictive performance on novel mixtures is worse than a simple baseline.
   4. No compression: required generators ≈ all qualities.




                                                   8
10. Conjectural Research Direction (Regularity)
Under Lipschitz continuity in stimulus space and Wasserstein-2 similarity:


    1. ∣λN (n + 1) − λN (n)∣ ≤ C/nα
    2. No knife-edges under small TV perturbations
    3. Compressibility: K(λN [1 : n]) = O( n log n)




11. Implementation Notes
     • Bayesian inference: Stan (NUTS/HMC), multiple chains, posterior predictive checks, and simulation-
       based calibration.
     • PSIS-LOO / stacked weights: use loo tooling, monitor Pareto k ^ diagnostics.
     • Prefer clustered CV for dependence-heavy designs.
     • Keep all priors explicit and motivated by biology (normalization, saturation, nonnegativity where
       appropriate).




12. External References (selected)
Computable analysis / TTE / semimeasures
     • Klaus Weihrauch. Computable Analysis: An Introduction. Springer (2000). ISBN 978-3-540-66817-6. doi:
       10.1007/978-3-642-56999-9.
     • Vasco Brattka, Guido Gherardi, Arno Pauly. Weihrauch Complexity in Computable Analysis (arXiv:
       1707.03202).
     • Ray Solomonoff. The Discovery of Algorithmic Probability (retrospective; discusses universal a priori
       probability).
     • Scholarpedia entry: Algorithmic probability (overview of Solomonoff induction and universal priors).


Model evaluation and averaging
     • Aki Vehtari, Andrew Gelman, Jonah Gabry. Practical Bayesian model evaluation using leave-one-out
       cross-validation and WAIC (arXiv:1507.04544).
     • Aki Vehtari et al. Pareto Smoothed Importance Sampling (JMLR 2024; PSIS foundations).
     • Yuling Yao, Aki Vehtari, Daniel Simpson, Andrew Gelman. Using stacking to average Bayesian predictive
       distributions (Bayesian Analysis 2018; arXiv:1704.02030).


MDL / sparsity priors
     • Jorma Rissanen. Modeling by shortest data description. Automatica (1978).




                                                      9
     • Andrew Barron, Jorma Rissanen, Bin Yu. The Minimum Description Length Principle in Coding and
       Modeling (IEEE IT 1998).
     • Edward I. George, Robert E. McCulloch. Variable Selection Via Gibbs Sampling. JASA (1993).
     • Carlos M. Carvalho, Nicholas G. Polson, James G. Scott. The horseshoe estimator for sparse signals.
       Biometrika (2010).


Neural computation and taste mixture interactions
     • Matteo Carandini, David J. Heeger. Normalization as a canonical neural computation. Nat Rev Neurosci
       (2012). doi:10.1038/nrn3136.
     • David J. Heeger. Normalization of cell responses in cat striate cortex. Visual Neuroscience (1992).
     • B. G. Green et al. Taste mixture interactions: suppression, additivity, and the predominance of sweetness
       (2010).
     • Bob Carpenter et al. Stan: A Probabilistic Programming Language. Journal of Statistical Software (2017).

Citizen Gardens © 2025 CC-NC-ND 4.0




                                                      10

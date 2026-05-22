---
slug: meta-ensembles
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 05-systems/meta-ensembles/Meta_Ensembles.md
  last_synced: '2026-03-20T17:17:16.180340Z'
---

                            Meta-Ensembles
              A Mathematical Scaffold with Certified Stability
                              Ryan O. van Gelder & Tyler van Osdol

                                           Citizen Gardens

                                          December 18, 2025


                                                Abstract
          We formalize meta-ensembles as discrete-time recursions that combine a finite family of
      operators via an adaptive gate and a convex aggregator. We give two regimes with rigorous
      guarantees: a contractive regime on Banach spaces and an averaged-operator regime on Hilbert
      spaces leveraging Krasnosel’skii–Mann iteration. The framework supports optional composition
      via embed–glue–retract while preserving stability. We include ready-to-run code snippets and a
      benchmark plan.


1    Setting and Notation
Let (X, ∥·∥) be a real Banach space, time t ∈ N, and an index set P = {p1 , . . . , pm } with m ≥ 1.
A state is xt ∈ X. An operator family is {Πp }p∈P with Πp : X → X. A weight vector is
α(t) = (αp (t))p∈P ∈ ∆m−1 := {a ∈ Rm+ :  p ap = 1}. Optional exogenous terms: drift Bt ∈ X and
                                        P

perturbation Nt ∈ X.


2    Assumptions and Update Rule
Assumption 1 (Lipschitz operators). Each Πp is Lipschitz with constant Lp and supp Lp ≤ λ < 1.

Assumption 2 (Convex aggregator). µ(α, z1 , . . . , zm ) =      p αp zp for (α, z) ∈ ∆
                                                                                         m−1 × X m .
                                                              P


Assumption 3 (Gate). α(t) = ∆k−1 (xt ) ∈ ∆m−1 ; ∆k−1 is measurable in xt .

Assumption 4 (Errors).        t ∥Bt ∥ < ∞ and supt E ∥Nt ∥ < ∞.
                            P


    Define the time-t map

             Ft (x) := µ ∆k−1 (x), {Πp (x)}p∈P + Bt + Nt =            αp (t) Πp (x) + Bt + Nt .        (1)
                                                               X

                                                                  p

The recursion is xt+1 = Ft (xt ).

Optional composition. Let ι : X ,→ Y and R : Y → X be bounded linear maps with
                                                                               (j)
R ◦ ι = IdX . Let G : Y q → Y be nonexpansive. For q ensembles, set y (j) = ι Ft (x) and
                                                                                    

xt+1 = R G(y (1) , . . . , y (q) ).


                                                    1
3    Basic Properties in the Contractive Regime
Lemma 1 (Mixture nonexpansiveness). Under ?? 1–3,                       p αp (t) Πp (x) −       p αp (t) Πp (y)   ≤
                                                                    P                       P

λ ∥x − y∥.
Proposition 1 (Contraction with bounded noise). Assume ?? 1?? 4. With εt := ∥Bt ∥ + E ∥Nt ∥
and any fixed point x∗ of x 7→ p αp (t)Πp (x),
                              P


                                E ∥xt+1 − x∗ ∥ ≤ λ E ∥xt − x∗ ∥ + εt ,

so if supt εt ≤ ε then lim supt→∞ E ∥xt − x∗ ∥ ≤ ε/(1 − λ).


4    Averaged-Operator Variant (Hilbert Setting)
We now work on a real Hilbert space (X, ⟨·, ·⟩).
Assumption 5 (Averaged operators). Each Πp is βp -averaged, i.e., Πp = (1 − βp )Id + βp Np with
Np nonexpansive and βp ∈ (0, 1] [1, Sec. 4.2].
Assumption 6 (Common fixed points). Let Tt (x) :=             p αp (t) Πp (x). Assume           t≥0 Fix(Tt ) ̸= ∅.
                                                          P                                 T

Lemma 2 (Averagedness preserved by convex mixing). If Assumption 5 holds then for any α ∈ ∆m−1 ,
Tα (x) := p αp Πp (x) is β-averaged with β = p αp βp [1, Prop. 4.32].
         P                                  P

Theorem 1 (Krasnosel’skii–Mann with errors). Assume ?? 3–6. Consider the relaxed update

                       xt+1 = (1 − γ) xt + γ Tt (xt ) + Bt + Nt ,         γ ∈ (0, 1).                             (2)

Suppose the family {Tt } is finite and each map appears infinitely often. Then (xt ) is Fejér monotone
with respect to t Fix(Tt ) and converges weakly to a point x⋆ in this set. If, in addition, one active
                T

operator is a contraction or the family is demiregular at x⋆ , convergence is strong. [1, Thm. 5.14,
Cor. 5.15]; see also [2, 3].
Corollary 1 (Firmly nonexpansive case). If all Πp are firmly nonexpansive (βp = 1/2), then under
the hypotheses of Theorem 1 the relaxed iteration (2) converges; strong convergence holds under any
of the standard strengthening conditions (e.g., viscosity/Halpern variants [1, Sec. 5.2]).

Remark on gating. Measurable, state-dependent α(t) ∈ ∆m−1 does not change nonexpansiveness
or averagedness; no Lipschitz inflation arises from the gate itself.


5    Operator Library with Certified Parameters
Examples with computable constants:
• Linear: x 7→ Ax + b, ∥A∥ ≤ λ < 1 (contraction).

• Gradient step: x 7→ x − η∇f (x), f is L-smooth, η ∈ (0, 2/L) ⇒ averaged with β = ηL/2 [1,
  Ex. 4.38].

• Proximal: x 7→ proxηg (x) is firmly nonexpansive [4].

• Contractive denoiser: x 7→ D(x) with Lip(D) < 1.

                                                   2
6    Gate Design
Let S : X → Rr be a micro-statistic and gθ : Rr × R+ → ∆m−1 a gate; set α(t) = gθ S(xt ), τk .
                                                                                                

Examples: softmax at fixed temperature; Top-K followed by projection onto the simplex. Theory
requires only measurability and range in ∆m−1 .


7    Algorithmic Template

            Listing 1: Core Meta-Ensemble Loop (NumPy/PyTorch-like pseudocode)
import numpy as np

# operators: list of callables Pi[p](x)
# gate: returns simplex weights alpha(x) in R^m
# B_t: optional drift sequence; set to zero for theory runs

def meta_ensemble(x0, operators, gate, T, B=None, gamma=1.0):
    x = x0.copy()
    m = len(operators)
    if B is None:
        B = [0 for _ in range(T)]
    for t in range(T):
        alpha = gate(x) # in Delta^{m-1}
        z = [op(x) for op in operators]
        Fx = sum(alpha[p] * z[p] for p in range(m)) + B[t]
        x = (1 - gamma) * x + gamma * Fx
    return x



8    Evaluation Protocol
One dataset per domain; metrics: AUROC or macro-F1. Baselines: bagging, XGBoost, stacking,
MoE with softmax gate. Ablations: uniform α; single operator; remove glue; softmax↔Top-K;
temperature sweep. Use 5 seeds and pre-register operators, metrics, and thresholds.


9    Limitations
Convergence speed depends on contraction/averaged constants and perturbations. Nonconvex glue
or nonlinear aggregators may break guarantees. Statistical superiority over baselines is empirical
and currently unproven.


Acknowledgments
We thank standard references on nonexpansive operators and monotone operator theory for the
results used here.




                                                3
References
[1] H. H. Bauschke and P. L. Combettes. Convex Analysis and Monotone Operator Theory in
    Hilbert Spaces. 2nd ed., Springer, 2017.

[2] W. R. Mann. Mean value methods in iteration. Proceedings of the American Mathematical
    Society, 4(3):506–510, 1953.

[3] P. L. Combettes and J.-C. Pesquet. Stochastic quasi-Fejér monotonicity and block-coordinate
    fixed point algorithms with random sweeping. SIAM Journal on Optimization, 25(2):1221–1248,
    2015.

[4] N. Parikh and S. Boyd. Proximal algorithms. Foundations and Trends in Optimization, 1(3):127–
    239, 2014.




                                               4

---
slug: ccn-v2-minimal-axioms-representation-theorem-finite-case
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Ccn V2 Minimal Axioms + Representation Theorem (finite Case).md
  last_synced: '2026-03-20T17:17:20.020718Z'
---

Conserved Continuity Numerosity (CCN v2)
CCN v2 separates three notions that are often conflated in identity ethics:


      • Continuity Mass (CM): conserved moral stake flowing forward from pre-existing persons under
        branching.
      • Centerhood (CH): the (non-conserved) number of welfare-bearing loci/centers that exist after
        branching.
      • Creation Mass (CR): additional moral stake contributed by new roots (population/creation ethics).

This document formalizes a minimal axiom basis for CCN’s CM representation in the finite branching case,
replacing replication invariance (old A3) with branch mixture linearity (A7), and deriving A3 as a corollary.




1) Formal setup (finite case)

Worlds, roots, continuers

A world w contains:


      • A finite set of pre-existing roots Rw .
      • For each root i ∈ Rw , a finite set of continuer histories Hi (think: worldlines downstream of i). Let
       Hw = ⨆i∈Rw Hi .
      • A finite set of created roots Cw (entities not downstream of any i ∈ Rw under the chosen continuity
       relation).

Each history/root x ∈ (Hw ∪ Cw ) has:


      • Lifetime welfare u(x) ∈ R (already integrated over time, so no time-slice double counting).

Continuity flow (CM bookkeeping)

For each root i, define a continuity flow sw (i, ⋅) over Hi :


      • Support: sw (i, h) = 0 if h ∈
                                    / Hi .
      • Conservation: ∑h∈Hi sw (i, h) = 1.

Interpretation: sw (i, ⋅) is a probability distribution / conserved moral stake distribution over continuers of i.


Moral status weights

      • ω : Rw ∪ Cw → (0, ∞) gives status weight.
      • W-invariance (axiomatized below) prevents “status gaming” via branching.




                                                          1
2) Minimal axiom basis (A3 replaced by A7)
Below, “CM-value for a single root i” is a function Vi defined on finite lotteries over outcomes (here:
outcomes are continuer histories with welfare u(h)):


$$ V_i:\; \Delta(H_i) \to \mathbb{R},\quad p \mapsto V_i(p) $$


where p ∈ Δ(Hi ) is a probability distribution over Hi (i.e., the flow sw (i, ⋅)).


       Note: By taking the domain to be distributions Δ(Hi ), branch label invariance is “built in,” so
       an explicit branch-symmetry axiom is no longer needed.


M1. Root separability (across independent roots)

World value decomposes additively across distinct pre-existing roots (plus creation):


$$ \mathcal{V}(w)= \sum_{i\in R_w} \mathcal{V}i(w)\; +\; \mathcal{V}(w). $$}


No cross-terms between unrelated roots.


M2. Branch mixture linearity (A7)

For any two branch distributions p, q ∈ Δ(Hi ) and any t ∈ [0, 1]:


$$ V_i\big(tp+(1-t)q\big) = tV_i(p) + (1-t)V_i(q). $$


Interpretation: moral stake is divisible and behaves like a linear “portfolio” over branches.


M3. Continuity monotonicity

If p first-order stochastically dominates q with respect to welfare u, then


$$ V_i(p) \ge V_i(q). $$


(For finite supports, it’s enough to require: shifting probability mass from lower-welfare branches to higher-
welfare branches weakly increases value.)


M4. W-invariance (status inheritance)

Continuation value for root i scales only with ω(i) and cannot depend on independently assigned
descendant status weights.

                                                ~
Formally: there exists a root-level function V such that


$$ \mathcal{V}_i(w) = \omega(i)\, \tilde V\big(s_w(i,\cdot), u(\cdot)\big). $$




                                                         2
M5. Regularity

Vi is continuous on the simplex Δ(Hi ) (standard for finite mixture spaces).

M6. Creation modularity (CR separation)

Created roots contribute via a separate additive term that does not depend on the continuation flows for
Rw :

$$ \mathcal{V}{\text{creation}}(w)= \sum \omega(c)\,G\big(u(c)\big) $$


for some increasing function G (often taken to be the same as F below, but not required).




3) Representation theorem (finite case)

Theorem (Branching-respecting CM representation)

Assume M2 (mixture linearity), M3 (monotonicity), and M5 (regularity). Then there exists a strictly increasing
function F : R → R such that for any distribution p ∈ Δ(Hi ):


$$ V_i(p)= \sum_{h\in H_i} p(h)\,F\big(u(h)\big). $$


With M1, M4, M6, world value admits the CCN v2 form:


$$ \mathcal{V}(w)= \sum_{i\in R_w} \omega(i)\sum_{h\in H_i} s_w(i,h)\,F\big(u(h)\big) \; +\; \sum_{c\in C_w}
\omega(c)\,G\big(u(c)\big). $$


Proof sketch (finite, tight)

     1. Define the point-mass (degenerate) distribution δh with all mass on history h. Let

$$ F(u(h)) := V_i(\delta_h). $$


     1. Any p ∈ Δ(Hi ) is a convex combination of point-masses: p = ∑h p(h)δh .
     2. Apply M2 repeatedly to get

$$ V_i(p)=\sum_h p(h)V_i(\delta_h)=\sum_h p(h)F(u(h)). $$


     1. M3 implies F is increasing; M5 rules out pathological (non-measurable) constructions.

       Uniqueness: F is unique up to positive affine transformation when only preference order
       matters (as in standard expected utility representations).




                                                       3
4) Derived theorem: replication / refinement invariance (old A3)

Corollary (Replication invariance derived)

Suppose a branch h with share p(h) and welfare u(h) is replaced by n identical replicas h1 , … , hn each
with share p(h)/n and same welfare. Then


$$ \sum_{k=1}^n \frac{p(h)}{n}F(u(h_k)) = p(h)F(u(h)), $$


so Vi (hence V ) is invariant under arbitrary replication/refinement.


Interpretation: “No fission bonus” follows because splitting a conserved measure doesn’t create more
measure.



CCN v2 treats personal-identity theory as a parameterized kernel family:


      • Kpsy : psychological continuity
      • Kbio : biological/brain continuity
      • Kcausal : right-kind causal provenance

Mixture kernel:


$$ K_\theta(i,h)=\alpha K_{\text{psy}}(i,h)+\beta       K_{\text{bio}}(i,h)+\gamma   K_{\text{causal}}(i,h),\quad
\alpha+\beta+\gamma=1. $$


Flow definition by normalization:


$$ s_w(i,h)=\frac{K_\theta(i,h)}{\sum_{h'\in H_i}K_\theta(i,h')}. $$




6) Experimental battery (minimal, diagnostic)

Share elicitation prompt (standard)

       “You have 100 units of moral obligation owed to the original. Allocate these 100 units among
       downstream individuals.”


      • V1 Destructive upload (psy vs bio)
      • V2 Total amnesia with brain continuity (bio vs psy)
      • V3 Memory forgery (causal vs mere similarity)
      • V4 Asymmetric fission (substructure inside psychological continuity)

V5–V7: replication + monotonicity checks

      • V5 Symmetric fission (2 continuers)




                                                         4
      • V6 Replicated fission (4 continuers, identical)
      • V7 Welfare-weighted fission (high vs low welfare continuer)

V8: creation boundary

      • V8 Non-destructive copying (copy as new root vs continuer-share split)

V9 (recommended add-on): mixture linearity (tests M2 directly)

      • V9a: Scenario A → allocate.
      • V9b: Scenario B → allocate.
      • V9c: A fair coin decides A vs B before branching → allocate.

Prediction under M2:


$$ \text{V9c allocation} \approx \tfrac{1}{2}(\text{V9a allocation}) + \tfrac{1}{2}(\text{V9b allocation}). $$




7) Implementation & analysis (code snippets)

7.1 Data model (Python)


  from dataclasses import dataclass
  from typing import Dict, List, Tuple

  @dataclass
  class World:
      roots: List[str]                              # R_w
      created: List[str]                            # C_w
      histories: Dict[str, List[str]]               # H_i keyed by root
       welfare: Dict[str, float]                    # u(x) for x in histories ∪ created


  # flow s_w(i,h) stored as: flows[root][history] = share
  Flows = Dict[str, Dict[str, float]]



7.2 Kernel mixture → normalized flow


  def normalize(weights: Dict[str, float]) -> Dict[str, float]:
      Z = sum(max(v, 0.0) for v in weights.values())
      if Z <= 0:
          # no continuers => treat as no survival; caller decides
          return {k: 0.0 for k in weights}
      return {k: max(v, 0.0) / Z for k, v in weights.items()}

  def flow_from_kernel(
      root: str,




                                                         5
      H_i: List[str],
      K_psy: Dict[Tuple[str, str], float],
      K_bio: Dict[Tuple[str, str], float],
      K_causal: Dict[Tuple[str, str], float],
      alpha: float,
     beta: float,
     gamma: float,
 ) -> Dict[str, float]:
     raw = {}
      for h in H_i:
          raw[h] = (
              alpha * K_psy.get((root, h), 0.0)
              + beta * K_bio.get((root, h), 0.0)
              + gamma * K_causal.get((root, h), 0.0)
          )
      return normalize(raw)


7.3 CCN world value (CM + CR)


 def CCN_value(world: World, flows: Flows, omega: Dict[str, float], F, G=None) ->
 float:
     if G is None:
         G = F

      total = 0.0

      # Continuity mass term
      for i in world.roots:
          for h in world.histories[i]:
              s = flows[i].get(h, 0.0)
              total += omega[i] * s * F(world.welfare[h])

      # Creation mass term
      for c in world.created:
          total += omega[c] * G(world.welfare[c])

      return total


7.4 Simple constrained fit for (α,β,γ) (grid search)


 import numpy as np

 def fit_alpha_beta_gamma(loss_fn, step=0.05):
     best = None
     for a in np.arange(0, 1+1e-9, step):




                                             6
             for b in np.arange(0, 1-a+1e-9, step):
                 g = 1.0 - a - b
                 loss = loss_fn(a, b, g)
                 if best is None or loss < best[0]:
                     best = (loss, a, b, g)
        return best      # (loss, alpha, beta, gamma)


7.5 Invariance / linearity scores


  def invariance_score(total_alloc_v5: float, total_alloc_v6: float) -> float:
      return abs(total_alloc_v5 - total_alloc_v6)

  def mixture_linearity_score(alloc_v9a, alloc_v9b, alloc_v9c) -> float:
      # allocs can be vectors over recipients; use L1 distance
      target = 0.5 * (np.array(alloc_v9a) + np.array(alloc_v9b))
        return float(np.sum(np.abs(np.array(alloc_v9c) - target)))




8) External references (decision/ethics analogues)
      • John von Neumann & Oskar Morgenstern, Theory of Games and Economic Behavior (Princeton
        University Press; first ed. 1944; later eds. 1947/1953).
      • Leonard J. Savage, The Foundations of Statistics (1954).
      • F. J. Anscombe & R. J. Aumann, “A Definition of Subjective Probability,” Annals of Mathematical Statistics
        34(1):199–205 (1963).
      • John C. Harsanyi, “Cardinal Welfare, Individualistic Ethics, and Interpersonal Comparisons of Utility,”
        Journal of Political Economy 63(4):309–321 (1955).
      • David Deutsch, “Quantum Theory of Probability and Decisions,” Proceedings of the Royal Society A
        455:3129–3137 (1999).
      • David Wallace, “A formal proof of the Born rule from decision-theoretic assumptions,” arXiv:
        0906.2718 (2009).
      • Derek Parfit, Reasons and Persons (1984).




9) Optional: consent admissibility layer (operator constraint)
Define an action a that induces a transformation i ↦ Hi and flow s. Impose an admissibility gate:


$$ \text{Allowed}(a) \Rightarrow \forall i\in R: \; \text{Consent}(i,a)\ge \tau. $$


This is orthogonal to the CM representation: it filters which worlds/transformations are ethically permitted.


Citizen Gardens © 2025 CC-NC-ND 4.0




                                                         7

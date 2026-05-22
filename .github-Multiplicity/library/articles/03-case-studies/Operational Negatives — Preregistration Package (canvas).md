---
slug: operational-negatives-preregistration-package-canvas
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "03-case-studies/Operational Negatives \u2014 Preregistration Package (canvas).md"
  last_synced: '2026-03-20T17:17:20.950995Z'
---

Operational Negatives — Preregistration Package
Subtitle: Licensed inverses, torsor specificity, and closure diagnostics for negative-number reasoning
Project stack: hybrid experimental design + GLMMs + Bayesian two-policy mixture
Artifacts:      generator.py    •       two_policy_mixture.stan   •      absence_frame_pilot.md               •
sample_trials_frame_A_seed2026.json




0) Executive summary
Thesis. Negatives are licensed inverses of an operational practice. Participants perform best when the frame
makes the inverse role computable (netting to a neutral). They perform worst when “minus” is framed as
absence/removal (partial, non‑invertible). When only differences are meaningful (torsor), absolute queries
suffer while difference queries remain strong. A closure diagnostic (parenthesization sensitivity) captures
whether a frame induces an order‑sensitive, non‑closed internal operation.


Design overview (hybrid). Between‑subjects for Frame (A Netting‑Debt, B Netting‑Displacement, C
Pure‑Symbol minimally licensed control, D Absence/Removal). Within‑subjects for Origin (shown/hidden,
i.e., torsor toggle), Parenthesization (associator), and an Inventory Completion mini‑block (no‑backorders
vs backorders). Trial budget \~40–45 per participant (\~18–22 min).




1) Theoretical commitments (clarified)
     • Licensing criterion. A frame licenses negatives iff the participant’s implemented operation is or is
       treated as group‑like; otherwise “−” degenerates to removal in a partial algebra.
     • Torsor vs group. In a torsor, inversion lives in the acting group; there is no distinguished origin,
       only differences. Hiding the origin should selectively impair absolute queries in netting frames while
       leaving difference queries intact.
     • Completion. When a practice demands netting across gains/losses (e.g., backorders), the monoid
       completes to an abelian group (deficits become stable states).
     • Closure diagnostic. If a frame induces order sensitivity ((x ⊕ y) ⊕ z  x =  ⊕ (y ⊕ z) in behavior), it
       reveals missing state/closure; netting frames should minimize this.

Frame C (Pure‑Symbol) — baseline status. C is the minimally licensed control: standard rules allow
inverses but the UI provides no netting affordance or neutral substrate. Prediction: C > D but C < A/B.




2) Hypotheses (final text)
     • H1a (Netting vs Symbol): (A,B) > C on accuracy; RT (A,B) < C.
     • H1b (Symbol vs Absence): C > D on accuracy; RT C < D.
     • H2 (Torsor specificity; preregistered three‑way interaction). Frame × Origin (shown/hidden) ×
       Query‑Type (absolute/difference).




                                                      1
     • In A/B, hiding the origin selectively impairs absolute queries while sparing difference queries.
     • In C/D, this selective impairment is absent or markedly reduced.
     • Key test: Contrast of selective impairment under OriginHidden for A/B vs C/D.
     • H3 (Completion). Allowing backorders reduces clamp‑to‑zero errors and improves generalization to
       novel signed items.
     • H4 (Parenthesization / associator). Simple ΔAssoc (absolute difference in error rate or mean
       response deviation between left vs right parenthesization) satisfies: D > C > (A,B). Distributional W1
       serves as a secondary, group‑level confirmation.




3) Design & materials
Between‑subjects: Frame ∈ {A,B,C,D}. Target N = 240 → \~60 per frame. Primary contrasts: (A∪B) vs C;
C vs D. Pairwise A vs B exploratory.


Within‑subjects (inside assigned frame):


     • Origin: shown vs hidden (torsor toggle), stratified across items.
     • Parenthesization: 4 matched operand triples → 8 trials (L/R) for the simple associator.
     • Inventory mini‑block: 12 trials (6 no‑backorders, 6 backorders).

Trial plan per participant:


     • Main block (28 trials): 8 signed sums; 10 sign‑structure (double negative, subtracting a negative,
       unary vs binary minus, etc.); 6 comparisons; 4 parenthesization pairs (8 trials included in the 28).
       Origin and Query‑Type are balanced.
     • Inventory block (12 trials): toggles backorders (completion). “Cannot perform” feedback only in
       no‑backorders.

Manipulation checks: End‑of‑block strategy check: two forced‑choice (behavioral descriptions) + one free
response (30s). Use as a moderator, not exclusion.


Absence/Removal (D) contamination guard: purely verbal/static pictorial prompts; hard floor at zero; no
symmetric arrows, no neutral line; correctness feedback only.




4) Variables & derived metrics
Primary outcomes: accuracy (0/1), RT (ms, log‑transformed).
Error taxonomy: sign flip, magnitude error, unary/binary confusion, clamp‑to‑zero.


Clamp‑to‑zero (operational):


     • Strict: correct answer < 0 and response == 0.
     • Lenient: correct answer < 0 and response ≥ 0.




                                                      2
Parenthesization effect (simple ΔAssoc ). For each participant × frame: absolute difference in mean
response deviation (or error rate) between left vs right parenthesization of the same triple. This simple
effect (and its Frame interaction) is the primary test; distributional W1 is secondary and computed at group
level via bootstrap.




5) Analysis plan
Frequentist (primary; fixed‑N).


      • Accuracy (GLMM): acc ~ frame * origin * query_type + item_type + (1 |
       participant) + (1 | item)
        Planned contrasts: H1a (A∪B) > C; H1b C > D; H2 three‑way interaction; H4 parenthesization main
        effect × frame.
      • RT (LMM on log‑RT): same fixed/random structure; report ex‑Gaussian sensitivity in appendix if
       needed.

Bayesian (secondary): two‑policy mixture.


      • Bernoulli mixture with two logistic channels (Netting vs Absence‑like), mixture weight π varying by
        Frame and Origin with participant random intercept.
      • Priors: N (0, 1) on fixed effects; HalfNormal(0,1) on random‑effect SD.
      • ROPE for negligible frame differences on logit: ±0.1 (OR ≈ [0.90, 1.11]).
      • Use WAIC/LOO for model comparison; simulated recovery included.

Stopping. Fixed‑N for all frequentist tests. Bayesian fits may be extended only for posterior precision
(reported separately).


Order & fatigue. Include origin order and inventory order as fixed effects; report interactions. Robustness:
drop first 4 trials per block and re‑fit.




6) Falsification map (explicit)
      • Licensing theory fails if A/B do not beat C and C does not beat D on accuracy/RT.
      • Torsor specificity fails if the OriginHidden effect is not selectively larger for absolute than
        difference queries in A/B (or if C/D show the same selective pattern).
      • Completion fails if backorders do not reduce clamp‑to‑zero errors and improve generalization.
      • Closure diagnostic fails if D ≯ C ≯ (A,B) on the simple parenthesization effect.




7) Implementation notes (critical)
      • Frame contrasts: Primary = (A∪B) vs C; C vs D. A vs B exploratory (power).
      • Uniform feedback: All main‑block trials accept any numeric answer; feedback is ✓/✗ only. “Cannot
       perform” is restricted to Inventory/no‑backorders.



                                                       3
     • Strategy check wording (behavioral):
     • “I canceled credits and debts to reach zero.” (Netting)
     • “I imagined physically removing things.” (Absence)
     • “I followed the math rules I learned in school.” (Pure‑Symbol)
     • “I only focused on how much things changed.” (Difference)




8) Artifacts & how to use them
     • Stimulus JSON Generator: generator.py
      Usage: python generator.py --frame A --seed 2026 --out trials_A_2026.json
      Outputs per‑participant JSON with balanced items, origin toggle, and inventory block. Includes
       copy_keys for frame‑specific UI text.


     • Bayesian mixture model scaffold: two_policy_mixture.stan
      Implements the Bernoulli logistic two‑channel mixture with frame/origin‑dependent mixture weights
      and participant random intercept. Provides log_lik for WAIC/LOO.


     • Absence frame pilot spec: absence_frame_pilot.md
      One‑page implementation with 12 pilot items, 2 comprehension checks, and strict contamination
      guardrails.


     • Sample trials (Frame A): sample_trials_frame_A_seed2026.json
      Demonstration of generator output.


Download links:


     • generator.py — sandbox:/mnt/data/generator.py
     • two_policy_mixture.stan — sandbox:/mnt/data/two_policy_mixture.stan
     • absence_frame_pilot.md — sandbox:/mnt/data/absence_frame_pilot.md
     • sample_trials_frame_A_seed2026.json — sandbox:/mnt/data/sample_trials_frame_A_seed2026.json




9) External references (selected)
     • Vlassis, J. (2004). Making sense of the minus sign or negativity. (On classic difficulties with “−”, roles, and
       instruction).
       https://www.sciencedirect.com/science/article/abs/pii/S0959475204000441
     • Fischer, M. H., & Shaki, S. (2014). Do negative numbers have a place on the mental number line?
       https://www.researchgate.net/publication/
       228967986_Do_negative_numbers_have_a_place_on_the_mental_number_line
     • McNeil, N. M., et al. Making Sense of Negative Numbers. GUPEA repository.
       https://gupea.ub.gu.se/handle/2077/24151
     • Murray, H. (1991). Children's Ideas of Negative Numbers. ERIC.
       https://files.eric.ed.gov/fulltext/ED342632.pdf




                                                         4
     • Sneed, G., & colleagues (2024). Tools, Tricks and Topics Teachers Use for Integer Arithmetic. EJ RSME.
       https://ejrsme.icrsme.com/article/view/23771/14961

Notes. These external sources establish (i) the systematic difficulty with negatives, (ii) number‑line and
spatial encodings, and (iii) the role of context/metaphor. Our contributions add the practice‑first licensing
criterion, torsor specificity, and a closure diagnostic (behavioral associator) that together make the
theory falsifiable.




10) Ethics & data management
     • Adult online participants (18+), informed consent, anonymized data.
     • Exclusion: ≥2 failed attention checks in any two blocks; trial‑level RT trimming (<300 ms or >10 s;
       3×IQR within‑block).
     • Share de‑identified data + code + materials post‑acceptance.




11) Timeline
     • Week 1: Pilot Absence frame; finalize item banks and copy.
     • Week 2: Launch main study (N=240).
     • Week 3: Primary analyses (GLMMs), then Bayesian mixture + robustness.




12) Appendices

A. Parenthesization items (templates)

     • L: (a + b) + c vs R: a + (b + c) over matched signed triples (balanced magnitudes / signs); 4 pairs
       per participant.

B. Negative‑number screener (3 items)

    1. Place −4 and −7 on a number line; which is larger?
    2. What does the minus sign mean in “−x”?
    3. Compute 5 − (−3).

C. Inventory completion examples

     • No‑backorders: start=5, ship=7 → cannot perform (strict), clamp metric stored as 0.
     • Backorders: start=5, ship=7 → −2 (valid state).



Prepared for preregistration and immediate build. This document consolidates the final design, analysis plan,
falsification commitments, artifacts, and references.




                                                         5
Citizen Gardens © 2025 CC-NC-ND 4.0




                                      6

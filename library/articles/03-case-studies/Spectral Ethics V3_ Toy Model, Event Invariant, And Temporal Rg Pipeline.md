---
slug: spectral-ethics-v3-toy-model-event-invariant-and-temporal-rg-pipeline
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Spectral Ethics V3_ Toy Model, Event Invariant, And Temporal
    Rg Pipeline.md
  last_synced: '2026-03-20T17:17:21.545454Z'
---

Spectral Ethics v3: Minimal Toy Model + Noise-
Robust Event Invariant + Temporal RG
This document consolidates the latest developments into a publishable, reproducible framework:


     1. Minimal n=2 dynamical system for cognitive/ethical phases with a Lyapunov (gradient-flow)
        backbone.
     2. Noise-robust quasi-topological event invariant based on gap hysteresis excursions with
        orientation.
     3. Temporal “poor man’s RG”: coarse-graining via smoothing, followed by chained, reference-free
        fitting of effective couplings.
     4. Uncertainty quantification via block bootstrap with interpretable β-sign probabilities.




1) Core n=2 model

1.1 State and ethical field

      • Cognitive state: an angle α(t) ∈ R with ψ(α) = (cos α, sin α)⊤ .
      • Ethical order parameter: e(t) ∈ R (double-well).

1.2 Potential and overdamped stochastic dynamics

Define the potential


                             U (α, e) = λ sin2 α + ηe cos(2α) + 14 (e2 − 1)2 .

Its gradients:

                       ∂α U = (λ − 2ηe) sin(2α),           ∂e U = η cos(2α) + e3 − e.

Overdamped (gradient-flow) SDE:

                         α̇ = −κα ∂α U + σα ξα (t),         ė = −κe ∂e U + σe ξe (t).

1.3 Deterministic Lyapunov theorem (noise-free)

For σα = σe = 0,

                             d
                                U (α(t), e(t)) = −κα (∂α U )2 − κe (∂e U )2 ≤ 0,
                             dt
with equality iff ∂α U = ∂e U = 0. Consequences: - Monotone descent of U . - No sustained oscillations/limit
cycles (2D gradient system). - Metastable phases correspond to basins near local minima of U .




                                                      1
2) Diagnostic Hamiltonian, gap, and alignment

2.1 Ethical Hamiltonian with avoided crossings

Use a real symmetric 2×2 Hamiltonian:


                        He (t) = (                     ) = λ2 I + (                 ),
                                     ηe(t)       ϵ                  d(t)       ϵ
                                       ϵ     λ − ηe(t)               ϵ        −d(t)

where

                                             d(t) = ηe(t) − λ2 .

Eigenvalues:

                                        μ± (t) = λ2 ±     d(t)2 + ϵ2 ,

Gap:

                                 g(t) = μ+ (t) − μ− (t) = 2        d(t)2 + ϵ2 .

Minimum gap is 2ϵ, attained when d(t) = 0.


2.2 Exact alignment observable A(t)

Let P− (t) be the instantaneous ground-state projector of He (t). Define


                                A(t) = ⟨ψ(α(t)), P− (t)ψ(α(t))⟩ ∈ [0, 1].

Closed form:


                           A(t) = 12 (1 −                                         ).
                                              ϵ sin(2α(t)) + d(t) cos(2α(t))
                                                          d(t)2 + ϵ2

Interpretation: - A(t) measures geometric alignment between cognitive state and the Hamiltonian’s
instantaneous ground direction. - Reorganizations (large changes in A) concentrate near small gap g(t).




3) Event invariant: hysteresis excursions of the gap

3.1 Why hysteresis

Naively counting dip points or local minima can chatter under noise. A Schmitt-trigger style hysteresis
provides robust event segmentation.




                                                      2
3.2 Hysteresis excursion definition

Choose thresholds gon < goff . An excursion event occurs when: - the trajectory enters {t : g(t) < gon }
(“turns on”), and - later exits when g(t) > goff (“turns off”).


3.3 Orientation and quasi-topological count

For an excursion with entry time tin and exit time tout , define orientation


                                        orient = sign(d(tout ) − d(tin )).

Skip if orientation = 0. The event invariant:


                                                Iso =     ∑          orient.
                                                        excursions


Also track: - excursion rate R = #excursions/T - density I = Iso/T - near-gap mass M = T1 ∫ 1[g(t) <
gon ] dt - optional tie-breaker I/R when R > 0

3.4 Adaptive thresholds (robust)

Two modes: - eps-based: gon = c ⋅ 2ϵ with c ∈ [1.3, 2.0] - quantile-based: gon = Qq (g) with q ∈
[0.05, 0.15]

Hysteresis width:


                                   Δ = 0.74 MAD(g),                   goff = gon + Δ,

with fallbacks if MAD≈0.




4) Temporal RG: coarse-graining + chained effective couplings

4.1 Coarse-graining operator

Define a family Sw (Gaussian smoothing) acting on e(t):


                                                    ew = Sw e.

Evaluate diagnostics on ew across a log-spaced set of scales wk .


4.2 Observables per scale

On each scale w , compute: - R(w): excursion rate of gw (t) = 2                (ηew − λ/2)2 + ϵ2 - M (w): fraction of
time gw (t) < gon (w) - I(w): Iso(w)/T - I(w)/R(w): optional directional tie-breaker




                                                            3
4.3 Reference-free chained fitting (poor man’s RG)

Infer effective couplings (ηeff (wk ), ϵeff (wk )) by matching the diagnostics at each scale, while enforcing
continuity across scales.


Loss at scale k :


Lk (η, ϵ) = (Rη,ϵ (wk ) − Rk )2 + (Mη,ϵ (wk ) − Mk )2 + λI (Iη,ϵ (wk ) − Ik )2 + λIR (IRη,ϵ (wk ) − IRk )2 + λsmooth,k ∥θ − θk−1

where θ = (η, ϵ). Key practical choices: - Sparse-event boost: if nexc (wk ) < 2, multiply λsmooth,k to
stabilize. - Weak anchor: tiny λanchor resolves degeneracy when events vanish. - Optional: freeze ϵ when
nexc = 0.

4.4 Empirical β-functions

With x = log(w + 1), define

                                                 dηeff                    dϵeff
                                      βη (x) =         ,       βϵ (x) =         .
                                                  dx                       dx
Compute using a low-degree polynomial fit in x with AIC-ish degree selection.


Expected qualitative flow (testable): - R(w) decreases with w (events collapse at coarse scales). - ϵeff (w)
tends to increase (effective gap protection). - ηeff (w) tends to decrease (drive dilution).




5) Uncertainty quantification: block bootstrap

5.1 Why block bootstrap

Excursions are autocorrelated. Resampling individual points breaks temporal structure; block bootstrap
preserves local dependence.


5.2 Auto block length

Estimate a correlation time from e(t) autocorrelation: choose block length as the first lag where autocorr
drops below e−1 (or a similar threshold).


5.3 Bootstrap outputs

Across bootstrap replicates, compute: - mean/std/quantiles for ηeff (wk ), ϵeff (wk ) - mean/std/quantiles for β
- sign probabilities: P(βϵ > 0), P(βη < 0)


These yield interpretable confidence statements (e.g., “P(βϵ > 0) > 0.95 for intermediate scales”).




                                                           4
6) Recommended figures (paper core)

Figure A: single trajectory mechanism

Panels vs time: 1) e(t), d(t) = ηe − λ/2 2) g(t) with excursion bands marked (below gon / above goff ) 3)
A(t) showing sharp reorganizations aligned with excursions

Figure B: RG flow

Panels vs log w : 1) R(w) (event rate) decays 2) ϵeff (w) and ηeff (w) with confidence bands Inset: flow in
(η, ϵ) plane (arrows by scale)

Figure C: β-sign confidence

Bar plots per scale: - P(βϵ > 0) - P(βη < 0)




Code Appendix: consolidated NumPy-only
rg_run_v3
       Paste the full rg_run_v3 implementation from the assistant message into your codebase.
       It includes: - smoothing, thresholds, hysteresis events - chained multistart fitting with sparse
       boost + anchor - AIC poly smoothing for β - optional block bootstrap with auto block length




7) Practical defaults

Simulation-friendly defaults

     • threshold_mode="eps" , c_on=1.5 , eps_for_thresholds = ε
     • w_steps_list=(0,2,5,10,20,40) (in sample steps)
     • lam0_smooth=2.0 , sparse_boost=5.0 , lam_anchor=0.05
     • n_boot=50

Real-data-friendly defaults

     • threshold_mode="quantile" , q_on≈0.10 , with quantile clipping
     • Use a data proxy for d(t) if η is not meaningful; treat ϵ as the only gap-floor parameter




8) Key claims (tight, defensible)
    1. Deterministic backbone: The noise-free overdamped system is a gradient flow of U with Lyapunov
       monotonicity.



                                                      5
    2. Noise-robust event statistic: Hysteresis excursions define stable, interpretable events; Iso is an
       oriented, quasi-topological count.
    3. Temporal RG: Coarse-graining suppresses events and induces a flow in effective couplings,
       measurable via β .
    4. Statistical defensibility: Block bootstrap yields uncertainty bands and β-sign probabilities for
       falsifiable claims.




9) Next extension (post n=2 paper)
Move to n = 3 with a 2D ethical field (e1 , e2 ) so topology becomes literal (winding around degeneracy
points), while retaining the same event/flow machinery.




                                                      6

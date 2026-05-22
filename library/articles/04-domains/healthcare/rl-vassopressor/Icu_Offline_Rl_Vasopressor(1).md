---
slug: icu-offline-rl-vasopressor-1
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 04-domains/healthcare/rl-vassopressor/Icu_Offline_Rl_Vasopressor(1).md
  last_synced: '2026-03-20T17:17:18.754777Z'
---

        Offline Clinical Policy Optimization for ICU Vasopressor
                                          Ryan O. Van Gelder

                                             Citizen Gardens

                                            October 23, 2025


                                                 Abstract
          We specify a pre-registered offline reinforcement learning (RL) protocol to learn and evaluate
      vasopressor dosing policies from observational ICU data. The design defines the MDP, reward,
      safety constraints, and off-policy evaluation (OPE) using self-normalized importance sampling,
      doubly robust estimation, and fitted Q evaluation [6, 10, 13]. Learning uses Conservative Q-
      Learning to control extrapolation [9]. We provide acceptance gates, a readiness checklist, and a
      data dictionary skeleton suitable for replication on public cohorts (eICU, MIMIC-IV) [7, 11].


1    Problem Setup
Goal. Learn a policy πθ (a | s) that maximizes expected clinical utility for vasopressor dosing using
only logged data.
   Data. Patient trajectories τ = (s0 , a0 , r0 , . . . , sT ) aligned to an hourly grid across 72 hours.
   Endpoint. Primary: vasopressor-free hours (VFH) in [0, 72]. Per-hour reward

                           rt = ⊮[no vasopressor] − λ ⊮[MAP < 65 mmHg].                                    (1)

Secondary: in-ICU mortality, AKI progression, norepinephrine-equivalent exposure, and hypotension
burden (time-under-threshold).
    Assumptions. Consistency, sequential strong ignorability given st , and positivity on the support
of πθ .


2    State, Action, Reward
State st : demographics, comorbidities, vitals, labs, urine output, ventilation status, fluid balance,
current dose, time since ICU admit, and missingness flags. Standardize continuous features on the
training split.
    Action at : discretized norepinephrine-equivalent dose: A = {0, ∆, . . . , (K−1)∆} in µg kg−1 min−1 .
Optional binary co-action: fluid bolus in past hour.
    Terminal condition: ICU discharge or death.


3    Learning
Sequence encoder zt = fψ (s0:t ) (causal RNN/transformer). Action-value Qϕ (z, a).



                                                      1
Conservative Q-Learning (CQL). Minimize
                                   h                                                    i
                                                                              ′     ′ 2
             L(ϕ, ψ) = E(s,a,s′ )∼D (Qϕ (fψ (s), a) − r̂ − γ max    Qϕ (fψ (s   ), a ))                    (2)
                                                               a′
                                     X                                                   
                       + α Es∼D [log       eQϕ (fψ (s),a) ] − E(s,a)∼D [Qϕ (fψ (s), a)] ,                  (3)
                                              a∈A

with α > 0 [9]. Extract soft policy πθ (a | s) ∝ exp{Qϕ (fψ (s), a)/τ }.

Behavior policy model. Train β̂(a | s) via calibrated multinomial logistic regression or gradient
boosting. Assess calibration with reliability diagrams, ECE, and Brier score [2, 5].


4    Safety Constraints
1. KL trust region: KL(πθ (· | s) ∥ β̂(· | s)) ≤ ε on validation.

2. Action-ratio cap: Reject actions where πθ (a | s)/β̂(a | s) > cmax .

3. Dose monotonicity: If MAP ≥ 65 for ≥2 consecutive hours and lactate slope ≤ 0 over 4 hours,
   enforce non-increasing dose; otherwise allow step changes of at most one bin per hour.


5    Off-Policy Evaluation
                                 Qt     πθ (ak |sk )
Define cumulative ratios wt =       k=0 β̂(ak |sk ) .

SNIPS       P P
             i Pt wi,t ri,t
   V̂SNIPS = P              [13].
              i   t wi,t

DR V̂DR = N1 i t γ t wi,t [ri,t − Q̂(si,t , ai,t )] + V̂ (si,t ) with V̂ (s) = a πθ (a | s)Q̂(s, a) [6].
            P P                                                              P

FQE
      Regress Q̂π on Bellman targets under πθ and estimate V̂ = N1
                                                                           P
                                                                              i V̂ (si,0 ) [10].

Report point estimates with 1000-sample patient-level bootstrap CIs [3].


6    Experimental Design
Cohort. Adults (≥18) with shock receiving any vasopressor. Exclude ICU stays < 6h, or > 30%
missing MAP or dose in the first 24h.
    Time grid. 1-hour steps to 72h. Carry-forward for intermittent labs with missingness indicators.
    Splits. Patient-level 60/20/20 train/val/test. Fit preprocessing on train only. Hyperparameters
selected by validation FQE with safety constraints enforced.
    Baselines. Supervised outcome models; behavior cloning; offline RL baselines BCQ and IQL
[4, 8].
    Robustness. Sensitivity to action binning (K, ∆), α, τ , and reward weight λ. Negative control
outcomes and Rosenbaum sensitivity bounds [12].




                                                        2
 7    Readiness Checklist
 Mark each item when satisfied.

 1. Data use approved. De-identified dataset available. Extraction reproducible (commit hash
    recorded). □
 2. Data dictionary completed (Section 9). Units and value ranges verified. □
 3. Dose mapping to norepinephrine-equivalent validated by pharmacist. □
 4. Temporal alignment fixed: time zero definition, resampling, carry-forward rules. □
 5. Behavior model β̂ calibrated: reliability plots, ECE < ϵ, Brier score reported [2, 5]. □
 6. Overlap audited: state-action support maps, max wt and coefficient of variation thresholds defined.
    □
 7. Safety thresholds pre-specified: (ε, cmax ) and monotonicity triggers. □
 8. OPE power analysis: variance of DR/FQE, effective sample size, minimal detectable ∆V . □
 9. Pre-registration filed: endpoints, exclusions, reward λ grid, hyperparameters, seeds. □
10. Governance in place: DSMB charter, incident reporting, kill switch. □


 8    Acceptance Gates
 Accept πθ for prospective silent-mode if all hold on the held-out test set:

 1. Value lift: LCI95 (V̂DR (πθ ) − V̂DR (β)) ≥ δ.

 2. Weight health: maxi maxt wi,t ≤ cmax , median(wi,t ) ≤ m, and ESS ≥ E for ≥ p% of trajecto-
    ries.

 3. Safety non-inferiority: No degradation versus β in mortality, AKI, and hypotension burden
    after multiplicity control.

 4. Overlap: Fraction of state-action pairs outside support ≤ q%; those regions masked at inference.

 5. Calibration: β̂ passes ECE and Brier thresholds; reliability diagram shows no extreme miscali-
    bration.

 6. Guardrail adherence: KL and ratio caps never violated in validation replays.


 9    Data Dictionary Skeleton
 Populate per-variable entries before training. Example schema:

  Name                   Type          Unit          Sampling Preprocessing                    Range
  Patient ID             categorical   –             episode    hashed, one-hot                unique
  Age                    numeric       years         baseline   z-score                        [18,120]
  Sex                    categorical   –             baseline   one-hot                        M/F/other



                                                     3
 Name                 Type          Unit        Sampling Preprocessing                        Range
 MAP                  numeric       mmHg        hourly       carry-forward 2h max; win-       [30,140]
                                                             sorize 0.5%
 Heart rate           numeric       bpm          hourly      carry-forward 2h; z-score        [30,220]
 Lactate              numeric       mmol/L       lab times   forward-fill 6h; missing flag    [0.5,20]
 Creatinine           numeric       mg/dL        lab times   forward-fill 24h; missing flag   [0.3,12]
 Urine output         numeric       mL           hourly      none; rolling 6h sum             [0,1000]
 Ventilation status   categorical   –            hourly      binary encode                    0/1
 Fluid bolus          categorical   mL           hourly      binary in past hour              0/1
 Vaso dose (NE-eq)    numeric       µg kg−1 min−1hourly      map from drug-specific           {0, ∆, . . .}
                                                             doses; discretize by ∆
 Time since admit     numeric       h           hourly       none                             [0,72]
 Missingness flags    categorical   –           hourly       one-hot per variable             0/1

   Dose mapping note. Provide a table converting epinephrine, vasopressin, dopamine, etc., to
norepinephrine equivalents, reviewed by a pharmacist.


10     Implementation Notes
Adam optimizer, dropout, gradient clipping, early stopping on validation FQE. Strict temporal
splits and leakage controls. PID-style heuristic baseline for comparison [1].


11     Deployment Path
(1) Silent mode with logging of disagreements. (2) Guardrailed suggestions only when agreement
with β̂ or high confidence. (3) Randomized A/B with clinician override.


12     Limitations
Observational confounding risk; discrete actions may limit titration fidelity; OPE variance under
weak overlap; reward shaping encodes preferences. Mitigate via sensitivity, overlap audits, and
reward sweeps.


References
 [1] Karl J. Åström and Richard M. Murray. Feedback Systems: An Introduction for Scientists and
     Engineers. Princeton University Press, 2008.

 [2] Glenn W Brier. Verification of forecasts expressed in terms of probability. Monthly Weather
     Review, 1950.

 [3] Bradley Efron and Robert Tibshirani. An Introduction to the Bootstrap. Chapman and
     Hall/CRC, 1994.

 [4] Scott Fujimoto, David Meger, and Doina Precup. Off-policy deep reinforcement learning without
     exploration for multi-step tasks. In Advances in Neural Information Processing Systems, 2019.
     Batch-Constrained deep Q-learning.

                                                4
 [5] Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q. Weinberger. On calibration of modern neural
     networks. In International Conference on Machine Learning, 2017.

 [6] Nan Jiang and Lihong Li. Doubly robust off-policy value evaluation for reinforcement learning.
     In International Conference on Machine Learning, 2016.

 [7] Alistair E. W. Johnson et al. MIMIC-IV (version 2.2). PhysioNet, 2023.

 [8] Ilya Kostrikov, Ashvin Nair, and Sergey Levine. Offline reinforcement learning with implicit
     Q-learning. In International Conference on Learning Representations, 2022.

 [9] Aviral Kumar, Aurick Zhou, George Tucker, and Sergey Levine. Conservative Q-learning for
     offline reinforcement learning. Advances in Neural Information Processing Systems, 2020.

[10] Hoang Minh Le, Cameron Voloshin, and Yisong Yue. Batch policy learning under constraints.
     In Advances in Neural Information Processing Systems, 2019.

[11] Tom J Pollard, Alistair E W Johnson, Jesse Raffa, et al. The eICU collaborative research
     database, a freely available multi-center database for critical care research. Scientific Data,
     2018.

[12] Paul R. Rosenbaum. Observational Studies. Springer, 2002.

[13] Adith Swaminathan and Thorsten Joachims. Counterfactual risk minimization: Learning from
     logged bandit feedback. In Proceedings of the 22nd ACM SIGKDD International Conference
     on Knowledge Discovery and Data Mining, 2015.




                                                 5

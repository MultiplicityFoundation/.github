---
slug: certified-multiplicity-governance-cmg-formal-spec-minimal-implementation-plan
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "03-case-studies/Certified Multiplicity Governance (cmg) \u2014 Formal Spec\
    \ + Minimal Implementation Plan.md"
  last_synced: '2026-03-20T17:17:21.688723Z'
---

Certified Multiplicity Governance (CMG)
A formal specification for a reciprocity-centered civic system with a single stability spine (certified contraction),
auditable observables, rights-first governance gates, and uncertainty-aware tensor auditing.




0. Scope and goals
CMG is a layered system:


     1. Observation layer: logs interactions as typed events, aggregates them into intensities, reciprocity,
        and participation.
     2. Inference layer: estimates a latent relational state and a forward-looking rights-risk probability qt
        using a robust state-space model (with a dedicated jump channel).
     3. Stability layer: chooses a scalar gain Λm (t) by certified contraction (global and local certificates),
        optionally anchored to slow drift.
     4. Governance layer: admits proposals only when rights constraints hold, resonance persists above
        a calibrated threshold, and predicted rights-risk remains below a ceiling.
     5. Auditing layer: maintains a low-rank, uncertainty-aware impact tensor and produces explanations
        only at rights boundaries or regime changes.

Primary objective: make governance computable without making it unfalsifiable—all steering must be
subordinate to identifiable inference and certified stability.




1. Definitions

1.1 Sets and indices

       • Agents: V = {1, … , n}
       • Time windows: discrete index t ∈ Z with window length Δ
       • Interaction types: k ∈ K (e.g., care, labor, knowledge, repair)
       • Proposals: p ∈ P
       • Stakeholder groups: g ∈ G
       • Moral dimensions: d ∈ D (e.g., dignity, autonomy, fairness, privacy, safety)

1.2 Event log

An event is


$$ e = (i\to j,\; \tau,\; k,\; a,\; \text{ctx}) $$




                                                         1
where:


       • i, j ∈ V : source/target
       • τ : timestamp
       • k ∈ K: type
       • a ≥ 0: magnitude
       • ctx: optional context metadata (channel, task id, etc.)

1.3 Aggregated interaction intensities

For a time window [t − Δ, t]:


$$ x_{ij}^k(t) = \sum_{e:\; i\to j,\;k,\;\tau\in[t-\Delta,t]} a_e $$


Typed weights αk > 0 yield total intensity


$$ x_{ij}(t) = \sum_{k\in\mathcal{K}} \alpha_k\,x_{ij}^k(t). $$


1.4 Reciprocity, participation, and multiplicity

Pairwise reciprocal coupling:


$$ r_{ij}(t) = \min{x_{ij}(t),\,x_{ji}(t)}. $$


Total reciprocity:


$$ C(t)=\sum_{1\le i<j\le n} r_{ij}(t). $$


Total participation:


$$ P(t)=\sum_{i\ne j} x_{ij}(t). $$


Multiplicity observable (dimensionless):


$$ \mathcal{M}(t)=\frac{C(t)}{\Lambda_m(t)\,P(t)^{\beta}},\qquad \beta\in[0,1]. $$


Interpretation:


       • C(t) measures matched reciprocity.
       • P (t) controls for raw activity/logging volume.
       • Λm (t) is a certified gain ensuring the latent dynamics remain contractive.




                                                             2
1.5 Latent state and observations

Latent relational state:


      • St ∈ Rd summarizes relational dynamics (trust/strain/cohesion proxies).

Observation vector:


      • Ot aggregates measurable signals (incidents, moderation actions, surveys, churn, message rates,
         etc.).




2.1 State equation (discrete-time)

$$ S_{t+1} = F(S_t, U_t) + J_t + \omega_t $$


where:


      • Ut : optional exogenous inputs (platform changes, policy updates, holidays)
      • ωt : routine process noise
      • Jt : jump channel reserved for rights-critical shocks (sparse, heavy magnitude)

2.2 Observation equation

$$ O_t = G(S_t) + \epsilon_t $$


with robust noise


$$ \epsilon_t \sim t_{\nu}(0,R). $$


2.3 Rights-risk probability

Define a rights-risk event label Et:t+Δ ∈ {0, 1} (conservative operationalization, see §6). The filter produces


$$ q_t := \Pr(E_{t:t+\Delta}=1\mid O_{\le t}). $$


2.4 Identifiability / observability guard

CMG forbids treating St as meaningful unless the observation map has sufficient information:


      • Compute an empirical observability / Fisher-information proxy over a rolling window.
      • If the proxy rank falls below a threshold, reduce state dimension or enrich observations.

This is a required precondition for any governance steering.




                                                       3
3.1 Local linearization / Jacobian proxy

                                           ^t :
Define a local linear approximation around S


$$ S_{t+1} \approx A_t S_t + b_t. $$


At may be derived from:

      • Jacobian of a learned F
      • local regression / linearization fit
      • or a stable parametrization (e.g., diagonal + low-rank)

3.2 Contraction margin

Choose a contraction margin ϵ ∈ (0, 1). The goal is to enforce a certified contraction factor 1 − ϵ.


3.3 Two certificates

Global certificate (operator norm):


$$ \Lambda_{\text{glob}}(t)=\frac{1-\epsilon}{|A_t|_2}. $$


Local certificate (metric contraction):


Choose a PSD metric Qt ≻ 0 (e.g., from filter covariance or a Lyapunov candidate). Define


$$ \Lambda_{\text{loc}}(t)=\frac{1-\epsilon}{\sqrt{\lambda_{\max}(Q_t^{1/2}A_t^\top Q_t A_t Q_t^{-1/2})}}. $
$


Equivalent inequality form:


$$ A_t^\top Q_t A_t \preceq (1-\epsilon)^2 Q_t. $$


3.4 Hybrid certified gain policy

$$ \Lambda_m(t)=\min{\Lambda_{\text{glob}}(t),\,\Lambda_{\text{loc}}(t),\,\Lambda_{\max}}. $$


Interpretation: the safer bound always wins.


3.5 Optional slow-drift prior (anchored, never destabilizing)
                        ~
Propose a drifting gain Λm (t) via AR(1) on the log scale:


$$ \log\tilde\Lambda_m(t)=\mu+\phi(\log\tilde\Lambda_m(t-1)-\mu)+\nu_t. $$


Then certify by clipping:




                                                       4
$$           \Lambda_m(t)=\min{\tilde\Lambda_m(t),\,\Lambda_{\text{glob}}(t),\,\Lambda_{\text{loc}}(t),\,
\Lambda_{\max}}. $$




4. Governance layer: resonance + rights-first gates

4.1 Resonance score

For proposal p, define


$$ \mathcal{R}_p(t)=A_p(t)\cdot I_p(t), $$


where:


      • Ap (t) ∈ [0, 1]: alignment (stance variance, agreement, or structured consent)
      • Ip (t) ∈ [0, 1]: insight/quality (feasibility, reversibility, equity checks)

4.2 Persistence window

Let ω denote a stability window. Persistence requirement:


$$ \min_{u\in[t-\omega,t]} \mathcal{R}_p(u) \ge \theta_t. $$


4.3 Rights predicate (hard constraint)

A proposal must satisfy


$$ \text{Rights}(p)=\text{true}. $$


Rights is an explicit checklist / predicate over constraints (privacy bounds, non-coercion, due process,
minimum guarantees, etc.). It is not optimized as a soft penalty.


4.4 Risk ceiling

Only admit proposals when predicted rights-risk is sufficiently low:


$$ q_t \le q_{\max}. $$


4.5 Admission rule

A proposal p passes at time t iff:


     1. Rights(p) = true, and
     2. minu∈[t−ω,t] Rp (u) ≥ θt , and
     3. qt ≤ qmax .




                                                            5
Update θt to maintain a target false-negative bound on rights-risk (calibration target), rather than relying
only on "stable/unstable" history.


Operationally:


     • Maintain a passing-decision set Dt .
     • Require empirical Pr(E = 1 ∣ pass) to stay below a configured ceiling.




5. Tensorial auditing layer

5.1 Group-level ethical impact tensor

Define impacts


$$ Y_{g,a,d,t} \sim \mathcal{N}(\widehat Y_{g,a,d,t},\tau_{g,a,d,t}^2) $$


where:


     • g ∈ G : stakeholder group
     • a ∈ A: institutional action type
     • d ∈ D : moral dimension

5.2 Low-rank factorization (rank-capped)

Use CP/Tucker with a capped rank K and sparsity support. The purpose is forecasting + uncertainty—not
metaphysical truth.


5.3 Explanation budget

Generate explanations/attributions only when:


     • a rights boundary is approached/violated, or
     • a regime-change alert fires (latent factor shift, residual spike).




6. Invariants and required properties
These are the invariants CMG must preserve.




                                                        6
6.1 Certified contraction invariant

At every time t, the chosen Λm (t) must satisfy the certificate inequalities (global and/or local). If neither can
be satisfied (e.g., Λm (t) falls below a minimum), CMG must:


      • declare the model unstable/untrustworthy,
      • halt steering (freeze governance automation), and
      • require human review / model retraining.

6.2 Rights-first invariant

No optimization or threshold update may override Rights(⋅). If Rights fails, the proposal cannot pass.


6.3 Identifiability invariant

If observability checks fail, CMG must reduce model complexity or enrich observations before using qt for
governance.


6.4 Calibration invariant

The risk predictor qt must pass calibration thresholds (e.g., Brier score, reliability curve) prior to enabling
any automated steering (θt adaptation).


6.5 Auditability invariant

Every decision must be reproducible from:


      • immutable event logs (or cryptographic hashes),
      • model version IDs, and
      • the stored Λm certificates and governance gates applied.




7. Test suite (must-run)

7.1 Unit tests (logic correctness)

     1. Event aggregation: intensities xkij match manual counts.
     2. Reciprocity correctness: rij = min(xij , xji ).
     3. Multiplicity computation: M(t) handles edge cases (P (t) = 0, missing types).
     4. Rights predicate: returns deterministic pass/fail with explicit reasons.

7.2 Certificate tests (stability spine)

     1. Global certificate: verify ∥Λm At ∥2 ≤ 1 − ϵ.
     2. Local certificate: verify A⊤                2
                                   t Qt At ⪯ (1 − ϵ) Qt .
     3. Hybrid policy: Λm = min(⋅) always satisfies the stricter bound.




                                                          7
    4. Non-normal stress: generate non-normal A where spectral radius differs from norm; confirm local
       vs global behavior is meaningful.

7.3 Inference tests (statistical correctness)

    1. Filter sanity: predictive residuals show no systematic drift under stable periods.
    2. Jump channel detection: injected shock events increase jump probability; routine noise does not.
    3. Identifiability: rank proxy flags underdetermined states.

7.4 Calibration and prediction tests

    1. Calibration: reliability curve within tolerance; Brier score below a defined baseline.
    2. Predictive lift: qt beats baselines (activity-only, sentiment-only) on AUC/log-loss.
    3. Lead time: median lead time to rights-risk events exceeds baseline by a defined margin.

7.5 Governance tests

    1. Admission rule: proposals fail if any gate fails; gates are logged with reasons.
    2. Persistence: resonance must stay above θt for full ω .
    3. No-override: rights failures cannot be "fixed" by improving resonance.

7.6 Gaming resistance tests

    1. Reciprocity spam: simulated low-magnitude ping-pong does not produce outsized M(t) (requires
       diminishing returns / anti-collusion rule if needed).
    2. Logging policy drift: changes in reporting rate are detected (participation normalization; bias latent
       if implemented).




8. Minimal implementation plan
This plan prioritizes identifiable, deployable modules first, postponing high-variance choices.


8.1 Data schema (minimal viable)

Table: events


     • event_id (uuid)
     • ts (timestamp)
     • actor_id (string)
     • target_id (string or null)
     • interaction_type (enum)
     • magnitude (float, default 1.0)
     • context (json: channel/task/thread)

Table: windows (precomputed aggregates per window)


     • window_end_ts




                                                      8
     • x_ij_type_sparse (optional: stored as edge list table)
     • x_ij_sparse
     • r_ij_sparse
     • C_total
     • P_total
     • n_active_agents

Table: observations (per window)


     • window_end_ts
     • incident_count (int)
     • mod_actions (int)
     • churn_count (int)
     • complaint_count (int)
     • survey_trust_mean (float, optional)
     • other platform signals

Table: proposals


     • proposal_id
     • created_ts
     • active_until_ts
     • alignment_series (time-indexed)
     • insight_series (time-indexed)
     • rights_checklist_result (json + boolean)
     • decision_ts
     • outcome (passed/failed)

Table: model_registry


     • model_version
     • parameters (json)
     • training_window
     • feature_schema_hash

Table: certificates


     • window_end_ts
     • model_version
     • A_t (reference/summary)
     • Q_t (reference/summary)
     • Lambda_glob
     • Lambda_loc
     • Lambda_m
     • epsilon
     • pass/fail flags




                                                       9
Table: risk_predictions


     • window_end_ts
     • model_version
     • q_t
     • calibration_bin (optional)

8.2 Easiest model choices to fit first

Stage 1: Baseline risk model (fast, interpretable)


     • Logistic regression / Poisson regression predicting rights-risk events using:
     • incident_count, mod_actions, churn_count, complaint_count
     • C_total, P_total, C/P β (no Λm yet)
     • Purpose: establish baselines, labels, and evaluation pipelines.

Stage 2: Linear Gaussian state-space (Kalman) with robustification


     • Start with linear dynamics:
     • St+1 = ASt + But + ωt
     • Ot = HSt + ϵt
     • Use robust innovations (Huber) before moving to Student-t.
     • Estimate A, H via EM.
     • Derive At ≡ A initially (time-invariant) for certificates.

Stage 3: Jump channel (rights-critical shocks)


     • Add a two-regime mixture:
     • normal regime + shock regime
     • Simple implementation: latent indicator zt ∈ {0, 1} with elevated process noise when zt = 1.

Stage 4: Certified **Λm (t)** gating


     • Implement global certificate first (cheap): ∥A∥2 .
     • Then add local certificate with Q from covariance or a fixed Lyapunov metric.
     • Turn on hybrid min policy.

Stage 5: Governance gating (shadow mode)


     • Compute Rp (t), θt fixed.
     • Use rights predicate as strict gate.
     • Run in shadow mode; log hypothetical pass/fail.

**Stage 6: Calibration-driven **θt


     • Enable threshold adaptation only after calibration checks pass for N consecutive windows.
     • Maintain a false-negative target for rights-risk.




                                                       10
Stage 7: Tensor auditing (optional, later)


     • Implement group-level low-rank factorization only after stable inference + governance gating are
       validated.
     • Start with CP rank K ≤ 5 and sparse data handling.

8.3 Minimal label definitions (for validation)

Rights-risk event (conservative): define Et:t+Δ = 1 if any of:


     • spike in targeted harassment reports
     • emergency moderator interventions
     • verified privacy breach
     • formal grievance escalation

Keep it conservative to avoid muddy ground truth.


8.4 Evaluation metrics (required)

     • Calibration: Brier score, reliability curve
     • Discrimination: AUC, log-loss
     • Lead time: time-to-event detection
     • Governance safety: empirical Pr(E = 1 ∣ pass)
     • Stability: frequency of Λm clipping; certificate failure rate




9. Release discipline
CMG must ship with:


     • an immutable log schema,
     • a model registry with versioning,
     • certificate outputs stored per window,
     • and a reproducible evaluation notebook/runner that regenerates all metrics.

Steering is only enabled after:


    1. identifiability checks pass,
    2. calibration meets thresholds, and
    3. certificate failures are rare and explainable.




10. External references (selected)
This section lists foundational references that support CMG’s core modules (contraction certification, small-
gain feedback discipline, state-space inference and robust filtering, calibration, reciprocity theory, commons
governance, and tensor methods).



                                                        11
10.1 Contraction, fixed points, and stability certificates

    • Banach, S. (1922). Sur les opérations dans les ensembles abstraits et leur application aux équations
      intégrales. Fundamenta Mathematicae, 3(1), 133–181.
      (Foundational fixed-point / contraction principle.)

10.2 Small-gain and feedback interconnections

    • Jiang, Z.-P., Teel, A. R., & Praly, L. (1994). Small-gain theorem for ISS systems and applications.
      Mathematics of Control, Signals and Systems, 7, 95–120.
      (Canonical nonlinear small-gain/ISS reference; motivates CMG’s “legal coupling” philosophy.)

10.3 State-space modeling and filtering

    • Kalman, R. E. (1960). A new approach to linear filtering and prediction problems. Journal of Basic
      Engineering, 82(1), 35–45.
      (Origin of Kalman filtering.)


    • Shumway, R. H., & Stoffer, D. S. (1982). An approach to time series smoothing and forecasting using the
      EM algorithm. Journal of Time Series Analysis, 3(4), 253–264.
      (EM for linear dynamical systems / smoothing; motivates CMG’s staged fitting plan.)


    • Dempster, A. P., Laird, N. M., & Rubin, D. B. (1977). Maximum likelihood from incomplete data via the EM
      algorithm. Journal of the Royal Statistical Society: Series B (Methodological), 39(1), 1–38.
      (General EM machinery used in LDS estimation.)


    • Doucet, A., de Freitas, N., & Gordon, N. (Eds.). (2001). Sequential Monte Carlo Methods in Practice.
      Springer.
      (Particle filtering / SMC foundations for CMG’s robust inference layer.)


10.4 Robust statistics (for heavy tails and outliers)

    • Huber, P. J. (1964). Robust estimation of a location parameter. The Annals of Mathematical Statistics,
      35(1), 73–101.
      (Canonical robust estimation; informs robust innovations before Student-t.)

10.5 Forecast evaluation and probability calibration

    • Brier, G. W. (1950). Verification of forecasts expressed in terms of probability. Monthly Weather Review,
      78(1), 1–3.
      (Brier score; calibration as a first-class metric.)


    • DeGroot, M. H., & Fienberg, S. E. (1983). The comparison and evaluation of forecasters. Journal of the
      Royal Statistical Society: Series D (The Statistician), 32(1–2), 12–22.
      (Foundational calibration/refinement framing; motivates CMG’s reliability discipline.)




                                                      12
     • Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017). On calibration of modern neural networks. In
       ICML 2017, PMLR 70, 1321–1330.
       (Modern calibration toolkit; useful if CMG uses flexible learners later.)


10.6 Reciprocity and cooperation (conceptual grounding)

     • Axelrod, R. (1984). The Evolution of Cooperation. Basic Books.
       (Reciprocity dynamics and incentives; background for anti-gaming constraints.)


     • Nowak, M. A., & Sigmund, K. (1998). Evolution of indirect reciprocity by image scoring. Nature, 393,
       573–577.
       (Reputation-mediated reciprocity; informs measurement design beyond pairwise exchange.)


     • Nowak, M. A., & Sigmund, K. (2005). Evolution of indirect reciprocity. Nature, 437(7063), 1291–1298.
       (Broader synthesis; clarifies when reciprocity must be modeled beyond dyads.)


10.7 Commons governance and institutional design

     • Ostrom, E. (1990). Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge
       University Press.
       (Institutional principles for commons; complements CMG’s rights-first procedural layer.)

10.8 Tensor decompositions (auditing layer)

     • Kolda, T. G., & Bader, B. W. (2009). Tensor decompositions and applications. SIAM Review, 51(3), 455–
       500.
       (Survey of CP/Tucker and software ecosystem; base reference for tensorial auditing.)

Citizen Gardens © 2025 CC-NC-ND 4.0




                                                     13

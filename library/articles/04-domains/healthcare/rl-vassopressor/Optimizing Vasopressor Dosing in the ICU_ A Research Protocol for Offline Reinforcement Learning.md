---
slug: optimizing-vasopressor-dosing-in-the-icu-a-research-protocol-for-offline-reinforcement-learning
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 04-domains/healthcare/rl-vassopressor/Optimizing Vasopressor Dosing in the
    ICU_ A Research Protocol for Offline Reinforcement Learning.md
  last_synced: '2026-03-20T17:17:18.750198Z'
---

**Optimizing Vasopressor Dosing in the ICU: A Research Protocol for Offline Reinforcement Learning**
====================================================================================================

### **1.0 Introduction and Rationale**

The management of patients in shock within the intensive care unit (ICU)
is a persistent and high-stakes clinical challenge. A central component
of this care is the administration of vasopressors---potent medications
used to restore adequate blood pressure. The effective dosing of these
agents represents a critical juncture in patient care, with direct and
immediate impacts on outcomes.

The core clinical problem lies in navigating a narrow therapeutic window
with incomplete information. Clinicians must maintain a delicate
balance: insufficient dosing can lead to prolonged hypotension and
subsequent organ damage, while excessive dosing is associated with
severe complications, including arrhythmias and ischemia. This difficult
trade-off, performed under pressure, results in significant practice
variability and presents a clear opportunity for data-driven clinical
decision support.

Offline reinforcement learning (RL) has emerged as an innovative and
powerful solution to this challenge. Its core value proposition is the
ability to learn data-driven clinical policies by leveraging the vast
experience captured in existing observational datasets, such as
electronic health records (EHRs). By analyzing thousands of patient
trajectories, offline RL can derive a vasopressor dosing strategy that
systematically learns the complex relationship between patient states,
clinician actions, and subsequent outcomes.

The primary purpose of this proposal is to specify a comprehensive,
pre-registered protocol for learning, rigorously evaluating, and
ensuring the safety of a novel vasopressor dosing policy derived using
offline RL. This document serves as a blueprint to guide the development
of a decision-support tool that is not only potentially more effective
but also robust, reliable, and trustworthy.

This protocol begins by defining the specific, measurable objectives
that will guide the entire research endeavor.

### **2.0 Study Objectives**

Clearly defined study endpoints provide the precise, clinically
meaningful criteria against which the success and safety of the learned
policy will be measured. This ensures a focused, transparent evaluation
aligned with outcomes that matter to patients and clinicians.

**Primary Objective** To learn a vasopressor dosing policy (*πθ*) from
observational data that maximizes the primary clinical endpoint of
vasopressor-free hours (VFH) over a 72-hour period.

**Secondary Objectives** The learned policy will also be evaluated on
its impact on the following secondary endpoints:

-   In-ICU mortality

-   Progression of Acute Kidney Injury (AKI)

-   Total norepinephrine-equivalent exposure

-   Hypotension burden, defined as the time-under-threshold for Mean
    > Arterial Pressure

The following sections detail the rigorous methodology designed to
achieve these objectives in a reproducible and scientifically sound
manner.

### **3.0 Research Design and Methodology**

This section serves as the operational blueprint for the study. The
following subsections detail the study design, cohort definition, data
processing, and the formal problem definition. Each component is crucial
for ensuring the reproducibility and validity of the research findings
and for transforming the clinical challenge into a concrete
computational problem.

**Overall Study Design** This study is a retrospective analysis of
observational ICU data from large, publicly available cohorts, such as
the eICU Collaborative Research Database and the MIMIC-IV database. The
investigation will leverage offline reinforcement learning to develop
and evaluate a new clinical policy for vasopressor dosing.

**Study Population** The patient cohort will be defined according to the
following selection criteria:

-   **Inclusion Criteria:**

    -   Adult patients (≥18 years) admitted to the ICU.

    -   Patients with a diagnosis of shock who are receiving any
        > vasopressor agent.

-   **Exclusion Criteria:**

    -   Patients with an ICU length of stay less than 6 hours.

    -   Patients with greater than 30% missing Mean Arterial Pressure
        > (MAP) or vasopressor dose data within the first 24 hours of
        > treatment.

**Markov Decision Process (MDP) Formulation** To apply reinforcement
learning, the clinical problem of vasopressor dosing is formalized as a
Markov Decision Process (MDP). This mathematical framework provides the
necessary structure---states, actions, rewards, and terminal
conditions---for the algorithm to learn an optimal strategy.

-   **State Space (s):** The state vector represents a comprehensive
    > snapshot of a patient\'s clinical condition at a given hour. It
    > includes:

    -   Demographics (e.g., age, sex) and comorbidities

    -   Vital signs (e.g., MAP, heart rate)

    -   Laboratory results (e.g., lactate, creatinine)

    -   Urine output and fluid balance

    -   Ventilation status

    -   Current vasopressor dose

    -   Time since ICU admission

    -   Missingness flags for imputed variables

-   **Action Space (a):** The action is defined as the discretized
    > norepinephrine-equivalent vasopressor dose administered during a
    > given hour. An optional co-action representing whether a fluid
    > bolus was administered in the past hour may also be included.

-   **Reward Function (r):** The reward function is explicitly designed
    > to balance the goal of liberating a patient from vasopressors
    > while preventing hypotension. The function is defined as: rt =
    > ⊮\[no vasopressor\] − λ⊮\[MAP \< 65mmHg\] The clinical intuition
    > is straightforward: the policy is rewarded for hours spent off
    > vasopressors and penalized for hours where the MAP falls below the
    > critical threshold of 65 mmHg. The hyperparameter *λ* serves as a
    > weighting factor to adjust the relative importance of the
    > hypotension penalty.

-   **Terminal Conditions:** A patient\'s trajectory is considered
    > complete upon either discharge from the ICU or in-ICU death.

This formal MDP structure provides the necessary foundation for applying
the specific learning algorithms and safety frameworks detailed in the
following section.

### **4.0 Policy Learning and Safety Framework**

This section details the advanced algorithm chosen to learn a robust
policy and, just as importantly, the multi-layered safety framework
designed to ensure the policy\'s recommendations are clinically
plausible and safe. This dual focus on performance and safety is
non-negotiable for any artificial intelligence system intended for
clinical use.

**Policy Learning Algorithm: Conservative Q-Learning (CQL)** The primary
learning algorithm is Conservative Q-Learning (CQL), which is
specifically chosen to address the critical challenge of *extrapolation
error* in offline RL. This error occurs when a model makes unrealistic
and overly optimistic value predictions for actions not well-represented
in the training data. CQL mitigates this risk by adding a regularization
term that learns a conservative Q-function, effectively pushing down
Q-values for out-of-distribution actions while pushing up Q-values for
actions observed in the dataset.

The final soft policy is extracted from the learned Q-function using the
following formula, where *τ* is a temperature parameter: πθ(a \| s) ∝
exp{Qϕ(fψ(s), a)/τ}

**Behavior Policy Estimation (β̂)** A critical component of this
framework is the accurate modeling of the clinicians\' historical dosing
strategy, referred to as the \"behavior policy\" (β̂). This model
estimates the probability that a clinician would have taken a specific
action given a patient\'s state. Potential models for this task include
calibrated multinomial logistic regression or gradient boosting
classifiers. The fidelity of this model is paramount, and its
calibration will be rigorously assessed using a suite of three metrics:

-   Reliability diagrams

-   Expected Calibration Error (ECE)

-   Brier Score

**Pre-Specified Safety Constraints** To ensure patient safety and
clinical feasibility, the learned policy will be augmented with a series
of hard-coded rules. These constraints are designed to prevent the model
from recommending actions that are excessively different from observed
practice or are clinically unstable.

1.  **KL Trust Region:** A mathematical constraint, KL(πθ \|\| β̂) ≤ ε,
    > will be enforced to ensure the learned policy does not deviate
    > excessively from the observed clinical practice. This acts as a
    > global \"trust region\" around the historical standard of care.

2.  **Action-Ratio Cap:** This rule prevents the policy from taking any
    > action a where the likelihood ratio πθ(a \| s) / β̂(a \| s) exceeds
    > a pre-defined threshold. This provides a state-specific safety
    > layer, rejecting actions that are highly unlikely under the
    > behavior policy, and serves a crucial technical purpose: to ensure
    > the stability of the importance sampling weights used in OPE
    > methods.

3.  **Dose Monotonicity Rule:** This clinical heuristic enforces dose
    > stability. The policy is constrained to recommend a non-increasing
    > dose if a patient is stable (MAP ≥65 mmHg for ≥2 hours) and their
    > lactate is not worsening (slope ≤ 0 over the past 4 hours). In all
    > other states, dose changes are limited to at most one discrete bin
    > per hour to prevent abrupt and potentially dangerous adjustments.

With the learning and safety framework established, we next specify the
rigorous methods for evaluating the final, constrained policy.

### **5.0 Evaluation and Analysis Plan**

A multi-faceted evaluation framework is essential for establishing
confidence in the learned policy\'s estimated clinical value and
robustness. This approach combines rigorous off-policy evaluation to
estimate performance on held-out data, benchmarking against alternative
models, and a series of sensitivity analyses to test the stability of
the findings.

**Off-Policy Evaluation (OPE)** Off-policy evaluation (OPE) methods are
required to estimate the clinical value of the new policy using only
held-out test data, without deploying it in a live environment. To
ensure a robust estimate, three distinct OPE estimators will be
employed:

-   **Self-Normalized Importance Sampling (SNIPS):** A foundational
    > method that calculates a weighted average of the observed rewards,
    > re-weighted by the likelihood ratio of the new policy to the
    > behavior policy.

-   **Doubly Robust (DR) Estimation:** A more advanced method that
    > combines a regression-based model with importance sampling. Its
    > \"doubly robust\" property means the estimate is consistent if
    > *either* the regression model (Q-model) *or* the behavior policy
    > model is correctly specified, making it more robust to modeling
    > errors.

-   **Fitted Q Evaluation (FQE):** A model-based approach that directly
    > learns the value function (Q-function) for the new policy.

All point estimates from these methods will be reported with 95%
confidence intervals generated via a 1000-sample patient-level bootstrap
to provide a clear assessment of uncertainty.

**Baseline Comparisons** The performance of the learned policy will be
benchmarked against a suite of alternative models to provide context.
These baselines include supervised outcome models, Behavior Cloning
(BC), other offline RL algorithms (BCQ, IQL), and a PID-style heuristic
controller.

**Robustness and Sensitivity Analyses** A series of analyses are planned
to test the stability of the study\'s conclusions against key modeling
decisions and assumptions.

-   **Hyperparameter Sensitivity:** The impact of varying key parameters
    > will be analyzed, including the action discretization scheme (K,
    > Δ), the CQL penalty weight (α), the policy temperature (τ), and
    > the reward penalty weight (λ).

-   **Negative Control Outcomes:** The policy will be evaluated on
    > outcomes that it should not plausibly affect. The absence of an
    > effect would provide evidence against certain types of unmeasured
    > confounding.

-   **Unobserved Confounding:** The potential impact of unmeasured
    > confounders on the study\'s conclusions will be assessed using
    > methods such as Rosenbaum sensitivity bounds.

Before this evaluation plan is executed, the project must adhere to the
strict governance procedures and readiness checks outlined below.

### **6.0 Study Governance and Readiness**

Scientific rigor in data-driven clinical research depends on
pre-specification, transparency, and clear criteria for success. This
section outlines the procedural safeguards and decision gates that will
govern the study\'s execution, ensuring that the path from development
to potential implementation is guided by objective evidence.

**Pre-Execution Readiness Checklist** The following steps must be
completed and documented *before* any model training or evaluation is
initiated on the final datasets:

1.  **Data Governance:** Confirmation of IRB approval and that a
    > reproducible, version-controlled data extraction pipeline is in
    > place.

2.  **Data Integrity:** Completion of a comprehensive data dictionary
    > and formal, pharmacist-led validation of the
    > norepinephrine-equivalent dose mapping.

3.  **Modeling Pre-specification:** Finalization of behavior model
    > calibration targets and all safety thresholds (ε, cmax).

4.  **Statistical Plan:** Completion of a power analysis for the OPE
    > estimators to determine the minimal detectable effect size.

5.  **Pre-registration:** Filing of the complete protocol, including all
    > endpoints, cohort criteria, and hyperparameter grids, in a public
    > repository.

6.  **Oversight:** Establishment of a Data and Safety Monitoring Board
    > (DSMB) charter for any future prospective studies.

**Policy Acceptance Criteria** The final learned policy will only be
considered for prospective deployment if it successfully passes all of
the following pre-defined \"Acceptance Gates\" on the held-out test set:

1.  **Superior Value:** The 95% lower confidence bound of the value
    > lift, as estimated by the doubly robust estimator, V̂DR(πθ) -
    > V̂DR(β̂), must be greater than a pre-specified positive threshold
    > *δ*.

2.  **Importance Weight Health:** The importance weights must be
    > well-behaved, as defined by three conditions: the maximum weight
    > must not exceed a pre-specified cap (max i,t wi,t ≤ cmax), the
    > median weight must be below a threshold m, and the effective
    > sample size (ESS) must be greater than E for at least p% of
    > trajectories.

3.  **Safety Non-Inferiority:** The policy must demonstrate no
    > statistically significant degradation in key safety outcomes
    > (mortality, AKI progression) when compared to the behavior policy,
    > after appropriate correction for multiple comparisons.

4.  **Sufficient Overlap:** The fraction of evaluated state-action pairs
    > that fall outside the support of the training data must be below a
    > pre-specified threshold, and those state-action pairs falling
    > outside the support will be masked during inference.

5.  **Behavior Model Calibration:** The behavior policy model β̂ must
    > pass its pre-specified ECE and Brier score thresholds on the test
    > set.

6.  **Guardrail Adherence:** The policy must not violate any
    > pre-specified safety guardrails during simulated replays on the
    > validation set.

This rigorous governance is underpinned by the inherent challenges of
observational data analysis, which are addressed directly in the
following section.

### **7.0 Limitations and Mitigation Strategies**

Any analysis of observational data has inherent limitations. This
proposal directly acknowledges these challenges and integrates specific
methodological choices designed to mitigate their potential impact,
ensuring a transparent and honest assessment of the findings.

  Limitation                                          Mitigation Strategy
  --------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Observational Confounding Risk**                  Utilize sensitivity analyses (e.g., Rosenbaum bounds) and evaluate negative control outcomes to detect potential systemic bias from unmeasured variables.
  **Discretized Action Space**                        Assess the impact of representing continuous doses as discrete bins via sensitivity analysis on the number and size of the dose bins (K, Δ).
  **High Variance of OPE Estimators**                 Formally audit the dataset for sufficient state-action overlap and rely on a consensus of multiple OPE methods (SNIPS, DR, FQE) to ensure stable estimates.
  **Reward Shaping Encodes Subjective Preferences**   Conduct a sensitivity analysis by sweeping the reward weight parameter λ to understand its impact on the final learned policy and the clinical trade-offs it implies.

By acknowledging these limitations and proactively addressing them, we
can proceed with a clear-eyed view of the long-term vision for this
research.

### **8.0 Dissemination and Future Deployment Pathway**

The long-term vision of this research is to translate retrospective
findings into tangible clinical impact. Should the learned policy
successfully pass all acceptance criteria, a phased deployment pathway
is proposed to ensure a safe, effective, and evidence-driven transition
from a validated offline model to a real-world clinical tool.

1.  **Phase 1: Silent Mode:** The model will be deployed prospectively
    > in a non-interventional \"silent mode.\" It will receive real-time
    > patient data and generate recommendations that are logged for
    > validation but not shown to clinicians. This phase allows for
    > analysis of the model\'s real-world behavior without impacting
    > patient care.

2.  **Phase 2: Guardrailed Suggestions:** Following a successful silent
    > mode evaluation, the model\'s recommendations will be introduced
    > into the clinical workflow as a decision-support tool. Initially,
    > these suggestions will be heavily guardrailed, appearing only
    > under high-confidence conditions or when its suggestion aligns
    > with the likely action of the clinician behavior model.

3.  **Phase 3: Randomized Controlled Trial (RCT):** The final stage of
    > evaluation is a formal RCT to definitively assess the policy\'s
    > clinical efficacy and impact on patient outcomes compared to the
    > standard of care. Critically, clinicians will always retain the
    > final authority to override any AI-generated suggestion.

This protocol\'s strength lies in the synthesis of a safety-aware
offline RL algorithm (CQL) with a multi-layered framework for clinical
plausibility, rigorous statistical validation, and pre-registered
scientific governance. By adhering to this structured and transparent
protocol, this project provides a robust framework for developing an
AI-driven vasopressor policy, paving the way for a rigorous, phased
evaluation from retrospective validation to prospective clinical impact.

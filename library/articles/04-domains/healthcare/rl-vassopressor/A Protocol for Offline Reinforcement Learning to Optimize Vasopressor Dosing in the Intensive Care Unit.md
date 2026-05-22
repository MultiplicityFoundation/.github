---
slug: a-protocol-for-offline-reinforcement-learning-to-optimize-vasopressor-dosing-in-the-intensive-care-unit
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 04-domains/healthcare/rl-vassopressor/A Protocol for Offline Reinforcement
    Learning to Optimize Vasopressor Dosing in the Intensive Care Unit.md
  last_synced: '2026-03-20T17:17:18.735702Z'
---

**A Protocol for Offline Reinforcement Learning to Optimize Vasopressor Dosing in the Intensive Care Unit**
===========================================================================================================

### **1.0 Introduction and Rationale**

The management of patients in shock within the intensive care unit (ICU)
presents a persistent clinical challenge. A central component of this
care is the administration of vasopressors, potent medications used to
restore and maintain adequate blood pressure. The dosing of these agents
requires a delicate balance: insufficient dosing can lead to prolonged
hypotension and organ damage, while excessive dosing is associated with
complications such as arrhythmias and ischemia. Clinicians must navigate
this narrow therapeutic window using incomplete information, leading to
significant practice variability and a clear opportunity for data-driven
clinical decision support.

Offline reinforcement learning (RL) has emerged as a powerful
methodology for deriving data-driven clinical policies from large,
existing observational datasets. The core value proposition of this
approach lies in its ability to leverage the vast repository of clinical
experience captured in electronic health records (EHRs). By analyzing
thousands of patient trajectories, offline RL can learn a vasopressor
dosing strategy that systematically explores the relationship between
actions (doses), patient states, and subsequent outcomes, with the goal
of improving patient health.

The overall purpose of this document is to specify a comprehensive,
pre-registered protocol for learning, evaluating, and ensuring the
safety of a novel vasopressor dosing policy derived using offline RL.
This document therefore serves as a pre-specified protocol to rigorously
guide the development and evaluation of this policy, beginning with the
primary and secondary clinical endpoints.

### **2.0 Study Objectives**

Clearly defined study endpoints are of strategic importance, as they
provide the precise criteria against which the success and safety of the
learned policy will be measured. These objectives ensure that the
evaluation is focused, transparent, and aligned with clinically
meaningful outcomes.

-   **Primary Objective:**

    -   To learn a vasopressor dosing policy (*πθ*) from observational
        > data that maximizes the primary clinical endpoint of
        > **vasopressor-free hours (VFH)** over a 72-hour period.

-   **Secondary Objectives:**

    -   Evaluate the learned policy\'s impact on **in-ICU mortality**.

    -   Assess the effect on the progression of **Acute Kidney Injury
        > (AKI)**.

    -   Quantify the total **norepinephrine-equivalent exposure**.

    -   Measure the impact on **hypotension burden**, defined as the
        > time-under-threshold for Mean Arterial Pressure (MAP).

The subsequent sections of this protocol detail the rigorous methodology
designed to achieve these objectives in a reproducible and
scientifically sound manner.

### **3.0 Study Design and Methodology**

This section operationalizes the study objectives by providing a
detailed specification of the study design, cohort definition, data
processing pipeline, and the formal Markov Decision Process that frames
the clinical problem. These elements are crucial for ensuring the
reproducibility and validity of the findings, providing a clear
blueprint for data handling, modeling, and analysis.

#### **3.1 Overall Study Design**

This study is a retrospective analysis of observational ICU data. The
investigation will leverage offline reinforcement learning to develop
and evaluate a new clinical policy for vasopressor dosing. The potential
data sources for this analysis include large, publicly available
critical care cohorts such as the eICU Collaborative Research Database
and the MIMIC-IV database.

#### **3.2 Study Population and Cohort Selection**

The patient cohort will be defined according to the following criteria:

-   **Inclusion Criteria:** Adult patients (≥18 years) admitted to the
    > ICU who are diagnosed with shock and are receiving any vasopressor
    > agent.

-   **Exclusion Criteria:**

    -   Patients with ICU stays shorter than 6 hours.

    -   Patients with greater than 30% of Mean Arterial Pressure (MAP)
        > or vasopressor dose data missing within the first 24 hours of
        > treatment.

#### **3.3 Data Acquisition and Preprocessing**

Patient data will be structured into trajectories, with each patient\'s
ICU stay aligned to a 1-hour time grid spanning a maximum of 72 hours
from the initiation of vasopressor therapy. Data preprocessing will
involve several key steps to ensure consistency and quality.
Intermittent laboratory values will be handled using a carry-forward
imputation method. To account for this process, missingness indicators
will be included as features in the model. All continuous features will
be standardized using the mean and standard deviation derived
*exclusively from the training set*. This practice is essential to
prevent data leakage from the validation and test sets into the training
process.

#### **3.4 Markov Decision Process (MDP) Formulation**

To apply reinforcement learning, the clinical problem of vasopressor
dosing is formalized as a Markov Decision Process (MDP). This framework
consists of states, actions, rewards, and terminal conditions, which are
defined as follows.

##### **3.4.1 State Space (s)**

The state vector, st, represents a comprehensive snapshot of a
patient\'s clinical condition at a given hour and includes the following
components:

-   Demographics (e.g., age, sex)

-   Comorbidities

-   Vital signs (e.g., MAP, heart rate)

-   Laboratory results (e.g., lactate, creatinine)

-   Urine output and fluid balance

-   Ventilation status

-   Current vasopressor dose

-   Time since ICU admission

-   Missingness flags for imputed variables

##### **3.4.2 Action Space (a)**

The action, at, is defined as the discretized norepinephrine-equivalent
vasopressor dose administered during a given hour. The model may also
consider an optional co-action representing whether a fluid bolus was
administered in the past hour.

##### **3.4.3 Reward Function (r)**

The per-hour reward function is explicitly designed to balance the goals
of liberating a patient from vasopressors while preventing hypotension.
The function is defined as:

rt = ⊮\[no vasopressor\] − λ⊮\[MAP \< 65mmHg\]

Here, the policy is rewarded for hours spent off vasopressors and
penalized for hours where the MAP falls below the critical threshold of
65 mmHg. The hyperparameter λ serves as a weighting factor to adjust the
relative importance of the hypotension penalty.

##### **3.4.4 Terminal Conditions**

A patient\'s trajectory is considered complete, or terminal, upon either
discharge from the ICU or in-ICU death.

This formal MDP structure provides the necessary foundation for applying
the specific learning algorithms detailed in the following section.

### **4.0 Policy Learning and Modeling**

This section details the specific algorithms and safety constraints
chosen to learn a robust and clinically plausible policy from the
observational data. The selected approach is designed to maximize the
potential for clinical utility while rigorously controlling for the
risks inherent in learning from offline, non-randomized data.

#### **4.1 Policy Learning Algorithm: Conservative Q-Learning (CQL)**

The primary learning algorithm for this study is **Conservative
Q-Learning (CQL)**. This algorithm is specifically designed to address a
critical failure mode in offline RL known as extrapolation error, which
occurs when a model makes unrealistic value predictions for actions not
well-represented in the training data. CQL mitigates this risk by adding
a regularization term that learns a conservative Q-function by pushing
down Q-values for out-of-distribution actions while pushing up Q-values
for actions present in the dataset. The final policy, *πθ*, will be
extracted as a soft policy proportional to the exponentiated Q-values
learned by the CQL model, governed by a temperature parameter τ: πθ(a \|
s) ∝ exp{Qϕ(fψ(s), a)/τ}.

#### **4.2 Behavior Policy Estimation**

A critical component of offline RL is the accurate modeling of the
clinicians\' historical dosing policy, referred to as the \"behavior
policy\" (*β̂*). This model estimates the probability that a clinician
would have taken a specific action given a patient\'s state. Potential
models for this task include calibrated multinomial logistic regression
or gradient boosting classifiers. The calibration of *β̂* will be
rigorously assessed using a suite of metrics to ensure its fidelity:

-   **Reliability diagrams:** To visually assess the correspondence
    > between predicted probabilities and observed frequencies.

-   **Expected Calibration Error (ECE):** A quantitative measure of
    > miscalibration across all probability bins.

-   **Brier Score:** A comprehensive metric that assesses both the
    > accuracy and calibration of the probabilistic predictions.

#### **4.3 Pre-Specified Safety Constraints**

To ensure patient safety and clinical feasibility, the learned policy
*πθ* will be augmented with a series of pre-specified, hard-coded rules.
These constraints are designed to prevent the model from recommending
actions that are excessively different from observed practice or
clinically unstable.

1.  **KL Trust Region:** A Kullback-Leibler (KL) divergence constraint
    > (KL(πθ \|\| β̂) ≤ ε) will be enforced. This mathematical constraint
    > ensures that the learned policy does not deviate excessively from
    > the observed clinical practice, acting as a global \"trust
    > region\" around the behavior policy.

2.  **Action-Ratio Cap:** The policy will be prevented from taking any
    > action a where the likelihood ratio πθ(a \| s) / β̂(a \| s) exceeds
    > a pre-defined maximum threshold cmax. This rule provides a
    > state-specific safety layer, rejecting actions that are highly
    > unlikely under the behavior policy.

3.  **Dose Monotonicity Rule:** A clinical heuristic will be implemented
    > to enforce dose stability. The policy is constrained to recommend
    > a non-increasing dose if two conditions are met: the patient\'s
    > MAP has been stable (≥65 mmHg for ≥2 hours) AND their lactate is
    > not worsening (slope ≤ 0 over the past 4 hours). In all other
    > states, dose changes are limited to at most one discrete bin per
    > hour.

With the learning and safety framework established, the protocol next
turns to the methods that will be used to evaluate the final,
constrained policy.

### **5.0 Evaluation and Analysis Plan**

This section outlines the comprehensive evaluation framework designed to
assess the learned policy\'s performance and robustness. A multi-faceted
approach is essential for establishing confidence in the policy\'s
estimated clinical value. This includes rigorous off-policy evaluation
to estimate performance on held-out data, benchmarking against
alternative models, and a series of sensitivity analyses to test the
stability of the findings.

#### **5.1 Off-Policy Evaluation (OPE)**

Off-policy evaluation (OPE) methods are required to estimate the
clinical value of the new policy *πθ* using only the held-out test
dataset, without deploying it in a live environment. To ensure a robust
estimate, three distinct OPE estimators will be employed:

-   **Self-Normalized Importance Sampling (SNIPS):** This method
    > calculates a weighted average of the observed rewards, where each
    > trajectory is re-weighted by the likelihood ratio of the new
    > policy to the behavior policy. The normalization helps control for
    > variance \[13\].

-   **Doubly Robust (DR) Estimation:** This estimator combines a
    > regression-based model of state-action values with importance
    > sampling. Its \"doubly robust\" property means the estimate is
    > consistent if *either* the regression model (Q-model) *or* the
    > behavior policy model is correctly specified, making it more
    > robust to modeling errors than estimators that rely on only one
    > model \[6\].

-   **Fitted Q Evaluation (FQE):** This method involves learning a
    > Q-function specifically for the new policy *πθ* by iterating on
    > the Bellman equation. The estimated value of the policy is then
    > derived from this learned Q-function \[10\].

All point estimates from these methods will be reported with 95%
confidence intervals generated via a 1000-sample patient-level
bootstrap.

#### **5.2 Baseline Comparisons**

The performance of the learned policy (*πθ*) will be benchmarked against
a suite of alternative models to provide context for its performance.
These baselines include:

-   Supervised outcome models

-   Behavior Cloning (BC)

-   Alternative offline RL algorithms (Batch-Constrained Q-Learning
    > \[BCQ\], Implicit Q-Learning \[IQL\])

-   A PID-style heuristic controller

#### **5.3 Robustness and Sensitivity Analyses**

A series of analyses are planned to test the robustness of the study\'s
conclusions to key modeling decisions and assumptions.

-   **Hyperparameter Sensitivity:** The impact of varying key parameters
    > will be analyzed, including the action discretization scheme (K,
    > ∆), the CQL penalty weight (α), the policy temperature (τ), and
    > the reward penalty weight (λ).

-   **Negative Control Outcomes:** The policy will be evaluated on
    > outcomes that it should not plausibly affect. The absence of an
    > effect on these outcomes would provide evidence against certain
    > types of unmeasured confounding.

-   **Unobserved Confounding:** The potential impact of unmeasured
    > confounders on the study\'s conclusions will be assessed using
    > methods such as Rosenbaum sensitivity bounds.

Before this final evaluation is conducted, the study must pass a series
of readiness checks and adhere to strict governance procedures.

### **6.0 Study Governance and Readiness**

Scientific rigor in data-driven clinical research depends on
pre-specification, transparency, and clear criteria for success. This
section outlines the procedural safeguards and decision gates that will
govern the study\'s execution, from initial data access to the final
decision on whether the learned policy is suitable for further testing.

#### **6.1 Pre-Execution Readiness Checklist**

The following steps must be completed and documented *before* any model
training or evaluation is initiated on the final datasets:

1.  **Data Governance:** Confirmation that data use has been approved by
    > the relevant institutional bodies, the de-identified dataset is
    > available and secured, and the data extraction pipeline is
    > version-controlled and reproducible.

2.  **Data Integrity:** Completion of a comprehensive data dictionary,
    > validation of all variable units and physiological ranges, and a
    > formal pharmacist-led validation of the norepinephrine-equivalent
    > dose mapping.

3.  **Modeling Pre-specification:** Finalization of all temporal
    > alignment rules (e.g., time zero definition, resampling),
    > confirmation that the behavior model (*β̂*) meets its calibration
    > targets, an audit of the state-action space to ensure sufficient
    > data overlap, and pre-specification of all safety thresholds (ε,
    > cmax).

4.  **Statistical Plan:** Completion of a power analysis for the OPE
    > estimators to determine the minimal detectable effect size, given
    > the variance and effective sample size of the dataset.

5.  **Pre-registration:** Filing of a complete pre-registration of the
    > protocol in a public repository. This will include all primary and
    > secondary endpoints, cohort inclusion/exclusion criteria,
    > hyperparameter grids, and random seeds to be used for model
    > training.

6.  **Oversight:** Establishment of a Data and Safety Monitoring Board
    > (DSMB) charter, an incident reporting plan for future prospective
    > studies, and a defined \"kill switch\" mechanism for any potential
    > deployment.

#### **6.2 Policy Acceptance Criteria**

The final learned policy, *πθ*, will only be accepted for consideration
in a prospective, silent-mode deployment if it successfully passes a
series of pre-defined \"Acceptance Gates\" on the held-out test set. All
of the following criteria must be met:

1.  **Superior Value:** The 95% lower confidence bound of the value
    > lift, as estimated by the doubly robust estimator, V̂DR(πθ) -
    > V̂DR(β̂), must be greater than a pre-specified positive threshold δ.

2.  **Importance Weight Health:** The importance weights (wi,t) must be
    > well-behaved, as defined by: 1) the maximum weight across all
    > trajectories and timepoints must not exceed a pre-specified cap
    > (max i,t wi,t ≤ cmax), 2) the median weight must be below a
    > threshold m, and 3) the effective sample size (ESS) must be
    > greater than E for at least p% of trajectories.

3.  **Safety Non-Inferiority:** The policy must demonstrate no
    > statistically significant degradation in key safety outcomes
    > (mortality, AKI, hypotension burden) when compared to the behavior
    > policy, after appropriate correction for multiple comparisons.

4.  **Sufficient Overlap:** The fraction of state-action pairs evaluated
    > that fall outside the support of the training data must be below a
    > pre-specified threshold q%, and those state-action pairs falling
    > outside the support will be masked during inference.

5.  **Behavior Model Calibration:** The behavior policy model *β̂* must
    > pass its pre-specified ECE and Brier score thresholds on the test
    > set.

6.  **Guardrail Adherence:** The policy must not violate any of the
    > pre-specified safety guardrails (KL divergence or action-ratio
    > caps) during simulated replays on the validation set.

### **7.0 Data Management and Dictionary**

A meticulously documented data dictionary is essential for the
reproducibility, clarity, and extension of this research. The following
table provides the schema and examples for the variables to be included
in the analysis.

  Name                     Type          Unit           Sampling    Preprocessing                                   Range
  ------------------------ ------------- -------------- ----------- ----------------------------------------------- -------------
  **Patient ID**           categorical   --             episode     Hashed, one-hot                                 unique
  **Age**                  numeric       years          baseline    z-score                                         \[18,120\]
  **Sex**                  categorical   --             baseline    one-hot                                         M/F/other
  **MAP**                  numeric       mmHg           hourly      Carry-forward 2h max; winsorize 0.5%            \[30,140\]
  **Heart rate**           numeric       bpm            hourly      Carry-forward 2h; z-score                       \[30,220\]
  **Lactate**              numeric       mmol/L         lab times   Forward-fill 6h; missing flag                   \[0.5,20\]
  **Creatinine**           numeric       mg/dL          lab times   Forward-fill 24h; missing flag                  \[0.3,12\]
  **Urine output**         numeric       mL             hourly      None; rolling 6h sum                            \[0,1000\]
  **Ventilation status**   categorical   --             hourly      Binary encode                                   0/1
  **Fluid bolus**          categorical   mL             hourly      Binary in past hour                             0/1
  **Vaso dose (NE-eq)**    numeric       µg kg⁻¹min⁻¹   hourly      Map from drug-specific doses; discretize by ∆   {0,∆, \...}
  **Time since admit**     numeric       h              hourly      None                                            \[0,72\]
  **Missingness flags**    categorical   --             hourly      One-hot per variable                            0/1

**Dose Mapping** A separate, detailed table is required to convert all
administered vasopressor agents (e.g., epinephrine, vasopressin,
dopamine) into standardized norepinephrine equivalents. This conversion
table must be developed and reviewed by a clinical pharmacist to ensure
its accuracy and clinical validity.

### **8.0 Limitations and Mitigation Strategies**

The following limitations are inherent to any offline RL analysis of
observational data. We detail them here alongside the specific
methodological choices---such as the use of multiple OPE estimators,
Rosenbaum bounds, and pre-specified safety guardrails---that have been
integrated into this protocol to directly mitigate their impact.

  Limitation                                          Mitigation Strategy
  --------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Observational Confounding Risk**                  The relationship between actions and outcomes may be biased by unmeasured variables. This will be addressed through the use of sensitivity analyses (e.g., Rosenbaum bounds) and the evaluation of negative control outcomes to detect potential systemic bias.
  **Discretized Action Space**                        Representing continuous vasopressor doses as discrete bins may limit the fidelity of the learned policy. The impact of this choice will be assessed via sensitivity analysis on the number and size of the dose bins.
  **High Variance of OPE Estimators**                 Off-policy evaluation can be unreliable if there is poor overlap between the learned policy and the behavior policy. This will be mitigated by formally auditing the dataset for sufficient overlap and by relying on a consensus of multiple OPE methods (SNIPS, DR, FQE).
  **Reward Shaping Encodes Subjective Preferences**   The choice of the reward function, particularly the weight λ, encodes a subjective preference for the trade-off between hypotension and vasopressor use. This will be addressed by conducting a sensitivity analysis, sweeping the reward weight parameter λ to understand its impact on the final policy.

### **9.0 Dissemination and Future Deployment Path**

The long-term vision of this research extends beyond retrospective
analysis to a tangible impact on clinical care. Should the learned
policy successfully pass all acceptance criteria, a phased deployment
pathway is proposed to translate these findings safely and effectively
into the clinical setting.

1.  **Phase 1: Silent Mode:** The model will be deployed in a
    > prospective, non-interventional \"silent mode.\" It will receive
    > real-time patient data and generate recommendations, which will be
    > logged but not shown to clinicians. This phase will allow for the
    > validation of the model\'s performance on prospective data and a
    > comparison of its recommendations against actual clinician actions
    > and subsequent patient outcomes.

2.  **Phase 2: Guardrailed Suggestions:** The model\'s recommendations
    > will be introduced into the clinical workflow as a
    > decision-support tool. Initially, these suggestions will be
    > guardrailed, appearing only when the model has high confidence in
    > its recommendation or when its suggestion aligns with the likely
    > action of the clinician behavior model.

3.  **Phase 3: Randomized Controlled Trial:** A formal randomized
    > controlled trial (RCT) will be conducted to definitively assess
    > the policy\'s clinical efficacy. This would take the form of an
    > A/B test comparing clinicians who have access to the AI
    > decision-support tool versus those receiving the standard of care.
    > Critically, the clinician will always retain final authority and
    > have the ability to override any AI-generated suggestion.

By adhering to this structured protocol, we provide a robust and
transparent framework for developing an AI-driven vasopressor policy,
laying the groundwork for a rigorous, phased evaluation pathway from
retrospective validation to prospective clinical impact.

### **10.0 References**

1.  Åström, K. J., & Murray, R. M. (2008). *Feedback Systems: An
    > Introduction for Scientists and Engineers*. Princeton University
    > Press.

2.  Brier, G. W. (1950). Verification of forecasts expressed in terms of
    > probability. *Monthly Weather Review*.

3.  Efron, B., & Tibshirani, R. (1994). *An Introduction to the
    > Bootstrap*. Chapman and Hall/CRC.

4.  Fujimoto, S., Meger, D., & Precup, D. (2019). Off-policy deep
    > reinforcement learning without exploration for multi-step tasks.
    > In *Advances in Neural Information Processing Systems*.
    > Batch-Constrained deep Q-learning.

5.  Guo, C., Pleiss, G., Sun, Y., & Weinberger, K. Q. (2017). On
    > calibration of modern neural networks. In *International
    > Conference on Machine Learning*.

6.  Jiang, N., & Li, L. (2016). Doubly robust off-policy value
    > evaluation for reinforcement learning. In *International
    > Conference on Machine Learning*.

7.  Johnson, A. E. W., et al. (2023). MIMIC-IV (version 2.2).
    > *PhysioNet*.

8.  Kostrikov, I., Nair, A., & Levine, S. (2022). Offline reinforcement
    > learning with implicit Q-learning. In *International Conference on
    > Learning Representations*.

9.  Kumar, A., Zhou, A., Tucker, G., & Levine, S. (2020). Conservative
    > Q-learning for offline reinforcement learning. In *Advances in
    > Neural Information Processing Systems*.

10. Le, H. M., Voloshin, C., & Yue, Y. (2019). Batch policy learning
    > under constraints. In *Advances in Neural Information Processing
    > Systems*.

11. Pollard, T. J., Johnson, A. E. W., Raffa, J., et al. (2018). The
    > eICU collaborative research database, a freely available
    > multi-center database for critical care research. *Scientific
    > Data*.

12. Rosenbaum, P. R. (2002). *Observational Studies*. Springer.

13. Swaminathan, A., & Joachims, T. (2015). Counterfactual risk
    > minimization: Learning from logged bandit feedback. In
    > *Proceedings of the 22nd ACM SIGKDD International Conference on
    > Knowledge Discovery and Data Mining*.

---
slug: research-proposal-development-and-validation-of-a-multi-horizon-early-risk-prediction-model-for-type-2-diabetes
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 04-domains/healthcare/healthspan/Research Proposal_ Development and Validation
    of a Multi-Horizon Early-Risk Prediction Model for Type 2 Diabetes.md
  last_synced: '2026-03-20T17:17:18.788234Z'
---

**Research Proposal: Development and Validation of a Multi-Horizon Early-Risk Prediction Model for Type 2 Diabetes**
====================================================================================================================

### **1.0 Introduction and Rationale**

The early identification of individuals at high risk for developing Type
2 Diabetes (T2D) remains a significant clinical challenge. Proactive
risk stratification offers the potential to target preventive
interventions, yet traditional methods often lack the temporal
granularity to capture dynamic changes in a patient\'s risk profile. The
widespread availability of longitudinal Electronic Health Record (EHR)
data presents a powerful opportunity to develop sophisticated predictive
models that can learn from routine clinical encounters over time,
enabling a more proactive and personalized approach to care.

The core purpose of this research is to develop and rigorously validate
a multi-horizon T2D risk prediction model capable of forecasting the
onset of the disease at 1, 3, and 5-year intervals. By leveraging only
routine, structured EHR data, the proposed model is designed for
scalability and seamless integration into existing clinical data
ecosystems.

This project places a strong emphasis on the key desiderata for modern
clinical machine learning models. Beyond predictive accuracy, our
protocol is designed to ensure robust model calibration, demonstrated
decision-analytic utility, fairness to established baseline models, and
an unwavering commitment to scientific reproducibility. This principled
approach is essential for building trust and facilitating the
responsible translation of predictive analytics from research into
clinical practice.

To achieve these goals, this proposal outlines the specific, measurable
objectives that will guide the development, validation, and
comprehensive evaluation of the proposed model.

### **2.0 Research Aims and Objectives**

To ensure a focused and rigorous investigation, this project is guided
by a set of clear, quantifiable objectives. This section outlines the
primary and secondary aims of the study, along with the precise success
criteria that will be used to determine the project\'s outcome.

**Primary Aim** The primary aim of this project is to develop and
validate a model that accurately predicts incident Type 2 Diabetes at a
**3-year horizon**. The primary evaluation metric for this aim will be
the **Area Under the Receiver Operating Characteristic Curve (AUROC)**.

**Secondary Aims** In addition to the primary objective, this study will
pursue the following secondary aims:

-   Evaluate the model\'s predictive performance at **1-year and 5-year
    > horizons** using AUROC.

-   Assess model performance using a comprehensive suite of
    > supplementary metrics, including the **Area Under the
    > Precision-Recall Curve (AUPRC)**, **Expected Calibration Error
    > (ECE)**, and the **Brier score**.

-   Quantify the model\'s potential clinical utility through
    > **decision-curve net benefit analysis**.

**Project Success Criteria** The project will be formally considered
successful if the proposed model meets the following two criteria on the
held-out test set for the primary 3-year prediction horizon:

1.  Achieves a minimum performance gain of **ΔAUROC of ≥ 0.02** versus a
    > powerful XGBoost baseline model.

2.  Demonstrates excellent calibration with a maximum **Expected
    > Calibration Error (ECE) of ≤ 0.03**.

These defined objectives and success criteria provide a clear pathway
for the detailed methodology that will be employed to develop and
evaluate the model.

### **3.0 Methodology**

This section provides a detailed blueprint for the study, outlining the
complete methodology from cohort definition and data processing to model
development and training protocols. Each step is designed to ensure a
transparent, rigorous, and reproducible investigation.

#### **3.1 Study Population and Cohort Design**

The study cohort will be constructed from a de-identified EHR database,
adhering to the following criteria:

-   **Inclusion Criteria:** The target cohort will include all adult
    > patients aged 18--90 who have a history of at least three clinical
    > encounters and a minimum of 12 months of clinical data available
    > prior to their index date (t0).

-   **Exclusion Criteria:** Any patient with prior evidence of Type 2
    > Diabetes before the index date will be excluded from the cohort.

-   **Cohort Construction and Data Splitting:** We will target a final
    > sample size of N ≥ 10,000 with an event rate of ≥ 10%. If the
    > natural event rate is lower, class-balanced sampling will be
    > employed during training. The cohort will be split at the person
    > level into training (70%), validation (15%), and testing (15%)
    > sets, ensuring strict temporal separation to prevent data leakage.

-   **External Validation:** If a dataset from a second institution is
    > available, it will be used for external validation. In its
    > absence, a strict temporal external test set will be constructed
    > using the most recent 12 months of data from the primary site to
    > assess model performance on the most contemporary patient
    > population.

#### **3.2 Outcome Endpoint Definition**

The primary outcome is the first occurrence of incident Type 2 Diabetes,
which will be scored independently for each prediction horizon (H = {1,
3, 5} years) following the index date. A patient will be defined as a
positive T2D case upon the first documentation of any of the following
criteria:

1.  An ICD-10 diagnosis code of E11.\* recorded on at least two
    > different dates.

2.  An HbA1c measurement of ≥6.5% that is subsequently confirmed on a
    > separate date.

3.  A new prescription for a non-insulin antihyperglycemic agent.

#### **3.3 Data Sources and Feature Engineering**

The model will be developed using only structured EHR data extracted
from the 24-month observation period preceding each patient\'s index
date.

The following categories of features will be extracted:

-   **Demographics**

-   **Vitals**

-   **Laboratory Results:** HbA1c, fasting glucose, lipid panel,
    > ALT/AST, creatinine/eGFR, CRP, CBC.

-   **Medications:** Antihypertensives, statins, steroids, atypical
    > antipsychotics.

-   **Utilisation Features**

Key preprocessing steps will include: binning all time-series data into
monthly intervals; standardizing continuous features on a per-site basis
using statistics derived only from the training set; clipping extreme
values at the 0.5th and 99.5th percentiles to reduce the impact of
outliers; and encoding medication data as monthly exposure counts. To
handle missing data, binary flags indicating the absence of a
measurement will be included as features, and forward-filling of values
will be limited to a maximum of 90 days.

#### **3.4 Comparative Baseline Models**

To provide a rigorous and multi-faceted performance benchmark, the
proposed model will be evaluated against a gauntlet of four baseline
models of increasing complexity. This strategy ensures that any claims
of superior performance are robustly tested against diverse and powerful
alternatives. The baselines are:

1.  **L2-Regularized Logistic Regression:** A standard, interpretable
    > statistical model trained on engineered features (last value,
    > mean, and slope over the prior 6, 12, and 24 months). This
    > represents a strong conventional statistical baseline.

2.  **XGBoost:** A high-performance gradient tree-boosting model trained
    > on the same engineered features. This model represents the
    > conventional state-of-the-art for tabular machine learning and
    > serves as the primary benchmark for the project\'s success
    > criteria.

3.  **Feature-Hashing Logistic Regression:** A model designed to
    > efficiently handle high-cardinality, sparse event codes (e.g., all
    > diagnosis and procedure codes) without explicit feature
    > engineering, using 2\^i buckets where i ∈ {12, 13, 14}. This tests
    > the value of leveraging raw event data.

4.  **Simple Clinician Rule (Positive Control):** A heuristic model that
    > serves as a non-inferiority bar rooted in current clinical
    > practice, assigning a risk of 1 if the last HbA1c \> 6.0% or
    > fasting glucose ≥ 110 mg/dL, and 0 otherwise.

#### **3.5 Proposed Multi-Horizon Predictive Model**

The proposed model is a sequence classifier built upon a **Transformer
encoder architecture**. This design is specifically chosen because the
slow-burn progression of T2D involves complex, long-range dependencies
in a patient\'s clinical trajectory; the Transformer\'s self-attention
mechanism is hypothesized to be superior at capturing these temporal
patterns compared to conventional models.

-   **Core Architecture:** The model processes sequences of monthly data
    > slices (xi,t) from each patient\'s 24-month history. The input
    > embedding process (zi,t = Wxi,t + b + et) combines learned feature
    > embeddings with learnable positional vectors (et) to encode the
    > temporal order of clinical events. The model\'s backbone will be a
    > 2-4 layer Transformer encoder, which utilizes a masking mechanism
    > to properly handle missing months. The final patient
    > representation (hi = Pool({z′i,t})) is generated via a pooling
    > operation over the encoder\'s output sequence.

-   **Multi-Horizon Training Strategy:** A single, shared Transformer
    > encoder will learn a rich representation of the patient\'s
    > history. This shared representation will then be fed into
    > horizon-specific prediction heads. To inform the model of the
    > prediction window, a special \"horizon token\" (eH) will be added
    > to each input timestep. This allows for efficient, simultaneous
    > training of the 1, 3, and 5-year risk predictors.

-   **\"Fairness to Baselines\" Design Principle:** To ensure a
    > scientifically rigorous comparison, summary features (last value,
    > mean, and slope) identical to those used by the XGBoost baseline
    > will be appended to the Transformer\'s sequence representation
    > just before the final prediction heads. This principle ensures
    > that any performance gain is attributable to the model\'s superior
    > temporal processing capabilities, not merely its access to a
    > different feature set.

-   **Model Ablations:** To investigate the sources of model
    > performance, a series of ablation studies will be conducted. These
    > include: replacing the Transformer encoder with a Gated Recurrent
    > Unit (GRU), removing the time embeddings, conducting systematic
    > sweeps of network depth and hidden-size, and implementing a
    > prime-hashing variant for mapping high-cardinality IDs.

#### **3.6 Model Training and Calibration Protocol**

The model will be trained and optimized using a carefully designed
protocol to ensure stability and reliability.

-   **Model Optimization:** The overall loss function is a weighted sum
    > of the per-horizon losses (L = ∑H αH BCEH), where weights (αH) are
    > inversely proportional to the outcome prevalence for each horizon
    > (αH ∝ 1/prevalenceH). This approach, combined with class weights
    > within each binary cross-entropy calculation, addresses class
    > imbalance. A sensitivity analysis will be performed using a focal
    > loss function. The AdamW optimizer will be used with a learning
    > rate selected from the range {1e-4, 3e-4}.

-   **Regularization and Stopping Criteria:** To prevent overfitting,
    > dropout (in the range of 0.1--0.3) and weight decay (10⁻⁵) will be
    > applied. Training will be governed by an early stopping protocol
    > with a patience of 10 epochs, monitoring the validation set AUROC
    > for the primary H=3 year horizon.

-   **Post-Training Calibration:** After training is complete, the
    > model\'s raw predictions will be calibrated on the held-out
    > validation set. Either Platt scaling or isotonic regression will
    > be used to transform the model\'s scores into reliable,
    > well-calibrated risk probabilities.

This comprehensive methodology provides a robust foundation for
developing the predictive model, leading into the equally rigorous
framework for its evaluation.

### **4.0 Comprehensive Evaluation Framework**

A successful clinical prediction model must be more than statistically
accurate; it must also be clinically relevant, robust, and trustworthy.
Therefore, this project employs a multi-faceted evaluation framework
designed to assess the model\'s performance from statistical, clinical,
and operational perspectives. All evaluations will be performed a single
time on the held-out test set.

#### **4.1 Statistical Performance Evaluation**

The model\'s core predictive accuracy and reliability will be quantified
using the following statistical metrics:

-   **AUROC and AUPRC:** Both metrics will be reported with
    > 1,000-replicate bootstrap confidence intervals to provide a robust
    > estimate of performance and uncertainty.

-   **Expected Calibration Error (ECE):** ECE will be calculated with 10
    > probability bins to measure the alignment between predicted risks
    > and observed outcomes. A corresponding calibration plot will be
    > generated for visual inspection.

-   **Brier Score:** This metric will be used to measure the model\'s
    > overall accuracy, incorporating both discrimination and
    > calibration.

Statistical comparisons between the proposed model and baselines will be
conducted using the **DeLong test** for differences in AUROC and
**McNemar's test** for comparing performance at a specific operating
threshold.

#### **4.2 Clinical Utility and Decision Analysis**

To assess the model\'s practical utility in a clinical setting, the
following analyses will be performed:

-   **Decision-Curve Analysis:** This analysis will be used to evaluate
    > the standard and standardised net benefit of using the model to
    > guide clinical decisions across a range of clinically relevant
    > risk thresholds (1--20%).

-   **Number Needed to Screen (NNS):** We will calculate the NNS to
    > quantify the clinical effort (i.e., the number of patients that
    > need to be screened) required to identify one true T2D case at a
    > given risk threshold.

-   **Lead-Time Analysis:** This analysis will estimate the potential
    > gain in early detection time afforded by the model compared to the
    > time of diagnosis under standard care.

-   **Risk Persistence Rule:** We will evaluate a more robust
    > \"high-risk\" flagging rule, a direct attempt to improve Positive
    > Predictive Value (PPV) and reduce alert fatigue in a real-world
    > setting. An alert is only triggered if a patient\'s predicted risk
    > is ≥ τ at two or more encounters within a 6-month period. The
    > impact of this rule on the PPV and sensitivity will be reported.

-   **Subgroup Performance:** We will report the model\'s PPV in
    > predefined high-risk subgroups.

#### **4.3 Model Robustness, Fairness, and Interpretability**

Ensuring the model is robust, fair, and understandable is critical for
responsible implementation.

-   **Robustness and Fairness:** Model performance will be evaluated
    > across key demographic subgroups, including sex, pre-defined age
    > bands, and race/ethnicity. Temporal robustness will be assessed by
    > training the model on all data up to a specific cutoff date
    > \[−T, 0) and evaluating its performance on a held-out test set
    > comprising only the most recent 12 months of data (0, T′\].

-   **Model Interpretability:** We will employ two state-of-the-art
    > methods to interpret the predictions of the best-performing
    > models:

    -   **SHAP (SHapley Additive exPlanations)** for the XGBoost
        > baseline.

    -   **Integrated Gradients** for the Transformer-based sequence
        > model.

-   **Error Analysis:** A qualitative error analysis will be conducted
    > via manual chart review of at least 50 high-confidence false
    > positive and 50 high-confidence false negative predictions. The
    > goal is to categorize the primary sources of error (e.g., label
    > noise, data gaps, atypical physiology) and use these insights to
    > inform potential future model improvements.

This comprehensive evaluation framework transitions into the final
component of the proposal: the governance and dissemination standards
that will underpin the entire project.

### **5.0 Project Governance and Dissemination**

This project is committed to the highest standards of scientific rigor,
transparency, and responsible model lifecycle management. These
principles are essential for building a trustworthy clinical tool and
are embedded in the project\'s governance structure.

#### **5.1 Reproducibility and Open Science Commitments**

To ensure the study\'s findings are transparent and reproducible, we
will adhere to the following open science practices:

-   Pre-registration of the complete study protocol before analysis
    > begins.

-   Use of containerised training environments with deterministic seeds
    > to ensure computational reproducibility.

-   Full release of all non-proprietary source code, model configuration
    > files, and a comprehensive feature dictionary.

-   Publication of a formal model card detailing the model\'s intended
    > use, performance characteristics, and limitations.

-   Maintenance of a versioned data processing lineage to track all data
    > transformations.

Regarding data governance, all Patient Health Information (PHI) will
remain securely within the source institution\'s environment at all
times. Any potential multi-site training will be conducted using a
federated aggregation approach, where only aggregated, non-identifiable
model updates are shared.

#### **5.2 Risk Management and Monitoring Plan**

A proactive risk management plan is in place to address potential
challenges during the model\'s lifecycle.

  Risk                                Mitigation Strategy
  ----------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Model Performance Degradation**   Implement specific recalibration/rollback triggers: ECE \> 0.05 or AUROC drop ≥ 0.03 for two consecutive quarters; a significant Spiegelhalter\'s z-test (p \< 0.01); or Population Stability Index (PSI) \> 0.2 on any top-10 feature. Actions include recalibration, retraining, and rollback.
  **Label Noise**                     Utilize confirmatory rules for endpoint definition (e.g., requiring two diagnostic codes). Perform a sensitivity analysis by removing diagnoses based only on prescription data.
  **Selection Bias**                  Generate a detailed cohort selection flow diagram (STROBE/CONSORT style). Compare the demographic and clinical characteristics of the included versus excluded populations to identify potential biases.
  **Overfitting**                     Rigorously compare against strong baseline models. Perform model ablations to understand component contributions. Use early stopping on a dedicated validation set to prevent over-optimization.
  **Data Quality Issues**             Implement automated data quality checks, including plausibility checks on variable ranges and systematic unit harmonisation across data sources.

#### **5.3 Project Acceptance Criteria and Dissemination Plan**

The transition from the research phase to any subsequent implementation
study is contingent upon meeting a set of formal acceptance gates. The
project will proceed only if all three of the following criteria are
met:

1.  For the primary H=3 year horizon, the final model must achieve a
    > **ΔAUROC ≥ 0.02** versus the XGBoost baseline, maintain an **ECE ≤
    > 0.03**, and demonstrate positive net benefit via decision-curve
    > analysis at a clinically meaningful threshold.

2.  The H=1 and H=5 year models must demonstrate robust performance,
    > with any degradation from the primary model being deemed not
    > clinically material. Models failing this test will be explicitly
    > reported as negative results for their respective horizons.

3.  Under the risk persistence rule, the model must demonstrate a clear
    > improvement in PPV with **≤ 25% relative loss in sensitivity**
    > compared to a single-encounter alerting rule.

If these criteria are not met, the project will be stopped, and a
manuscript detailing the negative result will be prepared for
publication to contribute to the scientific literature. This rigorous,
pre-specified structure ensures that only models with demonstrated
clinical potential proceed.

### **6.0 Potential Clinical Impact and Future Directions**

A successful model from this research could have a substantial clinical
impact. An accurate, well-calibrated, and interpretable T2D risk score,
integrated into clinical workflows, could empower clinicians to move
from reactive to proactive care. Such a tool would enable the targeted
deployment of preventive interventions---such as lifestyle counseling,
metformin therapy, or increased screening frequency---to individuals at
the highest risk. By increasing the lead time for diagnosis, this model
has the potential to delay or prevent the onset of T2D and its
associated complications, ultimately improving patient outcomes and
reducing healthcare costs.

Upon successful completion of this project, future directions would
include prospective validation in a silent, real-world clinical setting,
followed by formal implementation studies to assess the impact of the
model on clinical decision-making and patient outcomes. Furthermore, the
multi-horizon, sequence-based modeling framework developed here could be
adapted to predict the risk of other chronic diseases, providing a
scalable platform for proactive health management.

### **7.0 References**

Brier, G. W. (1950). Verification of forecasts expressed in terms of
probability. *Monthly Weather Review*, 78(1), 1--3.

Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting
system. In *KDD*.

DeLong, E. R., DeLong, D. M., & Clarke-Pearson, D. L. (1988). Comparing
the areas under two or more correlated ROC curves: A nonparametric
approach. *Biometrics*, 837--845.

Efron, B. (1979). Bootstrap methods: Another look at the jackknife.
*Annals of Statistics*, 7(1), 1--26.

Kairouz, P., et al. (2021). Advances and Open Problems in Federated
Learning. *Foundations and Trends in Machine Learning*, 14(1-2), 1--210.

Lin, T.-Y., Goyal, P., Girshick, R., He, K., & Dollár, P. (2017). Focal
Loss for Dense Object Detection. In *ICCV*.

Loshchilov, I., & Hutter, F. (2019). Decoupled weight decay
regularization. In *ICLR*.

Lundberg, S. M., & Lee, S.-I. (2017). A Unified Approach to Interpreting
Model Predictions. In *NIPS*.

McNemar, Q. (1947). Note on the sampling error of the difference between
correlated proportions or percentages. *Psychometrika*, 12(2), 153--157.

Platt, J. (1999). Probabilistic outputs for SVMs and comparisons to
regularized likelihood methods. *Advances in Large Margin Classifiers*.

Spiegelhalter, D. J. (1986). Probabilistic prediction in patient
management and clinical trials. *Statistics in Medicine*, 5(5),
421--433.

Sundararajan, M., Taly, A., & Yan, Q. (2017). Axiomatic attribution for
deep networks. In *ICML*.

Vaswani, A., et al. (2017). Attention Is All You Need. In *NIPS*.

Vickers, A. J., & Elkin, E. B. (2006). Decision curve analysis: a novel
method for evaluating prediction models. *Medical Decision Making*,
26(6), 565--574.

Weinberger, K., Dasgupta, A., Langford, J., Smola, A., & Attenberg, J.
(2009). Feature Hashing for Large Scale Multitask Learning. In *ICML*.

Zadrozny, B., & Elkan, C. (2002). Transforming classifier scores into
accurate multiclass probability estimates. In *KDD*.

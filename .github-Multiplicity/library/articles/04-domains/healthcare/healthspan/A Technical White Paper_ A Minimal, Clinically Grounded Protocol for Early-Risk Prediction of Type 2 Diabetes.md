---
slug: a-technical-white-paper-a-minimal-clinically-grounded-protocol-for-early-risk-prediction-of-type-2-diabetes
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 04-domains/healthcare/healthspan/A Technical White Paper_ A Minimal, Clinically
    Grounded Protocol for Early-Risk Prediction of Type 2 Diabetes.md
  last_synced: '2026-03-20T17:17:18.803006Z'
---

**A Technical White Paper: A Minimal, Clinically Grounded Protocol for Early-Risk Prediction of Type 2 Diabetes**
=================================================================================================================

### **Introduction**

The early prediction of incident type 2 diabetes (T2D) represents a
significant opportunity to enable preventive care and improve patient
outcomes, yet developing robust and trustworthy clinical AI models
remains a complex challenge. This document specifies a pragmatic,
rigorous, and reproducible protocol for developing such a prediction
model using routine Electronic Health Record (EHR) data. Its purpose is
to provide a clear blueprint that guides researchers and developers from
task definition through to responsible deployment.

The core tenets of this protocol emphasize a multi-faceted approach to
model development and evaluation. It prioritizes robust calibration to
ensure that predicted risks are reliable and clinically actionable. It
measures success not just by statistical performance but by
decision-analytic utility, assessing whether the model provides tangible
benefit in a clinical context. Crucially, the protocol mandates fairness
to strong, well-established baseline models to guarantee that any added
complexity provides a meaningful improvement. Finally, it incorporates
clear, pre-defined acceptance gates that serve as a final checkpoint,
preventing the deployment of models that fail to demonstrate a
clinically significant advantage and ensuring a commitment to
responsible innovation.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

**1.0 Prediction Task: Objective and Endpoint Definition**
----------------------------------------------------------

A precisely defined and clinically meaningful prediction target is the
foundation of any successful clinical AI project. This clarity ensures
that the resulting model is aligned with a real-world healthcare need
and that its performance can be measured against objective, relevant
criteria. This section specifies the primary prediction goal, the full
suite of metrics for evaluation, the criteria for success, and the exact
clinical definition of the T2D endpoint.

The primary objective is to predict incident T2D at multiple time
horizons: **H={1, 3, 5} years**. The primary performance metric for
model selection and success evaluation is the **Area Under the Receiver
Operating Characteristic Curve (AUROC) at the H=3 year horizon**.

### **1.1 Key Performance Metrics**

A comprehensive evaluation requires a suite of metrics that assess
different aspects of model performance, from discrimination to
calibration and clinical utility.

-   **Primary Metric:** AUROC at H=3y measures the model\'s ability to
    > discriminate between patients who will and will not develop T2D
    > within three years.

-   **Secondary Metrics:**

    -   **AUROC at H=1y and H=5y:** Provides a complete picture of
        > discrimination at different clinical horizons.

    -   **Area Under the Precision-Recall Curve (AUPRC):** Particularly
        > informative for tasks with class imbalance, which is common in
        > clinical prediction, as it focuses on the performance on the
        > positive (event) class.

    -   **Expected Calibration Error (ECE) and Brier Score:** These
        > metrics are chosen to penalize models that are confidently
        > wrong---a critical safety feature---by measuring the
        > discrepancy between predicted probabilities and observed
        > outcomes.

-   **Decision Utility Metric:** Decision-curve net benefit assesses the
    > model\'s clinical value across a range of risk thresholds,
    > translating statistical performance into a measure of potential
    > clinical impact.

### **1.2 Success Criteria**

For the project to be considered successful, the proposed model must
meet two primary conditions: it must achieve a **∆AUROC of ≥ 0.02**
versus the XGBoost baseline and demonstrate excellent calibration with
an **ECE ≤ 0.03** on the held-out test set.

### **1.3 Clinical Endpoint Definition**

The binary outcome for T2D is defined as the first occurrence of any of
the following criteria within the specified prediction horizon. The
\"index date\" (t0) for prediction is the last encounter in the
patient\'s observation window. A key exclusion criterion is the presence
of any evidence of T2D prior to this index date.

1.  An ICD-10 code for T2D (E11.\*) is recorded on at least two
    > different dates.

2.  A laboratory result shows an HbA1c level of ≥6.5%, which is
    > **confirmed on a separate date**.

3.  A new prescription is issued for a non-insulin antihyperglycemic
    > medication.

Having established *what* will be predicted, the following section
details *who* will be included in the study cohort and the methodology
for model development.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

**2.0 Methodology: From Cohort Selection to Model Training**
------------------------------------------------------------

A rigorous and transparent methodology is essential for building
reproducible and reliable clinical models. This section outlines the
complete development pipeline, beginning with the criteria for defining
the patient cohort and processing the source data, and concluding with
the architecture of the proposed sequence model and its associated
training protocol.

### **2.1 Study Cohort and Data**

#### **Cohort Inclusion Criteria**

Patients are included in the study cohort if they meet the following
criteria:

-   **Age:** Between 18 and 90 years old.

-   **Encounter History:** A minimum of three (≥3) encounters recorded
    > in the EHR.

-   **Observation History:** At least twelve (≥12) months of available
    > history prior to the index date (t0).

#### **Cohort Size and Sampling**

The target cohort size is a minimum of **N ≥ 10,000** patients with an
event rate of **≥ 10%**. If the natural event rate is lower,
class-balanced sampling may be employed during training to ensure the
model learns effectively from positive cases.

#### **Data Splitting Strategy**

The cohort is split at the person level into **70% training, 15%
validation, and 15% test** sets. This split must enforce temporal
separation to prevent data leakage. For external validation, data from a
second clinical site is required. If a second site is unavailable, a
strict temporal split will be used, with the most recent 12 months of
data serving as the external test set.

#### **Data Sources and Features**

The model will be trained using **structured EHR data only**. The
observation window for feature generation is the **24 months** leading
up to the index date. Features will not be forward-filled beyond 90 days
to avoid unrealistic data imputation. The included data types are:

-   **Demographics:** Age, sex, race/ethnicity.

-   **Vitals:** BMI, systolic/diastolic blood pressure, heart rate.

-   **Labs:** Key analytes such as HbA1c, fasting glucose, lipid panel,
    > ALT/AST, creatinine/eGFR, CRP, and CBC.

-   **Medications:** Classes relevant to T2D risk, including
    > antihypertensives, statins, steroids, and atypical antipsychotics.

-   **Utilisation:** Features derived from encounter patterns.

-   **Missingness Flags:** Binary flags indicating whether a feature was
    > observed or missing in a given time bin.

### **2.2 Preprocessing Steps**

The raw longitudinal data is transformed through a standardized
preprocessing pipeline:

1.  **Temporal Binning:** All time-stamped data is aggregated into
    > monthly bins.

2.  **Standardization:** Features are standardized (z-scored) using
    > statistics (mean and standard deviation) calculated exclusively
    > from the training set on a per-site basis.

3.  **Outlier Clipping:** Feature values are clipped at the **0.5th and
    > 99.5th percentiles** to mitigate the impact of extreme outliers.

4.  **Medication Encoding:** Medication exposures are encoded as monthly
    > counts.

### **2.3 Proposed Model Architecture**

To ensure a rigorous evaluation, the proposed deep learning model is
benchmarked against a set of strong, conventional baselines.

#### **Baseline Models**

1.  **Logistic Regression (L2):** A standard linear model trained on
    > engineered features (last value, mean, and slope calculated over
    > 6, 12, and 24 months).

2.  **XGBoost:** A powerful gradient-boosted tree model trained on the
    > same engineered feature set, representing a high-performance
    > standard.

3.  **Feature-hashing Logistic Regression:** A linear model designed to
    > handle high-dimensional, sparse event data without explicit
    > feature engineering, using a hash function with **2\^i buckets,
    > where i ∈ \\{12, 13, 14\\}**.

4.  **Clinician Rule (Positive Control):** A simple, transparent rule
    > that serves as a clinical positive control, classifying a patient
    > as high-risk if their most recent HbA1c is \>6.0% or their last
    > fasting glucose is ≥110 mg/dL.

#### **Sequence Model Architecture**

The proposed model is a sequence classifier built upon a **2--4 layer
Transformer encoder** architecture, designed to learn complex patterns
directly from the longitudinal data. It consists of an input embedding
layer with learnable positional vectors, the Transformer backbone to
process the sequence of monthly data slices, and a final pooling and
output head to generate risk predictions.

Key architectural features and training strategies are employed to
enhance performance and ensure a fair comparison:

-   **Fairness to Baselines:** To ensure that the Transformer\'s
    > performance gains are attributable to its ability to learn from
    > raw sequences rather than simply superior feature engineering, the
    > same summary features used by the XGBoost baseline are explicitly
    > appended to the sequence representation before the final
    > classification head. This creates an architecturally fair
    > comparison.

-   **Multi-horizon Training:** A single, shared encoder is used to
    > learn a common patient representation. This is fed into
    > horizon-specific output heads, and a horizon-specific token is
    > added to the input embeddings. The overall training loss is a
    > weighted sum of the binary cross-entropy (BCE) loss from each
    > horizon: L = ∑H αH BCEH.

-   **Regularisation:** Standard regularisation techniques are applied
    > to prevent overfitting, including dropout (**0.1--0.3**) and
    > weight decay (**10−5**).

-   **Planned Ablations:** To understand the sources of model
    > performance, several ablation studies are planned: replacing the
    > Transformer with a GRU, **removing time embeddings**, performing a
    > **depth/hidden-size sweep**, and testing a prime-hashing variant
    > for handling high-cardinality features.

### **2.4 Training and Calibration Protocol**

#### **Training Procedure**

The model is trained using a weighted binary cross-entropy loss function
to handle class imbalance, with sensitivity analysis using focal loss.
The **AdamW optimizer** is used with a learning rate selected from the
range of **{1e--4, 3e--4}**. Early stopping is employed, monitoring the
validation set AUROC at the primary H=3y horizon with a patience of 10
epochs to prevent overfitting.

#### **Calibration Method**

Post-training, the model\'s raw output scores are calibrated to produce
accurate probabilities. This is achieved using either **Platt scaling**
or **isotonic regression**, with the calibration model trained
exclusively on the held-out validation set.

#### **Computational Budget**

All model runs, including hyperparameter tuning and ablations, must be
completed within a specified computational budget: **≤1×A100 40GB** or
**≤2×RTX 3090** for a total runtime of **\<24 hours**.

With the model\'s architecture and training regimen established, the
protocol shifts to a comprehensive evaluation framework designed to
rigorously test its performance, utility, and safety before any
consideration of deployment.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

**3.0 Comprehensive Evaluation Framework**
------------------------------------------

A single performance metric is insufficient to determine a model\'s
clinical readiness. This section outlines a multi-faceted evaluation
framework designed to rigorously assess not only predictive accuracy but
also model calibration, clinical utility, robustness to data shifts, and
fairness across demographic subgroups.

### **3.1 Performance and Robustness Assessment**

The model\'s performance and stability are evaluated using a variety of
statistical methods and stress tests, organized in the table below.

  Evaluation Category                Specific Methods and Metrics
  ---------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Statistical Performance**        Report AUROC and AUPRC with 1,000 bootstrap confidence intervals. Report ECE (10 bins) and Brier score. Use the DeLong test for statistical comparison of AUROC differences and McNemar's test for threshold-based comparisons.
  **Calibration**                    Generate a calibration plot and a reliability table to visually and quantitatively assess the agreement between predicted probabilities and observed outcomes.
  **Subgroup Performance**           Evaluate and report performance stratified by key demographic subgroups, including sex, pre-defined age bands, and race/ethnicity, to identify any potential performance disparities.
  **Temporal Robustness**            Evaluate performance degradation by calendar quarter to monitor for concept drift. Conduct a strict temporal test by training on historical data \[−T, 0) and testing on the most recent 12 months (0, T′\].
  **Risk Stability (Persistence)**   Implement and evaluate a \"risk persistence rule\" where a high-risk alert is triggered only if risk ≥ τ at two or more (≥2) encounters within a six-month (≤6) period. Report the resulting change in PPV, sensitivity, and total alert volume compared to a single-encounter rule. An optional stability penalty ablation may be performed by adding a term \`λmean\_t

### **3.2 Clinical Utility and Interpretability**

Beyond statistical metrics, the model must be evaluated for its
practical value and transparency.

#### **Clinical Utility Metrics**

To translate model scores into clinical value, several methods are
employed. The **Number Needed to Screen (NNS)** is calculated at a
chosen risk threshold (τ) to estimate the workload required to identify
one positive case. Lead-time gain versus standard care is estimated to
quantify the potential benefit of earlier detection. Finally,
**decision-curve analysis** is used to calculate the standard and
standardised net benefit, providing a clear picture of the model\'s
utility across a range of clinical preferences.

#### **Interpretability Methods**

To ensure the model\'s predictions are understandable and clinically
plausible, the following interpretability techniques will be used:

-   **SHAP** (SHapley Additive exPlanations) for the XGBoost baseline
    > model.

-   **Integrated Gradients** for the deep learning sequence model.

-   Ranking of the **top-10 contributing features** for the overall
    > population and within key subgroups.

-   Review of feature attributions by a **clinical panel** to assess
    > face-validity.

#### **Error Analysis Protocol**

A manual error analysis will be conducted to understand the model\'s
failure modes. This involves a detailed chart review of **≥50
high-confidence false positives** and **≥50 high-confidence false
negatives**. The goal is to categorize the primary causes of error
(e.g., label noise, data gaps, unusual physiology). The resulting
findings will be used to **publish a taxonomy of errors and remediation
actions**.

This comprehensive evaluation framework provides the evidence base for
the final governance and acceptance decisions that follow.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

**4.0 Governance, Reproducibility, and Acceptance**
---------------------------------------------------

Technical excellence alone is insufficient for deploying AI in a
clinical setting. A robust governance framework, a firm commitment to
reproducibility, and pre-defined acceptance gates are essential for
ensuring that models are safe, reliable, and trustworthy. This section
details the operational standards required for responsible
implementation.

### **4.1 Reproducibility and Governance Standards**

#### **Reproducibility Commitments**

To ensure the results can be independently verified and reproduced, the
following actions are mandatory:

-   **Pre-registration:** The full study protocol will be pre-registered
    > before analysis begins.

-   **Containerised Training:** The training environment will be
    > containerised to ensure dependencies are locked.

-   **Deterministic Execution:** All random seeds will be fixed for
    > deterministic model training.

-   **Code and Configuration Release:** The full source code,
    > configuration files, a feature dictionary, and a model card will
    > be released.

-   **Data Lineage:** The data processing pipeline will be versioned to
    > provide a clear lineage from raw data to model-ready features.

#### **Data Governance**

All patient data, including Protected Health Information (PHI), will
never leave the source clinical site. In multi-site training scenarios,
a **federated aggregation** approach will be used to train a global
model without sharing patient-level data.

### **4.2 Risk Mitigation Plan**

A proactive approach to identifying and mitigating potential risks is
critical for long-term model performance and safety. While this
mitigation plan addresses ongoing operational risks, the following
pre-defined acceptance gate serves as the final, one-time checkpoint. It
translates the project\'s core objectives---superior performance, robust
calibration, and clinical utility---into non-negotiable success
criteria.

  Identified Risk         Mitigation Strategy / Trigger
  ----------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Performance Drift**   **Recalibration/Rollback Triggers:** ECE \> 0.05 for two consecutive quarters; AUROC drop ≥ 0.03 for two consecutive quarters; Spiegelhalter's calibration z test p \< 0.01; or PSI \> 0.2 on any top-10 feature. **Actions:** Recalibrate -\> Retrain -\> Rollback.
  **Label Noise**         Use confirmatory rules for endpoint definition; conduct a sensitivity analysis by removing cases identified only through new prescriptions (Rx-only).
  **Selection Bias**      Generate a study flow diagram (e.g., STROBE); perform a detailed statistical and demographic comparison of the included vs. excluded patient populations.
  **Overfitting**         Benchmark against strong baselines; perform ablation studies to understand sources of performance gain; use early stopping on a held-out validation set.
  **Data Quality**        Implement automated plausibility checks (e.g., for lab values) and unit harmonisation protocols during the data processing phase.

### **4.3 Final Acceptance Gate**

To proceed with deployment or clinical implementation, the model **must
meet all three** of the following conditions on the held-out test set.
If any condition is not met, the project is considered a negative result
and should be published as such to contribute to the scientific
literature.

1.  **H=3y Performance:** The model must demonstrate a statistically
    > significant and clinically meaningful improvement over the XGBoost
    > baseline (**∆AUROC ≥ 0.02**), be well-calibrated (**ECE ≤ 0.03**),
    > and show a positive net benefit via decision-curve analysis at a
    > clinically chosen risk threshold.

2.  **Multi-Horizon Performance:** The model must show no clinically
    > material performance degradation at the **H=1y and H=5y**
    > horizons. If performance is substantially worse at these horizons,
    > they will be reported as negative results.

3.  **Persistence Rule Utility:** Under the risk persistence rule, the
    > model must demonstrate an improved Positive Predictive Value (PPV)
    > with a relative loss in sensitivity of **no more than 25%**
    > compared to the single-encounter alerting rule.

This governance framework bridges the gap between model development and
responsible implementation, leading into the technical details required
for execution.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

**5.0 Technical Appendix: Implementation Blueprint**
----------------------------------------------------

This appendix provides concrete technical artifacts to facilitate the
reproduction and implementation of the described protocol. These code
snippets and templates serve as a blueprint for developers and
researchers.

### **5.1 Repository Structure**

The proposed code repository is organized with a clear and logical
structure to separate data contracts, configurations, source code, and
reports.

healthspan-t2d/

├── data\_contract/

│ └── columns.md

├── sql/

│ └── cohort.sql

├── configs/

│ └── default.yaml

├── src/

│ ├── models/

│ │ └── transformer.py

│ ├── utils/

│ │ └── metrics.py

│ ├── train.py

│ └── eval.py

├── notebooks/

│ └── calibration.ipynb

└── reports/

└── model\_card.md

### **5.2 Configuration File**

The configs/default.yaml file centralizes key hyperparameters for the
model architecture and training process, enabling easy modification and
tracking of experiments.

seed: 13

horizons: \[1,3,5\]

window\_months: 24

batch\_size: 256

lr: 0.0003

dropout: 0.2

weight\_decay: 1e-5

transformer:

layers: 3

d\_model: 128

n\_heads: 4

ff\_mult: 4

loss:

type: bce

alpha\_by\_prevalence: true

early\_stopping:

monitor: auroc\_h3

patience: 10

calibration: isotonic

### **5.3 Key Code Snippets**

The following snippets illustrate core components of the implementation.

This class defines the multi-horizon Transformer model, which uses a
single shared encoder to learn a patient representation and
horizon-specific tokens and output heads to generate predictions for 1,
3, and 5 years.

\# src/models/transformer.py

import torch

import torch.nn as nn

class MHTransformer(nn.Module):

\"\"\"Multi-horizon Transformer with shared encoder and horizon-specific
heads.\"\"\"

def \_\_init\_\_(self, d\_in, d\_model=128, layers=3, n\_heads=4,
horizons=(1,3,5), max\_months=24):

super().\_\_init\_\_()

self.horizons = \[str(h) for h in horizons\]

self.proj = nn.Linear(d\_in, d\_model)

self.pos = nn.Embedding(max\_months + 1, d\_model) \# months + pad

self.horiz = nn.Embedding(8, d\_model) \# horizon token index

enc\_layer = nn.TransformerEncoderLayer(d\_model, n\_heads, d\_model \*
4, batch\_first=True)

self.enc = nn.TransformerEncoder(enc\_layer, layers)

self.heads = nn.ModuleDict({h: nn.Linear(d\_model, 1) for h in
self.horizons})

def forward(self, x, t\_idx, h\_idx, mask=None, return\_logits=True):

\# x: \[B, T, d\_in\], t\_idx: \[B, T\], h\_idx: \[B, T\], mask: \[B,
T\] (True for PAD)

z = self.proj(x) + self.pos(t\_idx) + self.horiz(h\_idx)

z = self.enc(z, src\_key\_padding\_mask=mask)

\# mean pool over valid timesteps

denom = (\~mask).sum(1).clamp\_min(1).unsqueeze(-1)

h = (z.masked\_fill(mask.unsqueeze(-1), 0).sum(1)) / denom

out = {k: self.heads\[k\](h).squeeze(-1) for k in self.heads} \# logits

if return\_logits:

return out

return {k: torch.sigmoid(v) for k, v in out.items()}

This utility file provides simple wrappers for calculating standard
performance metrics.

\# src/utils/metrics.py

from sklearn.metrics import roc\_auc\_score, average\_precision\_score,
brier\_score\_loss

def auroc(y, p):

return roc\_auc\_score(y, p)

def auprc(y, p):

return average\_precision\_score(y, p)

def brier(y, p):

return brier\_score\_loss(y, p)

This sketch outlines the main training loop, highlighting the
calculation of the multi-horizon loss, which is a weighted sum of the
binary cross-entropy from each prediction head, and the application of
class-specific weights to manage data imbalance.

\# src/train.py (sketch)

import torch, torch.nn as nn

from torch.utils.data import DataLoader

\# dataset yields (x, t\_idx, h\_idx, mask, labels\_dict) where
labels\_dict\[\'1\'\],\[\'3\'\],\[\'5\'\]

bce = nn.BCEWithLogitsLoss(reduction=\'none\')

alpha = {1: 0.5, 3: 0.3, 5: 0.2} \# set 1/prevalence then normalize

for epoch in range(max\_epochs):

model.train()

for x, t\_idx, h\_idx, mask, y in DataLoader(train\_ds,
batch\_size=cfg.batch\_size, shuffle=True):

out = model(x, t\_idx, h\_idx, mask, return\_logits=True)

loss = 0.0

for H in (1,3,5):

logits = out\[str(H)\]

target = y\[str(H)\].float()

w = class\_weights\[str(H)\] \# tensor scalar per-H

l = bce(logits, target)

l = (w \* target + (1 - target)) \* l \# pos\_weight-like effect

loss = loss + alpha\[H\] \* l.mean()

opt.zero\_grad(); loss.backward(); opt.step()

### **5.4 SQL and Template Skeletons**

This skeleton SQL query provides a starting point for extracting the
patient cohort and relevant features.

\-- sql/cohort.sql (skeleton)

WITH base AS (

SELECT p.person\_id, v.visit\_date, v.hba1c, v.fpg, v.bmi, v.sbp, v.dbp,
v.hrate,

v.alt, v.ast, v.egfr, v.crp, v.ldl, v.hdl, v.tg,

med.atyp\_antipsych, med.steroids, med.statins,

diag.icd10\_code

FROM visits v

JOIN persons p ON p.person\_id = v.person\_id

LEFT JOIN meds med ON med.person\_id = v.person\_id AND med.visit\_id =
v.visit\_id

LEFT JOIN diags diag ON diag.person\_id = v.person\_id AND
diag.visit\_id = v.visit\_id

),

labels AS (

SELECT person\_id,

MIN(CASE WHEN icd10\_code LIKE \'E11%\' THEN visit\_date END) AS
first\_e11,

MIN(CASE WHEN hba1c \>= 6.5 THEN visit\_date END) AS first\_hba1c,

MIN(CASE WHEN new\_t2d\_rx = 1 THEN visit\_date END) AS first\_rx

FROM base

GROUP BY person\_id

)

SELECT \*

FROM base b

LEFT JOIN labels l USING (person\_id);

This template provides a structured guide for selecting and documenting
the final clinical risk threshold (τ).

τ selection:

\- Clinical prevalence: \_\_

\- FP/FN cost ratio: \_\_

\- Decision-curve net benefit at τ: \_\_

\- Persistence rule effect (PPV ∆, Sensitivity ∆): \_\_

Final τ\*: \_\_ Rationale: \_\_

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

**6.0 Conclusion**
------------------

This document outlines the Healthspan T2D prediction protocol, a
comprehensive and clinically grounded blueprint for developing a
high-quality, early-risk prediction model from EHR data. Its value lies
in its synthesis of best practices across the entire development
lifecycle. By emphasizing methodological rigor, transparent evaluation
against strong baselines, a focus on clinical utility, and the
integration of robust governance and acceptance criteria, this protocol
serves as a best-practice template. It is designed not only to produce a
high-performing model but to ensure that the final product is reliable,
reproducible, and ready for responsible clinical implementation. As a
final and critical step, any potential deployment of a model developed
under this protocol must be preceded by a thorough institutional review
and be subject to ongoing clinical governance.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

**7.0 References**
------------------

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

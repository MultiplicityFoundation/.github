---
slug: standard-operating-procedure-statistical-analysis-and-quality-control-for-multi-analyte-panels
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 04-domains/healthcare/clinical-lab-analytics/Standard Operating Procedure_
    Statistical Analysis and Quality Control for Multi-Analyte Panels.md
  last_synced: '2026-03-20T17:17:18.809051Z'
---

**Standard Operating Procedure: Statistical Analysis and Quality Control for Multi-Analyte Panels**
===================================================================================================

  **SOP Number**       QMS-STAT-001
  -------------------- -------------------------------------------------------------------------------------------------
  **Version**          1.0
  **Title**            Standard Operating Procedure: Statistical Analysis and Quality Control for Multi-Analyte Panels
  **Effective Date**   \[Date\]
  **Author**           \[Author Name, Title\]
  **Approver**         \[Approver Name, Title\]

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

### **1.0 Purpose**

The strategic implementation of a standardized statistical analysis and
quality control framework is fundamental to the analytical and clinical
integrity of laboratory operations. This Standard Operating Procedure
(SOP) is established to ensure the analytical validity of all
multi-analyte testing, mitigate the risk of false-positive results
inherent in high-dimensional data, and maintain full compliance with
regulatory standards.

The primary purpose of this SOP is to establish validated and
transparent procedures for managing data quality, controlling for
statistical multiplicity, monitoring analytical performance via Quality
Control (QC) charting, and executing lot-to-lot validation for new
reagents. Adherence to these procedures is critical for producing
reliable, consistent, and defensible results. This document outlines the
scope of these procedures and the responsibilities of personnel in their
execution.

### **2.0 Scope**

This SOP defines the required procedures governing the statistical
analysis of all multi-analyte panels performed within the laboratory.
Its scope encompasses the initial data quality assessment, the
application of appropriate statistical adjustments for multiple
comparisons, the ongoing monitoring of instrument and assay performance
using QC materials, and the formal validation of new reagent and
calibrator lots prior to their use in production.

This document applies to all laboratory personnel involved in performing
data analysis, reviewing quality control data, certifying results, and
participating in method validation activities. The procedures herein are
mandatory for ensuring the quality and integrity of the laboratory\'s
analytical outputs. The following sections detail the specific roles and
responsibilities required to execute these procedures effectively.

### **3.0 Responsibilities**

A robust quality management system, as required by standards such as ISO
15189, relies on the clear definition of roles and responsibilities.
This ensures accountability, consistency, and a high standard of
operational excellence. All personnel are expected to be familiar with
and adhere to the responsibilities assigned to their role.

-   **Laboratory Personnel:** Responsible for the day-to-day execution
    > of the analytical and quality control procedures outlined in this
    > SOP. This includes the routine monitoring of QC charts for
    > out-of-control signals and the timely escalation of any
    > non-conformances or system-generated warnings to the appropriate
    > supervisory staff.

-   **Quality Assurance Manager:** Responsible for the comprehensive
    > oversight of the quality system. This includes the final review
    > and approval of analytical results, the periodic review of system
    > audit logs to ensure procedural adherence and data integrity, and
    > verifying that all personnel are adequately trained and have
    > demonstrated competency in the procedures relevant to their roles.

-   **Parameter Board:** A designated governance body responsible for
    > the formal pre-approval and configuration control of all
    > statistical parameters used in production. This includes, but is
    > not limited to, the values for EWMA and CUSUM charting (λ, L,
    > k, h) and the significance thresholds for multiplicity control (q,
    > α). This pre-registration of parameters is a critical control to
    > prevent post-hoc adjustments to production data.

Adherence to these defined responsibilities ensures the integrity of the
procedures detailed in the following sections.

### **4.0 Definitions**

-   **Family-Wise Error Rate (FWER):** The probability of making at
    > least one false-positive finding (Type I error) across all
    > hypotheses being tested in a panel.

-   **False Discovery Rate (FDR):** The expected proportion of
    > false-positive findings among all results that are declared
    > statistically significant.

-   **Exponentially Weighted Moving Average (EWMA):** A type of control
    > chart that uses a weighted average of all past and current
    > observations, giving more weight to recent data, making it
    > sensitive to small, sustained shifts in the process mean.

-   **Cumulative Sum (CUSUM):** A type of control chart that plots the
    > cumulative sum of deviations from a target value, making it
    > effective for detecting small, persistent shifts in the process
    > mean.

-   **Two One-Sided Tests (TOST):** A statistical procedure used to
    > demonstrate equivalence between two groups (e.g., reagent lots).
    > It tests the hypothesis that the difference between the groups is
    > not meaningfully large in either direction.

-   **Equivalence Margin (δ):** A pre-defined, clinically acceptable
    > range of difference. In TOST, equivalence is demonstrated if the
    > confidence interval for the mean difference falls entirely within
    > this margin (-δ to +δ).

### **5.0 Procedure: Data and Quality Control Analysis**

This section details the required, sequential steps for all analytical
data processing and quality control. The procedures described below must
be followed in order to progress from raw instrument output to final,
certified results.

#### **5.1 Mandatory Data Quality Gates**

Robust, automated data quality checks serve as the first line of defense
against erroneous results and are a prerequisite for any subsequent
statistical analysis. All data streams must pass these automated checks
before being accepted for processing. Data that fails a \"Block\"
condition must be quarantined pending investigation.

1.  **Missingness Assessment:** The system will calculate the rate of
    > missing data points on both a per-analyte and a per-run basis.

    -   **Action:** Issue a Warn notification if the missingness rate is
        > between 2% and 4%.

    -   **Action:** Block the run from further processing if the
        > missingness rate is greater than 5%, unless a pre-configured
        > missing-at-random (MAR) handling protocol is in place. Data
        > failing **Little\'s MCAR test** must be escalated for manual
        > review.

2.  **Analyte Range Checks:** All results will be checked against the
    > established Analytic Measurement Range (AMR) for the respective
    > assay.

    -   **Action:** Soft-flag any value that falls within 5% of the
        > lower or upper bounds of the AMR for review.

3.  **Data Stream Integrity:** Data integrity is verified for
    > uniqueness, units, and temporal sequence.

    -   **Action:** The system must identify and reject duplicate
        > records based on the composite key of sample + analyte +
        > timestamp.

    -   **Action:** The system must verify that all unit codes within a
        > data set are correct and consistent. Mixed units will be
        > rejected.

    -   **Action:** For all time-series data (e.g., QC), the system must
        > enforce non-decreasing timestamps.

4.  **Time Series Plausibility Checks:** For control material data, the
    > system must forbid impossible jumps in values between consecutive
    > data points, based on pre-configured instrument specifications.

5.  **Instrument Flag Integration:** Error codes generated by the
    > analytical instrument\'s software must be ingested and acted upon.

    -   **Action:** Any critical error flags reported by the
        > manufacturer\'s software must automatically halt any
        > corresponding QC data updates until the error is resolved.

6.  **Data Immutability:** The system must enforce a policy of
    > non-destructive data editing to ensure full traceability.

    -   **Action:** All raw, cleaned, and derived data fields must be
        > retained. No destructive edits are permitted. All actions
        > performed on the data must be recorded in a permanent audit
        > log.

Once analytical data has successfully passed these quality gates, it may
proceed to statistical significance testing.

#### **5.2 Multiplicity Control for Panel-Level Inference**

When multiple analytes are tested simultaneously as part of a panel, the
probability of observing at least one false-positive result increases
significantly. This phenomenon, known as multiplicity, must be
statistically controlled to ensure the validity of panel-level
conclusions.

The following methods are approved for controlling statistical error
rates in multi-analyte panels:

-   **For Exploratory/Screening Panels:** The **Benjamini-Hochberg
    > (BH)** procedure shall be used. This method controls the False
    > Discovery Rate (FDR), which is the expected proportion of false
    > positives among all significant results. The target FDR is **q =
    > 0.05**.

-   **For Confirmatory Panels/Reflex Rules:** The **Holm** procedure
    > shall be used. This method controls the Family-Wise Error Rate
    > (FWER), which is the probability of making one or more
    > false-positive claims across the entire panel. The target FWER is
    > **α = 0.05**.

Laboratory personnel shall follow this procedure for all panel-level
analyses:

1.  **Confirm Method Selection:** Before initiating the analysis, verify
    > that the system is configured with the correct error control
    > method (Holm or BH) and its corresponding pre-registered
    > significance threshold (α or q) for the specific panel being
    > evaluated.

2.  **Execute Analysis:** Initiate the system analysis. The software
    > will automatically process the raw p-values from each analyte in
    > the panel and generate adjusted p-values according to the selected
    > method.

3.  **Review System Output:** Carefully examine the system-generated
    > report. The report must clearly state the number of analytes
    > tested (m), the multiplicity control method used, the raw
    > p-values, the adjusted p-values, and the final list of analytes
    > considered statistically significant (i.e., rejected null
    > hypotheses).

4.  **Apply Clinical Interpretation:** Clinical interpretation, reflex
    > testing decisions, and any subsequent actions must *only* be based
    > on the set of results identified as significant *after* the
    > multiplicity adjustment has been applied.

5.  **Certify and Record:** Certify the final panel results. This action
    > must be automatically recorded in the audit log, capturing the
    > final decision, the exact timestamp, and the operator\'s User ID.

Following panel-level inference, the ongoing stability of the analytical
process is monitored using QC charts.

#### **5.3 Ongoing Quality Control (QC) Charting and Monitoring**

Quality Control (QC) charts are essential tools for monitoring the
stability and precision of an analytical process over time. The timely
detection of shifts, trends, or increased variability is critical for
maintaining high-quality results and preventing the release of erroneous
patient data.

The following univariate QC charting methods are approved for use:

-   **Shewhart Charts:** These charts are used to detect large shifts in
    > the process mean. Control limits are established at the process
    > mean (µ) ± 3 standard deviations (3σ). Specific violation rules
    > (e.g., Westgard rules) must be pre-registered in the system for
    > automated flagging.

-   **Exponentially Weighted Moving Average (EWMA) Charts:** This method
    > is highly effective for detecting small, persistent shifts in the
    > process mean. Control limits are calculated based on the
    > pre-approved weighting parameter λ and the limit multiplier L.

-   **Cumulative Sum (CUSUM) Charts:** This method is also used to
    > detect small, sustained shifts. This method operates by
    > accumulating deviations from a target mean, incorporating an
    > allowance parameter (k). A process is flagged as out-of-control if
    > the cumulative sum exceeds the pre-approved control limit (h).

##### **Multivariate QC**

For panels containing clinically or analytically correlated analytes,
multivariate QC methods such as **Hotelling\'s T²** or **Multivariate
EWMA (MEWMA)** will be employed to monitor the process as a whole. Even
when a multivariate chart is in use, the corresponding univariate charts
for each individual analyte must be maintained and monitored. This is
essential for correctly interpreting an out-of-control signal from the
multivariate chart and identifying the specific analyte(s) responsible
for the deviation.

The next section details the procedure for validating new lots of
reagents and calibrators.

#### **5.4 Reagent Lot-to-Lot Validation**

Lot-to-lot validation is a critical procedure performed to ensure that a
new lot of reagents or calibrators performs in a manner statistically
equivalent to the current in-use lot. This process prevents abrupt
shifts or drifts in patient results that could arise from manufacturing
variability between lots.

The validation study must adhere to the following design:

1.  **Sample Selection:** A minimum of 20 unique patient samples must be
    > selected for the study. These samples should be chosen to span the
    > clinically relevant analytical measurement range of the assay.

2.  **Testing Protocol:** Each of the selected patient samples must be
    > tested using both the current, in-use lot (Lot A) and the new
    > candidate lot (Lot B). The testing should be performed in a paired
    > or bridged fashion to minimize temporal variation. As part of the
    > analysis, regression with intercept and slope must be evaluated in
    > addition to the formal equivalence test.

The statistical acceptance criteria for the new lot are as follows:

-   The primary acceptance decision will be based on the **Two One-Sided
    > Tests (TOST) for equivalence**.

-   The objective of the TOST procedure is to provide statistical
    > evidence that the new lot is equivalent to the old lot, not just
    > that it is not different. This is achieved by confirming that the
    > 90% confidence interval for the mean difference between the lots
    > (µB − µA) is contained *entirely* within a pre-defined, clinically
    > acceptable equivalence margin (-δ to +δ).

-   **Passing Condition:** The new lot (Lot B) is formally accepted for
    > clinical use if the TOST procedure yields a p-value ≤ 0.05, which
    > confirms statistical equivalence.

### **6.0 Documentation and Audit Trail**

Complete, accurate, and immutable documentation is a cornerstone of
laboratory quality assurance. A comprehensive audit trail is required
for regulatory compliance (e.g., CLIA, CAP), troubleshooting, and
ensuring full traceability of every result. The system must
automatically log all actions governed by this SOP.

The system\'s audit log must capture the following minimum data points
for every recorded event:

-   Event Timestamp (to the second or finer resolution)

-   User ID of the operator performing the action

-   The specific action or endpoint invoked (e.g., panel\_evaluate,
    > lot\_tost)

-   All parameters used for the analysis (e.g., panel\_id, p\_values,
    > method, q\_or\_alpha)

-   The complete, unabridged result of the action

-   The unique configuration version number that was active at the time
    > of the event

### **7.0 References**

This SOP is based on principles and methods described in the following
scientific literature.

1.  Holm, S. "A simple sequentially rejective multiple test procedure."
    > *Scandinavian Journal of Statistics*, 6(2):65--70, 1979.

2.  Benjamini, Y. and Hochberg, Y. "Controlling the false discovery
    > rate: a practical and powerful approach to multiple testing."
    > *Journal of the Royal Statistical Society: Series B*,
    > 57(1):289--300, 1995.

3.  Benjamini, Y. and Yekutieli, D. "The control of the false discovery
    > rate in multiple testing under dependency." *Annals of
    > Statistics*, 29(4):1165--1188, 2001.

4.  Storey, J. D. "A direct approach to false discovery rates." *Journal
    > of the Royal Statistical Society: Series B*, 64(3):479--498, 2002.

5.  Roberts, S. W. "Control chart tests based on geometric moving
    > averages." *Technometrics*, 1(3):239--250, 1959.

6.  Lucas, J. M. and Saccucci, M. S. "Exponentially weighted moving
    > average control schemes: properties and enhancements."
    > *Technometrics*, 32(1):1--12, 1990.

7.  Page, E. S. "Continuous inspection schemes." *Biometrika*,
    > 41(1/2):100--115, 1954.

8.  Hotelling, H. "Multivariate Quality Control." In *Techniques of
    > Statistical Analysis*, 111--184, McGraw-Hill, 1947.

9.  Lowry, C. A., Woodall, W. H., Champ, C. W., and Rigdon, S. E. "A
    > multivariate exponentially weighted moving average control chart."
    > *Technometrics*, 34(1):46--53, 1992.

10. Ledoit, O. and Wolf, M. "A well-conditioned estimator for
    > large-dimensional covariance matrices." *Journal of Multivariate
    > Analysis*, 88(2):365--411, 2004.

11. Schuirmann, D. J. "A comparison of the two one-sided tests procedure
    > and the power approach for assessing the equivalence of average
    > bioavailability." *Journal of Pharmacokinetics and
    > Biopharmaceutics*, 15(6):657--680, 1987.

12. Little, R. J. A. "A test of Missing Completely at Random for
    > multivariate data with missing values." *Journal of the Royal
    > Statistical Society: Series C (Applied Statistics)*,
    > 37(3):259--268, 1988.

---
slug: cardiovascular-disease
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 04-domains/healthcare/Cardiovascular_Disease.md
  last_synced: '2026-03-20T17:17:18.694132Z'
---

         Cardiovascular Risk Prediction: Clean Mathematical
                  Specification and Validation Plan
                                        Ryan O. van Gelder

                                          Citizen Gardens

                                         October 23, 2025


                                              Abstract
          We specify, justify, and operationalize a reproducible pipeline for predicting major ad-
      verse cardiovascular events (MACE: myocardial infarction, stroke, cardiovascular death) at
      1, 3, and 5 years, with both binary horizons and time-to-event formulations. We include
      cohort definitions, preprocessing, feature engineering from EHR and ECG, model families,
      calibration, evaluation, ablations, governance, and a validation and regulatory plan. Code
      snippets illustrate the training workflow.


1    Objective
Predict incident MACE in primary prevention using EHR and ECG. Outputs: calibrated risk
at fixed horizons and individual survival curves. Decisions are supported by thresholds derived
from explicit utility.


2    Cohorts and Indexing
    • Adults (≥ 18 y). Exclude prevalent CVD at baseline.
    • Derive on Site A. Hold out Site B for external validation.
    • Index date: first ECG with same-day labs and vitals within a ±90-day window.


3    Notation
For patient i and time index t: observations yit ∈ Rp , exogenous inputs uit ∈ Rq , latent state
xit ∈ Rd . Event time T̃i , censoring Ci , observed Ti = min(T̃i , Ci ), indicator ∆i = 1[T̃i ≤ Ci ].


4    Data Preprocessing
    • Units harmonized to SI; winsorize at 0.5% and 99.5% after standardization.
    • Missingness mask mit . Within-encounter forward fill; global-median imputation; record
      indicators. Sensitivity with MICE.
    • Patient-level split: 70/10/20 train/val/test. External Site B held out.
    • z-score normalization using training moments.




                                                   1
5     Feature Engineering
5.1   Demographics, Vitals, Labs, Medications
Age, sex, race/ethnicity; SBP, DBP, HR, BMI, SpO2; LDL-C, HDL-C, TC, TG, HbA1c, fasting
glucose, creatinine/eGFR, hs-CRP; medication exposures (statins, antihypertensives, antidia-
betics, antiplatelets) as binary indicators over 180 days.

5.2   ECG Features and QA
Intervals PR, QRS, QT and QTc (Bazett, Fridericia) [1, 2]. Heart rate, axes, simple HRV metrics
from 10 s strips when feasible. Extraction uses QRS detection (Pan–Tompkins) with wavelet-
based delineation [3]. QA gates: per-lead SNR > 6 dB; at least 8 good leads; morphology
stability. Vendor harmonization maps XML/HL7 fields to a common schema. HRV from short
strips is exploratory and excluded from primary models.

5.3   Temporal Alignment and Recency
Within a ±90-day window around the index ECG, choose nearest measurements. If multiple
values exist, compute a recency-weighted snapshot with weight w = exp(−∆t/30 days), and
include ∆t as a feature. If no value exists in-window, mark missing.


6     Models
6.1   Static Baselines
                                                      (τ )
Logistic Regression at Horizon τ . pi (τ ) = σ(β0 + β (τ )⊤ zi ), with engineered index-time
features zi . Trained with class weighting and elastic net.

Cox Proportional Hazards. h(t | zi ) = h0 (t) exp(β ⊤ zi ). Fit by maximizing partial likeli-
hood [4]. PH assumptions checked via Schoenfeld residuals [5]. Time-varying extensions used
if violated.

6.2   Time-series Models
Linear-Gaussian State Space. Dynamics xi,t+1 = Axit + Buit + wit , observation yit =
Cxit + vit with wit ∼ N (0, Q) and vit ∼ N (0, R). Parameters A, B, C, Q, R estimated by EM
with Kalman smoothing [6]. Filtered states feed a survival head.

Discrete-time Hazard (Dynamic).          For intervals k = 1, . . . , K up to horizon τ :
                                                                    
                             Pr(Ti = k | Hi,k ) = σ αk + g(Hi,k ) ,

where history Hi,k summarizes (yi,1:k , ui,1:k ) via GRU/Transformer or Kalman states.

6.3   Competing Risks
We model cause-specific hazards for MACE and non-CV death and report cumulative incidence
via Aalen–Johansen [7]. We include Fine–Gray subdistribution modeling as a secondary analysis
[8].




                                                2
7     Estimation and Calibration
7.1     Estimation
Logistic models minimize cross-entropy with elastic net. Cox models maximize partial like-
lihood with L2 penalty. State-space learned by EM. Dynamic hazard trained with negative
log-likelihood and early stopping.

7.2     Calibration
Binary horizons use isotonic regression [9] or Platt scaling [10]. Survival models assess calibration-
in-the-large and slope, and use baseline-hazard recalibration when needed.


8     Evaluation
     • Discrimination: AUROC and AUPRC at 1/3/5 years; Harrell’s C for survival [11].
     • Accuracy: Brier and Integrated Brier [12].
     • Calibration: reliability diagrams, expected calibration error, slope/intercept.
     • Clinical utility: decision curve analysis [13]; net reclassification improvement vs baselines.
     • Uncertainty: 1000 bootstrap replicates with patient clustering.


9     Benchmarks
ASCVD Pooled Cohort Equations [14], Framingham 2008 general CVD [15], QRISK3 [16], and
SCORE2 where applicable [17]. Refit or recalibrate to the local cohort.


10      Ablations and Stress Tests
Comparisons: static logistic vs Cox vs dynamic hazard vs state-space; no-ECG vs with-ECG;
labs-only vs labs+vitals vs +meds vs +ECG; imputation methods; regularization types; Kalman
vs GRU vs Transformer summarizers; cross-site and temporal generalization; drift robustness.


11      Decision Thresholds and Utility
Choose thresholds by expected utility using cost matrix {cF P , cF N , cT P , cT N }. Report sensitiv-
ity, specificity, PPV, NPV at chosen operating points.


12      Reproducibility and Governance
Fixed seeds, versioned data, stored splits. Pre-registered metrics and endpoint. Model cards in-
clude intended use, calibration domain, and monitoring plan. Bias audits by sex, race/ethnicity,
and age with equal-calibration checks.


13      Monitoring and Model Updating
Quarterly monitoring. Recalibration triggers: ECE > 0.03 or calibration slope outside [0.9, 1.1].
Annual refit with data through the prior quarter. Rolling predictions at each new encounter;
alert cooldown 30 days.




                                                  3
14      Validation and Regulatory Plan
14.1    ECG Feature Validation
Reference set of ≥ 1000 ECGs across devices and rhythms. Two cardiologists annotate fiducials
and intervals; disagreements adjudicated. Report MAE, bias, ICC, and Bland–Altman limits.
Acceptance: PR/QRS/QT MAE ≤ 8/6/12 ms, QTc MAE ≤ 15 ms.

14.2    QA Failure Rates
Track failure reasons: noise, lead loss, rhythm, vendor parse, short duration. KPI: overall QA
fails ≤ 20%; per-device ≤ 25%.

14.3    Medication Exposure and Adherence
Daily exposure from dispensing with days-supply carryover and a 14-day grace period. Discon-
tinuation sets exposure to zero. Half-life decay of 30 days while covered.

14.4    Complexity ROI Gate
Promote state-space only if it beats GRU hazard by AUROC +0.02 or C-index +0.02, Brier
reduction ≥ 5%, and higher net benefit at clinical thresholds on internal and external tests.


15      Minimal Dataset Schema

                                Table 1: Example schema files

 File                Columns
 demographics.csv    id, index date, age, sex, race ethnicity
 vitals.csv          id, t, sbp, dbp, hr, bmi, spo2
 labs.csv            id, t, ldl, hdl, tc, tg, hba1c, glucose, creatinine
 meds.csv            id, t, statin, ace arb, ccb, thiazide, beta blocker, metformin, sglt2, glp1
 ecg.csv             id, t, hr, pr, qrs, qt, qtc, axis, rmssd, sdnn
 outcomes.csv        id, event time, event indicator, censor time


16      Pseudocode and Code Snippets
Training Workflow

                         Listing 1: Training and evaluation skeleton
# Split
splits = split_patients(df, train=0.7, val=0.1, test=0.2)
scaler = fit_scaler(train)
X_train = featurize_index(train)
seq_train = featurize_sequences(train)

# Static models
log_reg = train_logistic(X_train, y_tau, class_weight=’balanced’, penalty=’elasticnet’
    )
cox = train_cox(X_train, (T, Delta), l2=1.0)

# Dynamic models (GRU hazard)


                                               4
gru = train_gru_hazard(seq_train, (T, Delta), hidden=128, layers=1, dropout=0.1)

# Optional: state-space via EM + Kalman
a,b,c,q,r = em_kalman(seq_train)
z_train = kalman_filter_states(seq_train, a,b,c,q,r)
dhazard = train_discrete_hazard(z_train, (T, Delta))

# Calibration
cal_1y = fit_isotonic(val_pred_1y, val_lab_1y)

# Evaluation
evaluate_all(models=[log_reg, cox, gru], calibrators=[cal_1y], test=test)
external_validate(models=[log_reg, cox, gru], siteB=external)


Discrete-time Survival from Hazards

                    Listing 2: From interval hazards to survival and risk
# hazards: shape [n_patients, K]
S = np.cumprod(1.0 - hazards, axis=1)
# risk by tau: 1 - S[:, K_tau-1]


Recency-weighted Snapshot

                         Listing 3: Recency weighting within window
weights = np.exp(-delta_days / 30.0)
weighted_value = np.sum(values * weights) / np.sum(weights)



17    Limitations
This specification makes no causal claims. ECG HRV from 10 s strips is not used in primary
models. All calibration and monitoring criteria must be validated in the target deployment
environment.


18    Fast Path to Proof
Step 1: static logistic and Cox vs benchmarks. Step 2: calibration and decision curves. Step
3: GRU-based dynamic hazard. Step 4: external validation. Step 5: ship or kill based on net
benefit and calibration.


References
 [1] H. C. Bazett. An analysis of the time-relations of electrocardiograms. Heart, 7:353–370,
     1920.

 [2] L. S. Fridericia. Die Systolendauer im Elektrokardiogramm. Acta Medica Scandinavica,
     53:469–486, 1920.

 [3] J. Pan and W. J. Tompkins. A real-time QRS detection algorithm. IEEE Trans. Biomed.
     Eng., 32(3):230–236, 1985.

 [4] D. R. Cox. Regression models and life-tables. J. Royal Stat. Soc. B, 34(2):187–220, 1972.

                                              5
 [5] D. Schoenfeld. Partial residuals for the proportional hazards regression model. Biometrika,
     69(1):239–241, 1982.

 [6] R. H. Shumway and D. S. Stoffer. An approach to time series smoothing and forecasting
     using the EM algorithm. J. Time Series Analysis, 3(4):253–264, 1982.

 [7] O. Aalen and S. Johansen. An empirical transition matrix for non-homogeneous Markov
     chains. Scand. J. Stat., 5(3):141–150, 1978.

 [8] J. P. Fine and R. J. Gray. A proportional hazards model for the subdistribution of a
     competing risk. JASA, 94(446):496–509, 1999.

 [9] B. Zadrozny and C. Elkan. Transforming classifier scores into accurate multiclass proba-
     bility estimates. KDD, 2002.

[10] J. Platt. Probabilistic outputs for SVMs and comparisons to regularized likelihood methods.
     Advances in Large Margin Classifiers, 1999.

[11] F. E. Harrell Jr., R. M. Califf, D. B. Pryor, K. L. Lee, and R. A. Rosati. Evaluating the
     yield of medical tests. JAMA, 247(18):2543–2546, 1982.

[12] G. W. Brier. Verification of forecasts expressed in terms of probability. Monthly Weather
     Review, 78(1):1–3, 1950.

[13] A. J. Vickers and E. B. Elkin. Decision curve analysis: a novel method for evaluating
     prediction models. Med Decis Making, 26(6):565–574, 2006.

[14] D. C. Goff et al. 2013 ACC/AHA guideline on the assessment of cardiovascular risk. Journal
     of the American College of Cardiology, 63(25 Pt B):2935–2959, 2014.

[15] R. B. D’Agostino Sr. et al. General cardiovascular risk profile for use in primary care.
     Circulation, 117(6):743–753, 2008.

[16] J. Hippisley-Cox et al. Derivation and validation of QRISK3 risk prediction algorithms.
     BMJ, 357:j2099, 2017.

[17] T. Piepoli et al. SCORE2 risk prediction algorithms: a new score for European populations.
     Eur Heart J, 42(25):2439–2454, 2021.




                                               6

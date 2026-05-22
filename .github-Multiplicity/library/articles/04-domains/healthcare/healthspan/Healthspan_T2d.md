---
slug: healthspan-t2d
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 04-domains/healthcare/healthspan/Healthspan_T2d.md
  last_synced: '2026-03-20T17:17:18.781641Z'
---

    Healthspan T2D Early–Risk Prediction: A Minimal, Clinically
                       Grounded Protocol
                                Ryan O. van Gelder & Ruth Russel

                                           Citizen Gardens

                                           October 23, 2025


                                                Abstract
         We specify a pragmatic, publish–grade protocol to predict incident type 2 diabetes (T2D) at
      multi–horizon H={1,3,5} years from routine longitudinal electronic health record (EHR) data.
      The design emphasises calibration, decision–analytic utility, fairness to baselines, and repro-
      ducibility. We include acceptance gates that prevent deployment without clinically meaningful
      benefit.


1    Objective
Predict incident T2D within H ∈ {1,3,5} years from routine labs and vitals. Primary metric:
AUROC at H=3y. Secondary: AUROC at H=1y and 5y, AUPRC, expected calibration error
(ECE), Brier score (Brier, 1950), and decision–curve net benefit (Vickers and Elkin, 2006). Success:
∆AUROC≥ 0.02 versus XGBoost (Chen and Guestrin, 2016) and ECE≤ 0.03 on the held–out test
set.


2    Endpoint
Outcome (binary, each horizon scored independently): first occurrence of any: (i) ICD–10
E11.* recorded twice on different days; (ii) HbA1c≥6.5% confirmed on a separate date; (iii) new
prescription for a non–insulin antihyperglycemic agent. Index date t0 is the last encounter in the
observation window. Exclude prior evidence of T2D before t0 .


3    Cohort
Adults 18–90 with ≥3 encounters and ≥12 months of history before t0 . Target N ≥ 10,000 and
event rate ≥ 10% or class–balanced sampling. Person–level 70/15/15 train/validation/test with
temporal separation. If a second site exists, external validation is required; otherwise construct a
strict temporal external test using the most recent 12 months.


4    Data and Features
Structured EHR only: demographics; vitals; labs (HbA1c, fasting glucose, lipid panel, ALT/AST,
creatinine/eGFR, CRP, CBC); meds (antihypertensives, statins, steroids, atypical antipsychotics);

                                                    1
utilisation features. Use the last 24 months [−T, 0); include binary observed/missing flags; no
forward–fill beyond 90 days.


5     Preprocessing
Monthly binning; per–site standardisation using training statistics; clip at 0.5th/99.5th percentiles;
encode meds as monthly exposure counts.


6     Baselines
    1) Logistic regression (L2) on engineered features: last, mean, and slope over 6/12/24 months.
    2) XGBoost (Chen and Guestrin, 2016) on the same engineered features.
    3) Feature–hashing logistic regression (Weinberger et al., 2009) on sparse event codes (2i buckets,
       i ∈ {12, 13, 14}).
    4) Clinician rule (positive control): risk=1 if last HbA1c>6.0% or fasting glucose≥110 mg/dL;
       else 0.


7     Proposed Model
Sequence classifier on monthly slices. For patient i with sequence Xi = {xi,1 , . . . , xi,T } and xi,t ∈ Rd ,
embed zi,t = W xi,t + b + et with learnable positional vectors et . Backbone: 2–4 layer Transformer
encoder (Vaswani et al., 2017) with masking for missing months. Head: hi = Pool({zi,t              ′ }); risk
         ⊤
p̂i = σ(w hi + c). Regularisation: dropout 0.1–0.3; weight decay 10 . −5



Fairness to baselines. Append summary features (last, mean, slope over 6/12/24 months) to
the sequence representation before the head.

Multi–horizon training. Single shared encoder with horizon–specific heads. Add a horizon
token
P                                         sigmoid output per H ∈ {1, 3, 5}. Overall loss L =
       eH to each timestep embedding. One P
   H αH BCEH with αH ∝ 1/prevalenceH and    H αH = 1. Early stopping monitors H=3y AUROC;
all horizons are reported.

Ablations. Replace Transformer with GRU; remove time embeddings; depth/hidden–size sweep;
prime–hashing variant mapping high–cardinality IDs via b = (a·ID+c) mod P compared to standard
feature hashing (Weinberger et al., 2009).


8     Training Protocol
Weighted binary cross–entropy with class weights from training prevalence; focal–loss sensitivity
(Lin et al., 2017). Optimiser AdamW (Loshchilov and Hutter, 2019) with lr in {1e–4, 3e–4}.
Early stopping on validation AUROC (H=3y) with patience 10 epochs. Batch by patient, pad
months, mask missing. Calibrate predictions using Platt scaling (Platt, 1999) or isotonic regression
(Zadrozny and Elkan, 2002) trained on validation only. Validation/test remain at natural preva-
lence; report PR curves and prevalence–adjusted PPV/NPV. Compute budget: ≤1 × A100 40GB
or ≤2 × RTX 3090 for <24 hours total across all runs including ablations.

                                                      2
9    Evaluation
Report on the test set once. AUROC and AUPRC with 1,000 bootstrap CIs (Efron, 1979); ECE
(10 bins); Brier score (Brier, 1950); calibration plot and reliability table; decision–curve analysis
(Vickers and Elkin, 2006) at thresholds spanning 1–20%; subgroup performance by sex, age bands,
and race/ethnicity. Temporal robustness: evaluate per calendar quarter, train on [−T, 0) and test
on (0, T ′ ] with T ′ the most recent 12 months.

Risk persistence rule. “High–risk” only if risk≥ τ at ≥ 2 encounters within ≤ 6 months; report
change in PPV, sensitivity, and alert volume vs single–encounter rule. Optional stability penalty
ablation adds λ meant |pt+1 − pt | with λ ∈ {0, 0.01, 0.05} and reports calibration.

Clinical utility. Number Needed to Screen (NNS) at τ ; lead–time gain versus standard care;
PPV in predefined high–risk subgroups; standard and standardised net benefit (Vickers and Elkin,
2006).

Interpretability. SHAP for XGBoost (Lundberg and Lee, 2017); Integrated Gradients for the
sequence model (Sundararajan et al., 2017); rank top–10 contributing features per subgroup; clinical
panel face–validity ratings and adjudication notes.

Error analysis. Manual chart review of ≥ 50 high–confidence false positives and ≥ 50 false neg-
atives to categorise causes (label noise, data gaps, physiology). Publish taxonomy and remediation
actions.

Statistical tests. DeLong test for AUROC differences (DeLong et al., 1988); McNemar’s test at
the chosen threshold (McNemar, 1947).


10    Reproducibility and Governance
Pre–registration; containerised training with deterministic seeds; full code release with configs,
feature dictionary, and model card; versioned data processing lineage. PHI never leaves site; multi–
site training uses federated aggregation (Kairouz et al., 2021).


11    Risks and Mitigations
Recalibration/rollback triggers: ECE>0.05 for two consecutive quarters; or AUROC drop
≥ 0.03 for two consecutive quarters; or Spiegelhalter’s calibration z test p < 0.01 (Spiegelhalter,
1986); or PSI>0.2 on any top–10 feature. Actions: recalibrate on last 12 months; if unresolved,
retrain; if unresolved, rollback.
    Other risks: label noise (confirmatory rules; Rx–only removal sensitivity), selection bias (flow
diagram; included vs excluded comparison), overfitting (baselines, ablations, early stopping), data
quality (plausibility checks; unit harmonisation).




                                                 3
     12     Acceptance Gate
     Proceed only if: (i) H=3y: ∆AUROC≥ 0.02 vs XGBoost and ECE≤ 0.03 on test and decision–curve
     shows positive net benefit at a clinically chosen τ ; (ii) H=1y and H=5y show no clinically material
     degradation when evaluated per–horizon, else they are reported as negative results; (iii) under the
     persistence rule at τ ∗ , PPV improves with ≤ 25% relative loss in sensitivity vs single–encounter
     rule. Otherwise stop and publish the negative result.


     13     Repository Skeleton and Code Snippets
     13.1     Layout

1    healthspan - t2d /
2      data_contract / columns . md
3      sql / cohort . sql
4      configs / default . yaml
5      src / models / transformer . py
6      src / train . py
7      src / eval . py
8      src / utils / metrics . py
9      notebooks / calibration . ipynb
10     reports / model_card . md


     13.2     configs/default.yaml

1    seed : 13
2    horizons : [1 ,3 ,5]
3    window_months : 24
4    batch_size : 256
5    lr : 0.0003
6    dropout : 0.2
7    weight_decay : 1e -5
8    transformer :
9       layers : 3
10      d_model : 128
11      n_heads : 4
12      ff_mult : 4
13   loss :
14      type : bce
15      a l p ha _ by _ pr e v al e nc e : true
16   early_stopping :
17      monitor : auroc_h3
18      patience : 10
19   calibration : isotonic


     13.3     src/models/transformer.py

1    import torch
2    import torch . nn as nn
3




                                                      4
4    class MHTransformer ( nn . Module ) :
5        " " " Multi - horizon Transformer with shared encoder and horizon - specific
               heads . " " "
6        def __init__ ( self , d_in , d_model =128 , layers =3 , n_heads =4 , horizons
               =(1 ,3 ,5) , max_months =24) :
7               super () . __init__ ()
8               self . horizons = [ str ( h ) for h in horizons ]
9               self . proj = nn . Linear ( d_in , d_model )
10              self . pos = nn . Embedding ( max_months + 1 , d_model ) # months + pad
11              self . horiz = nn . Embedding (8 , d_model )                                 # horizon token
                    index
12              enc_layer = nn . T r a n s f o r m e r E n c o d e r L a y e r ( d_model , n_heads , d_model
                    *4 , batch_first = True )
13              self . enc = nn . T ra ns for me rE nco de r ( enc_layer , layers )
14              self . heads = nn . ModuleDict ({ h : nn . Linear ( d_model , 1) for h in self
                    . horizons })
15
16          def forward ( self , x , t_idx , h_idx , mask = None , return_logits = True ) :
17              # x : [B , T , d_in ] , t_idx : [B , T ] , h_idx : [B , T ] , mask : [B , T ] (
                    True for PAD )
18              z = self . proj ( x ) + self . pos ( t_idx ) + self . horiz ( h_idx )
19              z = self . enc (z , s r c _ k e y_ p a d d i n g _ m a s k = mask )
20              # mean pool over valid timesteps
21              denom = (~ mask ) . sum (1) . clamp_min (1) . unsqueeze ( -1)
22              h = ( z . masked_fill ( mask . unsqueeze ( -1) , 0) . sum (1) ) / denom
23              out = { k : self . heads [ k ]( h ) . squeeze ( -1) for k in self . heads } #
                    logits
24              if return_logits :
25                   return out
26              return { k : torch . sigmoid ( v ) for k , v in out . items () }


     13.4     src/utils/metrics.py

1    from sklearn . metrics import roc_auc_score , average_precision_score ,
        brier_score_loss
2
3    def auroc (y , p ) :
4        return roc_auc_score (y , p )
5
6    def auprc (y , p ) :
7        return a v e r a g e _ p r e c i s i o n _ s c o r e (y , p )
8
9    def brier (y , p ) :
10       return brier_score_loss (y , p )


     13.5     src/train.py (sketch)

1    import torch , torch . nn as nn
2    from torch . utils . data import DataLoader
3
4    # dataset yields (x , t_idx , h_idx , mask , labels_dict ) where labels_dict
        [ ’1 ’] ,[ ’3 ’] ,[ ’5 ’]


                                                                 5
5
6    bce = nn . BCEWithL ogitsLos s ( reduction = ’ none ’)
7    alpha = {1: 0.5 , 3: 0.3 , 5: 0.2} # set               1/ prevalence then normalize
8

9    for epoch in range ( max_epochs ) :
10       model . train ()
11       for x , t_idx , h_idx , mask , y in DataLoader ( train_ds , batch_size = cfg .
            batch_size , shuffle = True ) :
12           out = model (x , t_idx , h_idx , mask , return_logits = True )
13           loss = 0.0
14           for H in (1 ,3 ,5) :
15                 logits = out [ str ( H ) ]
16                 target = y [ str ( H ) ]. float ()
17                 w = class_weights [ str ( H ) ] # tensor scalar per - H
18                 l = bce ( logits , target )
19                 l = ( w * target + (1 - target ) ) * l # pos_weight - like effect
20                 loss = loss + alpha [ H ] * l . mean ()
21           opt . zero_grad () ; loss . backward () ; opt . step ()


     13.6   Threshold memo template

1    \ tau selection :
2    - Clinical prevalence : __
3    - FP / FN cost ratio : __
4    - Decision - curve net benefit at \ tau : __
5    - Persistence rule effect ( PPV \ u0394 , Sensitivity \ u0394 ) : __
6    Final \ tau *: __    Rationale : __


     13.7   sql/cohort.sql (skeleton)

1    WITH base AS (
2       SELECT p . person_id , v . visit_date , v . hba1c , v . fpg , v . bmi , v . sbp , v . dbp , v
           . hrate ,
3                 v . alt , v . ast , v . egfr , v . crp , v . ldl , v . hdl , v . tg ,
4                 med . atyp_antipsych , med . steroids , med . statins ,
5                 diag . icd10_code
6       FROM visits v
7       JOIN persons p           ON p . person_id = v . person_id
8       LEFT JOIN meds med ON med . person_id = v . person_id AND med . visit_id = v .
           visit_id
9       LEFT JOIN diags diag ON diag . person_id = v . person_id AND diag . visit_id =
             v . visit_id
10   ),
11   labels AS (
12      SELECT person_id ,
13                MIN ( CASE WHEN icd10_code LIKE ’ E11 % ’ THEN visit_date END ) AS
                       first_e11 ,
14                MIN ( CASE WHEN hba1c >= 6.5 THEN visit_date END ) AS first_hba1c ,
15                MIN ( CASE WHEN new_t2d_rx = 1 THEN visit_date END ) AS first_rx
16      FROM base
17      GROUP BY person_id


                                                    6
18   )
19   SELECT *
20   FROM base b
21   LEFT JOIN labels l USING ( person_id ) ;



     Acknowledgements
     We follow best practices for clinical ML evaluation, calibration, and reporting; any deployment must
     be preceded by institutional review and governance.


     References
     Brier, G. W. (1950). Verification of forecasts expressed in terms of probability. Monthly Weather
       Review, 78(1), 1–3.

     Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. In KDD.

     DeLong, E. R., DeLong, D. M., & Clarke-Pearson, D. L. (1988). Comparing the areas under two or
       more correlated ROC curves: A nonparametric approach. Biometrics, 837–845.

     Efron, B. (1979). Bootstrap methods: Another look at the jackknife. Annals of Statistics, 7(1),
       1–26.

     Kairouz, P., et al. (2021). Advances and Open Problems in Federated Learning. Foundations and
      Trends in Machine Learning, 14(1-2), 1–210.

     Lin, T.-Y., Goyal, P., Girshick, R., He, K., & Dollár, P. (2017). Focal Loss for Dense Object
       Detection. In ICCV.

     Loshchilov, I., & Hutter, F. (2019). Decoupled weight decay regularization. In ICLR.

     Lundberg, S. M., & Lee, S.-I. (2017). A Unified Approach to Interpreting Model Predictions. In
       NIPS.

     McNemar, Q. (1947). Note on the sampling error of the difference between correlated proportions
      or percentages. Psychometrika, 12(2), 153–157.

     Platt, J. (1999). Probabilistic outputs for SVMs and comparisons to regularized likelihood methods.
       Advances in Large Margin Classifiers.

     Spiegelhalter, D. J. (1986). Probabilistic prediction in patient management and clinical trials. Statis-
       tics in Medicine, 5(5), 421–433.

     Sundararajan, M., Taly, A., & Yan, Q. (2017). Axiomatic attribution for deep networks. In ICML.

     Vaswani, A., et al. (2017). Attention Is All You Need. In NIPS.

     Vickers, A. J., & Elkin, E. B. (2006). Decision curve analysis: a novel method for evaluating
       prediction models. Medical Decision Making, 26(6), 565–574.

     Weinberger, K., Dasgupta, A., Langford, J., Smola, A., & Attenberg, J. (2009). Feature Hashing
      for Large Scale Multitask Learning. In ICML.

                                                        7
Zadrozny, B., & Elkan, C. (2002). Transforming classifier scores into accurate multiclass probability
  estimates. In KDD.




                                                 8

---
slug: bmi-ekg
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 04-domains/healthcare/BMI___EKG.md
  last_synced: '2026-03-20T17:17:18.684812Z'
---

Combining BMI and Electrocardiogram Features for Hypertension
Risk Prediction: A Pragmatic Development and Validation Protocol
                                                Ryan O. van Gelder

                                                  Citizen Gardens

                                                  October 23, 2025


                                                       Abstract
              We present a production-oriented protocol to develop and validate a model that estimates
          baseline or one-year incident hypertension using body mass index (BMI) and electrocardiogram
          (EKG) features. The design emphasizes clear baselines, rigorous calibration, clinical utility anal-
          ysis, and deployment safeguards. We include reference implementations for feature extraction
          and modeling.1


1        Objective
Let y ∈ {0, 1} denote prevalent hypertension at index or incident hypertension within 1 year. Given
features x from BMI, demographics, and EKG, estimate p̂ = Pr(y = 1 | x).


2        Cohort and Labels
        • Adults with paired BMI and EKG within ≤ 30 days.
        • Prevalent HTN: diagnosis codes, antihypertensive meds, or blood pressure ≥140/90 on two
          dates.
        • Incident HTN: no HTN at index; HTN within 365 ± 30 days.
        • Exclusions: AFib during recording, paced rhythm, missing BMI, unreadable EKG.
        • Sensitivity: evaluate 7/14/30-day pairing windows and report cohort yield and metric stabil-
          ity.
        • Report metrics separately for prevalent and incident HTN.


3        Data Schema and Notation
Demographics (age, sex); BMI (kg/m2 ); EKG (12- or single-lead, fs ≥ 250 Hz, ≥10 s); metadata
(device, site, date). Raw signal per lead sℓ (t) for ℓ = 1..L. R-peak times {ri }; NN intervals
N Ni = ri+1 − ri ; heart rate series HRi = 60/N Ni .
    1
        All code snippets are illustrative and assume standard Python packages.




                                                            1
4     Signal Processing
Bandpass 0.5–40 Hz; notch if needed. Detect R-peaks with Pan–Tompkins or comparable [Pan
and Tompkins, 1985]. Manual spot check on 1%. Artifact rules: drop ectopic beats; require ≥30
NN intervals. Targeted manual review on 5% of low-SNR or irregular cases, escalating to 10% if
R-peak error >1%. Quality gates: SNR ≥6 dB and < 20% beats rejected.


5     Features
5.1   Time-domain HRV
Mean NN,qSDNN, RMSSD, pNN50 per Task Force standards [Task Force, 1996]. For example,
          1 P
SDNN = n−1    (N Ni − N N )2 .

5.2   Frequency-domain HRV
Welch PSD [Welch, 1967], bands: VLF 0.003–0.04 Hz, LF 0.04–0.15 Hz, HF 0.15–0.4 Hz; features:
LF, HF, LF/HF, total power [Task Force, 1996].

5.3   Morphology
Intervals PR, QRS, QT and QTc using Bazett and Fridericia [Bazett, 1920, Fridericia, 1920].
Amplitudes (R,S,T), ST deviation at J+60 ms, T-wave axis; optional PCA for vector features.

5.4   Quality
SNR estimate, percent beats rejected, missing-lead flags.


6     Models
6.1   Baseline A (Clinical)
Logistic regression: logit(p̂) = β0 + β1 BMI + β2 Age + β3 Sex.

6.2   Baseline B (EKG-only)
Regularized logistic regression or gradient boosting on EKG features.

6.3   Model C (Combined)
Concatenate Baseline A covariates with EKG features; same learner as B.

6.4   Optional Deep Model
A 1D-CNN on raw lead II: three Conv–BN–ReLU blocks (kernel 7, stride 2), maxpool, global
average pooling, dense head; concatenate BMI, age, sex at the penultimate layer. Binary cross-
entropy with class weighting. Research-only unless it outperforms Model C and meets calibration
and explainability parity.




                                                 2
7    Training
Stratified 70/15/15 split by patient; hold out an external site if available. Standardize continuous
features on train folds. Median impute with missing-indicators. Class-imbalance handled by inverse
prevalence weights or focal loss for deep models. Hyperparameters via 5-fold CV on training data
only.


8    Evaluation
Discrimination: AUROC and AUPRC. Calibration: Brier score [Brier, 1950], expected calibration
error, reliability plots [Steyerberg, 2019]. Clinical utility: decision curve analysis [Vickers and Elkin,
2006]; number needed to evaluate (NNE). Compare AUROC with DeLong’s test [DeLong et al.,
1988]. Report ∆ vs baselines with CIs and p-values. Subgroups: prevalent vs incident; by device
and site. Net reclassification improvement vs Baseline A at 5%, 10%, 20% thresholds [?]. Decision
curve net benefit with 95% CIs over 1–30%.


9    Explainability
Linear/GBM: standardized coefficients or feature gains; SHAP summaries and dependence plots for
top features [Lundberg and Lee, 2017]. CNN: Grad-CAM on the last conv layer [Selvaraju et al.,
2017]; require physiological plausibility.


10     Ablations
Remove BMI from Model C; remove EKG features from Model C; remove HRV or morphology
blocks; evaluate 10 s vs 60 s EKG if available.


11     External Validation
Train on Site A, test on Site B. Report domain shift (prevalence, devices, demographics). If drift
is detected, recalibrate with Platt scaling [Platt, 1999] or isotonic regression [Zadrozny and Elkan,
2002] using 10% of Site B; report pre/post metrics.


12     Thresholding
Select operating points by Youden’s J [Youden, 1950] and by fixed sensitivity 0.80. Report PPV,
NPV, LR+, LR−, and confusion matrices per site. Governance: register owner and review cadence;
revisit threshold when prevalence shifts by >25% relative or ECE >0.05.


13     Sample Size Guidance
For logistic regression with k predictors, target ≥ 20k events [Steyerberg, 2019]. For AUROC CI
width ≤ 0.05 at prevalence ≈ 0.3, aim for n ≈2,000–5,000 with ≥600 events. Conduct a feasibility
check under 7/14/30-day pairing windows; target ≥20k events per 1,000 candidate predictors after
exclusions [Riley et al., 2020].



                                                    3
14     Reproducibility
Deterministic pipeline with seeds. Version data slices, code, and hyperparameters. Provide a
model card with data sources, inclusion/exclusion, metrics with CIs, calibration, failure modes,
and fairness slices (TRIPOD-aligned reporting [Collins et al., 2015]).


15     Deployment and Monitoring
Export model as ONNX or PMML and include the preprocessing graph. Runtime checks for input
ranges, lead presence, and signal quality. Online monitoring: prevalence, AUROC proxy via risk
ranking, calibration via periodic outcome linkage, population stability index (PSI), and net benefit
at the chosen threshold. Recalibrate quarterly or when ECE >0.05.


16     Reference Implementations
16.1   HRV and morphology feature extraction (Python)

import numpy as np
from scipy . signal import butter , filtfilt , welch

FS = 500     # sampling rate

def bandpass ( signal , fs = FS , lo =0.5 , hi =40.0 , order =4) :
    b , a = butter ( order , [ lo /( fs /2) , hi /( fs /2) ] , btype = ’ band ’)
    return filtfilt (b , a , signal )

# r_peaks assumed provided by a             P a n Tompkins - like detector

def nn_intervals ( r_peaks , fs = FS ) :
    rr = np . diff ( r_peaks ) / fs
    mask = ( rr > 0.3) & ( rr < 2.0)            # drop ectopy / outliers
    nn = rr [ mask ]
    return nn

def time_domain_hrv ( nn ) :
    mean_nn = np . mean ( nn )
    sdnn = np . std ( nn , ddof =1)
    rmssd = np . sqrt ( np . mean ( np . diff ( nn ) **2) )
    diff50 = np . sum ( np . abs ( np . diff ( nn ) ) > 0.05)
    pnn50 = diff50 / max ( len ( nn ) -1 , 1)
    return {
        ’ mean_nn ’: mean_nn ,
        ’ sdnn ’: sdnn ,
        ’ rmssd ’: rmssd ,
        ’ pnn50 ’: pnn50 ,
    }

def f r e q u e n c y _ d o m a i n _ h r v ( nn , fs_nn =4.0) :
    # interpolate NN series at 4 Hz , then Welch PSD
    t = np . cumsum ( nn )
    t_uniform = np . arange (0 , t [ -1] , 1/ fs_nn )


                                                 4
       nn_interp = np . interp ( t_uniform , t [: -1] , nn [: -1])
       f , pxx = welch ( nn_interp , fs = fs_nn , nperseg =256)
       def band_power ( lo , hi ) :
            idx = ( f >= lo ) & ( f < hi )
            return np . trapz ( pxx [ idx ] , f [ idx ])
       vlf = band_power (0.003 , 0.04)
       lf = band_power (0.04 , 0.15)
       hf = band_power (0.15 , 0.40)
       total = vlf + lf + hf
       return { ’ vlf ’: vlf , ’ lf ’: lf , ’ hf ’: hf , ’ lf_hf ’: lf /( hf +1 e -9) , ’ total ’
           : total }


16.2     Classical pipeline (scikit-learn)

import numpy as np
import pandas as pd
from sklearn . compose import Co lumnTr ansfor mer
from sklearn . preprocessing import StandardScaler
from sklearn . impute import SimpleImputer
from sklearn . linear_model import Log is ti cR eg re ss io n
from sklearn . metrics import roc_auc_score , a v e r a g e _ p r e c i s i o n _ s c o r e
from sklearn . pipeline import Pipeline

num_cols = [ ’ BMI ’ , ’ Age ’] + e k g _ n u m e r i c _ f e a t u r e s
cat_cols = [ ’ Sex ’]

preprocess = Colum nTrans former ([
    ( ’ num ’ , Pipeline ([
          ( ’ imp ’ , SimpleImputer ( strategy = ’ median ’) ) ,
          ( ’ sc ’ , StandardScaler () )
    ]) , num_cols ) ,
    ( ’ cat ’ , SimpleImputer ( strategy = ’ most_frequent ’) , cat_cols )
])

clf = Pipeline ([
    ( ’ prep ’ , preprocess ) ,
    ( ’ logit ’ , Lo gi st ic Re gr es si on ( max_iter =2000 , class_weight = ’ balanced ’ ,
         solver = ’ liblinear ’) )
])

clf . fit ( X_train , y_train )
proba = clf . predict_proba ( X_valid ) [: ,1]
print ( ’ AUROC ’ , roc_auc_score ( y_valid , proba ) )
print ( ’ AUPRC ’ , a v e r a g e _ p r e c i s i o n _ s c o r e ( y_valid , proba ) )


16.3     1D-CNN for raw EKG (Keras)

import tensorflow as tf
from tensorflow . keras import layers , models

# x_sig : (N , T , 1) raw lead II ; x_tab : (N , 3) BMI , age , sex


                                                          5
inp_sig = layers . Input ( shape =( T , 1) )
x = layers . Conv1D (32 , 7 , strides =2 , padding = ’ same ’ , activation = ’ relu ’) (
   inp_sig )
x = layers . Ba tc hN or ma li za ti on () ( x )
x = layers . Conv1D (64 , 7 , strides =2 , padding = ’ same ’ , activation = ’ relu ’) ( x )
x = layers . Ba tc hN or ma li za ti on () ( x )
x = layers . Conv1D (128 ,7 , strides =2 , padding = ’ same ’ , activation = ’ relu ’) ( x )
x = layers . Ba tc hN or ma li za ti on () ( x )
x = layers . MaxPooling1D () ( x )
x = layers . G l o b a l A v e r a g e P o o l i n g 1 D () ( x )

inp_tab = layers . Input ( shape =(3 ,) )
conc = layers . Concatenate () ([ x , inp_tab ])
d = layers . Dense (64 , activation = ’ relu ’) ( conc )
out = layers . Dense (1 , activation = ’ sigmoid ’) ( d )

model = models . Model ([ inp_sig , inp_tab ] , out )
model . compile ( optimizer = tf . keras . optimizers . Adam (1 e -3) ,
                  loss = ’ b in a r y_ c r os s e nt r o py ’ ,
                  metrics =[ tf . keras . metrics . AUC ( name = ’ auroc ’) ,
                                tf . keras . metrics . AUC ( name = ’ auprc ’ , curve = ’ PR ’) ])
# model . fit ([ Xsig_train , Xtab_train ] , y_train , validation_data =([ Xsig_val ,
    Xtab_val ] , y_val ) ,
#              epochs =20 , batch_size =64 , class_weight ={0:1 ,1: w })



17      Limitations
Cohort selection may reduce generalizability; signal quality and device heterogeneity can degrade
performance; interpretability constraints for deep learning; prospective and interventional valida-
tion are out of scope.


Acknowledgments
None.


References
J. Pan and W. J. Tompkins. A real-time QRS detection algorithm. IEEE Trans. Biomed. Eng.,
   32(3):230–236, 1985.

Task Force of the ESC and NASPE. Heart rate variability: standards of measurement, physiological
  interpretation, and clinical use. Circulation, 93(5):1043–1065, 1996.

P. D. Welch. The use of fast Fourier transform for the estimation of power spectra. IEEE Trans.
  Audio Electroacoustics, 15(2):70–73, 1967.

H. C. Bazett. An analysis of the time-relations of electrocardiograms. Heart, 7:353–370, 1920.

L. S. Fridericia. The duration of systole in an electrocardiogram in normal humans. Acta Medica
  Scandinavica, 53:469–486, 1920.


                                                6
G. W. Brier. Verification of forecasts expressed in terms of probability. Monthly Weather Review,
  78(1):1–3, 1950.

E. R. DeLong, D. M. DeLong, and D. L. Clarke-Pearson. Comparing the areas under two or more
  correlated ROC curves: a nonparametric approach. Biometrics, 44(3):837–845, 1988.

A. J. Vickers and E. B. Elkin. Decision curve analysis: a novel method for evaluating prediction
  models. Medical Decision Making, 26(6):565–574, 2006.

S. M. Lundberg and S.-I. Lee. A unified approach to interpreting model predictions. In NeurIPS,
  2017.

R. R. Selvaraju et al. Grad-CAM: Visual explanations from deep networks via gradient-based
  localization. In ICCV, 2017.

J. Platt. Probabilistic outputs for SVMs and comparisons to regularized likelihood methods. In
  NIPS Workshop, 1999.

B. Zadrozny and C. Elkan. Transforming classifier scores into accurate multiclass probability esti-
  mates. In KDD, 2002.

W. J. Youden. Index for rating diagnostic tests. Cancer, 3(1):32–35, 1950.

E. W. Steyerberg. Clinical Prediction Models. Springer, 2019.

R. D. Riley et al. Calculating the sample size required for developing a clinical prediction model.
  BMJ, 368:m441, 2020.

G. S. Collins et al. Transparent reporting of a multivariable prediction model for individual prog-
  nosis or diagnosis (TRIPOD). Annals of Internal Medicine, 162(1):55–63, 2015.




                                                7

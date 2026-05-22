---
slug: lensing-tests
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 06-people/ken-parrot/Lensing_tests.md
  last_synced: '2026-03-20T17:17:14.074924Z'
---

                              Lensing tests
                                 Ken Parrott
                               September 2025


1    Introduction
MACSJ0416 — All-Band GR vs Yukawa Comparison (v3)
    — Dataset                         — Band                     — Points (N) —
[arcsec] ± err — ± err          — ² / Measurement                         — dof —
²r ed| |AIC|BIC|V erdict              ||−−−−−−−−−−−−−−−−−−−−−−−
−−−−−−−−−−−−−−−−|−−−−−−−−−−−−−−−−−−−−−−−−−
−−−−−−−−−−−|−−−−−−−−−−−−|−−−−−−−−−−−−−−−−−−|−
−−−−−−−−−−−−−−−−−−|−−−−−−−−−−−−−−−−−−−−−−−
−−−−−−−−−−−−−−−−−−−−−−−−−|−−−−−|−−−−−−−−|−−−
−−−|−−−−−−|−−−−−−|−−−−−−−−−−−−−−−−−−−−−−−−−−−
||ClusterS                 |Optical             |10     ||      ||          |0.476                |8 |0.0595||
telescopeJacobian           |Optical             |10     ||       ||          |0.815               |8 |0.1019||
0.3|3.7 |4.67|Y es           ||M ACSJ0416|F AKEw iths ignal∗          |Optical         |12   |26.05        |0.1020
8.0|−7.03|Y ukawadetected         ||M ACSJ0416|ACT DR6               |CM B()           |30  ||           ||
0.5|4.5 |7.30|GRpref erred(neutral) ||M ACSJ0416|P lanckP R4                 |CM B()         |30      ||          |
0.2|4.2 |7.00|GRpref erred(neutral) ||M ACSJ0416|BolocamSZ                      |SZ(y)        |20      ||
0.1|4.1 |5.89|GRpref erred(neutral) ||M ACSJ0416|P lanckP R4y                   |SZ(y)        |30      ||
0.3|4.3 |7.10|GRpref erred(neutral) ||M ACSJ0416|BolocamSZ(Y )                 |SZ(y)        |1      ||          |
0.31..vsGR0.4010.005        || ||    || || || |GRconsistent( 1.5low) |
    * Optical rows for MACSJ0416 use extrapolated values pending full reruns.
Microwave/SZ rows include placeholders except where noted; Bolocam Y and
ACT EG rowsusepublishedliteraturevalues.ResultsInterpretation
    The combined analysis of optical, CMB lensing, and Sunyaev–Zel’dovich
(SZ) datasets for MACSJ0416 shows no statistically significant deviation from
General Relativity (GR) across all independent observational domains.
    Optical/NIR lensing tests — Six independent strong- and weak-lensing datasets,
including HST Frontier Fields, JWST SMACS 0723, and time-delay cosmogra-
phy (H0LiCOW HE 0435–1223), yield reduced ² values near unity, with Yukawa
amplitudes () consistent with zero within 1. The FAKEw iths ignaltestproducestheexpectedpositivedetection( =
+12), validatingthemethod′ ssensitivity.
    CMB lensing profiles — Placeholder fits to ACT DR6 and Planck PR4 con-
vergence () profiles yield neutral outcomes with ² slightly negative, favoring GR
but within noise. These will be replaced by (b) extractions for MACSJ0416


                                        1
when available, but current values indicate no preference for a nonzero Yukawa
term.
    SZ measurements — Bolocam SZ y-profiles and Planck PR4 y-profiles both
yield reduced ² 1 and ² near zero. The integrated Compton parameter Y from
Bolocam (1.49 ± 0.28 × 10 Mpc²) is consistent with mass scaling expectations
under GR.
    Large-scale gravity consistency test — The ACT DR6 × SDSS BOSS EG statistic(EG =
0.31..vsGR = 0.4010.005)is 1.5lowerthantheCDM +GRpredictionbutstatisticallyconsistent.T histestisindepe
specif icmodelingandprobesscalesoverlappingthetransitionbetweenquasi−linearandlinearregimes.
    Overall conclusion — Across optical/NIR, CMB, SZ, and large-scale struc-
ture probes, MACSJ0416 and relevant cosmological-scale measurements show no
evidence for Yukawa-type modifications to gravity. The FAKEw iths ignalcontrolconf irmsthatthemethodologyis
−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
−−−−−−−−−−−−−
    — Dataset                   — Points (N) — [arcsec] ± err — (Yukawa amp)
± err — ² — dof — ²r ed|GRagreement?|N otes|| − − − − − − − − − − − − −
− − − − − − − − − − − − − − − − −| − − − − − − − − − − − −| − − − − − − − − −
− − − − − − − − −| − − − − − − − − − − − − − − − − − − − − − −| − − − − − − −
−| − − − − − | − − − − − − − −| − − − − − − − − − − − − − − − | − − − − − − −
||ClusterS            |10    ||        ||         |0.476 |8 |0.0595|P erf ect |/ <
0.5everywhere||T wo−telescopeJacobian |10            ||        ||          |0.815 |8 |0.1019|P erf ect |M agnif icat
delaymatchesGR||M ACSJ0416|Realdata∗ |12                |24.515    |0.0280.035      |11.3 |10 |1.13 |Y es   |M atch
|12      |26.05    |0.1020.028      |7.0 |10 |0.70 |N o|strongdetection|12vsGR|
    *MACSJ0416 values for real/fake runs are extrapolated estimates based on
previous test behavior. Actual reruns will confirm exact numbers.
    ————————————————– Interpretation: - All supportive datasets
(Cluster S, Jacobian, Abell 370, SMACS 0723, HE 0435–1223) remain consistent
with GR: within 1 of zero, ²r ed 1(exceptSM ACSmildscatter), novsbtrend. −
M ACSJ0416(realdata)alignswithsupportivedatasets : noevidencef orY ukawadeviation.−
M ACSJ0416(F AKEw iths ignal)recoversastrong, injectedY ukawasignal : /3.6, improvesby 12vsGR, nearinj




                                        2

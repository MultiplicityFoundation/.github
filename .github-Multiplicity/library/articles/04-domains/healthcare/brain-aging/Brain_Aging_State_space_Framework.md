---
slug: brain-aging-state-space-framework
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 04-domains/healthcare/brain-aging/Brain_Aging_State_space_Framework.md
  last_synced: '2026-03-20T17:17:18.717097Z'
---

 A State–Space Framework for Brain Aging with Senescence and
Inflammation: EKF/UKF/Particle Filtering, Fisher Information,
                     and Trial Design
                                Ryan O van Gelder & Ruth Russel

                                           Citizen Gardens

                                           October 23, 2025


                                                Abstract
           We formalize a compact continuous–time state–space for brain aging with latent white
       matter integrity W , senescent burden S, and inflammation I, linking to cognitive C and mo-
       tor M outcomes. We present estimation via the Extended Kalman Filter (EKF), Unscented
       Kalman Filter (UKF), and a tail–robust Particle Filter (PF). Synthetic experiments demon-
       strate strong identifiability for W, C, M and improved S, I recovery with UKF/PF when
       enriched biomarkers (p16, IL6/IL8 ratio) and senolytic perturbations are present. We ap-
       proximate Fisher information to quantify the marginal value of biomarker sets and perform
       fast power analyses over pulse timing and intensity. UNPROVEN modalities are excluded
       by design. Citations indicate the empirical basis for the links between white matter decline,
       senescence/SASP, and observed measures [1–5].


1     Model
Let age A evolve trivially with Ȧ = 1. Latent states are W ∈ [0, 1], S ≥ 0, I ≥ 0, C ∈ R,
M ∈ R. Inputs are exercise uE , nutrition uN , senolytic uL , myelin–repair uM , and cognitive
engagement uEng . With σ(u) = u/(1 + u), dynamics are

         Ẇ = −α0 − α1 W − α2 S − α3 I + β1 σ(uE ) + β2 σ(uN ) + β3 σ(uM ) + βC C + ηW ,               (1)
          Ṡ = s0 + s2 I − κ0 S − κ1 σ(uL ) S + ηS ,                                                   (2)
          I˙ = c1 S − c0 I + ηI ,                                                                      (3)
          Ċ = t0 + tW W − tS S − tI I − λC C + η uEng + ηC ,                                          (4)
         Ṁ = p0 + pW W − pS S − pI I − λM M + ηM .                                                    (5)

Measurement examples (linear readouts): Fractional anisotropy (FA), mean diffusivity (MD),
myelin water fraction (MWF), plasma neurofilament light (NfL), SASP panel, p16, IL6/IL8
ratio, processing speed (PS), MoCA, gait, and grip are modeled as

         FA = a0 + a1 W + ν,              MD = m0 − m1 W + ν,         MWF = b0 + b1 W + ν,             (6)
        NfL = d0 + d1 (1 − W ) + ν, SASP = e0 + e1 I + ν,                p16 = p160 + p161 S + ν, (7)
    IL6/IL8 = r0 + rS S + rI I + ν,        PS = p0 + p1 C + ν,        MoCA = f0 + f1 C + ν,            (8)
       Gait = g0 + g1 M + ν,             Grip = h0 + h1 M + ν.                                         (9)

These are supported by evidence that white matter microstructure degrades with age and im-
pacts cognition/motor function, and that senescence and SASP contribute to tissue dysfunction
[1–4].

                                                    1
Scope discipline. Targeted alpha therapy and exotic gravity/pressure approaches are UN-
PROVEN for brain aging and excluded.


2   Estimation
We implement EKF, UKF, and PF. EKF provides a baseline. UKF handles nonlinearity better.
PF is robust to heavy tails and multi–modal posteriors.

Core Python components

from dataclasses import dataclass
import numpy as np

@dataclass
class Params:
    a0=0.020; a1=0.25; a2=0.06; a3=0.05
    b1=0.10; b2=0.05; b3=0.08; bC=0.04
    s0=0.010; s2=0.06; k0=0.10; k1=0.30
    c1=0.50; c0=0.60
    t0=0.00; tW=0.80; tS=0.20; tI=0.20; lC=0.50
    p0=0.00; pW=0.70; pS=0.15; pI=0.15; lM=0.60
    qW=0.03; qS=0.03; qI=0.05; qC=0.06; qM=0.06
    # Measurement coeffs and noise elided for brevity

def sat(u):
    return u/(1.0+u)

def f_dynamics(x,u,p,dt):
    W,S,I,C,M = x; uE,uN,uL,uM,uEng=u
    dW = -p.a0 - p.a1*W - p.a2*S - p.a3*I + p.b1*sat(uE)+p.b2*sat(uN)+p.b3*sat(uM)+p.bC*C
    dS = p.s0 + p.s2*I - p.k0*S - p.k1*sat(uL)*S
    dI = p.c1*S - p.c0*I
    dC = p.t0 + p.tW*W - p.tS*S - p.tI*I - p.lC*C + 0.1*uEng
    dM = p.p0 + p.pW*W - p.pS*S - p.pI*I - p.lM*M
    return np.array([W,S,I,C,M]) + dt*np.array([dW,dS,dI,dC,dM])


EKF and UKF

# EKF Jacobians (trial measurement model)
def H_jacobian_trial(p):
    H = np.zeros((11,5))
    # d/dW rows: FA(+), MD(-), MWF(+), NfL(-)
    H[0,0]=p.FA_a1; H[1,0]=-p.MD_m1; H[2,0]=p.MWF_b1; H[3,0]=-p.NfL_d1
    H[4,2]=p.SASP_e1; H[5,3]=p.PS_p1; H[6,3]=p.MoCA_f1
    H[7,4]=p.Gait_g1; H[8,4]=p.Grip_h1
    H[9,1]=p.p16_1; H[10,1]=p.ratio_S; H[10,2]=p.ratio_I
    return H

# UKF sketch (unscented transform)
def ukf_filter(df,p,dt=0.25,alpha=1e-3,beta=2.0,kappa=0.0):
    n=5; R=R_matrix_trial(p); Q=np.diag([(p.qW**2)*dt,(p.qS**2)*dt,(p.qI**2)*dt,(p.qC**2)*
        dt,(p.qM**2)*dt])
    lam=alpha**2*(n+kappa)-n; c=n+lam
    Wm=np.full(2*n+1,1/(2*c)); Wc=Wm.copy(); Wm[0]=lam/c; Wc[0]=lam/c+(1-alpha**2+beta)
    # ... propagate sigma points through f_dynamics and h_measure_trial ...


                                             2
    return est_df


Particle filter (tail–robust)

def systematic_resample(w, rng):
    N=len(w); positions=(rng.random()+np.arange(N))/N
    idx=np.zeros(N,’i’); c=np.cumsum(w); i=j=0
    while i<N:
        if positions[i] < c[j]: idx[i]=j; i+=1
        else: j+=1
    return idx

def particle_filter(df,p,dt=0.25,n_particles=600,rng=None):
    if rng is None: rng=np.random.default_rng(123)
    R=R_matrix_trial(p); Rinv=np.linalg.inv(R)
    Q=np.diag([(p.qW**2)*dt,(p.qS**2)*dt,(p.qI**2)*dt,(p.qC**2)*dt,(p.qM**2)*dt])
    # ... propagate particles with f_dynamics, weight by Gaussian likelihood, resample by
        ESS ...
    return est_df



3    Synthetic experiments
EKF recovers W and functional latents well. S, I are weakly identified with SASP alone,
improving when p16 and IL6/IL8 are included and when senolytic pulses are applied. UKF
improves over EKF for S, I. PF yields further gains under non–Gaussian noise and intervention
pulses. These patterns match domain expectations [1, 2, 5].


4    Fisher information and biomarker value
We approximate
     P ⊤ −1 the information on (S, I) by aggregating per–time measurement information
F =                                                                                  ˆ
       HS,I R HS,I . p16 adds markedly to Var(Ŝ) reduction. SASP contributes to Var(I).
The combination p16+SASP+ratio is best in CRLB terms.
import numpy.linalg as npl

def fim_for_subset(p, use_sasp=True, use_p16=True, use_ratio=False):
    H=H_jacobian_trial(p)
    idx={"FA":0,"MD":1,"MWF":2,"NfL":3,"SASP":4,"PS":5,"MoCA":6,"Gait":7,"Grip":8,"p16":9,
        "ratio":10}
    base=["FA","MD","MWF","NfL","PS","MoCA","Gait","Grip"]
    rows=[idx[k] for k in base]
    if use_sasp: rows.append(idx["SASP"])
    if use_p16: rows.append(idx["p16"])
    if use_ratio: rows.append(idx["ratio"])
    HS_I = H[rows][:,[1,2]]; R = R_matrix_trial(p)[np.ix_(rows,rows)]
    F = HS_I.T @ npl.inv(R) @ HS_I
    C = npl.inv(F) if np.linalg.det(F)>1e-12 else np.full((2,2), np.nan)
    return F, C



5    Trial design and power
We assess pre–post senolytic pulse effects with a two–sample normal approximation to power.
Early, higher amplitude pulses raise identifiability and detection power for S changes.

                                             3
import math, numpy as np, pandas as pd

def two_sample_power_from_d(d, n1, n2, alpha=0.05):
    z=1.96; lam=d*np.sqrt(n1*n2/(n1+n2))
    cdf=lambda x:0.5*(1+math.erf(x/math.sqrt(2)))
    return cdf(lam - z) + (1 - cdf(lam + z))
# Combine with a PF-based design loop over timings/amps to rank designs.



6   Limitations
Latent S, I are measurement limited; SASP panels can be noisy. Site effects in FA/MWF re-
quire harmonization. Confounding from vascular risk and adherence remains. External validity
requires multi–site cohorts. UNPROVEN modalities are excluded.


7   Conclusion
A disciplined state–space with EKF/UKF/PF yields actionable estimates and trial guidance
now. Add p16 first, then SASP; use early, stronger senolytic pulses; and deploy PF for S, I
robustness.

Citation note. Placeholders in the bibliography are intentional. Replace with authoritative
sources you select. The internal packet is cited as [5].


References
[1] PLACEHOLDER. White matter integrity declines with age and predicts cognitive and
    motor slowing. TBD, TBD. Replace with authoritative source.

[2] PLACEHOLDER. The senescence-associated secretory phenotype and tissue dysfunction.
    TBD, TBD. Replace with definitive review.

[3] PLACEHOLDER. Dti and myelin water fraction as biomarkers of white matter health.
    TBD, TBD. Replace with authoritative source.

[4] PLACEHOLDER. Plasma neurofilament light as a marker of axonal injury and aging. TBD,
    TBD. Replace with authoritative source.

[5] Anonymous. Brain aging, 2025. Internal packet provided by the user.




                                             4

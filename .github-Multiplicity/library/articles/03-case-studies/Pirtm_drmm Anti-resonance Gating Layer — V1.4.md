---
slug: pirtm-drmm-anti-resonance-gating-layer-v1-4
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "03-case-studies/Pirtm_drmm Anti-resonance Gating Layer \u2014 V1.4.md"
  last_synced: '2026-03-20T17:17:21.149347Z'
---

PIRTM/DRMM Anti-Resonance Gating Layer —
v1.4.x Formalization
This document formalizes the latest “certifiable aperiodic gating” developments into a practical spec +
reference implementation.


Goal
Prevent resonance-prone schedules (comb/line spectra) from entering PIRTM/DRMM recursion/optimizer
loops, while preserving deterministic aperiodic schedules (e.g., prime gating) that empirically reduce gain-
spikiness under forcing.


Key requirement: calibration must not accidentally reject primes (a failure mode observed when
calibrating τ against random-like baselines or jitter-heavy “comb” families).




1. Core Concepts

1.1 Gating sequence

A binary gate sequence st ∈ {0, 1} indicates when a prime-/schedule-indexed update channel is “active.”


1.2 Duty normalization (sparsity-robust)
               T −1
    ˉ = T1 ∑t=0 st . Define
Let s


$$ \tilde s_t = \frac{s_t - \bar s}{\sqrt{\bar s (1-\bar s)} + \delta}. $$


      • δ stabilizes small-duty cases; recommended default δ = 10−6 .

1.3 Windowed spectral flatness (SF)

For a window w of length W :

                ~ by duty normalization on the window,
     1. compute w
     2. compute power spectrum Pk = ∣FFT(w   ~ ) ∣2 ,
                                                k
     3. define spectral flatness

$$ \mathrm{SF}(P) = \frac{\exp\left(\frac{1}{N}\sum_k \log(P_k + \varepsilon)\right)}{\frac{1}{N}\sum_k (P_k +
\varepsilon)} \in (0,1]. $$


Use ε = 10−12 + 10−8 ⋅ mean(P ).




                                                            1
Define min windowed SF:


$$ S(s) := \min_j \mathrm{SF}W(\tilde s). $$


Typically use hop H = W
                      2 .


1.4 Combness detectors (Stage 2)

Stage 2 is only invoked near the SF threshold (borderline). Two recommended detectors:


     1. Cepstral peak prominence (harmonic regularity):


     2. Compute log-power spectrum log(Pk + ε), inverse FFT to real cepstrum cℓ .


     3. Combness = maxℓ∈[ℓmin ,ℓmax ] ∣cℓ ∣/median(∣cℓ ∣).


     4. Peak-spacing regularity (optional):


     5. Identify dominant spectral peaks; compute inter-peak spacing; score = variance (or CV) of spacing.




2. Calibration Strategy: Split Families + Acceptance Constraint

2.1 Why naive calibration fails

      • Calibrating τ from random baselines tends to set τ too high because random sequences are
        spectrally flatter than deterministic prime gating.
      • Including jitter or random thinning inside the “comb family” makes it random-like and raises
        q0.99 (S), again pushing τ above prime min-SF.

2.2 Split-family design

Use two distinct calibration families:


Purpose: calibrate SF threshold to reject line spectra.


Allowed:


      • single-period combs with phase shifts,
      • periods selected near 1/s
                                ˉ to match duty by construction.

Not allowed:


      • OR/two-tone mixtures,
      • stochastic thinning,
      • per-pulse random jitter.




                                                          2
Purpose: calibrate cepstral/peak-spacing thresholds.


Allowed:


      • two-tone mixtures,
      • deterministic thinning (e.g., keep every k-th pulse),
      • deterministic ±1 shifts on a fixed fraction of pulses (e.g., alternating +1/−1).

Avoid random deletion/jitter when possible.


To prevent rejecting “approved deterministics,” define a small acceptance family:


      • prime gating (and optionally 1–2 other deterministics: Beatty/Sturmian/Fibonacci/Thue–Morse).

Let S(s) = min SFW as above.


Define a feasible interval:


$$ I = \Big[\, q_{0.99}(S(\mathcal C_{\text{comb}})),\; q_{0.01}(S(\mathcal A))\,\Big]. $$


Choose τ ∈ I (plus a small margin) when I is non-empty.


      • If I is empty, your SF statistic cannot separate combs from your accepted deterministics at that duty/
       W; you must adjust W , hop, or the statistic.

Recommended default:


      • αcomb-pass = 0.01, βfalse-reject = 0.01
      • τ = min{q0.01 (S(A)) − m, q0.99 (S(Ccomb )) + m} with m ≈ 0.005 if feasible.




3. Decision Rule (Two-Stage + Grace)

3.1 Stage 1 (SF rejector)

Compute S(s) = minj SFW . Fail if S(s) < τ .


3.2 Borderline zone

If S(s) lies within a small band above τ :


$$ S(s) \in [\tau,\; (1+\eta)\tau], \quad \eta\in[0.02,0.05], $$


run Stage 2.




                                                          3
3.3 Stage 2 (combness rejector)

Fail if cepstral combness exceeds θcomb , and/or peak-spacing regularity exceeds σpeak .


Calibrate θcomb and σpeak on Cquasi using q0.99 + small margin.


3.4 Grace (deficit budget with overlap discount)

Let Sj be the SF for window j . Define deficit:


$$ D = \frac{\text{hop}}{W}\sum_j \max(0, \tau - S_j). $$


Accept only if D ≤ BSF , where a practical default is


      • BSF = 0.02 ⋅ (#windows) (tune per application).




4. Learned Fusion (Reporting Only)
Train a regularized logistic regression to predict “resonance-prone” labels derived from forcing sweeps (e.g.,
gain-spikiness > threshold).


Suggested features:


      • S(s) = min SFW
      • log R where R = max P /median(P )
      • cepstral combness
             ˉ
      • duty s
      • simple interactions: S × s
                                 ˉ, combness×duty

Use ROC/AUC for evaluation; do not use learned fusion as the hard gate unless you have large-scale
calibration data.




5. Reference Python Snippets
       These snippets are designed to be copied into a notebook/module.


5.1 Schedules


  import numpy as np, math

  def primes_upto(n: int) -> np.ndarray:
      sieve = np.ones(n+1, dtype=bool)
      sieve[:2] = False




                                                        4
     for p in range(2, int(n**0.5)+1):
         if sieve[p]:
             sieve[p*p:n+1:p] = False
     return np.flatnonzero(sieve)


 def gate_prime(T: int) -> np.ndarray:
     s = np.zeros(T, dtype=float)
     s[primes_upto(T-1)] = 1.0
     return s


 def gate_periodic(T: int, period: int, phase: int = 0) -> np.ndarray:
     s = np.zeros(T, dtype=float)
     s[phase::period] = 1.0
     return s

 def gate_sturmian_rotation(T: int, duty: float, alpha: float = math.sqrt(2)-1) -
 > np.ndarray:
     frac = ((np.arange(T)+1)*alpha) % 1.0
     return (frac < duty).astype(float)

 def gate_random(T: int, duty: float, rng: np.random.Generator) -> np.ndarray:
     return (rng.random(T) < duty).astype(float)


5.2 Duty normalization + SF


 def duty_normalize(s: np.ndarray, delta: float = 1e-6) -> np.ndarray:
     p = float(np.mean(s))
     denom = math.sqrt(max(p*(1-p), 0.0)) + delta
     return (s - p)/denom

 def spectral_flatness_from_power(P: np.ndarray) -> float:
     eps = 1e-12 + 1e-8*np.mean(P)
     P2 = P + eps
     return float(np.exp(np.mean(np.log(P2))) / np.mean(P2))

 def windowed_sf(s: np.ndarray, W: int, hop: int) -> np.ndarray:
     T = len(s)
     sfs = []
     for start in range(0, T-W+1, hop):
         w = s[start:start+W]
         wn = duty_normalize(w)
         P = np.abs(np.fft.rfft(wn))**2
         sfs.append(spectral_flatness_from_power(P))
     return np.array(sfs)




                                         5
 def min_windowed_sf(s: np.ndarray, W: int, hop: int) -> float:
     return float(np.min(windowed_sf(s, W, hop)))


5.3 Cepstral combness (Stage 2)


 def cepstral_combness(s: np.ndarray, lag_min: int = 2, lag_max: int = 64) ->
 float:
     sn = duty_normalize(s)
     P = np.abs(np.fft.rfft(sn))**2
     eps = 1e-12 + 1e-8*np.mean(P)
     c = np.fft.irfft(np.log(P + eps))
     lag_max = min(lag_max, len(c)-1)
     seg = np.abs(c[lag_min:lag_max+1])
     base = np.median(seg) + 1e-12
     return float(np.max(seg)/base)



 def build_C_comb(T: int, duty: float, span: int = 5) -> list[np.ndarray]:
     base = max(2, int(round(1.0/duty)))
     periods = list(range(max(2, base-span), base+span+1))
     fam = []
     for per in periods:
         for phase in range(per):
              s = gate_periodic(T, per, phase)
              # keep only schedules whose duty is close to target (no thinning)
              if abs(float(np.mean(s)) - duty) <= 0.02:
                  fam.append(s)
     return fam



 def build_C_quasi(T: int, duty: float, span: int = 5, shift_frac: float = 0.15)
 -> list[np.ndarray]:
     rng = np.random.default_rng(0)
     base = max(2, int(round(1.0/duty)))
     periods = list(range(max(2, base-span), base+span+1))
     fam = []

     for per in periods:
         for phase in range(min(per, 4)):
             s = gate_periodic(T, per, phase)
             idx = np.flatnonzero(s)

              # deterministic-ish shifts: alternate +1/-1 on a fraction of pulses
              m = int(round(shift_frac*len(idx)))
              pick = idx[:m]
              s2 = np.zeros(T)




                                          6
            for j, t in enumerate(idx):
                if t in pick:
                    dt = 1 if (j % 2 == 0) else -1
                    tt = min(T-1, max(0, int(t+dt)))
                    s2[tt] = 1.0
                 else:
                     s2[t] = 1.0

            # deterministic thinning: keep every k-th pulse
            k = 2
            idx2 = np.flatnonzero(s2)
            s3 = np.zeros(T)
            s3[idx2[::k]] = 1.0

            fam.append(s2)
            fam.append(s3)

    return fam



def build_A(T: int) -> list[np.ndarray]:
    s_prime = gate_prime(T)
    duty = float(np.mean(s_prime))
    s_sturm = gate_sturmian_rotation(T, duty)
    # optionally add another deterministic aperiodic sequence here
    return [s_prime, s_sturm]



def calibrate_thresholds(T: int, W: int, hop: int, span: int = 5):
    A = build_A(T)
    duty = float(np.mean(A[0]))

    Cc = build_C_comb(T, duty, span=span)
    Cq = build_C_quasi(T, duty, span=span, shift_frac=0.15)

    S_Cc = np.array([min_windowed_sf(s, W, hop) for s in Cc])
    S_A = np.array([min_windowed_sf(s, W, hop) for s in A])


    lo = float(np.quantile(S_Cc, 0.99))
    hi = float(np.quantile(S_A, 0.01))

    if lo >= hi:
        raise ValueError(f"No feasible tau interval: [lo={lo:.3f}, hi={hi:.3f}]
— adjust W/hop/statistic or families")

    tau = (lo + hi)/2.0   # simplest choice




                                          7
        comb_Cq = np.array([cepstral_combness(s) for s in Cq])
        theta = float(np.quantile(comb_Cq, 0.99))

        return dict(duty=duty, tau_interval=(lo, hi), tau=tau, theta_comb=theta)


5.8 Monitor evaluation


 def evaluate_gate(s: np.ndarray, W: int, hop: int, tau: float, theta_comb:
 float,
                   borderline_frac: float = 0.03, B_per_window: float = 0.02):
     sfs = windowed_sf(s, W, hop)
     Smin = float(np.min(sfs))

        # overlap-discounted deficit grace
        deficit = (hop/W) * float(np.sum(np.maximum(0.0, tau - sfs)))
        B = B_per_window * len(sfs)

     if deficit > B:
         return dict(pass_gate=False, reason="deficit_budget", Smin=Smin,
 deficit=deficit, B=B)

        if Smin < tau:
            return dict(pass_gate=False, reason="minSF", Smin=Smin, deficit=deficit,
 B=B)

     # Stage 2 only near threshold
     if Smin < (1.0 + borderline_frac)*tau:
         c = cepstral_combness(s)
         if c > theta_comb:
             return dict(pass_gate=False, reason="combness", Smin=Smin,
 combness=c, deficit=deficit, B=B)
         return dict(pass_gate=True, reason="borderline_pass", Smin=Smin,
 combness=c, deficit=deficit, B=B)

        return dict(pass_gate=True, reason="pass", Smin=Smin, deficit=deficit, B=B)




6. Minimal API Sketch (Toolkit)

 class AntiResonanceMonitor:
     def __init__(self, T, W=512, hop=None, span=5):
         self.T = T
         self.W = W
         self.hop = hop or (W//2)




                                           8
            self.span = span
            self.calib = calibrate_thresholds(T, W, self.hop, span=span)

       @property
       def tau_interval(self):
            return self.calib["tau_interval"]

       def check(self, s):
           return evaluate_gate(s, self.W, self.hop, self.calib["tau"],
  self.calib["theta_comb"])


Critical diagnostic: always expose tau_interval . If it is empty, the monitor is ill-posed at that duty/W.




7. Notes on Integration
     • PSMC / band-wise checks: compute SF on band-limited versions of s   ~, then aggregate conservatively
       (min across bands for safety).
     • Ethics hook: treat failures as an audit trigger, not as cohomology equivalence.
     • DRMM selector variation: keep as a separate “lawful sector” constraint; gating monitor only
       addresses resonance/forcing artifacts.




8. Next Validation Checklist
                    ˉ and window sizes W ; verify tau_interval non-empty.
    1. Sweep duties s
    2. Forcing sweeps: show gain-spikiness distributions for accepted vs rejected schedules.
    3. Report ROC/AUC for learned fusion (reporting only).
    4. Move to 2D/3D momentum optimizer analogue.




External References

Spectral flatness

     • MPEG-7 Audio (standard overview; includes spectral features such as spectral flatness /
       AudioSpectralFlatness descriptor). MPEG standards portal.
     • Madhu, N. “Note on measures for spectral flatness.” Electronics Letters (IET), 2009.
     • Open Audio Engineering (OpenAE) feature specification: “Spectral flatness” (geometric mean /
       arithmetic mean definition; sub-band variants).

Cepstrum / harmonic regularity detection

     • Bogert, B. P.; Healy, M. J. R.; Tukey, J. W. “The Quefrency Alanysis of Time Series for Echoes: Cepstrum,
       Pseudo-Autocovariance, Cross-Cepstrum and Saphe Cracking.” In Proceedings of the Symposium on
       Time Series Analysis (ed. M. Rosenblatt), Wiley, 1963.



                                                       9
     • Cepstrum overview reference (definition as inverse FFT of log spectrum; standard citation to Bogert–
       Healy–Tukey).

Contraction / certification foundations

     • Hunter, J. D. “The Contraction Mapping Theorem.” Chapter notes (UC Davis; PDF).
     • Banach fixed point theorem (contraction mapping principle; complete metric spaces; existence/
       uniqueness). Textbook appendix reference.

Small-gain and input–output stability

     • Desoer, C. A.; Vidyasagar, M. Feedback Systems: Input–Output Properties. SIAM Classics in Applied
       Mathematics (2nd ed. 2009; original 1975).
     • Zames, G. “On the input-output stability of time-varying nonlinear feedback systems (Part I).” IEEE
       Transactions on Automatic Control, 1966.
     • Khalil, H. K. Nonlinear Systems. 3rd ed., Prentice Hall, 2002. (Small-gain theorem and finite-gain
       stability concepts.)
     • Megretski, A. “Small Gain Theorem” lecture notes (MIT 6.241).

ML schedule baselines (why comb schedules appear in practice)

     • Smith, L. N. “Cyclical Learning Rates for Training Neural Networks.” arXiv:1506.01186, 2015.

Deterministic aperiodics (ablations / design curve)

     • Peng, L.; Kamae, T. “Spectral measure of the Thue–Morse sequence and the dynamical system and
       random walk related to it.” Ergodic Theory and Dynamical Systems, 2015.
     • Zaky, Z. A. et al. “Performance analysis of Thue–Morse acoustic resonators…” (2025; PMC-hosted
       article).

Note: the references above anchor the signal-processing and control-theoretic components (spectral
flatness, cepstrum, small-gain, contractions) and provide ML context (cyclical/periodic schedules). PIRTM/
DRMM-specific material remains project-specific; this section documents the external mathematical and
engineering lineage.


Citizen Gardens © 2025 CC-NC-ND 4.0




                                                     10

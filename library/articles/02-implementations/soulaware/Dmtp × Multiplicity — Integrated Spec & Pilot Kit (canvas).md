---
slug: dmtp-multiplicity-integrated-spec-pilot-kit-canvas
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "02-implementations/soulaware/Dmtp \xD7 Multiplicity \u2014 Integrated Spec\
    \ & Pilot Kit (canvas).md"
  last_synced: '2026-03-20T17:17:15.675662Z'
---

DMTP × Multiplicity — Integrated Spec & Pilot Kit
Version: 1.0
Date: Nov 26, 2025
Owner: Multiplicative




Bottom line (brutal)
     • Workshop (DMTP): Useful now. Run safely with clear boundaries.
     • Math layer (primes, Λm, δ_eth, PMDM, resonance): UNPROVEN. It must pass ablation + outcome
       links or be sunset.

Kill-switch thresholds (must meet): - Prime advantage: ΔAUC(Prime − best baseline) ≥ 0.05 (held-out).
- Parts decoding: weighted F1 ≥ 0.55 (held-out).
- External validity: ρ(Δδ_eth, ΔPANAS-N) ≥ 0.4.
Fail ≥ 2 ⇒ drop math layer; keep workshop.




Quick start
    1. Capture a session per protocol (phones as IMUs + video; optional HRV).
    2. Annotate parts via micro-annotations (exile/manager/firefighter/none).
    3. Run analysis (ablation, δ_eth, Λm, coherence).
    4. Report KPIs: contraction factor, resonance R, coherence index, decision gates.




Glossary (working definitions)
     • DMTP: Dance Me Through the Panic; tango-based, trauma-informed practice integrating IFS.
     • IFS parts: Exiles, Managers, Firefighters; Self (qualities: calm, clarity, confidence, compassion,
       courage, creativity, connectedness, curiosity).
     • Multiplicity: operator calculus that treats parts as prime-labeled modes; includes Λm (multiplicity
       drive), δ_eth (lawfulness functional), and PMDM (polymorphic multiplicity density matrices).
     • Resonance (R): fit score of an operator word to observed data (0–1).
     • Contraction factor (q): safety indicator, q = 1 − ε + c < 1 (stable) with small-gain bounds.




System overview (two-layer stack)
Layer 1 — Practice: DMTP session structure (baseline → priming → dance blocks → reframe → post-
baseline) with micro-annotation of parts.




                                                     1
Layer 2 — Math/Telemetry: Latent state, operator words (lead–follow order), Λm small-gain safety, δ_eth
coherence, PMDM mixtures, resonance fit, ablation vs baselines.




Mathematical specification

1) State, observation, and basis

      • Time lattice: beats/frames Tn = {0, 1, 2, … }.
      • Latent state: xt ∈ Rm , coordinates for putative “parts modes.”
      • Observation: yt = Cxt + ηt , with feature vector yt from IMU/video/HRV.
      • Basis choices (ablation): Prime BP , Random orthonormal BR , Fourier BF , Wavelet BW , Learned
       dictionary BL .
      • Projection: xt = B ⊤ ϕ(yt−W :t ), where ϕ is a feature map on a short window.

2) Dynamics and small-gain safety

Update (discrete time):


                                     Xt+1 = Ξ(t)Xt + Λm (t) T (Xt ) + ξt ,

with ∥Ξ(t)∥2 ≤ 1, T locally Lipschitz (LT = supt ∥JT (t)∥2 ), and scalar drive Λm (t).


Safety invariants (required per block):


                  sup ∥Ξ(t)∥2 ≤ 1 − ε,       LT < ε,    c := sup ∣Λm (t)∣ < ε,     ε ∈ (0, 1).
                    t                                          t

Then the contraction factor q = 1 − ε + c < 1, yielding bounded trajectories and geometric decay of
deviations. If any invariant fails ⇒ UNPROVEN; slow tempo, insert Self-led breathwork, reduce coupling
until invariants hold.


3) Lawfulness functional (δ_eth)

Use a convex, operational form:


                                 δeth (x) = x⊤ Lx + μ ∥x∥1 ,       L ⪰ 0, μ > 0.

- x⊤ Lx: quadratic “conflict energy” (e.g., manager↔exile antagonism).
- μ∥x∥1 : sparsity (fewer parts strongly active).
Goal: δeth decreases within-session and correlates with reduced PANAS-N (external validity).


4) Multiplicity drive (Λm) and regularizer

Define sliding activation counts Mt (k) for coordinate k :




                                                       2
                                                m                   −1
                                 Λm (t) = ( ∑ Mt (k) p−α
                                                      k ) ,              α ≈ 1.0.
                                               k=1

- pk : prime tag for mode k (Prime basis); ignored for non-prime baselines.
- Penalty: RΛm (t) = ∣Λm (t) − 1∣ (target 1 for stable recursion).
- Safety: enforce c = supt ∣Λm (t)∣ < ε.


5) Mixed/overlapping parts: PMDM

Represent blends in a sector p with a polymorphic mixture:


                              ρp (t) = ∑ wi ρp,i (t),          ∑ wi = 1, wi ≥ 0.
                                          i                     i

Unitary actions Upk gate sector dynamics: Upk ∣pk ⟩ = eiθ ∣pk ⟩.


6) Operator words (lead–follow order matters)

Define noncommuting operators per sector/level: subdivision Sp,r , rotation Rp,r , accent Ap,r , walk/
permutation Wp , projectors Πrp , event spikes Δrp .
Word: W = Wp1 ∘ Ap2 ∘ Rp3 ∘ ⋯.
Test: ablate lead↔follow (swap order) and measure ΔR. If ΔR ≈ 0 ⇒ noncommutativity claim is
UNREALISTIC for the data.


7) Resonance functional (R)

                   ^ (candidate word) to channels yc :
Operational fit of O

                                                       C
                                   ^ ; D) = 1 ∑ corr(yc , y^c (O
                              R(H, O                           ^ ))2 ∈ [0, 1].
                                            C c=1

Use R to select phrases and to quantify improvement after re-ordering.


8) Π-kernel update (per-part control)

Let coefficients cπ,t = Rπ xt with neighbors N (π). Proximal, nonexpansive update:


                   cπ,t+1 = (1 − απ )cπ,t + απ Pπ,t (Uπ,t ({cπ′ ,t }π′ ∈N (π) )),   0 < απ ≤ 1.

Stacked form ct+1 = Kt ct + ft with small-gain bounds gives a quadratic Lyapunov descent when safety
invariants hold.




Validation plan (2-week sprint)
      • n ≈ 12, two sessions (Day 0, Day 7).




                                                           3
    • Primary pass: Prime ΔAUC ≥ 0.05 and (H2 or H3): Δδeth ↓ pre→post or ρ(Δδ_eth, ΔPANAS-N) ≥ 0.4.
    • Stopping: fail ≥ 2 primary gates ⇒ sunset math layer.

Metrics (operational)

    • Cadence entropy: H = − ∑i pi log pi on inter-step intervals.
                                       1
    • Phase-locking value: PLV = N       ∑t ei(ϕlead −ϕf ollow ) .
    • Protector–Exile coupling: argmax lag of cross-correlation and its magnitude.
    • Lawfulness dwell: fraction of time δeth (xt ) ≤ ϵ.




Data schema (per-frame)

                    column                    type       description

                    participant_id            string     pseudonymous ID

                    session_id                int        0=Day0, 1=Day7

                    timestamp                 float      seconds from start

                    step_interval             float      seconds between steps

                    turn_rate                 float      rad/s

                    lin_vel                   float      m/s

                    ang_vel                   float      rad/s

                    jerk                      float      m/s^3

                    pause_density             float      proportion in 5s window

                    phase_continuity          float      [0,1]

                    pose_smoothness           float      1 − RMSE(keypoint velocity)

                    hr                        float      BPM (optional)

                    hrv                       float      RMSSD (optional)

                    event_label               string     none

                    cue_tempo                 float      BPM issued

                    cue_pause                 int        0/1

                    cue_figure_class          string     basic

                    cue_embrace_pressure      float      0–1




                                                     4
Code snippets (Python)

δ_eth and Λm


 import numpy as np

 def delta_eth(x_series, L=None, mu=0.01):
     X = np.asarray(x_series)
     m = X.shape[1]
     if L is None:
         L = np.eye(m)
     quad = np.einsum('ti,ij,tj->t', X, L, X)
     l1 = mu * np.sum(np.abs(X), axis=1)
     return quad + l1 # per-timepoint

 def lambda_m(x_series, primes, alpha=1.0, thresh=0.1, window=250):
     X = np.asarray(x_series)
     mags = np.abs(X)
     act = (mags >= thresh).astype(int)
     out = []
     for t in range(len(X)):
         s = max(0, t - window)
         M_counts = np.sum(act[s:t+1], axis=0)
         denom = np.sum(M_counts * (np.power(primes, -alpha)))
         out.append(1.0 / max(denom, 1e-8))
     return np.asarray(out)


Ablation (Prime vs baselines) & encoder


 from sklearn.model_selection import KFold, StratifiedKFold
 from sklearn.pipeline import make_pipeline
 from sklearn.linear_model import LogisticRegression
 from sklearn.preprocessing import StandardScaler
 from sklearn.metrics import roc_auc_score, f1_score

 def train_part_encoder(X, y):
     pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
     pipe.fit(X, y)
     return pipe

 def evaluate_encoder(pipe, X, y, folds=5):
     skf = StratifiedKFold(n_splits=folds, shuffle=True, random_state=42)
     scores = []
     for tr, te in skf.split(X, y):
         pipe.fit(X[tr], y[tr])




                                          5
         yhat = pipe.predict(X[te])
         scores.append(f1_score(y[te], yhat, average='weighted'))
     return np.mean(scores), np.std(scores)

 def ablation_auc(X, y, bases_dict):
     results = {}
     for name, B in bases_dict.items():
         Xproj = X @ B
         aucs = []
         kf = KFold(n_splits=5, shuffle=True, random_state=42)
         for tr, te in kf.split(Xproj):
             enc = train_part_encoder(Xproj[tr], y[tr])
             proba = enc.predict_proba(Xproj[te])
             K = proba.shape[1]
             aucs_k = [roc_auc_score((y[te]==k).astype(int), proba[:,k]) for k in
 range(K)]
             aucs.append(np.mean(aucs_k))
         results[name] = (np.mean(aucs), np.std(aucs))
     return results


Coherence metrics


 from scipy import signal

 def cadence_entropy(step_intervals, bins=10):
     s = np.asarray(step_intervals)
     s = s[np.isfinite(s) & (s>0)]
     if len(s) < 5: return np.nan
     hist, _ = np.histogram(s, bins=bins, density=True)
     p = hist[hist>0]
     return -np.sum(p*np.log(p))

 def phase_locking_value(lead_phase, follow_phase):
     z = np.exp(1j*(np.asarray(lead_phase)-np.asarray(follow_phase)))
     return np.abs(np.mean(z))

 def xcorr_lag(a, b, fs=50.0):
     a = np.asarray(a); b = np.asarray(b)
     corr = signal.correlate(a - a.mean(), b - b.mean(), mode='full')
     lags = signal.correlation_lags(len(a), len(b), mode='full')
     idx = np.argmax(np.abs(corr))
     return lags[idx]/fs, corr[idx]




                                          6
Π-kernel (pseudocode)


 Given coefficients c_pi,t and neighbor set N(pi):
 For each time t:
   for each atom pi:
     u = U_pi,t({c_pj,t for pj in N(pi)})          # proposal
     z = P_pi,t(u)                                 # proximal (nonexpansive)
     c_pi,t+1 = (1 - alpha_pi)*c_pi,t + alpha_pi*z
 Check small-gain conditions; if violated, reduce alpha_pi or insert stabilizer.




Protocol & facilitator checklist (summary)
    • Pre: consent; attach IMU; frame camera; HR strap optional; start baseline (5 min stand + 3 min walk).
    • IFS priming (5–10 min): explain parts as metaphors; participant names 1 exile + 1 protector.
    • Dance blocks (3 × 6 min): Block1 embrace/basic; Block2 pauses/weight shifts; Block3 ochos/turns;
      issue tempo/figure cues; ≤6 annotations per block.
    • Reframe (4–6 min) → Post baseline (8 min) → Surveys (SUDS, PANAS) → schedule 48h check-in →
      backup data.
    • Safety: immediate stop on distress; no diagnostic interpretations; cues are invitations.




Consent (one-page, minimal)
    • Research on movement and attention; not therapy.
    • You may stop or skip any activity; withdraw within 48h; no penalty.
    • Data pseudonymous; video used only for features; deletion after analysis (~3 months).
    • No diagnostic conclusions.




KPIs & reporting
    • Contraction factor: verify q = 1 − ε + c < 1 per block.
    • Resonance R: show increase after operator re-ordering / Self-first phrases.
    • Coherence index: cadence entropy ↓, PLV ↑, protector–exile lag ↓.
    • Ablation table: AUC(mean±sd) for Prime/Random/Fourier/Wavelet/Learned.
    • External validity: ρ(Δδ_eth, ΔPANAS-N).
    • Decision: [Math Works] / [Workshop Only] / [All Noise].




                                                    7
Config (YAML snippet)

 cv_folds: 5
 min_f1: 0.55
 prime_advantage_auc: 0.05
 delta_eth_corr_threshold: 0.4
 alpha_lambda_m: 1.0
 lambda_reg: 0.1
 epsilon_lawfulness: 0.15
 window_seconds: 5.0
 tempo_jitter: 0.05
 random_seed: 42




Roadmap & TRL
     • DMTP container: TRL 6–7 (run now).
     • Math layer: TRL 2–3 → 3–4 in 2 weeks if gates pass.
     • Next: multi-site replication; pre-registration; blinded raters for qualitative clips (optional).




Caveats (hard constraints)
     • Convergence claims require safety invariants; otherwise UNPROVEN.
     • If Prime loses to baselines, drop primes.
     • Treat all metrics as signals, not diagnoses.
     • Publish nulls; no p-hacking; ablation and thresholds pre-specified.




Appendix A — Decision matrix

                               Prime
 Outcome                                       Parts F1        δ_eth vs Outcomes     Action
                                Basis

 Math engine                ΔAUC ≥
                                                 ≥0.55                   ρ ≥ 0.4     PROCEED (scale study)
 works                         0.05

 Workshop is the                            borderline/              δ_eth tracks    SUNSET MATH; keep
                                  fail
 thing                                              fail               outcomes      workshop

 All noise                        fail            <0.55                   no link    STOP integration




                                                           8
Appendix B — Example CLI flow

 # 1) Put raw CSVs in data/raw and annotations in data/annotations
 # 2) Configure thresholds in config.yml
 python analysis/analysis_template.py > out.txt
 # 3) Fill report_template.md using out.txt summary




                                        9

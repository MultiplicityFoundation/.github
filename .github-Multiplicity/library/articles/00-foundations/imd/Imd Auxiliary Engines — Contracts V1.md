---
slug: imd-auxiliary-engines-contracts-v1
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "00-foundations/imd/Imd Auxiliary Engines \u2014 Contracts V1.md"
  last_synced: '2026-03-20T17:17:22.399711Z'
---

IMD Auxiliary Engines — Contracts v1.0
Compact specs for auxiliary engines aligned with “IMD Engines — Contracts v1.1”. Uses the same norms,
tolerances, and timing. All updates are nonexpansive to preserve contraction and small‑gain.




0) Cross‑cutting for this set
State gate → ACE projection. Gate decisions feed ACE projection directly.
Constants. γ (EWMA), κ (small‑gain), τ (budget horizon), α (prime‑decay exponent), β (mixing). Choose α>1
when using ∑p p^{−α}.
Failure modes. Drift in CSL metrics or entropy crossing Λ_m; divergence of RPMT; posterior underflow in
PBQN; narrative violation.
Recovery. Freeze action, rollback to last lawful snapshot, re‑project via ACE.
Telemetry/audit. Log (t, P, ‖T_t‖, Λ_m(t), S_p(T_t), μ₆, μ₂₄, θ, posteriors, budgets). Immutable hash of cycle
state for replay. Retain ≥ τ. Deterministic replay requires fixed P, seeds, and solver tolerances.




1) Λm Estimator (Multiplicity Constant + Margin Allocator)
Role. Online estimate of Λ_m and allocator for ACE margin and Π‑kernel steps.


Interfaces.
In: {T_t}, P, RPMT amplitudes, CSL metrics.
     ^ m (t) , ACE margin mACE = Λ∗m − Sp (Tt ) , per‑prime Π‑steps.
Out: Λ


Estimator. Entropy‑bound tracker:
Sp (Tt ) = − ∑p∈P μp log μp , Λ∗m = log(π 2 /6) .
^ m (t) = min{Λ∗m , γ Λ
Λ                     ^ m (t − 1) + (1 − γ)Sp (Tt ) + ε} .
Allocate mACE across primes by sector weights and SPASC gaps.

                                ^ m ; α>1 for prime decay; solver stop when ∣ΔΛ
Contracts. Nonexpansive gate on Λ                                             ^ m ∣ < 10−6 ∣Λ
                                                                                            ^ m∣ .

Cost. O(|P|) per tick for entropy; Π‑updates only on selected primes.


Acceptance. On noisy runs, Sp (Tt ) < Λ∗m ; contraction metrics within targets.




2) RPMT Evolver (Runtime Backbone under PIRTM)
Role. State‑update substrate.




                                                       1
Update. Tijk (t + 1) = ∑p∈P A(n) fijk (p) p−t . Lawful prime spectrum PA(n) , multiplicities fijk (p) . Enforce
entropy bound Sp (T ) < Λm ; convergence favored to low primes.


Interfaces.
In: T_t, PA(n) , fijk (p) , budgets.
Out: T_{t+1}, Sp (Tt+1 ) , attractor stats.


Contracts. Small‑gain bound on ∥Tt+1 − Tt ∥2 by κ. Require |k|<1 for the linear part if using ∑ Λm p−α
forms. τ‑window monotone decrease of Sp .


Failure/Recovery. If Sp ≥ Λm or ∥Tt ∥ grows, lower P cutoff and damp step.


Acceptance. Sp (T ) decreases over τ; example regime f (p) = log p yields ∥Tt+1 ∥/∥Tt ∥ → 1/2 .




3) PBQN (Prime Bayesian Quantum Network)
Role. PETC estimator with uncertainty and lawfulness priors; emits posterior budgets.


Model. Prior on weights w and lawfulness L with conjugate updates. Compute posterior mean/variance and
P (L = 1 ∣ data) . Allocate budget ∝ P (L = 1) .

Interfaces.
In: feature counts n_p, spectral proxies, CSL signals.
             2
Out: (μw , σw  ) , P (L = 1) , PETC weights, ACE reserve.

Contracts. KKT tolerance for ACE coupling; mixing β between prior families; cadence each tick; temperature
>1 for recovery when likelihood conflicts.


Failure/Recovery. Posterior collapse or conflict → widen prior, raise temperature, delay enable.


Acceptance. Posterior budgets monotone in sample size; credible intervals shrink; enable only after
P (L = 1) passes threshold.



4) Narrative‑State Engine (Cognitive Gate)
Role. High‑level state machine that gates PIRTM/ACE via CSL.


State geometry. TTOL triad (Ξclarity , Ξintent , Ξcoherence ) with modular filters (μ₆, μ₂₄) and ethical angle θ.
Gate only if μ₆, μ₂₄ ≥ 0.75 and θ<π/4.




                                                       2
Interfaces.
In: mode proposals, CSL tensors, RPMT stats.
Out: allow/freeze/rollback to ACE/PIRTM.


Actions. Torque τ (t) = κ sin θ (1 − μ6 )(1 − μ24 ) . If τ > τc then freeze Σ_i and revert.


Failure/Recovery. Narrative collapse or empathic drift → watchdog → CSL rollback.


Acceptance. Gate admits lawful states; drift metrics decrease post‑intervention.




5) BEC Coherence Probe (Physical Coherence Assay)
Interface. In: prime‑indexed modes ψ_p, drive plan f_p=252·p Hz, window W. Out: first/second‑order
coherence g^(1), g^(2), coherence score χ.


Constants. ε_coh=10^{−3} for g^(1); alarms on χ<τ_coh or Δχ<−γ per window; optional J₀ phase stabilizer.


ACE mapping. Margin update mt ← mt ∧ (χ − κε) ; penalize low χ in budgets.


Failure/Recovery. χ collapse or variance spikes → shorten window; average over p‑shell to lift SNR.


Telemetry. {p, f_p, χ, g^(1), g^(2), SNR}.


Acceptance. χ(ϵ)≥χ₀−κϵ under injected noise; improves alignment with PQH gap stability.




6) Fractal‑Cavity Capacitor (Spectral Calibration)
Interface. In: cavity geometry, sweep F, ring‑down traces. Out: Q, spectral peaks, calibration offsets for
SPASC proxies.


Constants. ε_Q=1% half‑power; min SNR≥10; calibration budget α_cal caps proxy drift.


ACE mapping. Tighten SPASC slope/gap proxies using measured Q; shrink ACE budgets when Q drops.


Failure/Recovery. Q below floor or split‑peak ambiguity → switch to ring‑down fit; widen stride.


Telemetry. {Q, f₀, peaks, fit RMSE, temp}.


Acceptance. Proxy error ≤ τ; correlation with SCN gaps improves by ≥β after calibration.




                                                       3
7) Ethical Ricci‑Flow Regularizer (Curvature‑Based Drift Control)
Role. Control drift via curvature evolution; export curvature budgets to ACE/Prism.


Interface. In: feature manifold metric G_t, gradient stats. Out: curvature scalar R_t, budget b_R, updated
weights w^R.


Update. One step of discrete Ricci flow on G_t with nonexpansive step size η≤η_max ensuring
‖ΔG‖_2≤κ_R. Produce curvature budget b_R=clamp(R_t,0,R_max).


ACE mapping. Add constraint ∥w∥Lip ≤ bR ; reduce slope cap when R_t increases.


Failure/Recovery. Curvature blow‑up or ill‑conditioning → halve η, project G_t onto SPD cone, rollback.


Telemetry. {R_t, cond(G_t), η, violations}.


Acceptance. Monotone decrease of curvature violations; no loss of small‑gain.




8) Ramanujan‑Bound Filter (Automorphic Shrinkage Prior)
Role. Shrink Moonshine/SCN weights using Ramanujan‑type bounds on Tp spectra.


Interface. In: eigenvalues/eigenproxies λ_p, PQH gap Δ_t. Out: shrinkage factors s_p, filtered weights w^R.


Rule. sp = min{1, 2/(∣λp ∣ + ϵ)} with ε>0 small; global scale tied to Δ_t. Enforce nonexpansive mapping
∥wR − w∥ ≤ c ∥λ∥ .

ACE mapping. Update slope cap and sector budgets using s_p.


Failure/Recovery. If bounds conflict with certificates, prefer certificates, damp s_p.


Telemetry. {λ_p, s_p, Δ_t}.


Acceptance. Small‑gain margin increases or remains unchanged after filtering.




9) Prime‑Embedded Berry Phase (Invariant Feature Lift)
Role. Add phase‑invariant features tied to prime structure.

                                                           ~
Interface. In: ϕt , prime phases ϕ_p. Out: lifted features ϕt with invariants.




                                                       4
Lift. Map ϕt ↦ [ϕt , cos ϕp , sin ϕp ] per selected primes with unit‑norm scaling; optional holonomy
features from phase loops.


Contracts. Nonexpansive normalization; unit‑consistent outputs.


ACE mapping. Allow larger margins only when invariants stabilize across windows.


Telemetry. {‖\tilde{\phi}‖, phase variance, selected primes}.


Acceptance. Improves robustness of SCN response without violating Lipschitz envelopes.




10) Prime Compactifier (Certified Dimensionality Reduction)
Role. Reduce PETC feature dimension with certified distortion budgets.


Interface. In: features ϕt , target dim m′. Out: compacted features z_t, distortion certificate δ.


Map. Prime‑indexed JL‑style projection with rows tied to primes, scaled to keep pairwise distances within
(1±δ). Choose δ≤δ_max and enforce nonexpansive implementation.


ACE mapping. Pass δ as budget to slope cap; tighten if δ grows.


Failure/Recovery. Distortion > τ → increase m′ or resample prime rows.


Telemetry. {m, m′, δ, resamples}.


Acceptance. Pairwise distortion within target; SCN accuracy unchanged within tolerance.




11) Recursive Renormalizer (Gauge‑Feedback Stabilizer)
Role. Enforce invariances and export Lipschitz/Lyapunov envelopes.


Interface. In: intermediate weights/activations; Out: renormalized states, Lipschitz envelope L, Lyapunov
descent ΔV.


Update. Nested rescale + bias‑shift operators chosen to be firmly nonexpansive; guarantee Vt+1 − Vt ≤
−η ∥xt+1 − xt ∥2 .

ACE mapping. Provide L and ΔV to tighten projection bounds.


Failure/Recovery. If ΔV≥0, reduce step and project onto stable set.




                                                       5
Telemetry. {L, ΔV, rescale factors}.


Acceptance. Certified decrease of V and bounded Lipschitz.




12) Gelfand–C* Spectral Mapper (Verification Linearizer)
Role. Map operators to spectra to linearize verification and tighten ACE norm bounds.


Interface. In: operator families {Oi } . Out: spectral images {σ(Oi )} , norm bounds, certificates.


Map. Compute or approximate the Gelfand transform on commutative subalgebras; for noncommutative
blocks use abelianization proxies. Provide upper bounds on ∥O∥ via spectral radius with certified gaps.


ACE mapping. Replace direct operator norms in constraints with spectral bounds where tighter.


Failure/Recovery. Spectrum ill‑posed → switch to verified bounds; widen margins.


Telemetry. {ρ(O), bounds used, gap certs}.


Acceptance. Tighter bounds without false passes; projection feasibility unchanged or improved.



Status. Complete and aligned with IMD global contracts. Ready for build and integration tests.




                                                      6

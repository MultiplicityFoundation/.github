---
slug: imd-engines-contracts-v1
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "00-foundations/imd/Imd Engines \u2014 Contracts V1.md"
  last_synced: '2026-03-20T17:17:22.232618Z'
---

IMD Engines — Contracts v1.1 (with fixes)
A compiled, implementation-ready specification for the six priority engines and cross-cutting controls in the
IMD stack.




0) Overview
Stack: ACE (safety) · PETC (structure) · Langlands Prism (integration) · Moonshine/SCN (control) · SPASC
(modeling) · PIRTM (runtime).
This doc: cross-cutting contracts + six engines with fixed conventions and testable criteria.


Disambiguations:
- κ : modular weight used in Ramanujan bounds.
- ktop : number of top eigenpairs selected in PQH bands.


Global thresholds:
- Relative gap floor Δmin,rel = 0.02 .
- Absolute gap floor Δmin,abs = 10−3 .
- Effective gap floor per tick: Δmin = max (Δmin,abs , Δmin,rel ρ(Ht )) , where ρ(Ht ) is the spectral radius.
- Unfreeze window M = 50 ticks.




1) Cross-cutting contracts

Interfaces (domains / codomains)

     • Features: xt ∈ Rd
     • PQH lift: ϕt = ΠΩ (Ht ) xt ∈ Rm
                                         ^ t ∈ Rd
     • PETC estimator: (xt , ϕt , mt ) ↦ w
     • CSL/Ξ: policy {πi } ↦ (At , bt )
                       ^t ↦ wt ∈ Rd
     • ACE projection: w
     • SCN control: wt ↦ ut ∈ Rk
     • SPASC masks: mt ∈ {0, 1}m
     • PIRTM state: Tt ∈ Rn×n

Units

     • Features, weights, budgets normalized to [0, 1] .
     • Time in seconds. Control period Tc = 20 ms .




                                                       1
Timing and call order (per control tick)

1) PQH build Ht and compute ϕt .
                ^t from (xt , ϕt , mt ) .
2) PETC propose w
3) CSL/Ξ compile policy to (At , bt ) .
               ^t → wt with (At , bt ) .
4) ACE project w
5) SCN act using wt ; SPASC updates mt+1 .
6) Ihara sieve refines mt+1 .
7) PIRTM update Tt+1 = F + KTt .
8) Watchdog evaluates Rt and may intervene.
9) Archivum commits record.


Constants, norms, and parameters

      • γ = 0.05 (target relative gap tightening per Ihara iteration).
      • κ = 2.0 (gap loss coefficient in PQH acceptance).
      • τ = 10−4 (KKT primal–dual tolerance).
      • α = 10−3 , β = 10−2 (SPRT type-I/II).
      • Vector norm ∥ ⋅ ∥2 ; operator norm spectral ∥ ⋅ ∥2 .
      • Lipschitz certificates as product of block spectral norms; SCN unitary blocks L = 1 .

Failure modes

Trigger on any:
- KKT infeasible or gap > τ .
- Δt < Δmin .
- Sato–Tate deviation DT > c/        ∣PT ∣ with c = 1.36 .
- ρ(B) increasing under Ihara updates.
- Rt > Rhigh .


Fallback: margin boost then projection freeze.
Recovery: rollback to last good ledger; gradual unfreeze when Rt < Rlow for M ticks.


Telemetry / audit

      • Per-tick fields: timestamp, RNG seed, ∣PT ∣ , Δt , ∣ΠΩ ∣ , KKT gap, Rt , DT , ρ(B) , SlopeUB, budgets,
        hashes.
      • Include hashes of (At , bt ) , solver options, and library versions.
      • Sampling: every tick; aggregate at 1 Hz.
      • Retention: raw 7 days or 106 ticks; aggregates 90 days.
      • Replay determinism: store RNG seed, solver tolerances, opcode versions, canonical orders; float64
        fixed-precision.

Time budget per tick (fraction of Tc )

PQH 0.40 · PETC 0.10 · ACE 0.20 · SPASC+Ihara 0.15 · PIRTM 0.05 · Watchdog 0.05 · Archivum 0.05.
Log overruns with component attribution.




                                                             2
2) Engine contracts

2.1 Prime Quantum Hamiltonian (PQH)

Purpose: maximal spectral leverage. Hecke/automorphic features drive SCN and SPASC with certified gaps.


I/O:
Ht = ∑p∈PT wp Tp on an automorphic basis; ϕt = ΠΩ (Ht )xt .

Normalization of Tp : choose orthonormal basis; scale Tp ↦ p−(κ−1)/2 Tp so Ramanujan proxy ∣λ(Tp )∣ ≤ 2
holds.


Band rule Ω : select top ktop eigenpairs maximizing instantaneous gap Δt = λktop − λktop +1 , with
ktop = min (64, ⌊0.05 m⌋) .

Projector solver: Lanczos with full reorthogonalization; tol 10−6 ; max 256 iters. Warm-start from Ht−1 . On
failure: widen Ω once; if still failing, reuse last certified ΠΩ .


ACE mapping: slope cap smax = 1/(Δt + ε) , ε = 10−3 . Tighten by Ramanujan proxy factor r =
            2
minp ∣λ(Tp )∣+10−6 : set smax ← r smax .




Compute cost: sparse O(ktop nnz(Ht )) or dense O(ktop m2 ) . Budget ≤ 0.40 Tc .


Certificates: Weyl-gap lower bound; Ramanujan proxy; small-gain ∥G∥∞ ∥K∥∞ < 1 .


Tests: noisy-gap stability Δ(ε) ≥ Δ0 − κε ; SCN Lipschitz envelope LSCN ∥ΠΩ ∥ < 1 .




2.2 CSL/Ξ Governor

Purpose: compile policy into hard projection constraints that ACE can certify.


I/O: clauses πi ↦ C = {w ∈ Rd : Aw ≤ b} .


Policy grammar → convex (A, b) :
- Box: wi ∈ [ℓ, u] .
- Sparsity: ∥w∥1 ≤ s or group-ℓ1,2 on groups {Gj } .
- Monotone: Dw ≥ 0 .
- Budget: ∥w∥1,α ≤ B with weighted ℓ1 .


Conflict resolution: Ξ-priority; drop lowest-priority clauses until feasible; log evictions.


Feasibility restore: homotopy on budgets B → ηB , η ↓ 0.9 until feasible or floor.




                                                           3
ACE program and KKT:
min ∥w∥1 s.t. Aw ≤ b and slope-cap smax .
Stationarity ∥∇f (w) + A⊤ λ∥∞ ≤ τ , primal–dual gap ≤ τ , λ ≥ 0 , λ ≤ λmax = 103 .


Cadence: re-project every tick; full recompilation on policy change or every 50 ticks.


Tests: adversarial policy fuzzing; feasibility margin minw∈C ∥Aw − b∥+ stays above target.




2.3 Archivum Ledger

Purpose: bind PETC proposals to ACE proofs with integer ledgers and sector weights.


Schema:
(t : u64, p : u32, hash(xt ) : bytes32, w^t : float64[d], ACE_certt : bytes, M  ^ ∧ (T , p) :
float64, hash(At , bt ) : bytes32, solver_opts : bytes, lib_versions : bytes) .

Security: SHA-256 content hashes; Ed25519 signatures; per-record Merkle leaf; chain via prev-hash. Key
rotation every 106 ticks or 30 days (keep last 3 for verify-only).


Replay determinism: store RNG seed, tolerances, op-order; verify by byte-wise equality of wt and certs;
mismatch threshold 0.

                         ^ ∧ (T , p) = 1 within 10−12 .
Conservation: enforce ∑p M
Budget monotonicity: cumulative spend non-decreasing; any decrease requires governance flag.


Tests: replay audit reproduces ACE projection (mismatch 0); divergence bounds between ledger and in-
memory model.




2.4 Sato–Tate / Frobenius Sampler

Purpose: automate spectral diagnostics used by SPASC.


Provenance of ap : from the automorphic lift or learned L-function module; clamp ap ∈ [−2        p, 2 p]
before arccos .


Prime schedule PT : sliding window [pmin , pmax ] with pmin = 101 ; geometric stride 1.2; target ∣PT ∣ =
128 ± 16 .

Estimator: θp = arccos(ap /(2     p)) ; histogram with B = 32 equal-width bins on [0, π] .
DKW constant: c = 1.36 (5%). Alarm if DT > c/       ∣PT ∣ .

Hysteresis: require two consecutive alarms to change SPASC/ACE settings; cool-down 10 ticks.




                                                       4
Feed: on alarm, SPASC increases mask sparsity; SlopeUB tightened by ×0.9; confidence bands passed to ACE
as slope caps.


Tests: deviation DT below control limit in nominal conditions; proxy–SCN eigen-gap correlation above
threshold.




2.5 Ihara–Graph Zeta Sieve

Purpose: gap-based partitioner for SPASC masks and slope bounds.


Graph construction: nodes = feature atoms; edge weight wij = cosine similarity of ϕt channels; threshold
at 0.2; zeta uses unweighted edges.


Solvers: build non-backtracking B ; power method for ρ(B) (tol 10−4 , max 200 iters). For normalized
Laplacian L , compute (λ1 , λ2 ) via Lanczos (tol 10−6 ).


Mask monotonicity and termination: let m = 1 mean “kept.” Update is monotone non-increasing: drop
edges/nodes that raise ρ(B) or reduce λ1 − λ2 . Each accepted step strictly decreases ρ(B) or increases
λ1 − λ2 by at least γ fraction; finite termination follows.

Cheeger link: use normalized-Laplacian bound hG ≥ λ2 /2 .
Gap target: per-iteration improvement (λ1 − λ2 )t+1 ≥ (1 + γ)(λ1 − λ2 )t until stop.


Tests: Algorithm-1 loop tightens gap by ≥ γ per accepted iteration; SlopeUB monotonically decreases until
stop.




2.6 Watchdog + OMEGA Node

Purpose: real-time safety trip before failure.


Risk metric:

                             ∥Tt+1 − Tt ∥2      Δmin − Δt        DT          spendt
                   Rt = w1                 + w2           + w3          + w4
                              ∥Tt ∥2 + ε        Δmin + ε       c/ ∣PT ∣      budgett

with w = (0.35, 0.35, 0.20, 0.10) , ε = 10−9 . Normalize spend as fraction of the current budget epoch
(clipped to [0, 1.5]) ).


Hysteresis: Rhigh = 1.0 , Rlow = 0.7 , window 5 ticks.


SPRT: log-LR on standardized increments of Rt .
                       1−β                   β
Thresholds: A = ln α ≈ 6.90 , B = ln 1−α ≈ −4.61 .
Design target: with DKL ≥ 0.5 , E[Tdetect ] ≲ A/DKL ≈ 14 ticks ≤ 15 Tc .




                                                        5
Actions: 1) margin boost smax ← 0.8 smax ; 2) projection freeze (hold wt ); 3) rollback to last good ledger
tick.
Delay bound: ensure DKL ≥ 0.5 by calibration; otherwise relax (α, β) or widen evidence window.


Tests: bounded-perturbation injections trip within target delay while small-gain is preserved.




3) Minimal acceptance checks
     • PQH: Δ(ε) ≥ Δ0 − κε on noisy runs; Δt ≥ Δmin .
     • CSL: minw∈C ∥Aw − b∥+ above target under fuzzed policies; convexity preserved.
                                                    ^ ∧ (T , p) = 1 ; version/hash fields present.
     • Archivum: replay mismatch 0; conservation ∑p M
     • ST/Frobenius: DT below control limit nominally; proxy–SCN gap correlation above threshold;
       hysteresis prevents flapping.
     • Ihara: mask monotone non-increasing; SlopeUB decreases each accepted step; termination in finite
       steps.
     • Watchdog: trips under bounded perturbation within ≤ 15 Tc ; small-gain condition remains
       satisfied.




4) Glossary of symbols
     • κ : modular weight in Ramanujan scaling.
     • ktop : number of eigenpairs in Ω .
     • Δt : eigen-gap λktop − λktop +1 .
     • Δmin : max(Δmin,abs , Δmin,rel ρ(Ht )) .
     • ρ(B) : spectral radius of non-backtracking matrix.
     • DKW constant c = 1.36 .
     • SPRT levels α = 10−3 , β = 10−2 ; thresholds A ≈ 6.90 , B ≈ −4.61 .
     • Unfreeze window M = 50 ticks.



Status: Ready for implementation.




                                                      6

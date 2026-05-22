---
slug: psmc-v4
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/PSMC V4.md
  last_synced: '2026-03-20T17:17:21.597045Z'
---

PSMC v4.1 (Final) — Formal Specification,
Experimental Protocol, and Reporting
0. What this document is
This document formalizes the final PSMC v4.1 design and the reviewer-proof experimental protocol
developed across iterations. It focuses on what is now fixed and frozen:


     • Mechanism: bandwise damped updates in the frequency domain with scheduled band activation.
     • Claim under test: whether deterministic aperiodic schedules (prime-derived) reduce tail update
       norms under periodic additive forcing, relative to matched random baselines (same period
       distribution).
     • Methodology: airtight pairing (init, data order, RNG snapshot), per-base-schedule analysis, seed-key
       intersection pairing, and global FDR.

       Note: This doc formalizes the framework and how to report results. It does not invent
       numerical outcomes.




1. Final mechanism (PSMC band engine)
Let xt ∈ Rd be a flattened parameter vector and gt its gradient (possibly forced).


     • Compute rFFT: X = rfft(xt ), G = rfft(gt ).
     • Partition rFFT frequencies into disjoint dyadic bands with masks Mj (including DC band j = 0).
     • Each band has a period hj and phase ϕj . Band j is active at step t iff (t + ϕj ) mod hj = 0.
     • DC band is always active: h0 = 1, ϕ0 = 0.

Per active band j , compute a damped affine update in FFT space:


                         Uj = Mj ⊙ ( − η G − (1 − aj )X + (optional noise))

Aggregate across active bands:


                                                U = ∑ Uj
                                                     j∈At

Normalize: - compute_fair: U ← U /∣At ∣ - flow_fair: U ← U ⋅ min (E[∣A∣]/∣At ∣, smax )


Finally, update in parameter space:


                                  Δxt = irfft(U ),        xt+1 = xt + Δxt




                                                      1
Key invariants frozen in v4.1 - Local RNG only inside schedule generation (no global RNG pollution). - DC
always active (prevents zero-update steps). - Flow-fair scaling is capped (prevents rare-step explosion). -
Update norms measured in parameter space (∥Δθt ∥) with reshape-safe flattening.




2. Schedules under test
For each base schedule S\in\{\texttt{prime_mod},\texttt{prime_gap},\texttt{prime_density}\}, evaluate:


    1. S (the prime-derived schedule)
    2. \texttt{matched_random_phase}(S) — same periods as S , randomized phases
    3. \texttt{matched_random_permutation}(S) — permuted periods across bands + random phases
    4. random — fully random periods/phases
    5. linear — regular / highly periodic baseline
    6. Optional: \texttt{sobol_phase} — same periods as base, Sobol low-discrepancy phases (clamped)

Primary comparison: S vs matched_random_phase(S).




3. Forcing model (resonance stress-test)
To make resonance measurable and persistent, inject an additive periodic component:

                                                             2πt
                                         gt ← gt + A sin (       )v
                                                              T
     • v is a fixed unit direction per run (and per parameter tensor for MNIST), held constant across
       schedules.
     • T is the forcing period; A is amplitude.




4. Metrics (tail-first, hypothesis-relevant)
Primary per-run scalar metrics computed from the time series ut = ∥Δθt ∥:


     • q95: Quantile0.95 (u)
     • CVaR95: E[ut ∣ ut ≥ q95]
     • max: maxt ut
     • Optional: recovery time after known forcing peaks

Synthetic gate uses a combined summary:

                                                  adv(CVaR95) + adv(max)
                                combined =
                                                            2
where adv(metric) = 100 ⋅ (baseline − schedule)/(baseline + ϵ).




                                                       2
5. Pairing and determinism (airtight protocol)

5.1 What is paired

For each (\text{seed}, T, \text{base_schedule}): - identical initial weights (cloned init_state) - identical batch
order (fixed-order loader) - identical forcing vectors (v_map) - identical RNG streams across schedules
(CPU/NumPy/CUDA RNG snapshot restore)


5.2 Why seed-key intersection is final

All paired tests are performed using seed-key intersection: - build {seed → result} dictionaries - intersect
seeds between schedule and baseline - test only on common seeds


This prevents silent mispairing from missing or duplicated entries.




6. Statistical testing (final)
Within each base schedule and each forcing period T :


      • paired t-test on q95, CVaR95, max vs matched_random_phase

Then apply Benjamini–Hochberg FDR:


      • Per-base FDR: correction across all (period × schedule × metric) tests within that base schedule.
      • Optional cross-base FDR: correction across all base schedules as a separate, stronger claim.

Reporting should clearly state which FDR family is being used.




7. Decision gates

7.1 Synthetic gate (fast falsification)

Run the synthetic quadratic task using the same PSMC engine code path.


Proceed to MNIST only if: - combined advantage mean ≥ 2% for at least one normalization mode.


7.2 Publishable positive

Claim schedule-specific benefit only if: - FDR-corrected p < 0.05 for at least one tail metric and - advantage
≥ 5% in ≥ 2 forcing periods (recommended robustness threshold).


Otherwise, the clean null is still valuable: - “No evidence primes outperform matched random under this
forcing model.”




                                                        3
8. Minimal code excerpt (final patterns)
Below is a compact snippet that captures the final patterns that made the framework airtight:



  import numpy as np
  import scipy.stats as stats
  from statsmodels.stats.multitest import multipletests


  # --- pairing-safe analysis ---

  def perform_paired_analysis(test_data):
      """test_data[T][schedule] = list of dicts with keys: seed,q95,cvar95,max"""
      results = {}

       for T, sched_map in test_data.items():
           if 'matched_random_phase' not in sched_map:
               continue

          baseline_dict = {r['seed']: r for r in
  sched_map['matched_random_phase']}

            for schedule, runs in sched_map.items():
                 if schedule == 'matched_random_phase':
                     continue

                 schedule_dict = {r['seed']: r for r in runs}
                 common = sorted(set(schedule_dict) & set(baseline_dict))
                 if len(common) < 2:
                     continue

                 def paired(metric):
                     a = [schedule_dict[s][metric] for s in common]
                     b = [baseline_dict[s][metric] for s in common]
                     t, p = stats.ttest_rel(a, b)
                     adv = 100.0 * (np.mean(b) - np.mean(a)) / (np.mean(b) + 1e-8)
                     return t, p, adv


                 t_q95, p_q95, adv_q95 = paired('q95')
                 t_cvar, p_cvar, adv_cvar = paired('cvar95')
                 t_max, p_max, adv_max = paired('max')

                 results.setdefault(T, {})[schedule] = {
                     'n_pairs': len(common),
                     'common_seeds': common,
                     't_q95': t_q95,   'p_q95': p_q95,   'mean_adv_q95': adv_q95,
                     't_cvar': t_cvar, 'p_cvar': p_cvar, 'mean_adv_cvar': adv_cvar,




                                                     4
                't_max': t_max,   'p_max': p_max,   'mean_adv_max': adv_max,
            }

    return results



def apply_global_fdr_correction(results):
    pvals, keys = [], [] # keys = (T, schedule, metric)


    for T, sched_map in results.items():
        for schedule, m in sched_map.items():
            for metric in ('q95', 'cvar', 'max'):
                pk = f'p_{metric}'
                if pk in m:
                    pvals.append(m[pk])
                    keys.append((T, schedule, metric))

    if not pvals:
        return results

    _, fdr, _, _ = multipletests(pvals, alpha=0.05, method='fdr_bh')

    for (T, schedule, metric), p_adj in zip(keys, fdr):
        results[T][schedule][f'p_{metric}_fdr'] = float(p_adj)
        results[T][schedule][f'sig_{metric}_fdr'] = bool(p_adj < 0.05)

    return results



# --- per-base-schedule analysis skeleton ---

def analyze_per_base(all_results_by_base):
    """all_results_by_base[base][T][schedule] -> list of run dicts"""
    analysis_by_base = {}

    for base, schedule_results in all_results_by_base.items():
        # build test_data for this base only
        test_data = {}
        for T, sched_map in schedule_results.items():
            test_data[T] = {k: sorted(v, key=lambda r: r['seed']) for k, v in
sched_map.items()}

        analysis = perform_paired_analysis(test_data)
        analysis = apply_global_fdr_correction(analysis)
        analysis_by_base[base] = analysis

    return analysis_by_base




                                       5
9. Reporting template (copy/paste)
When runs complete, report in this structure:


    1. Synthetic gate summary
    2. per normalization mode: mean±std advantage for q95/CVaR95/max/combined

    3. gate pass/fail


    4. MNIST per-base results (separate sections for prime_mod / prime_gap / prime_density)


    5. for each T : q95/CVaR95/max advantages vs matched_random_phase
    6. paired t-test p-values and FDR-corrected p-values

    7. optional cross-base FDR if claimed


    8. Conclusion


    9. If primes ≈ matched baselines: “prime aperiodicity not special under this forcing.”
   10. If primes win under FDR: specify which base schedule(s), which T , and which tail metrics.




10. Final scope statement
What v4.1 definitively provides: a controlled instrument to isolate schedule timing effects on tail behavior
under known periodic forcing.


What v4.1 does not assume: that primes are inherently special. The protocol is designed so a strong null is
still a publishable outcome.




                                                     6

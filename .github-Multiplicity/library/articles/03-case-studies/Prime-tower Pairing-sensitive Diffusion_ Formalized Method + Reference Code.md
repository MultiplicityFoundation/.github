---
slug: prime-tower-pairing-sensitive-diffusion-formalized-method-reference-code
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Prime-tower Pairing-sensitive Diffusion_ Formalized Method
    + Reference Code.md
  last_synced: '2026-03-20T17:17:20.362187Z'
---

Prime‑Tower Pairing‑Sensitive Diffusion
This document compiles and formalizes the developed prime‑tower / pairing‑sensitive multiscale
diffusion framework into a falsifiable computational method, with a “logical ladder” of controls and a
reference implementation skeleton.




1. Core objective
We want to test whether tower structure (row‑wise pairing of multiscale parameters across levels) induces
detectable signatures in a diffusion‑like dynamical system beyond what is explained by:


1) marginal distributions of scales per level, and 2) the distribution of scale ratios rn = sn,2 /sn,1 .


The design goal is a method that remains interpretable under ablations:


     • γ = 0 should ablate any tower‑sensitive signal.
     • αd = 0 should remove pairing sensitivity when the diff term is constructed with clean ablation (no
       per‑diff normalization).




2. Formal model specification

2.1 Graph / state

We work on a 1D ring (periodic chain) with L nodes.


     • State at time t: Tt ∈ RL×d
     • Node index v ∈ {0, … , L − 1}, feature index ℓ ∈ {1, … , d}.

2.2 Gaussian ring kernel

For a scale s > 0, define a normalized Gaussian kernel on the ring:


                                            Δ2
                        Ks (Δ) ∝ exp (−         ),    Δ = min(∣i − j∣, L − ∣i − j∣).
                                            2s2

Convolution is implemented via FFT for efficiency.


2.3 Tower scales

We generate a matrix S ∈ RN ×K where


     • n ∈ {1, … , N } indexes tower rows,




                                                       1
      • k ∈ {1, … , K} indexes tower levels.

Prime‑tower prototype:


                  Sn,k = sfloor + log(1 + h(k) (n)),       h(1) (n) = pn , h(k+1) (n) = ph(k) (n) .

2.4 Level‑aware smoothing kernel

Define a nonnegative smoothing kernel as a level mixture:


      • Within level k : wn,k ∝ exp(α log Sn,k /τ ).
      • Across levels: πk ∝ exp(log Λk /τ ).

                                                       K         N
                                       Ksmooth = ∑ πk ∑ wn,k KSn,k .
                                                   k=1         n=1


2.5 Pairing‑sensitive signed correction (DoG‑like)

A zero‑sum signed correction term depends on paired scales per row:


                                 Δn = KSn,2 − KSn,1 ,                ∑ Δn (Δ) = 0.
                                                                     Δ

Ratio‑weighted diff weights:


                                     ~ ∝ exp (α log r ),                        Sn,2
                                     wn        d     n                   rn =        .
                                                                                Sn,1

Then (clean ablation):

                                                     N  ~ Δ
                                                   ∑n=1 w n n
                                          Kdiff =             .
                                                  ∥∑
                                                     N  ~
                                                       w Δ ∥
                                                           n=1       n    n 2

No per‑n normalization is applied to Δn ; this is critical so that αd = 0 makes pairing sensitivity collapse.


2.6 Combined kernel + spectral rescaling

Total convolution kernel:


                                          Ktotal = Ksmooth + γKdiff .

Let K (ω) be its FFT. Rescale to ensure nonexpansive convolution:


                                            K ← K / max ∣K (ω)∣.
                                                           ω

This provides a rigorous stability handle without clipping signs.




                                                           2
2.7 Dynamics

Define a Laplacian term on the ring:


                                 (ΔT )(v) = T (v + 1) + T (v − 1) − 2T (v).

Update:


                              Tt+1 = tanh (Tt + η ΔTt + (Ktotal ∗ Tt )) + ε ξt ,

where ∗ is circular convolution applied feature‑wise, and ξt ∼ N (0, I).




3. Measurement: prime‑indexed feature curves
A simple feature map is the “prime‑scale energy curve”:

                                             1
                                 Ψp (T ) =     ∑⟨T (v), (Klog(1+p) ∗ T )(v)⟩,
                                             L v

evaluated for the first N primes p. We typically time‑average Ψp over the second half of the trajectory.


       Optional diagnostic extension: compute two blocks of features, one using Ksmooth and one
       using Kdiff , enabling permutation‑importance attribution to “tower correction” vs “base
       smoothing.”




4. The logical ladder of controls
This ladder is the central interpretability device.


Level 0 — Null mechanism

      • γ = 0 (no signed correction)
      • or αd = 0 (diff weights uniform)

Expected: separability ~ chance.


Level 1 — Ratio distribution signal

      • Prime vs pairshuf (destroys pairing; preserves marginals)

Expected: separable when γ > 0 and αd > 0.


Level 2 — Pairing beyond ratio distribution

      • Prime vs ratio‑approximately‑matched shuffle (preserves ratio structure approximately)




                                                       3
Expected: if accuracy collapses, the effect is mostly ratio‑driven.


Level 3 — Recursion‑map specificity

      • Prime vs scrambled recursion (breaks index map; then marginal‑match)

Expected: separation here is the strongest evidence of “prime recursion beyond ratios/marginals.”




5. Interpretation guardrails
1) Avoid kernel clipping for signed corrections. Clipping destroys the DoG‑like mechanism. 2) Prefer
reporting separation ∣acc − 0.5∣ and permutation p‑values on separation. 3) “Ratio‑matched” shuffles are
approximate when N is small; interpret accordingly. 4) Beware degenerate controls (e.g., monotone fib
towers after quantile matching can collapse to prime pairing).




6. Reference code snippets

6.1 Prime utilities


  import numpy as np
  import math

  def prime_sieve(limit: int):
      sieve = np.ones(limit + 1, dtype=bool)
      sieve[:2] = False
      for i in range(2, int(limit**0.5) + 1):
          if sieve[i]:
              sieve[i*i : limit+1 : i] = False
      return np.nonzero(sieve)[0].tolist()

  PRIMES = prime_sieve(300000)

  def nth_prime(n: int) -> int:
       return PRIMES[n - 1]

  def first_primes(m: int):
      return [nth_prime(i) for i in range(1, m + 1)]

  def h_tower(n: int, k: int) -> int:
      idx = n
      for _ in range(k):
          idx = nth_prime(idx)
      return idx




                                                        4
6.2 Ring Gaussian kernel (time domain)


 def gaussian_ring_kernel_vec(L: int, s: float):
     r = np.arange(L)
     d = np.minimum(r, L - r).astype(float)
     k = np.exp(-(d*d) / (2.0*s*s))
     k /= k.sum()
     return k


6.3 Prime tower scale matrix


 def scales_matrix_prime(N: int, K: int, s_floor: float = 1.0):
     S = np.zeros((N, K), dtype=float)
     for n in range(1, N+1):
          for k in range(1, K+1):
               S[n-1, k-1] = s_floor + math.log1p(h_tower(n, k))
      return S


6.4 Correct quantile matching


 def quantile_match(src, tgt):
     src = np.asarray(src)
     order = np.argsort(src)
     out = np.empty_like(src, dtype=float)
     out[order] = np.sort(np.asarray(tgt))
     return out


6.5 Pairing shuffles


 def shuffle_pairings(S, rng):
     N, K = S.shape
     Sp = S.copy()
     for k in range(1, K):
          Sp[:, k] = rng.permutation(Sp[:, k])
      return Sp

 def ratio_matched_pairshuf(S, rng, Q=6):
     """Approx preserve ratio structure by shuffling within windows of sorted
 ratios."""
     N, K = S.shape
     if K < 2:
         return S.copy()
     Sp = S.copy()




                                          5
      ratios = Sp[:, 1] / (Sp[:, 0] + 1e-12)
      order = np.argsort(ratios)
      w = max(3, N // Q)
      for start in range(0, N, w):
          idx = order[start:start+w]
          Sp[idx, 1] = rng.permutation(Sp[idx, 1])
      return Sp


6.6 Scrambled recursion control (distinct from pairshuf)


 def scrambled_tower_scales(N, K, s_floor=1.0, rng=None):
     if rng is None:
         rng = np.random.default_rng(123)

      Sprime = scales_matrix_prime(N, K, s_floor)
      pvals = [nth_prime(i) for i in range(1, N+1)]
      M = max(pvals)

      g = np.arange(1, M+1)
      rng.shuffle(g) # permutation of indices 1..M

      S = np.zeros((N, K), dtype=float)
      for i, p_n in enumerate(pvals):
          S[i, 0] = s_floor + math.log1p(p_n)
          if K >= 2:
              idx2 = g[p_n - 1]
              val2 = nth_prime(idx2)
              S[i, 1] = s_floor + math.log1p(val2)

      # Match level-2 marginal to prime level-2 marginal
      if K >= 2:
          S[:, 1] = quantile_match(S[:, 1], Sprime[:, 1])
      return S


6.7 Clean ablation kernel (no clipping, signed diff, global norm)


 def effective_kernel_fft_levelwise(
     L: int, S_mat, alpha: float, tau: float, Lambda_k,
     gamma: float = 0.4, alpha_d: float = 1.0, clipz: float = 10.0
 ):
     N, K = S_mat.shape

      # level mixing
      lk = np.log(Lambda_k + 1e-12) / max(tau, 1e-6)
      lk -= lk.max()




                                            6
pi = np.exp(lk); pi /= pi.sum()

# smoothing mixture
ksmooth = np.zeros(L, dtype=float)
for k in range(K):
    svals = S_mat[:, k]
    z = (alpha * np.log(svals + 1e-12)) / max(tau, 1e-6)
    z = np.clip(z, -clipz, clipz)
    z -= z.max()
    w = np.exp(z); w /= w.sum()

    k_level = np.zeros(L, dtype=float)
    for wi, s in zip(w, svals):
        k_level += wi * gaussian_ring_kernel_vec(L, float(s))
    k_level /= k_level.sum() + 1e-12
    ksmooth += pi[k] * k_level

ksmooth /= ksmooth.sum() + 1e-12     # sum=1

# signed, zero-sum diff correction
kdiff = np.zeros(L, dtype=float)
if K >= 2 and gamma != 0:
    ratios = S_mat[:, 1] / (S_mat[:, 0] + 1e-12)
    zd = alpha_d * np.log(ratios + 1e-12)
    zd = np.clip(zd, -clipz, clipz)
    zd -= zd.max()
    w_d = np.exp(zd); w_d /= w_d.sum() + 1e-12

    for n in range(N):
        k2 = gaussian_ring_kernel_vec(L, float(S_mat[n, 1]))
        k1 = gaussian_ring_kernel_vec(L, float(S_mat[n, 0]))
        diff = k2 - k1
        diff -= diff.mean() # enforce zero-sum
        kdiff += w_d[n] * diff

    kdiff -= kdiff.mean()
    kdiff /= (np.linalg.norm(kdiff) + 1e-12)   # global norm only


# combine and spectral rescale
ktotal = ksmooth + gamma * kdiff
kfft = np.fft.fft(ktotal)
max_mag = np.max(np.abs(kfft))
if max_mag > 1:
    kfft /= max_mag
return kfft




                                      7
6.8 Diagnostics: ratio variance and gap statistic


 def ratio_stats(S):
     lr = np.log(S[:, 1] / (S[:, 0] + 1e-12) + 1e-12)
     var_log_r = float(np.var(lr))
     gap_stat = float(np.mean(np.abs(np.diff(np.sort(lr))))) if len(lr) > 1 else
 0.0
     return var_log_r, gap_stat


6.9 Spearman correlation (NumPy only)


 def spearman_corr(a, b):
     a = np.asarray(a); b = np.asarray(b)
     ra = np.argsort(np.argsort(a))
      rb = np.argsort(np.argsort(b))
      ra = (ra - ra.mean()) / (ra.std() + 1e-12)
      rb = (rb - rb.mean()) / (rb.std() + 1e-12)
      return float((ra * rb).mean())


6.10 Repeated CV accuracy and separation metric


 from sklearn.pipeline import make_pipeline
 from sklearn.preprocessing import StandardScaler
 from sklearn.linear_model import LogisticRegression
 from sklearn.model_selection import StratifiedKFold
 from sklearn.metrics import accuracy_score

 def cv_logreg_accuracy_repeated(X, y, repeats=10, folds=5, C=0.05):
     mus = []
     for r in range(repeats):
         skf = StratifiedKFold(n_splits=folds, shuffle=True, random_state=42+r)
         accs = []
         for tr, te in skf.split(X, y):
              clf = make_pipeline(StandardScaler(),
                                 LogisticRegression(max_iter=800, C=C,
 solver="liblinear"))
             clf.fit(X[tr], y[tr])
             accs.append(accuracy_score(y[te], clf.predict(X[te])))
         mus.append(np.mean(accs))
     mu = float(np.mean(mus))
     sd = float(np.std(mus))
     sep = abs(mu - 0.5)
     return mu, sd, sep




                                            8
6.11 Permutation test on separation


  def perm_test_separation(X, y, sep_obs, n_perm=500, rng=None):
      if rng is None:
          rng = np.random.default_rng(0)
      seps = []
      for _ in range(n_perm):
          yperm = rng.permutation(y)
           mu, sd, sep = cv_logreg_accuracy_repeated(X, yperm, repeats=5)
           seps.append(sep)
       seps = np.array(seps)
       p = float(np.mean(seps >= sep_obs))
       return p




7. Minimal “ladder” experiment recipe
Recommended minimal settings for a first publishable run:


     • Fix: α = 2, τ = 1
     • Ablations: γ ∈ {0, 0.4}, αd ∈ {0, 1}
     • Runs/class: 200
     • Steps: 100–150
     • Baselines: pairshuf , ratio_matched_pairshuf(Q=6) , scrambled_tower_scales

Expected ladder pattern:


1) γ = 0 or αd = 0: separations near 0. 2) γ > 0, αd > 0: prime vs pairshuf separable. 3) If ratio
dominates: prime vs ratio‑matched collapse. 4) If recursion matters beyond ratios: prime vs scrambled
remains separable.




8. Suggested narrative (paper abstract level)
A defensible, conservative claim that this suite supports:


       We introduce a pairing‑sensitive multiscale diffusion operator with a signed mean‑zero
       cross‑level correction. Using a ladder of structure‑preserving controls (marginal‑match,
       pairing shuffle, ratio‑approximately‑matched shuffle, and scrambled recursion), we show that
       detectability of prime‑tower constructions is largely explained by log‑compressed scale‑ratio
       concentration consistent with prime number theorem heuristics. The signal ablates when the
       signed correction is removed (γ = 0) or when ratio‑based weighting is disabled (αd = 0).




                                                       9
9. Next steps
   • Add optional feature blocks for smooth vs diff contributions to enable permutation‑importance
     analysis by block.
   • Extend to 2D torus with FFT‑based separable Gaussians (still efficient).
   • If “beyond ratios” is desired: introduce additional arithmetic‑sensitive statistics (e.g., prime
     gap‑driven weights) and add ratio‑matched controls that preserve additional moments.




                                                  10

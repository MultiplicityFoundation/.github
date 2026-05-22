---
slug: mscm-2
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Mscm 2.md
  last_synced: '2026-03-20T17:17:20.621488Z'
---

MSCM 2.0 Final Report
Why Translation-Invariant Prime-Shift Operators Don’t Encode
Arithmetic in k-Tuple Ratio Observables

Status

This document formalizes the complete set of developments, definitions, falsification tests, empirical
outcomes, and the mathematical explanation supporting the final conclusion:


       In translation-invariant linear models with smooth positive forcing, Hardy–Littlewood
       k-tuple constants are determined by local sieve admissibility [1,3,4].
       The global “prime-shift” operator acts as an arithmetic-agnostic smoother, and its effect
       cancels in the ratio observables studied.


This is a negative result for a broad class of operator-based prime models, and it provides a reusable null-
test framework for future operator proposals.




1. Research question
We test whether a translation-invariant linear operator built from prime-indexed shifts can encode
arithmetic structure relevant to the Hardy–Littlewood prime k-tuple correlations [1].


Two hypotheses:


     • H₀ (agnostic smoothing): Prime-shift dynamics is effectively indistinguishable from random sparse
       shift dynamics after stability normalization; observed constants are sieve-driven.
     • H₁ (arithmetic content): Prime-shift dynamics produces residue-specific distortions and/or spectral
       signatures not replicated by random-support operators.




2. Model definition (MSCM 2.0)

2.1 Ambient space

Work on the finite cyclic group


$$ G = \mathbb{Z}/N\mathbb{Z},\qquad f\in \ell^2(G). $$


The periodic setting enables FFT-based diagonalization and reproducible numerics.




                                                     1
2.2 Layer 1: translation-invariant dynamics

Define a circulant convolution operator


$$ (Af)(n)=\sum_{k\in G} a(k)f(n-k), $$


with kernel supported on a sparse set of shifts.


Prime-support kernel (nominal model):


$$ a(p)=\lambda\,p^{\alpha}\quad \text{for primes } p\le P,\qquad a(k)=0\text{ otherwise}. $$


Random-support kernel (null comparator): sample a sparse support on {2, … , P } with “prime-like”
inclusion probabilities proportional to 1/ log n (cf. Cramér-style random models [2,5]), then assign the same
weight rule λnα .


Stability normalization: choose λ so that


$$ \max_{\xi\in G^*} |\widehat a(\xi)| = \rho \in (0,1), $$


where a is the discrete Fourier transform (DFT) symbol.


2.3 Forcing and fixed point

Use a smooth positive forcing (baseline prime density proxy)


$$ g(n)=\frac{1}{\log(n+n_0)} \quad (n\ge 1), \qquad g(0)=\frac{1}{\log(n_0+1)}. $$


Assuming max ∣a∣ < 1, define the fixed point


$$ f_\infty = (I-A)^{-1}g. $$


In Fourier space (DFT indices ξ ):


$$ \widehat f_\infty(\xi)=\frac{\widehat g(\xi)}{1-\widehat a(\xi)}. $$




3. Layer 2: pattern-specific sieve mask
This layer implements the standard local admissibility viewpoint from sieve theory [3,4].


Let H = {h1 , … , hk } be a prime k-tuple pattern (e.g., {0, 2} for twins). Fix a sieve cutoff y .


Define the truncated admissibility mask




                                                         2
$$ M_{H,y}(n)=\prod_{p\le y}\mathbf{1}_{\forall h\in H:\ n+h\not\equiv 0\pmod p}. $$


Define the truncated Hardy–Littlewood singular series [1]


$$ \mathfrak{S}y(H)=\prod, $$}\frac{1-\nu_H(p)/p}{(1-1/p)^k


where νH (p) is the number of distinct residues occupied by H modulo p.




4. Observable (ratio form)
Define the weight signal


$$ w(n):=\prod_{h\in H} f_\infty(n+h)\ge 0. $$


Define the primary observable


$$ R_H(X;y) =\Big(\prod_{p\le y}(1-1/p)^{-k}\Big) \frac{\sum_{n\le X} M_{H,y}(n)\,w(n)}{\sum_{n\le X} w(n)}. $$


This ratio is designed to remove slow log-scale variation in f∞ and isolate local admissibility structure.




5. Mathematical explanation of the negative result

5.1 Cancellation principle

The observable is a weighted density of the mask:


$$ \frac{\sum_{n\le X} M_{H,y}(n)\,w(n)}{\sum_{n\le X} w(n)}. $$


If w is slowly varying relative to the periodic structure induced by primes ≤ y , or approximately
independent of MH,y , then


$$ \frac{\sum_{n\le X} M_{H,y}(n)\,w(n)}{\sum_{n\le X} w(n)} \approx \frac{1}{X}\sum_{n\le X}M_{H,y}(n), $$


hence


$$ R_H(X;y)\approx \mathfrak{S}_y(H). $$


This approximation becomes exact over full periods when w is constant on residue classes modulo the
primorial Q = ∏p≤y p.




                                                       3
5.2 Why Layer 1 is generically “smooth” here

      • Forcing g is positive and slowly varying.
      • (I − A)−1 is translation-invariant; its action is diagonal in Fourier space.
      • With ρ-normalization, prime-support and random-support kernels produce similar-scale Fourier
         symbols a(ξ), so f∞ stays in a low-frequency dominated, positive regime.
      • In the ratio observable, most global reweighting cancels.

Consequence: k-tuple constant recovery is sieve-dominated, while Layer 1 is arithmetic-agnostic for
these diagnostics.




6. Falsification protocols
We implement four tests intended to detect arithmetic content in Layer 1.


Test 1: Global constant recovery

Compare RH (X; y) to Sy (H) for several patterns H .


Test 2: Residue-conditioned ratios (definitive)

For a modulus m, define residue-conditioned ratios


$$ R_{H,a}(X;y;m)=\Big(\prod_{p\le y}(1-1/p)^{-k}\Big) \frac{\sum_{n\le X\atop n\equiv a\,(m)} M_{H,y}(n)w(n)}
{\sum_{n\le X\atop n\equiv a\,(m)} w(n)}. $$


If Layer 1 encodes arithmetic structure, prime-support and random-support operators should produce
measurably different vectors (RH,a )m−1
                                    a=0 .


Test 3: Dirichlet character correlations

Probe periodic structure by computing correlations against a non-principal Dirichlet character χ [4] (e.g.,
mod 3):


$$ C_\chi(X)=\sum_{n\le X} f_\infty(n)\chi(n), $$


and compare prime-support vs random-support models.


Test 4: Frequency response signatures

Define


$$ W(\xi)=\sum_{p\le P} p^\alpha e^{-2\pi i \xi p},\qquad T(\xi)=\frac{1}{|1-\lambda W(\xi)|}. $$




                                                        4
Compare T (ξ) for prime support vs random support, including rational ξ = a/q with small denominators
and dense frequency grids. (See also standard spectral heuristics around zeta zeros, e.g. Montgomery’s pair
correlation [6].)




7. Numerical results (definitive outcomes)
All outcomes below are computed under a consistent parameterization used throughout the investigation.


7.1 Parameterization used in the definitive run

     • N = 222 = 4,194,304
     • X = 2,000,000
     • P = 1000, y = 200
     • α = −1.5, ρ = 0.95, n0 = 10

7.2 Summary of falsification tests

(1) Global **RH **: matches Sy (H) within \~1% (sieve dominance).


(2) Residue-conditioned ratios: prime-support vs random-support vectors have correlation 1.0000 and
MAE < 3 × 10−5 for mod 30 and mod 210.


(3) Dirichlet sums: prime-support and random-support correlations are effectively identical (difference at
\~1e-10 scale after normalization).


(4) Frequency response: maximum observed z-scores lie within the noise envelope for many frequency
bins; no statistically significant prime-specific enhancement after ρ-normalization.




8. Figures and data artifacts (reproducibility bundle)

Convergence and baseline comparison

     • Full model convergence: mscm2_corrected_full_model_convergence.png
     • f∞ vs baseline density: mscm2_corrected_f_vs_baseline.png
     • Summary table (CSV): mscm2_corrected_summary.csv
     • Baseline vs full overlay: mscm2_baseline_vs_full_overlay.png

Residue-conditioned diagnostics

     • Mod 30 scatter: mscm2_residue_mod30_scatter.png
     • Mod 30 diff bars: mscm2_residue_mod30_diffbar.png
     • Mod 210 scatter: mscm2_residue_mod210_scatter.png
     • Mod 210 diff bars: mscm2_residue_mod210_diffbar.png
     • Residue-conditioned summary (CSV): mscm2_residue_conditioned_summary.csv




                                                    5
Dirichlet diagnostic

      • Dirichlet mod 3 summary (CSV): mscm2_dirichlet_mod3_summary.csv

Frequency-response diagnostics

      • Rationals table (CSV): mscm2_frequency_response_rationals.csv
      • Ratio plot: mscm2_frequency_response_ratio.png
      • Z-scores at rationals: mscm2_frequency_response_zscores.png
      • Z-score histogram (grid): mscm2_frequency_response_zscore_hist.png
      • Z-score curve (grid): mscm2_frequency_response_zscore_curve.png




9. Interpretation and implications

9.1 Core conclusion

Within the tested model class,


       Hardy–Littlewood constants emerge from local admissibility (sieve) structure [1,3,4].
       Global prime-shift dynamics contributes no detectable arithmetic content to the studied
       ratio and spectral diagnostics.


9.2 What this rules out

      • “Primes as eigenvalues” is not supported by translation-invariant convolution alone (cf. spectral
        heuristics around zeta zeros, e.g. Montgomery’s pair correlation [6]).
      • Prime-indexed kernels do not automatically produce residue-class signatures.
      • Spectral “resonances” at rationals do not appear as a robust prime-specific effect after stability
        normalization.

9.3 What this clarifies

This work identifies a broad dead-end: linear translation-invariant operator models with smooth
positive forcing are unlikely to encode prime-specific structure in ratio observables.


This complements probabilistic models of primes such as Cramér’s model [2] and refinements discussed by
Granville [5] by isolating the role of local admissibility.




10. Future directions (minimal changes that could matter)
To obtain arithmetic content in an operator model, at least one of the following must change.




                                                          6
Recent progress on bounded gaps and admissible k-tuple methods emphasizes the centrality of sieve
structure [7,8].


     1. Break translation invariance (introduce a residue-dependent potential V (n)):

$$ (Af)(n)=\sum_{p\le P} w(p)\,V(n)\,f(n-p). $$


     1. Use oscillatory forcing (probe response without positivity/low-frequency cancellation):

$$ g(n)=\chi(n)\quad\text{or}\quad g(n)=e^{2\pi i n/q}. $$


     1. Introduce nonlinearity:

$$ f_{t+1}=\sigma(Af_t+g), $$


where σ can amplify residue-dependent differences.




11. Paper-ready framing

Suggested title

Why Translation-Invariant Prime-Shift Operators Don’t Encode Arithmetic: A Negative Result for
Dynamical Models of Prime k-Tuples


Suggested abstract

We study whether translation-invariant linear operators built from prime-indexed shifts can encode
arithmetic information relevant to Hardy–Littlewood prime k-tuple correlations [1]. Using a two-layer
architecture—(i) a global prime-shift convolution dynamics and (ii) a local pattern-specific sieve mask—we
show that the Hardy–Littlewood constants are recovered entirely by the sieve layer [3,4]. Multiple
falsification tests (global ratios, residue-conditioned ratios, Dirichlet character probes, and transfer-function
diagnostics) demonstrate that the global operator is statistically indistinguishable from random-support
analogues matched in density and stability (cf. probabilistic prime models [2,5]). We provide a mathematical
explanation via ratio cancellation under smooth positive forcing and conclude that arithmetic content in
operator models likely requires non-translation-invariance, oscillatory forcing, or nonlinear dynamics.




12. Checklist for final submission
-




                                                       7
13. References
[1] G. H. Hardy and J. E. Littlewood, Some Problems of ‘Partitio Numerorum.’ III. On the Expression of a Number
as a Sum of Primes, Acta Mathematica 44 (1923), 1–70. doi:10.1007/BF02403921.


[2] H. Cramér, On the order of magnitude of the difference between consecutive prime numbers, Acta
Arithmetica 2 (1936), 23–46. doi:10.4064/aa-2-1-23-46.


[3] H. Halberstam and H.-E. Richert, Sieve Methods, Academic Press, 1974.


[4] H. Iwaniec and E. Kowalski, Analytic Number Theory, AMS Colloquium Publications, Vol. 53, American
Mathematical Society, 2004.


[5] A. Granville, Harald Cramér and the distribution of prime numbers, Scandinavian Actuarial Journal
1995(1) (1995), 12–28. doi:10.1080/03461238.1995.10413946.


[6] H. L. Montgomery, The pair correlation of zeros of the zeta function, in Analytic Number Theory, Proc.
Sympos. Pure Math., Vol. 24, American Mathematical Society, 1973, pp. 181–193.


[7] J. Maynard, Small gaps between primes, Annals of Mathematics 181(1) (2015), 383–413. doi:10.4007/
annals.2015.181.1.7.


[8] Y. Zhang, Bounded gaps between primes, Annals of Mathematics 179(3) (2014), 1121–1174. doi:10.4007/
annals.2014.179.3.7.


Citizen Gardens © 2025 CC-NC-ND 4.0




                                                      8

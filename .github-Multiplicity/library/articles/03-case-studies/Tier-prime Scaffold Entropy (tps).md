---
slug: tier-prime-scaffold-entropy-tps
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Tier-prime Scaffold Entropy (tps).md
  last_synced: '2026-03-20T17:17:21.264737Z'
---

Tier-Prime Scaffold Entropy (TPS)
0. Purpose
We formalize an entropic framework where geometry/meaning comes from a learned tier embedding
(semantics/cost), while primes serve only as a canonical indexing scaffold for tiers. The resulting
descriptors support (i) within-window compressibility and (ii) cross-window novelty/stability.




1. Data model
Let Σ be a finite (or countable) symbol set. A data stream is (Xt )t∈Z with Xt ∈ Σ. A window of length n
ending at time t is


$$ x_t := (X_{t-n+1},\dots,X_t)\in \Sigma^n. $$


Let cs (x) denote the count of symbol s in window x.




2. Learned embedding and tier coordinate

2.1 Embedding

Let fθ : Σ → Rd be an embedding map and define


$$ z(s) := f_\theta(s)\in\mathbb{R}^d. $$


We require an ordered scalar coordinate τ : Σ → R. Two standard constructions:


(A) Cost-supervised tier (if costs E(s) are available):


      • Learn fθ and a head g to predict costs.

$$ \tau(s):=\hat E(s)=g(z(s)). $$


(B) Self-supervised / unsupervised tier (if only sequences are available):


      • Learn fθ from context, then choose a 1D projection (e.g., PCA axis) u ∈ Rd and set

$$ \tau(s):=u^\top z(s). $$


Assumption (Tier identifiability): τ is chosen so that nearby τ -values correspond to semantically/cost-similar
symbols.




                                                          1
3. Tier quantization
Fix an integer K ≥ 2 and thresholds


$$ -\infty=b_0 < b_1 < \cdots < b_{K-1} < b_K=+\infty. $$


Define the tier assignment


$$ \kappa(s)=k\quad\Longleftrightarrow\quad \tau(s)\in[b_{k-1},b_k),\qquad k\in{1,\dots,K}. $$


For a window x, define tier-counts


$$ C_k(x):=\sum_{j=1}^n \mathbf{1}{\kappa(x_j)=k},\qquad n=\sum_{k=1}^K C_k(x), $$


and tier-frequencies


$$ w_k(x):=\frac{C_k(x)}{n}. $$


Choice of thresholds. Common options:


      • Equal-mass bins under a baseline distribution q(s) (e.g., long-run frequencies) so each tier has
        comparable prior mass.
      • Equal-width bins in τ -space.
      • Learned bins that optimize downstream objectives (compression/anomaly labels).




4. Prime indexing scaffold
Let pk be the k -th prime: p1 = 2, p2 = 3, ….


4.1 Tier-coded integer (optional algebraic summary)

Define


$$ N(x):=\prod_{k=1}^K p_k^{C_k(x)}. $$


This representation is not used for factorization; it is a commutative bookkeeping device. All computable
statistics depend only on Ck (or wk ).




5. Within-window entropy: type/multiplicity entropy
Define the tier type class size (multinomial coefficient)




                                                       2
$$ |T(C(x))|:=\frac{n!}{\prod_{k=1}^K C_k(x)!}. $$


Define type/multiplicity entropy


$$ H_T(x):=\frac{1}{n}\log |T(C(x))| = \frac{1}{n}\log\frac{n!}{\prod_{k=1}^K C_k(x)!}. $$


5.1 Asymptotics (Shannon emergence)

Let wk = Ck /n. By Stirling, for large n,


$$ H_T(x)= -\sum_{k=1}^K w_k\log w_k + O\Big(\frac{\log n}{n}\Big). $$


Thus HT approaches Shannon entropy of the tier distribution.




6. Tier spread (geometry-driven disorder)
To measure dispersion along the learned axis, assign each tier a representative coordinate τ~k . Common
choices:


      • midpoint τ~k = (bk−1 + bk )/2 when finite,
      • conditional mean τ~k = E[τ (S) ∣ κ(S) = k] under a baseline distribution,
      • empirical mean of τ (s) for symbols currently mapped to tier k .

Define the tier mean and variance in a window


$$ \mu_\tau(x):=\sum_{k=1}^K w_k(x)\,\tilde\tau_k,\qquad V_\tau(x):=\sum_{k=1}^K w_k(x)\,(\tilde\tau_k-
\mu_\tau(x))^2. $$


Interpretation: Vτ measures tier-mixing across cost/semantic levels. Low Vτ indicates concentration in a
narrow band.




7. Dynamics: novelty / stability via 1D transport
Define the induced discrete distribution on tier coordinates


$$ \rho_x:=\sum_{k=1}^K w_k(x)\,\delta_{\tilde\tau_k}. $$


Define the spectral change between adjacent windows (or any pair)


$$ \Delta_\tau(t):=W_1\big(\rho_{x_t},\rho_{x_{t-1}}\big), $$


where W1 is the 1-Wasserstein distance on R.




                                                        3
Computation (1D). In one dimension, W1 can be computed from cumulative distributions; for discrete tiers
this reduces to a simple cumulative-sum formula.


Interpretation: Δτ is a sensitive regime-shift statistic capturing mass transport along the tier axis.




8. Combined score (optional scalarization)
If a single scalar is desired, define for α ∈ [0, 1]


$$ \mathrm{TPS}\alpha(x):=\alpha\,H_T(x) + (1-\alpha)\,\sqrt{V\tau(x)}. $$


For dynamics, use (HT (xt ),     Vτ (xt ), Δτ (t)) as a 3D descriptor.



9. Properties and invariances
     1. No symbol relabeling sensitivity (conditional): If τ is learned/defined from semantics/cost and κ
       depends only on τ , then permuting symbol names does not change (HT , Vτ , Δτ ).
     2. Prime scaffold irrelevance: Primes do not affect (HT , Vτ , Δτ ); they only provide canonical labels
       k ↦ pk for algebraic bookkeeping.
     3. Shannon emergence: HT converges to the Shannon entropy of the tier-frequency vector w for
       large n.
     4. Geometric refinement: Two windows with identical w (hence identical HT ) can still differ in Vτ if
       tiers are defined differently (via learned τ ), and can differ in Δτ across time.




10. Practical validation protocol (minimal)

10.1 Synthetic separation

Construct windows with (approximately) equal tier Shannon entropy but different tier placement/mixing
along τ~. Verify Vτ and Δτ separate cases where HT does not.


10.2 Compression correlation

On real streams, compute sliding-window HT and Vτ , and correlate with achieved compression ratio (e.g.,
zstd/gzip) under fixed windowing. Expect (HT , Vτ ) to outperform HT alone for short windows.


10.3 Anomaly / regime shifts

Apply change-point detection to Δτ (and optionally           Vτ ). Inject controlled novelty events and evaluate
detection delay and false positives.




                                                         4
11. Notes on design choices
     • Choice of ****K ****: Larger K gives finer geometry but increases variance of estimates in short
       windows.
     • Tier drift: If τ is learned online, keep tiers stable via slow updates or anchoring to a baseline
       distribution.
     • Embedding updates: Separate timescales: fast window statistics; slow embedding/tier updates.




12. Summary
TPS replaces assigned primes with a learned tier geometry τ (semantics/cost). The system is summarized
per window by:


     • HT : microstate multiplicity of tier counts (type entropy),
     • Vτ : dispersion across the learned tier axis,
     • Δτ : temporal mass transport along tiers (novelty/stability). Primes remain only as a canonical
                                                                                                C
       indexing scaffold for tiers, optionally yielding a compact integer summary N (x) = ∏ pk k .


References
    1. Apostol, T. M. (1976). Introduction to Analytic Number Theory. Springer. (See Ch. 1: The Fundamental
       Theorem of Arithmetic.)
    2. Hardy, G. H., & Wright, E. M. (2008). An Introduction to the Theory of Numbers (6th ed.). Oxford
       University Press.
    3. Shannon, C. E. (1948). A mathematical theory of communication. Bell System Technical Journal, 27,
       379–423, 623–656.
    4. Cover, T. M., & Thomas, J. A. (2006). Elements of Information Theory (2nd ed.). Wiley.
    5. Csiszár, I. (1998). The method of types. IEEE Transactions on Information Theory, 44(6), 2505–2523.
    6. Csiszár, I., & Körner, J. (2011). Information Theory: Coding Theorems for Discrete Memoryless Systems
       (2nd ed.). Cambridge University Press.
    7. Rissanen, J. (1978). Modeling by shortest data description. Automatica, 14(5), 465–471.
    8. Polyanskiy, Y., Poor, H. V., & Verdú, S. (2010). Channel coding rate in the finite blocklength regime.
       IEEE Transactions on Information Theory, 56(5), 2307–2359.
    9. Kostina, V., & Verdú, S. (2012). Fixed-length lossy compression in the finite blocklength regime. IEEE
       Transactions on Information Theory, 58(6), 3309–3338.
   10. Villani, C. (2009). Optimal Transport: Old and New. Springer.
   11. Peyré, G., & Cuturi, M. (2019). Computational optimal transport. Foundations and Trends in Machine
       Learning, 11(5–6), 355–607.
   12. Santambrogio, F. (2015). Optimal Transport for Applied Mathematicians: Calculus of Variations, PDEs, and
       Modeling. Birkhäuser.
   13. Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient estimation of word representations in
       vector space. arXiv:1301.3781.
   14. Mikolov, T., Sutskever, I., Chen, K., Corrado, G., & Dean, J. (2013). Distributed representations of words
       and phrases and their compositionality. In Advances in Neural Information Processing Systems (NeurIPS
       2013).




                                                       5
   15. Pennington, J., Socher, R., & Manning, C. D. (2014). GloVe: Global vectors for word representation. In
       Proceedings of EMNLP 2014 (pp. 1532–1543).
   16. Devlin, J., Chang, M.-W., Lee, K., & Toutanova, K. (2019). BERT: Pre-training of deep bidirectional
       transformers for language understanding. In Proceedings of NAACL-HLT 2019 (pp. 4171–4186).
   17. van den Oord, A., Li, Y., & Vinyals, O. (2018). Representation learning with contrastive predictive
       coding. arXiv:1807.03748.
   18. Gutmann, M. U., & Hyvärinen, A. (2010). Noise-contrastive estimation: A new estimation principle for
       unnormalized statistical models. In Proceedings of AISTATS 2010 (PMLR 9, pp. 297–304).
   19. Han, T. S. (2003). Information-Spectrum Methods in Information Theory. Springer.
   20. Page, E. S. (1954). Continuous inspection schemes. Biometrika, 41(1–2), 100–114.
   21. Killick, R., Fearnhead, P., & Eckley, I. A. (2012). Optimal detection of changepoints with a linear
       computational cost. Journal of the American Statistical Association, 107(500), 1590–1598.

Citizen Gardens © 2025 CC-NC-ND 4.0




                                                      6

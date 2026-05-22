---
slug: strang-gate-o-d-scan-estimator-ewma-lps-ramanujan-expander-d-12
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Strang Gate_ O(d) Scan Estimator + Ewma (lps Ramanujan Expander,
    D=12).md
  last_synced: '2026-03-20T17:17:21.206111Z'
---

Strang-Splitting Online Gate with O(D) Memory
Estimator
This document consolidates the second-order (Strang) split-step stability gate for a Π-kernel swarm with:


     • Expander model: LPS Ramanujan family, fixed degree d = 12 (choose p = 11)
     • Spectral constant: σ = 2 d − 1/d = 2 11/12 ≈ 0.552771, so 1 − σ ≈ 0.447229
     • Estimator settings: m = 8 probes, EWMA window W = 19 ⇒ β = 0.9, safety inflation χ = 1.5

The goal is a single scalar gate that can be enforced online:


$$ \frac{\Delta t^3}{8}\,\chi\,\widetilde C_{\oplus}(t)\;\le\;\alpha\Big[\lambda\gamma + (1-\lambda\gamma)\,
\eta(1-\sigma)\Big] $$


where C⊕ (t) is a smoothed (EWMA) estimate of the nested-commutator magnitude.




1) Objects and definitions

Operators

Let H1 , H2 be linear operators (typically Hermitian generators). Define nested commutators:


$$ K_1 := [H_1,[H_1,H_2]],\qquad K_2 := [H_2,[H_2,H_1]]. $$


Expanded forms (useful for computation):


$$ K_1 = H_1^2H_2 - 2H_1H_2H_1 + H_2H_1^2, $$


$$ K_2 = H_1H_2^2 - 2H_2H_1H_2 + H_2^2H_1. $$


Contraction slack (expander-dependent)

Let κ = 1 − λγ . Using lazy mixing A(η) = (1 − η)I + ηP , the expander disagreement contraction
margin contributes the factor η(1 − σ).


Define the available slack:


$$ S(\alpha,\eta,\lambda,\gamma) := \alpha\Big[\lambda\gamma + (1-\lambda\gamma)\,\eta(1-\sigma)
\Big]. $$


For d = 12 Ramanujan expanders:




                                                      1
$$ 1-\sigma \approx 0.447229, \qquad S = \alpha\Big[\lambda\gamma + 0.447229\,\eta(1-\lambda\gamma)
\Big]. $$




2) Single-scalar commutator estimator with shared probes
We estimate


$$ |K_1|_F^2 + |K_2|_F^2. $$


Shared-probe Hutchinson estimator
                              †
Let probes zk satisfy E[zk zk ] = I (Rademacher/Steinhaus/complex normal). With m = 8 probes:


$$ \widehat S(t) := \frac{1}{8}\sum_{k=1}^8 \big(|K_1 z_k|_2^2 + |K_2 z_k|_2^2\big) \approx |K_1|_F^2 + |
K_2|_F^2. $$


Define C⊕ (t) :=     S (t).

EWMA smoothing (β = 0.9)

Smooth the squared quantity:


$$ \widetilde S(t) = 0.9\,\widetilde S(t-1) + 0.1\,\widehat S(t), \qquad \widetilde C_{\oplus}(t) = \sqrt{\widetilde
S(t)}. $$


Initialize S (0) = S (0).




3) The Strang gate (single inequality)
With χ = 1.5:


$$ \boxed{
\frac{\Delta t^3}{8}\,(1.5)\,\widetilde C_{\oplus}(t) \;\le\; \alpha\Big[\lambda\gamma + 0.447229\,\eta(1-
\lambda\gamma)\Big] \ } $$


Equivalently (since 1.5/8 = 0.1875):


$$ \boxed{
0.1875\,\Delta t^3\,\widetilde      C_{\oplus}(t)   \;\le\;   \alpha\Big[\lambda\gamma       +   0.447229\,\eta(1-
\lambda\gamma)\Big] \ } $$


If violated, shrink to the boundary:




                                                          2
$$ \Delta t \leftarrow \min\left(\Delta t,\ \Big(\frac{8}{1.5}\cdot\frac{S(\alpha,\eta,\lambda,\gamma)}
{\widetilde C_{\oplus}(t)}\Big)^{1/3}\right) =\min\left(\Delta t,\ \Big(5.333333\cdot\frac{S}{\widetilde
C_{\oplus}}\Big)^{1/3}\right). $$




4) O(D) peak-memory estimator: scan over probes
When even a batch (D, 8) is too large, compute each probe sequentially with peak memory O(D).


Minimal-apply per-probe kernel (12 applies)


  # Pseudocode: single probe, O(D) memory
  # H1_one, H2_one: (D,) -> (D,)

  def one_probe_score(H1_one, H2_one, z):
      # 1–6 shared intermediates
      z1 = H1_one(z)       # (1) H1 z
      z2 = H2_one(z)       # (2) H2 z

       z12 = H1_one(z2)          # (3) H1 H2 z
       z21 = H2_one(z1)          # (4) H2 H1 z

       z11 = H1_one(z1)          # (5) H1^2 z
       z22 = H2_one(z2)          # (6) H2^2 z

       # K1 z = H1^2H2 z - 2 H1H2H1 z + H2H1^2 z
       tmp = H1_one(z12)              # (7) H1^2H2 z
       tmp = tmp + H2_one(z11)        # (8) + H2H1^2 z
       tmp = tmp - 2.0 * H1_one(z21) # (9) - 2 H1H2H1 z
       s1 = (tmp.conj() @ tmp).real

       # K2 z = H1H2^2 z - 2 H2H1H2 z + H2^2H1 z
       tmp = H1_one(z22)              # (10) H1H2^2 z
       tmp = tmp + H2_one(z21)        # (11) + H2^2H1 z
       tmp = tmp - 2.0 * H2_one(z12) # (12) - 2 H2H1H2 z
       s2 = (tmp.conj() @ tmp).real


       return s1 + s2


Scan over m=8 probes


  # Z: (m, D) probes, m=8

  def estimate_S_hat_scan(H1_one, H2_one, Z):
      total = 0.0




                                                   3
       for z in Z:
           total += one_probe_score(H1_one, H2_one, z)
       return total / Z.shape[0]


EWMA + gate integration


  # fixed: beta=0.9, chi=1.5


  S_hat   = estimate_S_hat_scan(H1_one, H2_one, Z)                    # scalar
  S_tilde = 0.9 * S_tilde + 0.1 * S_hat
  C_tilde = sqrt(S_tilde)

  slack = alpha * (lambda_*gamma + 0.447229*eta*(1 - lambda_*gamma))

  if 0.1875 * (dt**3) * C_tilde > slack:
       dt = min(dt, (5.333333 * slack / C_tilde) ** (1/3))




5) Batched micro-optimized estimator (low intermediates, returns
S_hat only)
When (D, 8) fits, batching is typically faster (BLAS/FFT/block-Krylov gains).



  # Z: (D, m) columns are probes (m=8)
  # H1, H2: batched apply functions (D,m)->(D,m)

  def col_norm2(X):
      return (abs(X)**2).sum(axis=0)              # (m,)

  def estimate_S_hat_strang_batched(H1, H2, Z):
      # Shared intermediates
      Z1 = H1(Z)       # (1)
      Z2 = H2(Z)       # (2)
       Z12 = H1(Z2)           # (3)
       Z21 = H2(Z1)           # (4)
       Z11 = H1(Z1)           # (5)
       Z22 = H2(Z2)           # (6)

       # K1 part (tmp reused; no K1Z stored)
       tmp = H1(Z12)            # (7)
       tmp = tmp + H2(Z11)      # (8)
       tmp = tmp - 2.0*H1(Z21) # (9)
       s = col_norm2(tmp)




                                                       4
          # K2 part
          tmp = H1(Z22)                 # (10)
          tmp = tmp + H2(Z21)           # (11)
          tmp = tmp - 2.0*H2(Z12)       # (12)
          s = s + col_norm2(tmp)


          return s.mean()




6) Apply-count and cost table (this schedule)

Fixed apply counts (per probe)

      • Total operator applies: 12 per probe
      • Split: 6 calls to H1 , 6 calls to H2
      • Plus vector AX+Y and two dot products: O(D) extra

Complexity comparison

 Operator          One apply
                                     Per-probe cost here            Notes
 type              cost (rough)

                                                                    Batch (D, 8) uses GEMM for speed;
 Dense Hv          Θ(D2 )            12 Θ(D2 )
                                                                    scan uses GEMV.

                                                                    Usually bandwidth-bound; avoid
 Sparse SpMV       Θ(nnz)            6 Θ(nnz1 ) + 6 Θ(nnz2 )
                                                                    composite products (densify).

                   ≈
 FFT-based                           \~12 FFTs per probe (since 6   Diagonal H2 is O(D). Use rFFT if
     −1            2c D log D +
 F        ΛF                         H1 applies × (FFT+IFFT))       real.
                   O(D)

                   ≈                                                Batch enables block-Krylov; scan
 Krylov solve
                   k(Cmatvec +       6k1 (⋅) + 6k2 (⋅)              loses block benefits but saves
 A−1 v
                   CM )                                             memory.




7) Example operator apply patterns

(a) Dense


 def H1(X): return H1_mat @ X

 def H2(X): return H2_mat @ X




                                                         5
(b) Sparse


  def H1(X): return H1_sp @ X


  def H2(X): return H2_sp @ X


(c) FFT-based (kinetic + potential)


  def H1(X):
      Xk = fft(X, axis=0)
      Yk = k_hat[:, None] * Xk
      return ifft(Yk, axis=0)

  def H2(X):
      return V[:, None] * X


(d) Black-box Krylov (implicit inverse)


  def H1(X): return solve_block(A, X, M=precondA)


  def H2(X): return solve_block(B, X, M=precondB)




References (background)
    1. Lubotzky, Phillips, Sarnak. Ramanujan Graphs (construction of LPS graphs).
    2. Lubotzky. Discrete Groups, Expanding Graphs and Invariant Measures (expander background).
    3. Hairer, Lubich, Wanner. Geometric Numerical Integration (splitting methods; Strang error terms via
       nested commutators).
    4. Hutchinson. A stochastic estimator of the trace of the influence matrix for Laplacian smoothing splines
       (randomized trace estimators).
    5. Avron, Toledo. Randomized algorithms for estimating the trace of an implicit symmetric positive
       semidefinite matrix (variance bounds/modern view).

Citizen Gardens © 2025 CC-NC-ND 4.0




                                                       6

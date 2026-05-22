---
slug: ragi-c-full-spec-reference-code
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "05-systems/agi/Ragi\u2011c_ Full Spec + Reference Code.md"
  last_synced: '2026-03-20T17:17:17.806093Z'
---

RAGI‑C: Contractive LTV Affine Core — Full Spec
and Reference Code
Bottom line: single inequality drives everything. Design so


                                qt := ∥Ξ(t)∥ + ∥Λop
                                                 m (t)∥ LT < 1       for all t.

Then you have unique trajectories, geometric contraction, ISS, and a stationary fixed point when limits exist.
Everything else is optional.




1) Objects and norms
     • Space: Banach (Hilbert optional) (H, ∥ ⋅ ∥) .
     • State: Xt ∈ H .
     • Blocks: {Bp (t)}p∈Pt ⊂ B(H) with certified bounds bp (t) ≥ ∥Bp (t)∥ . Finite support per t .
     • Weights: w(t) = (wp (t)) ∈ R∣Pt ∣ .
     • Operator mix:

                            Ξ(t) = ∑ wp (t)Bp (t),         ∥Ξ(t)∥ ≤ ∑ bp (t) ∣wp (t)∣.
                                     p∈Pt                             p∈Pt

     • Multiplicity operator: Λop
                               m (t) ∈ B(H) , bounded.
     • Nonlinearity: T : H → H globally Lipschitz with constant LT ≥ 0 .
     • Optional ethics projector: P : H → H with P 2 = P , ∥P ∥ ≤ 1 .


2) Discrete dynamics (with optional input)

                                Xt+1 = P (Ξ(t)Xt + Λop
                                                    m (t) T (Xt ) + Gt ),

where Gt ∈ H is exogenous input (can be 0 ). If you omit P , take it as identity.


3) Contraction condition and guarantees
Define per‑step Lipschitz constant


                                       qt := ∥Ξ(t)∥ + ∥Λop
                                                        m (t)∥ LT .

Assume supt qt ≤ q < 1 . Then for any two trajectories Xt , Yt : - Incremental contraction: ∥Xt+1 −
Yt+1 ∥ ≤ q ∥Xt − Yt ∥ . Hence ∥Xt − Yt ∥ ≤ q t ∥X0 − Y0 ∥ . - ISS bound with input Gt : ∥Xt ∥ ≤ q t ∥X0 ∥ +
1−q t                                                                                    ∗           ∗
1−q supτ ∥Gτ ∥ . - Stationary limit: if Ξ(t) → Ξ , Λm (t) → Λ , Gt → G , then Xt → X solving X =
                                                    op

P (ΞX ∗ + ΛT (X ∗ ) + G) . Banach applies because the self‑map has Lipschitz ≤ q < 1 .




                                                       1
Ethics projector noncommutation budget (optional)

If P may not commute with Ξ(t) : define ηt := ∥P Ξ(t) − Ξ(t)P ∥ . The effective contraction factor is qt +
ηt . Require supt (qt + ηt ) < 1 . Prefer commuting designs to keep ηt = 0 .


4) ACE: weighted‑ℓ1 projection on weights
Goal: enforce ∥Ξ(t)∥ ≤ 1 − ε by construction.


     • Safety set at step t :

                                St := {w : ∑ bp (t) ∣wp ∣ ≤ 1 − ε},      ε ∈ (0, 1).
                                             p∈Pt

                                       ~ :
     • Projection problem for proposal wt

                                               ~ ∥2 s.t. ∑ b (t)∣w ∣ ≤ 1 − ε.
                                   min 12 ∥w − wt 2         p     p
                                    w
                                                            p

     • KKT soft‑threshold solution: for some λ ≥ 0

                                                ~ ) max (∣w
                                     wp∗ = sign(w         ~ ∣ − λ b (t), 0).
                                                 p         p       p

       Choose λ = 0 if feasible; else pick the unique λ making the constraint tight. Then

                                         ∥Ξ(t)∥ ≤ ∑ bp (t)∣wp∗ ∣ ≤ 1 − ε.
                                                        p

     • Log primal/dual residuals each step for audit.


5) Continuous‑time extension (optional)
Ẋ = F (τ )X + Λop
                m (τ )T (X) + g(τ ) . For contraction you need a logarithmic‑norm bound with respect to
the chosen norm:


                                μ(F (τ )) + ∥Λop
                                              m (τ )∥ LT ≤ −α < 0      a.e. τ .

Then ∥X(τ ) − Y (τ )∥ ≤ e−α(τ −τ0 ) ∥X(τ0 ) − Y (τ0 )∥ .


6) Minimal loop (pseudocode)

  init X0
  for t in 0..T-1:
      # 1) propose weights
      w_tilde = propose_weights()

       # 2) ACE projection to S_t
       w, lambda_, res = project_l1_weighted(w_tilde, b=bp(t), R=1-epsilon)




                                                        2
        # 3) build Xi(t)
        Xi = sum_p w[p] * Bp(t)[p]

        # 4) compute q_t and check margin
        q_t = op_norm(Xi) + op_norm(Lambda_op(t)) * L_T
        assert q_t < 1 - margin

        # 5) update state
        X = P( Xi @ X + Lambda_op(t) @ T(X) + G_t )

        # 6) log: q_t, sum b|w|, primal/dual residuals, optional commutator norm




Reference Python snippets (NumPy)
Notes: H = Rd with Euclidean norm. Use certified bounds bp . The spectral norm check is for diagnostics
only.


7) Weighted‑ℓ1 projection

  import numpy as np

  def project_l1_weighted(w_tilde, b, R, tol=1e-9, max_iter=100):
      """
      Solve min 0.5*||w - w_tilde||_2^2 s.t. sum_i b_i*|w_i| <= R.
      Returns (w, lam, info) with primal/dual residuals.
      Assumes b_i > 0 and R >= 0.
      """
      w_tilde = np.asarray(w_tilde, dtype=float)
      b = np.asarray(b, dtype=float)
      assert np.all(b > 0), "All b_i must be > 0"
      abs_w = np.abs(w_tilde)
      S = float(np.dot(b, abs_w))
      if S <= R or R == 0 and np.allclose(S, 0.0):
          lam = 0.0
          w = w_tilde.copy()
      else:
          # Bisection on lambda in [0, lam_max], where at lam_max -> w=0
          lam_lo, lam_hi = 0.0, np.max(abs_w / b)
          for _ in range(max_iter):
              lam = 0.5 * (lam_lo + lam_hi)
              shrink = np.maximum(abs_w - lam * b, 0.0)
              S_lam = float(np.dot(b, shrink))




                                                  3
                if S_lam > R:
                    lam_lo = lam
                else:
                    lam_hi = lam
                if lam_hi - lam_lo <= tol * (1.0 + lam_hi):
                    break
            lam = lam_hi
            w = np.sign(w_tilde) * np.maximum(abs_w - lam * b, 0.0)
        # Residuals
        primal = max(0.0, float(np.dot(b, np.abs(w)) - R))
        # Dual residual: stationarity w - w_tilde + lam * s = 0 with s_i in b_i*∂|
 w_i|
        s = np.empty_like(w)
        nz = np.abs(w) > 0
        s[nz] = b[nz] * np.sign(w[nz])
        # For zeros, pick subgradient minimizing residual magnitude
        z = ~nz
        if np.any(z):
            s[z] = b[z] * np.clip(w_tilde[z] / (lam + 1e-16), -1.0, 1.0)
        dual = float(np.linalg.norm(w - w_tilde + lam * s))
        return w, lam, {"primal_res": primal, "dual_res": dual}



8) Operator assembly and norms

 def op_norm(A):
     """Spectral norm for diagnostics (Euclidean)."""
     return float(np.linalg.norm(A, 2))

 def build_Xi(blocks, weights):
     """blocks: list/array of (d,d) arrays; weights: array shape (P,)."""
     Xi = np.zeros_like(blocks[0])
     for w, B in zip(weights, blocks):
         Xi += w * B
     return Xi



9) Example nonlinearity and projector

 def T_identity(x):
     """Lipschitz L_T = 1."""
     return x

 def P_identity(x):
     return x




                                           4
 def make_mask_projector(mask):
     """mask in {0,1}^d, nonexpansive orthogonal projector."""
     M = np.diag(mask.astype(float))
     return lambda x: M @ x



10) One simulation step

 def step(X, blocks, b, w_tilde, epsilon, Lambda_op, T, P=None, G=None,
          tol=1e-9):
     R = 1.0 - epsilon
     w, lam, info = project_l1_weighted(w_tilde, b=b, R=R, tol=tol)
     Xi = build_Xi(blocks, w)
     q_t = op_norm(Xi) + op_norm(Lambda_op) * L_T_from_T(T)
     if P is None:
         P = lambda x: x
     if G is None:
         G = np.zeros_like(X)
     X_next = P(Xi @ X + Lambda_op @ T(X) + G)
     telemetry = {
         "sum_b_abs_w": float(np.dot(b, np.abs(w))),
         "lambda": float(lam),
         "q_t": float(q_t),
         "primal_res": info["primal_res"],
         "dual_res": info["dual_res"],
         "Xi_norm_diag": float(op_norm(Xi)),
     }
     return X_next, w, telemetry

 def L_T_from_T(T):
     """Provide Lipschitz constant. For T_identity, L_T=1. Replace as needed."""
     return 1.0



11) Minimal end‑to‑end demo (deterministic)

 np.random.seed(7)
 d, P = 64, 20
 # Build blocks with certified bounds b_p
 blocks, b = [], []
 for _ in range(P):
     A = np.random.randn(d, d)
     # Scale to spectral norm <= b_p
     raw = np.linalg.norm(A, 2)
     bp = 0.4 * np.random.rand() + 0.1 # in (0.1, 0.5]
     B = (bp / max(raw, 1e-12)) * A




                                        5
     blocks.append(B)
     b.append(bp)
 b = np.array(b)

 # Dynamics params
 epsilon = 0.3 # ensures ||Xi|| <= 0.7
 Lambda_op = 0.2 * np.eye(d) # ||Lambda|| = 0.2
 L_T = 1.0 # T = identity


 # Two initial states to test contraction
 X = np.random.randn(d)
 Y = np.random.randn(d)

 for t in range(50):
     w_tilde = np.random.randn(P)
     X, wX, logX = step(X, blocks, b, w_tilde, epsilon, Lambda_op, T_identity)
     Y, wY, logY = step(Y, blocks, b, w_tilde, epsilon, Lambda_op, T_identity)
     ratio = np.linalg.norm(X - Y) / np.linalg.norm(wX - wY + 1e-16)
     # Diagnostic contraction rate on states
     rate = np.linalg.norm(X - Y) / (np.linalg.norm(X) + np.linalg.norm(Y) +
 1e-16)
     print({"t": t, "q_t": logX["q_t"], "sum_b|w|": logX["sum_b_abs_w"],
 "rate_diag": rate})



12) Unit checks to include
    • ACE feasibility: sum_b_abs_w <= 1 - epsilon + tol .
    • q_t margin: q_t <= (1 - epsilon) + ||Lambda|| L_T and < 1 by design.
    • Contraction (empirical): for fixed wt and same inputs, check ||X_{t+1}-Y_{t+1}|| <= q_t *
     ||X_t-Y_t|| + tol .
    • Stationary limit (linear case): set constant Ξ, Λ, G ; iterate until convergence; verify residual of
      fixed‑point equation.
    • Ethics projector: if used, and not guaranteed to commute, log eta_t = ||P Xi - Xi P|| and
     enforce q_t + eta_t < 1 .




13) Deployment checklist
   1. Pick H and norm. Rd with Euclidean norm is fine.
   2. Define blocks Bp (t) and certify bp (t) ≥ ∥Bp (t)∥ .
   3. Choose ε and implement ACE projection.
   4. Set Λop
           m (t) and bound its norm. Know LT .
   5. Verify qt < 1 at design time. Monitor at runtime.
   6. Log KKT residuals, ∑ bp ∣wp ∣ , qt , and optional commutator norms.




                                                      6
14) What is conjecture (exclude from guarantees)
“CSL,” “prime‑indexability,” “Zeno‑locking,” “Langlands braids,” “moonshine,” etc., unless expressed as
operators and inequalities that lower qt or ηt .



End of spec. Keep the inequality. Everything else is implementation detail.




                                                      7

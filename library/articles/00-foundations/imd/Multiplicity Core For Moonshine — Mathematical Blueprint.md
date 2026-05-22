---
slug: multiplicity-core-for-moonshine-mathematical-blueprint
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "00-foundations/imd/Multiplicity Core For Moonshine \u2014 Mathematical Blueprint.md"
  last_synced: '2026-03-20T17:17:22.247225Z'
---

Multiplicity Core for Moonshine — Mathematical
Blueprint
0. Scope and goal
A runtime-safe, mathematically grounded blueprint for Multiplicity Core targeted at moonshine-style
workloads. It removes category-theoretic formalism and keeps only the primitives supported by the docs:
projector kernel Π, ACE budgeted gain, PETC estimator/ledger, and sector-weight telemetry. The result is a
verifiable fixed‑point engine with certified contraction, block commutation, and conservation bookkeeping.




1. State space, channels, and gains
State space. Work in a real or complex Hilbert/Banach space H with norm ∥ ⋅ ∥ .


Channels. A finite index set P ("primes"). For each p ∈ P , a bounded linear operator Bp ∈ L(H) with
known bound ∥Bp ∥ ≤ bp and a typed tag used by PETC.


Gain. Per step t , weights wp,t ∈ R . Define the aggregate gain


                                            Kt = ∑ wp,t Bp .
                                                    p∈P


ACE budget. A strict small‑gain constraint holds each step:


                                     ∑ bp ∣wp,t ∣ ≤ τt ,      0 ≤ τt < 1.
                                     p∈P


External term. A bounded operator or vector‑valued map Ft (can be time‑varying) with Ft (0) finite and
Lipschitz on the certified window.




2. Projector kernel Π
Prime projectors. For each p , a projector Πp : H → H selecting the p -sector. Require idempotence and
orthogonality on the certified window: Π2p = Πp , Πp Πq = 0 for p  q ,=and ∑p Πp = ΠP , the projector
onto the prime span.


Scalar projector. Optionally a scalar projector      ΠS onto a certified subspace. All projectors are
nonexpansive: ∥Π∥ ≤ 1 .


Block commutation requirement. For every audited update operator Ut used inside the step, enforce




                                                     1
                       Ut Πp = Πp Ut      for all p ∈ P       (on the certified window).

Projector kernel. Choose Π ∈ {ΠP , ΠS } . Π is not a functor; it is a 1‑Lipschitz projector applied inside the
iteration to keep evolution on‑manifold and within budget.




3. PETC estimator and ledger (conservation bookkeeping)
Signature. A prime signature e ∈ ZP associated with typed operators. Composition is additive on the
signature monoid.


Ledger. For each step, PETC emits: (i) a per‑prime weight proposal wp,t consistent with typed updates; (ii) a
conservation certificate verifying that, for any typed split Y = ∑i Xi , the signature satisfies e(Y ) =
∑i e(Xi ) and that sector totals update losslessly.

Run‑time role. PETC is the source of wp,t used by ACE, and the sink for conservation checks. Fail‑closed
semantics hold: if conservation fails, freeze wp,t to last good and trigger rollback.




4. Runtime iteration
Define the state Tt ∈ H . The core iteration is


                                         Tt+1 = Π (Ft + Kt Tt ).

Telemetry. Maintain sector shares qp,t (nonnegative, summing to one) derived from Tt via the prime
projectors, an acceptance metric ME(t) ∈ [0, 1] that measures on‑manifold energy (e.g., the fraction
aligned with ΠP ), and an entropy H[qt ] over {qp,t } .




5. Certified contraction and convergence
Assumptions. For each t , ACE budget holds with margin 1 − τt > 0 . Projector Π is nonexpansive. Ft is
bounded and Lipschitz on the certified window. The operator application pipeline used inside the step
block‑commutes with {Πp } .

                                                      ^ t denote the realized linear part at step t
Theorem (linear convergence on certified window). Let K
                                        ^ t ∥ ≤ τt < 1 for all t , then the projected iteration is a contraction
restricted to the certified window. If ∥K
                                                                                                              ~
mapping each step and admits a unique fixed point on the window. Moreover, for any two trajectories Tt , Tt
driven by the same schedule,

                                               ~                 ~
                                       ∥Tt+1 − Tt+1 ∥ ≤ τt ∥Tt − Tt ∥.

Sketch. Π is 1‑Lipschitz. x ↦ Ft + Kt x is τt ‑Lipschitz by ACE. Composition is τt ‑Lipschitz. Apply Banach
fixed‑point theory stepwise.



                                                          2
6. Block commutation and invariants
Requirement. For any audited update Ut used inside Ft or building Kt , enforce Ut Πp = Πp Ut . This yields
sector‑wise invariance of the projected flow and enables per‑prime telemetry to be well‑posed.


Check. Measure the commutation residual Δp,t = ∥Ut Πp − Πp Ut ∥ . Accept only if maxp Δp,t ≤ η for a
configured η .




7. Conservation via PETC
Bookkeeping invariant. For any typed decomposition, PETC ensures exact additivity of prime signatures
and sector totals in the ledger. This is an accounting invariant, not a physical law.


Runtime rule. A step is valid only if PETC conservation checks pass and ACE remains within budget. On
violation: freeze sector weights to last good, project state with Π , and rollback or damp.




8. Sector metrics and acceptance
Define per‑prime share


                                  ∥Πp Tt ∥2
                       qp,t =                    (define 0/0 := 0),      ∑ qp,t = 1.
                                ∑r∈P ∥Πr Tt ∥2                            p

Define entropy H[qt ] = − ∑p qp,t log qp,t .


Define manifold energy ME(t) ∈ [0, 1] as the fraction of energy within the prime span, e.g.


                                                      ∥ΠP Tt ∥2
                                           ME(t) =               .
                                                      ∥Tt ∥2 + ε

                                                                ^ t ∥ ≤ τt ; - ME(t) ≥ 1 − ϵME ; -
Acceptance gates. Proceed only if - τt ≤ τmax < 1 and measured ∥K
entropy bounds hold: H[qt ] ∈ [Hmin , Hmax ] per policy; - commutation residual maxp Δp,t ≤ η ; - PETC
conservation passes.




9. Moonshine workload binding
This runtime is neutral to domain math. For moonshine, bind lanes to Fourier indices and classes and treat
arithmetic in the update map: - State lanes: buffers for coefficients cn (g) per index n and selected
conjugacy classes g . - Arithmetic map Ft : includes Hecke and replicability mixers acting on {cn (g)} ,




                                                     3
implemented as sparse stencils. These sit inside Ft and are audited to satisfy commutation on the certified
window. - Π and PETC operate as above; they are agnostic to the lane semantics.




10. Minimal algorithmic skeleton

  Initialize T_0, PETC ledger, Π (choose Π_P or Π_S), thresholds (τ_max, ε_ME, η,
  H-bounds).
  for t = 0,1,2,...:
      # Proposals and budget
       w_t ← PETC.propose_weights(T_t)
       assert Σ_p b_p |w_{p,t}| ≤ τ_max
       K_t ← Σ_p w_{p,t} B_p

       # Update map (domain-specific), audited
       U_t, F_t ← build_update(T_t)
       assert max_p ||U_t Π_p − Π_p U_t|| ≤ η

       # Projected step
       T_{t+1} ← Π ( F_t + K_t T_t )


       # Telemetry
       q_t ← sector_shares(T_{t+1}, {Π_p})
       ME_t ← manifold_energy(T_{t+1}, Π_P)
       assert ME_t ≥ 1 − ε_ME and H[q_t] within bounds

       # Ledger
       PETC.update(T_t → T_{t+1})           # check conservation; fail-closed on violation

       # Rollback/damping if any gate fails




11. Test plan (fastest path to proof)
1) Projective contraction. On synthetic linear cases with known ∥K∥ , verify empirical rate ρ satisfies ρ ≤
τmax . 2) Block commutation. Compute Δp,t over a window; require maxt maxp Δp,t ≤ η . 3) PETC
exactness. Stress splits/merges and verify signature additivity and exact sector totals. 4) Sector metrics.
Keep ME(t) ≥ 1 − ϵME and entropy within policy under representative workloads.




12. Requirements and limitations
Required. Strict ACE budget < 1 ; nonexpansive Π; audited operators that block‑commute with {Πp } ;
typed paths for PETC.




                                                     4
Limitations. Linear core guarantees; nonlinear variants require separate analysis. PETC conservation is
bookkeeping; in noisy regimes it may hold while the state drifts—detected and curtailed via Π , ME(t) ,
and entropy gates.




13. Optional moonshine notes
Use the core with moonshine arithmetic by placing Hecke/replicability in Ft . Treat index mixing as part of
the audited update. Keep Π and PETC unchanged. This preserves the blueprint and gives per‑index
observability without altering the runtime invariants.




Addendum v2 — Implementation‑critical revisions

A) Certified window (explicit definition, monitoring, boundary policy)

Definition. The certified window W is the set of states that satisfy all of: - Norm bound: ||T|| ≤ R. -
Manifold alignment: ME(T) ≥ 1 − eps_ME. - Commutation bound: max_p Delta_p(T) ≤ eta, measured against
the audited update U_t. - Entropy bounds: H_min ≤ H[q(T)] ≤ H_max.


Monitoring. Check membership T_t ∈ W before every step. Log margins to drive policy.


Boundary policy. If outside W: (1) soft backoff: scale weights by gamma in (0,1) and project T_t ← Pi T_t; (2)
guarded damping: shrink K_t by theta to restore budget and local Lipschitz; (3) hard rollback after L
consecutive breaches, then reduce R.




B) Projector kernel Pi — feasibility, approximations, and error impact

Constructions. 1. Disjoint partition projectors (exact, orthogonal) using coordinate masks. 2. Basis
projectors via QR/SVD on sector bases with regularization. 3. Soft projectors: Pi_hat = (1/2)(I + S) with S
firmly nonexpansive (prox/averaged operator).


Nonexpansiveness. Enforce ||Pi_hat|| ≤ 1 by design (averaging) and track its spectral bound at runtime.


Error propagation. With projector error delta = ||Pi_hat − Pi|| and commutation residual eta, the realized
step is at most (tau + delta + eta)‑Lipschitz on the certified window. Require tau + delta + eta < 1 to retain
contraction. Gate on measured delta and eta.


Risk note. Projector construction is the highest‑risk item. Treat delta as a first‑class runtime metric and
budget it like tau.




                                                      5
C) PETC currencies and conservation

Currencies. - Operation signature e_op: exact counts of typed ops (T_2, T_3, Pi, B_p). Fully conserved by
construction. - Sector energy ledger E_p: energy or norm per sector. PETC records a flux matrix Phi_{p->q}
per step so that E_q(t+1) = E_q(t) + sum_p Phi_{p->q} + R_q, where total residual sum_q R_q is bounded and
gated (epsilon_flux). - ACE weights w_{p,t}: proposed and budget‑checked.


Fail‑closed. On any ledger violation, freeze weights to last good and rollback or damp.




D) Minimal moonshine binding example (truncated toy that exercises all components)

State. H = sequences a[0..N] representing q‑series coefficients.


Sectors. P = {2,3} with disjoint index sets: - S2 = { n : n even and 3 not dividing n } - S3 = { n : n divisible by 3
and n odd } Let Pi_2 and Pi_3 be coordinate masks onto S2, S3; Pi_P = Pi_2 + Pi_3. The remainder S0 is
outside the prime span and is suppressed by Pi_P.


Channels. B_2, B_3 are diagonal scaling within their sectors: (B_p a)[n] = beta_{p,n} a[n] for n in S_p, zero
otherwise, with |beta_{p,n}| ≤ b_p.


Hecke‑style mixers inside F_t. - (T2 a)[n] = a[2n] + (n even ? a[n/2] : 0) - (T3 a)[n] = a[3n] + (n mod 3 == 0 ?
a[n/3] : 0) Use F_t = alpha2_t T2 a + alpha3_t T3 a + c * e_{-1} (with truncation guards at the boundaries).


Step. T_{t+1} = Pi( F_t + K_t T_t ), K_t = w2_t B_2 + w3_t B_3.


PETC. - e_op counts {T2, T3, Pi, B_2, B_3}. - Energy ledger: E_2 = ||Pi_2 a||^2, E_3 = ||Pi_3 a||^2. Compute
fluxes Phi_{p->q} induced by T2/T3 stencils; gate on total residual ≤ epsilon_flux.


Validation hooks. - Contraction: ||K_t|| ≤ |w2_t| b_2 + |w3_t| b_3 < tau. - Commutation: B_p commute
with Pi_p exactly; measure Delta_p for the T2/T3 part and enforce Delta_max ≤ eta.




E) Algorithmic skeleton corrections

      • Check ACE budget before forming K_t.
      • Insert certified window check and boundary policy at the top of the loop.
      • Add a flux‑balance gate (epsilon_flux) to acceptance.

(These revisions supersede the corresponding parts of §§1–3, 8–10 in the main blueprint.)




                                                          6

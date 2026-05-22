---
slug: kernel-clean-mathematical-revision
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "05-systems/\u03A0\u2011kernel/\u03A0\u2011kernel \u2014 Clean Mathematical\
    \ Revision.md"
  last_synced: '2026-03-20T17:17:17.813741Z'
---

Π‑kernel — Clean Mathematical Revision
Abstract
We define a Π‑indexed update kernel on a Hilbert space with per‑atom proposals and proximals. We
formalize analysis–synthesis via frame bounds, give an affine coefficient dynamics, provide a computable
small‑gain contraction condition, and certify stability with a quadratic Lyapunov function. Split‑step
execution with noncommuting operators is covered by an explicit commutator budget. All symbols are fixed
once.




1. Setting and Notation
      • Ambient space: complex separable Hilbert space H with inner product ⟨·,·⟩ and norm ∥·∥.
      • Indexing set: Π (finite or countable). For each π∈Π, an analysis operator R_π∈B(H).
      • Coefficients: c_{π}:=R_π x∈H_π (subspace for atom π). Stack c:=⨁{π} c. Block norms use the ℓ₂ sum
        over π.
      • Synthesis operator: S:=∑_{π} R_π. Perfect recomposition means S=I. General case allows defect
       δ:=∥I−S∥≥0.
      • Frame bounds (overlay energy control): there exist 0<A≤B<∞ with

                                         A∥x∥2 ≤ ∑ ∥Rπ x∥2 ≤ B∥x∥2 .
                                                       π

      • Neighbor graph: N_π⊆Π is the set of atoms that feed π’s proposal. Max degree Δ:=sup_π |N_π|.




2. Per‑Atom Proposal and Proximal Update
For each π and time t: - Proposal map. U_{π,t}: ⨁{π'∈N_π} H → H_π, assumed block‑Lipschitz:


                             ∥Uπ,t (z) − Uπ,t (z ′ )∥ ≤ ∑ LU ,ππ′ ,t ∥zπ′ − zπ′ ′ ∥.
                                                           π ′ ∈Nπ

- Proximal/averaged map. P_{π,t}: H_π→H_π, nonexpansive with constant L_{prox,π,t}≤1 (firmly
nonexpansive proximals have L_{prox}=1; if λ‑averaged then L_{prox}≤1−λ). - Relaxation. α_π∈(0,1]. -
Per‑atom update. With c_{π,t}:=R_π x_t and z_{π,t}:=U_{π,t}( (c_{π',t}){π'∈N_π} ),

                                    cπ,t+1 = (1 − απ )cπ,t + απ Pπ,t (zπ,t ).

Stacked form:

                           ct+1 = Kt ct + ft ,       Kt := diag(1 − απ ) + Dα Gt ,

with D_α:=diag(α_π), G_t the block‑Lipschitz bound induced by P, and f_t collects exogenous terms (set f_t=0 if
none).}∘U_{π,t




                                                           1
3. Small‑Gain Matrix and Contraction
Define the block small‑gain matrix M_t with entries


                                         (Mt )ππ′ := απ Lprox,π,t LU ,ππ′ ,t .

Pick a subordinate block norm ∥·∥◻ (e.g., block‑ℓ₂ or block‑ℓ∞). Sufficient condition for contraction in
coefficient space:

                                  sup ∥Mt ∥◻ < 1           ⇒      sup ∥Kt ∥◻ < 1.
                                    t                              t


In the uncoupled case (N_π={π}) this reduces to α_π L<1 for all π.} L_{U,ππ,t




4. Orthogonal Partition vs. Frame Overlay

4.1 Orthogonal partition (ideal case)

Assume R_π are orthogonal projections with R_π R_{π'}=0 for π≠π' and ∑π R_π=I. Then x_t=∑_π c and


                                        ∥xt+1 − x∗t ∥ ≤ ∥Kt ∥◻ ∥xt − x∗t ∥,

where x_t^* is the unique fixed point if ∥K_t∥_◻≤ρ<1 uniformly. Quadratic Lyapunov function V(c)=∑_π
w_π ∥c_π∥^2 with w_π>0 decreases by factor ≤ρ².


4.2 Frame overlay with synthesis defect

Let S=∑π R_π and δ=∥I−S∥. Then x=S c and



                                                       B                         B
                              ∥x∥ ≤ ∥S∥∥c∥ ≤             ∥c∥,          ∥c∥ ≤       ∥x∥.
                                                       A                         A
Moreover, ∥x − Sc∥ ≤ δ∥x∥ implies

                                                   B
                                    ∥xt+1 ∥ ≤        ∥Kt ∥◻ ∥ct ∥ + δ∥xt+1 ∥.
                                                   A
Solve for ∥x)∥x_t∥ to obtain the synthesis‑aware bound

                                                        B ∥Kt ∥◻
                                           ∥xt+1 ∥ ≤             ∥xt ∥.
                                                        A 1−δ

A uniform contraction holds if

                               B supt ∥Kt ∥◻
                                             ≤1−η               for some η ∈ (0, 1).
                               A    1−δ



                                                          2
}∥ and use ∥c_t∥ ≤ (\sqrt{B}/\sqrt{A




5. Lyapunov Certificate
Let W=diag(w_π I_{H_π}) with w_π>0 and define V(c)=⟨c, W c⟩. If ∥Kt ∥W ≤ 1 − η for all t under the induced
norm, then


                                         V (ct+1 ) − V (ct ) ≤ −η V (ct ).
                                                                 ~
In the frame case, combine with §4.2 to obtain a decrease of V (x) := B
                                                                      A
                                                                        V (c) provided
                                              B 1
                                    (1 − η)         ≤ 1 − η~ (η~ > 0).
                                              A 1−δ
Pick weights w_π to tighten the bound via scaling of M_t.




6. Regularity and Prox Assumptions
      • Proximals used must be nonexpansive; firmly nonexpansive maps satisfy ∥P u−P v∥^2 ≤ ⟨P u−P v,
        u−v⟩, hence 1‑Lipschitz. If P=(1−λ)I+λ T with nonexpansive T and λ∈(0,1], then L_{prox}≤1−λ.
      • Proposal maps must satisfy the stated block‑Lipschitz bounds with finite degree Δ to keep
        ∥M_t∥_◻ estimable.
      • Time variation: assume parameter measurability in t and uniform bounds on L_{U,ππ',t} and
        L_{prox,π,t}.




7. Split‑Step Execution and Noncommutation
For operator splitting with A_t and B_t acting on x, use Strang splitting

                                    Δt          Δt
                                  e 2 At eΔtBt e 2 At = eΔt(At +Bt ) + O(Δt3 ).

Control the local error via a commutator budget

                                            ∥[At , Bt ]∥ Δt2 ≤ εsplit ,

and ensure the residual εsplit fits inside the slack η from §4–§5 so the net step remains contractive.




8. Algorithm (Synthesis‑Aware)
Inputs: x_0, horizon T, operators {R_π}, frame constants (A,B), defect δ, maps U_{π,t}, P_{π,t}, relaxations
α_π.




                                                        3
 # Precompute bounds
 compute A, B, δ, and choose block norm ∥·∥_◻
 estimate L_{U,ππ',t}, L_{prox,π,t} ⇒ M_t and K_t bounds
 require sup_t ∥M_t∥_◻ < 1 and (B/A) sup_t ∥K_t∥_◻ /(1−δ) ≤ 1−η

 # Iteration
 x ← x0
 for t = 0 … T−1:
     # Analysis
     for π in Π:
          c[π] ← R_π x


     # Per‑atom proposals and proximal steps
     for π in Π:
          z[π] ← U_{π,t}( {c[π'] : π' ∈ N_π} )
          c[π] ← (1−α[π]) * c[π] + α[π] * P_{π,t}( z[π] )

     # Synthesis with defect control
     x ← S c
     # Optional: if ∥I−S∥ is large, project x ← (I−(I−S)) x or reduce step sizes

     # Runtime checks (see §9)




9. Runtime Checks (Computable)
  1. Estimate A, B from sample batches; track κ := B/A .
  2. Track δ=∥I−S∥ and enforce δ≤δ_max.
  3. Maintain online bounds for L_{U,ππ',t} and L_{prox,π,t}; compute ∥Mt ∥◻ and ∥Kt ∥◻ .
  4. Require ∥Mt ∥◻ ≤ 1 − ϵ and κ∥Kt ∥◻ /(1 − δ) ≤ 1 − η with fixed ϵ, η > 0 .
  5. If splitting is used, ensure ∥[At , Bt ]∥Δt2 ≤ ηsplit and ηsplit < η .




10. Summary of Guarantees
   • Unique fixed point of the affine coefficient dynamics when supt ∥Kt ∥◻ < 1 .
   • Exponential convergence in coefficient norm; exponential convergence in state norm with factor
     bounded by (B/A)∥Kt ∥◻ /(1 − δ) .
   • Robustness to time variation and partial updates as long as the uniform bounds hold and the
     small‑gain condition is preserved.




                                                      4

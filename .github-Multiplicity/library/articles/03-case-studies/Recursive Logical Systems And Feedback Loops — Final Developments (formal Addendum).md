---
slug: recursive-logical-systems-and-feedback-loops-final-developments-formal-addendum
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "03-case-studies/Recursive Logical Systems And Feedback Loops \u2014 Final\
    \ Developments (formal Addendum).md"
  last_synced: '2026-03-20T17:17:21.560681Z'
---

Recursive Logical Systems and Feedback Loops —
Final Developments
This document consolidates the latest refinements into a single, camera-ready addendum. It is designed to
be appended after the current “Camera-Ready Version” section.




1. Semantics Options (Continuity-Preserving)
We retain the core setting: - atoms A = {p1 , … , pn ), valuations x ∈ [0, 1]n , and an update operator Φ :
[0, 1]n → [0, 1]n defined coordinatewise by formulas φi .

1.1 Łukasiewicz (default)

¬a = 1 − a, a ∧L b       = max(0, a + b − 1), a ∨L b = min(1, a + b), a →L b          = min(1, 1 − a + b).

1.2 Idempotent–Continuous Variant (optional)

To address non-idempotence of ∧L while preserving continuity (and thus the Brouwer existence pipeline),
we may optionally use:


        ¬a = 1 − a, a ∧I b     = min(a, b), a ∨I b = max(a, b), a →L b          = min(1, 1 − a + b).

Note. This choice is not the standard Gödel residuated implication (which is generally discontinuous); it is a
continuity-preserving hybrid intended for dynamical fixed-point semantics.




2. Convergence: Regionwise Affine Dynamics (Main Practical Tool)
Recall the damped update


                          xt+1 = F (xt ) = (1 − α)xt + αΦ(xt ),         α ∈ (0, 1].

2.1 Local linear convergence on a linearity region

Because Łukasiewicz semantics is continuous piecewise-affine, Φ is affine on each region of linearity.


Theorem (Local convergence on an affine region). Let x∗ be a fixed point of Φ. Suppose there exists a
neighborhood U of x∗ such that


                                 Φ(x) = A(x − x∗ ) + x∗       for all x ∈ U .

Then




                                                      1
                            F (x) = B(x − x∗ ) + x∗ ,           B = (1 − α)I + αA.

If ρ(B) < 1 (spectral radius), then for all x0 sufficiently close to x∗ , the iterates xt+1 = F (xt ) converge to
x∗ at a linear rate.

Caveat. This is a local diagnostic: if trajectories cross region boundaries, the affine matrix A (hence B )
changes.




3. MILP as Ground-Truth Oracle (with Practical Solver Notes)
The fixed-point condition Φ(x) = x can be encoded exactly as a MILP by introducing auxiliary variables for
subexpressions and linearizing min / max with binary variables.


3.1 Safe big-M

Use M = 2 as a uniform constant since affine pre-activations such as a + b and 1 − a + b range over [0, 2]
when a, b ∈ [0, 1].


3.2 Solver-native constraints

Many MILP solvers support indicator constraints or general constraints for min / max. Using these
(when available) can significantly improve relaxations compared to manual big-M .


3.3 “All fixed points” enumeration

To enumerate multiple fixed points, solve repeatedly and add no-good cuts (or use a solution pool) to
exclude previously found solutions.


3.4 Structural acceleration

Before encoding, compute the dependency graph and decompose into SCCs. Encode only strongly
connected components that actually require fixed-point solving.




4. Tensor Surrogate: Semantics-Consistent Training
                     ^θ (φ; x) is trained to approximate [[φ]]x while maintaining compositional consistency.
The tensor surrogate v


4.1 Loss with identity regularization

                 L(θ) = E(x,φ) [(v^θ (φ; x) − [[φ]]x )2 ] + λ E(x,ψ≡χ) [(v^θ (ψ; x) − v^θ (χ; x))2 ].

Use only identities valid in the chosen semantics (e.g., double negation, De Morgan, commutativity/
associativity of ∧, ∨). Avoid regularizing excluded middle p ∨ ¬p = 1, which fails in Łukasiewicz.




                                                          2
5. Proof Search Guidance: Energy per Cost
Given proof state s as a set of sequents and energy


                                  E(s) = ∑ (1 − [[⋀ Γ → ⋁ Δ]]x ),
                                              Γ⊢Δ∈s

choose an inference rule r that optimizes expected energy reduction per computational cost:

                                        E[ΔEr ]
                         r ∈ arg max                  (optionally with exploration).
                                    r    c(r)

The tensor surrogate can be used to cheaply estimate ΔEr before exact semantic evaluation.




6. First-Order Extension (Semantic Definition vs Approximation)
For a domain U (possibly infinite), define:


                          [[∀x φ(x)]] = inf [[φ(d)]],       [[∃x φ(x)]] = sup[[φ(d)]].
                                         d∈U                              d∈U

Implementation may approximate these with sampling/active selection. This is an approximation
algorithm, not a change in the semantic definition.




7. Reference Code Snippet (Semantics Options + Damped Iteration)

  import math
  from dataclasses import dataclass
  from typing import Dict, List, Tuple, Union, Callable

  AST = Union[str, Tuple]          # atom or (op, ...)

  # --- Semantics modules ---

  class Lukasiewicz:
      @staticmethod
      def neg(a: float) -> float:
          return 1.0 - a

       @staticmethod
       def and_(a: float, b: float) -> float:
           return max(0.0, a + b - 1.0)

       @staticmethod
       def or_(a: float, b: float) -> float:




                                                        3
           return min(1.0, a + b)

    @staticmethod
    def implies(a: float, b: float) -> float:
        return min(1.0, 1.0 - a + b)



class IdempotentContinuous:
    """Idempotent ∧/∨ via min/max; keep neg=1-a and Łukasiewicz implication for
continuity."""

    @staticmethod
    def neg(a: float) -> float:
        return 1.0 - a

    @staticmethod
    def and_(a: float, b: float) -> float:
        return min(a, b)

    @staticmethod
    def or_(a: float, b: float) -> float:
        return max(a, b)

    @staticmethod
    def implies(a: float, b: float) -> float:
        return min(1.0, 1.0 - a + b)



# --- Recursive system ---

@dataclass
class RecursiveLogicSystem:
    atoms: List[str]
    formulas: Dict[str, AST]           # atom -> AST
    alpha: float = 0.5
    logic: object = Lukasiewicz        # choose Lukasiewicz or IdempotentContinuous

    def evaluate(self, v: Dict[str, float], phi: AST) -> float:
        if isinstance(phi, str):
            return float(v[phi])
        op = phi[0]
        if op == '¬':
            return self.logic.neg(self.evaluate(v, phi[1]))
           if op == '∧':
               return self.logic.and_(self.evaluate(v, phi[1]), self.evaluate(v,
phi[2]))
           if op == '∨':




                                          4
               return self.logic.or_(self.evaluate(v, phi[1]), self.evaluate(v,
phi[2]))
           if op == '→':
               return self.logic.implies(self.evaluate(v, phi[1]), self.evaluate(v,
phi[2]))
           raise ValueError(f"Unknown op: {op}")

    def Phi(self, v: Dict[str, float]) -> Dict[str, float]:
        return {a: self.evaluate(v, self.formulas[a]) for a in self.atoms}

    def step(self, v: Dict[str, float]) -> Dict[str, float]:
        pv = self.Phi(v)
        a = self.alpha
        return {k: (1.0 - a) * v[k] + a * pv[k] for k in self.atoms}

    def iterate(self, v0: Dict[str, float], tol: float = 1e-8, max_iter: int =
5000) -> Dict[str, float]:
        v = {k: float(v0[k]) for k in self.atoms}
        for _ in range(max_iter):
            vn = self.step(v)
            err = max(abs(vn[k] - v[k]) for k in self.atoms)
            v = vn
            if err < tol:
                 break
        return v



# --- Example: P ↔ (P ∧ Q), Q ↔ ¬P ---

atoms = ['P', 'Q']
formulas = {
    'P': ('∧', 'P', 'Q'),
    'Q': ('¬', 'P')
}

sys_L = RecursiveLogicSystem(atoms=atoms, formulas=formulas, alpha=0.5,
logic=Lukasiewicz)
sys_I = RecursiveLogicSystem(atoms=atoms, formulas=formulas, alpha=0.5,
logic=IdempotentContinuous)

v0 = {'P': 0.8, 'Q': 0.3}
print("Łukasiewicz:", sys_L.iterate(v0))
print("Idempotent variant:", sys_I.iterate(v0))




                                          5
8. Suggested Validation Addendum
   • Semantics comparison: run the same benchmark suite under Łukasiewicz vs the idempotent–
     continuous variant; compare fixed-point distributions (Boolean vs interior) and stability basins.
   • Solver triad: tensor surrogate → damped refinement → MILP verification.
   • Boolean-slice benchmark: enumerate fixed points under MILP and measure when thresholding
     succeeds/fails; correlate with polarity/antitone structure and SCC size.




                                                   6

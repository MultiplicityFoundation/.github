
# Generate the complete I-ACFL module file scaffold and test workbench

iacfl_files = {}

# ============================================================
# shared/types.py — shared types (referenced by iacfl)
# ============================================================
iacfl_files["packages/dnakey/src/shared/__init__.py"] = '''"""Shared types and interfaces for DNA KEY modules."""
'''

iacfl_files["packages/dnakey/src/shared/types.py"] = '''"""Shared type definitions for forward and inverted operator modules."""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from enum import Enum
import numpy as np


class OperatorMode(Enum):
    FORWARD = "forward"
    INVERTED = "inverted"
    BLEND = "blend"


class TruthCategory(Enum):
    ABSOLUTELY_FALSE = (0.0, "Absolutely false")
    ALMOST_FALSE = (0.1, "Almost false")
    QUITE_FALSE = (0.2, "Quite false")
    SOMEWHAT_FALSE = (0.3, "Somewhat false")
    MORE_FALSE_THAN_TRUE = (0.4, "More false than true")
    AS_TRUE_AS_FALSE = (0.5, "As true as false")
    MORE_TRUE_THAN_FALSE = (0.6, "More true than false")
    SOMEWHAT_TRUE = (0.7, "Somewhat true")
    ENOUGH_TRUE = (0.8, "Enough true")
    ALMOST_TRUE = (0.9, "Almost true")
    ABSOLUTELY_TRUE = (1.0, "Absolutely true")

    @classmethod
    def from_value(cls, v: float) -> "TruthCategory":
        closest = min(cls, key=lambda c: abs(c.value[0] - v))
        return closest


@dataclass(frozen=True)
class OperatorResult:
    """Result of any fuzzy operator evaluation."""
    value: float
    inputs: Tuple[float, ...]
    weights: Optional[Tuple[float, ...]] = None
    mode: OperatorMode = OperatorMode.FORWARD
    truth_category: Optional[str] = None
    metadata: Dict = field(default_factory=dict)


@dataclass(frozen=True)
class DivergenceResult:
    """Result of divergence analysis between two operator evaluations."""
    forward_value: float
    inverted_value: float
    delta: float
    relative_delta: float
    inputs: Tuple[float, ...]
    metadata: Dict = field(default_factory=dict)


@dataclass(frozen=True)
class BlendResult:
    """Result of parameterized blend between forward and inverted operators."""
    blended_value: float
    alpha: float
    forward_value: float
    inverted_value: float
    inputs: Tuple[float, ...]
    metadata: Dict = field(default_factory=dict)


@dataclass
class AdversarialReport:
    """Report from adversarial harness comparing operator systems."""
    total_cases: int = 0
    max_divergence: float = 0.0
    mean_divergence: float = 0.0
    decision_reversals: int = 0
    reversal_rate: float = 0.0
    worst_case_inputs: Optional[Tuple[float, ...]] = None
    divergence_distribution: Optional[np.ndarray] = None
    metadata: Dict = field(default_factory=dict)
'''

iacfl_files["packages/dnakey/src/shared/operators.py"] = '''"""Base operator abstract classes and protocols."""

from abc import ABC, abstractmethod
from typing import Tuple
from shared.types import OperatorResult


class FuzzyConjunction(ABC):
    """Abstract base for all conjunction operators (forward and inverted)."""

    @abstractmethod
    def evaluate(self, inputs: Tuple[float, ...]) -> OperatorResult:
        ...

    @abstractmethod
    def arity(self) -> int:
        ...


class FuzzyDisjunction(ABC):
    """Abstract base for all disjunction operators."""

    @abstractmethod
    def evaluate(self, inputs: Tuple[float, ...]) -> OperatorResult:
        ...


class FuzzyNegation(ABC):
    """Abstract base for negation operators."""

    @abstractmethod
    def evaluate(self, x: float) -> float:
        ...
'''

iacfl_files["packages/dnakey/src/shared/validators.py"] = '''"""Shared validation utilities for operator modules."""

from typing import Tuple
import numpy as np


def validate_inputs(inputs: Tuple[float, ...], min_arity: int = 2) -> None:
    """Validate all inputs are in [0,1] and arity >= min_arity."""
    if len(inputs) < min_arity:
        raise ValueError(f"Arity must be >= {min_arity}, got {len(inputs)}")
    for i, x in enumerate(inputs):
        if not (0.0 <= x <= 1.0):
            raise ValueError(f"Input at position {i} is {x}, must be in [0,1]")


def validate_alpha(alpha: float) -> None:
    """Validate blend parameter alpha is in [0,1]."""
    if not (0.0 <= alpha <= 1.0):
        raise ValueError(f"Alpha must be in [0,1], got {alpha}")


def is_close(a: float, b: float, tol: float = 1e-10) -> bool:
    """Numerical closeness check."""
    return abs(a - b) < tol
'''

# ============================================================
# iacfl/ — I-ACFL standalone module
# ============================================================
iacfl_files["packages/dnakey/src/iacfl/__init__.py"] = '''"""
I-ACFL: Inverted Archimedean Compensatory Fuzzy Logic Module

Standalone inversion module for ACFL operators.
Provides inverted conjunction, inverted disjunction, divergence analysis,
parameterized blending, and adversarial testing harness.

Architecture: Sibling module to acfl/, imports shared types from shared/.
Hierarchy: CRMF governs -> ACFL reasons -> I-ACFL tests boundaries.
"""

__version__ = "0.1.0"

from iacfl.operators import (
    InvertedConjunction,
    InvertedDisjunction,
    StandardConjunction,
    StandardDisjunction,
    StandardNegation,
)
from iacfl.divergence import DivergenceAnalyzer
from iacfl.blend import ParameterizedBlend
from iacfl.adversarial import ACFLAdversarialHarness
'''

iacfl_files["packages/dnakey/src/iacfl/operators.py"] = '''"""
I-ACFL Operators: Standard and Inverted ACFL conjunction/disjunction.

Standard ACFL conjunction (GMBCL):
    c(x1,...,xn) = prod(xi)^(1/n)

Inverted ACFL conjunction:
    c_inv(x1,...,xn) = 1 - prod(1 - xi)^(1/n)

Standard ACFL disjunction (De Morgan dual):
    d(x1,...,xn) = 1 - prod(1 - xi)^(1/n)

Inverted ACFL disjunction:
    d_inv(x1,...,xn) = prod(xi)^(1/n)

Standard negation:
    n(x) = 1 - x
"""

from typing import Tuple, Optional
import numpy as np

from shared.types import OperatorResult, OperatorMode, TruthCategory
from shared.validators import validate_inputs


class StandardConjunction:
    """ACFL standard conjunction: GMBCL with uniform 1/n weights.
    
    c(x1,...,xn) = prod(xi^(1/n))
    
    Axioms satisfied:
        i.   Compensation: min(x) <= c(x) <= max(x)
        ii.  Commutativity: c(x1,...,xn) = c(x_sigma(1),...,x_sigma(n))
        iii. Strict monotonicity: dc/dxi > 0 when xi > 0
        iv.  Veto: if any xi = 0, c = 0
        v.   Reciprocity: c(x,y) + c(1-x,1-y) = 1
        vi.  Transitivity: inherits from >= on R
        vii. De Morgan: n(c(x)) = d(n(x))
    """

    def evaluate(self, inputs: Tuple[float, ...]) -> OperatorResult:
        validate_inputs(inputs)
        n = len(inputs)
        
        # Veto check: any zero kills the conjunction
        if any(x == 0.0 for x in inputs):
            value = 0.0
        else:
            log_sum = sum(np.log(x) for x in inputs)
            value = np.exp(log_sum / n)
        
        tc = TruthCategory.from_value(value)
        return OperatorResult(
            value=value,
            inputs=inputs,
            weights=tuple(1.0 / n for _ in inputs),
            mode=OperatorMode.FORWARD,
            truth_category=tc.value[1],
        )


class InvertedConjunction:
    """I-ACFL inverted conjunction.
    
    c_inv(x1,...,xn) = 1 - prod((1 - xi)^(1/n))
    
    Properties:
        - Inverts the veto: all inputs must be 0 for output to be 0
        - Anti-pessimistic: high inputs dominate
        - Equivalent to standard disjunction under De Morgan
        - The key test: does c_inv produce novel behavior vs d(x)?
    """

    def evaluate(self, inputs: Tuple[float, ...]) -> OperatorResult:
        validate_inputs(inputs)
        n = len(inputs)
        complements = tuple(1.0 - x for x in inputs)
        
        # If any complement is 0 (i.e., input is 1), product term = 0
        if any(c == 0.0 for c in complements):
            product = 0.0
        else:
            log_sum = sum(np.log(c) for c in complements)
            product = np.exp(log_sum / n)
        
        value = 1.0 - product
        tc = TruthCategory.from_value(value)
        return OperatorResult(
            value=value,
            inputs=inputs,
            weights=tuple(1.0 / n for _ in inputs),
            mode=OperatorMode.INVERTED,
            truth_category=tc.value[1],
        )


class StandardDisjunction:
    """ACFL standard disjunction (De Morgan dual of conjunction).
    
    d(x1,...,xn) = 1 - prod((1 - xi)^(1/n))
    """

    def evaluate(self, inputs: Tuple[float, ...]) -> OperatorResult:
        validate_inputs(inputs)
        n = len(inputs)
        complements = tuple(1.0 - x for x in inputs)
        
        if any(c == 0.0 for c in complements):
            product = 0.0
        else:
            log_sum = sum(np.log(c) for c in complements)
            product = np.exp(log_sum / n)
        
        value = 1.0 - product
        tc = TruthCategory.from_value(value)
        return OperatorResult(
            value=value,
            inputs=inputs,
            weights=tuple(1.0 / n for _ in inputs),
            mode=OperatorMode.FORWARD,
            truth_category=tc.value[1],
        )


class InvertedDisjunction:
    """I-ACFL inverted disjunction.
    
    d_inv(x1,...,xn) = prod(xi^(1/n))
    
    This is the De Morgan dual of the inverted conjunction.
    Equivalent to the standard conjunction — confirmed by construction.
    """

    def evaluate(self, inputs: Tuple[float, ...]) -> OperatorResult:
        validate_inputs(inputs)
        n = len(inputs)
        
        if any(x == 0.0 for x in inputs):
            value = 0.0
        else:
            log_sum = sum(np.log(x) for x in inputs)
            value = np.exp(log_sum / n)
        
        tc = TruthCategory.from_value(value)
        return OperatorResult(
            value=value,
            inputs=inputs,
            weights=tuple(1.0 / n for _ in inputs),
            mode=OperatorMode.INVERTED,
            truth_category=tc.value[1],
        )


class StandardNegation:
    """Standard fuzzy negation: n(x) = 1 - x."""

    def evaluate(self, x: float) -> float:
        if not (0.0 <= x <= 1.0):
            raise ValueError(f"Input {x} must be in [0,1]")
        return 1.0 - x
'''

iacfl_files["packages/dnakey/src/iacfl/divergence.py"] = '''"""
Divergence Analyzer: Measures delta between standard and inverted ACFL operators.

Key metrics:
    - Absolute divergence: |c_standard(x) - c_inverted(x)|
    - Relative divergence: delta / max(c_standard, c_inverted, epsilon)
    - Distribution statistics across random input populations
    - Boundary behavior at veto points, unity points, and midpoints
"""

from typing import Tuple, List, Optional
import numpy as np

from shared.types import DivergenceResult, OperatorResult
from shared.validators import validate_inputs
from iacfl.operators import StandardConjunction, InvertedConjunction


class DivergenceAnalyzer:
    """Analyzes divergence between standard ACFL and I-ACFL operators."""

    def __init__(self):
        self.forward = StandardConjunction()
        self.inverted = InvertedConjunction()

    def analyze_single(self, inputs: Tuple[float, ...]) -> DivergenceResult:
        """Compute divergence for a single input vector."""
        fwd = self.forward.evaluate(inputs)
        inv = self.inverted.evaluate(inputs)
        delta = abs(fwd.value - inv.value)
        denom = max(fwd.value, inv.value, 1e-12)
        return DivergenceResult(
            forward_value=fwd.value,
            inverted_value=inv.value,
            delta=delta,
            relative_delta=delta / denom,
            inputs=inputs,
        )

    def analyze_population(
        self, 
        arity: int, 
        n_samples: int = 10000, 
        seed: int = 42
    ) -> dict:
        """Run divergence analysis across random input population.
        
        Returns:
            dict with keys: max_delta, mean_delta, std_delta, median_delta,
                           percentile_95, percentile_99, worst_case_inputs,
                           all_deltas (np.ndarray)
        """
        rng = np.random.default_rng(seed)
        deltas = np.zeros(n_samples)
        worst_delta = 0.0
        worst_inputs = None

        for i in range(n_samples):
            inputs = tuple(rng.uniform(0.0, 1.0, size=arity))
            result = self.analyze_single(inputs)
            deltas[i] = result.delta
            if result.delta > worst_delta:
                worst_delta = result.delta
                worst_inputs = inputs

        return {
            "arity": arity,
            "n_samples": n_samples,
            "max_delta": float(np.max(deltas)),
            "mean_delta": float(np.mean(deltas)),
            "std_delta": float(np.std(deltas)),
            "median_delta": float(np.median(deltas)),
            "percentile_95": float(np.percentile(deltas, 95)),
            "percentile_99": float(np.percentile(deltas, 99)),
            "worst_case_inputs": worst_inputs,
            "all_deltas": deltas,
        }

    def analyze_boundary(self, arity: int) -> List[DivergenceResult]:
        """Test divergence at critical boundary points.
        
        Boundary cases:
            - All zeros (veto)
            - All ones (unity)
            - All 0.5 (midpoint)
            - One zero, rest 0.5 (single veto)
            - One zero, rest 1.0 (veto vs unity)
            - Alternating 0.1 and 0.9
        """
        cases = [
            tuple(0.0 for _ in range(arity)),          # all zeros
            tuple(1.0 for _ in range(arity)),          # all ones
            tuple(0.5 for _ in range(arity)),          # all midpoint
            tuple([0.0] + [0.5] * (arity - 1)),       # single veto
            tuple([0.0] + [1.0] * (arity - 1)),       # veto vs unity
            tuple(0.1 if i % 2 == 0 else 0.9 
                  for i in range(arity)),               # alternating
            tuple([0.01] + [0.99] * (arity - 1)),     # extreme spread
        ]
        return [self.analyze_single(c) for c in cases]
'''

iacfl_files["packages/dnakey/src/iacfl/blend.py"] = '''"""
Parameterized Blend: Continuous interpolation between forward and inverted ACFL.

    c_alpha(x) = alpha * c_standard(x) + (1 - alpha) * c_inverted(x)

Properties:
    - alpha = 1.0: pure standard ACFL conjunction
    - alpha = 0.0: pure inverted ACFL conjunction
    - alpha = 0.5: midpoint blend
    - Continuous in alpha for fixed inputs
    - Preserves [0,1] output range by convexity
"""

from typing import Tuple, List
import numpy as np

from shared.types import BlendResult
from shared.validators import validate_inputs, validate_alpha
from iacfl.operators import StandardConjunction, InvertedConjunction


class ParameterizedBlend:
    """Blends standard and inverted ACFL operators along alpha axis."""

    def __init__(self):
        self.forward = StandardConjunction()
        self.inverted = InvertedConjunction()

    def evaluate(
        self, inputs: Tuple[float, ...], alpha: float = 0.5
    ) -> BlendResult:
        """Compute blended operator value.
        
        Args:
            inputs: tuple of truth values in [0,1]
            alpha: blend parameter in [0,1]
                   1.0 = pure forward, 0.0 = pure inverted
        """
        validate_inputs(inputs)
        validate_alpha(alpha)

        fwd = self.forward.evaluate(inputs)
        inv = self.inverted.evaluate(inputs)
        blended = alpha * fwd.value + (1.0 - alpha) * inv.value

        return BlendResult(
            blended_value=blended,
            alpha=alpha,
            forward_value=fwd.value,
            inverted_value=inv.value,
            inputs=inputs,
        )

    def sweep_alpha(
        self, inputs: Tuple[float, ...], steps: int = 101
    ) -> List[BlendResult]:
        """Sweep alpha from 0.0 to 1.0 and return all blend results."""
        alphas = np.linspace(0.0, 1.0, steps)
        return [self.evaluate(inputs, alpha=float(a)) for a in alphas]

    def find_crossover(
        self, inputs: Tuple[float, ...], threshold: float = 0.5
    ) -> float:
        """Find the alpha where the blended value crosses a threshold.
        
        Returns alpha in [0,1] or -1.0 if no crossover exists.
        """
        results = self.sweep_alpha(inputs, steps=1001)
        for i in range(1, len(results)):
            prev = results[i - 1].blended_value
            curr = results[i].blended_value
            if (prev - threshold) * (curr - threshold) <= 0:
                # Linear interpolation for crossover point
                alpha_prev = results[i - 1].alpha
                alpha_curr = results[i].alpha
                if abs(curr - prev) < 1e-15:
                    return alpha_curr
                frac = (threshold - prev) / (curr - prev)
                return alpha_prev + frac * (alpha_curr - alpha_prev)
        return -1.0
'''

iacfl_files["packages/dnakey/src/iacfl/adversarial.py"] = '''"""
Adversarial Harness: Tests forward ACFL against inverted ACFL.

Purpose:
    - Identify input regions where inversion changes decision outcomes
    - Measure decision reversal rate (forward says X, inverted says Y)
    - Find worst-case divergence inputs
    - Generate adversarial test vectors for upstream modules (WKD, DHT)
"""

from typing import Tuple, List, Optional, Dict
import numpy as np

from shared.types import AdversarialReport, DivergenceResult
from iacfl.operators import StandardConjunction, InvertedConjunction
from iacfl.divergence import DivergenceAnalyzer


class ACFLAdversarialHarness:
    """Adversarial testing harness comparing ACFL vs I-ACFL."""

    def __init__(self, decision_threshold: float = 0.5):
        """
        Args:
            decision_threshold: truth value above which a predicate
                                is considered "decided true"
        """
        self.analyzer = DivergenceAnalyzer()
        self.forward = StandardConjunction()
        self.inverted = InvertedConjunction()
        self.threshold = decision_threshold

    def run(
        self, 
        arity: int, 
        n_samples: int = 10000, 
        seed: int = 42
    ) -> AdversarialReport:
        """Execute full adversarial analysis.
        
        Measures:
            - Max divergence
            - Mean divergence
            - Decision reversal rate
            - Worst-case inputs
        """
        rng = np.random.default_rng(seed)
        deltas = np.zeros(n_samples)
        reversals = 0
        worst_delta = 0.0
        worst_inputs = None

        for i in range(n_samples):
            inputs = tuple(rng.uniform(0.0, 1.0, size=arity))
            fwd = self.forward.evaluate(inputs).value
            inv = self.inverted.evaluate(inputs).value
            delta = abs(fwd - inv)
            deltas[i] = delta

            # Decision reversal: one above threshold, other below
            fwd_decision = fwd >= self.threshold
            inv_decision = inv >= self.threshold
            if fwd_decision != inv_decision:
                reversals += 1

            if delta > worst_delta:
                worst_delta = delta
                worst_inputs = inputs

        return AdversarialReport(
            total_cases=n_samples,
            max_divergence=float(np.max(deltas)),
            mean_divergence=float(np.mean(deltas)),
            decision_reversals=reversals,
            reversal_rate=reversals / n_samples,
            worst_case_inputs=worst_inputs,
            divergence_distribution=deltas,
            metadata={
                "arity": arity,
                "threshold": self.threshold,
                "seed": seed,
            },
        )

    def targeted_adversarial(
        self, 
        arity: int, 
        n_attempts: int = 50000,
        seed: int = 42
    ) -> Dict:
        """Search for maximum-divergence inputs via random sampling.
        
        Focuses on inputs near decision boundary (forward ~= threshold)
        where inversions are most likely to flip decisions.
        """
        rng = np.random.default_rng(seed)
        best_delta = 0.0
        best_inputs = None
        boundary_reversals = []

        for _ in range(n_attempts):
            inputs = tuple(rng.uniform(0.0, 1.0, size=arity))
            fwd = self.forward.evaluate(inputs).value
            inv = self.inverted.evaluate(inputs).value
            delta = abs(fwd - inv)

            if delta > best_delta:
                best_delta = delta
                best_inputs = inputs

            # Track cases near decision boundary
            if abs(fwd - self.threshold) < 0.05:
                boundary_reversals.append({
                    "inputs": inputs,
                    "forward": fwd,
                    "inverted": inv,
                    "delta": delta,
                    "reversal": (fwd >= self.threshold) != (inv >= self.threshold),
                })

        return {
            "max_divergence": best_delta,
            "max_divergence_inputs": best_inputs,
            "boundary_cases": len(boundary_reversals),
            "boundary_reversals": sum(
                1 for b in boundary_reversals if b["reversal"]
            ),
            "boundary_reversal_rate": (
                sum(1 for b in boundary_reversals if b["reversal"])
                / max(len(boundary_reversals), 1)
            ),
        }
'''

iacfl_files["packages/dnakey/src/iacfl/validators.py"] = '''"""
I-ACFL Validators: Axiom verification for inverted operators.

Tests which ACFL axioms survive inversion and which break.
Documents the axiom profile of I-ACFL operators.
"""

from typing import Tuple, List, Dict
import numpy as np
from itertools import permutations

from iacfl.operators import InvertedConjunction, InvertedDisjunction, StandardNegation


class IACFLAxiomValidator:
    """Validates ACFL axioms i-vii against inverted operators."""

    def __init__(self, tolerance: float = 1e-10):
        self.inv_conj = InvertedConjunction()
        self.inv_disj = InvertedDisjunction()
        self.negation = StandardNegation()
        self.tol = tolerance

    def check_compensation(
        self, inputs: Tuple[float, ...]
    ) -> Dict:
        """Axiom i: min(x) <= c_inv(x) <= max(x)."""
        result = self.inv_conj.evaluate(inputs)
        mn, mx = min(inputs), max(inputs)
        holds = (mn - self.tol) <= result.value <= (mx + self.tol)
        return {
            "axiom": "i_compensation",
            "holds": holds,
            "value": result.value,
            "min_input": mn,
            "max_input": mx,
        }

    def check_commutativity(
        self, inputs: Tuple[float, ...]
    ) -> Dict:
        """Axiom ii: c_inv(x_sigma) = c_inv(x) for all permutations sigma."""
        base = self.inv_conj.evaluate(inputs).value
        # Test a sample of permutations (full set is n!)
        n = len(inputs)
        if n <= 5:
            perms = list(permutations(inputs))
        else:
            rng = np.random.default_rng(0)
            indices = [rng.permutation(n) for _ in range(120)]
            perms = [tuple(inputs[i] for i in idx) for idx in indices]
        
        all_equal = all(
            abs(self.inv_conj.evaluate(p).value - base) < self.tol
            for p in perms
        )
        return {
            "axiom": "ii_commutativity",
            "holds": all_equal,
            "base_value": base,
            "n_permutations_tested": len(perms),
        }

    def check_strict_monotonicity(
        self, inputs: Tuple[float, ...], epsilon: float = 0.01
    ) -> Dict:
        """Axiom iii: increasing any xi (with others > 0) increases c_inv."""
        base = self.inv_conj.evaluate(inputs).value
        violations = []
        for i in range(len(inputs)):
            if inputs[i] >= 1.0 - epsilon:
                continue  # Can't increase beyond 1
            modified = list(inputs)
            modified[i] = min(inputs[i] + epsilon, 1.0)
            new_val = self.inv_conj.evaluate(tuple(modified)).value
            if new_val < base - self.tol:
                violations.append(i)
        return {
            "axiom": "iii_strict_monotonicity",
            "holds": len(violations) == 0,
            "violations": violations,
        }

    def check_veto(self, arity: int) -> Dict:
        """Axiom iv: if any xi = 0, c_inv = 0.
        
        NOTE: This axiom DOES NOT hold for inverted conjunction.
        c_inv(0, 0.9) = 1 - (1*0.1)^(1/2) != 0.
        The inverted conjunction has ANTI-VETO: all inputs must be 0 for output 0.
        This is a documented axiom break.
        """
        # Test: one zero, rest 0.5
        inputs = tuple([0.0] + [0.5] * (arity - 1))
        result = self.inv_conj.evaluate(inputs)
        holds = abs(result.value) < self.tol
        return {
            "axiom": "iv_veto",
            "holds": holds,
            "value": result.value,
            "note": "Inverted conjunction breaks veto. c_inv(0,x) != 0 for x > 0.",
        }

    def check_de_morgan(self, inputs: Tuple[float, ...]) -> Dict:
        """Axiom vii: n(c_inv(x)) = d_inv(n(x))."""
        c_inv = self.inv_conj.evaluate(inputs).value
        n_c_inv = self.negation.evaluate(c_inv)
        
        negated_inputs = tuple(self.negation.evaluate(x) for x in inputs)
        d_inv = self.inv_disj.evaluate(negated_inputs).value
        
        holds = abs(n_c_inv - d_inv) < self.tol
        return {
            "axiom": "vii_de_morgan",
            "holds": holds,
            "n_c_inv": n_c_inv,
            "d_inv_n": d_inv,
            "delta": abs(n_c_inv - d_inv),
        }

    def full_axiom_report(
        self, inputs: Tuple[float, ...]
    ) -> List[Dict]:
        """Run all axiom checks and return comprehensive report."""
        return [
            self.check_compensation(inputs),
            self.check_commutativity(inputs),
            self.check_strict_monotonicity(inputs),
            self.check_veto(len(inputs)),
            self.check_de_morgan(inputs),
        ]
'''

# ============================================================
# tests/iacfl/ — Test workbench
# ============================================================
iacfl_files["tests/iacfl/__init__.py"] = ''

iacfl_files["tests/iacfl/conftest.py"] = '''"""Shared fixtures for I-ACFL test suite."""

import pytest
import numpy as np
from typing import Tuple, List


@pytest.fixture
def rng():
    """Deterministic random number generator."""
    return np.random.default_rng(42)


@pytest.fixture
def random_inputs_2d(rng) -> List[Tuple[float, ...]]:
    """100 random 2-input vectors."""
    return [tuple(rng.uniform(0, 1, size=2)) for _ in range(100)]


@pytest.fixture
def random_inputs_4d(rng) -> List[Tuple[float, ...]]:
    """100 random 4-input vectors."""
    return [tuple(rng.uniform(0, 1, size=4)) for _ in range(100)]


@pytest.fixture
def boundary_inputs_4d() -> List[Tuple[float, ...]]:
    """Critical boundary cases for 4-input operators."""
    return [
        (0.0, 0.0, 0.0, 0.0),    # all zero
        (1.0, 1.0, 1.0, 1.0),    # all one
        (0.5, 0.5, 0.5, 0.5),    # all midpoint
        (0.0, 0.5, 0.5, 0.5),    # single veto
        (0.0, 1.0, 1.0, 1.0),    # veto + unity
        (0.01, 0.99, 0.01, 0.99),# extreme alternating
        (0.0, 0.0, 0.0, 1.0),    # three veto + one unity
        (1.0, 1.0, 1.0, 0.0),    # three unity + one veto
    ]


@pytest.fixture
def acfl_reference_vectors() -> List[dict]:
    """Reference test vectors from ACFL literature.
    
    Source: Espin-Andrade GMBCL published results.
    BUPA dataset truth value: 0.995
    Car dataset truth value: 0.93
    """
    return [
        {
            "name": "BUPA_benchmark",
            "inputs": (0.99, 0.99, 0.99, 0.99, 0.99),
            "expected_gmbcl": 0.99,
            "tolerance": 0.01,
        },
        {
            "name": "high_compensation",
            "inputs": (0.3, 0.9, 0.8, 0.7),
            "expected_gmbcl_range": (0.3, 0.9),
        },
    ]
'''

iacfl_files["tests/iacfl/test_operators.py"] = '''"""
Tests for I-ACFL operators: standard and inverted conjunction/disjunction.

Test categories:
    1. Axiom verification (which hold, which break)
    2. Numerical correctness against hand-computed values
    3. Boundary behavior (zeros, ones, midpoints)
    4. Property-based tests across random populations
    5. Operator identity checks (c_inv vs d_standard)
"""

import pytest
import numpy as np
from iacfl.operators import (
    StandardConjunction,
    InvertedConjunction,
    StandardDisjunction,
    InvertedDisjunction,
    StandardNegation,
)


class TestStandardConjunction:
    """Verify forward ACFL conjunction as baseline for inversion tests."""

    def setup_method(self):
        self.op = StandardConjunction()

    def test_known_value_2_input(self):
        # c(0.4, 0.9) = (0.4 * 0.9)^(1/2) = 0.36^0.5 = 0.6
        result = self.op.evaluate((0.4, 0.9))
        assert abs(result.value - 0.6) < 1e-10

    def test_idempotency(self):
        # c(x, x, ..., x) = x
        for x in [0.1, 0.3, 0.5, 0.7, 0.9]:
            result = self.op.evaluate((x, x, x, x))
            assert abs(result.value - x) < 1e-10

    def test_veto(self):
        result = self.op.evaluate((0.0, 0.8, 0.9))
        assert result.value == 0.0

    def test_unity(self):
        result = self.op.evaluate((1.0, 1.0, 1.0))
        assert abs(result.value - 1.0) < 1e-10

    def test_compensation(self, random_inputs_4d):
        for inputs in random_inputs_4d:
            if any(x == 0 for x in inputs):
                continue
            result = self.op.evaluate(inputs)
            assert min(inputs) <= result.value + 1e-10
            assert result.value <= max(inputs) + 1e-10

    def test_commutativity(self):
        result_a = self.op.evaluate((0.3, 0.7, 0.5))
        result_b = self.op.evaluate((0.7, 0.5, 0.3))
        result_c = self.op.evaluate((0.5, 0.3, 0.7))
        assert abs(result_a.value - result_b.value) < 1e-10
        assert abs(result_a.value - result_c.value) < 1e-10

    def test_strict_monotonicity(self):
        base = self.op.evaluate((0.3, 0.5, 0.7)).value
        increased = self.op.evaluate((0.4, 0.5, 0.7)).value
        assert increased > base


class TestInvertedConjunction:
    """Verify I-ACFL inverted conjunction properties."""

    def setup_method(self):
        self.op = InvertedConjunction()

    def test_known_value_2_input(self):
        # c_inv(0.4, 0.9) = 1 - (0.6 * 0.1)^(1/2) = 1 - 0.06^0.5
        expected = 1.0 - np.sqrt(0.06)
        result = self.op.evaluate((0.4, 0.9))
        assert abs(result.value - expected) < 1e-10

    def test_idempotency(self):
        # c_inv(x, x, ..., x) = 1 - (1-x)^1 = x
        for x in [0.1, 0.3, 0.5, 0.7, 0.9]:
            result = self.op.evaluate((x, x, x, x))
            assert abs(result.value - x) < 1e-10

    def test_veto_broken(self):
        """CRITICAL: Inverted conjunction BREAKS the veto axiom."""
        result = self.op.evaluate((0.0, 0.8, 0.9))
        assert result.value > 0.0, "I-ACFL should NOT veto on single zero"

    def test_anti_veto(self):
        """All inputs must be 0 for inverted conjunction to output 0."""
        result = self.op.evaluate((0.0, 0.0, 0.0))
        assert abs(result.value) < 1e-10

    def test_unity(self):
        result = self.op.evaluate((1.0, 1.0, 1.0))
        assert abs(result.value - 1.0) < 1e-10

    def test_compensation(self, random_inputs_4d):
        """Compensation should still hold for inverted conjunction."""
        for inputs in random_inputs_4d:
            result = self.op.evaluate(inputs)
            assert min(inputs) - 1e-10 <= result.value
            assert result.value <= max(inputs) + 1e-10

    def test_commutativity_holds(self):
        """Inverted conjunction remains commutative (uniform weights)."""
        result_a = self.op.evaluate((0.3, 0.7, 0.5))
        result_b = self.op.evaluate((0.7, 0.5, 0.3))
        assert abs(result_a.value - result_b.value) < 1e-10

    def test_strict_monotonicity(self):
        base = self.op.evaluate((0.3, 0.5, 0.7)).value
        increased = self.op.evaluate((0.4, 0.5, 0.7)).value
        assert increased > base

    def test_de_morgan_duality(self):
        """n(c_inv(x)) = d_inv(n(x))."""
        neg = StandardNegation()
        inv_disj = InvertedDisjunction()
        inputs = (0.3, 0.6, 0.8)
        c_inv = self.op.evaluate(inputs).value
        n_c_inv = neg.evaluate(c_inv)
        neg_inputs = tuple(neg.evaluate(x) for x in inputs)
        d_inv = inv_disj.evaluate(neg_inputs).value
        assert abs(n_c_inv - d_inv) < 1e-10


class TestOperatorIdentity:
    """Test critical identity: is c_inv == d_standard?"""

    def test_inverted_conjunction_equals_standard_disjunction(self):
        """c_inv(x) should equal d(x) for uniform-weight ACFL.
        
        This is the De Morgan identity: inverting conjunction = disjunction.
        If this holds universally, I-ACFL inverted conjunction adds no
        new information beyond standard ACFL disjunction.
        """
        c_inv = InvertedConjunction()
        d_std = StandardDisjunction()
        
        rng = np.random.default_rng(42)
        all_equal = True
        for _ in range(10000):
            inputs = tuple(rng.uniform(0, 1, size=4))
            c_val = c_inv.evaluate(inputs).value
            d_val = d_std.evaluate(inputs).value
            if abs(c_val - d_val) > 1e-10:
                all_equal = False
                break
        
        # EXPECTED: all_equal = True for uniform-weight ACFL
        # This confirms that I-ACFL's value is in the DIVERGENCE ANALYSIS
        # and BLEND, not in the inverted operator alone.
        assert all_equal, (
            "c_inv != d_standard — unexpected! This would mean I-ACFL "
            "produces genuinely novel outputs."
        )

    def test_inverted_disjunction_equals_standard_conjunction(self):
        """d_inv(x) should equal c(x) — the dual identity."""
        d_inv = InvertedDisjunction()
        c_std = StandardConjunction()
        
        rng = np.random.default_rng(42)
        for _ in range(10000):
            inputs = tuple(rng.uniform(0, 1, size=4))
            d_val = d_inv.evaluate(inputs).value
            c_val = c_std.evaluate(inputs).value
            assert abs(d_val - c_val) < 1e-10


class TestInputValidation:
    """Verify input validation catches invalid inputs."""

    def test_input_below_zero(self):
        with pytest.raises(ValueError):
            StandardConjunction().evaluate((-0.1, 0.5))

    def test_input_above_one(self):
        with pytest.raises(ValueError):
            InvertedConjunction().evaluate((0.5, 1.1))

    def test_arity_one(self):
        with pytest.raises(ValueError):
            StandardConjunction().evaluate((0.5,))
'''

iacfl_files["tests/iacfl/test_divergence.py"] = '''"""
Tests for DivergenceAnalyzer.
"""

import pytest
import numpy as np
from iacfl.divergence import DivergenceAnalyzer


class TestDivergenceAnalyzer:

    def setup_method(self):
        self.analyzer = DivergenceAnalyzer()

    def test_zero_divergence_at_idempotent(self):
        """c(x,x,...,x) = c_inv(x,x,...,x) = x. Divergence = 0."""
        for x in [0.1, 0.3, 0.5, 0.7, 0.9]:
            result = self.analyzer.analyze_single((x, x, x, x))
            assert result.delta < 1e-10

    def test_maximum_divergence_direction(self):
        """Inverted conjunction >= standard conjunction for all inputs."""
        rng = np.random.default_rng(42)
        for _ in range(1000):
            inputs = tuple(rng.uniform(0, 1, size=4))
            result = self.analyzer.analyze_single(inputs)
            # c_inv >= c_standard for GMBCL (anti-pessimistic vs pessimistic)
            assert result.inverted_value >= result.forward_value - 1e-10

    def test_population_analysis_returns_all_keys(self):
        stats = self.analyzer.analyze_population(arity=4, n_samples=100)
        required_keys = [
            "arity", "n_samples", "max_delta", "mean_delta",
            "std_delta", "median_delta", "percentile_95",
            "percentile_99", "worst_case_inputs", "all_deltas",
        ]
        for key in required_keys:
            assert key in stats

    def test_boundary_analysis(self):
        results = self.analyzer.analyze_boundary(arity=4)
        assert len(results) >= 7

        # All zeros: both should be 0
        assert results[0].forward_value < 1e-10
        assert results[0].inverted_value < 1e-10
        assert results[0].delta < 1e-10

        # All ones: both should be 1
        assert abs(results[1].forward_value - 1.0) < 1e-10
        assert abs(results[1].inverted_value - 1.0) < 1e-10

    def test_veto_divergence(self):
        """Single zero: forward = 0 (veto), inverted > 0 (no veto)."""
        result = self.analyzer.analyze_single((0.0, 0.8, 0.9, 0.7))
        assert result.forward_value == 0.0
        assert result.inverted_value > 0.0
        assert result.delta > 0.0
'''

iacfl_files["tests/iacfl/test_blend.py"] = '''"""
Tests for ParameterizedBlend.
"""

import pytest
import numpy as np
from iacfl.blend import ParameterizedBlend


class TestParameterizedBlend:

    def setup_method(self):
        self.blend = ParameterizedBlend()

    def test_alpha_one_is_pure_forward(self):
        result = self.blend.evaluate((0.3, 0.7, 0.5), alpha=1.0)
        assert abs(result.blended_value - result.forward_value) < 1e-10

    def test_alpha_zero_is_pure_inverted(self):
        result = self.blend.evaluate((0.3, 0.7, 0.5), alpha=0.0)
        assert abs(result.blended_value - result.inverted_value) < 1e-10

    def test_alpha_half_is_midpoint(self):
        result = self.blend.evaluate((0.3, 0.7, 0.5), alpha=0.5)
        expected = 0.5 * result.forward_value + 0.5 * result.inverted_value
        assert abs(result.blended_value - expected) < 1e-10

    def test_blend_in_unit_interval(self):
        """Blended value must always be in [0,1]."""
        rng = np.random.default_rng(42)
        for _ in range(1000):
            inputs = tuple(rng.uniform(0, 1, size=4))
            alpha = rng.uniform(0, 1)
            result = self.blend.evaluate(inputs, alpha=alpha)
            assert 0.0 <= result.blended_value <= 1.0

    def test_sweep_alpha_length(self):
        results = self.blend.sweep_alpha((0.3, 0.7), steps=51)
        assert len(results) == 51
        assert results[0].alpha == 0.0
        assert abs(results[-1].alpha - 1.0) < 1e-10

    def test_monotonic_sweep(self):
        """For inputs where forward < inverted, blend decreases with alpha."""
        inputs = (0.2, 0.8, 0.3, 0.9)
        results = self.blend.sweep_alpha(inputs, steps=101)
        # Forward (pessimistic) < Inverted (optimistic)
        # So increasing alpha (toward forward) should decrease blend
        for i in range(1, len(results)):
            assert results[i].blended_value <= results[i-1].blended_value + 1e-10

    def test_invalid_alpha(self):
        with pytest.raises(ValueError):
            self.blend.evaluate((0.5, 0.5), alpha=1.5)
        with pytest.raises(ValueError):
            self.blend.evaluate((0.5, 0.5), alpha=-0.1)
'''

iacfl_files["tests/iacfl/test_adversarial.py"] = '''"""
Tests for ACFLAdversarialHarness.
"""

import pytest
from iacfl.adversarial import ACFLAdversarialHarness


class TestAdversarialHarness:

    def setup_method(self):
        self.harness = ACFLAdversarialHarness(decision_threshold=0.5)

    def test_report_structure(self):
        report = self.harness.run(arity=4, n_samples=100)
        assert report.total_cases == 100
        assert report.max_divergence >= 0
        assert report.mean_divergence >= 0
        assert 0 <= report.reversal_rate <= 1
        assert report.worst_case_inputs is not None

    def test_nonzero_reversals(self):
        """Expect some decision reversals at threshold=0.5."""
        report = self.harness.run(arity=4, n_samples=10000)
        assert report.decision_reversals > 0, (
            "Expected nonzero decision reversals between forward and inverted"
        )

    def test_max_divergence_bounded(self):
        """Divergence should be < 1.0 for inputs in [0,1]."""
        report = self.harness.run(arity=4, n_samples=10000)
        assert report.max_divergence < 1.0

    def test_targeted_adversarial(self):
        result = self.harness.targeted_adversarial(arity=4, n_attempts=5000)
        assert "max_divergence" in result
        assert "boundary_cases" in result
        assert result["max_divergence"] >= 0

    def test_high_arity_divergence(self):
        """Higher arity should produce different divergence characteristics."""
        report_2 = self.harness.run(arity=2, n_samples=5000)
        report_8 = self.harness.run(arity=8, n_samples=5000)
        # Both should produce valid reports
        assert report_2.total_cases == 5000
        assert report_8.total_cases == 5000
'''

iacfl_files["tests/iacfl/test_validators.py"] = '''"""
Tests for IACFLAxiomValidator.
"""

import pytest
from iacfl.validators import IACFLAxiomValidator


class TestAxiomValidator:

    def setup_method(self):
        self.validator = IACFLAxiomValidator()

    def test_compensation_holds(self):
        result = self.validator.check_compensation((0.3, 0.6, 0.8))
        assert result["holds"] is True

    def test_commutativity_holds(self):
        result = self.validator.check_commutativity((0.2, 0.5, 0.8))
        assert result["holds"] is True

    def test_strict_monotonicity_holds(self):
        result = self.validator.check_strict_monotonicity((0.3, 0.5, 0.7))
        assert result["holds"] is True

    def test_veto_breaks(self):
        """The veto axiom must NOT hold for inverted conjunction."""
        result = self.validator.check_veto(arity=4)
        assert result["holds"] is False, (
            "Veto axiom should break for I-ACFL. If it holds, the "
            "inversion is not functioning correctly."
        )

    def test_de_morgan_holds(self):
        result = self.validator.check_de_morgan((0.3, 0.6, 0.8))
        assert result["holds"] is True

    def test_full_axiom_report(self):
        report = self.validator.full_axiom_report((0.3, 0.5, 0.7, 0.9))
        assert len(report) == 5
        
        # Expected: compensation=True, commutativity=True,
        # monotonicity=True, veto=False, de_morgan=True
        axiom_names = [r["axiom"] for r in report]
        assert "i_compensation" in axiom_names
        assert "iv_veto" in axiom_names
        
        veto_result = next(r for r in report if r["axiom"] == "iv_veto")
        assert veto_result["holds"] is False
'''

# Write all files and produce summary
print(f"Total files generated: {len(iacfl_files)}")
print("\nFile scaffold:")
for path in sorted(iacfl_files.keys()):
    lines = iacfl_files[path].count('\n')
    print(f"  {path} ({lines} lines)")

# Write the file listing to a summary CSV
import csv
with open("iacfl_scaffold_manifest.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["file_path", "line_count", "category"])
    for path in sorted(iacfl_files.keys()):
        lines = iacfl_files[path].count('\n')
        if path.startswith("tests/"):
            cat = "test"
        elif "shared/" in path:
            cat = "shared"
        else:
            cat = "module"
        writer.writerow([path, lines, cat])

# Also write all files to disk for inspection
import os
for path, content in iacfl_files.items():
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

print("\nAll files written to disk.")
print(f"\nModule files: {sum(1 for p in iacfl_files if 'iacfl/' in p and not p.startswith('tests/'))}")
print(f"Shared files: {sum(1 for p in iacfl_files if 'shared/' in p)}")
print(f"Test files: {sum(1 for p in iacfl_files if p.startswith('tests/'))}")

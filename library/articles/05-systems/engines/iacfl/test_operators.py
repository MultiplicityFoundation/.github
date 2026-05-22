"""
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

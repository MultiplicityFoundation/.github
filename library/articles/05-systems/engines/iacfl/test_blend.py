"""
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

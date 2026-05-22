"""
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

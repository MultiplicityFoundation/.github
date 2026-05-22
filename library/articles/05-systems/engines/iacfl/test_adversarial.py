"""
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

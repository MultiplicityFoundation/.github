"""
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

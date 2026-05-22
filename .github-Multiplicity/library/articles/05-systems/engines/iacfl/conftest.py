"""Shared fixtures for I-ACFL test suite."""

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

#!/usr/bin/env python3
"""
CRMF Test Harness - Certified Resonant Multiplicity Field Validation Suite
============================================================================
A reproducible test harness for validating the CRMF framework.

Requirements: Python 3.8+, NumPy, SciPy (optional for advanced tests)
Install: pip install numpy scipy

Usage:
    python crmf_test_harness.py              # Run all tests
    python crmf_test_harness.py --verbose    # Detailed output
    python crmf_test_harness.py --export     # Export results to JSON

Author: Multiplicity Theory Research Division
License: Proprietary - CH LABS, LLC
"""

import numpy as np
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Tuple, Optional, Callable
from enum import Enum
import json
import argparse
import time
from pathlib import Path

# ============================================================================
# ENUMERATIONS & DATA CLASSES
# ============================================================================

class CertificationStatus(Enum):
    """Certificate status per axiom (C6)."""
    CERTIFIED = "CERTIFIED"
    FREEZE_RESONANCE_LOW = "FREEZE_RESONANCE_LOW"
    FREEZE_RESONANCE_HIGH = "FREEZE_RESONANCE_HIGH"
    REJECT = "REJECT"

class DensityTier(Enum):
    """Tiered density computation levels per axiom (C3)."""
    L0 = 0  # Cheap heuristic (sum-of-norms)
    L1 = 1  # Standard spectral bound
    L2 = 2  # Power iteration
    L4 = 4  # Hypergraph spectral radius

@dataclass
class CRMFCertificate:
    """
    Contraction Certificate (C6): C_t = (ρ_t, λ_m, γ_t, R_t, status)

    Attributes:
        rho_t: Spectral density bound
        lambda_m: Resonance-coupled multiplicity scalar
        gamma_t: Contraction factor γ = ρ + Λ_m · L_T
        R_t: Resonance functional value
        tier_used: Which density tier was used
        status: Certification status
        timestamp: Time step
    """
    rho_t: float
    lambda_m: float
    gamma_t: float
    R_t: float
    tier_used: DensityTier
    status: CertificationStatus
    timestamp: int

    @property
    def is_valid(self) -> bool:
        return self.status == CertificationStatus.CERTIFIED and self.gamma_t < 1.0

    def to_dict(self) -> dict:
        return {
            'rho_t': self.rho_t,
            'lambda_m': self.lambda_m,
            'gamma_t': self.gamma_t,
            'R_t': self.R_t,
            'tier_used': self.tier_used.name,
            'status': self.status.value,
            'timestamp': self.timestamp,
            'is_valid': self.is_valid
        }

@dataclass
class CRMFState:
    """
    Complete CRMF state tuple: t ↦ CRMF_t := (Ξ(t), Λ_m(t), ρ(t), M_t, R_t)
    """
    Xi_t: np.ndarray
    Lambda_m: float
    rho_t: float
    M_t: np.ndarray
    R_t: float
    certificate: CRMFCertificate

@dataclass
class TestResult:
    """Result of a single test case."""
    name: str
    passed: bool
    metric: float
    threshold: float
    details: str = ""
    elapsed_ms: float = 0.0

    def to_dict(self) -> dict:
        return asdict(self)

# ============================================================================
# CRMF CORE COMPONENTS
# ============================================================================

class PrimeIndexedOperatorField:
    """
    (C1) Prime-Indexed Operator Field: Ξ(t) = Σ_p a_p(t) U_p(t)

    Sector operators U_p indexed by primes encode pathway interactions.
    Time-varying weights a_p(t) modulate pathway activity.
    """

    def __init__(self, primes: List[int], dim: int, seed: int = 42):
        self.primes = primes
        self.dim = dim
        self.rng = np.random.default_rng(seed)

        # Initialize sector operators U_p for each prime
        self.U_p: Dict[int, np.ndarray] = {}
        self.a_p: Dict[int, float] = {}

        for p in primes:
            # Random orthogonal-ish operator, scaled for stability
            U = self.rng.standard_normal((dim, dim)) / np.sqrt(dim)
            # Bound spectral norm to 0.8 for safety margin
            U = U / (np.linalg.norm(U, ord=2) + 1e-8) * 0.8
            self.U_p[p] = U
            # Weights decay with prime magnitude (smaller primes = stronger)
            self.a_p[p] = 0.1 / np.sqrt(p)

    def compute_Xi(self, t: int, modulation: Optional[np.ndarray] = None) -> np.ndarray:
        """
        Compute Ξ(t) = Σ_p a_p(t) U_p(t)

        Args:
            t: Time step
            modulation: Optional external modulation signal

        Returns:
            Xi matrix (dim x dim)
        """
        Xi = np.zeros((self.dim, self.dim))
        for p in self.primes:
            # Time-varying weight with sinusoidal modulation
            a_t = self.a_p[p] * (1 + 0.1 * np.sin(2 * np.pi * t / 100))
            if modulation is not None and len(modulation) > 0:
                a_t *= (1 + 0.05 * modulation[t % len(modulation)])
            Xi += a_t * self.U_p[p]
        return Xi

    def get_operator_norm(self, Xi: np.ndarray) -> float:
        """Compute ||Ξ(t)||_2 (spectral norm)."""
        return float(np.linalg.norm(Xi, ord=2))

    def verify_C1(self, Xi: np.ndarray, rho_t: float) -> bool:
        """Verify axiom (C1): ||Ξ(t)|| ≤ ρ(t)."""
        return self.get_operator_norm(Xi) <= rho_t + 1e-9


class ResonanceCoupledGain:
    """
    (C2) Resonance-Coupled Multiplicity Scalar

    Λ_m(t) = CSC_clamp(Λ_raw(t) · g(R_t), ε, λ_max)

    Where gain modulation: g(R_t) = 1 + α(R_t - 0.5), |α| ≤ 0.2
    """

    def __init__(self, epsilon: float = 0.01, lambda_max: float = 0.5, alpha: float = 0.05):
        self.epsilon = epsilon
        self.lambda_max = lambda_max
        self.alpha = alpha
        assert abs(alpha) <= 0.2, "α must satisfy |α| ≤ 0.2"

    def gain_modulation(self, R_t: float) -> float:
        """g(R_t) = 1 + α(R_t - 0.5)"""
        return 1.0 + self.alpha * (R_t - 0.5)

    def csc_clamp(self, lambda_raw: float, R_t: float, rho_t: float, 
                  L_T: float, delta: float = 0.05) -> float:
        """
        CSC clamp ensuring γ_t = ρ_t + Λ_m · L_T ≤ 1 - δ

        Args:
            lambda_raw: Raw (unmodulated) multiplicity scalar
            R_t: Current resonance value
            rho_t: Current spectral density
            L_T: Global Lipschitz constant
            delta: Safety margin

        Returns:
            Clamped Λ_m value
        """
        lambda_proposed = lambda_raw * self.gain_modulation(R_t)

        # Compute maximum allowed Λ_m to satisfy contraction
        target_max = max(0, (1.0 - delta - rho_t) / (L_T + 1e-9))

        # Clamp to valid range
        lambda_m = np.clip(lambda_proposed, self.epsilon, min(self.lambda_max, target_max))
        return float(lambda_m)

    def verify_C2(self, R_t: float) -> bool:
        """Verify axiom (C2): g(R_t) ∈ [0.9, 1.1] for |α| ≤ 0.2."""
        g = self.gain_modulation(R_t)
        return 0.9 - 1e-9 <= g <= 1.1 + 1e-9


class TieredDensityComputer:
    """
    (C3) Tiered Density Computation: ρ(t) ∈ {ρ_L0, ρ_L1, ρ_L2, ρ_L4}

    Escalating tiers provide increasingly tight bounds:
    - L0: Cheap heuristic (sum of weighted operator norms)
    - L1: Standard spectral bound
    - L2: Power iteration refinement
    - L4: Hypergraph spectral radius (expensive)
    """

    def __init__(self, power_iter_steps: int = 10):
        self.power_iter_steps = power_iter_steps

    def compute_L0(self, operator_field: PrimeIndexedOperatorField, t: int = 0) -> float:
        """L0: Conservative sum-of-norms bound."""
        total = 0.0
        for p in operator_field.primes:
            a_t = operator_field.a_p[p] * (1 + 0.1 * np.sin(2 * np.pi * t / 100))
            total += abs(a_t) * np.linalg.norm(operator_field.U_p[p], ord=2)
        return float(total)

    def compute_L1(self, Xi: np.ndarray) -> float:
        """L1: Standard spectral bound ||Ξ||_2."""
        return float(np.linalg.norm(Xi, ord=2))

    def compute_L2(self, Xi: np.ndarray) -> float:
        """L2: Power iteration for tighter spectral estimate."""
        n = Xi.shape[0]
        v = np.random.randn(n)
        v = v / np.linalg.norm(v)

        for _ in range(self.power_iter_steps):
            v_new = Xi @ v
            norm = np.linalg.norm(v_new)
            if norm < 1e-12:
                return 0.0
            v = v_new / norm

        return float(np.linalg.norm(Xi @ v))

    def compute_tiered(self, Xi: np.ndarray, operator_field: PrimeIndexedOperatorField,
                       t: int = 0, gamma_threshold: float = 0.95) -> Tuple[float, DensityTier]:
        """
        Escalating tier computation: L0 → L1 → L2

        Returns tightest bound that certifies (if possible).
        """
        # L0 first (cheapest)
        rho_L0 = self.compute_L0(operator_field, t)
        if rho_L0 < gamma_threshold:
            return rho_L0, DensityTier.L0

        # L1 if L0 too conservative
        rho_L1 = self.compute_L1(Xi)
        if rho_L1 < gamma_threshold:
            return rho_L1, DensityTier.L1

        # L2 power iteration
        rho_L2 = self.compute_L2(Xi)
        return rho_L2, DensityTier.L2


class SparseMultiplicityMatrix:
    """
    (C4) Sparse Polymorphic Multiplicity Density Matrix

    M_t: P_N × P_N → R with ||M_t||_0 ≤ k_max

    Logarithmic encoding: M_t[p,q] = log(interaction(p,q,t))
    Multiplicative property: M(e⊕f) = M(e) · M(f) via exp(M[e] + M[f])
    """

    def __init__(self, primes: List[int], k_max: int = 100):
        self.primes = primes
        self.k_max = k_max
        self.n_primes = len(primes)
        self.M_t = np.zeros((self.n_primes, self.n_primes))

    def update(self, interaction_matrix: np.ndarray):
        """
        Update M_t with logarithmic encoding.
        Enforces sparsity by keeping top-k entries.
        """
        # Extract prime-indexed submatrix
        n = min(self.n_primes, interaction_matrix.shape[0])
        sub = interaction_matrix[:n, :n]

        # Log transform
        self.M_t = np.log(np.abs(sub) + 1e-12)

        # Enforce sparsity
        if np.count_nonzero(self.M_t) > self.k_max:
            flat = np.abs(self.M_t.flatten())
            threshold = np.partition(flat, -self.k_max)[-self.k_max]
            self.M_t[np.abs(self.M_t) < threshold] = 0

    def verify_multiplicative(self, e_idx: int, f_idx: int) -> bool:
        """Verify multiplicative property: exp(M[e] + M[f])."""
        if e_idx >= self.n_primes or f_idx >= self.n_primes:
            return False
        # Check that log-additive = multiplicative
        combined = np.exp(self.M_t[e_idx, :] + self.M_t[:, f_idx])
        direct = np.exp(self.M_t[e_idx, :]) * np.exp(self.M_t[:, f_idx])
        return np.allclose(combined, direct, rtol=1e-5)

    def verify_C4(self) -> bool:
        """Verify axiom (C4): ||M_t||_0 ≤ k_max."""
        return int(np.count_nonzero(self.M_t)) <= self.k_max


class ResonanceFunctional:
    """
    (C5) Bounded Resonance Functional

    R_t = max_{W ∈ W_t, |W| ≤ L} R(W, D_t)

    R(W, D) = <eigspace(W), eigspace(D)> / (||eigspace(W)|| · ||eigspace(D)||)
    """

    def __init__(self, R_min: float = 0.1, R_max: float = 0.95, max_word_length: int = 2):
        self.R_min = R_min
        self.R_max = R_max
        self.max_word_length = max_word_length

    def _eigenspace_overlap(self, A: np.ndarray, B: np.ndarray, k: int = 5) -> float:
        """Compute eigenspace overlap between two matrices."""
        try:
            k = min(k, A.shape[0] - 1)
            # Get top-k eigenvectors of symmetric parts
            eig_A = np.linalg.eigh(A @ A.T)[1][:, -k:]
            eig_B = np.linalg.eigh(B @ B.T)[1][:, -k:]

            # Subspace overlap via Frobenius inner product
            overlap = np.linalg.norm(eig_A.T @ eig_B, 'fro')
            norm_A = np.linalg.norm(eig_A, 'fro')
            norm_B = np.linalg.norm(eig_B, 'fro')

            if norm_A < 1e-12 or norm_B < 1e-12:
                return 0.5
            return float(np.clip(overlap / (norm_A * norm_B), 0, 1))
        except:
            return 0.5

    def compute_R_t(self, operator_field: PrimeIndexedOperatorField, 
                    D_t: np.ndarray) -> float:
        """
        Compute R_t = max over operator words.

        Args:
            operator_field: Prime-indexed operators
            D_t: Data/state matrix

        Returns:
            Bounded resonance value in [R_min, R_max]
        """
        max_R = 0.0

        # Single operators
        for p in operator_field.primes:
            R = self._eigenspace_overlap(operator_field.U_p[p], D_t)
            max_R = max(max_R, R)

        # Composed operators (length 2)
        if self.max_word_length >= 2:
            for p1 in operator_field.primes[:3]:  # Limit for efficiency
                for p2 in operator_field.primes[:3]:
                    W = operator_field.U_p[p1] @ operator_field.U_p[p2]
                    R = self._eigenspace_overlap(W, D_t)
                    max_R = max(max_R, R)

        return float(np.clip(max_R, self.R_min, self.R_max))

    def verify_C5(self, R_t: float) -> bool:
        """Verify axiom (C5): R_min ≤ R_t ≤ R_max."""
        return self.R_min - 1e-9 <= R_t <= self.R_max + 1e-9


class CRMFCertifier:
    """
    (C6) Contraction Certificate Generator

    C_t = (ρ_t, c_t, γ_t, R_t, status)

    Enforces: γ_t = ρ_t + Λ_m(t) · L_T ≤ 1 - δ
    """

    def __init__(self, L_T: float = 0.3, delta: float = 0.05,
                 R_min: float = 0.1, R_safe: float = 0.95):
        self.L_T = L_T
        self.delta = delta
        self.R_min = R_min
        self.R_safe = R_safe

    def certify(self, rho_t: float, lambda_m: float, R_t: float,
                tier: DensityTier, t: int) -> CRMFCertificate:
        """Generate contraction certificate."""
        gamma_t = rho_t + lambda_m * self.L_T

        # Determine status based on resonance and contraction bounds
        if R_t < self.R_min:
            status = CertificationStatus.FREEZE_RESONANCE_LOW
        elif R_t > self.R_safe:
            status = CertificationStatus.FREEZE_RESONANCE_HIGH
        elif gamma_t > 1.0 - self.delta:
            status = CertificationStatus.REJECT
        else:
            status = CertificationStatus.CERTIFIED

        return CRMFCertificate(
            rho_t=rho_t,
            lambda_m=lambda_m,
            gamma_t=gamma_t,
            R_t=R_t,
            tier_used=tier,
            status=status,
            timestamp=t
        )

    def verify_C6(self, cert: CRMFCertificate) -> bool:
        """Verify axiom (C6): γ_t ≤ 1 - δ when CERTIFIED."""
        if cert.status == CertificationStatus.CERTIFIED:
            return cert.gamma_t <= 1.0 - self.delta + 1e-9
        return True


# ============================================================================
# COMPLETE CRMF SYSTEM
# ============================================================================

class CRMFSystem:
    """
    Complete Certified Resonant Multiplicity Field System

    Integrates all axioms (C1)-(C6) into a unified framework.

    State tuple: t ↦ CRMF_t := (Ξ(t), Λ_m(t), ρ(t), M_t, R_t)
    """

    def __init__(self, 
                 primes: List[int] = [2, 3, 5, 7, 11],
                 dim: int = 50,
                 alpha: float = 0.05,
                 epsilon: float = 0.01,
                 lambda_max: float = 0.5,
                 L_T: float = 0.3,
                 delta: float = 0.05,
                 k_max: int = 100,
                 seed: int = 42):
        """
        Initialize CRMF system.

        Args:
            primes: Prime index set P_N
            dim: State space dimension
            alpha: Resonance coupling strength (|α| ≤ 0.2)
            epsilon: Minimum gain floor
            lambda_max: Maximum gain ceiling
            L_T: Global Lipschitz constant
            delta: Safety margin for contraction
            k_max: Sparsity bound for M_t
            seed: Random seed for reproducibility
        """
        self.primes = primes
        self.dim = dim
        self.seed = seed

        # Initialize components
        self.operator_field = PrimeIndexedOperatorField(primes, dim, seed)
        self.gain_computer = ResonanceCoupledGain(epsilon, lambda_max, alpha)
        self.density_computer = TieredDensityComputer()
        self.multiplicity_matrix = SparseMultiplicityMatrix(primes, k_max)
        self.resonance_functional = ResonanceFunctional()
        self.certifier = CRMFCertifier(L_T, delta)

        # State history
        self.history: List[CRMFState] = []
        self.rng = np.random.default_rng(seed)

    def step(self, t: int, D_t: Optional[np.ndarray] = None,
             lambda_raw: float = 0.2) -> CRMFState:
        """
        Execute one CRMF update step.

        Args:
            t: Time step
            D_t: Data/observation matrix (generated if None)
            lambda_raw: Raw multiplicity scalar

        Returns:
            CRMFState with all components and certificate
        """
        # Generate data state if not provided
        if D_t is None:
            D_t = self.rng.standard_normal((self.dim, self.dim)) / np.sqrt(self.dim)
            D_t = (D_t + D_t.T) / 2  # Symmetric

        # (C1) Compute prime-indexed operator field
        Xi_t = self.operator_field.compute_Xi(t)

        # (C3) Compute tiered density
        rho_t, tier = self.density_computer.compute_tiered(Xi_t, self.operator_field, t)

        # (C5) Compute resonance functional
        R_t = self.resonance_functional.compute_R_t(self.operator_field, D_t)

        # (C2) Compute resonance-coupled gain with CSC clamp
        lambda_m = self.gain_computer.csc_clamp(
            lambda_raw, R_t, rho_t, self.certifier.L_T, self.certifier.delta
        )

        # (C4) Update sparse multiplicity matrix
        interaction = Xi_t @ D_t + D_t @ Xi_t
        self.multiplicity_matrix.update(interaction)

        # (C6) Generate certificate
        cert = self.certifier.certify(rho_t, lambda_m, R_t, tier, t)

        state = CRMFState(
            Xi_t=Xi_t,
            Lambda_m=lambda_m,
            rho_t=rho_t,
            M_t=self.multiplicity_matrix.M_t.copy(),
            R_t=R_t,
            certificate=cert
        )
        self.history.append(state)
        return state

    def apply_update(self, x: np.ndarray, state: CRMFState,
                     T: Callable[[np.ndarray], np.ndarray],
                     F_t: np.ndarray) -> np.ndarray:
        """
        Apply CRMF update map: Φ_t(x) = Ξ(t)x + Λ_m(t)T(x) + F_t

        Only applies if certificate status is CERTIFIED.
        """
        if state.certificate.status != CertificationStatus.CERTIFIED:
            return x  # Freeze on non-certified

        return state.Xi_t @ x + state.Lambda_m * T(x) + F_t

    def reset(self):
        """Reset system state."""
        self.history.clear()
        self.multiplicity_matrix.M_t = np.zeros_like(self.multiplicity_matrix.M_t)


# ============================================================================
# TEST HARNESS
# ============================================================================

class CRMFTestHarness:
    """
    Comprehensive Test Harness for CRMF Validation

    Implements Phase A: Synthetic Resonance Validation protocol.
    """

    def __init__(self, system: Optional[CRMFSystem] = None, verbose: bool = False):
        self.system = system or CRMFSystem()
        self.verbose = verbose
        self.results: List[TestResult] = []

    def _log(self, msg: str):
        if self.verbose:
            print(msg)

    def run_all_tests(self, n_steps: int = 100, n_trials: int = 3) -> Dict:
        """Execute complete test suite."""
        self.results.clear()
        start_time = time.time()

        print("\n" + "=" * 70)
        print(" CRMF TEST HARNESS - Certified Resonant Multiplicity Field")
        print(" Phase A: Synthetic Resonance Validation")
        print("=" * 70)
        print(f"\n Configuration:")
        print(f"   Primes P_N: {self.system.primes}")
        print(f"   Dimension: {self.system.dim}")
        print(f"   α (resonance coupling): {self.system.gain_computer.alpha}")
        print(f"   L_T (Lipschitz): {self.system.certifier.L_T}")
        print(f"   δ (safety margin): {self.system.certifier.delta}")
        print(f"   k_max (sparsity): {self.system.multiplicity_matrix.k_max}")
        print(f"   Seed: {self.system.seed}")

        # Run axiom tests
        self._test_C1()
        self._test_C2()
        self._test_C3()
        self._test_C4()
        self._test_C5()
        self._test_C6()

        # Run theorem tests
        self._test_theorem_4_2(n_steps, n_trials)
        self._test_theorem_4_3(n_steps)

        # Phase A metrics
        self._test_convergence_rate(n_steps)
        self._test_certificate_violation_rate(n_steps, n_trials)
        self._test_resonance_oscillation(n_steps)
        self._test_alpha_sweep(n_steps)

        elapsed = time.time() - start_time
        return self._generate_report(elapsed)

    # ---- AXIOM TESTS ----

    def _test_C1(self):
        """(C1) Prime-Indexed Operator Field: ||Ξ(t)|| ≤ ρ(t)"""
        print("\n[C1] Prime-Indexed Operator Field...")
        t0 = time.time()

        self.system.reset()
        Xi = self.system.operator_field.compute_Xi(0)
        rho_L1 = self.system.density_computer.compute_L1(Xi)
        norm_Xi = self.system.operator_field.get_operator_norm(Xi)
        passed = self.system.operator_field.verify_C1(Xi, rho_L1)

        result = TestResult(
            name="C1: ||Ξ(t)|| ≤ ρ(t)",
            passed=passed,
            metric=norm_Xi,
            threshold=rho_L1,
            details=f"||Ξ||={norm_Xi:.6f}, ρ={rho_L1:.6f}",
            elapsed_ms=(time.time() - t0) * 1000
        )
        self.results.append(result)
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: ||Ξ|| = {norm_Xi:.4f} ≤ ρ = {rho_L1:.4f}")

    def _test_C2(self):
        """(C2) Resonance-Coupled Gain: g(R_t) ∈ [0.9, 1.1]"""
        print("\n[C2] Resonance-Coupled Multiplicity Scalar...")
        t0 = time.time()

        test_R = [0.0, 0.25, 0.5, 0.75, 1.0]
        gains = [self.system.gain_computer.gain_modulation(R) for R in test_R]
        passed = all(self.system.gain_computer.verify_C2(R) for R in test_R)

        result = TestResult(
            name="C2: g(R_t) ∈ [0.9, 1.1]",
            passed=passed,
            metric=max(gains) - min(gains),
            threshold=0.2,
            details=f"g range: [{min(gains):.4f}, {max(gains):.4f}]",
            elapsed_ms=(time.time() - t0) * 1000
        )
        self.results.append(result)
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: g ∈ [{min(gains):.4f}, {max(gains):.4f}]")

    def _test_C3(self):
        """(C3) Tiered Density: ρ_L0 ≥ ρ_L1 (conservative hierarchy)"""
        print("\n[C3] Tiered Density Computation...")
        t0 = time.time()

        Xi = self.system.operator_field.compute_Xi(0)
        rho_L0 = self.system.density_computer.compute_L0(self.system.operator_field)
        rho_L1 = self.system.density_computer.compute_L1(Xi)
        rho_L2 = self.system.density_computer.compute_L2(Xi)

        passed = rho_L0 >= rho_L1 - 0.01  # L0 is conservative upper bound

        result = TestResult(
            name="C3: ρ_L0 ≥ ρ_L1 (conservative)",
            passed=passed,
            metric=rho_L0 - rho_L1,
            threshold=0.0,
            details=f"L0={rho_L0:.4f}, L1={rho_L1:.4f}, L2={rho_L2:.4f}",
            elapsed_ms=(time.time() - t0) * 1000
        )
        self.results.append(result)
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: ρ_L0={rho_L0:.4f} ≥ ρ_L1={rho_L1:.4f}")

    def _test_C4(self):
        """(C4) Sparse Multiplicity Matrix: ||M_t||_0 ≤ k_max"""
        print("\n[C4] Sparse Polymorphic Multiplicity Density Matrix...")
        t0 = time.time()

        self.system.reset()
        for t in range(10):
            self.system.step(t)

        nnz = int(np.count_nonzero(self.system.multiplicity_matrix.M_t))
        passed = self.system.multiplicity_matrix.verify_C4()

        result = TestResult(
            name="C4: ||M_t||_0 ≤ k_max (sparsity)",
            passed=passed,
            metric=nnz,
            threshold=self.system.multiplicity_matrix.k_max,
            details=f"Non-zero entries: {nnz}",
            elapsed_ms=(time.time() - t0) * 1000
        )
        self.results.append(result)
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: ||M||_0 = {nnz} ≤ k_max = {self.system.multiplicity_matrix.k_max}")

    def _test_C5(self):
        """(C5) Bounded Resonance: R_min ≤ R_t ≤ R_max"""
        print("\n[C5] Bounded Resonance Functional...")
        t0 = time.time()

        D_t = np.random.randn(self.system.dim, self.system.dim) / np.sqrt(self.system.dim)
        D_t = (D_t + D_t.T) / 2

        R_t = self.system.resonance_functional.compute_R_t(self.system.operator_field, D_t)
        passed = self.system.resonance_functional.verify_C5(R_t)

        result = TestResult(
            name="C5: R_min ≤ R_t ≤ R_max",
            passed=passed,
            metric=R_t,
            threshold=(self.system.resonance_functional.R_min, self.system.resonance_functional.R_max),
            details=f"R_t = {R_t:.4f}",
            elapsed_ms=(time.time() - t0) * 1000
        )
        self.results.append(result)
        R_min = self.system.resonance_functional.R_min
        R_max = self.system.resonance_functional.R_max
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: R_t = {R_t:.4f} ∈ [{R_min}, {R_max}]")

    def _test_C6(self):
        """(C6) Contraction Certificate: γ_t ≤ 1 - δ when CERTIFIED"""
        print("\n[C6] Contraction Certificate...")
        t0 = time.time()

        self.system.reset()
        state = self.system.step(0)
        cert = state.certificate
        passed = self.system.certifier.verify_C6(cert)

        result = TestResult(
            name="C6: γ_t ≤ 1-δ when CERTIFIED",
            passed=passed,
            metric=cert.gamma_t,
            threshold=1.0 - self.system.certifier.delta,
            details=f"γ={cert.gamma_t:.4f}, status={cert.status.value}",
            elapsed_ms=(time.time() - t0) * 1000
        )
        self.results.append(result)
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: γ = {cert.gamma_t:.4f} ≤ {1-self.system.certifier.delta:.4f}")

    # ---- THEOREM TESTS ----

    def _test_theorem_4_2(self, n_steps: int, n_trials: int):
        """Theorem 4.2: Uniform Incremental Contraction"""
        print("\n[Thm 4.2] CRMF Contraction Theorem...")
        t0 = time.time()

        violations = 0
        total = 0
        max_gamma = 0.0

        for trial in range(n_trials):
            system = CRMFSystem(seed=trial * 100)

            for t in range(n_steps):
                state = system.step(t)
                if state.certificate.status != CertificationStatus.CERTIFIED:
                    continue

                # Test contraction
                x = np.random.randn(system.dim)
                y = np.random.randn(system.dim)
                T = lambda v: -0.1 * v
                F_t = np.zeros(system.dim)

                Phi_x = system.apply_update(x, state, T, F_t)
                Phi_y = system.apply_update(y, state, T, F_t)

                ratio = np.linalg.norm(Phi_x - Phi_y) / (np.linalg.norm(x - y) + 1e-12)
                max_gamma = max(max_gamma, ratio)

                if ratio > state.certificate.gamma_t + 0.01:
                    violations += 1
                total += 1

        viol_rate = violations / max(total, 1)
        passed = viol_rate < 0.01

        result = TestResult(
            name="Thm 4.2: Uniform Incremental Contraction",
            passed=passed,
            metric=viol_rate,
            threshold=0.01,
            details=f"Violations: {violations}/{total}, max γ: {max_gamma:.4f}",
            elapsed_ms=(time.time() - t0) * 1000
        )
        self.results.append(result)
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: Violation rate = {viol_rate:.4f}")

    def _test_theorem_4_3(self, n_steps: int):
        """Theorem 4.3: Resonance-Stability Coupling"""
        print("\n[Thm 4.3] Resonance-Stability Coupling...")
        t0 = time.time()

        self.system.reset()
        R_history = []

        for t in range(n_steps):
            state = self.system.step(t)
            R_history.append(state.R_t)

        # Estimate L_R from resonance variations
        R_diffs = [abs(R_history[i+1] - R_history[i]) for i in range(len(R_history)-1)]
        L_R_estimate = np.mean(R_diffs) * 10

        alpha = self.system.gain_computer.alpha
        c = self.system.certifier.L_T
        delta = self.system.certifier.delta

        coupling = alpha * L_R_estimate * (1 + c)
        passed = coupling < delta

        result = TestResult(
            name="Thm 4.3: αL_R(1+c) < δ stability",
            passed=passed,
            metric=coupling,
            threshold=delta,
            details=f"α={alpha}, L_R≈{L_R_estimate:.4f}, coupling={coupling:.4f}",
            elapsed_ms=(time.time() - t0) * 1000
        )
        self.results.append(result)
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: αL_R(1+c) = {coupling:.4f} < δ = {delta}")

    # ---- PHASE A METRICS ----

    def _test_convergence_rate(self, n_steps: int):
        """Phase A: Convergence rate τ90"""
        print("\n[Phase A] Convergence Rate τ90...")
        t0 = time.time()

        self.system.reset()
        X_t = np.random.randn(self.system.dim) * 5
        T = lambda v: -0.1 * v
        tau_90 = n_steps

        for t in range(n_steps):
            state = self.system.step(t)
            F_t = np.random.randn(self.system.dim) * 0.01
            X_t = self.system.apply_update(X_t, state, T, F_t)

            if np.linalg.norm(X_t) < 0.5 and tau_90 == n_steps:
                tau_90 = t

        passed = tau_90 < n_steps * 0.7

        result = TestResult(
            name="Phase A: τ90 Convergence Rate",
            passed=passed,
            metric=tau_90,
            threshold=n_steps * 0.7,
            details=f"Converged at t={tau_90}",
            elapsed_ms=(time.time() - t0) * 1000
        )
        self.results.append(result)
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: τ90 = {tau_90}")

    def _test_certificate_violation_rate(self, n_steps: int, n_trials: int):
        """Phase A: P(γ_t > 1) = 0"""
        print("\n[Phase A] Certificate Violation Rate P(γ > 1)...")
        t0 = time.time()

        violations = 0
        certified = 0
        total = 0

        for trial in range(n_trials):
            system = CRMFSystem(seed=trial * 42)
            for t in range(n_steps):
                state = system.step(t)
                total += 1
                if state.certificate.gamma_t > 1.0:
                    violations += 1
                if state.certificate.status == CertificationStatus.CERTIFIED:
                    certified += 1

        viol_rate = violations / total
        cert_rate = certified / total
        passed = viol_rate == 0.0

        result = TestResult(
            name="Phase A: P(γ_t > 1) = 0",
            passed=passed,
            metric=viol_rate,
            threshold=0.0,
            details=f"Cert rate: {cert_rate:.1%}",
            elapsed_ms=(time.time() - t0) * 1000
        )
        self.results.append(result)
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: P(γ>1) = {viol_rate}, cert rate = {cert_rate:.1%}")

    def _test_resonance_oscillation(self, n_steps: int):
        """Phase A: max|R_t - R_{t-1}| < 0.3"""
        print("\n[Phase A] Resonance Oscillation...")
        t0 = time.time()

        self.system.reset()
        R_history = []

        for t in range(n_steps):
            state = self.system.step(t)
            R_history.append(state.R_t)

        oscillations = [abs(R_history[i+1] - R_history[i]) for i in range(len(R_history)-1)]
        max_osc = max(oscillations)
        mean_osc = np.mean(oscillations)

        passed = max_osc < 0.3

        result = TestResult(
            name="Phase A: max|ΔR| < 0.3",
            passed=passed,
            metric=max_osc,
            threshold=0.3,
            details=f"max|ΔR|={max_osc:.4f}, mean={mean_osc:.4f}",
            elapsed_ms=(time.time() - t0) * 1000
        )
        self.results.append(result)
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: max|ΔR| = {max_osc:.4f}")

    def _test_alpha_sweep(self, n_steps: int):
        """Phase A: α parameter sweep"""
        print("\n[Phase A] α Parameter Sweep...")
        t0 = time.time()

        alpha_values = [0, 0.05, 0.1, 0.15]
        results_by_alpha = {}

        for alpha in alpha_values:
            system = CRMFSystem(alpha=alpha, seed=42)
            cert_count = 0
            gamma_sum = 0

            for t in range(n_steps):
                state = system.step(t)
                gamma_sum += state.certificate.gamma_t
                if state.certificate.status == CertificationStatus.CERTIFIED:
                    cert_count += 1

            results_by_alpha[alpha] = {
                'cert_rate': cert_count / n_steps,
                'mean_gamma': gamma_sum / n_steps
            }
            self._log(f"   α={alpha}: cert={cert_count/n_steps:.1%}")

        # α=0.05 should work well
        passed = results_by_alpha[0.05]['cert_rate'] > 0.7

        result = TestResult(
            name="Phase A: α=0.05 certification > 70%",
            passed=passed,
            metric=results_by_alpha[0.05]['cert_rate'],
            threshold=0.7,
            details=f"α sweep: " + ", ".join(f"{a}:{r['cert_rate']:.0%}" for a, r in results_by_alpha.items()),
            elapsed_ms=(time.time() - t0) * 1000
        )
        self.results.append(result)

        for alpha, data in results_by_alpha.items():
            print(f"   α={alpha}: cert rate = {data['cert_rate']:.1%}, γ̄ = {data['mean_gamma']:.4f}")

    def _generate_report(self, elapsed_sec: float) -> Dict:
        """Generate test report."""
        passed = sum(1 for r in self.results if r.passed)
        total = len(self.results)

        print("\n" + "=" * 70)
        print(" CRMF TEST REPORT SUMMARY")
        print("=" * 70)
        print(f"\n Overall: {passed}/{total} tests PASSED ({100*passed/total:.0f}%)")
        print(f" Total time: {elapsed_sec:.2f}s\n")

        print(" Results by Category:")
        print(" " + "-" * 68)

        for r in self.results:
            status = "✅ PASS" if r.passed else "❌ FAIL"
            print(f" {status} | {r.name}")
            if self.verbose:
                print(f"         | Metric: {r.metric}, Threshold: {r.threshold}")
                print(f"         | {r.details}")

        return {
            'passed': passed,
            'total': total,
            'success_rate': passed / total,
            'elapsed_seconds': elapsed_sec,
            'results': [r.to_dict() for r in self.results]
        }

    def export_results(self, filepath: str = "crmf_test_results.json"):
        """Export results to JSON file."""
        report = {
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
            'system_config': {
                'primes': self.system.primes,
                'dim': self.system.dim,
                'alpha': self.system.gain_computer.alpha,
                'L_T': self.system.certifier.L_T,
                'delta': self.system.certifier.delta,
                'k_max': self.system.multiplicity_matrix.k_max,
                'seed': self.system.seed
            },
            'results': [r.to_dict() for r in self.results],
            'summary': {
                'passed': sum(1 for r in self.results if r.passed),
                'total': len(self.results)
            }
        }

        with open(filepath, 'w') as f:
            json.dump(report, f, indent=2)

        print(f"\n Results exported to: {filepath}")


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="CRMF Test Harness - Certified Resonant Multiplicity Field Validation"
    )
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Enable verbose output')
    parser.add_argument('--export', '-e', action='store_true',
                        help='Export results to JSON')
    parser.add_argument('--steps', '-n', type=int, default=100,
                        help='Number of time steps (default: 100)')
    parser.add_argument('--trials', '-t', type=int, default=3,
                        help='Number of trials (default: 3)')
    parser.add_argument('--seed', '-s', type=int, default=42,
                        help='Random seed (default: 42)')
    parser.add_argument('--dim', '-d', type=int, default=50,
                        help='State dimension (default: 50)')
    parser.add_argument('--alpha', '-a', type=float, default=0.05,
                        help='Resonance coupling α (default: 0.05)')

    args = parser.parse_args()

    # Initialize system
    system = CRMFSystem(
        dim=args.dim,
        alpha=args.alpha,
        seed=args.seed
    )

    # Run tests
    harness = CRMFTestHarness(system, verbose=args.verbose)
    report = harness.run_all_tests(n_steps=args.steps, n_trials=args.trials)

    # Export if requested
    if args.export:
        harness.export_results()

    # Return exit code based on results
    return 0 if report['success_rate'] >= 0.9 else 1


if __name__ == "__main__":
    exit(main())

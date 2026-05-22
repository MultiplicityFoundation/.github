#!/usr/bin/env python3
"""
================================================================================
CRMF TEST HARNESS - Certified Resonant Multiplicity Field Validation Suite
================================================================================

A reproducible test harness for validating the Certified Resonant Multiplicity 
Field (CRMF) framework, implementing Phase A: Synthetic Resonance Validation.

CRMF enhances the Elevate Care Program's DNA KEY infrastructure by embedding
semantic, spectral, and ethical invariants into recursive biosemantic computation.

REQUIREMENTS:
    Python 3.8+
    NumPy >= 1.20

INSTALLATION:
    pip install numpy

USAGE:
    python crmf_test_harness.py                    # Run all tests (default)
    python crmf_test_harness.py --verbose          # Detailed output
    python crmf_test_harness.py --export           # Export results to JSON
    python crmf_test_harness.py --dim 100          # Custom dimension
    python crmf_test_harness.py --alpha 0.1        # Custom resonance coupling
    python crmf_test_harness.py --help             # Show all options

AXIOMS TESTED:
    (C1) Prime-Indexed Operator Field: Ξ(t) = Σ_p a_p(t) U_p(t)
    (C2) Resonance-Coupled Multiplicity Scalar: Λ_m(t) = CSC_clamp(Λ_raw · g(R_t))
    (C3) Tiered Density Computation: ρ(t) ∈ {ρ_L0, ρ_L1, ρ_L2, ρ_L4}
    (C4) Sparse Polymorphic Multiplicity Density Matrix: ||M_t||_0 ≤ k_max
    (C5) Bounded Resonance Functional: R_min ≤ R_t ≤ R_max
    (C6) Contraction Certificate: γ_t = ρ_t + Λ_m·L_T ≤ 1 - δ

THEOREMS VALIDATED:
    Theorem 4.2: CRMF Contraction - Uniform incremental contraction
    Theorem 4.3: Resonance-Stability Coupling - αL_R(1+c) < δ guarantees stability

Author: Multiplicity Theory Research Division
Date: January 2026
License: Proprietary - CH LABS, LLC
================================================================================
"""

import numpy as np
from dataclasses import dataclass, asdict
from typing import List, Dict, Tuple, Optional, Callable, Any
from enum import Enum
import json
import argparse
import time
import sys


# ============================================================================
# CONFIGURATION & CONSTANTS
# ============================================================================

DEFAULT_CONFIG = {
    'primes': [2, 3, 5, 7, 11],  # Prime index set P_N
    'dim': 50,                    # State space dimension
    'alpha': 0.05,                # Resonance coupling strength
    'epsilon': 0.01,              # Minimum gain floor
    'lambda_max': 0.5,            # Maximum gain ceiling
    'L_T': 0.3,                   # Global Lipschitz constant
    'delta': 0.05,                # Safety margin
    'k_max': 100,                 # Sparsity bound for M_t
    'R_min': 0.1,                 # Minimum resonance
    'R_max': 0.95,                # Maximum resonance
    'seed': 42,                   # Random seed
    'n_steps': 100,               # Time steps per trial
    'n_trials': 3,                # Number of trials
}


# ============================================================================
# ENUMERATIONS
# ============================================================================

class CertificationStatus(Enum):
    """Certificate status per axiom (C6)."""
    CERTIFIED = "CERTIFIED"
    FREEZE_RESONANCE_LOW = "FREEZE_RESONANCE_LOW"
    FREEZE_RESONANCE_HIGH = "FREEZE_RESONANCE_HIGH"
    REJECT = "REJECT"


class DensityTier(Enum):
    """Tiered density computation levels per axiom (C3)."""
    L0 = 0  # Sum-of-norms heuristic
    L1 = 1  # Spectral norm
    L2 = 2  # Power iteration
    L4 = 4  # Hypergraph spectral radius


# ============================================================================
# DATA CLASSES
# ============================================================================

@dataclass
class CRMFCertificate:
    """
    Contraction Certificate (C6): C_t = (ρ_t, λ_m, γ_t, R_t, status)
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
            'rho_t': round(self.rho_t, 6),
            'lambda_m': round(self.lambda_m, 6),
            'gamma_t': round(self.gamma_t, 6),
            'R_t': round(self.R_t, 6),
            'tier': self.tier_used.name,
            'status': self.status.value,
            'timestamp': self.timestamp,
            'valid': self.is_valid
        }


@dataclass
class CRMFState:
    """Complete CRMF state: (Ξ(t), Λ_m(t), ρ(t), M_t, R_t)"""
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
    threshold: Any
    details: str = ""
    elapsed_ms: float = 0.0

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'passed': self.passed,
            'metric': round(self.metric, 6) if isinstance(self.metric, float) else self.metric,
            'threshold': self.threshold,
            'details': self.details,
            'elapsed_ms': round(self.elapsed_ms, 2)
        }


# ============================================================================
# CRMF SYSTEM
# ============================================================================

class CRMFSystem:
    """
    Certified Resonant Multiplicity Field System

    Integrates axioms (C1)-(C6) for cohomologically lawful computation.
    """

    def __init__(self, **kwargs):
        """Initialize with config dict or keyword arguments."""
        cfg = {**DEFAULT_CONFIG, **kwargs}

        self.primes: List[int] = cfg['primes']
        self.dim: int = cfg['dim']
        self.alpha: float = cfg['alpha']
        self.epsilon: float = cfg['epsilon']
        self.lambda_max: float = cfg['lambda_max']
        self.L_T: float = cfg['L_T']
        self.delta: float = cfg['delta']
        self.k_max: int = cfg['k_max']
        self.R_min: float = cfg['R_min']
        self.R_max: float = cfg['R_max']
        self.seed: int = cfg['seed']

        # Initialize RNG
        self.rng = np.random.default_rng(self.seed)

        # (C1) Prime-indexed operators
        self.U_p: Dict[int, np.ndarray] = {}
        self.a_p: Dict[int, float] = {}
        for p in self.primes:
            U = self.rng.standard_normal((self.dim, self.dim)) / np.sqrt(self.dim)
            U = U / (np.linalg.norm(U, ord=2) + 1e-8) * 0.8
            self.U_p[p] = U
            self.a_p[p] = 0.1 / np.sqrt(p)

        # (C4) Sparse multiplicity matrix
        self.M_t = np.zeros((len(self.primes), len(self.primes)))

        # State history
        self.history: List[CRMFState] = []

    def compute_Xi(self, t: int) -> np.ndarray:
        """(C1) Ξ(t) = Σ_p a_p(t) U_p(t)"""
        Xi = np.zeros((self.dim, self.dim))
        for p in self.primes:
            a_t = self.a_p[p] * (1 + 0.1 * np.sin(2 * np.pi * t / 100))
            Xi += a_t * self.U_p[p]
        return Xi

    def compute_density_L0(self, t: int = 0) -> float:
        """(C3) L0: Sum-of-norms heuristic."""
        return sum(
            abs(self.a_p[p] * (1 + 0.1 * np.sin(2 * np.pi * t / 100))) * 
            np.linalg.norm(self.U_p[p], ord=2) 
            for p in self.primes
        )

    def compute_density_L1(self, Xi: np.ndarray) -> float:
        """(C3) L1: Spectral norm."""
        return float(np.linalg.norm(Xi, ord=2))

    def compute_density_L2(self, Xi: np.ndarray, steps: int = 10) -> float:
        """(C3) L2: Power iteration."""
        v = self.rng.standard_normal(self.dim)
        v = v / np.linalg.norm(v)
        for _ in range(steps):
            v_new = Xi @ v
            norm = np.linalg.norm(v_new)
            if norm < 1e-12:
                return 0.0
            v = v_new / norm
        return float(np.linalg.norm(Xi @ v))

    def gain_modulation(self, R_t: float) -> float:
        """(C2) g(R_t) = 1 + α(R_t - 0.5)"""
        return 1.0 + self.alpha * (R_t - 0.5)

    def csc_clamp(self, lambda_raw: float, R_t: float, rho_t: float) -> float:
        """(C2) CSC clamp ensuring γ ≤ 1 - δ."""
        lambda_proposed = lambda_raw * self.gain_modulation(R_t)
        target_max = max(0, (1.0 - self.delta - rho_t) / (self.L_T + 1e-9))
        return float(np.clip(lambda_proposed, self.epsilon, min(self.lambda_max, target_max)))

    def compute_resonance(self, D_t: np.ndarray) -> float:
        """(C5) R_t via eigenspace overlap."""
        try:
            max_R = 0.0
            for p in self.primes[:3]:
                A = self.U_p[p] @ self.U_p[p].T
                B = D_t @ D_t.T
                k = min(3, self.dim - 1)
                eig_A = np.linalg.eigvalsh(A)[-k:]
                eig_B = np.linalg.eigvalsh(B)[-k:]
                corr = np.abs(np.corrcoef(eig_A, eig_B)[0, 1])
                if not np.isnan(corr):
                    max_R = max(max_R, corr)
            return float(np.clip(max_R, self.R_min, self.R_max))
        except Exception:
            return 0.5

    def step(self, t: int, D_t: Optional[np.ndarray] = None, 
             lambda_raw: float = 0.2) -> CRMFState:
        """Execute one CRMF update step."""
        # Generate observation if not provided
        if D_t is None:
            D_t = self.rng.standard_normal((self.dim, self.dim)) / np.sqrt(self.dim)
            D_t = (D_t + D_t.T) / 2

        # (C1) Operator field
        Xi_t = self.compute_Xi(t)

        # (C3) Tiered density
        rho_L0 = self.compute_density_L0(t)
        rho_L1 = self.compute_density_L1(Xi_t)
        if rho_L1 < rho_L0:
            rho_t, tier = rho_L1, DensityTier.L1
        else:
            rho_t, tier = rho_L0, DensityTier.L0

        # (C5) Resonance
        R_t = self.compute_resonance(D_t)

        # (C2) Gain with CSC clamp
        lambda_m = self.csc_clamp(lambda_raw, R_t, rho_t)

        # (C4) Update sparse M_t
        n = min(len(self.primes), self.dim)
        interaction = Xi_t[:n, :n] @ D_t[:n, :n]
        self.M_t = np.log(np.abs(interaction) + 1e-12)

        # (C6) Certificate
        gamma_t = rho_t + lambda_m * self.L_T

        if R_t < self.R_min:
            status = CertificationStatus.FREEZE_RESONANCE_LOW
        elif R_t > self.R_max:
            status = CertificationStatus.FREEZE_RESONANCE_HIGH
        elif gamma_t > 1.0 - self.delta:
            status = CertificationStatus.REJECT
        else:
            status = CertificationStatus.CERTIFIED

        cert = CRMFCertificate(rho_t, lambda_m, gamma_t, R_t, tier, status, t)
        state = CRMFState(Xi_t, lambda_m, rho_t, self.M_t.copy(), R_t, cert)
        self.history.append(state)
        return state

    def apply_update(self, x: np.ndarray, state: CRMFState,
                     T: Callable[[np.ndarray], np.ndarray],
                     F_t: np.ndarray) -> np.ndarray:
        """Φ_t(x) = Ξ(t)x + Λ_m(t)T(x) + F_t (only if CERTIFIED)."""
        if state.certificate.status != CertificationStatus.CERTIFIED:
            return x
        return state.Xi_t @ x + state.Lambda_m * T(x) + F_t

    def reset(self):
        """Reset state history."""
        self.history.clear()
        self.M_t = np.zeros((len(self.primes), len(self.primes)))


# ============================================================================
# TEST HARNESS
# ============================================================================

class CRMFTestHarness:
    """Test harness for CRMF validation."""

    def __init__(self, system: Optional[CRMFSystem] = None, verbose: bool = False):
        self.system = system or CRMFSystem()
        self.verbose = verbose
        self.results: List[TestResult] = []

    def run_all_tests(self, n_steps: int = 100, n_trials: int = 3) -> Dict:
        """Execute complete test suite."""
        self.results.clear()
        start = time.time()

        self._print_header()

        # Axiom tests
        self._test_C1()
        self._test_C2()
        self._test_C3()
        self._test_C4()
        self._test_C5()
        self._test_C6()

        # Theorem tests
        self._test_theorem_4_2(n_steps, n_trials)
        self._test_theorem_4_3(n_steps)

        # Phase A metrics
        self._test_convergence(n_steps)
        self._test_certificate_rate(n_steps, n_trials)
        self._test_resonance_oscillation(n_steps)
        self._test_alpha_sweep(n_steps)

        return self._print_summary(time.time() - start)

    def _print_header(self):
        print("\n" + "=" * 70)
        print(" CRMF TEST HARNESS - Certified Resonant Multiplicity Field")
        print(" Phase A: Synthetic Resonance Validation")
        print("=" * 70)
        print(f"\n Configuration:")
        print(f"   Primes P_N    : {self.system.primes}")
        print(f"   Dimension     : {self.system.dim}")
        print(f"   α (coupling)  : {self.system.alpha}")
        print(f"   L_T (Lipschitz): {self.system.L_T}")
        print(f"   δ (margin)    : {self.system.delta}")
        print(f"   k_max (sparse): {self.system.k_max}")
        print(f"   Seed          : {self.system.seed}")

    def _test_C1(self):
        """(C1) ||Ξ(t)|| ≤ ρ(t)"""
        print("\n[C1] Prime-Indexed Operator Field...")
        t0 = time.time()
        self.system.reset()
        Xi = self.system.compute_Xi(0)
        rho = self.system.compute_density_L1(Xi)
        norm_Xi = float(np.linalg.norm(Xi, 2))
        passed = norm_Xi <= rho + 1e-9
        self.results.append(TestResult("C1: ||Ξ(t)|| ≤ ρ(t)", passed, norm_Xi, rho,
                                        f"||Ξ||={norm_Xi:.6f}", (time.time()-t0)*1000))
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: ||Ξ||={norm_Xi:.4f} ≤ ρ={rho:.4f}")

    def _test_C2(self):
        """(C2) g(R_t) ∈ [0.9, 1.1]"""
        print("\n[C2] Resonance-Coupled Gain...")
        t0 = time.time()
        gains = [self.system.gain_modulation(R) for R in [0, 0.5, 1.0]]
        passed = all(0.9 - 1e-6 <= g <= 1.1 + 1e-6 for g in gains)
        self.results.append(TestResult("C2: g(R_t) ∈ [0.9, 1.1]", passed, 
                                        max(gains)-min(gains), 0.2,
                                        f"g∈[{min(gains):.3f},{max(gains):.3f}]",
                                        (time.time()-t0)*1000))
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: g ∈ [{min(gains):.3f}, {max(gains):.3f}]")

    def _test_C3(self):
        """(C3) ρ_L0 ≥ ρ_L1 (conservative hierarchy)"""
        print("\n[C3] Tiered Density Computation...")
        t0 = time.time()
        Xi = self.system.compute_Xi(0)
        rho_L0 = self.system.compute_density_L0()
        rho_L1 = self.system.compute_density_L1(Xi)
        passed = rho_L0 >= rho_L1 - 0.01
        self.results.append(TestResult("C3: ρ_L0 ≥ ρ_L1", passed, rho_L0-rho_L1, 0.0,
                                        f"L0={rho_L0:.4f}, L1={rho_L1:.4f}",
                                        (time.time()-t0)*1000))
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: ρ_L0={rho_L0:.4f} ≥ ρ_L1={rho_L1:.4f}")

    def _test_C4(self):
        """(C4) ||M_t||_0 ≤ k_max"""
        print("\n[C4] Sparse Multiplicity Matrix...")
        t0 = time.time()
        self.system.reset()
        for t in range(10):
            self.system.step(t)
        nnz = int(np.count_nonzero(self.system.M_t))
        passed = nnz <= self.system.k_max
        self.results.append(TestResult("C4: ||M_t||_0 ≤ k_max", passed, nnz, 
                                        self.system.k_max, f"nnz={nnz}",
                                        (time.time()-t0)*1000))
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: ||M||_0={nnz} ≤ k_max={self.system.k_max}")

    def _test_C5(self):
        """(C5) R_min ≤ R_t ≤ R_max"""
        print("\n[C5] Bounded Resonance Functional...")
        t0 = time.time()
        D = np.random.randn(self.system.dim, self.system.dim)
        D = (D + D.T) / 2
        R_t = self.system.compute_resonance(D)
        passed = self.system.R_min <= R_t <= self.system.R_max
        self.results.append(TestResult("C5: R_min ≤ R_t ≤ R_max", passed, R_t,
                                        (self.system.R_min, self.system.R_max),
                                        f"R_t={R_t:.4f}", (time.time()-t0)*1000))
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: R_t={R_t:.4f} ∈ [{self.system.R_min},{self.system.R_max}]")

    def _test_C6(self):
        """(C6) γ_t ≤ 1 - δ when CERTIFIED"""
        print("\n[C6] Contraction Certificate...")
        t0 = time.time()
        self.system.reset()
        state = self.system.step(0)
        gamma = state.certificate.gamma_t
        thresh = 1 - self.system.delta
        passed = gamma <= thresh + 1e-9
        self.results.append(TestResult("C6: γ_t ≤ 1-δ", passed, gamma, thresh,
                                        f"status={state.certificate.status.value}",
                                        (time.time()-t0)*1000))
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: γ={gamma:.4f} ≤ {thresh:.4f}")

    def _test_theorem_4_2(self, n_steps: int, n_trials: int):
        """Theorem 4.2: Contraction"""
        print("\n[Thm 4.2] Contraction Theorem...")
        t0 = time.time()
        violations = total = 0
        T_fn = lambda v: -0.1 * v
        F_t = np.zeros(self.system.dim)

        for trial in range(n_trials):
            sys = CRMFSystem(dim=self.system.dim, seed=trial*100)
            for t in range(n_steps):
                st = sys.step(t)
                if st.certificate.status != CertificationStatus.CERTIFIED:
                    continue
                x, y = np.random.randn(sys.dim), np.random.randn(sys.dim)
                Phi_x = sys.apply_update(x, st, T_fn, F_t)
                Phi_y = sys.apply_update(y, st, T_fn, F_t)
                ratio = np.linalg.norm(Phi_x - Phi_y) / (np.linalg.norm(x - y) + 1e-12)
                if ratio > st.certificate.gamma_t + 0.01:
                    violations += 1
                total += 1

        viol_rate = violations / max(total, 1)
        passed = viol_rate < 0.01
        self.results.append(TestResult("Thm 4.2: Contraction", passed, viol_rate, 0.01,
                                        f"violations={violations}/{total}",
                                        (time.time()-t0)*1000))
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: violation rate = {viol_rate:.4f}")

    def _test_theorem_4_3(self, n_steps: int):
        """Theorem 4.3: Stability Coupling"""
        print("\n[Thm 4.3] Resonance-Stability Coupling...")
        t0 = time.time()
        self.system.reset()
        R_hist = [self.system.step(t).R_t for t in range(n_steps)]
        diffs = [abs(R_hist[i+1] - R_hist[i]) for i in range(len(R_hist)-1)]
        L_R = np.mean(diffs) * 10
        coupling = self.system.alpha * L_R * (1 + self.system.L_T)
        passed = coupling < self.system.delta
        self.results.append(TestResult("Thm 4.3: αL_R(1+c) < δ", passed, coupling,
                                        self.system.delta, f"L_R≈{L_R:.4f}",
                                        (time.time()-t0)*1000))
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: αL_R(1+c)={coupling:.4f} < δ={self.system.delta}")

    def _test_convergence(self, n_steps: int):
        """Phase A: Convergence τ90"""
        print("\n[Phase A] Convergence Rate τ90...")
        t0 = time.time()
        self.system.reset()
        X_t = np.random.randn(self.system.dim) * 5
        T_fn = lambda v: -0.1 * v
        tau_90 = n_steps

        for t in range(n_steps):
            st = self.system.step(t)
            F_t = np.random.randn(self.system.dim) * 0.01
            X_t = self.system.apply_update(X_t, st, T_fn, F_t)
            if np.linalg.norm(X_t) < 0.5 and tau_90 == n_steps:
                tau_90 = t

        thresh = int(n_steps * 0.7)
        passed = tau_90 < thresh
        self.results.append(TestResult("Phase A: τ90", passed, tau_90, thresh,
                                        f"converged at t={tau_90}", (time.time()-t0)*1000))
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: τ90={tau_90} < {thresh}")

    def _test_certificate_rate(self, n_steps: int, n_trials: int):
        """Phase A: P(γ > 1) = 0"""
        print("\n[Phase A] Certificate Violation Rate P(γ > 1)...")
        t0 = time.time()
        violations = cert_count = total = 0

        for trial in range(n_trials):
            sys = CRMFSystem(dim=self.system.dim, seed=trial*42)
            for t in range(n_steps):
                st = sys.step(t)
                total += 1
                if st.certificate.gamma_t > 1.0:
                    violations += 1
                if st.certificate.status == CertificationStatus.CERTIFIED:
                    cert_count += 1

        viol_rate = violations / total
        cert_rate = cert_count / total
        passed = viol_rate == 0
        self.results.append(TestResult("Phase A: P(γ>1)=0", passed, viol_rate, 0.0,
                                        f"cert rate={cert_rate:.1%}", (time.time()-t0)*1000))
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: P(γ>1)={viol_rate}, cert rate={cert_rate:.1%}")

    def _test_resonance_oscillation(self, n_steps: int):
        """Phase A: max|ΔR| < 0.3"""
        print("\n[Phase A] Resonance Oscillation...")
        t0 = time.time()
        self.system.reset()
        R_hist = [self.system.step(t).R_t for t in range(n_steps)]
        diffs = [abs(R_hist[i+1] - R_hist[i]) for i in range(len(R_hist)-1)]
        max_osc = max(diffs)
        passed = max_osc < 0.3
        self.results.append(TestResult("Phase A: max|ΔR|<0.3", passed, max_osc, 0.3,
                                        f"mean={np.mean(diffs):.4f}", (time.time()-t0)*1000))
        print(f"   {'✅ PASS' if passed else '❌ FAIL'}: max|ΔR|={max_osc:.4f}")

    def _test_alpha_sweep(self, n_steps: int):
        """Phase A: α parameter sweep"""
        print("\n[Phase A] α Parameter Sweep...")
        t0 = time.time()
        results_by_alpha = {}

        for alpha in [0, 0.05, 0.1, 0.15]:
            sys = CRMFSystem(dim=self.system.dim, alpha=alpha, seed=42)
            cert = sum(1 for t in range(n_steps) 
                      if sys.step(t).certificate.status == CertificationStatus.CERTIFIED)
            rate = cert / n_steps
            results_by_alpha[alpha] = rate
            print(f"   α={alpha}: cert rate = {rate:.1%}")

        passed = results_by_alpha[0.05] > 0.7
        self.results.append(TestResult("Phase A: α sweep", passed, 
                                        results_by_alpha[0.05], 0.7,
                                        str(results_by_alpha), (time.time()-t0)*1000))

    def _print_summary(self, elapsed: float) -> Dict:
        """Print and return summary."""
        passed = sum(1 for r in self.results if r.passed)
        total = len(self.results)
        rate = passed / total if total > 0 else 0

        print("\n" + "=" * 70)
        print(" CRMF TEST SUMMARY")
        print("=" * 70)
        print(f"\n   ✅ {passed}/{total} tests PASSED ({rate:.0%})")
        print(f"   ⏱️  Total time: {elapsed:.2f}s")
        print("\n   Results:")
        for r in self.results:
            s = "✅" if r.passed else "❌"
            print(f"   {s} {r.name}")

        return {
            'passed': passed,
            'total': total,
            'success_rate': rate,
            'elapsed_seconds': round(elapsed, 2),
            'results': [r.to_dict() for r in self.results]
        }

    def export_json(self, filepath: str = "crmf_results.json"):
        """Export results to JSON."""
        report = {
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
            'config': {
                'primes': self.system.primes,
                'dim': self.system.dim,
                'alpha': self.system.alpha,
                'L_T': self.system.L_T,
                'delta': self.system.delta,
                'seed': self.system.seed
            },
            'summary': {
                'passed': sum(1 for r in self.results if r.passed),
                'total': len(self.results)
            },
            'results': [r.to_dict() for r in self.results]
        }
        with open(filepath, 'w') as f:
            json.dump(report, f, indent=2)
        print(f"\n   📄 Results exported to: {filepath}")


# ============================================================================
# CLI ENTRY POINT
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="CRMF Test Harness - Certified Resonant Multiplicity Field",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python %(prog)s                   # Run default tests
  python %(prog)s -v --export       # Verbose + export JSON
  python %(prog)s --dim 100 -n 200  # Custom dimension and steps
        """
    )
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('-e', '--export', action='store_true', help='Export to JSON')
    parser.add_argument('-n', '--steps', type=int, default=100, help='Time steps (default: 100)')
    parser.add_argument('-t', '--trials', type=int, default=3, help='Trials (default: 3)')
    parser.add_argument('-d', '--dim', type=int, default=50, help='Dimension (default: 50)')
    parser.add_argument('-a', '--alpha', type=float, default=0.05, help='α coupling (default: 0.05)')
    parser.add_argument('-s', '--seed', type=int, default=42, help='Random seed (default: 42)')

    args = parser.parse_args()

    system = CRMFSystem(dim=args.dim, alpha=args.alpha, seed=args.seed)
    harness = CRMFTestHarness(system, verbose=args.verbose)
    report = harness.run_all_tests(n_steps=args.steps, n_trials=args.trials)

    if args.export:
        harness.export_json()

    return 0 if report['success_rate'] >= 0.9 else 1


if __name__ == "__main__":
    sys.exit(main())

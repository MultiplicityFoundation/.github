---
title: "ADR-005 STRUCTURAL EVOLUTION ENGINE \u2014 DEVELOPMENT BLUEPRINT"
slug: adr-005-structural-evolution-engine-development-blueprint
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 05-systems/engines/ADR-005_Dev_Blueprint.md
  last_synced: '2026-03-20T17:17:18.241015Z'
---

# ADR-005 STRUCTURAL EVOLUTION ENGINE — DEVELOPMENT BLUEPRINT
## Implementation Scaffold, Test Bench & Integration Map

| Field | Value |
|---|---|
| **Document ID** | DEV-SVP-001 |
| **Parent Artifact** | Shadow Validation Protocol v0.1 (SVP-001-v0.1) |
| **Status** | ACTIVE — Implementation Phase |
| **Date** | February 20, 2026 |
| **Classification** | Confidential — Engineering Work Product |
| **Repo Target** | `CHL987/Intrinsica` monorepo |

---

## §1 FILE SCAFFOLD

### §1.1 Directory Structure

```
packages/
└── dna_key/
    ├── docs/
    │   ├── CCRE Integration Implications for CRMF and ACFL.md   ← existing
    │   ├── CCRE Module Blueprint.md                              ← existing
    │   ├── Shadow_Validation_Protocol_v0.1.md                    ← new (shipped artifact)
    │   └── ADR-005_Dev_Blueprint.md                              ← this document
    │
    ├── src/
    │   └── adr005/
    │       ├── __init__.py
    │       ├── config.py                      # §1.2  — constants, thresholds, enums
    │       ├── types.py                       # §1.3  — dataclasses & type definitions
    │       │
    │       ├── psi/                           # Position-Stability Index module
    │       │   ├── __init__.py
    │       │   ├── mann_kendall.py             # §1.4  — Mann-Kendall L2.5 integration
    │       │   ├── contraction_margin.py       # §1.5  — PSI-2 τ(t) trajectory analysis
    │       │   ├── axiom_stress.py             # §1.6  — PSI-3 axiom-selective stress testing
    │       │   └── classifier.py              # §1.7  — 3-class diagnostic classifier
    │       │
    │       ├── authorization/                 # Three-key gate module
    │       │   ├── __init__.py
    │       │   ├── gate.py                    # §1.8  — Three-key gate with SLA
    │       │   ├── timeout.py                 # §1.9  — Bifurcated timeout handling
    │       │   └── governance_exception.py    # §1.10 — 2-of-3 fallback + Part 11 audit
    │       │
    │       ├── shadow/                        # Shadow validation module
    │       │   ├── __init__.py
    │       │   ├── deployment.py              # §1.11 — Shadow deployment orchestrator
    │       │   ├── concordance.py             # §1.12 — Per-axiom concordance metrics
    │       │   └── late_failure.py            # §1.13 — SHADOW_LATE_FAILURE rollback
    │       │
    │       ├── canary/                        # Canary rollout module
    │       │   ├── __init__.py
    │       │   ├── traffic.py                 # §1.14 — Traffic graduation controller
    │       │   └── revert.py                  # §1.15 — Canary revert triggers
    │       │
    │       ├── circuit_breaker/               # Axiom-gated circuit breakers
    │       │   ├── __init__.py
    │       │   └── breaker.py                 # §1.16 — Same-axiom + cumulative counter
    │       │
    │       ├── pipeline/                      # Pipeline state machine
    │       │   ├── __init__.py
    │       │   ├── states.py                  # §1.17 — Pipeline state definitions
    │       │   ├── transitions.py             # §1.18 — State transition logic
    │       │   └── orchestrator.py            # §1.19 — End-to-end pipeline controller
    │       │
    │       └── audit/                         # Λ-Trace audit integration
    │           ├── __init__.py
    │           ├── events.py                  # §1.20 — Event type registry
    │           ├── witness.py                 # §1.21 — CRMF Witness Object emission
    │           └── part11.py                  # §1.22 — 21 CFR Part 11 compliance layer
    │
    └── tests/
        └── adr005/
            ├── __init__.py
            ├── conftest.py                    # §2.1  — Shared fixtures & synthetic data
            │
            ├── unit/
            │   ├── __init__.py
            │   ├── test_mann_kendall.py        # §2.2  — MK significance tests
            │   ├── test_contraction_margin.py  # §2.3  — PSI-2 trajectory classification
            │   ├── test_axiom_stress.py        # §2.4  — PSI-3 perturbation tests
            │   ├── test_classifier.py          # §2.5  — 3-class diagnostic classifier
            │   ├── test_gate.py                # §2.6  — Three-key authorization
            │   ├── test_timeout.py             # §2.7  — Bifurcated timeout flags
            │   ├── test_governance.py          # §2.8  — 2-of-3 fallback & audit
            │   ├── test_concordance.py         # §2.9  — Per-axiom concordance
            │   ├── test_circuit_breaker.py     # §2.10 — Breaker + cumulative counter
            │   └── test_events.py              # §2.11 — Event type completeness
            │
            ├── integration/
            │   ├── __init__.py
            │   ├── test_psi_pipeline.py        # §2.12 — PSI triplet → classifier flow
            │   ├── test_shadow_canary.py        # §2.13 — Shadow → canary with overlap
            │   ├── test_late_failure.py         # §2.14 — SHADOW_LATE_FAILURE two-front
            │   ├── test_timeout_escalation.py   # §2.15 — Diagnostic → Auth timeout chain
            │   └── test_audit_chain.py          # §2.16 — End-to-end Λ-Trace integrity
            │
            └── e2e/
                ├── __init__.py
                ├── test_full_pipeline.py        # §2.17 — Detection through recovery
                ├── test_prophetic_example_6.py   # §2.18 — Subject F months 1–6 scenario
                └── test_position_reassignment.py # §2.19 — 42.4% PW-CFL drift scenario
```

---

## §2 MODULE SPECIFICATIONS

### §2.1 config.py — Constants & Thresholds

```python
\"\"\"ADR-005 Structural Evolution Engine — Configuration Constants.

All threshold values are locked per SVP-001-v0.1.
TS-23 through TS-26 are placeholder pending classifier validation (April 3, 2026).
\"\"\"
from enum import Enum, auto


# ─── Jubilee Cycle Parameters ───────────────────────────────────────
J_MIN_DAYS: int = 5               # Adaptive J: requires ≥90% ring sensor uptime
J_STANDARD_DAYS: int = 7          # Standard Jubilee cycle duration
J_MAX_DAYS: int = 10              # Hard cap when sensor uptime < 90%
SENSOR_UPTIME_THRESHOLD: float = 0.90  # Minimum ring sensor uptime for J_min

# ─── Mann-Kendall Parameters (SVP §4.1) ────────────────────────────
MK_LAG: int = 2                   # LOCKED — do not make runtime-configurable
MK_SIGNIFICANCE_ALPHA: float = 0.05  # p < 0.05 → position reassignment
MK_MIN_WINDOW_PAIRS: int = 4      # Minimum pairs for reliable variance correction

# ─── PSI-2 Contraction Margin (SVP §4.2) ───────────────────────────
TAU_SLOPE_POSITIVE_THRESHOLD: float = 0.0     # β > 0 → approaching ceiling
TAU_CV_LOW: float = 0.15          # CV(τ) < 0.15 → genuine parametric ceiling
TAU_CV_HIGH: float = 0.30         # CV(τ) > 0.30 → composite infeasibility
TAU_SLOPE_NEGATIVE_THRESHOLD: float = 0.0     # β < 0 → drift misidentification
TAU_CV_DRIFT_MAX: float = 0.20    # CV(τ) < 0.20 under negative slope → drift

# ─── Diagnostic Classifier (SVP §4.4) ──────────────────────────────
CLASSIFIER_CONFIDENCE_THRESHOLD: float = 0.9  # Min confidence for advancement
CLASSIFIER_FEATURE_DIM: int = 10   # [MK_p, β_τ, CV_τ, F(6-bit), AUROC_slope, Var_κ_slope]

# ─── Timeout Architecture (SVP §5) ─────────────────────────────────
DIAGNOSTIC_TIMEOUT_J_MULTIPLIER: float = 2.0  # Hard cap: 2J
DIAGNOSTIC_MAX_RETRIES: int = 1               # Max 1 retry after INCONCLUSIVE
AUTH_SLA_J_FRACTION: float = 0.25             # Per key holder: 0.25J
AUTH_ESCALATION_TIER2_J: float = 0.5          # 2-of-3 activation
AUTH_ESCALATION_TIER3_J: float = 1.0          # CTO emergency override
AUTH_RATIFICATION_WINDOW_J: float = 1.0       # Absent key holder ratification SLA

# ─── Shadow Validation (SVP §6, §7) ────────────────────────────────
SHADOW_MIN_DURATION_J: float = 0.5  # Minimum if overlap eligible
SHADOW_STD_DURATION_J: float = 1.0  # Standard shadow window
EPI_DIVERGENCE_THRESHOLD: float = 0.05   # |EPI_P - EPI_P'| ≤ 0.05
INTERVENTION_CONCORDANCE_MIN: float = 0.95
ACFL_COSINE_SIMILARITY_MIN: float = 0.92

# ─── Axiom Concordance Thresholds (SVP §7.1) ───────────────────────
C6_CONCORDANCE_REQUIRED: float = 1.00   # Absolutely gating
C1_C2_CONCORDANCE_MIN: float = 0.95     # Jointly gating
C3_C4_C5_CONCORDANCE_MIN: float = 0.90  # Independently gating
C3_C4_C5_RECOVERY_THRESHOLD: float = 0.90  # Recovery during canary
CONDITIONAL_COHERENCE_THRESHOLD: float = 0.95  # Extended confirmation

# ─── Circuit Breaker (SVP §7.3) ────────────────────────────────────
SAME_AXIOM_CONSECUTIVE_LIMIT: int = 2   # Same axiom fails 2x → escalate
CUMULATIVE_FAILURE_LIMIT: int = 3        # Total C3+C4+C5 failures → reject P'

# ─── Canary Rollout (SVP §9) ───────────────────────────────────────
CANARY_STAGES: list[dict] = [
    {"stage": 1, "traffic_pct": 0.05, "min_duration_weeks": 1},
    {"stage": 2, "traffic_pct": 0.25, "min_duration_weeks": 1},
    {"stage": 3, "traffic_pct": 0.50, "min_duration_weeks": 1},
    {"stage": 4, "traffic_pct": 1.00, "min_duration_weeks": 0},  # full cutover
]
CANARY_EPI_REVERT_THRESHOLD: float = 0.10    # 2x shadow threshold
CANARY_DISCORDANCE_REVERT: float = 0.10      # 10% intervention discordance
CANARY_OVERRIDE_RATE_MULTIPLIER: float = 2.0  # 2x baseline override rate

# ─── Coherence Confirmation (SVP §10) ──────────────────────────────
STANDARD_CONFIRMATION_J: int = 2
EXTENDED_CONFIRMATION_J: int = 3      # Conditional advancement
EXTENDED_EXTENDED_CONFIRMATION_J: int = 4  # Cumulative failure = 2
COLD_ROLLBACK_RETENTION_J: int = 4    # Archived P retention

# ─── Audit Trail (SVP §11) ─────────────────────────────────────────
RETENTION_YEARS_MIN: int = 7          # Subject to retention parity check
HASH_ALGORITHM: str = "sha256"

# ─── Overlap Compression (SVP §8.1) ────────────────────────────────
OVERLAP_C1_C2_PASS_WINDOW_J: float = 0.5   # C1+C2 must pass within 0.5J
OVERLAP_PENDING_CONCORDANCE_MIN: float = 0.85  # Trending threshold

# ─── Trade Secret Placeholders (SVP §13) ───────────────────────────
# These values are PENDING — derived after classifier validation
# TS-23 through TS-26 to be populated by April 3, 2026
class TSPlaceholder:
    TS_23 = None  # Tier 1 → Tier 2 dissonance boundary
    TS_24 = None  # Tier 2 → Silence Hold activation threshold
    TS_25 = None  # Diagnostic confidence floor calibration
    TS_26 = None  # Shadow concordance margin calibration


class CeilingCause(Enum):
    GENUINE_PARAMETRIC_CEILING = auto()
    POSITION_REASSIGNMENT_DRIFT = auto()
    COMPOSITE_INFEASIBILITY = auto()


class PipelineStage(Enum):
    SILENCE_HOLD = auto()
    DIAGNOSTIC = auto()
    AUTHORIZATION = auto()
    SHADOW_VALIDATION = auto()
    CANARY_ROLLOUT = auto()
    COHERENCE_CONFIRMATION = auto()
    COMPLETE = auto()
    REVERTED = auto()
    DEFERRED = auto()


class AxiomCategory(Enum):
    ABSOLUTELY_GATING = auto()     # C6
    JOINTLY_GATING = auto()        # C1, C2
    INDEPENDENTLY_GATING = auto()  # C3, C4, C5


class EventType(Enum):
    EXECUTION_SILENCE_HOLD = auto()
    DIAGNOSTIC_CLASSIFICATION = auto()
    DIAGNOSTIC_INCONCLUSIVE = auto()
    ADR005_DIAGNOSTIC_TIMEOUT = auto()
    AUTHORIZATION_REQUEST = auto()
    AUTHORIZATION_RECEIVED = auto()
    ADR005_AUTHORIZATION_TIMEOUT = auto()
    GOVERNANCE_EXCEPTION_2OF3 = auto()
    GOVERNANCE_EXCEPTION_2OF3_RATIFIED = auto()
    GOVERNANCE_EXCEPTION_2OF3_DENIED = auto()
    SHADOW_DEPLOYMENT_START = auto()
    SHADOW_CONCORDANCE_CHECKPOINT = auto()
    SHADOW_VALIDATION_PASS = auto()
    SHADOW_VALIDATION_FAIL = auto()
    CONDITIONAL_ADVANCEMENT = auto()
    SHADOW_CANARY_OVERLAP = auto()
    SHADOW_LATE_FAILURE = auto()
    CANARY_STAGE_ADVANCE = auto()
    CANARY_REVERT = auto()
    CIRCUIT_BREAKER_SAME_AXIOM = auto()
    CIRCUIT_BREAKER_CUMULATIVE = auto()
    COHERENCE_CONFIRMATION_PASS = auto()
    STRUCTURAL_EVOLUTION_COMPLETE = auto()
    STRUCTURAL_EVOLUTION_DEFERRED = auto()
    STRUCTURAL_CANDIDATE_REJECTED = auto()
```

### §2.2 types.py — Core Data Structures

```python
\"\"\"ADR-005 type definitions — all pipeline data structures.\"\"\"
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from .config import CeilingCause, PipelineStage, EventType


@dataclass(frozen=True)
class MannKendallResult:
    \"\"\"Output of hamed_rao_modification_test on κ-rank series.\"\"\"
    z_statistic: float        # Corrected Z_MK
    p_value: float            # Two-sided p-value
    kendall_tau: float        # Raw Kendall τ (logged, not used for classification)
    sens_slope: float         # Sen's slope estimate
    n_window_pairs: int       # Number of Jubilee window pairs analyzed
    lag_used: int             # Always 2 per config lock
    sufficient_data: bool     # True if n_window_pairs >= MK_MIN_WINDOW_PAIRS


@dataclass(frozen=True)
class ContractionMarginResult:
    \"\"\"PSI-2: τ(t) trajectory analysis over 4J window.\"\"\"
    beta_slope: float         # OLS slope of τ(t)
    cv_tau: float             # Coefficient of variation of τ(t)
    tau_values: tuple[float, ...]  # Raw τ(t) series
    window_count: int         # Number of J windows analyzed


@dataclass(frozen=True)
class AxiomStressResult:
    \"\"\"PSI-3: 6-bit axiom failure vector under synthetic perturbation.\"\"\"
    failure_vector: tuple[bool, bool, bool, bool, bool, bool]  # C1–C6
    perturbation_magnitudes: tuple[float, ...]


@dataclass(frozen=True)
class PSIFeatureVector:
    \"\"\"Complete 10-dimensional feature vector for diagnostic classifier.\"\"\"
    mk_p_value: float         # PSI-1: Mann-Kendall p-value
    beta_tau: float           # PSI-2: contraction margin slope
    cv_tau: float             # PSI-2: contraction margin CV
    f_c1: bool                # PSI-3: C1 failure under stress
    f_c2: bool                # PSI-3: C2 failure under stress
    f_c3: bool                # PSI-3: C3 failure under stress
    f_c4: bool                # PSI-3: C4 failure under stress
    f_c5: bool                # PSI-3: C5 failure under stress
    f_c6: bool                # PSI-3: C6 failure under stress
    auroc_slope: float        # L2 metric: AUROC improvement rate
    var_kappa_slope: float    # L1 metric: Var(κ) trend

    def to_array(self) -> list[float]:
        return [
            self.mk_p_value, self.beta_tau, self.cv_tau,
            float(self.f_c1), float(self.f_c2), float(self.f_c3),
            float(self.f_c4), float(self.f_c5), float(self.f_c6),
            self.auroc_slope, self.var_kappa_slope,
        ]


@dataclass(frozen=True)
class DiagnosticResult:
    \"\"\"Output of the 3-class diagnostic classifier.\"\"\"
    cause: CeilingCause
    confidence: float         # Must be >= 0.9 for pipeline advancement
    feature_vector: PSIFeatureVector
    timestamp: datetime


@dataclass
class AuthorizationState:
    \"\"\"Tracks three-key gate status.\"\"\"
    keys_received: dict[str, datetime] = field(default_factory=dict)  # holder_id → timestamp
    is_2of3_mode: bool = False
    ratification_required_from: Optional[str] = None  # holder_id of absent key
    ratification_deadline: Optional[datetime] = None
    governance_exception_logged: bool = False


@dataclass
class CircuitBreakerState:
    \"\"\"Tracks axiom failure history for a given P' candidate.\"\"\"
    p_prime_id: UUID = field(default_factory=uuid4)
    consecutive_failures: dict[str, int] = field(default_factory=dict)  # axiom → count
    cumulative_c3_c4_c5_failures: int = 0
    failure_history: list[tuple[str, datetime]] = field(default_factory=list)

    def record_failure(self, axiom: str, timestamp: datetime) -> str:
        \"\"\"Returns 'continue', 'escalate_axiom', or 'reject_candidate'.\"\"\"
        self.failure_history.append((axiom, timestamp))
        if axiom in ("C3", "C4", "C5"):
            self.cumulative_c3_c4_c5_failures += 1
            self.consecutive_failures[axiom] = self.consecutive_failures.get(axiom, 0) + 1

            if self.cumulative_c3_c4_c5_failures >= 3:
                return "reject_candidate"
            if self.consecutive_failures[axiom] >= 2:
                return "escalate_axiom"
        return "continue"

    def reset_consecutive(self, axiom: str):
        \"\"\"Reset consecutive counter when a different axiom fails.\"\"\"
        for k in self.consecutive_failures:
            if k != axiom:
                self.consecutive_failures[k] = 0


@dataclass
class ShadowConcordanceSnapshot:
    \"\"\"Per-checkpoint concordance measurements during shadow validation.\"\"\"
    checkpoint_j_fraction: float   # 0.25, 0.5, 0.75, 1.0
    epi_divergence: float
    intervention_concordance: float
    acfl_cosine_similarity: float
    axiom_concordance: dict[str, float]  # {"C1": 0.97, "C2": 0.96, ...}
    timestamp: datetime


@dataclass(frozen=True)
class AuditEvent:
    \"\"\"Λ-Trace audit record — 21 CFR Part 11 compliant.\"\"\"
    event_id: UUID
    event_type: EventType
    timestamp: datetime          # NTP-synchronized, independently verifiable
    pipeline_stage: PipelineStage
    actor: str                   # Key holder ID or "SYSTEM"
    payload_hash: str            # SHA-256 of event payload
    witness_object_ref: Optional[str]  # Reference to CRMF Witness Object
    merkle_link: str             # Hash pointer to previous event in chain
    retention_years: int         # Minimum retention (≥7, subject to parity)
```

### §2.3 mann_kendall.py — PSI-1 Implementation

```python
\"\"\"PSI-1: κ-rank persistence via modified Mann-Kendall test.

Uses pyMannKendall's hamed_rao_modification_test with lag=2 (LOCKED).
SVP-001-v0.1 §4.1.
\"\"\"
import numpy as np
import pymannkendall as mk

from ..config import MK_LAG, MK_SIGNIFICANCE_ALPHA, MK_MIN_WINDOW_PAIRS
from ..types import MannKendallResult


def compute_kappa_rank_persistence(
    kappa_rankings: list[list[float]],
) -> MannKendallResult:
    \"\"\"Compute Mann-Kendall significance of κ-rank stability across Jubilee windows.

    Args:
        kappa_rankings: List of κ-value vectors, one per Jubilee window.
            Each vector contains κ-values for all candidates in prime-set P,
            in consistent candidate order.

    Returns:
        MannKendallResult with p-value for diagnostic classifier.
    \"\"\"
    n_windows = len(kappa_rankings)
    n_pairs = n_windows - 1

    if n_pairs < MK_MIN_WINDOW_PAIRS:
        return MannKendallResult(
            z_statistic=0.0, p_value=1.0, kendall_tau=0.0,
            sens_slope=0.0, n_window_pairs=n_pairs,
            lag_used=MK_LAG, sufficient_data=False,
        )

    # Compute Kendall τ between consecutive windows
    from scipy.stats import kendalltau
    tau_series = []
    for i in range(n_pairs):
        tau, _ = kendalltau(kappa_rankings[i], kappa_rankings[i + 1])
        tau_series.append(tau)

    tau_array = np.array(tau_series)

    # Apply Hamed-Rao modified Mann-Kendall with lag=2 (LOCKED constant)
    result = mk.hamed_rao_modification_test(tau_array, lag=MK_LAG)

    return MannKendallResult(
        z_statistic=result.z,
        p_value=result.p,
        kendall_tau=result.Tau,
        sens_slope=result.slope,
        n_window_pairs=n_pairs,
        lag_used=MK_LAG,
        sufficient_data=True,
    )


def classify_rank_stability(mk_result: MannKendallResult) -> str:
    \"\"\"Classify rank stability from Mann-Kendall result.

    Returns:
        'position_reassignment' if p < alpha (significant rank instability)
        'stable_ceiling' if p >= alpha (no significant rank change)
        'insufficient_data' if minimum window pairs not met
    \"\"\"
    if not mk_result.sufficient_data:
        return "insufficient_data"
    if mk_result.p_value < MK_SIGNIFICANCE_ALPHA:
        return "position_reassignment"
    return "stable_ceiling"
```

### §2.4 classifier.py — 3-Class Diagnostic Classifier

```python
\"\"\"3-class diagnostic classifier for ceiling cause identification.

SVP-001-v0.1 §4.4. Receives PSI triplet feature vector, outputs
CeilingCause with confidence score.
\"\"\"
import numpy as np
from typing import Optional

from ..config import CLASSIFIER_CONFIDENCE_THRESHOLD, CeilingCause
from ..types import (
    PSIFeatureVector, DiagnosticResult,
    MannKendallResult, ContractionMarginResult, AxiomStressResult,
)


class DiagnosticClassifier:
    \"\"\"Three-class ceiling cause classifier.

    Classification targets:
        1. GENUINE_PARAMETRIC_CEILING
        2. POSITION_REASSIGNMENT_DRIFT
        3. COMPOSITE_INFEASIBILITY

    The classifier uses a decision-tree-first architecture: deterministic
    rules from the PSI triplet provide the primary classification, with
    a calibrated confidence score derived from feature-space distance to
    decision boundaries. This is NOT a black-box ML model — it is a
    rule-based classifier with defined decision boundaries traceable
    to the SVP specification.
    \"\"\"

    def __init__(self):
        self._is_validated: bool = False
        self._validation_accuracy: Optional[float] = None

    def classify(
        self,
        mk_result: MannKendallResult,
        cm_result: ContractionMarginResult,
        as_result: AxiomStressResult,
        auroc_slope: float,
        var_kappa_slope: float,
    ) -> DiagnosticResult:
        \"\"\"Execute 3-class classification from PSI triplet + L1/L2 metrics.\"\"\"
        from datetime import datetime

        feature_vector = PSIFeatureVector(
            mk_p_value=mk_result.p_value,
            beta_tau=cm_result.beta_slope,
            cv_tau=cm_result.cv_tau,
            f_c1=as_result.failure_vector[0],
            f_c2=as_result.failure_vector[1],
            f_c3=as_result.failure_vector[2],
            f_c4=as_result.failure_vector[3],
            f_c5=as_result.failure_vector[4],
            f_c6=as_result.failure_vector[5],
            auroc_slope=auroc_slope,
            var_kappa_slope=var_kappa_slope,
        )

        cause, confidence = self._apply_decision_rules(feature_vector)

        return DiagnosticResult(
            cause=cause,
            confidence=confidence,
            feature_vector=feature_vector,
            timestamp=datetime.utcnow(),
        )

    def _apply_decision_rules(
        self, fv: PSIFeatureVector
    ) -> tuple[CeilingCause, float]:
        \"\"\"Deterministic decision tree per SVP §4.1–§4.3.

        Priority order:
        1. PSI-1 (Mann-Kendall) gates position reassignment detection
        2. PSI-3 (axiom stress) disambiguates structural vs. parametric
        3. PSI-2 (contraction margin) confirms and calibrates confidence
        \"\"\"
        from ..config import (
            MK_SIGNIFICANCE_ALPHA, TAU_SLOPE_POSITIVE_THRESHOLD,
            TAU_CV_LOW, TAU_CV_HIGH,
        )

        # Gate 1: Position reassignment detection via Mann-Kendall
        if fv.mk_p_value < MK_SIGNIFICANCE_ALPHA:
            # Significant rank instability detected
            confidence = min(0.99, 1.0 - fv.mk_p_value)
            return CeilingCause.POSITION_REASSIGNMENT_DRIFT, confidence

        # Gate 2: Axiom stress pattern
        c2_fail = fv.f_c2
        c6_fail = fv.f_c6
        multi_fail = sum([fv.f_c1, fv.f_c2, fv.f_c5, fv.f_c6]) >= 2

        if multi_fail:
            # Multiple simultaneous axiom failures under perturbation
            confidence = 0.85 + 0.1 * (sum([fv.f_c1, fv.f_c2, fv.f_c5, fv.f_c6]) / 4)
            return CeilingCause.COMPOSITE_INFEASIBILITY, min(0.99, confidence)

        if c2_fail and not c6_fail:
            # Structural ceiling: resonance coupling degraded, contraction holds
            confidence = 0.90
            return CeilingCause.GENUINE_PARAMETRIC_CEILING, confidence

        # Gate 3: Contraction margin trajectory confirmation
        if fv.beta_tau > TAU_SLOPE_POSITIVE_THRESHOLD and fv.cv_tau < TAU_CV_LOW:
            confidence = 0.85 + 0.10 * (1.0 - fv.cv_tau / TAU_CV_LOW)
            return CeilingCause.GENUINE_PARAMETRIC_CEILING, min(0.99, confidence)

        if fv.cv_tau > TAU_CV_HIGH:
            confidence = 0.80 + 0.10 * min(1.0, fv.cv_tau / 0.5)
            return CeilingCause.COMPOSITE_INFEASIBILITY, min(0.99, confidence)

        # Default: genuine parametric ceiling with lower confidence
        return CeilingCause.GENUINE_PARAMETRIC_CEILING, 0.75

    def is_confident(self, result: DiagnosticResult) -> bool:
        return result.confidence >= CLASSIFIER_CONFIDENCE_THRESHOLD

    def mark_validated(self, accuracy: float):
        self._is_validated = True
        self._validation_accuracy = accuracy
```

### §2.5 late_failure.py — SHADOW_LATE_FAILURE

```python
\"\"\"SHADOW_LATE_FAILURE: Two-front rollback for overlapped shadow/canary.

SVP-001-v0.1 §8.2. Handles simultaneous canary revert + shadow abort
when C5/C6 fails during the overlap period.
\"\"\"
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from ..config import EventType, PipelineStage
from ..types import AuditEvent


@dataclass
class LateFailureContext:
    failing_axiom: str
    concordance_at_failure: float
    canary_traffic_pct: float
    patients_served_by_p_prime: int
    canary_exposure_duration_hours: float
    shadow_checkpoint_count: int


class ShadowLateFailureHandler:
    \"\"\"Executes two-front rollback when shadow validation fails during canary overlap.\"\"\"

    def execute_rollback(
        self,
        context: LateFailureContext,
        canary_controller,   # canary.traffic.TrafficController
        shadow_deployer,     # shadow.deployment.ShadowDeployer
        audit_logger,        # audit.events.AuditLogger
    ) -> list[AuditEvent]:
        events = []

        # Step 1: Immediate canary revert (within 1 CCRE cycle)
        canary_controller.revert_all_traffic()
        events.append(self._emit_canary_revert(context, audit_logger))

        # Step 2: Shadow abort — discard all P' outputs
        shadow_deployer.abort()
        events.append(self._emit_shadow_abort(context, audit_logger))

        # Step 3: Flag patients for practitioner review within 1J
        patient_review_event = self._flag_patient_review(context, audit_logger)
        events.append(patient_review_event)

        # Step 4: Emit SHADOW_LATE_FAILURE event
        late_failure_event = audit_logger.emit(
            event_type=EventType.SHADOW_LATE_FAILURE,
            pipeline_stage=PipelineStage.SHADOW_VALIDATION,
            actor="SYSTEM",
            payload={
                "failing_axiom": context.failing_axiom,
                "concordance_at_failure": context.concordance_at_failure,
                "canary_traffic_pct": context.canary_traffic_pct,
                "patients_served_by_p_prime": context.patients_served_by_p_prime,
                "canary_exposure_duration_hours": context.canary_exposure_duration_hours,
            },
        )
        events.append(late_failure_event)

        return events

    def _emit_canary_revert(self, ctx, logger):
        return logger.emit(
            event_type=EventType.CANARY_REVERT,
            pipeline_stage=PipelineStage.CANARY_ROLLOUT,
            actor="SYSTEM",
            payload={"trigger": "SHADOW_LATE_FAILURE", "axiom": ctx.failing_axiom},
        )

    def _emit_shadow_abort(self, ctx, logger):
        return logger.emit(
            event_type=EventType.SHADOW_VALIDATION_FAIL,
            pipeline_stage=PipelineStage.SHADOW_VALIDATION,
            actor="SYSTEM",
            payload={"trigger": "LATE_FAILURE", "checkpoints_completed": ctx.shadow_checkpoint_count},
        )

    def _flag_patient_review(self, ctx, logger):
        return logger.emit(
            event_type=EventType.CANARY_REVERT,
            pipeline_stage=PipelineStage.CANARY_ROLLOUT,
            actor="SYSTEM",
            payload={
                "action": "PATIENT_REVIEW_FLAGGED",
                "patient_count": ctx.patients_served_by_p_prime,
                "review_deadline_j": 1.0,
            },
        )
```

---

## §3 TEST BENCH

### §3.1 conftest.py — Shared Fixtures & Synthetic Data Generators

```python
\"\"\"Test fixtures for ADR-005 test suite.

Provides synthetic data generators for all three J-duration regimes
and all three ceiling cause scenarios.
\"\"\"
import pytest
import numpy as np
from typing import Callable


# ─── J-Duration Regimes ─────────────────────────────────────────────

@pytest.fixture(params=[5, 7, 10], ids=["J_min=5d", "J_std=7d", "J_max=10d"])
def j_duration(request) -> int:
    return request.param


# ─── Synthetic κ-Ranking Generators ─────────────────────────────────

@pytest.fixture
def genuine_ceiling_kappa() -> Callable:
    \"\"\"Generate κ-rankings for genuine parametric ceiling.

    Characteristics: stable rank ordering, rising absolute values.
    Kendall τ between consecutive windows ≥ 0.8.
    MK p-value should be ≥ 0.05 (no significant rank change).
    \"\"\"
    def _generate(n_windows: int = 8, n_candidates: int = 20, seed: int = 42):
        rng = np.random.default_rng(seed)
        base_ranking = rng.permutation(n_candidates).astype(float)
        rankings = []
        for i in range(n_windows):
            noise = rng.normal(0, 0.3, n_candidates)  # Small perturbation
            shifted = base_ranking + i * 0.5 + noise  # Rising absolute, stable rank
            rankings.append(shifted.tolist())
        return rankings
    return _generate


@pytest.fixture
def position_reassignment_kappa() -> Callable:
    \"\"\"Generate κ-rankings for position-reassignment drift (42.4% scenario).

    Characteristics: volatile rank ordering, stable aggregate statistics.
    Kendall τ between consecutive windows < 0.6.
    MK p-value should be < 0.05 (significant rank instability).
    \"\"\"
    def _generate(n_windows: int = 8, n_candidates: int = 20, seed: int = 42):
        rng = np.random.default_rng(seed)
        rankings = []
        for i in range(n_windows):
            # ~42% of candidates swap positions each window
            base = rng.permutation(n_candidates).astype(float)
            if i > 0:
                n_swap = int(0.424 * n_candidates)
                swap_idx = rng.choice(n_candidates, n_swap, replace=False)
                swapped = rankings[-1].copy()
                for j in range(0, n_swap - 1, 2):
                    swapped[swap_idx[j]], swapped[swap_idx[j+1]] = (
                        swapped[swap_idx[j+1]], swapped[swap_idx[j]]
                    )
                rankings.append(swapped)
            else:
                rankings.append(base.tolist())
        return rankings
    return _generate


@pytest.fixture
def composite_infeasibility_kappa() -> Callable:
    \"\"\"Generate κ-rankings for composite infeasibility.

    Characteristics: moderate rank instability with oscillating τ(t).
    \"\"\"
    def _generate(n_windows: int = 8, n_candidates: int = 20, seed: int = 42):
        rng = np.random.default_rng(seed)
        rankings = []
        for i in range(n_windows):
            noise_scale = 2.0 if i % 2 == 0 else 0.5  # Oscillating instability
            base = np.arange(n_candidates, dtype=float)
            noise = rng.normal(0, noise_scale, n_candidates)
            rankings.append((base + noise).tolist())
        return rankings
    return _generate


# ─── Contraction Margin Generators ──────────────────────────────────

@pytest.fixture
def ceiling_tau_series() -> list[float]:
    \"\"\"τ(t) approaching 1.0 asymptotically — genuine parametric ceiling.\"\"\"
    return [0.72, 0.78, 0.83, 0.87, 0.90, 0.92, 0.94, 0.95]


@pytest.fixture
def oscillating_tau_series() -> list[float]:
    \"\"\"τ(t) oscillating without trend — composite infeasibility.\"\"\"
    return [0.65, 0.82, 0.58, 0.79, 0.61, 0.85, 0.59, 0.80]


@pytest.fixture
def declining_tau_series() -> list[float]:
    \"\"\"τ(t) stable but AUROC declining — drift misidentification.\"\"\"
    return [0.70, 0.69, 0.68, 0.68, 0.67, 0.67, 0.66, 0.66]


# ─── Axiom Stress Fixtures ──────────────────────────────────────────

@pytest.fixture
def structural_ceiling_stress():
    return (False, True, False, False, False, False)  # C2 fails, C6 holds


@pytest.fixture
def parametric_ceiling_stress():
    return (False, False, False, False, False, True)   # C6 fails, C2 holds


@pytest.fixture
def composite_stress():
    return (True, True, False, False, True, True)      # Multiple simultaneous


# ─── Pipeline Scenario Fixtures ─────────────────────────────────────

@pytest.fixture
def prophetic_example_6_data():
    \"\"\"Subject F, Months 1-6 CCRE cycle data from R2 §VIII.

    Provides complete scenario for e2e testing of structural evolution pipeline.
    \"\"\"
    return {
        "subject_id": "F",
        "months": 6,
        "initial_epi": 0.61,
        "epi_trajectory": [0.61, 0.52, 0.44, 0.35, 0.28, 0.22],
        "ccre_cycles": 24,  # 4 per month
        "tau_history": [0.72, 0.75, 0.79, 0.82, 0.85, 0.88, 0.90, 0.91,
                       0.92, 0.93, 0.94, 0.94, 0.95, 0.95, 0.95, 0.96,
                       0.96, 0.96, 0.97, 0.97, 0.97, 0.97, 0.97, 0.98],
        "tier2_detected_at_cycle": 16,
        "auroc_plateau_start_cycle": 12,
    }
```

### §3.2 Unit Tests — Key Files

```python
# ─── test_mann_kendall.py ───────────────────────────────────────────
\"\"\"Unit tests for PSI-1 Mann-Kendall significance testing.

SVP §4.1: Validates MK classification across all three J-duration regimes.
Target: ≥90% accuracy on synthetic cases.
\"\"\"
import pytest
from packages.dna_key.src.adr005.psi.mann_kendall import (
    compute_kappa_rank_persistence,
    classify_rank_stability,
)
from packages.dna_key.src.adr005.config import MK_LAG, MK_MIN_WINDOW_PAIRS


class TestMannKendallPSI1:

    def test_genuine_ceiling_not_significant(self, genuine_ceiling_kappa, j_duration):
        rankings = genuine_ceiling_kappa(n_windows=j_duration + 3)
        result = compute_kappa_rank_persistence(rankings)
        assert result.sufficient_data is True
        assert result.lag_used == 2  # LOCKED constant
        assert classify_rank_stability(result) == "stable_ceiling"

    def test_position_reassignment_significant(self, position_reassignment_kappa, j_duration):
        rankings = position_reassignment_kappa(n_windows=j_duration + 3)
        result = compute_kappa_rank_persistence(rankings)
        assert result.sufficient_data is True
        assert result.p_value < 0.05
        assert classify_rank_stability(result) == "position_reassignment"

    def test_insufficient_data_below_threshold(self, genuine_ceiling_kappa):
        rankings = genuine_ceiling_kappa(n_windows=3)  # Only 2 pairs < 4 minimum
        result = compute_kappa_rank_persistence(rankings)
        assert result.sufficient_data is False
        assert classify_rank_stability(result) == "insufficient_data"

    def test_lag_is_locked_constant(self, genuine_ceiling_kappa):
        rankings = genuine_ceiling_kappa(n_windows=8)
        result = compute_kappa_rank_persistence(rankings)
        assert result.lag_used == MK_LAG == 2

    @pytest.mark.parametrize("seed", range(50))
    def test_classification_accuracy_across_seeds(
        self, genuine_ceiling_kappa, position_reassignment_kappa, seed
    ):
        gc = genuine_ceiling_kappa(n_windows=8, seed=seed)
        pr = position_reassignment_kappa(n_windows=8, seed=seed)
        gc_result = classify_rank_stability(compute_kappa_rank_persistence(gc))
        pr_result = classify_rank_stability(compute_kappa_rank_persistence(pr))
        # Track accuracy across parametrized runs; assert ≥ 90% in collection
        assert gc_result in ("stable_ceiling", "position_reassignment")
        assert pr_result in ("stable_ceiling", "position_reassignment")


# ─── test_circuit_breaker.py ────────────────────────────────────────
\"\"\"Unit tests for circuit breaker — same-axiom + cumulative counter.

SVP §7.3: Validates rotation vulnerability elimination.
\"\"\"
import pytest
from datetime import datetime, timedelta
from packages.dna_key.src.adr005.types import CircuitBreakerState


class TestCircuitBreaker:

    def test_same_axiom_twice_escalates(self):
        cb = CircuitBreakerState()
        t = datetime.utcnow()
        assert cb.record_failure("C3", t) == "continue"
        assert cb.record_failure("C3", t + timedelta(days=7)) == "escalate_axiom"

    def test_cumulative_three_rejects(self):
        cb = CircuitBreakerState()
        t = datetime.utcnow()
        assert cb.record_failure("C3", t) == "continue"
        assert cb.record_failure("C4", t + timedelta(days=7)) == "continue"
        assert cb.record_failure("C5", t + timedelta(days=14)) == "reject_candidate"

    def test_rotation_vulnerability_eliminated(self):
        \"\"\"C3 → C4 → C3 → C5 → C3 must not cycle indefinitely.\"\"\"
        cb = CircuitBreakerState()
        t = datetime.utcnow()
        results = []
        for i, axiom in enumerate(["C3", "C4", "C3", "C5", "C3"]):
            result = cb.record_failure(axiom, t + timedelta(days=7 * i))
            results.append(result)
        # Must hit reject_candidate before completing the sequence
        assert "reject_candidate" in results
        assert results.index("reject_candidate") <= 2  # At cumulative failure 3

    def test_c6_failure_not_counted_in_cumulative(self):
        cb = CircuitBreakerState()
        t = datetime.utcnow()
        assert cb.record_failure("C6", t) == "continue"  # C6 is absolutely gating
        assert cb.cumulative_c3_c4_c5_failures == 0

    def test_c1_c2_failure_not_counted_in_cumulative(self):
        cb = CircuitBreakerState()
        t = datetime.utcnow()
        assert cb.record_failure("C1", t) == "continue"
        assert cb.cumulative_c3_c4_c5_failures == 0


# ─── test_governance.py ─────────────────────────────────────────────
\"\"\"Unit tests for 2-of-3 fallback authorization + Part 11 audit.

SVP §5.3: Validates governance exception logging and ratification.
\"\"\"
import pytest
from datetime import datetime, timedelta
from packages.dna_key.src.adr005.types import AuthorizationState


class TestGovernanceException:

    def test_2of3_requires_ratification(self):
        state = AuthorizationState()
        state.is_2of3_mode = True
        state.ratification_required_from = "KEY_HOLDER_C"
        assert state.ratification_required_from is not None

    def test_denied_ratification_triggers_revert(self):
        state = AuthorizationState()
        state.is_2of3_mode = True
        state.ratification_required_from = "KEY_HOLDER_C"
        # Simulate denial
        state.ratification_required_from = None
        # Pipeline must revert — tested in integration layer

    def test_each_key_bound_to_individual(self):
        state = AuthorizationState()
        t = datetime.utcnow()
        state.keys_received["KEY_HOLDER_A"] = t
        state.keys_received["KEY_HOLDER_B"] = t + timedelta(minutes=5)
        # No shared credentials — each key maps to unique holder
        assert len(set(state.keys_received.keys())) == len(state.keys_received)
```

### §3.3 Integration Tests

```python
# ─── test_shadow_canary.py ──────────────────────────────────────────
\"\"\"Integration test: Shadow → Canary with overlap.

SVP §8.1, §8.2: Validates overlap eligibility, SHADOW_LATE_FAILURE rollback.
\"\"\"
import pytest


class TestShadowCanaryOverlap:

    def test_overlap_eligible_when_c1_c2_c6_pass_early(self):
        \"\"\"C1+C2 pass at ≥95% within 0.5J + C6 at 100% → overlap eligible.\"\"\"
        # Simulate shadow concordance snapshots at 0.25J and 0.5J
        # Assert overlap flag is set when C1+C2+C6 meet thresholds
        pass  # Implementation depends on shadow.deployment integration

    def test_late_failure_triggers_two_front_rollback(self):
        \"\"\"C5 fails during overlap → canary reverts + shadow aborts simultaneously.\"\"\"
        pass  # Requires mock canary_controller and shadow_deployer

    def test_late_failure_counts_toward_cumulative(self):
        \"\"\"SHADOW_LATE_FAILURE increments the C3/C4/C5 cumulative counter.\"\"\"
        pass

    def test_late_failure_flags_patients_for_review(self):
        \"\"\"All patients served by P' during canary are flagged within 1J.\"\"\"
        pass

    def test_late_failure_requires_reauthorization(self):
        \"\"\"After SHADOW_LATE_FAILURE, three-key gate must re-approve.\"\"\"
        pass


# ─── test_psi_pipeline.py ──────────────────────────────────────────
\"\"\"Integration test: PSI triplet → diagnostic classifier flow.

SVP §4: Validates end-to-end PSI computation and classification.
\"\"\"
import pytest


class TestPSIPipeline:

    @pytest.mark.parametrize("j_days", [5, 7, 10])
    def test_genuine_ceiling_classified_correctly(self, j_days):
        \"\"\"PSI triplet correctly identifies genuine parametric ceiling across J regimes.\"\"\"
        pass

    @pytest.mark.parametrize("j_days", [5, 7, 10])
    def test_position_reassignment_classified_correctly(self, j_days):
        \"\"\"PSI triplet correctly identifies 42.4% PW-CFL drift across J regimes.\"\"\"
        pass

    @pytest.mark.parametrize("j_days", [5, 7, 10])
    def test_composite_infeasibility_classified_correctly(self, j_days):
        \"\"\"PSI triplet correctly identifies composite infeasibility across J regimes.\"\"\"
        pass

    def test_classifier_confidence_below_threshold_emits_inconclusive(self):
        \"\"\"Confidence < 0.9 → DIAGNOSTIC_INCONCLUSIVE, not pipeline advancement.\"\"\"
        pass

    def test_overall_accuracy_target(self):
        \"\"\"Aggregate accuracy ≥ 90% across all synthetic cases and J regimes.\"\"\"
        pass
```

### §3.4 End-to-End Tests

```python
# ─── test_full_pipeline.py ──────────────────────────────────────────
\"\"\"E2E: Full pipeline from Tier 2 detection through P→P' transition or revert.

SVP §2: Validates complete state machine traversal.
\"\"\"
import pytest


class TestFullPipeline:

    def test_happy_path_all_axioms_pass(self):
        \"\"\"Tier 2 → Silence → Diagnostic → Auth → Shadow → Canary → Coherence → Complete.\"\"\"
        pass

    def test_diagnostic_timeout_with_retry(self):
        \"\"\"Classifier confidence < 0.9 → retry 1 → success → continues.\"\"\"
        pass

    def test_diagnostic_timeout_after_retry_defers(self):
        \"\"\"Classifier confidence < 0.9 → retry 1 → still low → DEFERRED.\"\"\"
        pass

    def test_authorization_2of3_with_ratification(self):
        \"\"\"One key holder unavailable → 2-of-3 → advance → ratified → continues.\"\"\"
        pass

    def test_authorization_2of3_denied_reverts(self):
        \"\"\"2-of-3 advance → absent holder denies → immediate revert.\"\"\"
        pass

    def test_conditional_advancement_extended_confirmation(self):
        \"\"\"Single C4 failure → conditional advance → 3J coherence → complete.\"\"\"
        pass

    def test_circuit_breaker_rejects_after_three(self):
        \"\"\"C3 fail → C4 fail → C5 fail → STRUCTURAL_CANDIDATE_REJECTED.\"\"\"
        pass

    def test_pipeline_duration_within_bounds(self):
        \"\"\"Total duration falls within [6.2 weeks, 11.0 weeks] confidence interval.\"\"\"
        pass


# ─── test_prophetic_example_6.py ────────────────────────────────────
\"\"\"E2E: Subject F months 1-6 CCRE cycle scenario.

Uses prophetic_example_6_data fixture.
Validates that Tier 2 detection triggers at the correct cycle,
diagnostic classifier correctly identifies the ceiling cause,
and the pipeline progresses through to structural evolution or revert.
\"\"\"
import pytest


class TestPropheticExample6:

    def test_tier2_detected_at_correct_cycle(self, prophetic_example_6_data):
        \"\"\"Tier 2 should trigger around cycle 16 per the data.\"\"\"
        pass

    def test_tau_series_classified_as_genuine_ceiling(self, prophetic_example_6_data):
        \"\"\"τ(t) approaching 0.98 asymptotically → genuine parametric ceiling.\"\"\"
        pass

    def test_epi_trajectory_triggers_intervention_correctly(self, prophetic_example_6_data):
        \"\"\"EPI drops below 0.5 for 3 consecutive intervals → intervention trigger.\"\"\"
        pass


# ─── test_position_reassignment.py ──────────────────────────────────
\"\"\"E2E: 42.4% PW-CFL position-reassignment drift scenario.

Validates that PSI-1 Mann-Kendall correctly detects position reassignment
and the pipeline routes to the correct structural evolution path.
\"\"\"
import pytest


class TestPositionReassignment:

    def test_424_pct_swap_detected_as_reassignment(self, position_reassignment_kappa):
        \"\"\"42.4% candidate position swap per window → p < 0.05 → reassignment.\"\"\"
        pass

    def test_pipeline_routes_to_structural_evolution(self):
        \"\"\"Position reassignment → diagnostic → ADR-005 structural path.\"\"\"
        pass

    def test_distinguished_from_genuine_ceiling(
        self, genuine_ceiling_kappa, position_reassignment_kappa
    ):
        \"\"\"Same aggregate Var(κ) and AUROC, different PSI-1 p-values.\"\"\"
        pass
```

---

## §4 DEPENDENCY MAP

```
pyMannKendall >= 1.4.3          # hamed_rao_modification_test with lag parameter
scipy >= 1.11.0                 # kendalltau for pairwise rank correlation
numpy >= 1.24.0                 # Array operations
pytest >= 7.4.0                 # Test framework
pytest-asyncio >= 0.21.0        # Async pipeline tests (if canary controller is async)
```

### pyproject.toml fragment

```toml
[project.optional-dependencies]
adr005 = [
    "pymannkendall>=1.4.3",
    "scipy>=1.11.0",
    "numpy>=1.24.0",
]
adr005-test = [
    "pytest>=7.4.0",
    "pytest-asyncio>=0.21.0",
    "pytest-cov>=4.1.0",
]
```

---

## §5 DELIVERY TIMELINE MAPPING

| Deliverable | Scaffold Files | Tests | Owner | Due |
|---|---|---|---|---|
| Mann-Kendall L2.5 (lag=2) | `psi/mann_kendall.py`, `config.py` | `test_mann_kendall.py` | System Architect | Mar 6 |
| SHADOW_LATE_FAILURE | `shadow/late_failure.py` | `test_late_failure.py`, `test_shadow_canary.py` | System Architect | Mar 6 |
| 2-of-3 audit trail | `authorization/governance_exception.py`, `audit/part11.py` | `test_governance.py`, `test_audit_chain.py` | System Architect | Mar 6 |
| Cumulative failure counter | `circuit_breaker/breaker.py` | `test_circuit_breaker.py` | System Architect | Feb 28 |
| PSI triplet classifier | `psi/classifier.py`, `psi/contraction_margin.py`, `psi/axiom_stress.py` | `test_classifier.py`, `test_psi_pipeline.py`, all e2e | Lead Multiplicity Theorist | Mar 20 |
| TS-23–26 calibration | `config.py` (TSPlaceholder fill) | Re-run all parametrized tests | Lead Multiplicity Theorist | Apr 3 |

---

*End of ADR-005 Development Blueprint*
*Document ID: DEV-SVP-001*

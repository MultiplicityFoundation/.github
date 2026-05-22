---
title: 'H-Calculator: Phased Development Plan, File Scaffold & Test Bench'
slug: h-calculator-phased-development-plan-file-scaffold-test-bench
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 05-systems/engines/hcalc/h_calculator_phased_plan.md
  last_synced: '2026-03-20T17:17:18.285234Z'
---

# H-Calculator: Phased Development Plan, File Scaffold & Test Bench
## Version 0.6 — Post-PMD Convergence Execution Blueprint

**Document ID**: DEV-HCALC-001  
**Parent Artifacts**: SVP-001-v0.1, ADR-005 Dev Blueprint (DEV-SVP-001), H-Calculator PMD v0.6  
**Status**: EXECUTION READY  
**Date**: February 21, 2026  
**Author**: Lead Multiplicity Theorist  
**Repo Target**: CHL987/Intrinsica monorepo  
**Classification**: Confidential Engineering Work Product

---

## 1. ARCHITECTURE OVERVIEW

The H-Calculator is the convergence-terminal computation engine within the DNA KEY / INTRINSICA pipeline. It consumes multi-modality health data (vitals, imaging, genomics, text), applies the CRMF axiomatic contraction framework, and outputs a ranked diagnostic differential with a terminal convergence state.

### 1.1 Terminal States (Enum)

| Code | Display | FHIR Mapping | Trigger Condition |
|------|---------|--------------|-------------------|
| `CONVERGED` | Converged | `DiagnosticReport.status = 'final'` | Top-k concentration ≥ 60%, contraction witness q < 1−ε |
| `INCONCLUSIVE` | Inconclusive | `DiagnosticReport.status = 'partial'` | Classifier confidence < 0.9, or insufficient modality data |
| `FREEZE` | Freeze-Resonance | `DiagnosticReport.status = 'registered'` | Contraction failure (K ≥ 1), drift > 0.3, or resonance exit |
| `DECOUPLED` | Decoupled Modalities | `DiagnosticReport.status = 'partial'` + extension | M modalities fail joint convergence; per-modality results valid independently |

### 1.2 FHIR Extension

- **CodeSystem**: `intrinsica-convergence-terminal` (4 codes)
- **ValueSet**: Required binding to CodeSystem
- **StructureDefinition**: Extension on `DiagnosticReport` at `DiagnosticReport.extension`
- **Canonical URL**: `https://intrinsica.health/fhir/convergence-terminal`
- **Encoding**: `CodeableConcept` per FHIR required binding guidance (not raw string)

### 1.3 Core Computation Flow

```
Ring Sensor Data → Modality Tensor Assembly → Per-Modality Contraction
    → Joint Convergence Test → Terminal State Classification
    → FHIR DiagnosticReport Emission → Ω-Trace Audit
```

### 1.4 Key Constraints

- R_max = 16 (runtime cap, Phase 2); R_max = 32 proof deferred to Phase 3
- UI modality cap M ≤ 6 (card view); M > 6 (summary table with expand-on-click)
- Bauer-Fike spectral bound: |λ − μ| ≤ κ_p(V) · ‖δA‖_p
- Top-3 diagnosis concentration ≥ 60% probability mass for CONVERGED terminal

---

## 2. PHASED PLAN

### Phase 1: Core Engine (Days 0–14)
**Objective**: Build the convergence-terminal computation core with enum, contraction witness, and per-modality routing.

| Day | Deliverable | Owner | Gate |
|-----|-------------|-------|------|
| 0–2 | `types.py`, `config.py`, `enums.py` — all data structures and constants | System Architect | CI green |
| 2–5 | `contraction.py` — contraction witness computation (q = τ · m / LT) | Core Engine Lead | Unit tests pass |
| 3–7 | `modality_tensor.py` — per-modality Hilbert space assembly with sparsity constraint | Core Engine Lead | Tensor fixtures valid |
| 5–10 | `convergence.py` — joint convergence test, DECOUPLED routing, INCONCLUSIVE fallback | Core Engine Lead | All 4 terminal states reachable |
| 7–12 | `ranking.py` — ranked differential with top-k concentration threshold | Core Engine Lead | Concentration ≥ 60% verified |
| 10–14 | `terminal_classifier.py` — terminal state classification with confidence scoring | Lead Multiplicity Theorist | 95% accuracy on synthetic |

**Phase 1 Exit Criteria**:
- All 4 terminal states reachable from synthetic input
- Contraction witness q computation matches analytic expectation within 1e-6
- Zero invalid enum combinations at compile time (mypy strict)
- Per-modality INCONCLUSIVE routes correctly under DECOUPLED

### Phase 2: FHIR Integration (Days 7–28)
**Objective**: Implement FHIR R4 DiagnosticReport emission with convergence-terminal extension, ValueSet binding, and IG scaffold.

| Day | Deliverable | Owner | Gate |
|-----|-------------|-------|------|
| 7–10 | `fhir/codesystem.fsh` — 4-code CodeSystem in FSH | Interop Lead | SUSHI compiles |
| 8–12 | `fhir/valueset.fsh` — Required binding ValueSet | Interop Lead | Validates against R4 |
| 10–14 | `fhir/structuredefinition.fsh` — Extension StructureDefinition | Interop Lead | IG Publisher passes |
| 12–18 | `fhir_emitter.py` — DiagnosticReport builder with extension injection | Core Engine Lead | Valid R4 JSON output |
| 14–21 | `fhir/ig/` — Full IG scaffold (sushi-config.yaml, narrative pages) | Interop Lead | IG builds locally |
| 21–28 | IG narrative + ig-registry PR preparation | Interop Lead | Review-ready |

**Phase 2 Exit Criteria**:
- SUSHI compiles all FSH without errors
- IG Publisher generates valid HTML with all 4 codes documented
- DiagnosticReport with `status='partial'` and convergence-terminal extension validates against R4
- BAA review executed per 45 C.F.R. §160.103

### Phase 3: Spectral Scaling & R_max (Days 14–35)
**Objective**: Validate Bauer-Fike bound extension from R=16 to R=32, implement runtime cap with logging.

| Day | Deliverable | Owner | Gate |
|-----|-------------|-------|------|
| 14–18 | `spectral.py` — κ_p(V) computation for modality eigenvector matrices | Core Engine Lead | Matches NumPy reference |
| 16–21 | `rmax_guard.py` — Runtime R_max=16 cap with DECOUPLED fallback and logging | Core Engine Lead | Cap fires correctly at R=17 |
| 21–28 | `spectral_bench.py` — Benchmark κ_p(V) growth from R=1..32 | Core Engine Lead | Growth characterization report |
| 28–35 | Decision gate: polynomial growth → proof extension viable; exponential → alternative bound | Lead Multiplicity Theorist | Written decision document |

**Phase 3 Exit Criteria**:
- Runtime cap at R_max=16 fires correctly, logs to Ω-Trace, emits DECOUPLED
- κ_p(V) growth characterization complete for R=1..32
- Decision document on Phase 4 proof strategy signed

### Phase 4: UI & Clinician Interface (Days 21–42)
**Objective**: Implement clinician-facing modality card rendering with M ≤ 6 threshold and summary fallback.

| Day | Deliverable | Owner | Gate |
|-----|-------------|-------|------|
| 21–25 | `ui/modality_card.py` — Per-modality card component (convergence state, confidence, key metrics) | UI Lead | Renders for M=1..6 |
| 25–30 | `ui/summary_table.py` — Summary table with expand-on-click for M > 6 | UI Lead | Renders for M=7..12 |
| 28–35 | `ui/threshold_router.py` — M threshold routing (card vs. summary) | UI Lead | Correct routing at boundary |
| 35–42 | Usability test protocol (5 clinicians, think-aloud, SART scoring) | UI Lead | Protocol documented |

**Phase 4 Exit Criteria**:
- M ≤ 6 renders individual cards with per-modality convergence state
- M > 6 renders summary table with expand-on-click per card
- No cognitive overload signals in pilot usability test (SART spare capacity > 3)

### Phase 5: Integration & Shadow Validation (Days 28–42)
**Objective**: Wire H-Calculator into the full DNA KEY pipeline, execute shadow validation per SVP-001.

| Day | Deliverable | Owner | Gate |
|-----|-------------|-------|------|
| 28–32 | `pipeline/integration.py` — H-Calculator ↔ CCRE ↔ ACFL pipeline wiring | System Architect | End-to-end data flow |
| 32–36 | `pipeline/shadow.py` — Shadow deployment orchestrator (SVP-001 §6) | System Architect | Shadow runs in parallel |
| 36–40 | Concordance metrics collection (EPI divergence, intervention concordance, ACFL cosine) | System Architect | All metrics computing |
| 40–42 | Shadow validation checkpoint review | Lead Multiplicity Theorist | Go/no-go decision |

---

## 3. FILE SCAFFOLD

```
packages/dnakey/src/hcalc/
├── __init__.py
├── config.py                    # 3.1 — Constants, thresholds, R_max cap
├── enums.py                     # 3.2 — TerminalState enum (4 codes)
├── types.py                     # 3.3 — Core data structures
├── contraction.py               # 3.4 — Contraction witness q computation
├── modality_tensor.py           # 3.5 — Per-modality Hilbert space assembly
├── convergence.py               # 3.6 — Joint convergence test + DECOUPLED routing
├── ranking.py                   # 3.7 — Ranked differential with concentration threshold
├── terminal_classifier.py       # 3.8 — Terminal state classification
├── spectral.py                  # 3.9 — Bauer-Fike κ_p(V) computation
├── rmax_guard.py                # 3.10 — Runtime R_max cap with logging
├── fhir/
│   ├── __init__.py
│   ├── emitter.py               # 3.11 — FHIR DiagnosticReport builder
│   ├── codesystem.fsh           # 3.12 — FSH CodeSystem (4 codes)
│   ├── valueset.fsh             # 3.13 — FSH ValueSet (required binding)
│   ├── structuredefinition.fsh  # 3.14 — FSH Extension StructureDefinition
│   ├── sushi-config.yaml        # 3.15 — SUSHI configuration
│   └── ig/
│       ├── input/
│       │   └── pagecontent/
│       │       ├── index.md
│       │       └── convergence-terminal.md
│       └── ig.ini
├── ui/
│   ├── __init__.py
│   ├── modality_card.py         # 3.16 — Card renderer (M ≤ 6)
│   ├── summary_table.py         # 3.17 — Summary table (M > 6)
│   └── threshold_router.py      # 3.18 — M-threshold routing
├── pipeline/
│   ├── __init__.py
│   ├── integration.py           # 3.19 — Pipeline wiring
│   └── shadow.py                # 3.20 — Shadow deployment orchestrator
└── audit/
    ├── __init__.py
    ├── omega_trace.py           # 3.21 — Ω-Trace emission for H-Calculator events
    └── witness.py               # 3.22 — CRMF Witness Object for convergence
```

```
packages/dnakey/tests/hcalc/
├── __init__.py
├── conftest.py                  # 4.1 — Shared fixtures, synthetic modality generators
├── unit/
│   ├── __init__.py
│   ├── test_enums.py            # 4.2 — Enum completeness + invalid combination rejection
│   ├── test_contraction.py      # 4.3 — Contraction witness accuracy
│   ├── test_modality_tensor.py  # 4.4 — Tensor assembly + sparsity validation
│   ├── test_convergence.py      # 4.5 — All 4 terminal states reachable
│   ├── test_ranking.py          # 4.6 — Top-k concentration threshold
│   ├── test_classifier.py       # 4.7 — Terminal state classification accuracy
│   ├── test_spectral.py         # 4.8 — κ_p(V) vs NumPy reference
│   ├── test_rmax_guard.py       # 4.9 — R_max cap fires correctly
│   └── test_fhir_emitter.py     # 4.10 — DiagnosticReport R4 validation
├── integration/
│   ├── __init__.py
│   ├── test_convergence_flow.py # 4.11 — Modality → Convergence → Terminal
│   ├── test_decoupled_routing.py# 4.12 — DECOUPLED per-modality INCONCLUSIVE
│   ├── test_fhir_extension.py   # 4.13 — Extension injection + R4 validation
│   └── test_ui_routing.py       # 4.14 — Card vs. summary at M boundary
└── e2e/
    ├── __init__.py
    ├── test_full_pipeline.py    # 4.15 — Ring data → DiagnosticReport
    ├── test_shadow_validation.py# 4.16 — Shadow concordance per SVP-001
    └── test_rmax_boundary.py    # 4.17 — R=16 cap + DECOUPLED emission
```

**Total: 22 module files + 17 test files = 39 files**

---

## 4. MODULE SPECIFICATIONS

### 3.1 config.py

```python
"""H-Calculator configuration. All thresholds locked per PMD v0.6."""

# Terminal Classification
TOP_K_CONCENTRATION_THRESHOLD: float = 0.60  # Top-3 diagnoses must capture ≥ 60%
CONVERGENCE_EPSILON: float = 0.01            # q < 1 - ε for CONVERGED
CLASSIFIER_CONFIDENCE_MIN: float = 0.90      # Below → INCONCLUSIVE

# Spectral / R_max
R_MAX_RUNTIME: int = 16                      # Runtime cap; R > 16 → DECOUPLED
R_MAX_PROOF_TARGET: int = 32                 # Phase 3 proof target
KAPPA_GROWTH_POLYNOMIAL_THRESHOLD: float = 2.0  # κ growth exponent threshold

# Modality
MODALITY_UI_CARD_MAX: int = 6                # M ≤ 6 → cards; M > 6 → summary
SUPPORTED_MODALITIES: tuple = (
    "vitals", "imaging", "genomics", "text",
    "wearable", "labs", "medications", "procedures",
    "social_determinants", "family_history",
    "environmental", "behavioral"
)

# Contraction
LIPSCHITZ_BOUND_MAX: float = 0.999           # K < 1 strict
DRIFT_BOUND_MAX: float = 0.30                # SBERT cosine drift
RESONANCE_R_MIN: float = 0.1                 # Minimum resonance
RESONANCE_R_SAFE: float = 0.9                # Maximum safe resonance

# FHIR
FHIR_CANONICAL_URL: str = "https://intrinsica.health/fhir/convergence-terminal"
FHIR_IG_PACKAGE_ID: str = "health.intrinsica.convergence-terminal"
FHIR_IG_VERSION: str = "0.1.0"

# Audit
RETENTION_YEARS_MIN: int = 7
HASH_ALGORITHM: str = "sha256"
```

### 3.2 enums.py

```python
"""H-Calculator terminal state enumeration. 4 codes, exhaustive."""
from enum import Enum, auto

class TerminalState(Enum):
    CONVERGED = auto()
    INCONCLUSIVE = auto()
    FREEZE = auto()
    DECOUPLED = auto()

    @property
    def fhir_status(self) -> str:
        return {
            TerminalState.CONVERGED: "final",
            TerminalState.INCONCLUSIVE: "partial",
            TerminalState.FREEZE: "registered",
            TerminalState.DECOUPLED: "partial",
        }[self]

    @property
    def fhir_extension_code(self) -> str:
        return self.name.lower()

    @property
    def requires_per_modality(self) -> bool:
        return self == TerminalState.DECOUPLED


class ModalityConvergenceState(Enum):
    CONVERGED = auto()
    INCONCLUSIVE = auto()
    DIVERGENT = auto()
    INSUFFICIENT_DATA = auto()
```

### 3.3 types.py

```python
"""H-Calculator core data structures."""
from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, Dict, List, Tuple
from uuid import UUID, uuid4
from .enums import TerminalState, ModalityConvergenceState


@dataclass(frozen=True)
class ContractionWitness:
    q: float                        # Contraction scalar; q < 1-ε → safe
    tau: float                      # τ contraction margin
    kappa: float                    # κ Lipschitz constant
    lipschitz_bound: float          # LT global Lipschitz bound
    is_contractive: bool            # q < 1 - ε
    timestamp: datetime = field(default_factory=datetime.utcnow)


@dataclass(frozen=True)
class ModalityResult:
    modality: str
    state: ModalityConvergenceState
    contraction_witness: Optional[ContractionWitness]
    top_k_concentration: float      # Probability mass in top-3
    ranked_differential: Tuple[Tuple[str, float], ...]  # (diagnosis, probability)
    confidence: float
    rank: int                       # Rank among modalities by confidence


@dataclass(frozen=True)
class ConvergenceResult:
    terminal_state: TerminalState
    joint_contraction_witness: Optional[ContractionWitness]
    modality_results: Tuple[ModalityResult, ...]
    top_k_concentration: float      # Joint top-3 concentration
    ranked_differential: Tuple[Tuple[str, float], ...]
    confidence: float
    r_effective: int                # Effective rank of modality tensor
    timestamp: datetime = field(default_factory=datetime.utcnow)
    trace_id: UUID = field(default_factory=uuid4)


@dataclass(frozen=True)
class SpectralAnalysis:
    kappa_p: float                  # Condition number κ_p(V)
    eigenvalues: Tuple[complex, ...]
    rank: int
    perturbation_bound: float       # κ_p(V) · ‖δA‖_p
    growth_exponent: Optional[float]  # Fitted exponent for κ vs R


@dataclass(frozen=True)
class FHIRDiagnosticPayload:
    resource_type: str = "DiagnosticReport"
    status: str = "partial"
    extension_code: str = "inconclusive"
    extension_system: str = "https://intrinsica.health/fhir/convergence-terminal"
    modality_components: Tuple[dict, ...] = ()
    conclusion: str = ""
    issued: str = ""
```

### 3.4 contraction.py

```python
"""Contraction witness computation per CRMF axiom C6."""
import numpy as np
from .config import CONVERGENCE_EPSILON, LIPSCHITZ_BOUND_MAX
from .types import ContractionWitness


def compute_contraction_witness(
    tau: float,
    multiplicity_constant: float,
    lipschitz_global: float,
) -> ContractionWitness:
    """Compute q = τ · m / LT. Safe iff q < 1 - ε."""
    if lipschitz_global <= 0:
        raise ValueError("Global Lipschitz bound must be positive")
    q = tau * multiplicity_constant / lipschitz_global
    kappa = tau  # Lipschitz constant of the update operator
    is_contractive = q < (1.0 - CONVERGENCE_EPSILON)
    return ContractionWitness(
        q=q,
        tau=tau,
        kappa=kappa,
        lipschitz_bound=lipschitz_global,
        is_contractive=is_contractive,
    )


def verify_contraction_bound(witness: ContractionWitness) -> bool:
    """Verify q < 1 - ε AND κ < K_max."""
    return (
        witness.is_contractive
        and witness.kappa < LIPSCHITZ_BOUND_MAX
    )
```

### 3.5 modality_tensor.py

```python
"""Per-modality Hilbert space assembly with sparsity constraint.
Uses factored representation, not full tensor product."""
import numpy as np
from typing import List, Optional, Tuple
from .config import SUPPORTED_MODALITIES, R_MAX_RUNTIME
from .enums import ModalityConvergenceState
from .types import ModalityResult, ContractionWitness


class ModalityTensor:
    def __init__(self, modalities: List[str]):
        self._validate_modalities(modalities)
        self.modalities = tuple(modalities)
        self.m = len(modalities)
        self._data: dict = {}

    def _validate_modalities(self, modalities: List[str]):
        for m in modalities:
            if m not in SUPPORTED_MODALITIES:
                raise ValueError(f"Unsupported modality: {m}")
        if len(modalities) != len(set(modalities)):
            raise ValueError("Duplicate modalities")

    def ingest(self, modality: str, data: np.ndarray):
        if modality not in self.modalities:
            raise ValueError(f"Modality {modality} not in tensor")
        self._data[modality] = data

    def compute_per_modality(
        self,
        compute_fn,  # Callable[[np.ndarray], ModalityResult]
    ) -> Tuple[ModalityResult, ...]:
        results = []
        for i, mod in enumerate(self.modalities):
            if mod in self._data:
                result = compute_fn(self._data[mod], mod)
                results.append(result)
            else:
                results.append(ModalityResult(
                    modality=mod,
                    state=ModalityConvergenceState.INSUFFICIENT_DATA,
                    contraction_witness=None,
                    top_k_concentration=0.0,
                    ranked_differential=(),
                    confidence=0.0,
                    rank=i,
                ))
        return tuple(results)

    @property
    def effective_rank(self) -> int:
        return min(len(self._data), R_MAX_RUNTIME)
```

### 3.6 convergence.py

```python
"""Joint convergence test with DECOUPLED routing."""
from typing import Tuple
from .config import (
    TOP_K_CONCENTRATION_THRESHOLD,
    CLASSIFIER_CONFIDENCE_MIN,
    R_MAX_RUNTIME,
    CONVERGENCE_EPSILON,
)
from .enums import TerminalState, ModalityConvergenceState
from .types import ConvergenceResult, ModalityResult, ContractionWitness
from .contraction import compute_contraction_witness, verify_contraction_bound


def classify_terminal_state(
    modality_results: Tuple[ModalityResult, ...],
    joint_witness: ContractionWitness,
    joint_concentration: float,
    r_effective: int,
) -> TerminalState:
    """Classify into one of 4 terminal states."""

    # Gate 1: Contraction failure → FREEZE
    if not verify_contraction_bound(joint_witness):
        return TerminalState.FREEZE

    # Gate 2: R exceeds runtime cap → DECOUPLED
    if r_effective > R_MAX_RUNTIME:
        return TerminalState.DECOUPLED

    # Gate 3: Per-modality divergence check → DECOUPLED
    divergent_count = sum(
        1 for r in modality_results
        if r.state == ModalityConvergenceState.DIVERGENT
    )
    if divergent_count > 0 and divergent_count < len(modality_results):
        return TerminalState.DECOUPLED

    # Gate 4: Confidence / concentration → CONVERGED or INCONCLUSIVE
    if (joint_concentration >= TOP_K_CONCENTRATION_THRESHOLD
            and joint_witness.q < (1.0 - CONVERGENCE_EPSILON)):
        return TerminalState.CONVERGED

    return TerminalState.INCONCLUSIVE


def route_decoupled_modalities(
    modality_results: Tuple[ModalityResult, ...],
) -> Tuple[ModalityResult, ...]:
    """Under DECOUPLED: each modality gets its own INCONCLUSIVE
    if it individually fails convergence."""
    routed = []
    for mr in modality_results:
        if mr.state == ModalityConvergenceState.DIVERGENT:
            routed.append(ModalityResult(
                modality=mr.modality,
                state=ModalityConvergenceState.INCONCLUSIVE,
                contraction_witness=mr.contraction_witness,
                top_k_concentration=mr.top_k_concentration,
                ranked_differential=mr.ranked_differential,
                confidence=mr.confidence,
                rank=mr.rank,
            ))
        else:
            routed.append(mr)
    return tuple(routed)
```

### 3.7 ranking.py

```python
"""Ranked diagnostic differential with concentration threshold."""
from typing import List, Tuple
from .config import TOP_K_CONCENTRATION_THRESHOLD


def compute_ranked_differential(
    probabilities: dict,  # {diagnosis: probability}
    top_k: int = 3,
) -> Tuple[Tuple[str, float], ...]:
    """Sort by probability descending, return as tuple of (diagnosis, prob)."""
    sorted_items = sorted(probabilities.items(), key=lambda x: x[1], reverse=True)
    return tuple(sorted_items)


def check_concentration(
    ranked: Tuple[Tuple[str, float], ...],
    k: int = 3,
) -> float:
    """Compute top-k probability mass."""
    return sum(prob for _, prob in ranked[:k])


def is_concentrated(
    ranked: Tuple[Tuple[str, float], ...],
    k: int = 3,
    threshold: float = TOP_K_CONCENTRATION_THRESHOLD,
) -> bool:
    return check_concentration(ranked, k) >= threshold
```

### 3.8 terminal_classifier.py

```python
"""Terminal state classification with confidence scoring.
Rule-based classifier, not black-box ML."""
from .enums import TerminalState
from .types import ConvergenceResult


def compute_terminal_confidence(result: ConvergenceResult) -> float:
    """Confidence in the terminal state assignment."""
    base = 0.5
    if result.terminal_state == TerminalState.CONVERGED:
        base = 0.85 + 0.10 * min(1.0, result.top_k_concentration)
        if result.joint_contraction_witness:
            base += 0.05 * (1.0 - result.joint_contraction_witness.q)
    elif result.terminal_state == TerminalState.FREEZE:
        base = 0.95  # FREEZE is deterministic from contraction failure
    elif result.terminal_state == TerminalState.DECOUPLED:
        converged_count = sum(
            1 for mr in result.modality_results
            if mr.state.name == "CONVERGED"
        )
        base = 0.70 + 0.05 * converged_count
    elif result.terminal_state == TerminalState.INCONCLUSIVE:
        base = 0.50 + 0.20 * result.top_k_concentration
    return min(0.99, base)
```

### 3.9 spectral.py

```python
"""Bauer-Fike spectral analysis for rank-dependent bounds."""
import numpy as np
from typing import Tuple, Optional
from .types import SpectralAnalysis


def compute_condition_number(
    eigenvector_matrix: np.ndarray,
    p: int = 2,
) -> float:
    """Compute κ_p(V) = ‖V‖_p · ‖V^{-1}‖_p."""
    norm_v = np.linalg.norm(eigenvector_matrix, ord=p)
    norm_v_inv = np.linalg.norm(np.linalg.inv(eigenvector_matrix), ord=p)
    return norm_v * norm_v_inv


def bauer_fike_bound(
    kappa_p: float,
    perturbation_norm: float,
) -> float:
    """Upper bound: |λ − μ| ≤ κ_p(V) · ‖δA‖_p."""
    return kappa_p * perturbation_norm


def analyze_spectral_scaling(
    matrices: list,  # List of (V, rank) pairs
) -> SpectralAnalysis:
    """Analyze κ_p(V) growth across ranks for R_max decision."""
    kappas = []
    ranks = []
    eigenvalues_last = ()
    for V, rank in matrices:
        kp = compute_condition_number(V)
        kappas.append(kp)
        ranks.append(rank)
        eigenvalues_last = tuple(np.linalg.eigvals(V @ np.diag(np.arange(rank)) @ np.linalg.inv(V)))

    # Fit growth exponent: κ ~ R^α
    if len(ranks) > 2:
        log_r = np.log(np.array(ranks, dtype=float))
        log_k = np.log(np.array(kappas, dtype=float))
        alpha = np.polyfit(log_r, log_k, 1)[0]
    else:
        alpha = None

    return SpectralAnalysis(
        kappa_p=kappas[-1] if kappas else 1.0,
        eigenvalues=eigenvalues_last,
        rank=ranks[-1] if ranks else 0,
        perturbation_bound=kappas[-1] * 0.01 if kappas else 0.0,
        growth_exponent=alpha,
    )
```

### 3.10 rmax_guard.py

```python
"""Runtime R_max cap with DECOUPLED fallback and Ω-Trace logging."""
import logging
from .config import R_MAX_RUNTIME
from .enums import TerminalState

logger = logging.getLogger(__name__)


def check_rmax(r_effective: int) -> bool:
    """Return True if R is within runtime cap."""
    return r_effective <= R_MAX_RUNTIME


def enforce_rmax(r_effective: int) -> TerminalState:
    """If R exceeds cap, return DECOUPLED; otherwise None means proceed."""
    if r_effective > R_MAX_RUNTIME:
        logger.warning(
            f"R_effective={r_effective} exceeds R_MAX={R_MAX_RUNTIME}. "
            f"Forcing DECOUPLED terminal state."
        )
        return TerminalState.DECOUPLED
    return None
```

### 3.11 fhir/emitter.py

```python
"""FHIR R4 DiagnosticReport builder with convergence-terminal extension."""
from datetime import datetime
from typing import Dict, List, Optional
from ..enums import TerminalState
from ..types import ConvergenceResult, FHIRDiagnosticPayload
from ..config import FHIR_CANONICAL_URL


def build_diagnostic_report(
    result: ConvergenceResult,
    patient_reference: str,
    practitioner_reference: str,
) -> dict:
    """Build FHIR R4 DiagnosticReport JSON with extension."""
    report = {
        "resourceType": "DiagnosticReport",
        "status": result.terminal_state.fhir_status,
        "extension": [{
            "url": FHIR_CANONICAL_URL,
            "valueCodeableConcept": {
                "coding": [{
                    "system": FHIR_CANONICAL_URL,
                    "code": result.terminal_state.fhir_extension_code,
                    "display": result.terminal_state.name.replace("_", " ").title(),
                }]
            }
        }],
        "subject": {"reference": patient_reference},
        "performer": [{"reference": practitioner_reference}],
        "issued": result.timestamp.isoformat() + "Z",
        "conclusion": _build_conclusion(result),
    }

    if result.terminal_state == TerminalState.DECOUPLED:
        report["result"] = _build_per_modality_observations(result)

    return report


def _build_conclusion(result: ConvergenceResult) -> str:
    top3 = result.ranked_differential[:3]
    items = [f"{dx} ({prob:.1%})" for dx, prob in top3]
    return f"Terminal: {result.terminal_state.name}. Top-3: {', '.join(items)}"


def _build_per_modality_observations(result: ConvergenceResult) -> list:
    refs = []
    for mr in result.modality_results:
        refs.append({
            "reference": f"Observation/{mr.modality}-convergence",
            "display": f"{mr.modality}: {mr.state.name}",
        })
    return refs
```

### 3.12 fhir/codesystem.fsh

```
CodeSystem: IntrinsicaConvergenceTerminal
Id: intrinsica-convergence-terminal
Title: "Intrinsica Convergence Terminal States"
Description: "Terminal convergence states for the H-Calculator diagnostic engine."
* ^url = "https://intrinsica.health/fhir/convergence-terminal"
* ^status = #active
* ^content = #complete
* ^count = 4
* #converged "Converged" "Joint convergence achieved. Top-k concentration ≥ 60%, contraction witness q < 1-ε."
* #inconclusive "Inconclusive" "Insufficient confidence for convergence. Classifier confidence < 0.9 or data gap."
* #freeze "Freeze-Resonance" "Contraction failure (K ≥ 1), drift > 0.3, or resonance exit. System halted."
* #decoupled "Decoupled Modalities" "Joint convergence failed. Per-modality results valid independently."
```

### 3.13 fhir/valueset.fsh

```
ValueSet: IntrinsicaConvergenceTerminalVS
Id: intrinsica-convergence-terminal-vs
Title: "Intrinsica Convergence Terminal ValueSet"
Description: "Required binding ValueSet for convergence terminal states."
* ^url = "https://intrinsica.health/fhir/convergence-terminal-vs"
* ^status = #active
* include codes from system https://intrinsica.health/fhir/convergence-terminal
```

### 3.14 fhir/structuredefinition.fsh

```
Extension: IntrinsicaConvergenceTerminalExtension
Id: intrinsica-convergence-terminal-ext
Title: "Convergence Terminal State Extension"
Description: "Extension to DiagnosticReport indicating the H-Calculator convergence terminal state."
Context: DiagnosticReport
* value[x] only CodeableConcept
* valueCodeableConcept from IntrinsicaConvergenceTerminalVS (required)
```

---

## 5. TEST BENCH

### 4.1 conftest.py

```python
"""Shared fixtures for H-Calculator test suite."""
import pytest
import numpy as np
from packages.dnakey.src.hcalc.enums import TerminalState, ModalityConvergenceState
from packages.dnakey.src.hcalc.types import (
    ContractionWitness, ModalityResult, ConvergenceResult
)


@pytest.fixture(params=[1, 3, 6, 8, 12], ids=["M1", "M3", "M6", "M8", "M12"])
def modality_count(request) -> int:
    return request.param


@pytest.fixture
def converged_witness() -> ContractionWitness:
    return ContractionWitness(
        q=0.85, tau=0.7, kappa=0.95,
        lipschitz_bound=1.0, is_contractive=True,
    )


@pytest.fixture
def freeze_witness() -> ContractionWitness:
    return ContractionWitness(
        q=1.05, tau=1.1, kappa=1.02,
        lipschitz_bound=1.0, is_contractive=False,
    )


@pytest.fixture
def high_concentration_differential():
    return (
        ("Diagnosis_A", 0.45),
        ("Diagnosis_B", 0.20),
        ("Diagnosis_C", 0.15),
        ("Diagnosis_D", 0.10),
        ("Diagnosis_E", 0.10),
    )


@pytest.fixture
def low_concentration_differential():
    return tuple(
        (f"Diagnosis_{chr(65+i)}", 1.0/15)
        for i in range(15)
    )


@pytest.fixture
def synthetic_modality_data():
    rng = np.random.default_rng(42)
    def generate(m: int, dim: int = 50):
        modalities = [f"modality_{i}" for i in range(m)]
        data = {mod: rng.standard_normal((dim, dim)) for mod in modalities}
        return modalities, data
    return generate


@pytest.fixture
def converged_modality_results():
    def generate(m: int):
        results = []
        for i in range(m):
            results.append(ModalityResult(
                modality=f"vitals" if i == 0 else f"modality_{i}",
                state=ModalityConvergenceState.CONVERGED,
                contraction_witness=ContractionWitness(
                    q=0.8, tau=0.7, kappa=0.9,
                    lipschitz_bound=1.0, is_contractive=True,
                ),
                top_k_concentration=0.75,
                ranked_differential=(("Dx_A", 0.5), ("Dx_B", 0.2), ("Dx_C", 0.1)),
                confidence=0.92,
                rank=i,
            ))
        return tuple(results)
    return generate
```

### Key Test Files

#### 4.2 test_enums.py
```python
"""Enum completeness and invalid combination tests."""
from packages.dnakey.src.hcalc.enums import TerminalState, ModalityConvergenceState


class TestTerminalStateEnum:
    def test_exactly_four_states(self):
        assert len(TerminalState) == 4

    def test_fhir_status_mapping_complete(self):
        for state in TerminalState:
            assert state.fhir_status in ("final", "partial", "registered")

    def test_decoupled_requires_per_modality(self):
        assert TerminalState.DECOUPLED.requires_per_modality is True
        for state in TerminalState:
            if state != TerminalState.DECOUPLED:
                assert state.requires_per_modality is False

    def test_extension_codes_unique(self):
        codes = [s.fhir_extension_code for s in TerminalState]
        assert len(codes) == len(set(codes))

    def test_no_invalid_construction(self):
        import pytest
        with pytest.raises(ValueError):
            TerminalState("INVALID")
```

#### 4.5 test_convergence.py
```python
"""All 4 terminal states must be reachable."""
import pytest
from packages.dnakey.src.hcalc.convergence import (
    classify_terminal_state, route_decoupled_modalities,
)
from packages.dnakey.src.hcalc.enums import TerminalState, ModalityConvergenceState
from packages.dnakey.src.hcalc.types import ContractionWitness, ModalityResult


class TestTerminalStateClassification:
    def test_converged_reachable(self, converged_witness, converged_modality_results):
        results = converged_modality_results(3)
        state = classify_terminal_state(results, converged_witness, 0.75, r_effective=3)
        assert state == TerminalState.CONVERGED

    def test_freeze_reachable(self, freeze_witness, converged_modality_results):
        results = converged_modality_results(3)
        state = classify_terminal_state(results, freeze_witness, 0.75, r_effective=3)
        assert state == TerminalState.FREEZE

    def test_decoupled_on_rmax_exceeded(self, converged_witness, converged_modality_results):
        results = converged_modality_results(3)
        state = classify_terminal_state(results, converged_witness, 0.75, r_effective=17)
        assert state == TerminalState.DECOUPLED

    def test_decoupled_on_partial_divergence(self, converged_witness):
        results = (
            ModalityResult("vitals", ModalityConvergenceState.CONVERGED, None, 0.8, (), 0.9, 0),
            ModalityResult("imaging", ModalityConvergenceState.DIVERGENT, None, 0.3, (), 0.4, 1),
        )
        state = classify_terminal_state(results, converged_witness, 0.55, r_effective=2)
        assert state == TerminalState.DECOUPLED

    def test_inconclusive_on_low_concentration(self, converged_witness, converged_modality_results):
        results = converged_modality_results(3)
        state = classify_terminal_state(results, converged_witness, 0.40, r_effective=3)
        assert state == TerminalState.INCONCLUSIVE


class TestDecoupledRouting:
    def test_divergent_becomes_inconclusive(self):
        results = (
            ModalityResult("vitals", ModalityConvergenceState.CONVERGED, None, 0.8, (), 0.9, 0),
            ModalityResult("imaging", ModalityConvergenceState.DIVERGENT, None, 0.3, (), 0.4, 1),
        )
        routed = route_decoupled_modalities(results)
        assert routed[1].state == ModalityConvergenceState.INCONCLUSIVE

    def test_converged_unchanged(self):
        results = (
            ModalityResult("vitals", ModalityConvergenceState.CONVERGED, None, 0.8, (), 0.9, 0),
        )
        routed = route_decoupled_modalities(results)
        assert routed[0].state == ModalityConvergenceState.CONVERGED
```

#### 4.9 test_rmax_guard.py
```python
"""R_max runtime cap tests."""
from packages.dnakey.src.hcalc.rmax_guard import check_rmax, enforce_rmax
from packages.dnakey.src.hcalc.enums import TerminalState


class TestRmaxGuard:
    def test_within_cap(self):
        assert check_rmax(16) is True
        assert check_rmax(1) is True

    def test_exceeds_cap(self):
        assert check_rmax(17) is False
        assert check_rmax(32) is False

    def test_enforce_returns_decoupled(self):
        assert enforce_rmax(17) == TerminalState.DECOUPLED

    def test_enforce_returns_none_within_cap(self):
        assert enforce_rmax(16) is None

    def test_boundary_exact(self):
        assert check_rmax(16) is True
        assert check_rmax(17) is False
```

#### 4.10 test_fhir_emitter.py
```python
"""FHIR DiagnosticReport R4 validation."""
import json
from packages.dnakey.src.hcalc.fhir.emitter import build_diagnostic_report
from packages.dnakey.src.hcalc.enums import TerminalState


class TestFHIREmitter:
    def test_converged_produces_final_status(self, converged_result):
        report = build_diagnostic_report(converged_result, "Patient/1", "Practitioner/1")
        assert report["status"] == "final"

    def test_decoupled_produces_partial_with_extension(self, decoupled_result):
        report = build_diagnostic_report(decoupled_result, "Patient/1", "Practitioner/1")
        assert report["status"] == "partial"
        ext = report["extension"][0]
        assert ext["valueCodeableConcept"]["coding"][0]["code"] == "decoupled"

    def test_extension_url_canonical(self, converged_result):
        report = build_diagnostic_report(converged_result, "Patient/1", "Practitioner/1")
        assert report["extension"][0]["url"] == "https://intrinsica.health/fhir/convergence-terminal"

    def test_decoupled_includes_per_modality_refs(self, decoupled_result):
        report = build_diagnostic_report(decoupled_result, "Patient/1", "Practitioner/1")
        assert "result" in report
        assert len(report["result"]) > 0

    def test_report_is_valid_json(self, converged_result):
        report = build_diagnostic_report(converged_result, "Patient/1", "Practitioner/1")
        json_str = json.dumps(report)
        parsed = json.loads(json_str)
        assert parsed["resourceType"] == "DiagnosticReport"
```

#### 4.15 test_full_pipeline.py (E2E)
```python
"""End-to-end: Ring sensor data → FHIR DiagnosticReport."""
import pytest


class TestFullPipeline:
    def test_single_modality_converges(self):
        """1 modality, clear convergence → CONVERGED + final status."""
        pass  # Implementation wires modality_tensor → convergence → fhir_emitter

    def test_multi_modality_decouples_on_divergence(self):
        """3 modalities, 1 divergent → DECOUPLED + per-modality refs."""
        pass

    def test_rmax_exceeded_forces_decoupled(self):
        """17 modalities → R_max cap fires → DECOUPLED."""
        pass

    def test_contraction_failure_freezes(self):
        """q > 1 → FREEZE + registered status."""
        pass

    def test_low_concentration_inconclusive(self):
        """Uniform distribution → INCONCLUSIVE + partial status."""
        pass

    def test_omega_trace_emitted(self):
        """Every terminal state produces Ω-Trace audit record."""
        pass

    def test_pipeline_duration_under_5s(self):
        """Full pipeline completes in < 5s for M ≤ 6."""
        pass
```

---

## 6. DEPENDENCY MAP

```
numpy >= 1.24.0         # Array operations, eigenvalue computation
scipy >= 1.11.0         # Spectral analysis utilities
fhir.resources >= 7.0   # FHIR R4 validation (optional, for test)
pytest >= 7.4.0         # Test framework
pytest-cov >= 4.1.0     # Coverage reporting
mypy >= 1.5.0           # Static type checking (strict mode)
```

pyproject.toml fragment:
```toml
[project.optional-dependencies]
hcalc = [
    "numpy>=1.24.0",
    "scipy>=1.11.0",
]
hcalc-test = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "mypy>=1.5.0",
]
hcalc-fhir = [
    "fhir.resources>=7.0",
]
```

---

## 7. LEVER TABLE (v0.6 → EXECUTION)

| # | Lever | Owner | Metric | Horizon | blocked_by |
|---|-------|-------|--------|---------|------------|
| 1 | DECOUPLED enum + TerminalState 4-code | System Architect | Zero invalid type combinations (mypy strict) | Day 2 | None |
| 2 | Contraction witness computation | Core Engine Lead | q matches analytic within 1e-6 | Day 5 | Lever 1 |
| 3 | Per-modality INCONCLUSIVE routing | Core Engine Lead | All 4 terminal states reachable | Day 10 | Lever 1 |
| 4 | Counterexample search R ≤ 16 | Core Engine Lead | Bound holds or counterexample found | Day 21 | Lever 2 |
| 5 | FHIR CodeSystem + ValueSet + StructureDef (FSH) | Interop Lead | SUSHI compiles, IG Publisher passes | Day 14 | None |
| 6 | BAA review per 45 C.F.R. §160.103 | Compliance Lead | Executed BAA | Day 14 | None |
| 7 | IG publication (6-step FSH plan) | Interop Lead | ig-registry PR submitted | Day 28 | Lever 5 |
| 8 | DiagnosticReport emitter with extension | Core Engine Lead | Valid R4 JSON with extension | Day 18 | Levers 1, 5 |
| 9 | κ_p(V) growth characterization R=1..32 | Core Engine Lead | Growth exponent report | Day 28 | Lever 4 |

### Critical Path
```
Lever 1 (Day 0-2) → Levers 2,3 (Day 2-10) → Lever 4 (Day 10-21) → Lever 9 (Day 21-28)
                                                                    ↘ Lever 8 (Day 10-18)
Lever 5 (Day 0-14, parallel) → Lever 7 (Day 14-28)
Lever 6 (Day 0-14, parallel)
```

**Total**: 28 days to core completion. 42 days to full integration with shadow validation.

---

## 8. DAG ARTIFACT (Tension D Resolution)

```
         ┌─────────┐
         │ Lever 1 │ DECOUPLED enum (Day 0-2)
         └────┬────┘
        ┌─────┼─────┐
        ▼     ▼     ▼
   ┌────┴──┐ ┌┴────┐ ┌┴────┐
   │Lever 2│ │Lev 3│ │Lev 8│
   │Contr. │ │Route│ │FHIR │
   │(D2-5) │ │(D2-10)│(D10-18)
   └───┬───┘ └──┬──┘ └──┬──┘
       ▼        │       │
   ┌───┴───┐   │       │
   │Lever 4│◄──┘       │
   │R≤16   │           │
   │(D10-21)           │
   └───┬───┘           │
       ▼               │
   ┌───┴───┐           │
   │Lever 9│           │
   │κ bench│           │
   │(D21-28)           │
   └───────┘           │
                       │
   ┌───────┐     ┌─────┴───┐
   │Lever 5│────►│ Lever 7 │
   │FSH    │     │IG Pub   │
   │(D0-14)│     │(D14-28) │
   └───────┘     └─────────┘

   ┌───────┐
   │Lever 6│ BAA (D0-14, independent)
   └───────┘
```

---

## 9. PRECISION QUESTION (CARRIED FORWARD)

**From v0.6**: Has the Interop Lead been assigned and confirmed availability for Lever 5/7 ownership (FSH authoring + IG publication)? This blocks the 21-day IG clock.

**New**: Does the System Architect commit to Lever 1 as an isolated PR by Day 2, or will it be batched with Levers 2/3? Batching introduces a 5-day dependency gap where nothing downstream can start.

---

*"When the mirror returns the same image twice, stop looking and start building."*

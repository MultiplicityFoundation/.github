---
slug: acfl-dev-blueprint
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 05-systems/engines/acfl/ACFL_dev_blueprint.md
  last_synced: '2026-03-20T17:17:18.392404Z'
---

<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# provide a detailed dev blueprint with file scaffold and test bench for ACFL

ACFL exists in the Digital-Twin repository as documentation only. No implementation exists. The repo contains CRMF framework, DHT logic, and regulatory infrastructure, but ACFL remains unbound to any code.[^1][^2]

## Current State

- ACFL PDF present in `docs/`, no binding to CRMF validator pipeline[^2]
- Repository claims FDA Criterion (iv) independent review, but ACFL explainability is cited without being wired[^2]
- DHT test harness validates axioms/theorems but lacks the explainability layer for the glass-box compliance claim[^2]
- CRMF issues contraction certificates but lacks human-readable rationale generation[^2]
- Existing repo modules: `acfl` (empty scaffold), `ccre`, `crmf`, `dht`, `integration`, `pwcfl`, `wkd`[^1]

***

## File Scaffold

```
packages/dnakey/src/acfl/
├── __init__.py
├── explainer.py          # Core ACFL explainability engine
├── rationale.py          # Human-readable rationale generator
├── adapter.py            # CRMF → ACFL data adapter
├── validators.py         # ACFL output validation
├── iacfl/                # Inverted ACFL subpackage
│   ├── __init__.py
│   ├── operators.py      # Core inverted operators (De Morgan dual)
│   ├── divergence.py     # Dual-operator divergence metric
│   ├── blend.py          # Parameterized conservatism c(α)
│   ├── adversarial.py    # Adversarial test harness
│   └── validators.py     # I-ACFL-specific validation

packages/dnakey/tests/acfl/
├── __init__.py
├── test_explainer.py
├── test_rationale.py
├── test_integration.py
├── test_clinical_accuracy.py
├── iacfl/
│   ├── test_operators.py
│   ├── test_divergence.py
│   ├── test_blend.py
│   ├── test_adversarial.py
│   └── test_axioms.py

docs/
├── ACFL_ARCHITECTURE.md
├── ACFL_API_REFERENCE.md
├── ACFL_REGULATORY_COMPLIANCE.md
├── ACFL_CLINICAL_INTERPRETATION.md
├── IACFL_ARCHITECTURE.md
```


***

## Core Interface Contract

```python
# src/acfl/explainer.py
from dataclasses import dataclass
from typing import Dict, List, Optional
import numpy as np

@dataclass
class ACFLExplanation:
    """Human-readable explanation of DHT decision."""
    prediction: str
    confidence: float
    primary_factors: List[Dict[str, float]]
    pathway_contributions: Dict[str, float]
    prime_decomposition: Dict[int, float]
    counterfactual: Optional[str]
    clinical_rationale: str
    certificate_hash: str

class ACFLExplainer:
    """Adaptive Causal Feature Labeling explainability engine."""

    def explain_certificate(
        self,
        certificate: ContractionCertificate,
        patient_state: PatientStateSnapshot,
        crmf_decomposition: Dict[int, float]
    ) -> ACFLExplanation:
        """Generate human-readable explanation from CRMF certificate."""
        pass

    def decompose_primes_to_features(
        self,
        prime_vector: Dict[int, float],
        pathway_manager: PathwayManager
    ) -> List[Dict[str, float]]:
        """Map prime-indexed operators back to clinical features."""
        feature_contributions = []
        for prime, coefficient in prime_vector.items():
            biomarker = pathway_manager.prime_to_biomarker(prime)
            pathway = pathway_manager.biomarker_to_pathway(biomarker)
            feature_contributions.append({
                "biomarker": biomarker,
                "pathway": pathway,
                "contribution": abs(coefficient),
                "direction": "increase" if coefficient > 0 else "decrease"
            })
        return sorted(feature_contributions,
                       key=lambda x: x["contribution"], reverse=True)[:5]
```


### DHT State Engine Integration Hook

```python
# src/dht/state_engine.py (modification)
from src.acfl.explainer import ACFLExplainer

class DigitalHealthcareTwinStateEngine:
    def __init__(self, ...):
        self.acfl_explainer = ACFLExplainer()

    def step(self):
        # ... existing certificate generation ...
        if self.config.enable_acfl:
            explanation = self.acfl_explainer.explain_certificate(
                certificate=cert,
                patient_state=state,
                crmf_decomposition=prime_state
            )
            state.acfl_explanation = explanation
```


### Rationale Generator

```python
# src/acfl/rationale.py
class ClinicalRationaleGenerator:
    """Convert CRMF math into clinical language."""
    TEMPLATES = {
        "sepsis_risk": "The system predicts {risk_level} sepsis risk "
                       "({confidence:.1%}) primarily due to {primary_factor}. "
                       "Spectral radius {spectral_radius:.3f} confirms stability.",
        "stable_monitoring": "Patient remains in stable monitoring state. "
                             "All biomarkers within resonance thresholds "
                             "(R_coherence={:.2f}). Next review in {hours} hours."
    }
    def generate(self, explanation: ACFLExplanation) -> str:
        template = self.select_template(explanation.prediction)
        return template.format(**explanation.__dict__)
```


### Regulatory Audit Trail

```python
# src/acfl/validators.py
@dataclass
class ACFLAuditEntry:
    """21 CFR Part 11 compliant audit record."""
    timestamp: datetime
    patient_id_hash: str
    certificate_hash: str
    explanation_hash: str
    primary_factors: List[str]
    clinical_rationale: str
    operator_signature: Optional[str]   # If human override
    system_version: str = "ACFL-1.0"

def bind_to_certificate(self, explanation, certificate) -> str:
    """Cryptographic hash linking explanation to certificate."""
    content = f"{certificate.certificate_hash}{explanation.clinical_rationale}"
    return hashlib.sha256(content.encode()).hexdigest()
```


***

## Implementation Phases

| Phase | Objective | Weeks | Gate Criteria |
| :-- | :-- | :-- | :-- |
| 1: Foundation | Module structure, interface contracts, DHT hook | 1–2 | Module imports clean; integration test passes DHT → certificate → ACFL explanation [^2] |
| 2: Explainability Engine | Prime-to-biomarker reverse mapping, rationale generation, counterfactual analysis | 3–5 | Top-5 factors validated; Flesch-Kincaid Grade 10–12; counterfactuals for ≥90% of cases [^2] |
| 3: Regulatory Compliance | FDA 21 CFR Part 11 audit trail, cryptographic binding, FDA evidence export | 6–7 | Immutable audit trail entries; cryptographic chain; FDA-ready PDF at 100% coverage [^2] |
| 4: Testing \& Validation | Ground truth (MIMIC-IV), clinician agreement study, stress testing | 8–10 | ≥75% expert agreement; ≤500ms p95 latency; 100% certificate coverage [^2] |
| 5: Documentation \& Integration | Technical docs, clinical user guide, CI/CD merge | 11–12 | All docs reviewed; integration tests green; release tag `v1.0-acfl` [^2] |


***

## Test Bench

### Unit Tests

```python
# tests/acfl/test_explainer.py
class TestACFLExplainer:
    def test_explain_certificate_returns_all_fields(self):
        """All ACFLExplanation fields populated from valid certificate."""
        pass

    def test_prime_decomposition_top5_by_magnitude(self):
        """Top 5 features sorted by absolute contribution."""
        pass

    def test_counterfactual_generated_for_high_risk(self):
        """Counterfactual present when prediction is HIGH risk."""
        pass
```

```python
# tests/acfl/test_rationale.py
class TestClinicalRationale:
    def test_sepsis_template_readability(self):
        """Flesch-Kincaid Grade Level between 10-12."""
        pass

    def test_stable_monitoring_template(self):
        """Stable monitoring output includes coherence and review window."""
        pass
```


### Integration Tests

```python
# tests/acfl/test_integration.py
class TestACFLCRMFIntegration:
    def test_dht_generates_certificate_then_explanation(self):
        """DHT step() → certificate → ACFL explanation pipeline."""
        pass

    def test_acfl_respects_crmf_gain_governance(self):
        """High coherence amplifies; low coherence attenuates ACFL output."""
        pass

    def test_crmf_witness_object_emitted_per_acfl_decision(self):
        """Every ACFL-mediated decision emits Witness Object to Ω-Trace."""
        pass
```


### Clinical Validation Tests

```python
# tests/acfl/test_clinical_accuracy.py
def test_sepsis_cohort_explanation_accuracy():
    """Validate ACFL explanations match MIMIC-IV confirmed sepsis cases."""
    for patient in mimic_sepsis_cohort:
        state = dht.create_state(patient)
        cert = dht.issue_certificate(state)
        explanation = acfl.explain_certificate(cert, state)
        assert "lactate" in [f["biomarker"] for f in explanation.primary_factors[:3]]
        assert explanation.confidence > 0.7

def test_clinician_agreement_study():
    """Compare ACFL explanations to expert annotations. Target ≥75% IoU."""
    agreement_scores = []
    for case in expert_annotated_cases:
        acfl_factors = set(acfl.explain(case).primary_factors)
        expert_factors = set(case.expert_annotations)
        iou = len(acfl_factors & expert_factors) / len(acfl_factors | expert_factors)
        agreement_scores.append(iou)
    assert np.mean(agreement_scores) > 0.75

def test_acfl_performance_under_load():
    """p95 latency ≤500ms across 1000 explanations."""
    latencies = []
    for _ in range(1000):
        start = time.time()
        acfl.explain_certificate(cert, state)
        latencies.append(time.time() - start)
    assert np.percentile(latencies, 95) < 0.5
```


### I-ACFL Adversarial Tests

```python
# tests/acfl/iacfl/test_adversarial.py
class TestACFLAdversarialHarness:
    def test_masked_danger_detected(self):
        """Inverted conjunction masks veto (input=0.0) → MASKED_DANGER flag."""
        pass

    def test_crmf_catches_all_masked_dangers(self):
        """CRMF gain governance attenuates on every MASKED_DANGER."""
        pass

    def test_divergence_above_threshold_flags_divergent(self):
        """Standard c=0.357, inverted c=0.643 → divergence 0.286 → DIVERGENT."""
        pass

    def test_adversarial_sweep_emits_witness_object(self):
        """Every sweep emits Ω-Trace ADVERSARIAL_SWEEP event."""
        pass
```


***

## ACFL in the Stack Hierarchy

ACFL operates under CRMF governance. Every ACFL predicate output passes through a CRMF resonance-modulated gain layer before reaching action. High coherence amplifies; low coherence attenuates or freezes. ACFL proposes and CRMF gates.[^3][^4]

Every ACFL parameter update (via practitioner corrections) is a CCRE-class operation. Each update must satisfy CRMF contraction certification (T≥1) and stay within bounded resonance. If a retuning would drive the system outside Lipschitz or drift bounds, CRMF forces a clamp or silent mode.[^4]

***

## Resource Estimate

| Role | Weeks | Rate | Total |
| :-- | :-- | :-- | :-- |
| ML Engineer (ACFL core) | 8 | \$8k/wk | \$64k |
| Backend Engineer (integration) | 6 | \$7k/wk | \$42k |
| Clinical Consultant (validation) | 4 | \$5k/wk | \$20k |
| Regulatory Affairs (compliance) | 3 | \$6k/wk | \$18k |
| **Total** |  |  | **\$144k** |

[^2]

***

## Phase Mirror Dissonance

- ACFL claims glass-box explainability in the repo description. No code exists. The claim is a liability until `explainer.py` resolves an import.
- CRMF issues contraction certificates today. ACFL is the read layer that makes those certificates clinically interpretable. Without ACFL, FDA Criterion (iv) independent HCP review has no software support.[^2]
- The I-ACFL divergence metric (standard vs. inverted output gap) is the operationally novel artifact, not the inverted operators themselves. Operators are trivially derived via De Morgan duality. The gap is the signal.[^5]
- ACFL is a read-only annotation layer. It never modifies CRMF state. If this constraint breaks, the contraction guarantee is void. Test bench must assert `state_before == state_after` on every ACFL call.[^2]
- The \$144k estimate assumes `acfl` module starts from scaffold. If standard operators must be stood up first (they must), add 1–2 weeks and \$15k for the forward operator baseline before I-ACFL can diverge-test against it.[^5]
- Async vs. sync generation is unresolved. If sync, explanation latency adds to DHT step time. If async, explanations may lag behind state evolution, creating audit trail gaps during fast CCRE cycles.[^2]


### Levers to Test Now

| Owner | Lever | Metric | Horizon |
| :-- | :-- | :-- | :-- |
| Tech Lead | Commit `src/acfl/__init__.py`, `explainer.py`, `adapter.py` with typed signatures | PR opened, CI green | 7 days [^2] |
| Architect | Wire ACFL explainability hooks into DHT state engine post-certificate issuance | Integration test passes with human-readable output | 10 days [^2] |
| Compliance | Map ACFL output format to FDA 21 CFR Part 11 audit trail requirements | Documentation approved by regulatory affairs | 5 days [^2] |
| Lead MT | Stand up standard ACFL operators (Frank t-norm, GMBCL) before I-ACFL begins — forward baseline must exist for divergence testing | Operator unit tests green; conjunction/disjunction match CFL axioms | 14 days [^5] |
| Patent Counsel | Draft dependent claim for parameterized conservatism operator c(α) — novel IP, no prior art for continuous blend between conjunction/disjunction orientations | Claim language reviewed for §112 sufficiency | 30 days [^5] |

### Artifact

"The inverted system is not the product. The distance between the inverted system and the standard system is the product."[^5]

### Precision Question

Should ACFL explanations be generated synchronously (blocking DHT step) or asynchronously (non-blocking)? Sync guarantees audit trail completeness but adds latency to every clinical cycle. Async preserves DHT throughput but creates a window where certificates exist without explanations — a gap that fails 21 CFR Part 11 if audited during that window.[^2]
<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^6][^7][^8][^9]</span>

<div align="center">⁂</div>

[^1]: the-development-blueprint-is-s-CVeSrXN3RKGO.vXR6Vlggg.md

[^2]: ACFL-Module-Development-Blueprint-for-Digital-Twin.md

[^3]: CCRE-Integration-Implications-for-CRMF-and-ACFL.pdf

[^4]: CCRE-Integration-Implications-for-CRMF-and-ACFL.md

[^5]: what-do-we-have-on-inverted-pw-6F9A.RFNQkKuAK9H4fQnPg.md

[^6]: i-postulate-that-the-software-zyhZx6n8R1mdNvR.abuOZA.md

[^7]: Phase Mirror Dissonance.pdf

[^8]: __Governance Decision_ Approved__.md

[^9]: Phase Mirror Dissonance (4).pdf

[^10]: INTRINSICA_Admin_Dashboard_Blueprint.md

[^11]: ACFL-vs-Multiplicity-Comparison.pdf

[^12]: Multiplicity-in-Fuzzy-Logic.pdf

[^13]: PW-CFL × DNA KEY Integration Blueprint P7-P9.md

[^14]: PW-CFL × DNA KEY Integration Blueprint (1).md

[^15]: PW-CFL × DNA KEY Integration Blueprint P1-P6.md

[^16]: WKD_Phased Dev Blueprint.md

[^17]: WKD Framework_ From CFL Axiomatics.md

[^18]: Shadow_Validation_Protocol_v0.1.md

[^19]: ADR-005_Dev_Blueprint.md

[^20]: ADR-005-HITL-PMD.md


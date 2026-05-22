---
slug: lets-create-a-phased-plan-and-blueprint-for-acfl-i
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 05-systems/engines/acfl/Lets create a phased plan and blueprint for ACFL i.md
  last_synced: '2026-03-20T17:17:18.395636Z'
---

<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Lets create a phased plan and blueprint for ACFL including detailed instructions, file scaffolding, and test harness.

ACFL currently exists as documentation only in the Digital-Twin repository — no implementation code is bound. Below is the consolidated phased plan, file scaffold, and test harness, incorporating the existing blueprints and resolving the open tensions surfaced by prior PMD audits.[^1][^2]

***

## Phase Mirror Dissonance

- Glass-box explainability is claimed in the repo description. No code backs it. The claim is a liability until `explainer.py` resolves an import.[^2]
- CRMF issues contraction certificates today. ACFL is the read layer that makes those certificates clinically interpretable. Without it, FDA Criterion iv (independent HCP review) has no software support.[^1]
- The I-ACFL divergence metric (standard vs. inverted output gap) is the operationally novel artifact, not the inverted operators themselves. Operators are trivially derived via De Morgan duality. The gap is the signal.[^3]
- ACFL is a read-only annotation layer. It must never modify CRMF state. If this constraint breaks, the contraction guarantee is void.[^4]
- Async vs. sync generation is unresolved. Sync guarantees audit trail completeness but adds latency. Async preserves DHT throughput but creates a window where certificates exist without explanations — a gap that fails 21 CFR Part 11 if audited during that window.[^2]
- The 144k resource estimate assumes the `acfl/` module starts from scaffold. If standard operators must be stood up first (they must), add 1–2 weeks and ~15k for the forward operator baseline before I-ACFL can diverge-test against it.[^1]
- Archimedean t-norm claims are generic in the patent. The specification must lock down which t-norm (product, Lukasiewicz, Frank family), with exact formulas and boundary values, to survive 112 enablement challenges.[^5]
- ACFL operates under CRMF governance. Every predicate output passes through a CRMF resonance-modulated gain layer before reaching action. ACFL proposes; CRMF gates.[^4]

***

## File Scaffold

```
packages/dna-key/src/acfl/
├── __init__.py
├── explainer.py            # Core ACFLExplainer class
├── rationale.py            # ClinicalRationaleGenerator
├── adapter.py              # CRMF → ACFL data adapter
├── validators.py           # ACFLAuditEntry + 21 CFR Part 11 binding
├── operators.py            # Frank t-norm, GMBCL standard operators
├── membership.py           # Membership functions per biosensor type
├── counterfactual.py       # Counterfactual analysis engine
├── iacfl/
│   ├── __init__.py
│   ├── operators.py        # De Morgan dual / inverted operators
│   ├── divergence.py       # Dual-operator divergence metric
│   ├── blend.py            # Parameterized conservatism (c)
│   ├── adversarial.py      # Adversarial sweep harness
│   └── validators.py       # I-ACFL-specific validation

packages/dna-key/tests/acfl/
├── __init__.py
├── test_explainer.py
├── test_rationale.py
├── test_integration.py
├── test_clinical_accuracy.py
├── test_operators.py
├── test_membership.py
├── iacfl/
│   ├── test_operators.py
│   ├── test_divergence.py
│   ├── test_blend.py
│   ├── test_adversarial.py
│   └── test_axioms.py

docs/
├── ACFL-ARCHITECTURE.md
├── ACFL-API-REFERENCE.md
├── ACFL-REGULATORY-COMPLIANCE.md
├── ACFL-CLINICAL-INTERPRETATION.md
├── IACFL-ARCHITECTURE.md
```


***

## Phase 1 — Foundation (Weeks 1–2)

**Objective:** Establish module structure, interface contracts, and DHT integration hook.

**Deliverables:**

1. **`explainer.py` — Core Interface Contract**[^2]
```python
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
        certificate: "ContractionCertificate",
        patient_state: "PatientStateSnapshot",
        crmf_decomposition: Dict[int, float]
    ) -> ACFLExplanation:
        """Generate human-readable explanation from CRMF certificate."""
        ...
```

2. **`adapter.py` — CRMF→ACFL Data Adapter**[^4]
```python
class CRMFAdapter:
    """Translates CRMF certificate + prime state into ACFL input format."""

    def extract_prime_vector(self, certificate) -> Dict[int, float]: ...
    def extract_resonance_status(self, certificate) -> float: ...
    def apply_gain_governance(self, acfl_output, coherence: float) -> float:
        """High coherence amplifies; low coherence attenuates or freezes."""
        ...
```

3. **DHT State Engine Integration Hook**[^2]
```python
# src/dht/state_engine.py modification
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

**Gate Criteria:**

- `acfl/` module imports without errors
- Integration test passes: DHT generates certificate → ACFL explanation
- Output includes all required fields per FDA 21 CFR Part 11[^1]

***

## Phase 2 — Explainability Engine (Weeks 3–5)

**Objective:** Implement core ACFL algorithm: prime-to-biomarker reverse mapping, rationale generation, counterfactual analysis.

**Deliverables:**

1. **`operators.py` — Standard ACFL Operators**[^6]
```python
import math

def frank_t_norm(a: float, b: float, s: float = 2.0) -> float:
    """Frank family t-norm: T_s(a,b) = log_s(1 + (s^a - 1)(s^b - 1)/(s - 1))"""
    if s == 1.0:
        return a * b  # product t-norm limit
    return math.log(1 + ((s**a - 1) * (s**b - 1)) / (s - 1), s)

def gmbcl_conjunction(values: list, weights: list = None) -> float:
    """Geometric Mean Based Compensatory Logic conjunction."""
    n = len(values)
    if any(v == 0 for v in values):
        return 0.0  # veto axiom
    if weights is None:
        weights = [1/n] * n
    return math.prod(v**w for v, w in zip(values, weights))
```

2. **`membership.py` — Biosensor Membership Functions**[^5]
```python
def hrv_membership(x: float) -> Dict[str, float]:
    """HRV membership: CRITICALLY-LOW → CRITICALLY-HIGH"""
    return {
        "CRITICALLY_LOW": max(0, min(1, (30 - x) / 10)),
        "LOW":            trapezoidal(x, 20, 30, 40, 50),
        "MODERATE":       trapezoidal(x, 40, 50, 60, 70),
        "HIGH":           trapezoidal(x, 60, 70, 80, 90),
        "CRITICALLY_HIGH": max(0, min(1, (x - 80) / 10)),
    }
# Repeat for: bioimpedance_membership, spo2_membership,
# skin_temp_membership, ppg_membership, acceleration_membership
```

3. **`rationale.py` — Clinical Rationale Generator**[^2]
```python
class ClinicalRationaleGenerator:
    TEMPLATES = {
        "sepsis_risk": "The system predicts {risk_level} sepsis risk "
                       "({confidence:.1%}) primarily due to {primary_factor}. "
                       "Spectral radius {spectral_radius:.3f} confirms stability.",
        "stable_monitoring": "Patient remains in stable monitoring state. "
                             "All biomarkers within resonance thresholds "
                             "(R_coherence={coherence:.2f}). "
                             "Next review in {hours} hours.",
    }
```

4. **`counterfactual.py`** — "What would need to change to alter the prediction?"[^1]

**Gate Criteria:**

- Top-5 contributing features identified correctly (validated against manual review)
- Clinical rationale passes readability test: Flesch-Kincaid Grade 10–12
- Counterfactual scenarios generated for ≥90% of cases[^2]

***

## Phase 3 — I-ACFL + Adversarial Harness (Weeks 6–7)

**Objective:** Stand up Inverted ACFL operators and the divergence metric that is the operationally novel artifact.[^3]

**Deliverables:**

1. **`iacfl/operators.py` — De Morgan Dual Operators**
```python
def inverted_conjunction(values: list, weights: list = None) -> float:
    """De Morgan dual: NOT(AND(NOT(x_1), ..., NOT(x_n)))"""
    negated = [1.0 - v for v in values]
    return 1.0 - gmbcl_conjunction(negated, weights)
```

2. **`iacfl/divergence.py` — Divergence Metric**
```python
def acfl_divergence(standard_output: float, inverted_output: float) -> float:
    """The distance between standard and inverted is the product."""
    return abs(standard_output - inverted_output)

def classify_divergence(d: float, threshold: float = 0.2) -> str:
    return "DIVERGENT" if d > threshold else "CONCORDANT"
```

3. **`iacfl/blend.py` — Parameterized Conservatism**
```python
def blended_output(standard: float, inverted: float, c: float = 0.5) -> float:
    """c=0 → pure standard, c=1 → pure inverted."""
    return (1 - c) * standard + c * inverted
```

4. **`iacfl/adversarial.py` — Adversarial Sweep Harness**[^1]
```python
class AdversarialSweep:
    def sweep(self, input_space, n_samples=10000):
        """Sweep parameter space, flag MASKED_DANGER and DIVERGENT cases."""
        for sample in self.generate_samples(input_space, n_samples):
            std = gmbcl_conjunction(sample)
            inv = inverted_conjunction(sample)
            div = acfl_divergence(std, inv)
            if std == 0.0 and inv > 0.0:
                yield {"type": "MASKED_DANGER", "sample": sample, "div": div}
            elif div > self.threshold:
                yield {"type": "DIVERGENT", "sample": sample, "div": div}
```

**Gate Criteria:**

- Standard operators pass CFL axiom tests (veto, monotonicity, De Morgan duality)
- Divergence metric: standard (c=0.357), inverted (c=0.643) → divergence=0.286 flagged as DIVERGENT[^3]
- Every adversarial sweep emits a Λ-Trace `ADVERSARIAL_SWEEP` event[^1]

***

## Phase 4 — Regulatory Compliance + Validation (Weeks 8–10)

**Objective:** Satisfy FDA 21 CFR Part 11 audit trail requirements and validate clinical utility.

**Deliverables:**

1. **`validators.py` — Audit Trail + Cryptographic Binding**[^2]
```python
@dataclass
class ACFLAuditEntry:
    """21 CFR Part 11 compliant audit record."""
    timestamp: datetime
    patient_id_hash: str
    certificate_hash: str
    explanation_hash: str
    primary_factors: List[str]
    clinical_rationale: str
    operator_signature: Optional[str]  # If human override
    system_version: str = "ACFL-1.0"

def bind_to_certificate(explanation, certificate) -> str:
    content = f"{certificate.certificate_hash}{explanation.clinical_rationale}"
    return hashlib.sha256(content.encode()).hexdigest()
```

2. **FDA Evidence Export** — generates FDA 510(k) evidence bundle per cohort[^1]
3. **CRMF Gain Governance Integration** — every ACFL output passes through resonance-modulated gain layer; high coherence amplifies, low coherence attenuates or freezes[^4]

**Gate Criteria:**

- All ACFL explanations have immutable audit trail entries
- Cryptographic chain links: ACFL → Certificate → Patient State
- Export generates FDA-ready PDF with 100% coverage[^2]

***

## Phase 5 — Testing + Documentation (Weeks 11–14)

**Objective:** Clinical validation, performance stress test, documentation, merge to main.

### Test Harness

| Test Class | File | Assertion | Target |
| :-- | :-- | :-- | :-- |
| Sepsis cohort accuracy | `test_clinical_accuracy.py` | `lactate` in top-3 factors for MIMIC-IV sepsis cases | confidence > 0.7 [^1] |
| Clinician agreement | `test_clinical_accuracy.py` | IoU between ACFL factors and expert annotations | mean ≥ 0.75 [^2] |
| Performance under load | `test_clinical_accuracy.py` | p95 latency across 1000 explanations | ≤ 500ms [^1] |
| ACFL read-only invariant | `test_integration.py` | `state_before == state_after` on every ACFL call | 100% [^1] |
| CRMF gain governance | `test_integration.py` | High coherence amplifies, low coherence attenuates | pass/fail [^4] |
| Witness Object emission | `test_integration.py` | Every ACFL-mediated decision emits Witness Object to Λ-Trace | 100% [^1] |
| Masked danger detection | `iacfl/test_adversarial.py` | Inverted conjunction masks veto → `MASKED_DANGER` flag | detected [^1] |
| CRMF catches masked dangers | `iacfl/test_adversarial.py` | CRMF gain governance attenuates on every `MASKED_DANGER` | 100% [^1] |
| Divergence threshold | `iacfl/test_divergence.py` | Divergence > 0.2 → `DIVERGENT` flag | classified [^3] |
| CFL axiom compliance | `iacfl/test_axioms.py` | Veto (Axiom iv), monotonicity (iii), De Morgan (vii) | pass [^6] |

### Key Test Code

```python
# tests/acfl/test_clinical_accuracy.py
def test_sepsis_cohort_explanation_accuracy():
    for patient in mimic_sepsis_cohort:
        state = dht.create_state(patient)
        cert = dht.issue_certificate(state)
        explanation = acfl.explain_certificate(cert, state)
        assert "lactate" in [f["biomarker"] for f in explanation.primary_factors[:3]]
        assert explanation.confidence > 0.7

def test_clinician_agreement_study():
    scores = []
    for case in expert_annotated_cases:
        acfl_factors = set(acfl.explain(case).primary_factors)
        expert_factors = set(case.expert_annotations)
        iou = len(acfl_factors & expert_factors) / len(acfl_factors | expert_factors)
        scores.append(iou)
    assert np.mean(scores) >= 0.75

def test_acfl_performance_under_load():
    latencies = []
    for _ in range(1000):
        start = time.time()
        acfl.explain_certificate(cert, state)
        latencies.append(time.time() - start)
    assert np.percentile(latencies, 95) <= 0.5
```


***

## Levers to Test Now

| Owner | Lever | Metric | Horizon |
| :-- | :-- | :-- | :-- |
| Tech Lead | Commit `src/acfl/__init__.py`, `explainer.py`, `adapter.py` with typed signatures | PR opened, CI green | 7 days [^1] |
| Architect | Wire ACFL explainability hooks into DHT state engine post-certificate issuance | Integration test passes with human-readable output | 10 days [^2] |
| Compliance | Map ACFL output format to FDA 21 CFR Part 11 audit trail requirements | Documentation approved by regulatory affairs | 5 days [^1] |
| Lead MT | Stand up standard ACFL operators (Frank t-norm, GMBCL) before I-ACFL begins | Operator unit tests green; conjunction/disjunction match CFL axioms | 14 days [^3] |
| Patent Counsel | Draft dependent claim for parameterized conservatism operator (c) | Claim language reviewed for 112 sufficiency | 30 days [^3] |
| Architect | Resolve async vs. sync explanation generation | ADR drafted with latency/audit-gap tradeoff quantified | 7 days [^2] |


***

## Resource Estimate

| Role | Weeks | Rate | Total |
| :-- | :-- | :-- | :-- |
| ML Engineer (ACFL core) | 8 | \$8k/wk | \$64k |
| Backend Engineer (integration) | 6 | \$7k/wk | \$42k |
| Clinical Consultant (validation) | 4 | \$5k/wk | \$20k |
| Regulatory Affairs (compliance) | 3 | \$6k/wk | \$18k |
| **Total** |  |  | **\$144k** |

Add 1–2 weeks and ~\$15k if standard operators must be stood up before I-ACFL can diverge-test against them (they must).[^1]

***

## Artifact

"The inverted system is not the product. The distance between the inverted system and the standard system is the product."[^3]

## Precision Question

Which t-norm locks into the patent specification — product $T(a,b) = ab$, Frank family $T_s$ at a specific $s$, or Lukasiewicz $T(a,b) = \max(0, a+b-1)$? The answer determines `operators.py` implementation, membership function boundary behavior, and whether the 112 enablement challenge from the adversarial stress test is neutralized.[^5]
<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^17][^18][^19][^20][^21][^22][^23][^24][^25][^26][^27][^28][^29][^30][^31][^32][^33][^34][^35][^36][^37][^38][^39][^40][^41][^42][^43][^44][^45][^46][^47][^48][^49][^50][^7][^8][^9]</span>

<div align="center">⁂</div>

[^1]: provide-a-detailed-dev-bluepri-WU70byH7Sl6o5qMe2vM5dQ.md

[^2]: ACFL-Module-Development-Blueprint-for-Digital-Twin.md

[^3]: what-do-we-have-on-inverted-pw-6F9A.RFNQkKuAK9H4fQnPg.md

[^4]: CCRE-Integration-Implications-for-CRMF-and-ACFL.pdf

[^5]: ACFL-EXPLAINABLE-AI-SYSTEM.pdf

[^6]: ACFL-vs-Multiplicity-Comparison.pdf

[^7]: lets-create-a-phased-plan-and-hzWrMKHRTh.WyowS20gAJw.md

[^8]: a-self-contained-module-that-f-ShviRtO2RZuJBFQflFlKSQ.md

[^9]: here-is-the-concrete-execution-KlxRcA0QQtWx9aeaDm8dMw.md

[^10]: ΛProof_ A Technical Whitepaper on Prime-Lawful, Verifiable Systems.pdf

[^11]: ΛProof Certification Program Specification.pdf

[^12]: Λ-Constitution.pdf

[^13]: ΛProof Project for Artificial Intelligence.pdf

[^14]: ΛProof_ An Architectural Blueprint for Verifiable Artificial Intelligence.pdf

[^15]: ΛProof Protocols.pdf

[^16]: ΛProof Intent Schema Specification.pdf

[^17]: ΛProof Security Test Suite Specification.pdf

[^18]: Ξ-Constitution.pdf

[^19]: ΛProof_ Zero-Knowledge Systems for  Verifiable Computing.pdf

[^20]: i-postulate-that-the-software-zyhZx6n8R1mdNvR.abuOZA.md

[^21]: the-development-blueprint-is-s-CVeSrXN3RKGO.vXR6Vlggg.md

[^22]: Phase Mirror Dissonance.pdf

[^23]: __Governance Decision_ Approved__.md

[^24]: https://github.com/OpenFactoryTwin/ofact

[^25]: https://github.com/caltech-netlab/digital-twin-dataset

[^26]: https://github.com/orgs/digitaltwinconsortium/repositories

[^27]: https://github.com/TUMFTM/edgar_digital_twin

[^28]: https://github.com/oneapi-src/digital-twin

[^29]: https://github.com/stoa-xh91/ACFL

[^30]: https://github.com/realsanjeev/Air-conditioner-controller-recommendation-using-fuzzy-logic

[^31]: https://github.com/topics/digital-twin

[^32]: https://github.com/CopilotKit/CopilotKit

[^33]: https://github.com/holgern/sciflt

[^34]: https://github.com/Digital-Twin-Operational-Platform/Cristallo

[^35]: https://github.com/leerob

[^36]: https://github.com/gregory-chatelier/fuzzy-logic

[^37]: https://github.com/mmmmaria/Digital-twin

[^38]: https://github.com/abhiagwl

[^39]: https://www.digitaltwinconsortium.org/initiatives/open-source/

[^40]: https://dtw.twinbase.org

[^41]: https://github.com/programming-digital-twins/pdt-cfw-components

[^42]: https://pmc.ncbi.nlm.nih.gov/articles/PMC5880239/

[^43]: https://ri.conicet.gov.ar/bitstream/handle/11336/64926/CONICET_Digital_Nro.3d5c9377-a109-4439-90a8-dab6a8e8eacb_A.pdf?sequence=2\&isAllowed=y

[^44]: https://www.biorxiv.org/content/10.64898/2025.12.28.696672v1

[^45]: https://www.atlantis-press.com/journals/ijcis/25868673

[^46]: https://autotwin.github.io

[^47]: https://pubmed.ncbi.nlm.nih.gov/29500235/

[^48]: https://www.semanticscholar.org/paper/Archimedean-Compensatory-Fuzzy-Logic-as-a-Pluralist-Espín-Andrade-Cruz-Reyes/6038ce089b87187a97236a2e7f03f1f89396960c

[^49]: https://modeling-digital-twin.github.io/downloads/

[^50]: https://www.nature.com/articles/s41598-023-47462-5


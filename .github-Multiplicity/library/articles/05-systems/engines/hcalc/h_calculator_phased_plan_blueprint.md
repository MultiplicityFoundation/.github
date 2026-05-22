---
slug: h-calculator-phased-plan-blueprint
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 05-systems/engines/hcalc/h_calculator_phased_plan_blueprint.md
  last_synced: '2026-03-20T17:17:18.273534Z'
---

H-Calculator: Phased
Development Plan, File Scaffold
& Test Bench
Version 0.6 — Post-PMD Convergence
Execution Blueprint
Document ID: DEV-HCALC-001
Parent Artifacts: SVP-001-v0.1, ADR-005 Dev Blueprint (DEV-SVP-
001), H-Calculator PMD v0.6
Status: EXECUTION READY
Date: February 21, 2026
Author: Lead Multiplicity Theorist
Repo Target: CHL987/Intrinsica monorepo
Classification: Confidential Engineering Work Product


1. Architecture Overview
The H-Calculator is the convergence-terminal computation engine
within the DNA KEY / INTRINSICA pipeline. It consumes multi-
modality health data (vitals, imaging, genomics, text), applies the
CRMF axiomatic contraction framework, and outputs a ranked
diagnostic differential with a terminal convergence state.[1][2]

1.1 Terminal States (Enum)
  Code     Display    FHIR Mapping          Trigger Condition
 CONV                 DiagnosticRepo     Top-k concentration ≥
          Conver
 ERGE                 rt.status =        60%, contraction witness
          ged
 D                    'final'            q < 1−ε
 INCO                 DiagnosticRepo     Classifier confidence <
          Inconcl
 NCLU                 rt.status =        0.9, or insufficient
          usive
 SIVE                 'partial'          modality data
          Freeze-     DiagnosticRepo     Contraction failure (K ≥
 FREE
          Resona      rt.status =        1), drift > 0.3, or
 ZE
          nce         'registered'       resonance exit
          Decoupl     DiagnosticRepo     M modalities fail joint
 DECO
          ed          rt.status =        convergence; per-
 UPLE
          Modalit     'partial' +        modality results valid
 D
          ies         extension          independently

The 4-code enum resolves the v0.4 INCONCLUSIVE gap identified in
PMD. The DECOUPLED code was the key v0.5 addition, enabling per-
modality fallback when joint convergence fails. FHIR status mappings
use the R4 diagnostic-report-status ValueSet.[2][3][4]

1.2 FHIR Extension
    CodeSystem: intrinsica-convergence-terminal (4 codes)
    ValueSet: Required binding to CodeSystem
    StructureDefinition: Extension on DiagnosticReport at
    DiagnosticReport.extension
    Canonical URL: https://intrinsica.health/fhir/convergence-
    terminal
    Encoding: CodeableConcept per FHIR required binding guidance
    (not raw string)
FSH (FHIR Shorthand) is used for all conformance resources,
compiled via SUSHI. This aligns with the broader INTRINSICA
platform's FHIR R4 architecture.[5][6][7]
1.3 Core Computation Flow

  Ring Sensor Data → Modality Tensor Assembly → Per-Modality Contraction
    → Joint Convergence Test → Terminal State Classification
    → FHIR DiagnosticReport Emission → Ω-Trace Audit


The flow follows the CSP loop and Ω-Trace atoms defined in the
LProof architecture. The pipeline wires into the existing CCRE and
ACFL modules.[8][9][1]

1.4 Key Constraints
     R_max = 16 (runtime cap, Phase 2); R_max = 32 proof deferred to
     Phase 3
     UI modality cap M ≤ 6 (card view); M > 6 (summary table with
     expand-on-click)
     Bauer-Fike spectral bound:                           [10]
     Top-3 diagnosis concentration ≥ 60% probability mass for
     CONVERGED terminal


2. Phased Plan
Phase 1: Core Engine (Days 0–14)
Objective: Build the convergence-terminal computation core with
enum, contraction witness, and per-modality routing.
 Da
                  Deliverable              Owner          Gate
  y
         types.py, config.py, enums.py
 0–                                       System
         — all data structures and                     CI green
 2                                        Architect
         constants
         contraction.py — contraction     Core
 2–                                                    Unit tests
         witness computation (q = τ · m   Engine
 5                                                     pass
         / LT)                            Lead
         modality_tensor.py — per-
                                          Core         Tensor
 3–      modality Hilbert space
                                          Engine       fixtures
 7       assembly with sparsity
                                          Lead         valid
         constraint
         convergence.py — joint                        All 4
                                          Core
 5–      convergence test, DECOUPLED                   terminal
                                          Engine
 10      routing, INCONCLUSIVE                         states
                                          Lead
         fallback                                      reachable
         ranking.py — ranked              Core         Concentrati
 7–
         differential with top-k          Engine       on ≥ 60%
 12
         concentration threshold          Lead         verified
                                          Lead         95%
 10      terminal_classifier.py —
                                          Multiplici   accuracy
 –       terminal state classification
                                          ty           on
 14      with confidence scoring
                                          Theorist     synthetic

Phase 1 Exit Criteria:

      All 4 terminal states reachable from synthetic input
      Contraction witness q computation matches analytic expectation
      within 1e-6
      Zero invalid enum combinations at compile time (mypy strict)
      Per-modality INCONCLUSIVE routes correctly under
      DECOUPLED
This phase resolves PMD Lever 1 (DECOUPLED enum) and Levers 2-3
(contraction + routing).[11][2]
Phase 2: FHIR Integration (Days 7–28)
Objective: Implement FHIR R4 DiagnosticReport emission with
convergence-terminal extension, ValueSet binding, and IG scaffold.

  Da
                   Deliverable                 Owner        Gate
   y
 7–      fhir/codesystem.fsh — 4-code          Interop   SUSHI
 10      CodeSystem in FSH                     Lead      compiles
 8–      fhir/valueset.fsh — Required          Interop   Validates
 12      binding ValueSet                      Lead      against R4
                                                         IG
 10–     fhir/structuredefinition.fsh —        Interop
                                                         Publisher
 14      Extension StructureDefinition         Lead
                                                         passes
         fhir_emitter.py —                     Core      Valid R4
 12–
         DiagnosticReport builder with         Engine    JSON
 18
         extension injection                   Lead      output
 14–     fhir/ig/ — Full IG scaffold (sushi-   Interop   IG builds
 21      config.yaml, narrative pages)         Lead      locally
 21–     IG narrative + ig-registry PR         Interop   Review-
 28      preparation                           Lead      ready

Phase 2 Exit Criteria:

      SUSHI compiles all FSH without errors[6]
      IG Publisher generates valid HTML with all 4 codes documented
      DiagnosticReport with status='partial' and convergence-terminal
      extension validates against R4[4]
      BAA review executed per 45 C.F.R. §160.103
This phase resolves PMD Levers 5, 6, and 7 (FSH, BAA, IG publication).
[12]
Phase 3: Spectral Scaling & R_max (Days 14–35)
Objective: Validate Bauer-Fike bound extension from R=16 to R=32,
implement runtime cap with logging.

 Da
                  Deliverable                Owner           Gate
  y
 14      spectral.py — κ_p(V)               Core         Matches
 –       computation for modality           Engine       NumPy
 18      eigenvector matrices               Lead         reference
         rmax_guard.py — Runtime
 16                                         Core         Cap fires
         R_max=16 cap with
 –                                          Engine       correctly at
         DECOUPLED fallback and
 21                                         Lead         R=17
         logging
                                                         Growth
 21      spectral_bench.py —                Core
                                                         characteriz
 –       Benchmark κ_p(V) growth            Engine
                                                         ation
 28      from R=1..32                       Lead
                                                         report
         Decision gate: polynomial          Lead
 28                                                      Written
         growth → proof extension           Multiplici
 –                                                       decision
         viable; exponential →              ty
 35                                                      document
         alternative bound                  Theorist

Phase 3 Exit Criteria:

      Runtime cap at R_max=16 fires correctly, logs to Ω-Trace, emits
      DECOUPLED
      κ_p(V) growth characterization complete for R=1..32
      Decision document on Phase 4 proof strategy signed
This phase addresses PMD Tension E (R_max=32 horizon gap) and
Lever 4 (counterexample search).[10][2]
Phase 4: UI & Clinician Interface (Days 21–42)
Objective: Implement clinician-facing modality card rendering with
M ≤ 6 threshold and summary fallback.

 Da                                                Ow
                      Deliverable                             Gate
  y                                                ner
 21      ui/modality_card.py — Per-modality        UI
                                                           Renders
 –       card component (convergence state,        Lea
                                                           for M=1..6
 25      confidence, key metrics)                  d
 25                                                UI
         ui/summary_table.py — Summary                     Renders
 –                                                 Lea
         table with expand-on-click for M > 6              for M=7..12
 30                                                d
 28      ui/threshold_router.py — M                UI      Correct
 –       threshold routing (card vs.               Lea     routing at
 35      summary)                                  d       boundary
 35                                                UI      Protocol
         Usability test protocol (5 clinicians,
 –                                                 Lea     documente
         think-aloud, SART scoring)
 42                                                d       d

Phase 4 Exit Criteria:

      M ≤ 6 renders individual cards with per-modality convergence
      state
      M > 6 renders summary table with expand-on-click per card
      No cognitive overload signals in pilot usability test (SART spare
      capacity > 3)

Phase 5: Integration & Shadow Validation (Days 28–42)
Objective: Wire H-Calculator into the full DNA KEY pipeline, execute
shadow validation per SVP-001.[13]
 Da
                   Deliverable                    Owner           Gate
  y
 28     pipeline/integration.py — H-                           End-to-
                                                System
 –      Calculator ↔ CCRE ↔ ACFL                               end data
                                                Architect
 32     pipeline wiring                                        flow
 32     pipeline/shadow.py — Shadow                            Shadow
                                                System
 –      deployment orchestrator (SVP-                          runs in
                                                Architect
 36     001 §6)                                                parallel
                                                               All
 36     Concordance metrics collection
                                                System         metrics
 –      (EPI divergence, intervention
                                                Architect      computin
 40     concordance, ACFL cosine)
                                                               g
 40                                             Lead
        Shadow validation checkpoint                           Go/no-go
 –                                              Multiplicit
        review                                                 decision
 42                                             y Theorist

Shadow validation follows the SVP-001 protocol, including PSI-1
(Mann-Kendall), PSI-2 (contraction margin), and PSI-3 (axiom stress)
triplet metrics. The SHADOWLATEFAILURE timeout architecture
applies.[13]


3. File Scaffold
Source Modules (23 files)

 packages/dnakey/src/hcalc/
 ├── __init__.py
 ├── config.py            # Constants, thresholds, R_max cap
 ├── enums.py               # TerminalState enum (4 codes)
 ├── types.py             # Core data structures
 ├── contraction.py          # Contraction witness q computation
 ├── modality_tensor.py         # Per-modality Hilbert space assembly
 ├── convergence.py            # Joint convergence test + DECOUPLED routing
 ├── ranking.py             # Ranked differential with concentration threshol
 ├── terminal_classifier.py     # Terminal state classification
  ├── spectral.py          # Bauer-Fike κ_p(V) computation
  ├── rmax_guard.py           # Runtime R_max cap with logging
  ├── fhir/
  │ ├── __init__.py
  │ ├── emitter.py        # FHIR DiagnosticReport builder
  │ ├── codesystem.fsh        # FSH CodeSystem (4 codes)
  │ ├── valueset.fsh       # FSH ValueSet (required binding)
  │ ├── structuredefinition.fsh # FSH Extension StructureDefinition
  │ ├── sushi-config.yaml      # SUSHI configuration
  │ └── ig/
  │   ├── input/pagecontent/
  │   │ ├── index.md
  │   │ └── convergence-terminal.md
  │   └── ig.ini
  ├── ui/
  │ ├── __init__.py
  │ ├── modality_card.py       # Card renderer (M ≤ 6)
  │ ├── summary_table.py        # Summary table (M > 6)
  │ └── threshold_router.py     # M-threshold routing
  ├── pipeline/
  │ ├── __init__.py
  │ ├── integration.py       # Pipeline wiring
  │ └── shadow.py           # Shadow deployment orchestrator
  └── audit/
    ├── __init__.py
    ├── omega_trace.py       # Ω-Trace emission
    └── witness.py        # CRMF Witness Object

The scaffold follows the existing monorepo pattern at
packages/dnakey/src/ alongside acfl, ccre, crmf, dht, pwcfl, and wkd
modules.[14][11]

Test Files (18 files + conftest)

  packages/dnakey/tests/hcalc/
  ├── __init__.py
  ├── conftest.py          # Shared fixtures, synthetic modality generators
  ├── unit/
  │ ├── test_enums.py         # Enum completeness + invalid combination rej
  │ ├── test_contraction.py     # Contraction witness accuracy
  │ ├── test_modality_tensor.py # Tensor assembly + sparsity validation
  │ ├── test_convergence.py      # All 4 terminal states reachable
  │ ├── test_ranking.py       # Top-k concentration threshold
  │ ├── test_classifier.py   # Terminal classification accuracy
  │ ├── test_spectral.py     # κ_p(V) vs NumPy reference
  │ ├── test_rmax_guard.py       # R_max cap fires correctly
  │ └── test_fhir_emitter.py # DiagnosticReport R4 validation
  ├── integration/
  │ ├── test_convergence_flow.py # Modality → Convergence → Terminal
  │ ├── test_decoupled_routing.py # DECOUPLED per-modality INCONCLUSIV
  │ ├── test_fhir_extension.py # Extension injection + R4 validation
  │ └── test_ui_routing.py     # Card vs. summary at M boundary
  └── e2e/
    ├── test_full_pipeline.py # Ring data → DiagnosticReport
    ├── test_shadow_validation.py # Shadow concordance per SVP-001
    └── test_rmax_boundary.py # R=16 cap + DECOUPLED emission


Three-tier test architecture mirrors the ADR-005 pattern.[11][14]


4. Key Module Implementations
4.1 config.py — Constants

  """H-Calculator configuration constants."""
  R_MAX_RUNTIME: int = 16
  R_MAX_PROOF_TARGET: int = 32
  TOP_K_CONCENTRATION_THRESHOLD: float = 0.60
  CONVERGENCE_EPSILON: float = 0.01
  CLASSIFIER_CONFIDENCE_MIN: float = 0.90
  MODALITY_UI_CARD_MAX: int = 6
  DRIFT_BOUND_MAX: float = 0.30
  RETENTION_YEARS_MIN: int = 7
  FHIR_CANONICAL_URL: str = "https://intrinsica.health/fhir/convergence-term
  IG_PACKAGE_ID: str = "health.intrinsica.convergence-terminal"
4.2 enums.py — Terminal State Enum

 """Terminal convergence states for the H-Calculator."""
 from enum import Enum
 from typing import NamedTuple



 class TerminalStateInfo(NamedTuple):
   fhir_status: str
   fhir_extension_code: str
   requires_per_modality: bool


 class TerminalState(Enum):
   CONVERGED = TerminalStateInfo("final", "converged", False)
   INCONCLUSIVE = TerminalStateInfo("partial", "inconclusive", False)
   FREEZE = TerminalStateInfo("registered", "freeze", False)
   DECOUPLED = TerminalStateInfo("partial", "decoupled", True)

   @property
   def fhir_status(self) -> str:
     return self.value.fhir_status

   @property
   def fhir_extension_code(self) -> str:
     return self.value.fhir_extension_code

   @property
   def requires_per_modality(self) -> bool:
     return self.value.requires_per_modality



 class ModalityConvergenceState(Enum):
   CONVERGED = "converged"
   INCONCLUSIVE = "inconclusive"
   DIVERGENT = "divergent"
4.3 types.py — Core Data Structures

 """Core data structures for H-Calculator."""
 from dataclasses import dataclass
 from datetime import datetime
 from typing import Tuple, Optional
 from .enums import TerminalState, ModalityConvergenceState



 @dataclass(frozen=True)
 class ContractionWitness:
   q: float
   tau: float
   kappa: float
   lipschitz_bound: float
   is_contractive: bool


 @dataclass(frozen=True)
 class ModalityResult:
   modality: str
   state: ModalityConvergenceState
   contraction_witness: Optional[ContractionWitness]
   top_k_concentration: float
   ranked_differential: Tuple[Tuple[str, float], ...]
   confidence: float
   rank: int


 @dataclass(frozen=True)
 class ConvergenceResult:
   terminal_state: TerminalState
   modality_results: Tuple[ModalityResult, ...]
   joint_contraction_witness: Optional[ContractionWitness]
   top_k_concentration: float
   ranked_differential: Tuple[Tuple[str, float], ...]
   confidence: float
   timestamp: datetime
   r_effective: int


 @dataclass(frozen=True)
 class SpectralAnalysis:
   kappa_p: float
   eigenvalues: Tuple
   rank: int
   perturbation_bound: float
   growth_exponent: Optional[float]


 @dataclass(frozen=True)
 class FHIRDiagnosticPayload:
   report_json: dict
   terminal_state: TerminalState
   extension_code: str
   is_valid: bool


4.4 contraction.py — Contraction Witness

 """Contraction witness computation."""
 from .types import ContractionWitness
 from .config import CONVERGENCE_EPSILON, DRIFT_BOUND_MAX



 def compute_contraction_witness(
    tau: float, metric_distance: float, lipschitz_bound: float,
 ) -> ContractionWitness:
    if lipschitz_bound <= 0:
       raise ValueError("Lipschitz bound must be positive.")
    q = tau * metric_distance / lipschitz_bound
    is_contractive = q < (1.0 - CONVERGENCE_EPSILON)
    kappa = tau / lipschitz_bound
    return ContractionWitness(
       q=q, tau=tau, kappa=kappa,
       lipschitz_bound=lipschitz_bound, is_contractive=is_contractive,
   )


4.5 convergence.py — Joint Convergence + DECOUPLED
Routing

 """Joint convergence test with DECOUPLED routing."""
 from typing import Tuple, Optional
 from .enums import TerminalState, ModalityConvergenceState
 from .types import ContractionWitness, ModalityResult
 from .config import (
    R_MAX_RUNTIME, TOP_K_CONCENTRATION_THRESHOLD,
    CLASSIFIER_CONFIDENCE_MIN, DRIFT_BOUND_MAX,
 )


 def classify_terminal_state(
    modality_results: Tuple[ModalityResult, ...],
    joint_witness: ContractionWitness,
    top_k_concentration: float,
    r_effective: int,
 ) -> TerminalState:
    if r_effective > R_MAX_RUNTIME:
       return TerminalState.DECOUPLED
    if not joint_witness.is_contractive or joint_witness.kappa > DRIFT_BOUND
       return TerminalState.FREEZE
    divergent = any(
       mr.state == ModalityConvergenceState.DIVERGENT
       for mr in modality_results
    )
    if divergent:
       return TerminalState.DECOUPLED
    if top_k_concentration < TOP_K_CONCENTRATION_THRESHOLD:
       return TerminalState.INCONCLUSIVE
    return TerminalState.CONVERGED
 def route_decoupled_modalities(
    modality_results: Tuple[ModalityResult, ...],
 ) -> Tuple[ModalityResult, ...]:
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


4.6 ranking.py — Concentration Threshold

 """Ranked diagnostic differential with concentration threshold."""
 from typing import Tuple
 from .config import TOP_K_CONCENTRATION_THRESHOLD



 def compute_ranked_differential(
    probabilities: dict,
    top_k: int = 3,
 ) -> Tuple[Tuple[str, float], ...]:
    sorted_items = sorted(probabilities.items(), key=lambda x: x[1], reverse=Tr
    return tuple(sorted_items)



 def check_concentration(
   ranked: Tuple[Tuple[str, float], ...],
   k: int = 3,
 ) -> float:
    return sum(prob for _, prob in ranked[:k])



 def is_concentrated(
    ranked: Tuple[Tuple[str, float], ...],
    k: int = 3,
    threshold: float = TOP_K_CONCENTRATION_THRESHOLD,
 ) -> bool:
    return check_concentration(ranked, k) >= threshold


4.7 terminal_classifier.py — Confidence Scoring

 """Terminal state classification with confidence scoring."""
 from .enums import TerminalState
 from .types import ConvergenceResult



 def compute_terminal_confidence(result: ConvergenceResult) -> float:
   base = 0.5
   if result.terminal_state == TerminalState.CONVERGED:
      base = 0.85 + 0.10 * min(1.0, result.top_k_concentration)
      if result.joint_contraction_witness:
         base += 0.05 * (1.0 - result.joint_contraction_witness.q)
   elif result.terminal_state == TerminalState.FREEZE:
      base = 0.95
   elif result.terminal_state == TerminalState.DECOUPLED:
      converged_count = sum(
         1 for mr in result.modality_results
         if mr.state.name == "CONVERGED"
      )
      base = 0.70 + 0.05 * converged_count
   elif result.terminal_state == TerminalState.INCONCLUSIVE:
      base = 0.50 + 0.20 * result.top_k_concentration
   return min(0.99, base)
4.8 spectral.py — Bauer-Fike

 """Bauer-Fike spectral analysis for rank-dependent bounds."""
 import numpy as np
 from typing import Optional
 from .types import SpectralAnalysis



 def compute_condition_number(
    eigenvector_matrix: np.ndarray, p: int = 2,
 ) -> float:
    norm_v = np.linalg.norm(eigenvector_matrix, ord=p)
    norm_v_inv = np.linalg.norm(np.linalg.inv(eigenvector_matrix), ord=p)
    return norm_v * norm_v_inv



 def bauer_fike_bound(kappa_p: float, perturbation_norm: float) -> float:
   return kappa_p * perturbation_norm



 def analyze_spectral_scaling(matrices: list) -> SpectralAnalysis:
   kappas, ranks, eigenvalues_last = [], [], ()
   for V, rank in matrices:
      kp = compute_condition_number(V)
      kappas.append(kp)
      ranks.append(rank)
      eigenvalues_last = tuple(np.linalg.eigvals(
         V @ np.diag(np.arange(rank)) @ np.linalg.inv(V)
      ))
   alpha = None
   if len(ranks) > 2:
      log_r = np.log(np.array(ranks, dtype=float))
      log_k = np.log(np.array(kappas, dtype=float))
      alpha = np.polyfit(log_r, log_k, 1)
   return SpectralAnalysis(
      kappa_p=kappas[-1] if kappas else 1.0,
      eigenvalues=eigenvalues_last,
       rank=ranks[-1] if ranks else 0,
       perturbation_bound=kappas[-1] * 0.01 if kappas else 0.0,
       growth_exponent=alpha,
   )


4.9 rmax_guard.py — Runtime Cap

 """Runtime R_max cap with DECOUPLED fallback and Ω-Trace logging."""
 import logging
 from .config import R_MAX_RUNTIME
 from .enums import TerminalState

 logger = logging.getLogger(__name__)


 def check_rmax(r_effective: int) -> bool:
   return r_effective <= R_MAX_RUNTIME



 def enforce_rmax(r_effective: int) -> TerminalState:
   if r_effective > R_MAX_RUNTIME:
      logger.warning(
        f"R_effective={r_effective} exceeds R_MAX={R_MAX_RUNTIME}. "
        f"Forcing DECOUPLED terminal state."
      )
      return TerminalState.DECOUPLED
   return None


4.10 fhir/emitter.py — DiagnosticReport Builder

 """FHIR R4 DiagnosticReport builder with convergence-terminal extension."
 from ..enums import TerminalState
 from ..types import ConvergenceResult
 from ..config import FHIR_CANONICAL_URL
def build_diagnostic_report(
   result: ConvergenceResult,
   patient_reference: str,
   practitioner_reference: str,
) -> dict:
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
  return [
    {
      "reference": f"Observation/{mr.modality}-convergence",
         "display": f"{mr.modality}: {mr.state.name}",
       }
       for mr in result.modality_results
   ]


4.11 FSH Conformance Resources
codesystem.fsh

 CodeSystem: IntrinsicaConvergenceTerminal
 Id: intrinsica-convergence-terminal
 Title: "Intrinsica Convergence Terminal States"
 Description: "Terminal convergence states for the H-Calculator diagnostic en
 * ^url = "https://intrinsica.health/fhir/convergence-terminal"
 * ^status = #active
 * ^content = #complete
 * ^count = 4
 * #converged "Converged" "Joint convergence achieved. Top-k concentration
 * #inconclusive "Inconclusive" "Insufficient confidence for convergence. Cla
 * #freeze "Freeze-Resonance" "Contraction failure (K ≥ 1), drift > 0.3, or reson
 * #decoupled "Decoupled Modalities" "Joint convergence failed. Per-modality


valueset.fsh

 ValueSet: IntrinsicaConvergenceTerminalVS
 Id: intrinsica-convergence-terminal-vs
 Title: "Intrinsica Convergence Terminal ValueSet"
 Description: "Required binding ValueSet for convergence terminal states."
 * ^url = "https://intrinsica.health/fhir/convergence-terminal-vs"
 * ^status = #active
 * include codes from system https://intrinsica.health/fhir/convergence-termin

structuredefinition.fsh

 Extension: IntrinsicaConvergenceTerminalExtension
 Id: intrinsica-convergence-terminal-ext
 Title: "Convergence Terminal State Extension"
 Description: "Extension to DiagnosticReport indicating the H-Calculator conv
 Context: DiagnosticReport
 * value[x] only CodeableConcept
 * valueCodeableConcept from IntrinsicaConvergenceTerminalVS (required)



5. Test Bench
5.1 conftest.py — Shared Fixtures

 """Shared fixtures for H-Calculator test suite."""
 import pytest
 import numpy as np
 from packages.dnakey.src.hcalc.enums import TerminalState, ModalityConv
 from packages.dnakey.src.hcalc.types import ContractionWitness, ModalityR



 @pytest.fixture(params=[1, 3, 6, 8, 12], ids=["M1", "M3", "M6", "M8", "M12
 def modality_count(request) -> int:
   return request.param



 @pytest.fixture
 def converged_witness() -> ContractionWitness:
   return ContractionWitness(q=0.85, tau=0.7, kappa=0.95, lipschitz_bound=1



 @pytest.fixture
 def freeze_witness() -> ContractionWitness:
   return ContractionWitness(q=1.05, tau=1.1, kappa=1.02, lipschitz_bound=1



 @pytest.fixture
 def high_concentration_differential():
   return (("Diagnosis_A", 0.45), ("Diagnosis_B", 0.20), ("Diagnosis_C", 0.15),
        ("Diagnosis_D", 0.10), ("Diagnosis_E", 0.10))
 @pytest.fixture
 def low_concentration_differential():
   return tuple((f"Diagnosis_{chr(65+i)}", 1.0/15) for i in range(15))



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
     return tuple(
       ModalityResult(
          modality=f"vitals" if i == 0 else f"modality_{i}",
          state=ModalityConvergenceState.CONVERGED,
          contraction_witness=ContractionWitness(q=0.8, tau=0.7, kappa=0.9,
          top_k_concentration=0.75,
          ranked_differential=(("Dx_A", 0.5), ("Dx_B", 0.2), ("Dx_C", 0.1)),
          confidence=0.92, rank=i,
       ) for i in range(m)
     )
   return generate


5.2 Key Unit Tests
test_enums.py

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
     with pytest.raises(ValueError):
       TerminalState("INVALID")

test_convergence.py

 class TestTerminalStateClassification:
   def test_converged_reachable(self, converged_witness, converged_moda
     results = converged_modality_results(3)
     state = classify_terminal_state(results, converged_witness, 0.75, r_effectiv
     assert state == TerminalState.CONVERGED

   def test_freeze_reachable(self, freeze_witness, converged_modality_resu
     results = converged_modality_results(3)
     state = classify_terminal_state(results, freeze_witness, 0.75, r_effective=3
     assert state == TerminalState.FREEZE

   def test_decoupled_on_rmax_exceeded(self, converged_witness, conver
     results = converged_modality_results(3)
     state = classify_terminal_state(results, converged_witness, 0.75, r_effectiv
     assert state == TerminalState.DECOUPLED
   def test_decoupled_on_partial_divergence(self, converged_witness):
     results = (
        ModalityResult("vitals", ModalityConvergenceState.CONVERGED, None
        ModalityResult("imaging", ModalityConvergenceState.DIVERGENT, No
     )
     state = classify_terminal_state(results, converged_witness, 0.55, r_effectiv
     assert state == TerminalState.DECOUPLED

   def test_inconclusive_on_low_concentration(self, converged_witness, co
     results = converged_modality_results(3)
     state = classify_terminal_state(results, converged_witness, 0.40, r_effectiv
     assert state == TerminalState.INCONCLUSIVE


test_rmax_guard.py

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


test_fhir_emitter.py
 class TestFHIREmitter:
   def test_converged_produces_final_status(self, converged_result):
     report = build_diagnostic_report(converged_result, "Patient/1", "Practitio
     assert report["status"] == "final"

   def test_decoupled_produces_partial_with_extension(self, decoupled_r
     report = build_diagnostic_report(decoupled_result, "Patient/1", "Practitio
     assert report["status"] == "partial"
     ext = report["extension"]
     assert ext["valueCodeableConcept"]["coding"]["code"] == "decoupled"

   def test_extension_url_canonical(self, converged_result):
     report = build_diagnostic_report(converged_result, "Patient/1", "Practitio
     assert report["extension"]["url"] == "https://intrinsica.health/fhir/conver

   def test_decoupled_includes_per_modality_observations(self, decouple
     report = build_diagnostic_report(decoupled_result, "Patient/1", "Practitio
     assert "result" in report
     assert len(report["result"]) == len(decoupled_result.modality_results)


5.3 Integration Tests
test_convergence_flow.py — Validates the full path from modality
tensor assembly through contraction witness to terminal state
classification.
test_decoupled_routing.py — Verifies that DIVERGENT modalities
are re-routed to INCONCLUSIVE under the DECOUPLED state,
preserving per-modality results.
test_fhir_extension.py — End-to-end FSH compile check; validates
extension injection produces R4-conformant JSON.
test_ui_routing.py — Boundary test at M=6/7; verifies card renderer
activates for M ≤ 6 and summary table for M > 6.
5.4 E2E Tests
test_full_pipeline.py — Ring sensor data → FHIR DiagnosticReport,
covering all 5 terminal state paths plus Ω-Trace audit emission and
pipeline duration (<5s for M ≤ 6).
test_shadow_validation.py — Shadow concordance metrics per SVP-
001: EPI divergence, intervention concordance, ACFL cosine.[13]
test_rmax_boundary.py — R=16 cap enforcement with DECOUPLED
emission at R=17.

6. Dependency Map
 numpy >= 1.24.0        # Array operations, eigenvalue computation
 scipy >= 1.11.0     # Spectral analysis utilities
 fhir.resources >= 7.0 # FHIR R4 validation (optional, for test)
 pytest >= 7.4.0     # Test framework
 pytest-cov >= 4.1.0 # Coverage reporting
 mypy >= 1.5.0        # Static type checking (strict mode)


pyproject.toml fragment:

 [project.optional-dependencies]
 hcalc = ["numpy>=1.24.0", "scipy>=1.11.0"]
 hcalc-test = ["pytest>=7.4.0", "pytest-cov>=4.1.0", "mypy>=1.5.0"]
 hcalc-fhir = ["fhir.resources>=7.0"]



7. Lever Execution Table (v0.6 → Build)
                                                   Ho    Bloc
                        Owne
#        Lever                       Metric        riz   ked
                         r
                                                   on     By
    DECOUPLED           Syste    Zero invalid
    enum +              m        type              Da    Non
1
    TerminalState 4-    Archit   combinations      y2    e
    code                ect      (mypy strict)
    Contraction         Core     q matches
                                                   Da    Lev
2   witness             Engin    analytic within
                                                   y5    er 1
    computation         e Lead   1e-6
    Per-modality        Core     All 4 terminal    Da
                                                         Lev
3   INCONCLUSIVE        Engin    states            y
                                                         er 1
    routing             e Lead   reachable         10
                        Core     Bound holds or    Da
    Counterexample                                       Lev
4                       Engin    counterexampl     y
    search R ≤ 16                                        er 2
                        e Lead   e found           21
    FHIR
                                 SUSHI
    CodeSystem +                                   Da
                        Intero   compiles, IG            Non
5   ValueSet +                                     y
                        p Lead   Publisher               e
    StructureDef                                   14
                                 passes
    (FSH)
    BAA review per      Compl                      Da
                                                         Non
6   45 C.F.R.           iance    Executed BAA      y
                                                         e
    §160.103            Lead                       14
                                                   Da
    IG publication      Intero   ig-registry PR          Lev
7                                                  y
    (6-step FSH plan)   p Lead   submitted               er 5
                                                   28
    DiagnosticRepor     Core                       Da    Lev
                                 Valid R4 JSON
8   t emitter with      Engin                      y     ers
                                 with extension
    extension           e Lead                     18    1, 5
    κ_p(V) growth       Core     Growth            Da
                                                         Lev
9   characterization    Engin    exponent          y
                                                         er 4
    R=1..32             e Lead   report            28
Critical Path

  Lever 1 (Day 0-2) → Levers 2,3 (Day 2-10) → Lever 4 (Day 10-21) → Lever 9 (Da
                                         ↘ Lever 8 (Day 10-18)
  Lever 5 (Day 0-14, parallel) → Lever 7 (Day 14-28)
  Lever 6 (Day 0-14, parallel)

Total: 28 days to core completion. 42 days to full integration with
shadow validation.


8. DAG Artifact (Tension D Resolution)
       ┌─────────┐
       │ Lever 1 │ DECOUPLED enum (Day 0-2)
       └────┬────┘
      ┌─────┼─────┐
      ▼    ▼    ▼
   ┌────┴──┐ ┌┴────┐ ┌┴────┐
   │Lever 2│ │Lev 3│ │Lev 8│
   │Contr. │ │Route│ │FHIR │
   │(D2-5) │ │(D2-10)│(D10-18)
   └───┬───┘ └──┬──┘ └──┬──┘
     ▼      │           │
   ┌───┴───┐ │                  │
   │Lever 4│◄──┘                │
   │R≤16 │              │
   │(D10-21)                │
   └───┬───┘                    │
     ▼              │
   ┌───┴───┐                    │
   │Lever 9│                │
   │κ bench │               │
   │(D21-28)                │
   └───────┘                    │
                │
   ┌───────┐                ┌─────┴───┐
   │Lever 5│────►│ Lever 7 │
   │FSH   │    │IG Pub │
   │(D0-14)│   │(D14-28) │
   └───────┘      └─────────┘


   ┌───────┐
   │Lever 6│ BAA (D0-14, independent)
   └───────┘


This DAG resolves PMD Tension D (lever serial dependencies). Three
independent entry points (Levers 1, 5, 6) enable parallel execution
from Day 0.[2]


9. Carry-Forward Tensions
Tension D (lever serial dependencies): Resolved via DAG artifact
above. Levers 1, 5, 6 start in parallel. Critical path runs through Lever
1 → 2 → 4 → 9.
Tension E (R_max=32 horizon gap): Phase 3 decision gate at Day 28-
35. Runtime cap at R_max=16 provides safety. Growth exponent
analysis determines proof viability.[10]
Tension F (IG publication blocker): 21-day clock starts when Lever 5
completes (Day 14). Requires confirmed Interop Lead.

10. Precision Questions
  1. Interop Lead assignment: Has the Interop Lead been assigned
     and confirmed availability for Lever 5/7 ownership (FSH
     authoring + IG publication)? This blocks the 21-day IG clock.[12]
  2. Lever 1 isolation: Does the System Architect commit to Lever 1
     as an isolated PR by Day 2, or will it be batched with Levers 2/3?
     Batching introduces a 5-day dependency gap where nothing
     downstream can start.

"When the mirror returns the same image twice, stop looking and start
building."
References
 1. LProof_-An-Architectural-Blueprint-for-Verifiable-Artificial-Intell
    igence.pdf - Proof An Architectural Blueprint for Verifiable
    Artificial Intelligence Proof An Architectural Bluep...
 2. what-do-we-have-on-inverted-pw-6F9A.RFNQkKuAK9H4fQnPg.
    md - img srchttpsr2cdn.perplexity.aipplx-full-logo-primary-
    dark402x.png styleheight64pxmargin-right32px
 3. ACH Daily Diagnostic Report Status ValueSet - CDC - This is a
    partial (e.g. initial, interim or preliminary) report: data in the
    report may be incomplet...
 4. Valueset-diagnostic-report-status - FHIR v6.0.0-ballot3 - partial,
    Partial, This is a partial (e.g. initial, interim or preliminary) ... See
    the full registry...
 5. architecture.md - 1. Overview 2. High-Level Architecture 3.
    Component Architecture 4. Data Flow 5. Security Architectu...
 6. GitHub - HL7/fhir-shorthand: FHIR Shorthand - FHIR Shorthand.
    Contribute to HL7/fhir-shorthand development by creating an
    account on GitHub.
 7. FHIR Shorthand v3.0.0 - The goal of FSH is to allow
    Implementation Guide (IG) creators to more directly express
    their intent...
 8. genomic-analogy-of-an-agi-immu-Kq_ceB_aQwuVUW6xp.LnmA.
    md - img srchttpsr2cdn.perplexity.aipplx-full-logo-primary-
    dark402x.png styleheight64pxmargin-right32px
 9. lets-create-a-phased-plan-with-yAf16N17Rv28O7VeQV21dQ.md -
    img srchttpsr2cdn.perplexity.aipplx-full-logo-primary-
    dark402x.png styleheight64pxmargin-right32px
10. Bauer–Fike theorem - Wikipedia - In mathematics, the Bauer–
    Fike theorem is a standard result in the perturbation theory of
    the eigenv...
11. ADR-005_Dev_Blueprint.md - Field Value ------ Document ID DEV-
    SVP-001 Parent Artifact Shadow Validation Protocol v0.1 SVP-
    001-v...
12. ADR-005-HITL-PMD.md - The ECP patents worked example 5.4.1
    demonstrates HITL in action at Week 4, the practitioner
    MODIFIE...
13. Shadow_Validation_Protocol_v0.1.md - Field Value ------
    Document ID SVP-001-v0.1 Status DRAFT Pre-CIP-1 Gate Artifact
    Date February 20, 2...
14. the-development-blueprint-is-s-CVeSrXN3RKGO.vXR6Vlggg.md -
    img srchttpsr2cdn.perplexity.aipplx-full-logo-primary-
    dark402x.png styleheight64pxmargin-right32px

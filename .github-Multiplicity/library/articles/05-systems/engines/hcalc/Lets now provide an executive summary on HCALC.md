---
slug: lets-now-provide-an-executive-summary-on-hcalc
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 05-systems/engines/hcalc/Lets now provide an executive summary on HCALC.md
  last_synced: '2026-03-20T17:17:18.266104Z'
---

![](media/image-d8a1f50f9d1479049c8908f351a4b9f2686f9384.png){width="2.6466666666666665in"
height="0.6666666666666666in"}

**Lets now provide an executive summary on HCALC**

I now have comprehensive data on HCALC. Let me compile the executive
summary.

**H-Calculator (HCALC) Executive Summary**

**Repository:**
[[packages/hcalc/]{.underline}](https://github.com/CHL987/Intrinsica/tree/e8736239f7ab1c1223db5aa62bff7697935591ce/packages/hcalc)
\| **Version:** 0.1.0 \| **Date:** February 21, 2026

**Definition and Core Role**

The H-Calculator is the **Convergence-Terminal Computation Engine** for
INTRINSICA. It occupies a distinct position in the system: it does not
manage logic operators (ACFL), inversion operators (I-ACFL), or
distillation (WKD). Its singular function is to assemble multi-modal
clinical data into a ranked differential and emit one of four terminal
states that drive every downstream decision --- HITL escalation, FHIR
emission, and ACFL explanation.

H-Calculator lives in its **own top-level package** (packages/hcalc/)
--- separate from packages/dna\_key/. This is the only module in the
repo with that boundary. The separation signals architectural intent:
HCALC is a general-purpose convergence engine, not a DNA KEY sub-module.

**The Four Terminal States**

Every pipeline execution resolves to exactly one of four outcomes:

  ------------------ ---------------------------------------------------------- ----------------------------------------------------------
  Terminal State     Trigger                                                    Clinical Meaning
  **CONVERGED**      Top-3 concentration ≥ 0.60, confidence ≥ 0.90              Ranked differential is safe to emit; HITL review invited
  **INCONCLUSIVE**   Confidence \< 0.90                                         Insufficient signal; defer, request more modalities
  **FREEZE**         Contraction witness q ≥ 1 − ε (Lipschitz bound violated)   Computation is unsafe; all outputs inhibited
  **DECOUPLED**      M (modality count) \> R\_MAX\_RUNTIME = 16                 Tensor rank exceeds runtime bound; convergence is unsafe
  ------------------ ---------------------------------------------------------- ----------------------------------------------------------

The FREEZE state is the computational analog of HITL\'s ADR-005 circuit
breaker: the engine refuses to emit rather than produce an unreliable
result.

**Mathematical Foundation**

**Contraction witness** (safety invariant):

$$\mathit{q} < 1 - \mathit{\varepsilon},\ \mathit{\varepsilon} = 0.01$$

where $\mathit{q}$ is the Lipschitz constant of the convergence map
$\mathit{T}:\mathbb{R}^{\mathit{r}} \rightarrow \mathbb{R}^{\mathit{r}}$.
The Banach fixed-point theorem guarantees a unique stable attractor when
$\mathit{q} < 1$. If this is violated, FREEZE is emitted and all
downstream outputs are blocked.

**DECOUPLED guard** --- R\_max runtime cap:

$$\mathit{M} > \mathit{R}\_\text{MAX\textbackslash\_RUNTIME} = 16 \Rightarrow \text{DECOUPLED}$$

A proof-target of $\mathit{R} = 32$ is deferred (placeholder
R\_MAX\_PROOF\_TARGET = 32). The current runtime cap is empirical, not
formally proven.

**EPI divergence** (SVP-001 §6, shadow gate):

$$\text{JSD}(\mathit{P}_{\text{prod}},\mathit{P}_{\text{shadow}}) \leq 0.10$$

Jensen-Shannon divergence over the top-3 ranked-differential probability
vectors. Exceeding this threshold triggers REVIEW, not immediate NO\_GO.

**Source Module Architecture**

  ------------------------- --------- -----------------------------------------------------------------------------------------
  File                      Size      Function
  \_\_init\_\_.py           2.4 KB    Public API: 4 enums, 10 types, 6 constants
  config.py                 5.2 KB    All locked thresholds (PMD v0.6)
  enums.py                  7.1 KB    TerminalState, ModalityConvergenceState, ClassifierConfidenceLevel, DiagnosisRankStatus
  types.py                  11.6 KB   All dataclasses: ContractionWitness, ModalityTensor, TerminalOutput, OmegaTraceEvent
  modality\_tensor.py       9.4 KB    create\_tensor() --- assembles M modalities into ranked tensor
  contraction.py            10.2 KB   Contraction witness computation, Lipschitz bounding
  convergence.py            10.0 KB   run\_joint\_convergence() --- CCRE-gated convergence
  terminal\_classifier.py   10.4 KB   classify\_terminal() --- 4-state classification
  ranking.py                8.4 KB    Differential ranking, top-K concentration scoring
  rmax\_guard.py            1.7 KB    enforce\_rmax() --- single-line modality cap check
  spectral.py               3.5 KB    Spectral analysis for PT-symmetric Hamiltonian
  pipeline/integration.py   12.0 KB   HCalculatorPipeline.run() --- full 8-step orchestration
  pipeline/shadow.py        14.2 KB   ShadowOrchestrator.run\_shadow() --- SVP-001 §6 shadow gate
  audit/omega\_trace.py     \~8 KB    Ω-Trace audit event emission
  fhir/                     dir       FHIR R4 DiagnosticReport emitter
  ui/                       dir       Modality UI card rendering (≤6 cards; \>6 → summary table)
  ------------------------- --------- -----------------------------------------------------------------------------------------

**Phase 5 Pipeline --- 8-Step Execution Sequence**

The commit b91f843 (February 21, 2026) delivered pipeline/integration.py
and pipeline/shadow.py as §§3.19--3.20 of the H-Calculator phased plan.
The wired execution sequence:

1.  **Ω-Trace** → pipeline\_start event

2.  **Assemble** ModalityTensor via create\_tensor(modalities)

3.  **R\_max guard** → enforce\_rmax(M); DECOUPLED shortcut if M \> 16

4.  **CCRE** → run\_joint\_convergence(tensor) → TerminalOutput

5.  **Terminal classify** → classify\_terminal(output) ---
    post-validation pass

6.  **FHIR** → build\_diagnostic\_report() → FHIR R4 dict

7.  **ACFL** → best-effort explanation bridge
    (acfl.explainer.ACFLExplainer, optional import)

8.  **Ω-Trace** → terminal\_reached event with elapsed time

The pipeline is **stateless** --- safe for concurrent invocations. The
ACFL explanation (step 7) uses a dynamic importlib import with full
exception swallowing --- it never fails the pipeline.

**SVP-001 §6 Shadow Validation**

pipeline/shadow.py implements the production ↔ shadow paired execution
gate. Three locked concordance thresholds:

  -------------------------- -------------------------------------------------- ----------- --------------------
  Metric                     Computation                                        Threshold   Gate
  EPI divergence             JSD over top-3 differential probabilities          ≤ 0.10      REVIEW if exceeded
  Intervention concordance   Jaccard of top-3 ICD-10 code sets                  ≥ 0.80      REVIEW if below
  ACFL cosine                Cosine similarity of explanation feature vectors   ≥ 0.90      REVIEW if below
  -------------------------- -------------------------------------------------- ----------- --------------------

Gate precedence: **NO\_GO** (terminal states diverge) → **GO** (states
match + all metrics in tolerance) → **REVIEW** (states match, ≥1 metric
outside tolerance).

Special cases: ACFL cosine = 1.0 when both explanations are absent (no
explanation = agreement on absence); intervention concordance = 1.0 when
both differentials are absent (FREEZE/DECOUPLED agreement).

**Key Constants ([[config.py]{.underline}](http://config.py), locked per
PMD v0.6)**

  ---------------------------------- ---------------------------- ----------------------------------------
  Constant                           Value                        Role
  TOP\_K\_CONCENTRATION\_THRESHOLD   0.60                         CONVERGED gate: top-3 probability mass
  CONVERGENCE\_EPSILON               0.01                         Contraction safety margin (q \< 1 − ε)
  CLASSIFIER\_CONFIDENCE\_MIN        0.90                         INCONCLUSIVE threshold
  R\_MAX\_RUNTIME                    16                           DECOUPLED modality cap
  R\_MAX\_PROOF\_TARGET              32                           Deferred proof target
  LIPSCHITZ\_BOUND\_MAX              0.999                        Maximum safe K
  DRIFT\_BOUND\_MAX                  0.30                         Maximum SBERT cosine drift
  DIFFERENTIAL\_TOP\_K               3                            Top-k diagnoses in output
  DIAGNOSIS\_PROB\_MIN               0.05                         Minimum probability for inclusion
  MODALITY\_UI\_CARD\_MAX            6                            UI card render threshold
  FHIR\_CANONICAL\_URL               intrinsica.health/fhir/...   FHIR R4 extension URL
  RETENTION\_YEARS\_MIN              7                            HIPAA minimum audit retention
  ---------------------------------- ---------------------------- ----------------------------------------

**Supported Modalities (12 Types)**

config.py defines the full modality taxonomy:

-   vitals --- HR, BP, SpO₂, respiratory rate, temperature

-   imaging --- ECG, X-ray, ultrasound, MRI, CT

-   genomics --- SNP arrays, sequencing, variant calling

-   text --- Clinical notes, discharge summaries

-   wearable --- Ring, watch, continuous monitoring

-   labs --- CBC, CMP, troponin, BNP

-   medications --- Current medications, allergies

-   procedures --- Recent procedures, interventions

-   social\_determinants --- Housing, employment, food security

-   family\_history --- HPI, relevant family diagnoses

-   environmental --- Pollution exposure, climate factors

-   behavioral --- Smoking, alcohol, exercise

**Test Suite**

Delivered with the Phase 5 commit: 47 new tests, 0 failures:

  --------------------------------------- -------------- -----------------------------------------------------------------------------------------------------------------------------------
  Test File                               Tests          Coverage
  tests/e2e/test\_full\_pipeline.py       11             All 4 terminal states, R\_max guard, Ω-Trace emission, FHIR status mapping, \< 5s SLA
  tests/e2e/test\_shadow\_validation.py   36             EPI divergence, intervention concordance, ACFL cosine, GO/NO\_GO/REVIEW gate logic, ShadowRun structure, orchestrator integration
  tests/e2e/test\_rmax\_boundary.py       pre-existing   DECOUPLED trigger at M = 17
  tests/e2e/test\_audit\_pipeline.py      pre-existing   Ω-Trace chain integrity
  --------------------------------------- -------------- -----------------------------------------------------------------------------------------------------------------------------------

The \< 5s pipeline duration SLA is an explicit test assertion --- not a
soft goal.

**HCALC ↔ System Integration Points**

  ---------------------- ----------------------------------------------------------------------------
  Downstream Module      Integration
  **HITL (ADR-005)**     CONVERGED → HITL review portal; FREEZE → circuit breaker pattern
  **ACFL / WKD**         Step 7 best-effort explanation via acfl.explainer.ACFLExplainer (optional)
  **CCRE**               run\_joint\_convergence() --- CCRE is the convergence certifier
  **FHIR R4**            build\_diagnostic\_report() → DiagnosticReport dict per encounter
  **Ω-Trace**            OmegaTraceEvent emitted at pipeline\_start and terminal\_reached
  **dna\_key package**   ACFL bridge uses dynamic import from dna\_key package via importlib
  ---------------------- ----------------------------------------------------------------------------

**Phase Mirror Dissonance**

**Tensions:**

-   R\_MAX\_RUNTIME = 16 is empirically tuned; R\_MAX\_PROOF\_TARGET =
    32 is a deferred placeholder with no timeline or owner assigned. The
    gap between runtime cap and proof target is unresolved.

-   The ACFL explanation bridge (step 7) uses bare except Exception:
    return None --- any silent failure in the explanation path produces
    a PipelineResult with acfl\_explanation=None and no audit trace.
    Explanation absence is indistinguishable from explanation failure.

-   The SVP-001 shadow gate uses REVIEW (not NO\_GO) when metrics exceed
    tolerance but states match. REVIEW has no defined escalation path,
    owner, or resolution SLA in the current codebase.

-   CONTRACTION\_TAU\_SCALING = 0.85 is labeled \"empirically tuned\" in
    config comments. No derivation is documented. If CCRE parameters
    change, this constant is silent drift risk.

-   HCALC\'s 12-modality taxonomy includes social\_determinants,
    environmental, and behavioral --- none of which are wired to
    biosensor inputs in the current ring integration. These are
    taxonomically present but computationally inert.

**Levers to test now:**

-   **\[Lead MT\]** --- Assign R\_MAX\_PROOF\_TARGET a delivery owner
    and horizon --- Metric: formal proof or documented deferral
    rationale --- Horizon: 30 days

-   **\[System Architect\]** --- Add Ω-Trace event for ACFL explanation
    failure (distinguish None-by-absence from None-by-error) --- Metric:
    zero silent failures in audit log --- Horizon: next commit

-   **\[Lead MT\]** --- Define REVIEW escalation path for SVP-001 shadow
    gate --- Metric: written SLA with owner, trigger criteria, and
    rollback decision authority --- Horizon: before ECP Phase 1

**Optional artifact:** \"A contraction witness with no proof is a
promise, not a guarantee.\"

**Precision question:** Does the REVIEW outcome in the SVP-001 shadow
gate block canary stage progression, or does it permit advancement with
human sign-off? The current codebase has no gate binding for REVIEW.

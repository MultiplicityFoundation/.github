---
slug: untitled-document
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 02-implementations/soulaware/Untitled document.md
  last_synced: '2026-03-20T17:17:15.714106Z'
---

**1. Product shape and scope (v0 → v2)**
----------------------------------------

### **1.1. What the app *is* (near-term)**

Treat the app as a **PMD Lab + Facilitator Dashboard**, not a therapy
robot:

-   A tool that:

    -   Computes **Dissonance Index D(x)** and related metrics from
        > text/voice/sensor streams.

    -   Visualizes these over time at the level of person, dyad, group.

    -   Helps facilitators/researchers design **micro-experiments** and
        > **contradiction tests** and see what actually reduces /
        > modulates dissonance.

    -   Enforces safety constraints and ethical kill-switches (subspace
        > drift, descent violations, Goodharting).

-   v0 target users:

    -   You + close collaborators.

    -   Friendly research partners (N=1 to small-N).

    -   DMTP pilots (dance + parts annotation).

-   *Not* for:

    -   Acute crisis use (explicit exclusion, like in the Bridge doc).

    -   Unsupervised self-help in vulnerable populations (at least in
        > early phases).

### **1.2. Release milestones**

**v0 -- PMD Lab (offline + "light" web)\
** Goal: Validate D(x)/δ\_eth pipeline on uploaded data.

-   Upload transcripts (and later, movement / HRV files).

-   Compute:

    -   D(x) over time for each speaker/segment.

    -   Group metrics (average D, alignment, basic consensus measures).

    -   For DMTP sessions: δ\_eth, Λ\_m, contraction factor q, resonance
        > R (even if visually simple at first).

-   Visualize time series + mark events (prompts, parts labels,
    > interventions).

-   Export JSON/CSV for stats + papers (to support the Research Proposal
    > aims 1--3).

**v1 -- Facilitator Dashboard (near real-time)\
** Goal: Support *live* facilitation in low-risk contexts.

-   Real-time ingest of text (and later audio) for D(x) estimation.

-   **Dissonance Monitoring Dashboard**:

    -   Live D(x) per person/session.

    -   Drift / descent alerts (subspace drift, descent violations).

-   **Consent + Dissonance Envelope**:

    -   Dynamic consent profiles (max coupling κ, off-limits topics,
        > data retention).

    -   Adjustable "dissonance envelope" for each session (how much
        > destabilization is allowed).

-   **Prompt Library**:

    -   Structured prompts with metadata and expected ΔD,
        > contraindications.

**v2 -- Research & DMTP Suite (multi-tenant, multi-modal)\
** Goal: Serve as the main research platform for PMD/DMTP studies.

-   Multi-tenant deployment (labs, orgs, DMTP studios).

-   Multi-modal streams (text, audio, IMU, HRV, EEG).

-   Advanced analytics:

    -   δ\_eth vs PANAS-N correlation; Λ\_m and contraction factors per
        > session.

    -   Causal analysis of prompts (Ξ) vs outcomes.

-   Full kill-switch criteria wired in (if prime advantage / parts
    > decoding / external validity fail, math layer is dropped, practice
    > layer stays).

**2. Core architecture**
------------------------

Think **two-layer stack**, matching DMTP × Multiplicity:

1.  **Layer 1 -- Practice & Events\
    > ** Raw data from sessions (utterances, movement, HRV,
    > annotations).

2.  **Layer 2 -- Math & Telemetry\
    > ** PMD core: embeddings, Π, D(x), δ\_eth, Λ\_m, group dynamics,
    > safety checks.

### **2.1. Components**

**(a) Data Ingest & Storage**

-   **Session service**:

    -   Manages sessions, participants, roles, consent docs.

-   **Ingest pipelines**:

    -   Text/metadata via REST/websocket.

    -   Files for offline processing (audio, IMU, HRV, EEG).

-   **Storage**:

    -   Postgres (sessions, events, metrics).

    -   Object storage (raw media).

    -   Config store for Π versions, prompt templates, kill-switch
        > configs.

**(b) PMD Math Engine ("pmd-core")**

Implements the formal framework:

-   State representations:

    -   Embedding wrappers for text/voice/other.

-   Subspace Π management:

    -   Learn & freeze Π from corpus; track subspace drift (s\_avg,
        > θ\_max).

-   Core metrics:

    -   D(x) = ∥(I − Π)x∥² for individuals.

    -   Group D and alignment (Laplacian-style).

    -   DMTP metrics: δ\_eth, Λ\_m, contraction factor q, resonance R.

-   Dynamics simulators (optional at first):

    -   Single-agent gradient-descent dynamics.

    -   Group update equations with κ and δ\_i,t terms.

**(c) Governance & Ethics Layer**

Implements the risk register & consent logic:

-   Π governance hooks (versioning, hashes, drift monitors).

-   **ConsentManager** & permission checks per operation.

-   Safety checks:

    -   Descent violation rate v (how often D(x\_t+1) \> D(x\_t) + ε).

    -   Goodhart on D (require external outcome metrics per experiment).

-   EthicalBoundaryMonitor patterns (overwhelm, dissociation, protector
    > rigidity) that trigger "no more magic" protocols (grounding, human
    > contact, stop).

**(d) Intervention & Prompt Engine (Ξ layer)**

-   Prompt library with metadata & expected ΔD.

-   Adaptive Ξ tuning:

    -   Learn which prompts/Ξ configs work for which contexts & people.

-   Live recommendations via **DissonanceAPI**:

    -   Given current D(x) + history + consent, suggest:

        -   "Decrease intensity" (Nourish).

        -   "Offer reflection question" (Inquire).

        -   "Small destabilizing prompt with strong circuit breakers"
            > (Surprise).

        -   "Integration prompt" (Explore).

**(e) Analytics, Experiments & Murder-Board**

-   Define **experiments** around contradictions and micro-experiments:
    > IDs, hypotheses, metrics, decision rules.

-   Micro-experiment ledger module:

    -   5--10 minute tests, track outcomes (ΔD, BTI, external ratings).

-   Periodic "murder-board" UI:

    -   Flag which metrics/models / prompt types are underperforming and
        > should be pruned.

**3. Development phases and concrete tasks**
--------------------------------------------

### **Phase 0 -- Alignment & design "frame"**

1.  Pick **initial use case**:

    -   Probably: "N=1 and small-N sessions (EQ-style) with transcripts
        > and simple self-report."

2.  Freeze a **v0 Π**:

    -   Get a held-out corpus (e.g., coherent conversation + journaling)
        > and build Π via PCA/SVD or similar.

3.  Decide on **stack** (example):

    -   Backend: Python (FastAPI) + Postgres.

    -   Frontend: Next.js/React + TypeScript.

4.  Define **risk posture** in the codebase:

    -   No acute crisis use; require external outcomes for any "success"
        > claims (matches Methodology + Risk Register).

### **Phase 1 -- PMD core library (backend only)**

Deliverable: pip-installable internal package pmd\_core.

Tasks:

-   Implement:

    -   D(x) and residuals given Π.

    -   Simple group metrics (average D across participants).

    -   Subspace drift metrics (nuclear norm / principal angles).

-   Implement DMTP metrics:

    -   δ\_eth(x) = x\^T L x + μ‖x‖₁.

    -   Λ\_m and contraction factor q checks.

-   Add simple simulators for the single-agent and group update
    > equations (used for research, not live control yet).

### **Phase 2 -- Offline analysis tool (CLI + minimal UI)**

Deliverable: pmd-analyze CLI + simple report viewer.

Tasks:

-   CLI to:

    -   Ingest transcript JSON (speaker, timestamp, text).

    -   Embed each utterance → x.

    -   Compute D(x\_t), group averages, and simple plots.

-   For DMTP sessions:

    -   Ingest movement/HRV features (even synthetic at first).

    -   Compute δ\_eth, Λ\_m, q, resonance R on each block.

-   Output:

    -   JSON reports + basic HTML summary.

-   Validation:

    -   Reproduce the minimal experiments from the Research Proposal:

        -   D(x) drop in structured disagreement vs neutral.

        -   δ\_eth vs PANAS-N correlation (even in tiny pilot form).

### **Phase 3 -- Backend service (DissonanceAPI)**

Deliverable: pmd-api service.

Tasks:

-   Implement API endpoints:

    -   /sessions: create/update sessions, attach Π version, consent
        > state.

    -   /streams/text: send incremental text segments; returns D(x\_t)
        > and alerts.

    -   /metrics/session/{id}: historical D, δ\_eth, etc.

    -   /experiments: define & tag contradictions, micro-experiments,
        > decision rules.

-   Implement **DissonanceAPI.real\_time\_stream** shape described in
    > Enhancements (current\_dissonance, recommended\_intervention,
    > convergence\_trajectory, anomaly\_flags).

-   Add **ConsentManager** hooks around all state-changing operations.

-   Add **risk checks**:

    -   Subspace drift guard.

    -   Descent violation rate thresholds.

### **Phase 4 -- Frontend: PMD Lab & Facilitator Dashboard**

Deliverable: single web app with two main "personas".

**Researcher view (Lab)**

-   Upload data, run analyses, see:

    -   D(x) timelines with tags for prompts, contradictions,
        > micro-experiments.

    -   δ\_eth & Λ\_m for DMTP sessions (even if rough).

    -   Export datasets for R/Python.

**Facilitator view (Dashboard)**

-   Live D(x) strip with:

    -   Per-participant sparkline.

    -   Flags when D(x) spikes beyond the "dissonance envelope."

-   Session configuration page:

    -   Consent settings, opt-outs, D envelope, mode
        > (Nourish/Inquire/Surprise/Explore).

-   Prompt suggestion pane:

    -   Shows 2--3 candidate prompts with predicted ΔD and intensity
        > rating.

### **Phase 5 -- DMTP pilot & research automation**

-   Integrate with DMTP practice:

    -   Phone IMUs / wearables ingestion as per DMTP × Multiplicity spec
        > (baseline → priming → dance blocks → reframe → post-baseline).

    -   Micro-annotation UI for parts (exile/manager/firefighter/none).

-   Implement kill-switch thresholds from DMTP × Multiplicity:

    -   Prime advantage, parts decoding F1, δ\_eth ↔ PANAS-N
        > correlation.

    -   If ≥2 fail, UI and API drop the fancy math layer and fall back
        > to "simple D + narrative reflections."

-   Add research workflows aligned with the Methodology paper
    > (pre-register experiments, track outcomes and risk metrics per
    > study).

**4. Repository / file & folder scaffold**
------------------------------------------

Here's a monorepo scaffold that fits everything above.

pmd-platform/

├── README.md

├── LICENSE

├── docs/

│ ├── overview.md \# High-level product + architecture

│ ├── theory/

│ │ ├── pmd\_math.md \# D(x), Π, group dynamics summary

│ │ ├── dmtp\_spec.md \# DMTP × Multiplicity mapping

│ │ └── risk\_register.md \# R1--R3, kill-switch conditions

│ ├── ethics/

│ │ ├── consent\_model.md \# Consent states, envelopes, opt-outs

│ │ └── usage\_boundaries.md \# No acute crisis, required supervision

│ ├── research/

│ │ ├── aims\_and\_hypotheses.md \# From Research Proposal

│ │ └── experiment\_templates.md \# Pre-reg forms, murder-board rubric

│ └── ops/

│ ├── data\_retention\_policy.md

│ └── security\_privacy.md

│

├── backend/

│ ├── pyproject.toml

│ ├── pmd\_core/ \# Pure math + metrics

│ │ ├── \_\_init\_\_.py

│ │ ├── embeddings/

│ │ │ ├── base.py

│ │ │ ├── text\_openai.py

│ │ │ └── text\_local\_model.py

│ │ ├── subspaces/

│ │ │ ├── pca\_subspace.py

│ │ │ ├── prime\_basis.py

│ │ │ └── drift\_metrics.py

│ │ ├── metrics/

│ │ │ ├── dissonance.py \# D(x), residuals

│ │ │ ├── group.py \# group D, alignment

│ │ │ ├── dmtp.py \# δ\_eth, Λm, contraction q, R

│ │ │ └── safety.py \# descent violation, small-gain checks

│ │ ├── dynamics/

│ │ │ ├── single\_agent.py \# xt+1 = xt - η Ξ (I-Π) xt

│ │ │ └── group\_dynamics.py \# Laplacian-coupled updates

│ │ └── io/

│ │ ├── transcripts.py

│ │ └── timeseries.py

│ │

│ ├── pmd\_api/ \# Service layer (FastAPI)

│ │ ├── \_\_init\_\_.py

│ │ ├── main.py \# App entrypoint

│ │ ├── config.py

│ │ ├── models/ \# Pydantic models

│ │ │ ├── session.py

│ │ │ ├── participant.py

│ │ │ ├── metrics.py

│ │ │ └── consent.py

│ │ ├── services/

│ │ │ ├── dissonance\_service.py

│ │ │ ├── session\_service.py

│ │ │ ├── consent\_manager.py \# dynamic consent checks

│ │ │ ├── experiment\_service.py

│ │ │ └── xi\_tuning.py \# Adaptive Ξ tuning

│ │ ├── routers/

│ │ │ ├── sessions.py

│ │ │ ├── streams.py \# real\_time\_stream endpoint

│ │ │ ├── metrics.py

│ │ │ ├── experiments.py

│ │ │ └── governance.py \# Π versions, drift status

│ │ └── db/

│ │ ├── base.py

│ │ ├── models.py \# ORM models: Session, Event, Metric, ΠSnapshot

│ │ └── migrations/

│ │ └── 0001\_init.sql

│ │

│ └── scripts/

│ ├── run\_dev.sh

│ ├── seed\_demo\_data.py

│ └── export\_reports.py

│

├── frontend/

│ ├── package.json

│ ├── tsconfig.json

│ ├── app/ \# Next.js app router

│ │ ├── layout.tsx

│ │ ├── page.tsx \# Landing / overview

│ │ ├── lab/

│ │ │ └── \[sessionId\]/page.tsx \# Offline analysis view

│ │ ├── dashboard/

│ │ │ └── \[sessionId\]/page.tsx \# Live facilitator dashboard

│ │ ├── experiments/page.tsx \# Contradictions & micro-experiments

│ │ └── governance/page.tsx \# Π versions, risk status, murder-board

│ ├── components/

│ │ ├── charts/

│ │ │ ├── DTimeSeries.tsx

│ │ │ ├── MultiMetricChart.tsx

│ │ │ └── DriftGauge.tsx

│ │ ├── consent/

│ │ │ └── ConsentPanel.tsx

│ │ ├── prompts/

│ │ │ └── PromptSuggestionCard.tsx

│ │ ├── experiments/

│ │ │ └── ExperimentEditor.tsx

│ │ └── layout/

│ │ └── SessionHeader.tsx

│ └── public/

│ └── favicon.ico

│

├── experiments/

│ ├── notebooks/

│ │ ├── 01\_validate\_D\_vs\_selfreport.ipynb

│ │ ├── 02\_structured\_disagreement\_ablation.ipynb

│ │ └── 03\_dmtp\_pilot\_metrics.ipynb

│ ├── configs/

│ │ ├── eq\_lab\_pilot.yaml

│ │ └── dmtp\_pilot.yaml

│ └── results/

│ └── README.md

│

├── infra/

│ ├── docker/

│ │ ├── Dockerfile.backend

│ │ └── Dockerfile.frontend

│ ├── compose.dev.yml

│ └── k8s/

│ ├── pmd-api-deployment.yaml

│ ├── pmd-api-service.yaml

│ └── postgres-statefulset.yaml

│

└── .github/

├── workflows/

│ ├── ci.yml \# tests, lint

│ └── deploy\_dev.yml

└── ISSUE\_TEMPLATE.md

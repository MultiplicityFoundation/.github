---
slug: phase-mirror-dissonance-open-core-must-be-useful
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 00-foundations/phase-mirror/Phase mirror dissonance___Open core must be useful.md
  last_synced: '2026-03-20T17:17:21.965268Z'
---

Phase mirror dissonance:
"Open core must be useful on its own" stated but not tested: No metric defines "useful"
(adoption? completeness? time-to-value?).​
Tier B moat claimed as "research velocity" but no research function exists: Who produces
ongoing rule innovation? What's the cadence?​
Compliance packs as proprietary conflicts with trust positioning: "Explainable, auditable" brand
clashes with closed compliance logic.​
FP calibration network effect requires customer data pooling: Privacy/competitive concerns
may block opt-in. No consent mechanism spec'd.​
Dual-repo split creates sync tax: Schema changes in OSS must propagate to Pro. Versioning
friction not addressed.​
"Managed provisioning" as value prop is weak: Terraform modules + docs neutralize this in
days.

Recommended Division (revised)​
LayerOpen Core (Apache 2.0)Proprietary​
Rules​
Tier A (MD-001–005) + rule interface​
Tier B (semantic, cross-repo) + compliance packs​
Infrastructure​
Schema, redaction, decision logic, CLI, NoOp stores​
DynamoDB/Redis impls, hosted SaaS, federation​
Data​
Local FP tracking interface​
Aggregate FP calibration service (network-effect moat)​
Support​
Community + docs​
Priority SLA, custom rule dev, incident response mode

Moat analysis​
Claimed MoatDurabilityRisk​
Tier B rules​
Medium​
Replicable unless tied to proprietary data/models​
Compliance packs​
Low​
Standards are public; OSS clones emerge in 6–12 months​
FP calibration service​
High​
Requires cross-customer data; genuine network effect​
Hosted oracle SaaS​
Medium​
Ops convenience; commoditizes if self-host is easy​
Federation (multi-repo)​
High​
Enterprise coordination is painful; sticky once adopted

Levers​
OwnerLeverMetricHorizon​
You​
Define "research velocity" function: who, cadence, output artifact​
Rule release rate ≥2/quarter​
14 days​
You​
Add telemetry consent mechanism for FP calibration pooling​
Opt-in rate ≥30%​
30 days​
You​
Create schema-sync CI: OSS schema change → Pro test failure​
Zero drift incidents​
7 days​
You​
Decide compliance pack strategy: OSS rules + paid "certified" badge vs closed​
Decision documented​
7 days​
Biz​
Model LTV of enterprise seats vs usage-based SaaS​
Revenue model validated​
21 days

Optional artifact​
Checklist: Open-core boundary validation​
OSS version solves a complete problem without Pro​
Pro value is additive, not unlocking​
Security/safety fixes always ship to OSS first​
Schema versioning shared; no proprietary schema extensions​
Telemetry consent explicit and revocable​
Moat depends on data or velocity, not access control

Precision question​
Is the FP calibration service opt-in per-customer, per-repo, or per-rule—and who owns the
aggregated dataset if a customer churns?

The self-applied dissonance is correct. Addressing the precision question and the governance
gaps:


FP Calibration Consent Model

Recommended structure: Opt-in per-org, granularity per-repo, revocable.


 Level                             Control                              Default

 Org                               Master toggle: participate in        Off
                                   aggregate calibration

 Repo                              Include/exclude specific repos       All included if org opts in
                                   from pooling

 Rule                              No per-rule opt-out (too granular;   N/A
                                   creates sparse data)
Data Ownership on Churn

    Data type                                             On churn

    Customer's raw FP events                              Deleted within 30 days (contractual)

    Aggregated, anonymized contributions to calibration   Retained (no PII, no repo-identifiable data)
    model

    Customer's own historical reports                     Exportable; deleted after export window



This follows the "data contribution vs data ownership" split common in federated learning
contexts. The customer contributes signal; they don't own the aggregate model. Spell this out
in ToS.


Revised Division (Final)


Open Core (Apache 2.0)

packages/mirror-dissonance/​
├── src/​
│      ├── oracle.ts                              # Core engine​
│      ├── rules/​
│      │    ├── types.ts                          # RuleDefinition interface​
│      │    ├── registry.ts                       # Loader + hash​
│      │    ├── MD-001.ts                         # Status check mismatch​
│      │    ├── MD-002.ts                         # Unpinned binaries​
│      │    ├── MD-003.ts                         # Manifest drift​
│      │    ├── MD-004.ts                         # Write token in drift​
│      │    └── MD-005.ts                         # Merge queue gaps​
│      ├── policy/​
│      │    ├── decision.ts                       # pass/warn/block​
│      │    ├── thresholds.ts                     # FP tolerance​
│      │    └── promotion.ts                      # Tier criteria​
│      ├── redaction/                             # Full redaction stack​
│      ├── fp-store/​
│      │    ├── interface.ts                      # FPStore interface​
│      │    └── noop.ts                           # Local dev​
│      ├── block-counter/​
│   │   ├── interface.ts               # BlockCounter interface​
│   │   └── memory.ts                  # Tests​
│   └── nonce/​
│       ├── loader.ts                  # Interface + env fallback​
│       └── validator.ts               # Multi-nonce validation​
├── schemas/​
│   ├── dissonance-report.schema.json​
│   └── rule-definition.schema.json​
├── cli/​
└── docs/​




Proprietary (Separate Repo)

mirror-dissonance-pro/​
├── rules/​
│   ├── tier-b/​
│   │   ├── MD-100.ts                  # Semantic job drift​
│   │   ├── MD-101.ts                  # Cross-repo protection​
│   │   └── MD-102.ts                  # Runner trust chain​
│   └── compliance/​
│       ├── soc2/​
│       ├── hipaa/​
│       └── pci-dss/​
├── infra/​
│   ├── fp-store/​
│   │   └── dynamodb.ts                # Managed impl​
│   ├── block-counter/​
│   │   ├── dynamodb.ts​
│   │   └── redis.ts​
│   └── calibration/​
│       ├── aggregator.ts              # Cross-customer FP pooling​
│       ├── consent.ts                 # Opt-in/revoke logic​
│       └── anonymizer.ts              # Strip identifiers​
├── federation/​
│   ├── org-aggregator.ts              # Multi-repo rollup​
│   └── cross-repo-rules.ts            # Rules that span repos​
├── saas/​
│   └── hosted-oracle/                 # API + dashboard​
└── sync/​
       └── schema-check.ts                       # CI: OSS schema → Pro tests​




Governance Additions


Research Function

    Role                               Cadence                             Output

    Rule author (you initially)        Biweekly review of customer         Candidate rule spec
                                       incidents, CVEs, GitHub changelog

    Steward                            Monthly                             Promote/demote decisions, FP
                                                                           review

    Release                            Quarterly minimum                   ≥2 new Tier B rules or major rule
                                                                           revisions




Schema Sync CI

# In mirror-dissonance-pro CI​
name: Schema Sync Check​
on:​
    schedule:​
       - cron: '0 6 * * *'        # Daily​
    workflow_dispatch:​
​
jobs:​
    check:​
       runs-on: ubuntu-latest​
       steps:​
           - uses: actions/checkout@v4​
           ​
           - name: Fetch OSS schema​
               run: |​
                 curl -o oss-schema.json \​


https://raw.githubusercontent.com/<org>/mirror-dissonance/main/packages/mirror-dissonanc
e/schemas/dissonance-report.schema.json​
                 ​
           - name: Compare hash​
           run: |​
             OSS_HASH=$(sha256sum oss-schema.json | cut -d' ' -f1)​
             PRO_HASH=$(sha256sum schemas/dissonance-report.schema.json | cut -d' ' -f1)​
             if [ "$OSS_HASH" != "$PRO_HASH" ]; then​
               echo "::error::Schema drift detected"​
               exit 1​
             fi​




Telemetry Consent Schema

interface CalibrationConsent {​
     org_id: string;​
     enabled: boolean;​
     scope: 'all_repos' | 'selected_repos';​
     included_repos?: string[];      // If scope = selected_repos​
     excluded_repos?: string[];      // If scope = all_repos​
     granted_at: Date;​
     granted_by: string;             // User ID​
     revocable: true;                // Always true; contractual​
     data_retention_days: 30;        // Post-churn deletion window​
     anonymization_level: 'full';    // No repo names, no file paths in aggregate​
}​




Moat Validation Checklist

 ●​ [ ] OSS version solves a complete problem without Pro

 ●​ [ ] Pro value is additive, not unlocking

 ●​ [ ] Security/safety fixes always ship to OSS first

 ●​ [ ] Schema versioning shared; no proprietary schema extensions

 ●​ [ ] Telemetry consent explicit and revocable

 ●​ [ ] Moat depends on data or velocity, not access control

 ●​ [ ] Research function defined with cadence and owner

 ●​ [ ] Schema sync CI prevents drift

 ●​ [ ] Churn data policy documented in ToS
Remaining Lever

 Owner                        Lever                    Metric                  Horizon

 You                          Draft ToS section:       Legal review complete   14 days
                              "Calibration Data
                              Contribution"




"The mirror doesn't sell clarity. It sells the cost of avoiding it."​



⁂



    1.​ The Phase to Mirror Dissonance.pdf

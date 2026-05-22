---
slug: what-parts-would-we-divide-between-the-open-core-a
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 00-foundations/phase-mirror/What parts would we divide between the open-core
    a.md
  last_synced: '2026-03-20T17:17:21.972371Z'
---

What parts would we divide between the open-
core and proprietary extensions?
Good question. The division should follow a principle: the open core must be useful on its own,
and the proprietary layer adds value that's hard to replicate, not gatekeeps basic functionality.

Proposed Division

Open Core (Apache 2.0)
                          Component                                                     Rationale

    dissonance_report schema                                       Interoperability; others can build tooling against it

    Oracle engine (oracle.ts, decision logic)                      Core protocol must be auditable and trustworthy

    Rule interface (RuleDefinition, types.ts)                      Enables community rules

    Tier A rules (MD-001 through MD-005)                           Fast, well-understood checks with near-zero FP

    Redaction framework (patterns, policy, validation)             Safety-critical; must be inspectable

    CLI (--mode pull_request, --mode merge_group)                  Basic invocation

    GitHub Actions workflow templates                              Adoption friction removal

    NoOp implementations (FP store, block counter)                 Local dev and testing

    Schema versioning and hash utilities                           Determinism guarantees


Proprietary Extensions
                           Component                                                       Rationale

  Tier B rules (semantic analysis, cross-repo drift, merge-queue       Deep detection requires ongoing research; hard
  edge cases)                                                          to replicate

  Rule packs by domain (SOC2, HIPAA, PCI-DSS mappings)                 Compliance expertise has independent value

  FP calibration service (historical FP rates, auto-demotion
                                                                       Requires persistent infrastructure + data
  recommendations)

  Hosted oracle (SaaS)                                                 Ops burden, SLAs, availability guarantees

  Multi-repo federation (org-wide dissonance aggregation)              Enterprise-scale coordination

  Incident response mode (real-time dissonance during
                                                                       Requires low-latency infrastructure
  outages)
                         Component                                               Rationale

 Priority support + custom rule development                    Labor

 DynamoDB/Redis implementations with managed
                                                               Convenience; users can build their own
 provisioning


Phase Mirror Dissonance (on this division)
   Tier A vs Tier B boundary is governance, not code: If Tier B rules are just "more rules,"
   users will replicate them. The moat must be ongoing research velocity or data network
   effects.
   Redaction in open core is correct but creates obligation: If a vulnerability is found in
   redaction, you must patch the OSS version. No "security fixes only in paid tier."
   Compliance packs risk commoditization: SOC2/HIPAA mappings are well-documented;
   someone will publish OSS equivalents. Your moat is "maintained + tested + updated when
   standards change."
   FP calibration service has real network effects: Aggregate FP data across customers
   improves recommendations. This is defensible.

Concrete Boundary

 packages/
 ├── mirror-dissonance/                   # Apache 2.0
 │   ├── src/
 │   │   ├── rules/
 │   │   │   ├── MD-001.ts                    # OSS
 │   │   │   ├── MD-002.ts                    # OSS
 │   │   │   ├── MD-003.ts                    # OSS
 │   │   │   ├── MD-004.ts                    # OSS
 │   │   │   └── MD-005.ts                    # OSS
 │   │   ├── policy/                          # OSS (decision logic)
 │   │   ├── redaction/                       # OSS (safety-critical)
 │   │   └── fp-store/
 │   │       ├── interface.ts                 # OSS
 │   │       └── noop.ts                      # OSS
 │   └── schemas/                             # OSS

 ├── mirror-dissonance-pro/               # Proprietary (separate repo or private package)
 │   ├── rules/
 │   │   ├── MD-100.ts                        # Semantic job-name drift
 │   │   ├── MD-101.ts                        # Cross-repo protection inconsistency
 │   │   └── compliance/
 │   │       ├── SOC2-*.ts
 │   │       └── HIPAA-*.ts
 │   ├── fp-store/
 │   │   ├── dynamodb.ts                      # Managed implementation
 │   │   └── calibration.ts                   # FP rate analysis service
 │   └── federation/
 │       └── org-aggregator.ts                # Multi-repo rollup
Levers
  Owner                                   Lever                                       Metric           Horizon

  You       Define Tier B rule criteria: what makes a rule "deep" vs "fast"?   Criteria doc reviewed   7 days

  You       Identify 3 Tier B rules with genuine research moat                 Rules spec'd            14 days

            Decide: compliance packs proprietary or OSS with paid              Decision
  You                                                                                                  7 days
            support?                                                           documented

  You       Scope FP calibration service MVP                                   Service spec            21 days


Precision Question
What's your primary monetization goal—enterprise seats (compliance packs, support), usage-
based SaaS (hosted oracle), or both? That determines whether compliance packs stay
proprietary or become OSS with paid maintenance.
                                                          ⁂

  1. The Phase to Mirror Dissonance.pdf

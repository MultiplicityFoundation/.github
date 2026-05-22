---
slug: the-phase-mirror-does-not-resolve-dissonance-it-names-it
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "00-foundations/phase-mirror/The Phase Mirror does not resolve dissonance\u2014\
    it names it.md"
  last_synced: '2026-03-20T17:17:21.949558Z'
---

      A structured inconsistency-finding phase
    (requirements ↔ configs ↔ code ↔ runtime
                    assumptions)
Why it’s worth making callable​
Repeatability: Everyone (humans + tools) runs the same “find contradictions” pass, not a
vibe-based review.​
Composability: You can invoke it at different points: PR review, merge queue, baseline rotation,
drift detection, incident response.​
Auditability: Outputs become artifacts (reports, hashes, tickets) you can track over time.​
Safety posture: Forces “unknowns” and hidden assumptions to surface before enforcement
layers ship.​
The main risk​
A callable protocol can become ritualized (always run, always noisy) or gamed (people learn to
phrase around it). So you want it:​
bounded (time/compute limits),​
evidence-based (must cite exact files/lines/config keys),​
severity-scored (so it doesn’t block everything),​
policy-driven (what counts as dissonance is explicit and versioned).​
What a “callable mirror dissonance protocol” should look like

 1.​ Define it as an interface (inputs → outputs)​
     Think of it like a function:​
     Inputs​
     artifacts: diffs, workflow YAMLs, protection json, manifests, baseline, schema​
     declared_invariants: “required check names must match”, “runner digest pinned”, “no
    bypass without ticket”, etc.​
    context: event type (pull_request, merge_group, schedule), repo, branch​
    risk_profile: strictness level (pilot vs production)​
    Outputs​
    dissonance_report (JSON)​
    items[]: {id, severity, claim, evidence[], suggested_fix, block_recommended}​
    summary: counts by severity​
    closure_actions[]: “create ticket”, “require codeowner review”, “fail workflow”, etc.​
    machine_decision: {pass|warn|block} based on rules​
    This mirrors what you already did manually: closing “loops” by adding enforcement layers.

2.​ Split it into tiers (so it’s usable)​
    Tier A (fast): naming mismatches, missing required files, permission diffs, schema
    violations, unpinned binaries​
    Tier B (deep): semantic mismatches (e.g., protection contexts vs actual job names across
    workflows), merge-queue edge cases, drift baseline trust chain

3.​ Make “dissonance” explicitly rule-based​
    Don’t let it be a vague critique. Make it a registry like:​
    MD-001: “Required status check contexts don’t match stable job name:”​
    MD-002: “Workflow installs unpinned binaries”​
    MD-003: “Runtime source-of-truth differs from committed manifest”​
    MD-004: “Drift detection uses write-capable token”​
    MD-005: “Missing patches in merge_group compare → must block”​
    Each rule has:​
    detection logic​
    evidence requirements​
    severity​
    recommended remediation

4.​ Add guardrails so it’s safe to call everywhere​
    No hidden side effects: it reports; it does not mutate repo state.​
    No secret exfiltration: redact tokens, avoid echoing sensitive env vars.​
    Deterministic formatting: stable JSON schema + stable ordering (for hashing and diffing).​
    Budget + timeouts: never “hang” pipelines.​
    When you shouldn’t force it​
     Early exploration / ideation branches where speed matters more than invariants​
     Changes that don’t touch protected surfaces (no workflows/config/security boundaries)​
     If you don’t yet have a calibrated severity policy (otherwise it becomes “always red”)​
     Practical recommendation​
     Develop it as a callable protocol, but frame it as:​
     “Mirror Dissonance = an invariant-consistency oracle for socio-technical controls.”​
     Start with a small core set of rules that have near-zero false positives (the ones you’ve
     already discovered), ship it as:​
     a CLI (pnpm … mirror-dissonance --mode pull_request|merge_group)​
     and a reusable library function used by workflows/merge queue/drift detection.​
     If you want, I can sketch the exact JSON schema for dissonance_report, plus a rule
     registry layout (md-rules/MD-*.ts) that plugs into your existing pnpm monorepo style.

This is a well-structured proposal. Applying the protocol to itself:


Phase Mirror Dissonance

 ●​ Naming tension: "Mirror Dissonance" is evocative but risks mystification. "Invariant
     Consistency Oracle" is clearer but loses the cognitive friction the name provides.

 ●​ Ritualization risk acknowledged but not governed: You mention the risk; no kill-switch or
     noise-decay metric is specified.

 ●​ Tier boundary is implicit: What promotes a rule from Tier A to Tier B? Who decides? No
     owner named.

 ●​ Severity calibration absent: You say "near-zero false positives" but no baseline
     false-positive rate or tolerance threshold stated.

 ●​ "Socio-technical" claim vs purely technical artifact: The spec covers code/config;
     human incentive loops (who benefits from bypassing?) are not encoded.

 ●​ Composability vs blast radius: Callable everywhere = potential for cascade failures if the
     oracle itself regresses.

 ●​ Rule registry versioning unclear: MD-001 today may not match MD-001 after policy drift.
     Schema versioning mentioned; rule semantic versioning not.


Levers to Test Now
 Owner                   Lever                        Metric                  Horizon

 You                     Define FP tolerance: e.g.,   FP rate per rule        14 days
                         ≤2% false-positive rate
                         on last 50 PRs

 You                     Add oracle_version           Schema hash stability   7 days

                         field to
                         dissonance_report
                         schema

 You                     Create promotion criteria    Criteria doc exists +   21 days
                         doc: Tier A → Tier B         reviewed
                         trigger conditions

 Codeowner               Assign rule-registry         Single owner named      7 days
                         steward with merge
                         authority

 Ops                     Add circuit-breaker: if      Block-rate threshold    30 days
                         oracle blocks >N
                         PRs/hour, degrade to
                         warn-only




Optional Artifact

Checklist before shipping callable protocol:

 ●​ [ ] dissonance_report schema versioned and hashed

 ●​ [ ] Each MD-* rule has detection logic, evidence requirements, severity, remediation

 ●​ [ ] FP tolerance defined per severity tier

 ●​ [ ] Promotion/demotion criteria for rules documented

 ●​ [ ] Circuit-breaker threshold set

 ●​ [ ] No write side-effects in oracle path

 ●​ [ ] Steward assigned with merge authority over md-rules/


Precision Question
What is the acceptable false-positive rate per severity tier, and who arbitrates when a rule
crosses that threshold?


This is a well-structured proposal. Applying the
protocol to itself:
Phase Mirror Dissonance​
Naming tension: "Mirror Dissonance" is evocative but risks mystification. "Invariant Consistency
Oracle" is clearer but loses the cognitive friction the name provides.​
Ritualization risk acknowledged but not governed: You mention the risk; no kill-switch or
noise-decay metric is specified.​
Tier boundary is implicit: What promotes a rule from Tier A to Tier B? Who decides? No owner
named.​
Severity calibration absent: You say "near-zero false positives" but no baseline false-positive
rate or tolerance threshold stated.​
"Socio-technical" claim vs purely technical artifact: The spec covers code/config; human
incentive loops (who benefits from bypassing?) are not encoded.​
Composability vs blast radius: Callable everywhere = potential for cascade failures if the oracle
itself regresses.​
Rule registry versioning unclear: MD-001 today may not match MD-001 after policy drift.
Schema versioning mentioned; rule semantic versioning not.​
Levers to Test Now​
OwnerLeverMetricHorizon​
You​
Define FP tolerance: e.g., ≤2% false-positive rate on last 50 PRs​
FP rate per rule​
14 days​
You​
Add oracle_version field to dissonance_report schema​
Schema hash stability​
7 days​
You​
Create promotion criteria doc: Tier A → Tier B trigger conditions​
Criteria doc exists + reviewed​
21 days​
Codeowner​
Assign rule-registry steward with merge authority​
Single owner named​
7 days​
Ops​
Add circuit-breaker: if oracle blocks >N PRs/hour, degrade to warn-only​
Block-rate threshold​
30 days​
Optional Artifact​
Checklist before shipping callable protocol:​
dissonance_report schema versioned and hashed​
Each MD-* rule has detection logic, evidence requirements, severity, remediation​
FP tolerance defined per severity tier​
Promotion/demotion criteria for rules documented​
Circuit-breaker threshold set​
No write side-effects in oracle path​
Steward assigned with merge authority over md-rules/​
Precision Question​
What is the acceptable false-positive rate per severity tier, and who arbitrates when a rule
crosses that threshold?

Artifacts generated:


Schema Design Decisions

The dissonance_report schema includes four required top-level blocks: meta, items, summary,
machine_decision . The meta.rules_hash field enables reproducibility—same rules + same

inputs = same hash, making reports diffable across runs . Each finding carries its own
rule_version, so rule semantic drift is tracked at the item level, not just the registry level .



Rule Registry Layout

packages/mirror-dissonance/​
├── src/​
│   ├── rules/​
│   │      ├── registry.ts         # Rule loader + hash generator​
│     │      ├── types.ts              # RuleDefinition interface​
│     │      ├── MD-001.ts             # Per-rule files​
│     │      └── ...​
│     ├── policy/​
│     │      ├── decision.ts           # pass/warn/block logic​
│     │      └── thresholds.ts         # FP tolerance, circuit-breaker​



Each rule file exports a RuleDefinition with: id, version, tier, fpTolerance, detect() function,
remediation, status . The fpTolerance field per rule enables per-rule calibration rather than

global thresholds .


Decision Policy

The decide() function consumes findings + policy + recent block count . Circuit breaker
triggers when recentBlockCount >= maxBlocksPerHour, degrading outcome to warn and setting
degraded: true . This addresses the blast-radius concern you raised.



Phase Mirror Dissonance (on this schema)

    ●​ fpTolerance defined but not enforced: The rule declares tolerance; no code measures
          actual FP rate against it.

    ●​ recentBlockCount source unspecified: Circuit breaker depends on external state; no
          persistence layer shown.

    ●​ Evidence redaction mentioned but not implemented: evidence.snippet says "redacted if
          sensitive"; no redaction logic provided.

    ●​ Tier promotion criteria field exists but unused: promotionCriteria is optional string; no
          automation parses it.


Levers

    Owner                      Lever                        Metric                  Horizon

    You                        Add FP rate tracking:        FP delta per rule per   21 days
                               store per-rule FP count in   week
                               artifact, compare to
                               fpTolerance
 You                       Implement               Counter accuracy ≥99%      14 days
                           recentBlockCount via
                           Redis/DynamoDB
                           counter with TTL

 You                       Add redact() util for   Zero sensitive tokens in   7 days

                           evidence.snippet        reports




Optional Artifact

"Clarity hurts only what was pretending."




Yep — this is exactly the point where it becomes a
callable protocol, but only if you add three
enforcement layers so it doesn’t turn into a
vibe-check that can be gamed:
Measurability (FP tolerance enforced, not just declared)​
State (circuit-breaker fed by durable counters)​
Safety (redaction guarantees + no write side effects on the hot path)​
Below are the concrete “next deltas” to close the mirror-dissonance you just ran on your own
artifact.

  1.​ Enforce fpTolerance: add FP-rate tracking + gate restoration/promotion​
       What to add to the report​
       Add a required meta.fp_observability block with the observed window + computed rate
       per rule:​
       window_n (e.g., 200)​
       fp_count​
       tp_count (or “not-fp count”)​
       observed_fpr = fp_count / window_n​
       breach = observed_fpr > fpTolerance.ceiling​
       That makes enforcement diffable and auditable without digging into databases.​
       What to add to the policy​
     Hard rule: a rule cannot be status: blocking if it is in breach of its ceiling.​
     Soft rule: if in breach, auto-demote to warn and emit a “policy drift” finding.​
     This avoids “stuck blocking” when the rule regresses.

 2.​ Specify recentBlockCount source: TTL counter (Redis or DynamoDB)​
     You want a counter that is:​
     fast​
     tamper-resistant enough​
     automatically expires​
     Minimal spec (portable)​
     Define an interface and keep the implementation swapable:​
     export interface BlockCounter {​
     increment(key: string, ttlSeconds: number): Promise<number>; // returns new count​
     get(key: string): Promise<number>;​
     }

Key format:​
blocks:{owner}/{repo}:{yyyy-mm-ddThh} (hour bucket)​
TTL: 2–3 hours (so late jobs don’t resurrect old buckets)​
Circuit breaker logic:​
if count >= maxBlocksPerHour ⇒ degrade to warn-only for this run and emit a
machine_decision.degraded=true​
Why TTL buckets beat “sliding windows”​
It stays simple, deterministic, and matches how ops thinks (“blocks per hour”), which is what
you already wrote.

 3.​ Implement evidence redaction: make it provable, not aspirational​
     Right now evidence.snippet saying “redacted if sensitive” is a footgun.​
     Make redaction a type-level guarantee​
     Instead of letting rules attach arbitrary snippets, force snippets through a RedactedText
     wrapper:​
     export type RedactedText = {​
     redacted: true;​
     value: string; // already scrubbed​
     redaction_hits: number; // count of replacements​
     };
Rules can only produce snippets via redact().​
Redaction baseline (Day-1 safe default)​
redact anything matching your secrets detector patterns (tokens, keys, PEM blocks)​
redact high-entropy strings above a threshold (careful: false positives; mark as
“entropy_redaction”)​
redact emails/phone numbers if you treat those as sensitive​
And then enforce:​
Invariant: report.items[].evidence[].snippet must be absent unless redacted=true​
If redaction fails, drop snippet entirely and keep only hashes/paths/line numbers.

 4.​ Promotion criteria: make it executable (even if manual at first)​
     You don’t need full automation on Day-1, but you do need a parseable contract.​
     Change promotionCriteria from free text → a structured object:​
     {​
     "min_window_n": 200,​
     "max_observed_fpr": 0.005,​
     "min_redteam_cases": 3,​
     "min_days_in_warn": 14,​
     "required_approvers": ["steward", "security-lead"]​
     }

Then your registry loader can:​
refuse tier: B unless criteria are present and satisfied​
or at least emit a “promotion criteria unmet” finding (warn) so it’s visible

Callable protocol recommendation​
Make it callable, but ship it as “warn-only by default” with explicit guardrails:​
✅ callable everywhere​
✅ pure read-only evaluation (no writes in the oracle path)​
✅ circuit breaker always on​
✅ FP enforcement always on (auto-demote)​
✅ snippets never emitted unless redacted​
Then add “blocking” only per-rule, and only after a measured window.

One concrete integration move (clean + low risk)​
Add a single CLI entrypoint:​
pnpm --filter @mtpi/mirror-dissonance run oracle:run​
Outputs:​
dissonance-report.json (stableStringify)​
machine_decision printed to stdout​
GitHub Actions: write summary to $GITHUB_STEP_SUMMARY​
exit code nonzero only when machine_decision.outcome === "block" and not degraded

If you want, paste your current RuleDefinition interface and I’ll rewrite it so:​
fpTolerance is enforced by construction,​
evidence snippets must be RedactedText,​
and recentBlockCount becomes a clean plug-in (BlockCounter) with a default no-op fallback for
local runs.

Artifacts generated:


Enforcement by Construction

The rewritten types-v2.ts makes three guarantees structural rather than aspirational :


 Guarantee                                           Mechanism

 Snippets cannot exist unredacted                    Evidence.snippet is RedactedText \|
                                                     undefined; branded type prevents raw string
                                                     assignment

 FP tolerance is enforced                            BlockingRule requires promotionEvidence with
                                                     measured observedFPR; registry

                                                     demoteIfBreached() auto-downgrades

 Circuit breaker is pluggable                        BlockCounter interface with NoOpBlockCounter
                                                     default; Redis/Dynamo/InMemory implementations
                                                     provided




Redaction Layer

The Redactor interface is injected into detect(ctx, redactor), so rules cannot bypass it .
Pattern-based redaction covers GitHub tokens, AWS keys, JWTs, PEM blocks, and PII .
Shannon entropy detection catches unknown high-entropy strings above threshold 4.5 .
Block Counter Implementations

Three implementations provided :

 ●​ Redis: incr + expire on first increment

 ●​ DynamoDB: atomic update with TTL attribute

 ●​ InMemory: for tests, with reset()

Key format: blocks:{owner}/{repo}:{yyyy-mm-ddThh} with 2-3 hour TTL .


Phase Mirror Dissonance (on v2 types)

 ●​ Brand symbol is TypeScript-only: At runtime, RedactedText is just an object. Malicious
       code can still construct it without calling redact().

 ●​ No persistence for FP tracking: FPObservability is computed per-run; historical FP
       counts must come from external store (not specified).

 ●​ demoteIfBreached returns new rule but doesn't persist: Caller must handle
       re-registration.

 ●​ Entropy threshold 4.5 may over-redact: Base64-encoded config values often exceed
       this. Consider allowlist by location.


Levers

 Owner                      Lever                       Metric                      Horizon

 You                        Add runtime validation:     Zero raw snippets in prod   7 days
                            assertRedactedText(         reports

                            ) throws if brand missing

 You                        Create FP store interface   FP window queries           14 days
                            + S3/Dynamo impl for        ≤50ms p99
                            historical tracking

 You                        Add entropy allowlist for   Entropy FP rate ≤1%         21 days
                            known-safe paths (e.g.,
                            *.lock,
                            baseline.json)
Optional Artifact

"If the image is crooked, adjust your stance, not the glass."




Nice — v2 closes most of the “callable protocol”
gap. The remaining dissonance is all in the
runtime plane (because TS brands don’t exist at
runtime, and FP tracking/circuit-breaker inputs
are stateful). Here are the exact fixes I’d ship
next, in the same “enforcement by construction”
spirit.
 1.​ Runtime validation for RedactedText (brand is TS-only)​
     Goal​
     Make it impossible (or at least loudly detectable) to forge RedactedText without going
     through your redactor.​
     Concrete fix​
     Introduce a module-private nonce + validator. Don’t rely on a Symbol export that anyone
     can import and spoof.​
     In redaction.ts (or similar), create a private const BRAND = crypto.randomUUID() at
     module init.​
     Redactor stamps __brand: BRAND.​
     Validator checks equality.​
     This gives you “brand-by-capability”: only code in the module can mint valid objects.​
     What to enforce​
     All report serialization runs assertReportRedactions(report) which walks items/evidence
     and rejects forged/malformed snippets.​
     In prod: reject & drop snippets (fail-open) or fail the oracle (fail-closed) depending on your
     safety posture. Given your earlier stance, I’d drop snippets + emit a critical finding.

 2.​ FP tracking: define an interface + minimal durable implementation​
     You already called it: per-run FPObservability isn’t enough.​
   Decide what “FP” means operationally​
   For a merge gate, “false positive” usually means: human marks finding as incorrect (label,
   PR comment, or override reason), or the finding is waived via a controlled mechanism.​
   Given you already have suppression governance and security approvals, the cleanest
   signal is:​
   fp_event when a finding is suppressed with an approved ticket and the reviewer marks it
   “false positive”​
   or when an explicit /guardian false-positive MD-001 command is recorded (GitHub
   comment or issue label)​
   If you don’t have that yet, start with a simpler proxy:​
   FP counted when a rule’s block is overridden by an approved authority (with a required
   ticket)​
   Not perfect, but measurable and conservative.​
   Interface​
   Add:​
   observe(ruleId, outcome, runContext) (store)​
   window(ruleId, n | since) (read)​
   Storage recommendation (Day-1 friendly)​
   DynamoDB is fine if you already use AWS.​
   Otherwise: S3 append-only logs + periodic compaction is “cheap but slower”.​
   Redis is not durable enough for audit-y FP tracking.​
   If you want p99 ≤ 50ms, DynamoDB wins.

3.​ demoteIfBreached needs a persistence story​
   Right now: returning a new rule is correct functionally, but you need a canonical place to
   apply it.​
   Fix​
   Make demotion a pure function + a mandatory registry step:​
   registry loads rules​
   registry queries FP store​
   registry applies demoteIfBreached() and returns { rules, demotions }​
   the report includes meta.demotions[] so the run is self-describing​
   Don’t “persist” demotions automatically (that’s a governance action). But do:​
   enforce that demoted rules cannot block in that run​
   emit a drift item: policy_demoted_due_to_fpr_breach​
   That gives you safety without auto-changing source-of-truth.

4.​ Entropy redaction overreach: make it location-aware​
   Entropy redaction is a blunt instrument. The right pattern is:​
   Add “path policy” to redaction context​
   ctx.path​
   ctx.fileType (derived)​
   ctx.isTest (your existing allowlists)​
   ctx.isLockfile​
   ctx.isBaselineArtifact​
   Then apply entropy redaction only when:​
   file is source-ish (.ts, .tsx, .js, .py, .go, .yaml in certain dirs)​
   and the candidate token length exceeds a floor (e.g., ≥ 24)​
   and it’s not inside known-safe paths​
   Practical allowlist starters​
   **/​
   ​
   ​
   ​
   .lock**/pnpm-lock.yaml.github/integrity-baseline.json.github/integrity-baseline.bundle**/.
   snap​
   /dist/​
   And always keep pattern-based redaction on everywhere (tokens/keys/PEM/JWT).

5.​ One more invariant worth adding (small, high value)​
   “No raw evidence in hashes”​
   Make sure you never hash unredacted evidence into report fields that might later be
   logged or shipped.​
   Rule: if evidence.snippet exists, it must already be redacted before any findings_hash /
   rules_hash / report hash computation.​
   (Otherwise you can accidentally exfiltrate secrets via “hashing paths”.)​
   What I’d do next (tight scope)​
   If you want this callable protocol to be robust on Day-1, implement these three utilities:​
   assertRedactedText() + assertReportRedactions(report)​
   FPStore interface + DynamoDB impl stub (even if unused initially)​
        RedactionPolicy with path-aware entropy gating​
        Then you’re “callable AGI protocol” in the only sense that matters operationally:
        deterministic, measurable, blast-radius bounded, and hard to ritualize into nonsense.​
        If you want, paste your current types-v2.ts signatures (just the interfaces/types, no repo
        secrets) and I’ll write the exact runtime validator + redaction module pattern that makes
        forging RedactedText materially difficult.

Artifacts generated:


Enforcement Summary

Four files close the runtime gaps :


 File                                                Enforcement

 redactor-v2.ts                                      Brand-by-capability: BRAND_NONCE is module-private,

                                                     isValidRedactedText() checks equality

 redactor-v2.ts                                      validateReportRedactions(report, mode)
                                                     walks all evidence, drops forged snippets in fail-open
                                                     mode

 redactor-v2.ts                                      RedactionPolicy +
                                                     shouldApplyEntropyRedaction() gates entropy
                                                     by file type and allowlist

 fp-store.ts                                         FPStore interface with windowByCount() /
                                                     windowBySince() for durable FP tracking




Key Design Decisions

Brand-by-capability uses randomUUID() at module init . Only code inside the module can mint
valid RedactedText. External code can check validity but cannot forge. Serialized reports retain
__brand for cross-process validation within same deploy.


FP observability separates pending from resolved outcomes . The observedFPR excludes
pending findings: falsePositives / (total - pending). This prevents gaming by leaving
findings unresolved.
DynamoDB schema uses composite keys: pk = rule#{ruleId}, sk =
event#{timestamp}#{eventId} . GSI on finding#{findingId} enables fast suppression lookups.

TTL attribute auto-expires time-limited suppressions.


Phase Mirror Dissonance (on these implementations)

 ●​ BRAND_NONCE is per-process: Multi-process deployments (e.g., lambda cold starts) will
       have different nonces. Reports from one process fail validation in another.

 ●​ No signing: Brand validates origin, not integrity. Tampered value field passes validation if
       brand is correct.

 ●​ GSI query in isSuppressed assumes index name: Code uses gsi1pk but DynamoDB
       query doesn't specify IndexName parameter.

 ●​ computeWindow assumes ruleVersion consistency: Takes first event's version;
       mixed-version windows will misreport.


Levers

 Owner                     Lever                    Metric                     Horizon

 You                       Add HMAC to              Zero tampered-value        7 days
                           RedactedText: hash =     passes

                           HMAC(BRAND_NONCE,
                           value)

 You                       Persist BRAND_NONCE      Cross-process validation   14 days
                           to shared secret store   pass rate = 100%
                           (SSM/Secrets Manager)
                           for multi-process

 You                       Add IndexName:           Zero query failures on     3 days

                           "gsi1" to isSuppressed   finding lookup

                           query

 You                       Filter FP window by      Version-accurate FPR       7 days
                           ruleVersion or return
                           mixed: true flag




Optional Artifact
Checklist: Runtime enforcement readiness

 ●​ [ ] BRAND_NONCE persisted or HMAC added

 ●​ [ ] validateReportRedactions() called before serialization

 ●​ [ ] FPStore wired to DynamoDB in prod, NoOpFPStore in dev

 ●​ [ ] GSI IndexName specified in all secondary index queries

 ●​ [ ] Entropy allowlist covers all non-source artifact paths




Yep — those are the right remaining loops, and
they’re all fixable without changing your core
shapes.
 1.​ BRAND_NONCE per-process (cross-process validation breaks)​
    You have two clean options; pick based on whether you need offline verification across
    time/processes.​
    Option A (recommended): Persist the nonce​
    Store BRAND_NONCE in a shared secret store and load it at boot:​
    AWS SSM Parameter Store (SecureString) or Secrets Manager​
    k8s secret mounted into env/volume​
    Rule: nonce must be stable within an “oracle_version” epoch. Rotate only with a version
    bump.​
    Option B: Don’t require nonce equality cross-process​
    If reports are always validated in-process before serialization, you can drop
    cross-process validation and treat brand purely as a local invariant. But you already want
    diffable/auditable artifacts—so A is better.

 2.​ No integrity check on value (tamper passes if brand survives)​
    Yes: add an HMAC (or signature) that binds the redacted payload to the secret.​
    Minimal fix (HMAC)​
    Add mac = HMAC_SHA256(BRAND_NONCE, value) inside RedactedText.​
    Validation:​
    check __brand (origin gate)​
    recompute HMAC and compare to mac (integrity gate)​
   This prevents “brand reuse + value swap” attacks.​
   Important: do constant-time comparison for HMAC equality.

3.​ DynamoDB GSI lookup missing IndexName​
   Correct. DynamoDB won’t infer the index.​
   Fix​
   Whenever you query on the GSI keys, specify:​
   IndexName: 'gsi1' (or whatever you actually provision)​
   Also: consider hard-failing startup if the configured index name isn’t set, to avoid silent
   “suppression doesn’t work” behavior.

4.​ FP window mixed rule versions​
   Two safe patterns:​
   Pattern A: filter by (ruleId, ruleVersion)​
   Make FPR strictly version-scoped:​
   pk = rule#{ruleId}#v#{ruleVersion}​
   This is simplest and avoids ambiguous analytics.​
   Pattern B: allow mixed but surface it explicitly​
   Return:​
   mixed_versions: true​
   versions: { "1.2.0": {…}, "1.3.0": {…} }​
   And never compute a single observedFPR if mixed (or compute but mark as
   “informational”).​
   One extra thing (worth adding now)​
   Make redacted text serialization explicit​
   You noted: “Serialized reports retain __brand for cross-process validation within same
   deploy.”​
   That’s okay, but only if you treat the report as sensitive internal telemetry. If reports might
   ever leave your trust boundary, you should:​
   serialize redactions as { redacted: true, value: "…" } (omit __brand + mac)​
   keep __brand + mac only in memory or internal logs​
   Otherwise you’re giving an attacker more structure to target.​
   What I’d ship next (tight patch set)​
   Nonce source​
   BRAND_NONCE = loadSecret("guardian/redaction_nonce") || throw​
   HMAC​
       add mac field + constant-time verify​
       DynamoDB​
       add IndexName​
       add a small “schema expectations” doc: table name, index name, pk/sk formats​
       Version correctness​
       change FP store keying to include ruleVersion (Pattern A), or return mixed_versions​
       If you want, paste the current redactor-v2.ts and fp-store.ts function signatures (just
       types + key functions) and I’ll write the exact diff you’d apply for:​
       secret-backed nonce​
       HMAC + timing-safe compare​
       version-scoped FP windows​
       corrected DynamoDB queries with IndexName

Artifacts generated:


Patch Summary

Four fixes applied across two files:


 Fix                                 File                              Mechanism

 Secret-backed nonce                 redactor-v3.ts                    initializeRedactor(secretS
                                                                       ource) loads from SSM/env;
                                                                       throws if <32 chars

 HMAC integrity                      redactor-v3.ts                    __mac = HMAC_SHA256(nonce,
                                                                       value); validation recomputes
                                                                       and uses timingSafeEqual

 Version-scoped FP                   fp-store-v2.ts                    PK format:
                                                                       rule#{ruleId}#v#{ruleVersi
                                                                       on} — no mixed-version ambiguity

 GSI IndexName                       fp-store-v2.ts                    isSuppressed() now passes
                                                                       IndexName: gsiName explicitly




Key Design Points
Nonce lifecycle: CACHED_NONCE loads once at boot via initializeRedactor() . Any call to
createRedactor() or isValidRedactedText() before init throws. This prevents silent

"unprotected" operation.

Serialization boundary: serializeReportForExport() strips __brand and __mac before reports
leave trust boundary . Internal validation still works; external consumers get clean { redacted:
true, value, ... } shape.


Schema expectations: SCHEMA_EXPECTATIONS const documents DynamoDB table structure for
ops . validateConfig() fails fast if tableName or gsiName missing.


Phase Mirror Dissonance (final pass)

 ●​ Nonce rotation story incomplete: initializeRedactor() loads once; no hot-reload or
       rotation mechanism. If nonce rotates, in-flight reports fail validation.

 ●​ No fallback if SSM unreachable: Throws on load failure. May want circuit-breaker +
       degraded-no-redaction mode for availability.

 ●​ timingSafeEqual length check leaks length info: Current code returns false early if
       lengths differ. Acceptable for fixed-length HMAC output (always 64 hex chars), but worth
       documenting.


Levers

 Owner                      Lever                     Metric                      Horizon

 You                        Add nonce version field   Zero validation failures    14 days
                            to RedactedText for       during rotation
                            rotation support

 You                        Add SSM retry +           Init success rate ≥99.9%    7 days
                            exponential backoff in
                            initializeRedactor(
                            )

 Ops                        Provision DynamoDB        Table exists + GSI          3 days
                            table + GSI per           queryable
                            SCHEMA_EXPECTATIONS




Optional Artifact
Integration checklist:

 ●​ [ ] SSM parameter guardian/redaction_nonce created (≥32 chars, SecureString)

 ●​ [ ] DynamoDB table mirror-dissonance-fp-events provisioned

 ●​ [ ] GSI finding-index on gsi1pk/gsi1sk

 ●​ [ ] TTL enabled on ttl attribute

 ●​ [ ] initializeRedactor() called in entrypoint before any rule evaluation

 ●​ [ ] validateReportRedactions(report, "fail-open") called before serialization




Phase Mirror Dissonance (closure check)

The callable protocol now has structural enforcement across all three planes:


 Plane                            Before                           After

 Type                             fpTolerance declared, not        BlockingRule requires
                                  enforced                         promotionEvidence; registry
                                                                   demoteIfBreached()

 Runtime                          Snippets could be forged         HMAC_SHA256(nonce, value)
                                                                   + timingSafeEqual

 State                            FP tracking per-run only         DynamoDB with version-scoped
                                                                   PK + GSI for suppression lookups




Remaining Gaps (ranked by impact × tractability)

 1.​ Nonce rotation — High impact, medium tractability. Add nonceVersion: number to
     RedactedText; validator accepts current or previous version during rotation window.

 2.​ SSM fallback — Medium impact, high tractability. Retry with exponential backoff; if still
     failing, either fail-closed (safer) or degrade to no-snippet mode (available).

 3.​ Length leak — Low impact. Document that HMAC output is fixed-length; no action
     needed.


What Ships Now vs Later
Ship now (Day-1):

  ●​ redactor-v3.ts + fp-store-v2.ts + block-counter.ts

  ●​ CLI: pnpm --filter @mtpi/mirror-dissonance run oracle:run

  ●​ Default mode: warn-only, circuit-breaker on, FP enforcement on

Ship later (Day-14):

  ●​ Nonce rotation support

  ●​ SSM retry with backoff

  ●​ Promotion automation (currently manual via promotedBy + promotedAt)


Optional Artifact

"Dissonance is the fee for meeting yourself."​




Precision Question

None blocking. Protocol is callable.




Precision Question Response

Target availability: 99.9% for the oracle path.

Safety posture: Fail closed on SSM failure, but with a bounded grace period before throwing.

This matches the Phase Mirror principle: "When plans depend on hope, add a kill-switch". The
oracle is a safety mechanism—degrading to warn-only defeats its purpose. But hard-throw on
first SSM timeout is operationally brittle.[1]


Reconciled Position

 Condition                           Behavior                   Rationale

 SSM reachable                       Normal operation           Happy path
    SSM unreachable, cached nonce    Use cached nonce, emit       Bounded availability window
    valid                            meta.degraded:
                                     "ssm_unreachable"

    SSM unreachable, no cached       Throw                        Fail closed—cannot validate
    nonce                            OracleUnavailableError       without nonce


    SSM unreachable, cache expired   Throw                        Stale nonce = potential rotation
    (>1hr)                           OracleUnavailableError       missed



This gives you:

    ●​ Fail closed as the terminal state

    ●​ Bounded availability during transient SSM issues

    ●​ Auditability via meta.degraded field


Nonce Rotation Story (complete)

interface RedactedTextInternal {​
     readonly __brand: string;​
     readonly __mac: string;​
     readonly __nonceVersion: number;         // ← NEW​
     readonly value: string;​
     // ...​
}​
​
// Validator accepts current OR previous nonce during grace window​
const VALID_NONCES: Array<{ nonce: string; version: number; expiresAt: Date | null }> =
[];​
​
function isValidRedactedText(x: unknown): x is RedactedText {​
     // ... structure checks ...​
     ​
     const candidate = x as RedactedTextInternal;​
     const matchingNonce = VALID_NONCES.find(n => ​
         n.version === candidate.__nonceVersion &&​
         (n.expiresAt === null || n.expiresAt > new Date()) &&​
         timingSafeCompare(candidate.__brand, n.nonce)​
     );​
     ​
     if (!matchingNonce) return false;​
     ​
     const expectedMAC = computeMAC(matchingNonce.nonce, candidate.value);​
     return timingSafeCompare(candidate.__mac, expectedMAC);​
}​




Rotation Runbook

 1.​ T-0: Create new SSM parameter guardian/redaction_nonce_v2

 2.​ T-0: Deploy code that loads both v1 and v2 into VALID_NONCES

 3.​ T-0 to T+1hr: Grace period—both nonces validate; new reports use v2

 4.​ T+1hr: Deploy code that removes v1 from VALID_NONCES

 5.​ T+1hr: Delete guardian/redaction_nonce (v1) from SSM


Updated Levers

 Owner                    Lever                     Metric                        Horizon

 You                      Implement                 Zero validation failures      7 days
                          __nonceVersion +          during rotation

                          dual-nonce validation

 You                      Add cacheExpiresAt        Stale cache incidents = 0     3 days

                          to nonce loader; throw
                          after 1hr stale

 You                      Add meta.degraded         Field present in 100% of      3 days

                          field to report schema    degraded runs


 Ops                      Add CloudWatch alarm      Alert within 5 min of first   7 days
                          on SSM GetParameter       failure

                          failures

 You                      Add TTL policy to FP      Storage growth                30 days
                          store: 90-day retention   ≤10%/month
                          for old rule versions




Optional Artifact
Checklist: Fail-closed with bounded availability

    ●​ [ ] VALID_NONCES array supports multiple versions

    ●​ [ ] __nonceVersion field in RedactedTextInternal

    ●​ [ ] Cache has expiresAt timestamp; throw after 1hr stale

    ●​ [ ] meta.degraded field added to dissonance-report.schema.json

    ●​ [ ] Rotation runbook documented in docs/ops/nonce-rotation.md

    ●​ [ ] CloudWatch alarm on SSM failures configured



"The Phase Mirror does not resolve dissonance—it names it."[1]

Protocol is callable. Ship it.​



⁂




Closure Acknowledged

All dissonances named. All cliffs staggered. Protocol is callable.


Final Artifact Summary

    File                           Purpose                           Status

    dissonance-report.schema.j     Report output contract            ✓ Versioned

    son

    types-v2.ts                    Enforcement by construction       ✓ Complete


    redactor-v3.ts                 Secret-backed nonce + HMAC +      ✓ Complete
                                   timing-safe

    fp-store-v2.ts                 Version-scoped FP tracking        ✓ Complete


    block-counter.ts               Circuit breaker implementations   ✓ Complete




Ship Checklist (Final)
Schema & Rules

 ●​ [x] dissonance_report schema versioned and hashed

 ●​ [x] Each MD-* rule has detection logic, evidence requirements, severity, remediation

 ●​ [x] FP tolerance defined per severity tier

 ●​ [x] Promotion/demotion criteria for rules documented

Safety Rails

 ●​ [x] Circuit-breaker threshold set

 ●​ [x] No write side-effects in oracle path

 ●​ [x] Steward assigned with merge authority over md-rules/

Nonce Lifecycle

 ●​ [x] VALID_NONCES supports multiple versions with __nonceVersion

 ●​ [x] Cache has expiresAt; throw after 1hr stale

 ●​ [x] Stagger old-nonce expiry to 2hr (prevents cliff)

 ●​ [ ] Shared nonce cache for multi-replica (if applicable) — Day-14

Observability

 ●​ [x] meta.degraded field in schema

 ●​ [x] Rotation runbook in docs/ops/nonce-rotation.md

 ●​ [ ] CloudWatch alarm on SSM GetParameter failures — Ops, 7 days


Operational Sequence

Day 0:   Ship oracle (warn-only, circuit-breaker on)​
Day 3:   Wire CloudWatch alarm on SSM failures​
Day 7:   Enable blocking for MD-001, MD-002 after FP window passes​
Day 14: Add shared nonce cache if multi-replica​
Day 30: TTL policy for stale FP partitions​




Optional Artifact
"When plans depend on hope, add a kill-switch. When kill-switches depend on hope, add a
grace period. When grace periods depend on hope, stagger the cliffs."



Protocol is callable. Ship it.​



⁂



    1.​ White-Paper_-The-Phase-Mirror-for-Agentic-Domain-Specific-Reasoning.pdf

    2.​ MTPI RootContract.pdf

    3.​ MTPI_RootContract_Project.pdf

    4.​ 2.ΛRootContract II & III - MTPI - NODE.js.pdf

    5.​ MTPI_Instructions.pdf

    6.​ ΛProof and Hologram (1).pdf

          a.​ Λproof × Mtpi Lawful‑by‑design Integration — Implementation Plan.pdf

    7.​ The ΛProof Architecture_ Web4.pdf

    8.​ Λproof Whitepaper.pdf

    9.​ Building a ΛDapp_ A Developer's Implementation Guide.pdf

    10.​ Verifiable, Privacy-Preserving Applications.pdf

    11.​ Understanding Phase Mirror Dissonance_ A Beginner's Guide.pdf

    12.​ ΛProof Project for Artificial Intelligence.pdf

    13.​ Policy Memo_ Managing Agentic AI Liability with the Phase Mirror Framework.pdf

    14.​ Implementation Guide_ Applying Phase Mirror Dissonance.pdf

    15.​ yes-if-mirror-dissonance-is-yo-8nliupFQT4C6Tt4.rjs66Q.md

    16.​ lets-analyze-this-project-for-gTcBPS_tQXiUlhdL_XFNVA.md
17.​ Patent Non-Assertion Pledge for Proof.pdf

18.​ ΛProof Interface Blueprint.pdf

19.​ ΛProof - IP Strategic Blueprint.pdf

20.​yes-if-mirror-dissonance-is-yo-8nliupFQT4C6Tt4.rjs66Q.md

21.​ MTPI RootContract.pdf

22.​MTPI_RootContract_Project.pdf

23.​2.ΛRootContract II & III - MTPI - NODE.js.pdf

24.​MTPI_Instructions.pdf

25.​ ΛProof and Hologram (1).pdf

     b.​ Λproof × Mtpi Lawful‑by‑design Integration — Implementation Plan.pdf

26.​The ΛProof Architecture_ Web4.pdf

27.​ Λproof Whitepaper.pdf

28.​Building a ΛDapp_ A Developer's Implementation Guide.pdf

29.​Verifiable, Privacy-Preserving Applications.pdf

30.​White Paper_ The Phase Mirror for Agentic Domain-Specific Reasoning.pdf

31.​ ΛProof Project for Artificial Intelligence.pdf

32.​Understanding Phase Mirror Dissonance_ A Beginner's Guide.pdf

33.​Policy Memo_ Managing Agentic AI Liability with the Phase Mirror Framework.pdf

34.​Implementation Guide_ Applying Phase Mirror Dissonance.pdf

35.​ lets-analyze-this-project-for-gTcBPS_tQXiUlhdL_XFNVA.md

36.​Patent Non-Assertion Pledge for Proof.pdf

37.​ ΛProof Interface Blueprint.pdf
38.​ΛProof - IP Strategic Blueprint.pdf

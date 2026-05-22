---
slug: non-assertion-covenant-and-conformance-certification-plan-v1-1
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 02-implementations/q-calculator/Non-assertion Covenant And Conformance Certification
    Plan V1 (1).md
  last_synced: '2026-03-20T17:17:15.180758Z'
---

Public Non-Assertion Covenant and Conformance
Certification Plan
Version: 1.0
Status: Public Draft (template)
Note: This document is a template intended to express a trust-first posture (free use, anti-enclosure, non-
surveillance). It is not legal advice; have counsel review for your jurisdiction and patent portfolio.




1) Purpose and Principles
This document exists to:


     • Enable free, global use of the Covered Technology to advance sovereignty, anonymity, and non-
       surveillance.
     • Protect the ecosystem from enclosure (patent aggression, surveillance forks, trustwashing).
     • Provide a practical adoption engine via conformance testing and certification that makes trust
       measurable.

The core philosophy is simple: trust is the product. The technology is offered freely to maximize lawful
participation, minimize harm, and preserve user sovereignty.




2) Public Patent Non-Assertion + Defensive Termination Covenant
Clarification: This Covenant is separate from the Apache 2.0 license and does not impose conditions on
Apache-licensed use; it governs only patent non-assertion and certification mark usage.


2.1 Definitions

     • Covenantor: the person/entity publishing this Covenant.
     • Covered Technology: the specifications, reference implementations, interoperability profiles, and
       conformance tests designated by Covenantor (the Spec Suite).
     • Covered Patents: any patent claims owned or controlled by Covenantor that are necessarily
       infringed by implementing the Covered Technology as a Conformant Implementation.
     • Conformant Implementation: an implementation that (i) passes the published conformance test
       suite for the applicable profile(s), and (ii) does not include Surveillance Functionality.
     • Surveillance Functionality: collection, correlation, retention, or exfiltration of user identifiers,
       content, metadata, biometrics, location, device fingerprints, or interaction graphs beyond what is
       strictly required for Covered Technology, without explicit, informed, revocable user authorization
       and without a local-first/non-telemetry default.
     • Recipient: any person/entity making, using, selling, offering, or distributing a Conformant
       Implementation.




                                                     1
     • Patent Aggression: asserting any patent against Covenantor or any third party based on their
       making/using/distributing a Conformant Implementation, including threats, demand letters,
       injunction requests, ITC actions, or transferring/enabling a patent assertion entity to do so.
     • Enclosure Conduct: (a) Patent Aggression, (b) distributing/marketing a non-conformant or
       surveillance fork as conformant/certified, or (c) asserting claims intended to block Conformant
       Implementations.

2.2 Covenant / License Grant (Free Use)

Subject to Section 2.3, Covenantor irrevocably covenants not to sue any Recipient for infringement of
Covered Patents arising from making, using, selling, offering, or distributing a Conformant Implementation,
and grants Recipient a worldwide, royalty-free, non-exclusive license under Covered Patents to do the same.


2.3 Conditions (Trust-Preserving Use)

This Covenant applies only while Recipient:


1) Maintains conformance for the profile(s) it claims; 2) Does not include or enable Surveillance
Functionality; 3) Does not misrepresent certification status, interoperability, or privacy posture.


2.4 Defensive Termination (Automatic)

This Covenant and license automatically terminate for a Recipient (and its controlled affiliates) upon any
Enclosure Conduct by that Recipient. Termination is effective upon the earliest such act.


2.5 Cure / Reinstatement (Good-Faith Errors)

For unintentional conformance failures or accidental inclusion of disallowed telemetry, Covenantor may
(but is not required to) provide written notice and a 30-day cure period. If cured and independently
verified, Covenantor may reinstate coverage at its discretion. Patent Aggression is not curable.


2.6 Defensive Enforcement Scope

Upon termination, Covenantor may assert Covered Patents only against the terminated Recipient and
only to the extent reasonably necessary to stop Enclosure Conduct, surveillance forks, or patent aggression.


2.7 No Warranty; No Other Rights

Covered Technology is provided AS IS without warranties. No trademark rights are granted by this
Covenant. Certification marks and brand usage are governed separately (Section 3.6).


2.8 Updates and Versioning

Covenantor may publish updated versions of the Spec Suite and this Covenant for future coverage. A
Recipient remains protected under the version in effect at the time it first relied upon it for a given
Conformant Implementation, unless terminated under Section 2.4.




                                                     2
3) Conformance + Certification Plan (Trust Mark Adoption Engine)

3.1 Goal

Provide a measurable path for implementers (including banks, governments, enterprises, and open-source
teams) to adopt the technology while preserving:


     • Non-surveillance defaults
     • User sovereignty and anonymity
     • Verifiable lawfulness-by-design
     • Interoperability across independent implementations

3.2 Profiles (What “Conformant” Means)

Define a small set of profiles that implementers can target:


1) Core Profile: lawful state-transition governance + deterministic enforcement semantics. 2) Privacy
Profile: local-first behavior, data minimization, non-telemetry defaults. 3) Integrity Profile: anti-replay,
canonical commitments/fingerprints, deterministic trace schema. 4) Regulated Profiles (optional):
domain-specific operational constraints (e.g., finance/health) that tighten requirements without introducing
surveillance.


Each profile includes: - Normative requirements (MUST/SHOULD/MAY) - Test vectors and expected outputs
- Security & privacy invariants (fail-closed behavior; suppression on predicate failure)


3.3 Conformance Test Suite (What Gets Tested)

A conformance harness should verify:


A) Governance and Stability Predicates - Predicate computation is correct and deterministic - Drift/
coherence/stability checks enforce required thresholds - Fail/Pass semantics are consistent across runs and
implementations


B) Remediation and Enforcement - Deterministic nonexpansive remediation actions (e.g., project/freeze/
rollback) - Rollback behavior ties to an authenticated/committed lawful snapshot - No “continue anyway”
path exists under predicate failure


C) Emission Gating (Silent-Path) - Outputs/actions are suppressed/nullified when predicates fail - No
information leakage via side channels in the default configuration


D) Commitments, Fingerprints, and Anti-Replay - Canonical ordering and hashing of trace fields - Non-
collision fingerprinting for snapshots/events - Replay protection checks (e.g., rejecting reused proof
identifiers)


E) Non-Surveillance Verification - Telemetry defaults OFF - Zero unexpected network egress from the
reference runtime mode - Explicit, revocable consent for any optional diagnostics




                                                      3
F) Supply Chain Integrity (Recommended) - Reproducible builds - SBOM publication - Signed releases and
provenance metadata


3.4 Certification Levels (Procurement-Friendly)

     • Level 0 — Self-Attested: implementer runs tests; publishes conformance report + SBOM.
     • Level 1 — Verified: automated CI validates test pass + reproducible build + egress checks.
     • Level 2 — Certified: independent auditor validates Level 1 + threat model review.
     • Level 3 — Regulated Certified: adds operational controls (key mgmt, incident response, etc.).

3.5 Public Registry (Transparency Without Surveillance)

Maintain a public registry listing: - Implementation name and version - Profiles passed and certification level
- Build hash / artifact fingerprint - Test report references (redacted where necessary) - Issue history,
renewals, and revocations


The registry should contain no user data and no telemetry derived from end users.


3.6 Trust Mark (Certification Trademark)

Create a certification mark (e.g., “Certified Lawful Implementation”) that can only be used by Level 2/3
implementations.


Rules: - Misuse of the mark triggers revocation and may trigger Covenant termination (Section 2.4). -
Publicly publish mark usage guidelines and enforcement policy.


3.7 Revocation, Appeals, and Incident Response

     • Revocation triggers: surveillance functionality, misrepresentation, repeated failure to maintain
       conformance, refusal to cure.
     • Appeals: time-bound technical review by a governance committee.
     • Security response: coordinated disclosure process; registry updates; expedited re-certification path.

3.8 Rollout Plan (Practical Sequence)

1) Publish Spec Suite v1 with Core + Privacy profiles. 2) Release conformance harness + reference vectors.
3) Stand up registry + Level 0/1 automation. 4) Recruit independent auditors for Level 2. 5) Launch
certification mark + a procurement-ready “Trust Pack.”




4) How the Covenant and Certification Work Together
     • Covenant provides the legal shield: free use for conformant, non-surveillance implementations;
       termination for enclosure or aggression.
     • Conformance + Certification provides the technical shield: measurable compliance and a public
       trust signal.




                                                      4
      • Together they create an ecosystem where trust is the incentive, adoption is simplified, and
        surveillance forks lose legitimacy.




5) Publication and Contact
      • Spec Suite location: [insert link]
      • Conformance harness location: [insert link]
      • Registry: [insert link]
      • Security contact: [insert email]
      • Certification inquiries: [insert email]




6) Statecraft Specification (Protocol-State)
This section defines a protocol-state: a lawful-by-design order that can be adopted by individuals and
institutions without requiring surveillance or trust in a central operator. It is written to be both poetic
(purpose and ethos) and operational (rules, invariants, and verifiable procedures).


6.1 Preamble (Purpose)

We build a civil substrate for a world that cannot be trusted.


Not a kingdom of secrets, but a commons of proofs. Not a regime of observation, but a society of consent.
Not governance by power, but governance by lawfulness.


The purpose of this protocol-state is to:


      • Protect sovereignty: the individual is not a product.
      • Preserve anonymity: identity is a capability, not a dossier.
      • Honor silence: absence is a right; refusal is a valid state.
      • Prevent harm: the system fails closed rather than leak.
      • Enable trust: verification is mathematical, not institutional.

6.2 Rights (Sovereignty, Anonymity, Silence)

Rights are implemented as invariants. If an invariant cannot be proven, the system does not act.


R1 — Sovereignty

Poetic form: You are not owned. You are not indexed. You are not harvested.


Operational guarantees: - Local-first operation by default; no required cloud dependency. - Consent is
explicit, informed, revocable, and scoped. - Data minimization: collect only what is strictly required to
perform the requested operation.




                                                        5
Invariant: No state transition may expand disclosure scope without an explicit consent artifact.


R2 — Anonymity

Poetic form: You may pass through the door without revealing the key.


Operational guarantees: - Prove eligibility/authorization via cryptographic assertions (e.g., commitments /
zero-knowledge proofs / signatures) without revealing identifying attributes. - Credentials are selectively
disclosed; correlation is discouraged by design.


Invariant: Any verification step must accept a privacy-preserving proof path.


R3 — Silence

Poetic form: Refusal is lawful. Absence is not guilt.


Operational guarantees: - The system provides a silent path that suppresses emissions/outputs when
predicates fail or when consent is absent. - The system may “do nothing” as a first-class outcome.


Invariant: When lawfulness cannot be established, the system MUST fail closed (silence over leakage).


R4 — Non-Surveillance

Poetic form: Trust does not require watching.


Operational guarantees: - Telemetry OFF by default. - No correlation graphs, device fingerprinting, or
hidden identifiers. - Audits rely on commitments, proofs, and conformance—not user monitoring.


Invariant: No unconsented persistent identifiers may be emitted in default mode.


R5 — Due Process

Poetic form: Power must explain itself.


Operational guarantees: - Any adverse decision (deny, freeze, rollback, revoke) produces a reason code
and a verifiable decision artifact. - Appeals exist and are time-bounded.


Invariant: A denial must be explainable without exposing private witness data.


6.3 Powers (What the System Is Allowed to Do)

The protocol-state is intentionally limited. It is not a general ruler; it is an enforcement substrate.


P1 — Verify

The system MAY verify lawfulness predicates and proofs for requested operations.




                                                        6
P2 — Permit or Deny

The system MAY return allow/deny verdicts for protected actions based on verified predicates.


P3 — Remediate

The system MAY execute deterministic remediation actions when predicates fail: - Project to a feasible set -
Freeze an update or action - Rollback to a last lawful snapshot


P4 — Commit and Record

The system MAY emit canonical commitments (hashes/fingerprints) and minimal audit records that do not
expose user data.


P5 — Certify Implementations

The system MAY certify implementations via conformance testing and registry listing.


Prohibited Powers

The system MUST NOT: - Require surveillance as a condition of access. - Expand disclosure scope without
consent. - Emit personal identifiers by default. - Make irreversible punitive actions without due process.


6.4 Due Process (Tribunal / Disputes)

When math cannot fully resolve ambiguity (edge cases, conflicting attestations, contested evidence),
disputes enter a bounded tribunal process.


D1 — Jurisdiction

A tribunal is invoked only when: - two lawful proofs conflict, - a party alleges nonconformance or
misrepresentation, - a certification suspension/revocation is contested, - a remediation action is disputed as
incorrect.


D2 — Evidence

Evidence is submitted as artifacts, not personal data: - commitments (hashes / fingerprints) - conformance
reports - signed statements - ZK proof transcripts or verification outputs - reproducible build artifacts and
SBOMs


Rule: If evidence requires raw user data to be persuasive, the process is flawed; reframe the evidence.


D3 — Burden and Standard

     • Burden is on the claimant to show a rule violation.
     • Standard is “verifiable by independent reproduction,” whenever possible.




                                                      7
D4 — Outcomes

Tribunal outcomes are bounded to: - uphold/overturn a denial - require re-test/re-audit - suspend/revoke
certification - publish a clarification or patch requirement


D5 — Appeals

     • A single appeal is permitted within a defined window.
     • The final decision must publish a rationale without revealing private witness data.

6.5 Enforcement (Gates, Remediation, and Lawful Motion)

Enforcement is where ethos becomes physics.


E1 — Gates

Before protected actions, the system evaluates predicates such as: - drift/stability bounds - coherence/
consistency checks - replay protection - consent scope and authorization


Gate rule: if any required predicate fails, the gate returns DENY and enters the silent path.


E2 — Silent Path (Fail-Closed)

On DENY or uncertainty: - suppress outputs/actions - emit only minimal reason codes and commitments (no
private witness) - optionally require re-anchoring or re-attestation


E3 — Deterministic Remediation

When remediation is allowed by policy: - Project: map state to the nearest feasible state under defined
rules - Freeze: halt updates and require explicit re-authorization - Rollback: restore last lawful snapshot
(identified by a prior commitment)


Remediation MUST be deterministic given the same inputs and policy version.


E4 — Anti-Replay and Non-Collision Commitments

     • Every protected transition produces a canonical commitment over an ordered tuple of trace fields.
     • Reuse of proof identifiers (or replay tokens) is rejected.

E5 — Minimal Audit

Audit is supported by: - commitments, not raw data - conformance reports, not telemetry - proofs, not
dossiers


6.6 Trust Marks (How Outsiders Verify)

Outsiders (banks, governments, enterprises, citizens) should not be asked to “trust us.” They should verify:




                                                      8
T1 — Conformance as the Basis of Trust

Trust is anchored in: - public profiles (what conformance means) - test harnesses (how conformance is
measured) - reproducible evidence artifacts (how results are verified)


T2 — Certification Mark

A certification mark (“Certified Lawful Implementation”) is the public signal.


     • Only Level 2/3 implementations may display the mark.
     • The registry is the source of truth for certified versions and build hashes.
     • Misuse triggers revocation and may trigger covenant termination.

T3 — Procurement-Ready Verification

Institutions can adopt without surveillance by checking: - registry entry (status, profiles, certificate ID) -
conformance report signatures - build hash matches certified artifacts - incident history and renewals


T4 — The Social Contract

The protocol-state earns legitimacy by: - being transparent in rules - silent in the absence of lawfulness -
measurable in conformance - restrained in power




Appendix A — CONFORMANCE.md (Draft)
       This appendix is a standalone draft for a repository file named CONFORMANCE.md .



Conformance Profiles and Test Rules
Version: 1.0
Status: Draft


1) Purpose
This document defines the conformance profiles, normative requirements, and test rules for
implementations of the Spec Suite. Conformance provides a measurable basis for interoperability and for
use of the certification mark.


2) Scope
Conformance applies to any implementation that claims compatibility with one or more profiles defined
below, including reference implementations and independent implementations.




                                                       9
3) Normative Language
The key words MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are to be interpreted as normative
requirements.


4) Profiles
Implementations MAY claim any subset of profiles. Each profile has its own tests and required evidence
artifacts.


4.1 Core Profile

Goal: lawful-by-design state transition governance with deterministic enforcement semantics.


Core requirements (non-exhaustive): - The implementation MUST evaluate the required governance
predicates for each protected transition. - The implementation MUST fail closed when predicate evaluation
fails. - The implementation MUST execute deterministic remediation actions as specified (e.g., project/
freeze/rollback) and record a deterministic remediation outcome. - The implementation MUST produce a
canonical commitment/fingerprint for each protected transition event (see Integrity Profile for details).


4.2 Privacy Profile

Goal: sovereignty-preserving operation with non-surveillance defaults.


Privacy requirements (non-exhaustive): - Default operation MUST be local-first and non-telemetry by
default. - The implementation MUST NOT transmit user identifiers, content, metadata, device fingerprints,
location, or interaction graphs except as strictly required for conformance. - Any optional diagnostics MUST
require explicit, informed, revocable user authorization and MUST be disabled by default.


4.3 Integrity Profile

Goal: anti-replay, canonical commitments, deterministic trace schemas, and verifiable audit hooks.


Integrity requirements (non-exhaustive): - The implementation MUST compute commitments over a
canonical, ordered tuple of trace fields. - The implementation MUST implement replay protection such that
reused proof identifiers (or equivalent replay tokens) are rejected. - The implementation MUST expose a
deterministic “trace export” artifact that can be re-verified from published commitments.


4.4 Regulated Profiles (Optional)

Goal: procurement-ready operational constraints for regulated deployments without introducing
surveillance.


Examples (non-binding): - Finance Profile: stronger key management and audit retention controls;
restricted logging formats. - Health Profile: stricter consent boundaries; compartmentalized evidence
references.




                                                    10
Regulated profiles MUST preserve Privacy Profile guarantees and MUST NOT mandate surveillance.


5) Conformance Test Suite Structure
The conformance harness is organized into categories. Each profile defines which categories are required.


5.1 Predicate Evaluation

Tests validate correctness and determinism of required predicates, including: - Pass/fail semantics under
normal inputs - Boundary conditions near thresholds - Negative tests (invalid/malformed states)


5.2 Enforcement and Remediation

Tests validate that on predicate failure the implementation: - Fails closed - Executes deterministic
remediation (project/freeze/rollback) per the profile - Produces a deterministic remediation outcome artifact


5.3 Emission Gating (Silent-Path)

Tests validate that when predicates fail: - Action tensors/outputs are suppressed or nullified - No “partial
output” leaks occur - Default behavior remains suppressive unless explicitly and permissibly configured


5.4 Commitments, Fingerprints, and Trace Schema

Tests validate: - Canonical ordering of trace fields - Commitment computation over the exact required tuple
- Verification of the commitment from a reconstructed trace


5.5 Anti-Replay

Tests validate: - Reuse of replay tokens is rejected - Mirrored checks (if applicable) are consistent across
components


5.6 Non-Surveillance / Egress Controls (Privacy Profile)

Tests validate: - Telemetry defaults off - No unexpected outbound network connections in default mode - If
any network use is required, it is limited to conformance-required endpoints and carries no prohibited
payloads


5.7 Supply Chain Evidence (Recommended)

Where applicable, tests validate: - Reproducible build or deterministic build metadata - SBOM generation -
Signed artifacts and provenance metadata


6) Required Evidence Artifacts
An implementation claiming conformance MUST produce the following artifacts per test run:




                                                     11
1) Conformance Report (machine-readable JSON) containing: - Implementation name, version, build hash -
Profiles claimed - Test suite version and harness commit hash - Pass/fail summary + per-test results 2) Trace
Samples (redacted and non-user-specific) sufficient to verify canonical commitment rules. 3) SBOM
(recommended; required for Level 1+ certification).


7) How to Run Conformance Tests (Example)
Implementations SHOULD provide a command that can be executed in CI:


     • conformance test --profile core
     • conformance test --profile privacy
     • conformance test --profile integrity

The harness SHOULD exit non-zero on any failure.


8) Registry Submission
To be listed in the public registry, submit: - Conformance Report JSON - Build hash / artifact fingerprint -
Optional SBOM


Registry records MUST contain no user data and MUST NOT require telemetry.


9) Versioning, Compatibility, and Deprecation
     • Profiles and tests are versioned.
     • A profile version MAY deprecate older rules with a defined grace period.
     • Implementations MUST clearly state which profile version(s) they satisfy.


10) Security and Privacy Notes
Conformance does not imply “secure against all threats.” It certifies adherence to profile requirements,
including non-surveillance defaults where applicable. Security assessments and audits are part of
certification levels.




Appendix B — CERTIFICATION-MARK.md (Draft)
       This appendix is a standalone draft for a repository file named CERTIFICATION-MARK.md .



Certification Mark Policy
Version: 1.0
Status: Draft




                                                     12
1) Purpose
This policy governs use of the certification mark (the Mark) indicating that an implementation is certified as
conformant and non-surveillance by default. The Mark is designed to prevent “trustwashing” and protect
users and adopters.


2) Definitions
      • Mark: the certification trademark / trust mark designated by the program (e.g., “Certified Lawful
        Implementation”).
      • Certified Implementation: an implementation listed in the public registry at certification Level 2 or
        Level 3.
      • Registrant: the entity controlling the registry and certification program.
      • Certificate Term: the time period a certification remains valid before renewal is required.


3) Eligibility
To use the Mark, an implementation MUST: - Pass conformance tests for the claimed profile(s) (see
 CONFORMANCE.md ). - Meet certification Level 2 or Level 3 requirements. - Maintain non-surveillance
defaults consistent with the Privacy Profile. - Remain listed in the registry as Active (not Suspended/
Revoked/Expired).


4) Permitted Uses
A Certified Implementation MAY: - Display the Mark on websites, documentation, packaging, and
procurement materials only for the certified version(s). - State: “This implementation is certified for profiles:
[list], Level: [2/3], Certificate ID: [id].” - Link to the public registry entry.


5) Prohibited Uses
An implementation MUST NOT: - Use the Mark for non-certified versions, forks, builds, or configurations. -
Use the Mark in a way that implies endorsement beyond certification (e.g., “approved,” “government-grade,”
“unbreakable”). - Modify, stylize, or combine the Mark with other marks in confusing ways. - Use the Mark to
market a surveillance-enabled variant or telemetry-enabled-by-default build. - Use the Mark as part of a
product name in a way that suggests the Mark is the product brand.


6) Mark Presentation Rules
      • The Mark MUST be displayed exactly as provided by the Registrant (logo files, colors, spacing, and
        minimum size).
      • Where feasible, include the Certificate ID adjacent to the Mark.
      • Include a link or reference to the registry entry.




                                                       13
7) Certification Levels (Summary)
     • Level 2 — Certified: independent auditor validates Level 1 requirements + threat model review.
     • Level 3 — Regulated Certified: adds operational controls (key management, incident response,
       compliance artifacts).


8) Suspension and Revocation

8.1 Suspension Triggers

Registrant MAY suspend the Mark pending investigation if: - A credible report indicates conformance failure
or surveillance functionality. - The implementer refuses to provide requested verification artifacts. - A
material security incident suggests nonconformance with required invariants.


8.2 Revocation Triggers

Registrant MUST revoke (or may revoke, as specified by program rules) if: - Surveillance functionality is
discovered in a certified build or default configuration. - Misrepresentation occurs (false claims of
certification, altered test results, misleading marketing). - Conformance failures are not cured within the
cure window (if offered). - The implementer engages in patent aggression or enclosure conduct as defined
by the Covenant.


8.3 Public Notice

Suspensions and revocations MUST be recorded in the registry with: - Effective date - Reason category
(without exposing user data) - Remediation steps (if any)


9) Cure, Re-Certification, and Renewal
     • For good-faith issues, Registrant MAY offer a cure period (e.g., 30 days) to restore compliance.
     • After cure, the implementer MUST re-run conformance tests and MAY be required to undergo an
       audit.
     • Certifications expire at the end of the Certificate Term unless renewed.


10) Appeals
A suspended or revoked implementer MAY appeal: - Appeals MUST be filed within a stated window (e.g., 14
days). - Appeals are reviewed by a technical committee under published procedures. - A final decision and
rationale MUST be recorded in the registry.


11) Relationship to Licenses and the Patent Covenant
     • Use of the Mark is governed by this policy and the registry rules.
     • This policy does not change software license terms.
     • Patent non-assertion and defensive termination are governed by the separate Covenant.




                                                    14
12) Contact
     • Certification inquiries: [insert email]
     • Security reports: [insert email]
     • Registry: [insert link]

End of document.




                                                 15

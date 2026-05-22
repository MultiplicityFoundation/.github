---
slug: how-trust-is-measured
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 02-implementations/q-calculator/How Trust is Measured.md
  last_synced: '2026-03-20T17:17:15.296153Z'
---

How Trust is Measured: A Step-by-Step
Guide to Conformance and Certification
Introduction: From Promises to Proof

The system for building this technology begins with a poetic and powerful declaration of
purpose: "We build a civil substrate for a world that cannot be trusted." This statement sets the
stage for a core philosophy that is both simple and profound: Trust is the product. But in a
digital world filled with opaque systems and empty promises, how is that trust actually earned
and proven?

This document walks you through the practical, step-by-step process of how this technology is
tested and certified to prove it is trustworthy. It moves beyond simple promises to verifiable
proof. This system of rules and enforcement can be understood as a kind of "constitutional
order," ensuring that every component behaves predictably and lawfully.

This order is built upon two foundational pillars that work together to create a trustworthy
ecosystem.

1. The Two Shields of a Trustworthy System

To ensure trust is both legally protected and technically verifiable, the system uses two distinct
mechanisms that function as complementary shields for users and developers.



 The Legal Shield (The Promise)                      The Technical Shield (The Proof)



 The Public Patent Non-Assertion Covenant.           The Conformance & Certification Plan.
 Grants the right to freely use the technology, on   Provides measurable, technical proof that
 the condition that users do not engage in patent    an implementation is compliant and
 aggression or create surveillance-based forks.      creates a public signal of trust.



With the legal promise established, we now examine the technical shield that provides the
verifiable proof of that promise, beginning with conformance.

2. Step 1 - Conformance: Following the Rulebook
In this constitutional order, Conformance is the first step: proving an implementation follows the
"letter of the law." In simple terms, it means that a piece of software (an "implementation") has
successfully passed a published set of automated tests, proving that it correctly follows the rules
for a specific "profile."

Profiles are like different sets of rules that an implementation can choose to follow, depending
on its intended purpose. An implementation can be tested against one or more profiles to prove
it meets specific goals.



 Profile Name    Core Goal (in simple terms)



 Core Profile    To ensure the system correctly follows the rules for lawful operation and
                 predictable enforcement.



 Privacy         To ensure the system protects user sovereignty with "local-first" behavior and
 Profile         has no default spying (telemetry).



 Integrity       To ensure the system is protected against replay attacks and that its actions
 Profile         can be verified through "canonical commitments/fingerprints."



What Gets Tested?

The conformance test suite examines several key areas to ensure the software behaves exactly
as promised. These tests translate technical rules into tangible benefits for the user.

   ●​ Governance and Stability: This checks if the system's core rules are calculated
      correctly and consistently, ensuring predictable behavior.
   ●​ Enforcement Actions: This verifies the system correctly performs safe actions like
      "freeze" or "rollback" when rules fail, preventing harmful outcomes.
   ●​ Staying Silent When It Fails: Tests ensure that if a required check fails, the system
      stops and does not leak information or perform partial actions (this is called the
      "Silent-Path").
   ●​ Anti-Replay and Fingerprinting: This confirms the system can't be tricked by replaying
      old data and that every event has a unique, verifiable digital fingerprint.
   ●​ Non-Surveillance Verification: Tests explicitly verify that all telemetry (data collection)
      is turned OFF by default and that there is no unexpected network communication.
   ●​ Supply Chain Integrity: Recommends that tests verify the software was built in a
      reproducible way and that a Software Bill of Materials (SBOM) is published, providing
      transparency into its components.

Once an implementation successfully passes these conformance tests, the next step is to get
the results formally certified.

3. Step 2 - Certification: Getting the Stamp of Approval

Certification is the next step, acting like a "judicial review" that formally verifies the
conformance results. Its primary purpose is to create a "procurement-friendly" system that large,
risk-averse organizations like banks and governments can easily adopt because it provides a
clear, measurable signal of trust and reduces their risk.

There are four distinct Certification Levels, each representing a higher degree of verification.

   1.​ Level 0 — Self-Attested: The developer runs the tests themselves and publishes a
       conformance report and a Software Bill of Materials (SBOM).
   2.​ Level 1 — Verified: An automated system validates that the tests pass, verifies the
       build is reproducible, and checks for unexpected network communications
       (egress checks).
   3.​ Level 2 — Certified: An independent, third-party auditor validates the Level 1 results
       and performs a deeper review, including a formal threat model analysis.
   4.​ Level 3 — Regulated Certified: This adds domain-specific operational controls required
       for regulated industries like finance or healthcare.

After an implementation achieves a certain certification level, the results must be made visible to
the public.

4. Step 3 - Making Trust Visible: The Public Signals

For a system of trust to be useful, it must be transparent and easy for anyone to verify. This is
achieved through two key public signals.

The Public Registry

This is the system's official "public record"—a transparent list of all implementations that have
successfully passed testing. It serves as the single source of truth for the status of any piece of
software claiming to be compliant. The registry contains key information, including:

   ●​   The implementation's name and version
   ●​   The specific profiles it passed
   ●​   Its current certification level
   ●​   Build hash / artifact fingerprint
   ●​   Test report references
   ●​ Issue history, renewals, and any revocations

Crucially, the registry contains no user data or telemetry derived from end users.

The Trust Mark

The Trust Mark is a special certification logo (e.g., "Certified Lawful Implementation") that acts
as a quick, public signal of a high level of trust. This mark is carefully controlled to prevent
misuse. According to the rules, only implementations that achieve Level 2 or Level 3
certification are allowed to use this mark.

Together, the Public Registry and the Trust Mark make it easy for adopters to identify legitimate
implementations, effectively marginalizing non-compliant or surveillance-based forks.

5. Keeping the System Honest: Rules and Consequences

Certification is not a one-time event; it is a status that must be continuously maintained. An
implementation's certification can be revoked for failing to uphold the standards.

Key reasons for revocation include:

   ●​   Discovering hidden surveillance functionality in a certified version.
   ●​   Misrepresenting the certification status or making false claims.
   ●​   Repeatedly failing to maintain conformance with the technical rules.
   ●​   Engaging in patent aggression or creating a surveillance fork of the technology
        (known as "enclosure conduct").

To ensure fairness, the system includes a time-bound technical review process that allows
developers to appeal a revocation decision.

This combination of rules, testing, and consequences creates a robust and reliable ecosystem.

Conclusion: An Ecosystem Built on Verifiable Trust

This entire process demonstrates how a legal shield (the Covenant) and a technical shield
(Conformance & Certification) work together to create a system where trust is earned, not just
promised.

The step-by-step method of conformance testing, followed by tiered certification levels, a
transparent public registry, and a protected trust mark, creates a "legitimacy ladder." This
ladder allows the technology to be adopted by risk-averse institutions. This makes lawfulness
boringly testable and auditable without surveillance.

This system is designed to create an ecosystem where trust is the incentive, adoption is
simplified, and surveillance forks lose legitimacy.

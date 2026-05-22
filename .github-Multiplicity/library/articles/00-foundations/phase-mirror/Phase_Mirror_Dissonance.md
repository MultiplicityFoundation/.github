---
slug: phase-mirror-dissonance
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 00-foundations/phase-mirror/Phase_Mirror_Dissonance.md
  last_synced: '2026-03-20T17:17:22.167536Z'
---

              Defensive Publication:
      Phase Mirror Dissonance Methodology
  for Agentic AI Governance and Organizational
                   Diagnostics
                               Ryan O. Van Gelder
                          Crown City, Ohio, United States
                      Publication Date: January 28, 2026


Document Type: Technical Disclosure / Defensive Publication
Version: 1.0
Publication Date: January 28, 2026
License: CC BY 4.0 (Creative Commons Attribution 4.0 International)
Keywords: Phase Mirror Dissonance, Agentic AI Governance, Organizational Diag-
nostics, Enterprise AI Risk Management, Governance Mechanisms, Liability Architec-
ture, Callable Protocol, Mirror Dissonance Oracle
Subject Classification: Computer Science / Artificial Intelligence / Governance; Or-
ganizational Theory; Risk Management
DOI: [10.5281/zenodo.18407313]
Purpose: Establishment of prior art to prevent patent claims on the Phase Mirror
Dissonance methodology and its applications

                                          Abstract
    This defensive publication establishes comprehensive prior art for the Phase Mirror
Dissonance (PMD) methodology, a novel diagnostic framework for surfacing productive
contradictions in organizational systems, with particular application to agentic AI gover-
nance. The PMD methodology comprises three integrated components: (1) Mirror – objec-
tive reflection of stated claims without endorsement, (2) Dissonance – systematic identifi-
cation of structural tensions and missing bindings, and (3) Phase – generation of concrete,
testable interventions with explicit ownership and metrics.
    This publication documents the complete technical specification, operational framework,
implementation patterns, and novel applications of PMD, including: the five-step operat-
ing loop (Extract-Map-Rank-Produce-Question), standardized output templates (Standard,
Rapid Triage, Board Packet), binding artifact heuristics (replacing “align” with artifact, “col-
laborate” with binding), and the callable Mirror Dissonance Oracle protocol for automated
governance enforcement.
    Key innovations disclosed include: (1) the Compliance-Accuracy Tradeoff framework re-
quiring explicit policy encoding, (2) tiered governance models distinguishing human-in-the-
loop from human-on-exception oversight, (3) the dissonance report schema with provenance
tracking and false-positive calibration, (4) redaction-by-capability mechanisms using HMAC
integrity binding, (5) circuit-breaker patterns for blast-radius management, (6) a normative
implementation profile ensuring deterministic outputs across independent implementations,
and (7) a conformance test suite with seven test vectors providing cryptographic hash veri-
fication of interoperability.



                                               1
Defensive Publication: Phase Mirror Dissonance                                      January 28, 2026


          This disclosure includes a complete normative implementation profile (Appendix C) spec-
      ifying UTF-8 encoding, JSON serialization, timestamp formats, and hash computation re-
      quirements to enable verifiable conformance testing. Seven test vectors with computed SHA-
      256 hashes are provided to verify independent implementations produce byte-identical out-
      puts.


Contents
1 Introduction and Purpose                                                                          5
  1.1 Defensive Publication Objectives . . . . . . . . . . . . . . . . . . . . . . . . . . .        5
  1.2 Scope of Disclosure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     5
  1.3 Disclosure Boundaries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       5
       1.3.1 Disclosed Elements (Public Domain) . . . . . . . . . . . . . . . . . . . . .           5
       1.3.2 Retained Elements (Not Disclosed) . . . . . . . . . . . . . . . . . . . . . .          6
       1.3.3 Non-Claimed Elements (Out of Scope) . . . . . . . . . . . . . . . . . . . .            6
       1.3.4 Competitive Moat Protection . . . . . . . . . . . . . . . . . . . . . . . . .          7
  1.4 Publication Strategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      7
  1.5 Legal Framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       8

2 Background and Motivation                                                                         8
  2.1 The Governance Challenge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        8
  2.2 Prior Art Landscape . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       8
  2.3 Novel Contributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       9

3 Core Methodology: Phase Mirror Dissonance                                                          9
  3.1 Conceptual Foundation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        9
      3.1.1 Mirror: Objective Reflection . . . . . . . . . . . . . . . . . . . . . . . . . .         9
      3.1.2 Dissonance: Tension Identification . . . . . . . . . . . . . . . . . . . . . .          10
      3.1.3 Phase: Concrete Interventions . . . . . . . . . . . . . . . . . . . . . . . . .         10
  3.2 The Five-Step Operating Loop . . . . . . . . . . . . . . . . . . . . . . . . . . . .          11
      3.2.1 Step 1: Extract . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       11
      3.2.2 Step 2: Map Tensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          12
      3.2.3 Step 3: Rank Tensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         13
      3.2.4 Step 4: Produce Output Blocks . . . . . . . . . . . . . . . . . . . . . . . .           14
      3.2.5 Step 5: Pose Precision Question . . . . . . . . . . . . . . . . . . . . . . . .         15
  3.3 Standardized Output Templates . . . . . . . . . . . . . . . . . . . . . . . . . . . .         15
      3.3.1 Template A: Standard Analysis . . . . . . . . . . . . . . . . . . . . . . . .           15
      3.3.2 Template B: Rapid Triage . . . . . . . . . . . . . . . . . . . . . . . . . . .          16
      3.3.3 Template C: Board Packet . . . . . . . . . . . . . . . . . . . . . . . . . . .          16

4 Application Domain: Agentic AI Governance                                                         17
  4.1 The Autonomy-Governance Tension . . . . . . . . . . . . . . . . . . . . . . . . .             17
  4.2 Critical Dissonances in Agentic AI Systems . . . . . . . . . . . . . . . . . . . . .          17
      4.2.1 Dissonance 1: Reasoning vs. Data Hygiene . . . . . . . . . . . . . . . . .              17
      4.2.2 Dissonance 2: Domain-Specific Precision vs. Platform Scalability . . . . .              17
      4.2.3 Dissonance 3: Autonomy vs. Deterministic Success . . . . . . . . . . . . .              18
      4.2.4 Dissonance 4: Probabilistic Outputs vs. Binary Compliance . . . . . . . .               18
      4.2.5 Dissonance 5: Agency vs. Prediction (Liability Shift) . . . . . . . . . . . .           18
      4.2.6 Dissonance 6: No-Code Interfaces vs. Causal Expertise . . . . . . . . . . .             18
      4.2.7 Dissonance 7: Transparency Rhetoric vs. Proprietary Infrastructure . . .                19


                                            Page 2 of 48
Defensive Publication: Phase Mirror Dissonance                                     January 28, 2026


   4.3   The Compliance-Accuracy Tradeoff . . . . . . . . . . . . . . . . . . . . . . . . . .      19

5 The Mirror Dissonance Oracle: Callable Protocol                                                  20
  5.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   20
  5.2 Architectural Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     20
  5.3 Dissonance Report Schema . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         20
  5.4 Conformance Verification . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       22
       5.4.1 Test Vector Coverage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      22
       5.4.2 Test Vector Format . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      22
       5.4.3 Validation Procedure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      23
       5.4.4 Accessing Test Vectors . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      23
  5.5 Rule Registry Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      23
  5.6 False-Positive Calibration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     24
  5.7 Circuit-Breaker Pattern . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      25
  5.8 Boundary Clarification: Pattern vs. Credential . . . . . . . . . . . . . . . . . . .         26
       5.8.1 What is Disclosed (Public Domain) . . . . . . . . . . . . . . . . . . . . . .         26
       5.8.2 What is Retained (Operational Security) . . . . . . . . . . . . . . . . . . .         26
       5.8.3 Rationale . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     27
       5.8.4 Guidance for Independent Implementations . . . . . . . . . . . . . . . . .            27
  5.9 Redaction-by-Capability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      27
  5.10 Integration Patterns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    28

6 Implementation Guidelines                                                                        29
  6.1 Deployment Patterns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      29
      6.1.1 Centralized Oracle Service . . . . . . . . . . . . . . . . . . . . . . . . . . .       29
      6.1.2 Embedded CLI Tool . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          30
      6.1.3 Hybrid Model (Recommended) . . . . . . . . . . . . . . . . . . . . . . . .             30
  6.2 Operational Runbooks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       31
      6.2.1 Nonce Rotation Procedure . . . . . . . . . . . . . . . . . . . . . . . . . . .         31
      6.2.2 Circuit-Breaker Response . . . . . . . . . . . . . . . . . . . . . . . . . . .         31
      6.2.3 False-Positive Feedback Loop . . . . . . . . . . . . . . . . . . . . . . . . .         31
  6.3 Governance Framework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         32
      6.3.1 Rule Stewardship . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       32
      6.3.2 Promotion Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       32
      6.3.3 Demotion Triggers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        32

7 Extensions and Future Work                                                                       33
  7.1 Hierarchical PMD . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       33
  7.2 Multi-Stakeholder Orchestration . . . . . . . . . . . . . . . . . . . . . . . . . . .        33
  7.3 Causal PMD for Organizational Dynamics . . . . . . . . . . . . . . . . . . . . . .           33
  7.4 Integration with Formal Verification . . . . . . . . . . . . . . . . . . . . . . . . .       34
  7.5 Adaptive Governance with Reinforcement Learning . . . . . . . . . . . . . . . . .            34

8 Patent Claims Prevention                                                                         35
  8.1 Comprehensive Claims Coverage . . . . . . . . . . . . . . . . . . . . . . . . . . .          35
      8.1.1 Method Claims . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        35
      8.1.2 System Claims . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        36
      8.1.3 Apparatus Claims . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         36
      8.1.4 Article of Manufacture Claims . . . . . . . . . . . . . . . . . . . . . . . .          36
      8.1.5 Implementation Profile Claims . . . . . . . . . . . . . . . . . . . . . . . .          37


                                            Page 3 of 48
Defensive Publication: Phase Mirror Dissonance                                     January 28, 2026


   8.2   Variations and Extensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   38

9 Licensing and Usage                                                                              38
  9.1 Creative Commons Attribution 4.0 . . . . . . . . . . . . . . . . . . . . . . . . . .         38
  9.2 Trademark Notice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       39
  9.3 Implementation Freedom . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       39

10 Conclusion                                                                                      39
   10.1 Summary of Contributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     39
   10.2 Impact and Availability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    40
   10.3 Future Evolution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   40
   10.4 Acknowledgments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    40

Appendix A: Reference Implementation                                                               40

Appendix B: Glossary                                                                               43

Appendix C: Normative Implementation Profile                                                       44




                                            Page 4 of 48
Defensive Publication: Phase Mirror Dissonance                                  January 28, 2026


1     Introduction and Purpose
1.1     Defensive Publication Objectives
This document constitutes a defensive publication establishing comprehensive prior art for
the Phase Mirror Dissonance (PMD) methodology and all associated systems, methods, and
applications disclosed herein. The explicit purposes of this publication are:

    1. Prevent Patent Claims: To establish definitive, publicly accessible prior art that pre-
       vents any party—including the original developers—from obtaining patent protection on
       the PMD methodology, its constituent elements, or any derivative applications.

    2. Public Domain Contribution: To ensure that the innovations described remain freely
       available for use, modification, and extension by practitioners, researchers, and organiza-
       tions worldwide.

    3. Timestamp Establishment: To create a verifiable, immutable timestamp through pub-
       lication on Zenodo and other archival repositories, establishing the date of invention dis-
       closure.

    4. Comprehensive Coverage: To document not only the core methodology but all known
       variations, extensions, and applications to maximize prior art coverage.

1.2     Scope of Disclosure
This defensive publication covers:

    • The complete Phase Mirror Dissonance methodology and theoretical framework

    • All operational procedures, algorithms, and decision flows

    • Implementation patterns including software architectures and data schemas

    • Application domains including agentic AI governance, organizational diagnostics, and strate-
      gic planning

    • Novel mechanisms including the Mirror Dissonance Oracle, redaction protocols, and circuit-
      breaker patterns

    • Extensions and derivative works including hierarchical PMD and background/callable PMD
      distinctions

1.3     Disclosure Boundaries
This publication explicitly categorizes all disclosed elements into three boundary classes to pre-
vent ambiguity and establish clear expectations regarding what is placed in the public domain
versus what is retained as operational security or competitive advantage.

1.3.1    Disclosed Elements (Public Domain)
The following elements are placed in the public domain under CC BY 4.0 and may be freely
implemented by any party without restriction:




                                           Page 5 of 48
Defensive Publication: Phase Mirror Dissonance                                        January 28, 2026


            Element                      Scope                               Location
            PMD Triadic Framework        Complete     Mirror-Dissonance-     §3.1
                                         Phase methodology
            Five-Step Operating Loop     Extract-Map-Rank-Produce-           §3.2
                                         Question algorithm
            Tension Ranking Formula      Impact × Tractability prioritiza-   §3.2.3
                                         tion
            Output Templates             Standard, Rapid Triage, Board       §3.3
                                         Packet
            Seven Agentic AI Disso-      Complete enumeration                §4.2
            nances
            Compliance-Accuracy          Policy encoding framework           §4.3
            Tradeoff
            Dissonance         Report    JSON                   structure    §5.3
            Schema                       (meta/items/summary/decision)
            Rule Definition Interface    TypeScript interface with FP        §5.4
                                         tolerance
            False-Positive Calibration   Durable store, auto-demotion        §5.5
                                         pattern
            Circuit-Breaker Pattern      Block-rate threshold degradation    §5.6
            Tiered Governance Mod-       Four-tier human oversight (Tier     §4.2.3
            els                          0-3)

                         Table 1: Disclosed Elements (Public Domain)


1.3.2   Retained Elements (Not Disclosed)
The following implementation details are intentionally retained as operational security credentials
or trade secrets. While the patterns are disclosed, specific values and calibrations are not:
    Important Distinction: The pattern of HMAC-based redaction (Section 5.7) is disclosed
as prior art. The specific nonce value used in production systems is retained as an operational
security credential. Independent implementers should generate their own nonces using crypto-
graphically secure random number generators.

1.3.3   Non-Claimed Elements (Out of Scope)
The following are explicitly not claimed as prior art and should be disregarded for patent
analysis purposes:

   • Speculative quantum computing applications (no operational algorithms provided)

   • Hypothetical reinforcement learning extensions (future research direction only)

   • Unimplemented formal verification integration proposals (conceptual only)

   • Metaphorical references to quantum mechanics without operational specification

   • Vague organizational theory analogies without concrete implementation methods

    Rationale: These speculative extensions lack sufficient technical detail to constitute prior
art. They represent potential future research directions but are not part of the normative dis-
closure.




                                            Page 6 of 48
Defensive Publication: Phase Mirror Dissonance                                       January 28, 2026


          Element                      Reason for Retention               Competitive
                                                                          Moat
          Specific HMAC nonce val-     Security credential                Prevents clone-and-
          ues                                                             replace attacks
          Tuned FP rate thresholds     Calibrated      to   proprietary   Operational opti-
                                       datasets                           mization
          Proprietary rule logic       Client-specific domain expertise   Service differentia-
          (MD-050+)                                                       tion
          SSM parameter paths          Infrastructure-specific details    Operational secu-
                                                                          rity
          Internal metric baselines    Performance benchmarks from        Competitive intelli-
                                       production                         gence
          Enterprise     integration   Deployment know-how                Implementation
          playbooks                                                       maturity

                            Table 2: Retained Elements (Trade Secrets)

1.3.4    Competitive Moat Protection
The disclosed elements represent intentional contributions to the public domain to establish prior
art and prevent patent monopolization. Competitive advantages are retained through:
  1. Operational Data: Years of false-positive calibration data from production deployments,
     enabling tuned thresholds that minimize both false positives and false negatives.
  2. Proprietary Detection Rules: Client-specific domain expertise embodied in rules MD-
     050 and above, which address industry-specific governance challenges not disclosed in this
     publication.
  3. Security Credentials: HMAC nonces, SSM parameter paths, and infrastructure config-
     urations that cannot be reverse-engineered from disclosed patterns.
  4. Integration Maturity: Battle-tested deployment patterns, incident response procedures,
     and operational runbooks developed through real-world implementations.
  5. Brand Recognition: Trademark protection for "Phase Mirror Dissonance," "Mirror Dis-
     sonance Oracle," and potential certification programs that provide market differentiation.
  6. Network Effects: Early adopter community, switching costs, and ecosystem integrations
     that create barriers to entry for competitors implementing the disclosed methodology.
    This boundary strategy enables the publication to achieve its dual objectives: (1) estab-
lish comprehensive prior art preventing patent claims, and (2) preserve competitive advantages
through operational assets not disclosed herein.

1.4     Publication Strategy
Following defensive publication best practices [?], this document will be:
  1. Published on Zenodo to obtain a permanent DOI and ensure archival preservation
  2. Submitted to arXiv for academic indexing and citation tracking
  3. Made publicly accessible via institutional repositories and project documentation
  4. Indexed by search engines and patent databases to ensure discoverability
  5. Version-controlled with cryptographic hash verification for integrity

                                             Page 7 of 48
Defensive Publication: Phase Mirror Dissonance                                   January 28, 2026


1.5    Legal Framework
This publication is released under the Creative Commons Attribution 4.0 International
(CC BY 4.0) license, ensuring:

    • Freedom to use, modify, and distribute the methodologies described
    • Requirement for attribution to original source
    • No restrictions on commercial use
    • Compatibility with open-source and proprietary implementations

    Patent Rights Waiver: The authors explicitly waive any rights to pursue patent protection
on the inventions disclosed herein, contributing them to the public domain for the advancement
of organizational governance and AI safety practices.


2     Background and Motivation
2.1    The Governance Challenge
Modern organizations face a fundamental challenge when implementing autonomous AI systems:
the inherent tension between autonomy (the promise of self-directed decision-making) and gov-
ernance (the requirement for accountability, determinism, and human control). This is not a
solvable problem but a permanent structural tension that must be explicitly managed.
    Traditional governance frameworks rely on abstract principles such as “alignment,” “trans-
parency,” and “collaboration”—terms that lack concrete operational definitions and binding mech-
anisms. These vague claims, or vibe claims, create a false sense of control while hiding critical
mismatches between stated intentions and actual operating incentives.

2.2    Prior Art Landscape
Existing approaches to organizational diagnostics and AI governance include:

    • Risk assessment frameworks focusing on probabilistic threat modeling
    • Compliance checklists providing binary pass/fail criteria
    • Governance maturity models describing staged evolution paths
    • Policy analysis tools evaluating regulatory alignment

    However, none of these prior approaches:

    1. Systematically surface the structural contradictions inherent in complex organizational sys-
       tems
    2. Replace abstract governance language with concrete, binding artifacts
    3. Generate testable, metric-driven interventions with explicit ownership
    4. Provide callable, deterministic protocols for automated enforcement
    5. Address the specific challenges of agentic AI liability architecture

   The Phase Mirror Dissonance methodology fills this gap by providing a rigorous, repeatable
process for converting organizational ambiguity into actionable governance mechanisms.

                                            Page 8 of 48
Defensive Publication: Phase Mirror Dissonance                                 January 28, 2026


2.3     Novel Contributions
This disclosure establishes prior art for the following novel contributions:
     1. The PMD Triadic Framework: The integrated Mirror-Dissonance-Phase structure as
        a diagnostic and prescriptive methodology
     2. Operational Formalization: The five-step loop (Extract-Map-Rank-Produce-Question)
        as a repeatable algorithmic process
     3. Artifact-Binding Heuristics: Systematic replacement patterns (“align” → artifact; “col-
        laborate” → binding mechanism)
     4. Tension Ranking Formula: Impact × Tractability as a prioritization metric
     5. Standardized Output Templates: Three distinct formats (Standard, Rapid Triage,
        Board Packet) for different stakeholder audiences
     6. Callable Oracle Protocol: The Mirror Dissonance Oracle as a deterministic, auditable
        governance enforcement layer
     7. Compliance-Accuracy Tradeoff Framework: Explicit policy encoding for autonomous
        agent decision boundaries
     8. Redaction-by-Capability: HMAC-based evidence integrity with brand nonce validation
     9. Circuit-Breaker Patterns: Block-rate thresholds with automatic degradation to warn-
        only modes
    10. False-Positive Calibration: Per-rule FP tolerance tracking with automatic demotion
        mechanisms


3      Core Methodology: Phase Mirror Dissonance
3.1     Conceptual Foundation
The Phase Mirror Dissonance methodology is built on three foundational concepts:

3.1.1     Mirror: Objective Reflection
Definition: The Mirror component reflects the user’s stated claims, goals, and assumptions
back to them without endorsement, judgment, or interpretation. This creates a neutral analytical
surface.
    Purpose: To establish a factual baseline that separates what is said from what is incen-
tivized, exposing latent contradictions.
    Mechanism: Extract explicit statements from input text, including:
     • Stated goals and desired outcomes
     • Claimed constraints and limitations
     • Expressed fears and concerns
     • Implicit assumptions about causality
     • Temporal horizons for action
    Key Principle: The Mirror does not validate or affirm—it simply presents what has been
stated, creating cognitive distance for objective analysis.

                                             Page 9 of 48
Defensive Publication: Phase Mirror Dissonance                                  January 28, 2026


3.1.2     Dissonance: Tension Identification
Definition: Dissonance refers to structural tensions, contradictions, or missing bindings between
different components of a system, plan, or organization.
    Purpose: To identify the root causes of organizational paralysis, policy failure, or imple-
mentation gaps by exposing conflicts between:

   • Stated goals vs. operating incentives

   • Urgency of action vs. capacity to deliver

   • Risk claimed vs. risk owned

   • Control desired vs. control available

   • Compliance requirements vs. probabilistic outputs

   Typology of Dissonances:

  1. Incentive Misalignment: When rewards structure undermines stated objectives

  2. Capacity-Urgency Gap: When timeline demands exceed available resources

  3. Ownership Ambiguity: When accountability is claimed but not assigned

  4. Control Illusion: When governance authority is asserted without enforcement mecha-
     nisms

  5. Binary-Probabilistic Friction: When deterministic frameworks govern stochastic sys-
     tems

3.1.3     Phase: Concrete Interventions
Definition: A Phase is a small, testable shift in process, policy, or resource allocation designed
to restore coherence by addressing identified dissonances.
    Purpose: To convert diagnostic insight into actionable change with measurable outcomes.
    Structure of a Lever (Phase Implementation):
    Each Phase is formalized as a Lever with four mandatory components:

                            Lever = (Owner, Action, Metric, Horizon)                           (1)
   Where:

   • Owner: Specific individual or role accountable for execution

   • Action: Concrete, observable intervention (verb-noun format)

   • Metric: Quantifiable success criterion

   • Horizon: Time-bound deadline (days/weeks/quarters)

   Example:

        Owner: VP Customer Experience
        Action: Create tiered SLA and publish
        Metric: CSAT ≥ 4.5
        Horizon: 30 days

                                          Page 10 of 48
Defensive Publication: Phase Mirror Dissonance                                 January 28, 2026


3.2     The Five-Step Operating Loop
The PMD methodology follows a deterministic, repeatable process:

                  PMD(I) = (Extract ◦ Map ◦ Rank ◦ Produce ◦ Question)(I)                     (2)
    Where I represents the input text describing an organizational challenge, policy question, or
system design.

3.2.1    Step 1: Extract
Objective: Systematically identify all relevant components from the input.
  Extraction Categories:

  1. Goals: What outcomes are explicitly desired?

  2. Claims: What capabilities or conditions are asserted?

  3. Fears: What risks or failure modes are expressed?

  4. Constraints: What limitations are acknowledged (budget, time, policy)?

  5. Stakeholders: Who is affected or must act?

  6. Time Horizon: What is the decision or delivery timeline?

   Algorithm:

FUNCTION Extract(input_text):
    parsed_data = {
        ’goals’: [],
        ’claims’: [],
        ’fears’: [],
        ’constraints’: [],
        ’stakeholders’: set(),
        ’time_horizon’: None
    }

      FOR sentence IN tokenize(input_text):
          IF contains_modal_verb(sentence, [’want’, ’need’, ’must’]):
              parsed_data[’goals’].append(sentence)
          IF contains_assertion(sentence):
              parsed_data[’claims’].append(sentence)
          IF contains_risk_language(sentence):
              parsed_data[’fears’].append(sentence)
          IF contains_limitation(sentence):
              parsed_data[’constraints’].append(sentence)
          FOR entity IN extract_named_entities(sentence):
              IF is_role_or_actor(entity):
                  parsed_data[’stakeholders’].add(entity)
          IF contains_temporal_reference(sentence):
              parsed_data[’time_horizon’] = extract_timeline(sentence)

      RETURN parsed_data

                                         Page 11 of 48
Defensive Publication: Phase Mirror Dissonance                             January 28, 2026


3.2.2   Step 2: Map Tensions
Objective: Identify contradictions and missing bindings between extracted components.
  Tension Mapping Patterns:

            Component A                      Component B
            Stated goal                      Actual incentive structure
            Urgency claim                    Available capacity
            Risk acknowledged                Risk ownership assignment
            Control desired                  Enforcement mechanism
            Compliance requirement           Probabilistic system output
            Abstract principle (“align”)     Concrete artifact (spec/contract)
            Collaboration intent             Binding mechanism (cadence/quorum)

                            Table 3: Tension Mapping Patterns

   Algorithm:

FUNCTION MapTensions(parsed_data):
    tensions = []

    # Goal-Incentive Mismatch
    FOR goal IN parsed_data[’goals’]:
        FOR constraint IN parsed_data[’constraints’]:
            IF undermines(constraint, goal):
                tensions.append({
                    ’type’: ’goal_incentive_mismatch’,
                    ’components’: [goal, constraint],
                    ’severity’: ’high’
                })

    # Urgency-Capacity Gap
    IF parsed_data[’time_horizon’] < minimum_delivery_time(parsed_data):
        tensions.append({
            ’type’: ’urgency_capacity_gap’,
            ’severity’: ’critical’
        })

    # Risk-Ownership Ambiguity
    FOR fear IN parsed_data[’fears’]:
        IF NOT has_assigned_owner(fear, parsed_data[’stakeholders’]):
            tensions.append({
                ’type’: ’risk_ownership_ambiguity’,
                ’components’: [fear],
                ’severity’: ’medium’
            })

    # Abstract-Binding Missing
    FOR claim IN parsed_data[’claims’]:
        IF is_vibe_claim(claim): # e.g., "align", "collaborate"
            IF NOT has_artifact_binding(claim, parsed_data):

                                           Page 12 of 48
Defensive Publication: Phase Mirror Dissonance                                  January 28, 2026


                   tensions.append({
                       ’type’: ’abstract_binding_missing’,
                       ’components’: [claim],
                       ’severity’: ’medium’
                   })

    RETURN tensions

3.2.3   Step 3: Rank Tensions
Objective: Prioritize identified tensions to focus intervention efforts.
  Ranking Formula:

                           Priority(T ) = Impact(T ) × Tractability(T )                       (3)

   Where:

   • Impact ∈ [1, 10]: Magnitude of potential harm or organizational paralysis if unresolved

   • Tractability ∈ [0.1, 1.0]: Feasibility of addressing within available resources and authority

   Impact Scoring Criteria:

   • 10: Existential risk to organization or severe legal liability

   • 7–9: Major operational disruption or reputational damage

   • 4–6: Moderate efficiency loss or delayed strategic initiative

   • 1–3: Minor friction or localized team impact

   Tractability Scoring Criteria:

   • 0.9–1.0: Within direct control, solvable in current time horizon

   • 0.5–0.8: Requires coordination but no external dependencies

   • 0.2–0.4: Requires executive approval or budget allocation

   • 0.1: Systemic constraint requiring multi-year structural change

   Algorithm:

FUNCTION RankTensions(tensions):
    FOR tension IN tensions:
        tension[’impact’] = score_impact(tension)
        tension[’tractability’] = score_tractability(tension)
        tension[’priority’] = tension[’impact’] * tension[’tractability’]

    RETURN sort(tensions, key=’priority’, reverse=True)




                                          Page 13 of 48
Defensive Publication: Phase Mirror Dissonance                                  January 28, 2026


3.2.4    Step 4: Produce Output Blocks
Objective: Generate standardized, actionable output in three required blocks.
  Block A: Phase Mirror Dissonance
  A bullet list (5–9 items) that:
   • Reflects stated claims without endorsement
   • Names identified tensions explicitly
   • Confronts contradictions plainly
   Stylistic Requirements:
   • Short, declarative sentences
   • Neutral, non-emotive tone
   • No moralizing or judgment
   • Direct naming of risks
   Example:
        Phase Mirror Dissonance:
          • Cost reduction goal conflicts with white-glove service promise.
          • QA budget absent makes compliance breaches likely.
          • Ownership unclear for escalation when AI fails.
          • AI autonomy desired but deterministic success required.
          • No mechanism specified for accuracy-compliance tradeoff.
   Block B: Levers to Test Now
   A table (3–7 items) specifying concrete interventions:

            Owner     Lever                       Metric                      Horizon
            VP CX     Create tiered SLA           CSAT ≥ 4.5                  30 days
            Ops       Add spot-QA 5% tickets      Defect rate ≤ 1%            14 days
            Eng       Guardrails on responses     Policy violations ≤ 0.2%    21 days

                                 Table 4: Example Levers Table

   Block C: Optional Artifact
   One (and only one) of:
  1. Quote: A memorable one-liner that encapsulates the core insight
  2. Riddle: A thought-provoking question or paradox
  3. Checklist: A tactical pre-flight list for implementation
   Example Quotes:
   • “Clarity hurts only what was pretending.”
   • “When plans depend on hope, add a kill-switch.”
   • “The mirror disagrees, the ego calls it broken.”

                                          Page 14 of 48
Defensive Publication: Phase Mirror Dissonance                                 January 28, 2026


3.2.5    Step 5: Pose Precision Question
Objective: Ask one (and only one) clarifying question if a blocking ambiguity prevents resolu-
tion.
    Criteria for Precision Question:
   • A critical tradeoff remains unspecified
   • Ownership assignment is ambiguous at the executive level
   • Success metric definition is contested
   • Multiple valid interpretations exist for a key constraint
   Format: Single interrogative sentence, typically forcing a binary or prioritization choice.
   Examples:
   • “Which metric wins if cost and CSAT collide?”
   • “Does the agent optimize for accuracy or compliance?”
   • “Who arbitrates when a rule crosses FP tolerance threshold?”
   Anti-Pattern: Do NOT ask open-ended questions like “What are your thoughts?” or “How
do you feel about this?” These invite discussion rather than decision.
   sha256:722fc7cfeb9e2dac67b7d0b4f99ed26b7557b263f63e0bf865c8869a0e01223e

3.3     Standardized Output Templates
The PMD methodology provides three distinct output templates for different stakeholder con-
texts:

3.3.1    Template A: Standard Analysis
Use Case: Default format for most analyses; balances comprehensiveness with conciseness.
  Structure:
Phase Mirror Dissonance:
• [Tension 1]
• [Tension 2]
• [Tension 3]
• [Tension 4]
• [Tension 5]

Levers to Test Now:
| Owner | Lever | Metric | Horizon |
|-------|-------|--------|---------|
| [Role] | [Action] | [KPI] | [Days] |
| [Role] | [Action] | [KPI] | [Days] |
| [Role] | [Action] | [KPI] | [Days] |

Optional Artifact:
[Quote/Riddle/Checklist]

Precision Question:
[Single clarifying question, if needed]

                                         Page 15 of 48
Defensive Publication: Phase Mirror Dissonance                              January 28, 2026


   Length: 120–220 words

3.3.2   Template B: Rapid Triage
Use Case: High time-pressure situations; short prompts; quick decision gates.
  Structure:

Top 3 Tensions:
1. [Tension 1]
2. [Tension 2]
3. [Tension 3]

Levers:
• [Owner] → [Action] → [Metric] → [Horizon]
• [Owner] → [Action] → [Metric] → [Horizon]
• [Owner] → [Action] → [Metric] → [Horizon]

Artifact:
[Single quote]

[Question only if blocking]

   Length: ≤ 140 words

3.3.3   Template C: Board Packet
Use Case: Executive and board-level reporting; strategic oversight.
  Structure:

Top 5 Ranked Tensions:
1. [Tension] | Impact: [X] | Tractability: [Y] | Priority: [Z]
2. [Tension] | Impact: [X] | Tractability: [Y] | Priority: [Z]
3. [Tension] | Impact: [X] | Tractability: [Y] | Priority: [Z]
4. [Tension] | Impact: [X] | Tractability: [Y] | Priority: [Z]
5. [Tension] | Impact: [X] | Tractability: [Y] | Priority: [Z]

Key Levers with Baseline & Target:
| Owner | Lever | KPI | Baseline | Target | Horizon |
|-------|-------|-----|----------|--------|---------|
| [Role] | [Action] | [Metric] | [Current] | [Goal] | [Days] |

Risk Register:
| Risk | Trigger | Mitigation | Owner |
|------|---------|------------|-------|
| [Risk 1] | [Condition] | [Action] | [Role] |
| [Risk 2] | [Condition] | [Action] | [Role] |
| [Risk 3] | [Condition] | [Action] | [Role] |

Review Cadence:
[Proposed oversight frequency and forum]

   Length: 300–500 words

                                        Page 16 of 48
Defensive Publication: Phase Mirror Dissonance                                January 28, 2026


4     Application Domain: Agentic AI Governance
4.1     The Autonomy-Governance Tension
Agentic AI systems—autonomous agents capable of reasoning, planning, and acting without
constant human prompting—create a fundamental structural tension:

                    Agentic AI Promise ⊥ Enterprise Governance Requirement                  (4)
    Where:
    • Agentic AI Promise: Autonomous decision-making, adaptive behavior, permission to
      explore and fail
    • Enterprise Governance: Deterministic guarantees, audit trails, human accountability,
      zero-failure tolerance
   This is not a solvable contradiction—it is a permanent tension requiring explicit management
through binding mechanisms.

4.2     Critical Dissonances in Agentic AI Systems
Applying the PMD framework to agentic AI reveals seven recurring dissonances:

4.2.1     Dissonance 1: Reasoning vs. Data Hygiene
Tension: An agent’s capacity for causal reasoning exposes previously hidden gaps in data qual-
ity. Unlike black-box models that obscure data flaws, causal AI agents explicitly reason over
datasets—meaning inaccurate, biased, or incomplete data leads to fundamentally wrongful con-
clusions with direct liability.
    Mechanism: Causal graphs and structural causal models require:
    • Complete variable sets (all confounders identified)
    • Accurate edge directions (true causal relationships)
    • Valid conditional independence assumptions
    Governance Lever:
        Owner: Data Governance
        Lever: Quantify causal model validity score before deployment
        Metric: Graph Accuracy Score ≥ 0.90
        Horizon: 14 days

4.2.2     Dissonance 2: Domain-Specific Precision vs. Platform Scalability
Tension: Organizations desire scalable, general-purpose AI platforms, but agentic systems de-
liver measurable ROI only when tuned to specific domain contexts with high-precision outputs.
    Tradeoff:
    • General-Purpose Platform: Broad applicability, lower precision, slower adoption
    • Domain-Specific Agent: Narrow scope, high precision, immediate business impact
    Phase Recommendation: Pilot domain-specific agents first; abstract to platform after
validation.

                                         Page 17 of 48
Defensive Publication: Phase Mirror Dissonance                                   January 28, 2026


4.2.3     Dissonance 3: Autonomy vs. Deterministic Success
Tension: True autonomy implies permission to fail and learn. Enterprise governance demands
deterministic, predictable success—particularly in high-stakes environments (finance, healthcare,
critical infrastructure).
    Resolution Framework: Tiered governance models:

        Tier     Oversight Model                              Use Case
        Tier 0   Fully autonomous (no human gate)             Low-stakes, reversible actions
        Tier 1   Human-on-the-loop (review after action)      Medium-stakes, auditable
        Tier 2   Human-in-the-loop (approve before action)    High-stakes, irreversible
        Tier 3   Human-only (AI advisory)                     Critical infrastructure, legal

                                Table 5: Tiered Governance Model


4.2.4     Dissonance 4: Probabilistic Outputs vs. Binary Compliance
Tension: Agentic systems produce probabilistic outputs (Bayesian inference, confidence inter-
vals). Legal and compliance frameworks operate on binary pass/fail logic.
    Problem: Machine-to-machine decision chains amplify this friction—when one agent’s prob-
abilistic output becomes another’s input, uncertainty compounds.
    Governance Artifact:
        Spec: Define what constitutes an “acceptable error” vs. a “policy violation”
        Contract: Map probabilistic confidence thresholds to liability tiers
        SLA: Commit to audit pass rate ≥ 95%

4.2.5     Dissonance 5: Agency vs. Prediction (Liability Shift)
Tension: When a system shifts from prediction (recommending action) to agency (taking ac-
tion), liability moves from the end-user to the system designer/operator.
    Legal Exposure Categories:
   • Errors & Omissions (E&O): Faulty agent outputs causing financial harm
   • Cyber Liability: Agent manipulation or adversarial attacks
   • Employment Practices Liability: Discriminatory agent decisions in hiring, promotion,
     termination
  Governance Requirement: Explicit assignment of risk ownership with insurance coverage
mapping.

4.2.6     Dissonance 6: No-Code Interfaces vs. Causal Expertise
Tension: User-friendly no-code tools mask the deep theoretical expertise required to build valid
causal models. This creates risk of employees with insufficient training deploying agents that
produce faulty, liability-creating conclusions.
   Mitigation Lever:
        Owner: Product
        Lever: Measure user error in no-code model logic
        Metric: Logical Validity Score ≥ 90%
        Horizon: 30 days

                                           Page 18 of 48
Defensive Publication: Phase Mirror Dissonance                                January 28, 2026


   Implementation: Automated validation checks for:

   • Causal graph acyclicity

   • Conditional independence violations

   • Simpson’s paradox risks

   • Collider bias introduction

4.2.7     Dissonance 7: Transparency Rhetoric vs. Proprietary Infrastructure
Tension: Organizations claim commitment to AI transparency while building agents on propri-
etary, black-box platforms where decision-making logic is opaque.
    Consequence: When an agent makes an indefensible decision, the organization cannot
explain why—rendering the action legally and operationally unjustifiable.
    Governance Binding:

        SLA: Platform provider must commit to explainability standards
        Kill-Switch: If transparency drops below threshold, agent pauses and escalates

4.3     The Compliance-Accuracy Tradeoff
The most critical policy decision in agentic AI governance is:


      Does the agent optimize for the most accurate outcome or the most compliant one?      (5)

   This is not a system failure—it is a fundamental design choice requiring explicit policy en-
coding.
   Scenario: An agentic loan approval system:

   • Accuracy Optimization: Uses all available data (including protected attributes) to min-
     imize default risk

   • Compliance Optimization: Excludes protected attributes to ensure regulatory adher-
     ence, accepting higher default rate

    PMD Framework Requirement: The answer must be encoded as policy with explicit
triggers:

IF agent_reasoning_conflicts_with_rules:
    DO NOT freeze_or_hallucinate_compliance
    ESCALATE_TO pre_defined_exception_handler
    LOG rationale_and_context
    AWAIT human_adjudication

   Governance Artifact: A formal “Error Budget” specification:




                                          Page 19 of 48
Defensive Publication: Phase Mirror Dissonance                                  January 28, 2026


         Decision Type                    Allowable FP Rate        Allowable FN Rate
         Financial transaction approval         0.1%                      2%
         Content moderation                      1%                       5%
         Medical diagnosis support              0.01%                     10%

                           Table 6: Example Error Budget by Domain


5     The Mirror Dissonance Oracle: Callable Protocol
5.1    Motivation
The Phase Mirror Dissonance methodology, when applied manually, provides diagnostic value.
However, for continuous governance enforcement—particularly in CI/CD pipelines, merge queues,
and drift detection—a callable, deterministic protocol is required.
    The Mirror Dissonance Oracle is a software implementation of the PMD framework
designed to:

    1. Provide repeatability: Same inputs + same rules → same report

    2. Enable composability: Callable at multiple checkpoints (PR review, merge, baseline rota-
       tion)

    3. Ensure auditability: Outputs are artifacts with hashes, provenance, and diffability

    4. Enforce safety: Hard-coded guardrails, budget limits, redaction guarantees

5.2    Architectural Overview
Input:
    - Artifacts: diffs, workflows, configs, manifests
    - Context: event_type (PR/merge/drift), repo, branch
    - Risk Profile: strictness level (pilot vs. production)

Process:
    1. Load rule registry (MD-001, MD-002, ..., MD-NNN)
    2. Execute detection logic for each rule
    3. Collect findings with evidence (file:line:snippet)
    4. Apply false-positive calibration
    5. Enforce circuit-breaker thresholds
    6. Generate dissonance report (JSON)

Output:
    - dissonance_report.json with:
        * meta: oracle_version, rules_hash, budget_consumed
        * items: findings with severity, evidence, suggested_fix
        * summary: counts by severity
        * machine_decision: pass/warn/block

5.3    Dissonance Report Schema
The canonical output format is a JSON object conforming to the following schema:



                                          Page 20 of 48
Defensive Publication: Phase Mirror Dissonance                       January 28, 2026


{
    "meta": {
       "oracle_version": "1.3.2",
       "rules_hash": "sha256:a1b2c3...",
       "invocation_context": {
          "event_type": "pull_request",
          "repo": "org/repo-name",
          "branch": "feature/new-policy",
          "timestamp": "2026-01-27T23:45:00Z"
       },
       "budget_consumed_ms": 1847,
       "calibration_status": {
          "fp_observability": {
             "window_n": 200,
             "observed_fpr": 0.003,
             "breach": false
          }
       }
    },
    "items": [
       {
          "id": "MD-001-1",
          "rule_id": "MD-001",
          "rule_version": "1.2.0",
          "severity": "high",
          "claim": "Required status check contexts don’t match stable job name",
          "evidence": {
             "file": ".github/branch-protection.json",
             "line": 42,
             "snippet": {
               "redacted": true,
               "value": "[REDACTED]",
               "brand": "[NONCE-HASH]",
               "mac": "[HMAC-SHA256]"
             }
          },
          "suggested_fix": "Align protection contexts with workflow job IDs",
          "block_recommended": true
       }
    ],
    "summary": {
       "total": 3,
       "by_severity": {
          "critical": 0,
          "high": 1,
          "medium": 2,
          "low": 0
       }
    },


                                       Page 21 of 48
Defensive Publication: Phase Mirror Dissonance                                 January 28, 2026


    "machine_decision": {
      "outcome": "warn",
      "degraded": false,
      "reason": "High-severity findings present but below block threshold"
    }
}
     sha256:e0968afc977bd0aaae878e673a891cd67c8f3b46e6fa8c6544e24d6f958dd6c6

5.4     Conformance Verification
Independent implementations can verify conformance with this schema specification by executing
the test vector suite published alongside this defensive publication. The test suite provides
cryptographic verification that implementations produce byte-identical outputs when processing
identical inputs.

5.4.1    Test Vector Coverage
The conformance suite includes seven test vectors covering:
    1. Minimal Dissonance Report (tv-001): End-to-end test generating a complete report
       from simple natural language input. Verifies meta block, items array, summary counts,
       and machine decision structure.
    2. Tension Ranking Calculation (tv-002): Tests Impact × Tractability priority formula
       with floating-point precision handling and deterministic sorting.
    3. False-Positive Rate Calculation (tv-003): Validates FP rate computation with edge
       cases including pending events (which must be excluded from denominator) and breach
       detection logic.
    4. Circuit-Breaker Threshold (tv-004): Verifies circuit breaker triggers precisely at thresh-
       old, degrading to warn-only mode with appropriate reason string.
    5. UTF-8 Normalization (tv-005): Tests NFC normalization handling decomposed char-
       acters (e.g., café as e + combining acute accent) versus composed forms.
    6. JSON Key Ordering (tv-006): Validates lexicographic key sorting with case-sensitive
       comparison (ASCII uppercase sorts before lowercase).
    7. Floating-Point Edge Cases (tv-007): Confirms mandatory rejection of NaN, Infinity,
       and -Infinity, plus correct handling of negative zero and maximum precision decimals.

5.4.2    Test Vector Format
Each test vector includes:
    • id: Unique identifier (e.g., "tv-001")
    • name: Human-readable description
    • input: Structured input object
    • expected_output: Canonical output object
    • canonical_json: Exact byte sequence with sorted keys and trailing newline
    • sha256: 64-character lowercase hex hash for verification

                                          Page 22 of 48
Defensive Publication: Phase Mirror Dissonance                        January 28, 2026


5.4.3    Validation Procedure
To verify conformance:

  1. Parse the input object from test vector

  2. Execute implementation to generate output

  3. Canonicalize output (NFC normalization, key sorting)

  4. Compute SHA-256 of UTF-8 bytes (including trailing \n)

  5. Compare computed hash to sha256 field

  6. Test passes if and only if hashes match exactly

5.4.4    Accessing Test Vectors
Primary Location: Zenodo repository (DOI to be assigned)
Filename: pmd_test_vectors.json
Format: JSON with UTF-8 encoding
License: CC0 1.0 Universal (Public Domain Dedication)
Hash: [to be computed upon finalization]
   Validation Command (Linux/macOS):

cat pmd_test_vectors.json | jq --sort-keys -c ’.vectors[0]’ | sha256sum

   Normative Reference: For complete implementation requirements, see Appendix C (Nor-
mative Implementation Profile).

5.5     Rule Registry Structure
Each rule is a self-contained module with standardized interface:

interface RuleDefinition {
  id: string;              // e.g., "MD-001"
  version: string;         // Semantic versioning
  tier: "A" | "B";         // Tier A: fast; Tier B: deep
  fp_tolerance: {
     ceiling: number;      // Max allowable FP rate
     floor: number;        // Min required FP rate
  };
  detect: (ctx: DetectionContext) => Finding[];
  remediation: string;     // Human-readable fix guidance
  status: "warn" | "blocking";
  promotion_criteria?: string;
}

   Example Rule: MD-001

export const MD_001: RuleDefinition = {
  id: "MD-001",
  version: "1.2.0",
  tier: "A",

                                         Page 23 of 48
Defensive Publication: Phase Mirror Dissonance                               January 28, 2026


     fp_tolerance: { ceiling: 0.005, floor: 0.001 },

     detect: (ctx) => {
       const findings: Finding[] = [];
       const protectionContexts = ctx.loadJSON(’.github/branch-protection.json’);
       const workflowJobNames = ctx.extractWorkflowJobs();

          for (const context of protectionContexts.required_status_checks) {
            if (!workflowJobNames.includes(context)) {
              findings.push({
                rule_id: "MD-001",
                severity: "high",
                claim: ‘Context ’${context}’ has no matching workflow job‘,
                evidence: {
                   file: ’.github/branch-protection.json’,
                   line: ctx.getLineNumber(context),
                   snippet: ctx.redactor.redact(context)
                },
                suggested_fix: ‘Create workflow job named ’${context}’ or update protection‘
              });
            }
          }

          return findings;
     },

     remediation: "Align required status check contexts with stable workflow job names",
     status: "blocking",
     promotion_criteria: "200+ invocations with FPR < 0.5%"
};

      sha256:a9cebfa9a6ac6a9ce5eab95557e5f7b5535d8285967bd877f4533e4ebdebcb59

5.6        False-Positive Calibration
The oracle maintains a durable FP tracking store to prevent runaway false positives:

interface FPEvent {
  rule_id: string;
  rule_version: string;
  finding_id: string;
  timestamp: number;
  outcome: "false_positive" | "true_positive" | "pending";
  suppression_ticket?: string;
}

function computeFPRate(rule_id: string, rule_version: string,
                       window_n: number): FPObservability {
  const events = fpStore.query({
    rule_id,


                                        Page 24 of 48
Defensive Publication: Phase Mirror Dissonance                                January 28, 2026


      rule_version,
      limit: window_n,
      order: "desc"
    });

    const fp_count = events.filter(e => e.outcome === "false_positive").length;
    const total_count = events.filter(e => e.outcome !== "pending").length;
    const observed_fpr = total_count > 0 ? fp_count / total_count : 0;

    return {
       window_n: events.length,
       fp_count,
       observed_fpr,
       breach: observed_fpr > rule.fp_tolerance.ceiling
    };
}

    Automatic Demotion: If a rule exceeds its FP ceiling, it is automatically demoted from
“blocking” to “warn” status:

function demoteIfBreached(rule: BlockingRule, fpObs: FPObservability): Rule {
  if (fpObs.breach) {
    return {
       ...rule,
       status: "warn",
       promotion_evidence: null,
       demotion_reason: ‘FPR ${fpObs.observed_fpr} exceeds ceiling
                         ${rule.fp_tolerance.ceiling}‘
    };
  }
  return rule;
}

5.7    Circuit-Breaker Pattern
To prevent blast-radius scenarios where the oracle blocks excessive PRs/hour, a circuit-breaker
mechanism is enforced:

interface BlockCounter {
  increment(key: string, ttl_seconds: number): Promise<number>;
  get(key: string): Promise<number>;
}

const CIRCUIT_BREAKER_THRESHOLD = 10; // blocks per hour

async function decide(findings: Finding[],
                      context: InvocationContext): Promise<MachineDecision> {
  const blockKey = ‘blocks/${context.repo}/${hourBucket()}‘;
  const recentBlocks = await blockCounter.get(blockKey);



                                        Page 25 of 48
Defensive Publication: Phase Mirror Dissonance                                 January 28, 2026


    if (recentBlocks >= CIRCUIT_BREAKER_THRESHOLD) {
      return {
         outcome: "warn",
         degraded: true,
         reason: "Circuit breaker triggered: block rate exceeds threshold"
      };
    }

    const shouldBlock = findings.some(f => f.block_recommended &&
                                      f.severity === "high");

    if (shouldBlock) {
      await blockCounter.increment(blockKey, 3600); // 1 hour TTL
      return { outcome: "block", degraded: false };
    }

    return { outcome: "pass", degraded: false };
}

5.8     Boundary Clarification: Pattern vs. Credential
Critical Distinction for Patent Prior Art:
    This section discloses the pattern of HMAC-based capability branding as prior art, placing
it in the public domain. The specific nonce value used in production systems is intentionally
retained as an operational security credential.

5.8.1    What is Disclosed (Public Domain)
The following elements are prior art and freely implementable:

    • The RedactedText interface structure with fields: redacted, value, brand, mac

    • The branding algorithm: brand = HMAC-SHA256(nonce, "redacted")

    • The integrity verification pattern: mac = HMAC-SHA256(nonce, value)

    • The validation algorithm using timing-safe comparison to prevent side-channel attacks

    • The requirement for cryptographically secure nonce generation (minimum 256 bits entropy)

    • The monthly rotation pattern with dual-nonce acceptance during grace periods

    • The use of parameter stores (AWS SSM, HashiCorp Vault, etc.) for nonce management

5.8.2    What is Retained (Operational Security)
The following are not disclosed and remain protected as operational security:

    • The actual nonce value(s) used in production systems

    • The specific SSM Parameter Store path or secret management system location

    • The exact rotation schedule (monthly is disclosed; specific day/time is not)


                                         Page 26 of 48
Defensive Publication: Phase Mirror Dissonance                                January 28, 2026


   • The grace period duration for dual-nonce acceptance (exists; exact hours is not disclosed)

   • Monitoring thresholds and alerting logic for validation failures

   • Incident response procedures for nonce compromise

5.8.3    Rationale
Disclosing the actual nonce value would allow adversaries to forge valid RedactedText objects,
completely defeating the capability-based security model. The nonce functions as a cryptographic
credential, analogous to a private key in public-key cryptography.
    The pattern is prior art—preventing patents on HMAC-based redaction schemes. The cre-
dential is operational security—protecting production systems from forgery attacks.

5.8.4    Guidance for Independent Implementations
Implementers should:

  1. Generate a unique nonce using a cryptographically secure random number generator:

        openssl rand -hex 32    # Generates 256-bit nonce

  2. Store nonce in a secure parameter store or secret management system

  3. Implement nonce rotation (recommended: monthly, with 2-hour grace period)

  4. Never log, echo, or transmit the raw nonce value

  5. Use constant-time comparison for brand/MAC validation to prevent timing side-channels

  6. Monitor validation failure rates as a security metric

   Security Note: The disclosed pattern enables interoperability testing and patent prevention.
Each deployment should use independently generated nonces—there is no "shared secret" across
implementations.

5.9     Redaction-by-Capability
To ensure evidence snippets never leak secrets, a brand-by-capability mechanism is enforced:

const BRAND_NONCE = loadFromSSM("guardian/redaction/nonce");

interface RedactedText {
  redacted: true;
  value: string;               // Redacted content
  brand: string;               // HMAC(NONCE, "redacted")
  mac: string;                 // HMAC(NONCE, value)
}

function redact(raw: string, context: RedactionContext): RedactedText {
  let cleaned = raw;

  // Pattern-based redaction
  cleaned = cleaned.replace(/ghp_[A-Za-z0-9]{36}/g, "[TOKEN-REDACTED]");

                                         Page 27 of 48
Defensive Publication: Phase Mirror Dissonance                          January 28, 2026


    cleaned = cleaned.replace(/AKIA[A-Z0-9]{16}/g, "[AWS-KEY-REDACTED]");
    cleaned = cleaned.replace(/-----BEGIN [A-Z ]+-----[\s\S]+?-----END/g,
                             "[PEM-REDACTED]");

    // Entropy-based redaction (gated by file type)
    if (context.shouldApplyEntropyRedaction()) {
      cleaned = redactHighEntropy(cleaned, threshold=4.5);
    }

    return {
       redacted: true,
       value: cleaned,
       brand: HMAC_SHA256(BRAND_NONCE, "redacted"),
       mac: HMAC_SHA256(BRAND_NONCE, cleaned)
    };
}

function isValidRedactedText(obj: any): boolean {
  if (!obj.redacted || !obj.brand || !obj.mac) return false;

    const expectedBrand = HMAC_SHA256(BRAND_NONCE, "redacted");
    const expectedMac = HMAC_SHA256(BRAND_NONCE, obj.value);

    return timingSafeEqual(obj.brand, expectedBrand) &&
           timingSafeEqual(obj.mac, expectedMac);
}

     sha256:248359a245b5b47d49d7b5894f7fdebf96ec2840a869015085debccec838454c

5.10    Integration Patterns
GitHub Actions Workflow:

name: Mirror Dissonance Check
on: [pull_request, merge_group]

jobs:
  oracle:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
           fetch-depth: 0 # Full history for drift detection

        - name: Run Mirror Dissonance Oracle
          run: |
            pnpm --filter @mirror-dissonance/oracle run check \
              --mode ${{ github.event_name }} \
              --output dissonance-report.json



                                       Page 28 of 48
Defensive Publication: Phase Mirror Dissonance                        January 28, 2026


        - name: Upload Report
          uses: actions/upload-artifact@v4
          with:
            name: dissonance-report
            path: dissonance-report.json

        - name: Write Summary
          run: |
            pnpm --filter @mirror-dissonance/oracle run summarize \
              --input dissonance-report.json \
              >> $GITHUB_STEP_SUMMARY

        - name: Enforce Decision
          run: |
            OUTCOME=$(jq -r ’.machine_decision.outcome’ dissonance-report.json)
            if [ "$OUTCOME" = "block" ]; then
               echo " Dissonance check failed"
               exit 1
            elif [ "$OUTCOME" = "warn" ]; then
               echo " Dissonance warnings present"
               exit 0
            else
               echo " Dissonance check passed"
               exit 0
            fi

     Branch Protection Configuration:

{
    "required_status_checks": {
       "strict": true,
       "contexts": [
         "Mirror Dissonance Check / oracle"
       ]
    },
    "required_pull_request_reviews": {
       "required_approving_review_count": 1,
       "dismiss_stale_reviews": true
    },
    "enforce_admins": false,
    "restrictions": null
}


6     Implementation Guidelines
6.1     Deployment Patterns
6.1.1    Centralized Oracle Service
Deploy the Mirror Dissonance Oracle as a centralized service:


                                        Page 29 of 48
Defensive Publication: Phase Mirror Dissonance                             January 28, 2026


   • Infrastructure: AWS Lambda + API Gateway, or Kubernetes deployment

   • Storage: DynamoDB for FP events, S3 for report archives

   • Secrets: SSM Parameter Store for redaction nonce

   • Monitoring: CloudWatch for circuit-breaker alerts, FP rate tracking

   Advantages:

   • Centralized rule updates

   • Shared FP calibration across repos

   • Consistent redaction nonce

   Disadvantages:

   • Single point of failure

   • Network latency on every invocation

6.1.2   Embedded CLI Tool
Package the oracle as a CLI tool included in each repository:

pnpm add @mirror-dissonance/cli --save-dev

# In CI workflow
pnpm dlx @mirror-dissonance/cli check --mode pull_request

   Advantages:

   • No external dependencies

   • Fast local execution

   • Offline capability

   Disadvantages:

   • Decentralized FP tracking

   • Rule version drift across repos

6.1.3   Hybrid Model (Recommended)
CLI tool for execution + centralized FP store:

   • Oracle runs locally (fast, no network dependency)

   • FP events reported to central store (async, best-effort)

   • Rules fetched from central registry with caching




                                          Page 30 of 48
Defensive Publication: Phase Mirror Dissonance                             January 28, 2026


6.2     Operational Runbooks
6.2.1    Nonce Rotation Procedure
Frequency: Monthly or on-demand after security incident
   Steps:

  1. Generate new nonce: openssl rand -hex 32

  2. Store as guardian/redaction/nonce/v2 in SSM

  3. Update oracle config to accept both old and new nonce (grace period: 2 hours)

  4. Deploy updated oracle to all environments

  5. After grace period expires, delete old nonce from SSM

  6. Update VALID_NONCES array to remove old version

   Monitoring: CloudWatch alarm on validation failures

6.2.2    Circuit-Breaker Response
Trigger: Block rate exceeds threshold (10 blocks/hour)
   Automatic Response:

  1. Oracle degrades to warn-only mode

  2. machine_decision.degraded = true in report

  3. Incident ticket auto-created in issue tracker

   Human Response:

  1. Investigate root cause (new rule with high FP rate? Mass bad PRs?)

  2. If rule is faulty: demote rule to warn status, schedule fix

  3. If PRs are legitimately bad: temporary manual review process

  4. Reset block counter after resolution

6.2.3    False-Positive Feedback Loop
Trigger: Developer disputes a blocking finding
   Process:

  1. Developer adds label oracle:false-positive to PR

  2. Creates issue with template: FP Report:         MD-XXX

  3. Steward reviews within 24 hours

  4. If confirmed FP: Record in FP store, consider rule adjustment

  5. If true positive: Educate developer, close issue

  Escalation: If rule FP rate exceeds ceiling for 3 consecutive weeks, automatic demotion +
mandatory rule revision.

                                         Page 31 of 48
Defensive Publication: Phase Mirror Dissonance                                  January 28, 2026


6.3     Governance Framework
6.3.1    Rule Stewardship
Role: Rule Registry Steward
  Responsibilities:

   • Merge authority over src/rules/* directory

   • Review and approve new rule proposals

   • Monitor FP rates and enforce promotion/demotion criteria

   • Maintain rule documentation and remediation guidance

   • Quarterly rule registry audit

   Selection Criteria:

   • Deep understanding of PMD methodology

   • Domain expertise in relevant systems (CI/CD, security, compliance)

   • Track record of balanced judgment (not overly permissive or restrictive)

6.3.2    Promotion Criteria
A rule may be promoted from “warn” to “blocking” status only if:

  1. Measurement Window: ≥ 200 invocations recorded

  2. FP Rate: Observed FPR < fp_tolerance.ceiling

  3. Stability: No FPR spikes > 2× ceiling in past 30 days

  4. Documentation: Remediation guidance clear and tested

  5. Approval: Steward + Security Lead sign-off

6.3.3    Demotion Triggers
A rule is automatically demoted from “blocking” to “warn” if:

  1. FP Breach: Observed FPR exceeds fp_tolerance.ceiling

  2. Circuit Breaker: Contributes to 3+ circuit-breaker events in 7 days

  3. Security Incident: Rule logic exploited or bypassed

  4. Steward Override: Explicit demotion by Rule Steward




                                        Page 32 of 48
Defensive Publication: Phase Mirror Dissonance                                 January 28, 2026


7     Extensions and Future Work
7.1    Hierarchical PMD
Concept: Distinguish between “background PMD” (always-on, O(1) invariant checks) and
“callable PMD” (on-demand, deep semantic analysis).
    Tiers:

    • Tier A (Background): Fast checks (< 100ms): naming mismatches, missing files, schema
      violations, unpinned dependencies

    • Tier B (Callable): Deep checks (> 1s): cross-file semantic consistency, protection-
      workflow alignment, drift detection, causal graph validation

   Use Case: Background PMD runs on every file save in IDE. Callable PMD runs at PR
submit, merge queue, and scheduled drift detection.

7.2    Multi-Stakeholder Orchestration
Challenge: Large organizations have multiple teams with conflicting priorities. The PMD
framework can be extended to explicitly model stakeholder tradeoffs.
   Extension: Stakeholder Tension Matrix

interface StakeholderTension {
  stakeholder_a: string;
  stakeholder_b: string;
  tension: string;
  mediation_mechanism: "escalate" | "weighted_vote" | "exec_decision";
  quorum_required?: number;
  decision_threshold?: number;
}

    Example:

      Stakeholder A: Engineering (wants speed)
      Stakeholder B: Compliance (wants audit trail)
      Tension: Fast deployment vs. complete documentation
      Mediation: Weighted vote (Eng 40%, Compliance 40%, CTO 20%)

7.3    Causal PMD for Organizational Dynamics
Concept: Apply causal inference methods to organizational interventions.
  Research Questions:

    • Does implementing a specific lever causally reduce the target tension?

    • What is the treatment effect of introducing the Mirror Dissonance Oracle on CI/CD cycle
      time?

    • Are there confounders (team size, domain complexity) that mediate the relationship?

    Method:

    1. Define causal graph: Lever → Metric, with confounders


                                         Page 33 of 48
Defensive Publication: Phase Mirror Dissonance                                January 28, 2026


  2. Collect observational data from multiple implementations

  3. Apply propensity score matching or instrumental variables

  4. Estimate Average Treatment Effect (ATE)

   Open Questions:

   • Can we build a “meta-PMD” that analyzes PMD interventions themselves?

   • What is the minimal set of binding artifacts required for governance efficacy?

7.4   Integration with Formal Verification
Concept: Combine PMD’s diagnostic power with formal methods for provable correctness.
  Approach:

   • PMD identifies dissonances (e.g., “Policy claims X but code does Y”)

   • Formal verification tools (TLA+, Coq, Dafny) prove properties

   • Integration: PMD generates formal specifications from policy documents; verifier checks
     code against specs

   Example:

Policy: "All high-risk agent decisions require human approval"

PMD detects:
- Agent workflow missing approval gate
- Approval timeout not specified

Formal spec (TLA+):
THEOREM HighRiskApproval ==
  \A decision \in Decisions:
    decision.risk_level = "high" =>
      \E approval \in Approvals:
        approval.decision_id = decision.id /\
        approval.timestamp < decision.execution_timestamp

Verifier: Checks that agent orchestration code satisfies theorem

7.5   Adaptive Governance with Reinforcement Learning
Concept: Use RL to learn optimal lever selection and parameter tuning.
  Setup:

   • State: Current dissonance profile (tension vector)

   • Action: Select lever(s) to implement

   • Reward: Reduction in tension magnitude + increase in metric target achievement

   • Policy: Learned mapping from dissonance states to optimal levers

   Challenges:

                                        Page 34 of 48
Defensive Publication: Phase Mirror Dissonance                                    January 28, 2026


    • Organizational dynamics are non-stationary

    • Interventions have delayed effects

    • Credit assignment problem (which lever caused improvement?)

   Potential Solution: Meta-learning approach where policy adapts to organizational context
over time.


8     Patent Claims Prevention
8.1     Comprehensive Claims Coverage
This defensive publication explicitly discloses the following to prevent patent claims by any party:

8.1.1    Method Claims
Claim 1: A method for organizational diagnostics comprising:

    1. Extracting stated goals, claims, fears, constraints, and stakeholders from input text

    2. Mapping structural tensions between extracted components

    3. Ranking tensions by impact and tractability

    4. Generating standardized output blocks comprising dissonance list, actionable levers with
       owners/metrics/horizons, and optional artifact

    5. Optionally posing a single precision question to resolve blocking ambiguities

    Claim 2: A method for agentic AI governance comprising:

    1. Identifying the compliance-accuracy tradeoff in autonomous agent behavior

    2. Encoding explicit policy rules defining when compliance overrides accuracy

    3. Implementing tiered governance models (human-in-loop vs. human-on-exception)

    4. Escalating conflicts between agent reasoning and hard-coded rules to exception handlers
       with logged rationale

    Claim 3: A method for false-positive calibration comprising:

    1. Maintaining a durable store of rule invocation outcomes (true positive, false positive, pend-
       ing)

    2. Computing observed FP rate over a sliding window

    3. Automatically demoting rules from blocking to warn status when FP rate exceeds tolerance
       ceiling

    4. Requiring measured promotion evidence before re-enabling blocking status




                                           Page 35 of 48
Defensive Publication: Phase Mirror Dissonance                                 January 28, 2026


8.1.2   System Claims
Claim 4: A callable governance enforcement system comprising:

  1. A rule registry storing rule definitions with detection logic, FP tolerance, and promotion
     criteria

  2. An invocation engine executing rules against input artifacts

  3. A redaction module using capability-based branding to prevent secret leakage

  4. A circuit-breaker module tracking block rate and degrading to warn-only when threshold
     exceeded

  5. A decision engine producing machine-readable pass/warn/block determinations

   Claim 5: A dissonance report data structure comprising:

  1. Metadata block with oracle version, rules hash, invocation context, and budget consumed

  2. Items array containing findings with rule ID, severity, claim, evidence, and suggested fix

  3. Summary block with counts by severity

  4. Machine decision block with outcome, degraded status, and reason

8.1.3   Apparatus Claims
Claim 6: A computer-readable storage medium containing instructions that, when executed,
perform the PMD five-step loop.
   Claim 7: A distributed system comprising multiple instances of the Mirror Dissonance
Oracle sharing a centralized FP tracking store and redaction nonce service.

8.1.4   Article of Manufacture Claims
Claim 8: A software package distributable via package managers (npm, pip, cargo) providing:

   • CLI tool for oracle invocation

   • Library API for programmatic integration

   • Rule development SDK with validation tools

   • GitHub Actions workflow templates

   Claim 9: A governance artifact template set comprising:

   • Spec template for defining acceptable errors vs. violations

   • Contract template for liability tier assignment

   • SLA template for audit pass rate commitments

   • Dataset validity scoring checklist

   • Kill-switch governance trigger specification



                                          Page 36 of 48
Defensive Publication: Phase Mirror Dissonance                                  January 28, 2026


8.1.5   Implementation Profile Claims
Claim 10: A normative implementation profile for deterministic organizational diagnostic sys-
tems comprising:

  1. UTF-8 text encoding with Unicode NFC (Normalization Form C) preprocessing and rejec-
     tion of invalid byte sequences;

  2. Lexicographic JSON key ordering for canonical serialization, ensuring deterministic output
     regardless of internal data structure implementation;

  3. IEEE 754 double-precision floating-point arithmetic with round-to-nearest-even tie-breaking
     and mandatory rejection of special values (NaN, Infinity, -Infinity);

  4. ISO 8601 UTC timestamp normalization to second-level precision with mandatory ’Z’ time-
     zone designator;

  5. SHA-256 cryptographic hash computation over canonicalized UTF-8 byte sequences for
     verifiable content integrity;

  6. Impact × Tractability ranking formula with deterministic tie-breaking rules (descending
     impact, then alphabetical by type, then input order);

  7. Mandatory error rejection (fail-loud) for all non-conformant inputs including duplicate
     JSON keys, malformed timestamps, and out-of-range parameter values.

   Claim 11: A conformance test suite for verifying organizational diagnostic system imple-
mentations comprising:

  1. A plurality of input-output test vector pairs, each comprising:

        • A structured input object describing an organizational challenge or system configura-
          tion;
        • An expected canonical output object with deterministic field ordering and formatting;
        • A computed SHA-256 hash of the canonicalized output enabling cryptographic veri-
          fication of implementation correctness;

  2. Test cases covering at minimum:

        • End-to-end dissonance report generation from natural language input;
        • Tension ranking calculation with floating-point precision edge cases;
        • False-positive rate computation with pending event exclusion logic;
        • Circuit-breaker threshold triggering at exact boundary conditions;
        • UTF-8 normalization edge cases (decomposed vs. composed characters);
        • JSON key ordering with case-sensitive lexicographic comparison;
        • Floating-point special value rejection (NaN, Infinity validation);

  3. A validation procedure specifying:

        • Parsing and normalization steps for test vector inputs;
        • Canonical output generation requirements;
        • Hash computation methodology;

                                          Page 37 of 48
Defensive Publication: Phase Mirror Dissonance                                   January 28, 2026


         • Binary pass/fail criteria based on exact hash matching;

    4. Test vector metadata including format version, license terms (public domain or permissive
       open source), and references to the normative specification governing conformance.

    Variations Disclosed: The conformance test suite may be implemented in any machine-
readable format including but not limited to JSON, YAML, XML, Protocol Buffers, or custom
domain-specific languages. Test execution may be manual or automated via continuous integra-
tion systems. Pass/fail criteria may include tolerance thresholds for floating-point comparison in
addition to or instead of exact hash matching, provided tolerance values are explicitly specified.

8.2    Variations and Extensions
All variations of the disclosed methods, systems, and apparatuses are also placed in the public
domain, including but not limited to:

    • Alternative ranking formulas (e.g., Priority = Impact2 × Tractability)

    • Different output template structures (e.g., XML, YAML, Protocol Buffers instead of JSON)

    • Alternative storage backends (e.g., PostgreSQL, MongoDB instead of DynamoDB)

    • Different redaction algorithms (e.g., differential privacy, k-anonymity)

    • Integration with alternative CI/CD platforms (GitLab CI, CircleCI, Jenkins)

    • Graphical user interfaces for manual PMD analysis

    • Mobile applications for rapid triage mode

    • Browser extensions for inline GitHub PR diagnostics


9     Licensing and Usage
9.1    Creative Commons Attribution 4.0
This publication is released under CC BY 4.0, granting:

    • Share: Copy and redistribute in any medium or format

    • Adapt: Remix, transform, and build upon the material for any purpose, including com-
      mercially

    • Attribution: Must give appropriate credit, provide a link to the license, and indicate if
      changes were made

    • No Additional Restrictions: Cannot apply legal terms or technological measures that
      legally restrict others from doing anything the license permits




                                          Page 38 of 48
Defensive Publication: Phase Mirror Dissonance                              January 28, 2026


9.2    Trademark Notice
The following terms may be subject to trademark protection:

     • Phase Mirror Dissonance

     • Mirror Dissonance Oracle

    Trademark Usage: While the methodologies disclosed herein are freely usable, use of these
specific trademarks must comply with applicable trademark law and guidelines established by
the trademark holder(s).
    Certification Mark (Proposed): A certification program may be established whereby
implementations meeting specific criteria can be certified as “PMD-Compliant” This does not
restrict use of the underlying methodologies, only the certification mark itself.

9.3    Implementation Freedom
Any individual, organization, or entity is free to:

     • Implement the PMD methodology in any programming language or platform

     • Create commercial products or services based on these methods

     • Modify, extend, or adapt the framework for specific domains

     • Integrate with proprietary systems without disclosure obligations

     • Teach, train, and consult on these methodologies

    No Royalties or Fees: No royalties, fees, or permissions are required for any use of the
disclosed innovations.


10      Conclusion
10.1     Summary of Contributions
This defensive publication has established comprehensive prior art for:

  1. The Phase Mirror Dissonance methodology as a structured, repeatable framework for
     organizational diagnostics

  2. The five-step operating loop (Extract-Map-Rank-Produce-Question) as an algorithmic
     process

  3. Application to agentic AI governance, including the compliance-accuracy tradeoff
     framework and tiered oversight models

  4. The Mirror Dissonance Oracle as a callable, deterministic protocol for automated gov-
     ernance enforcement

  5. Novel mechanisms including false-positive calibration, circuit-breaker patterns, and
     redaction-by-capability

  6. Integration patterns for CI/CD pipelines, including GitHub Actions workflows and
     branch protection configurations

                                           Page 39 of 48
Defensive Publication: Phase Mirror Dissonance                                January 28, 2026


10.2   Impact and Availability
By publishing this disclosure under CC BY 4.0 and submitting to public archives (Zenodo,
arXiv), we ensure:

   • Perpetual Availability: These innovations remain freely accessible in perpetuity

   • Patent Prevention: No party can obtain patent protection on disclosed claims

   • Innovation Acceleration: Practitioners can build upon this foundation without legal
     uncertainty

   • Community Benefit: Organizations worldwide can adopt robust governance frameworks

10.3   Future Evolution
While this publication establishes prior art as of January 28, 2026, the Phase Mirror project
continues to evolve. Future developments will be documented through:

   • Version-controlled public repositories (GitHub, GitLab)

   • Updated defensive publications for novel extensions

   • Academic publications in peer-reviewed venues

   • Community contributions through open-source channels

    Invitation to Contribute: Researchers, practitioners, and organizations are encouraged to
extend, adapt, and improve upon these foundations. All derivative works that advance the state
of organizational governance and AI safety are welcomed.

10.4   Acknowledgments
This work represents the synthesis of insights from organizational theory, software engineering,
formal methods, causal inference, and governance practice. The authors acknowledge the broader
community of researchers and practitioners whose work has informed these innovations.
   Lead Theorist: Ryan O. Van Gelder Theorist, Worthington, Ohio, United States
   Publication Date: January 28, 2026
   Contact: For questions, clarifications, or collaboration inquiries regarding this defensive
publication, please refer to the project documentation and public communication channels.


Appendix A: Reference Implementation
A.1 Complete Rule Example
// packages/mirror-dissonance/src/rules/MD-002.ts

import { RuleDefinition, Finding, DetectionContext } from ’../types’;

/**
 * MD-002: Workflow Installs Unpinned Binaries
 *
 * Detects when GitHub Actions workflows install binaries without


                                         Page 40 of 48
Defensive Publication: Phase Mirror Dissonance                       January 28, 2026


 * pinning to specific versions or content hashes, creating supply
 * chain vulnerability.
 */
export const MD_002: RuleDefinition = {
  id: "MD-002",
  version: "1.1.0",
  tier: "A",

  fp_tolerance: {
     ceiling: 0.010,   // Max 1% FP rate
     floor: 0.001      // Target 0.1% FP rate
  },

  detect: async (ctx: DetectionContext): Promise<Finding[]> => {
    const findings: Finding[] = [];
    const workflowFiles = ctx.glob(’.github/workflows/*.{yml,yaml}’);

    for (const file of workflowFiles) {
      const content = await ctx.readFile(file);
      const lines = content.split(’\n’);

      for (let i = 0; i < lines.length; i++) {
        const line = lines[i];

         // Detect unpinned curl | sh patterns
         if (/curl\s+.+\|\s*sh/.test(line)) {
           findings.push({
             rule_id: "MD-002",
             rule_version: "1.1.0",
             severity: "high",
             claim: "Workflow installs binary via curl | sh without pinning",
             evidence: {
                file: file,
                line: i + 1,
                snippet: ctx.redactor.redact(line)
             },
             suggested_fix: "Pin to specific version or verify hash"
           });
         }

         // Detect unpinned npm/pip install -g
         if (/npm\s+install\s+-g\s+\S+(?!@[\d.]+)/.test(line)) {
           findings.push({
             rule_id: "MD-002",
             rule_version: "1.1.0",
             severity: "medium",
             claim: "npm install -g without version pin",
             evidence: {
               file: file,


                                       Page 41 of 48
Defensive Publication: Phase Mirror Dissonance                                January 28, 2026


                         line: i + 1,
                         snippet: ctx.redactor.redact(line)
                        },
                        suggested_fix: "Specify exact version: npm install -g pkg@1.2.3"
                      });
                  }
              }
          }

          return findings;
     },

     remediation: ‘
        Pinning Strategy Options:
        1. Version Pin: npm install -g package@1.2.3
        2. Hash Verification: curl -L <url> | shasum -a 256 -c <hash-file>
        3. Lockfile Commit: Use package-lock.json and commit
        4. Trusted Registry: Configure .npmrc to use internal mirror
     ‘,

     status: "blocking",

     promotion_criteria: ‘
       - 200+ workflow files scanned
       - FPR < 1% over 30 days
       - No critical bypasses detected
       - Remediation documented and tested
     ‘
};

A.2 CLI Entrypoint
#!/usr/bin/env node
// packages/mirror-dissonance/src/cli.ts

import { Command } from ’commander’;
import { runOracle } from ’./oracle’;
import { initializeRedactor } from ’./redaction’;
import { validateConfig } from ’./config’;

const program = new Command();

program
  .name(’mirror-dissonance’)
  .description(’Phase Mirror Dissonance Oracle for governance enforcement’)
  .version(’1.0.0’);

program
  .command(’check’)
  .description(’Run dissonance check’)

                                              Page 42 of 48
Defensive Publication: Phase Mirror Dissonance                               January 28, 2026


  .option(’--mode <type>’, ’Invocation mode’, ’pull_request’)
  .option(’--output <file>’, ’Output file path’, ’dissonance-report.json’)
  .option(’--strict’, ’Fail-closed mode’, false)
  .option(’--dry-run’, ’Warn-only mode’, false)
  .action(async (options) => {
    try {
      // Validate environment configuration
      validateConfig();

       // Initialize redaction subsystem
       await initializeRedactor();

       // Run oracle
       const report = await runOracle({
         mode: options.mode,
         strictMode: options.strict,
         dryRun: options.dryRun
       });

       // Write report
       await fs.writeFile(
          options.output,
          JSON.stringify(report, null, 2)
       );

      // Exit with appropriate code
      if (report.machine_decision.outcome === ’block’ && !options.dryRun) {
        console.error(’ Dissonance check BLOCKED’);
        process.exit(1);
      } else if (report.machine_decision.outcome === ’warn’) {
        console.warn(’ Dissonance warnings present’);
        process.exit(0);
      } else {
        console.log(’ Dissonance check passed’);
        process.exit(0);
      }
    } catch (error) {
      console.error(’Fatal error:’, error);
      process.exit(2);
    }
  });

program.parse();


Appendix B: Glossary
Agentic AI Autonomous artificial intelligence systems capable of reasoning, planning, and tak-
    ing actions without constant human prompting.



                                        Page 43 of 48
Defensive Publication: Phase Mirror Dissonance                                January 28, 2026


Artifact A concrete, binding object (spec, contract, SLA, dataset) that replaces abstract gov-
     ernance language with measurable commitments.

Binding Mechanism A formal process (forum, cadence, quorum, decision threshold) that re-
    places vague “collaboration” with enforceable structure.

Circuit Breaker A protective pattern that automatically degrades a system from blocking
     mode to warn-only when error rates exceed thresholds.

Compliance-Accuracy Tradeoff The fundamental choice in agentic systems between opti-
   mizing for regulatory compliance vs. optimal performance.

Defensive Publication A public disclosure of an invention intended to establish prior art and
    prevent patent claims.

Dissonance A structural tension, contradiction, or missing binding between components of a
     system or organization.

False-Positive (FP) A finding incorrectly flagged as problematic by a detection rule.

Lever A concrete intervention with assigned owner, measurable metric, and time horizon de-
    signed to address an identified dissonance.

Mirror The act of reflecting stated claims back objectively without endorsement to create an-
    alytical distance.

Phase A small, testable shift in process or policy designed to restore coherence by addressing
    dissonances.

PMD Phase Mirror Dissonance—the diagnostic methodology disclosed in this publication.

Precision Question A single, sharp clarifying question posed to resolve blocking ambiguities
     in decision-making.

Redaction-by-Capability A security pattern where the ability to create valid redacted text
    objects is restricted to code with access to a secret brand nonce.

Rule Registry A versioned, auditable collection of detection rules with explicit FP tolerance
    and promotion criteria.

Tiered Governance A model distinguishing levels of human oversight (fully autonomous, human-
     on-loop, human-in-loop, human-only) based on risk.

Vibe Claim Abstract, non-binding language (e.g., “align,” “collaborate”) lacking concrete op-
    erational definitions or enforcement mechanisms.


Appendix C: Normative Implementation Profile
This appendix specifies the canonical implementation requirements for deterministic, verifiable
outputs. Two independent implementations conforming to this profile MUST produce byte-
identical results when given identical inputs. These requirements constitute the normative spec-
ification for Phase Mirror Dissonance conformance.




                                         Page 44 of 48
Defensive Publication: Phase Mirror Dissonance                                   January 28, 2026


C.1 Text Encoding
Encoding: UTF-8 (RFC 3629)

Normalization: Unicode Normalization Form C (NFC) as specified in Unicode Standard Annex
    #15. All input text MUST be normalized to NFC before processing.

Invalid Sequences: Implementations MUST reject inputs containing invalid UTF-8 byte se-
     quences with an error. No replacement characters (U+FFFD) may be substituted.

Line Endings: All line endings MUST be normalized to LF (\n, U+000A) before processing.
     CRLF (\r\n) and CR (\r) sequences MUST be converted to LF.

Byte Order Mark (BOM): If a UTF-8 BOM (bytes EF BB BF) is present at the start of
    input, it MUST be stripped before processing.

Whitespace: Trailing whitespace on lines and trailing blank lines at end-of-file MUST be
    stripped before processing, except where explicitly required by format specifications (e.g.,
    JSON trailing newline).

    Rationale: NFC normalization ensures that "café" (composed é, U+00E9) and "café" (de-
composed e + combining acute, U+0065 U+0301) are treated as identical, preventing spurious
differences in hash computation.

C.2 JSON Serialization
Key Ordering: Object keys MUST be sorted lexicographically (ascending, case-sensitive, by
    Unicode codepoint) before serialization. This ensures deterministic output regardless of
    internal hash table ordering.

Duplicate Keys: JSON objects containing duplicate keys MUST be rejected with an error.
    Last-wins or first-wins semantics are NOT permitted.

Indentation: Two-space indentation for nested structures. No tabs permitted.

Trailing Newline: A single newline character (\n) MUST appear at the end of the serialized
     JSON document.

Number Format:         • No leading zeros except for "0." (e.g., "007" is invalid, "0.7" is valid)
        • No trailing decimal point (e.g., "42." is invalid, "42.0" or "42" are valid)
        • Exponential notation permitted for very large/small numbers (e.g., "1.23e+10")

Floating-Point: IEEE 754 double precision (binary64), round-to-nearest-even tie-breaking.

Special Values: The special floating-point values NaN, Infinity, and -Infinity MUST be
     rejected with an error. These values have no standard JSON representation.

String Escaping: Control characters (U+0000 through U+001F) MUST be escaped using
     \uXXXX notation. The solidus (/) MAY be escaped as \/ but is not required.

Null: The JSON null value is permitted and MUST serialize as lowercase null.

   Example Canonical JSON:



                                         Page 45 of 48
Defensive Publication: Phase Mirror Dissonance                                 January 28, 2026


{
    "items": [
       {
         "id": "MD-001-1",
         "severity": "high"
       }
    ],
    "meta": {
       "oracle_version": "1.0.0"
    }
}
     Note: Keys are sorted (items before meta), two-space indent, trailing newline.

C.3 Timestamp Format
Format: ISO 8601 date-time with UTC timezone: YYYY-MM-DDTHH:MM:SSZ

Timezone: All timestamps MUST be normalized to UTC. The literal character Z (Zulu time)
    MUST be used as the timezone designator. Numeric offsets (e.g., +00:00) are NOT per-
    mitted.

Precision: Second-level precision. Fractional seconds (milliseconds, microseconds) MUST NOT
     be included.

Calendar: Proleptic Gregorian calendar.

Leap Seconds: Implementations SHOULD handle leap seconds correctly but MAY represent
    them as 59.999... or 00 of the next minute, as long as the representation is deterministic.
Example: 2026-01-28T05:02:00Z

   Rationale: ISO 8601 is widely supported and unambiguous. Enforcing UTC eliminates
timezone conversion errors. Second precision is sufficient for governance timestamping while
avoiding floating-point subsecond edge cases.

C.4 Hash Computation
Algorithm: SHA-256 (FIPS 180-4)

Input: UTF-8 encoded bytes of the canonicalized content (after NFC normalization, JSON key
    sorting, etc.)

Representation: 64-character lowercase hexadecimal string with no prefix (no "0x", no "sha256:")
Verification: The hash MUST be computed over the exact byte sequence, including trailing
     newline if present in the canonical form.

     Example:
Input (UTF-8 bytes): {"key":"value"}\n
SHA-256: 8b4a2e1f9d3c7a5e8b2f4d6a9c1e5b7d3f9a5c7e1b9d4f8a2e6c9b5d3f7a1e4
     Validation Command (Linux/macOS):
echo -n ’{"key":"value"}’ | sha256sum

                                          Page 46 of 48
Defensive Publication: Phase Mirror Dissonance                                  January 28, 2026


C.5 Tension Ranking Formula
Impact Score: Integer in range [1, 10], where 10 = highest impact

Tractability Score: Floating-point in range [0.1, 1.0], rounded to 1 decimal place

Priority Calculation:
                                     Priority = Impact × Tractability
     Rounded to 1 decimal place using round-half-to-even (banker’s rounding).

Tie-Breaking: If two tensions have identical priority scores:

       1. Sort by Impact (descending: higher impact first)
       2. If Impact is equal, sort by tension type alphabetically (ascending)
       3. If type is equal, maintain original input order (stable sort)

   Example:

   • Tension A: Impact = 8, Tractability = 0.7 ⇒ Priority = 5.6

   • Tension B: Impact = 5, Tractability = 0.9 ⇒ Priority = 4.5

   • Tension C: Impact = 6, Tractability = 0.4 ⇒ Priority = 2.4

Ranking: A (5.6), B (4.5), C (2.4)

C.6 Conformance Testing
Implementations claiming Phase Mirror Dissonance conformance MUST pass all test vectors
published in the official test suite.
   Test Vector Repository:
https://zenodo.org/record/[DOI]/files/pmd_test_vectors.json
   Validation Procedure:

  1. Parse the input object from the test vector

  2. Apply normalization according to C.1 (UTF-8 NFC)

  3. Generate output according to specification

  4. Serialize output as canonical JSON according to C.2

  5. Compute SHA-256 hash according to C.4

  6. Compare computed hash to sha256 field in test vector

  7. Test passes if and only if hashes match exactly (all 64 hex digits)

   Test Suite Coverage:

   • Minimal dissonance report generation (end-to-end)

   • Tension ranking with floating-point precision

   • False-positive rate calculation with edge cases

   • Circuit-breaker threshold triggering

                                           Page 47 of 48
Defensive Publication: Phase Mirror Dissonance                                  January 28, 2026


   • UTF-8 normalization (NFD vs. NFC)

   • JSON key ordering (case-sensitive lexicographic)

   • Floating-point special value rejection (NaN, Infinity)

C.7 Error Handling
Implementations MUST fail loudly and immediately when encountering:

   • Invalid UTF-8 byte sequences

   • JSON duplicate keys

   • JSON NaN/Infinity values

   • Timestamps with non-UTC timezone

   • Impacts outside [1, 10] range

   • Tractability outside [0.1, 1.0] range

   Silent failures, warnings-only, or best-effort processing are NOT conformant.

C.8 Reference Implementation
A reference implementation in TypeScript/JavaScript is planned for publication alongside this
specification. The reference implementation will:

   • Pass all conformance test vectors

   • Include detailed comments mapping code to this specification

   • Be released under MIT License for maximum reusability

   • Serve as the canonical interpretation in case of specification ambiguity

    Note: Until the reference implementation is published, this written specification is authori-
tative. In case of ambiguity, prioritize determinism and verifiability over performance or conve-
nience.
    sha256:0c5f5b77a9f722bb21d5cf0f5d4d066002c3dc8f4f3c962eb8027ae83f1fad1b




                                             Page 48 of 48

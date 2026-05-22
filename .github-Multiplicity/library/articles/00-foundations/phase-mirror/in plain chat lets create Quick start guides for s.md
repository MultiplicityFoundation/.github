---
slug: in-plain-chat-lets-create-quick-start-guides-for-s
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 00-foundations/phase-mirror/in plain chat lets create Quick start guides for
    s.md
  last_synced: '2026-03-20T17:17:21.919336Z'
---

![](media/image-19209cf1bf2d0ed940cc1c7e89b68aa61a955723.png){width="2.6466666666666665in"
height="0.6666666666666666in"}

**in plain chat lets create Quick start guides for specific compliance
packs (EU AI Act, Financial Services)**

Here are comprehensive quick start guides for the EU AI Act and
Financial Services compliance packs:

**PHASE MIRROR COMPLIANCE PACK QUICK START GUIDES**

**Accelerated Implementation for Regulatory Requirements**

**Version:** 2.0 \| **Date:** January 2026

**QUICK START GUIDE: EU AI ACT COMPLIANCE PACK**

**Getting Compliant in 30 Days**

**OVERVIEW**

**What This Pack Does**

The EU AI Act Compliance Pack helps organizations prepare for and
maintain compliance with the European Union\'s AI Act (Regulation
2024/1689), which establishes a comprehensive regulatory framework for
AI systems in the EU.

  ------------------------------- -----------------------------------------------------------------
  Capability                      Description
  **Risk Classification**         Automatically classify AI systems per Annex III categories
  **High-Risk Requirements**      Track compliance with Articles 9-15 requirements
  **Conformity Assessment**       Guided workflows for self-assessment and third-party conformity
  **Documentation Templates**     Pre-built templates for technical documentation
  **Fundamental Rights Impact**   FRIA assessment workflows and templates
  **Incident Reporting**          Track and report serious incidents per Article 62
  **Provider/Deployer Views**     Role-specific dashboards and requirements
  ------------------------------- -----------------------------------------------------------------

**Who This Guide Is For**

  ----------------- --------------------------------------------------
  Role              Primary Focus
  **AI Provider**   You develop/train AI systems placed on EU market
  **AI Deployer**   You use AI systems in your operations within EU
  **Importer**      You bring non-EU AI systems into EU market
  **Distributor**   You make AI systems available in supply chain
  ----------------- --------------------------------------------------

**Key Deadlines**

  ------------------- ------------------------------------------
  Deadline            Requirement
  **February 2025**   Prohibited AI practices ban takes effect
  **August 2025**     GPAI and governance provisions apply
  **August 2026**     High-risk AI system requirements apply
  **August 2027**     Certain Annex I systems requirements
  ------------------- ------------------------------------------

**DAY 1-5: INITIAL SETUP**

**Step 1: Enable the EU AI Act Pack**

NAVIGATION: Settings → Compliance → EU AI Act → Enable\
\
┌─────────────────────────────────────────────────────────────────┐\
│ EU AI ACT COMPLIANCE PACK SETUP │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ Organization Role in AI Value Chain │\
│ ───────────────────────────────────────────────────────────── │\
│ Select all that apply: │\
│ │\
│ ☐ Provider (develop, train, place on market) │\
│ ☐ Deployer (use AI systems under your authority) │\
│ ☐ Importer (bring non-EU AI to EU market) │\
│ ☐ Distributor (supply chain participant) │\
│ │\
│ Geographic Scope │\
│ ───────────────────────────────────────────────────────────── │\
│ ☐ AI systems used within EU │\
│ ☐ AI systems whose output is used in EU │\
│ ☐ AI systems placed on EU market │\
│ │\
│ Notified Body Relationship (if applicable) │\
│ ───────────────────────────────────────────────────────────── │\
│ Notified Body: \[None selected ▼\] │\
│ │\
│ \[Cancel\] \[Save & Continue\] │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**Step 2: Configure Risk Classification Engine**

The EU AI Act defines four risk levels. Configure how your systems map
to these:

NAVIGATION: Compliance → EU AI Act → Classification Settings\
\
┌─────────────────────────────────────────────────────────────────┐\
│ RISK CLASSIFICATION CONFIGURATION │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ EU AI ACT RISK LEVELS │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ ┌─────────────────────────────────────────────────────────┐ │\
│ │ UNACCEPTABLE RISK (Prohibited) Article 5 │ │\
│ │ ─────────────────────────────────────────────────────── │ │\
│ │ • Social scoring by public authorities │ │\
│ │ • Exploitation of vulnerabilities │ │\
│ │ • Real-time biometric identification (with exceptions) │ │\
│ │ • Emotion recognition in workplace/education │ │\
│ │ • Untargeted scraping for facial recognition │ │\
│ │ │ │\
│ │ Action: Systems flagged → Immediate review required │ │\
│ └─────────────────────────────────────────────────────────┘ │\
│ │\
│ ┌─────────────────────────────────────────────────────────┐ │\
│ │ HIGH RISK (Annex III) Articles 6-51 │ │\
│ │ ─────────────────────────────────────────────────────── │ │\
│ │ Auto-classify when system matches: │ │\
│ │ │ │\
│ │ ☑ Biometric identification/categorization │ │\
│ │ ☑ Critical infrastructure management │ │\
│ │ ☑ Education/vocational training access │ │\
│ │ ☑ Employment, worker management, self-employment │ │\
│ │ ☑ Essential services access (public benefits, credit) │ │\
│ │ ☑ Law enforcement │ │\
│ │ ☑ Migration, asylum, border control │ │\
│ │ ☑ Justice and democratic processes │ │\
│ │ │ │\
│ │ Safety component in Annex I products: │ │\
│ │ ☑ Machinery, toys, medical devices, vehicles, etc. │ │\
│ └─────────────────────────────────────────────────────────┘ │\
│ │\
│ ┌─────────────────────────────────────────────────────────┐ │\
│ │ LIMITED RISK Article 50 │ │\
│ │ ─────────────────────────────────────────────────────── │ │\
│ │ Transparency obligations apply: │ │\
│ │ │ │\
│ │ ☑ Chatbots and conversational AI │ │\
│ │ ☑ Emotion recognition systems │ │\
│ │ ☑ Biometric categorization systems │ │\
│ │ ☑ Deep fake / synthetic content generators │ │\
│ └─────────────────────────────────────────────────────────┘ │\
│ │\
│ ┌─────────────────────────────────────────────────────────┐ │\
│ │ MINIMAL RISK │ │\
│ │ ─────────────────────────────────────────────────────── │ │\
│ │ No specific obligations (voluntary codes) │ │\
│ │ │ │\
│ │ Examples: Spam filters, inventory management, │ │\
│ │ recommendation systems (non-manipulative) │ │\
│ └─────────────────────────────────────────────────────────┘ │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**Step 3: Map Phase Mirror Risk Tiers to EU AI Act**

┌─────────────────────────────────────────────────────────────────┐\
│ RISK TIER MAPPING │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ Phase Mirror Tier │ EU AI Act Classification │\
│ ─────────────────────┼──────────────────────────────────── │\
│ Critical │ High-Risk (Annex III) │\
│ High │ High-Risk or Limited Risk │\
│ Medium │ Limited Risk or Minimal Risk │\
│ Low │ Minimal Risk │\
│ │\
│ ☑ Auto-elevate tier when EU AI Act classification is higher │\
│ ☑ Flag mismatches for Governance Lead review │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**DAY 6-15: SYSTEM CLASSIFICATION**

**Step 4: Run Classification on Existing Systems**

NAVIGATION: Compliance → EU AI Act → Classification → Run
Classification\
\
┌─────────────────────────────────────────────────────────────────┐\
│ BULK CLASSIFICATION │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ Scope: ○ All AI Systems ○ Unclassified Only ○ Selected │\
│ │\
│ \[Run Classification\] │\
│ │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ CLASSIFICATION RESULTS │\
│ │\
│ ┌──────────────────────────────────────────────────────────┐ │\
│ │ Total Systems Analyzed: 47 │ │\
│ │ │ │\
│ │ 🔴 Potentially Prohibited: 1 \[Review Immediately\] │ │\
│ │ 🟠 High-Risk (Annex III): 12 \[View Systems\] │ │\
│ │ 🟡 Limited Risk: 8 \[View Systems\] │ │\
│ │ 🟢 Minimal Risk: 23 \[View Systems\] │ │\
│ │ ⚪ Needs Manual Review: 3 \[Review Now\] │ │\
│ └──────────────────────────────────────────────────────────┘ │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**Step 5: Review and Confirm Classifications**

For each system, confirm or adjust the automated classification:

┌─────────────────────────────────────────────────────────────────┐\
│ SYSTEM: Customer Credit Scoring Model │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ AUTOMATED CLASSIFICATION: 🟠 HIGH-RISK │\
│ │\
│ Reason: Matches Annex III Category 5(b) │\
│ \"AI systems intended to be used to evaluate the │\
│ creditworthiness of natural persons\" │\
│ │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ CLASSIFICATION QUESTIONNAIRE │\
│ │\
│ 1. Does this system evaluate creditworthiness of │\
│ natural persons (individuals)? │\
│ ○ Yes ○ No ○ Partially │\
│ │\
│ 2. Is the output used to determine access to credit │\
│ or credit terms? │\
│ ○ Yes, directly determines ○ Yes, influences │\
│ ○ No, advisory only ○ No involvement │\
│ │\
│ 3. Are EU residents affected by this system? │\
│ ○ Yes ○ No ○ Unknown │\
│ │\
│ 4. Is this a safety component of another product? │\
│ ○ Yes (specify product) ○ No │\
│ │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ FINAL CLASSIFICATION │\
│ ○ Accept: High-Risk (Annex III, Category 5b) │\
│ ○ Override: \[Select different classification ▼\] │\
│ Justification:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│\
│ │\
│ \[Save Classification\] │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**Classification Decision Tree**

┌─────────────────────────┐\
│ START: AI System │\
└───────────┬─────────────┘\
│\
▼\
┌─────────────────────────┐\
│ Does it fall under │\
│ Article 5 prohibitions? │\
└───────────┬─────────────┘\
│\
┌───────────┴───────────┐\
YES NO\
│ │\
▼ ▼\
┌─────────────────┐ ┌─────────────────────────┐\
│ 🔴 PROHIBITED │ │ Is it a safety │\
│ Cannot deploy │ │ component of Annex I │\
│ in EU │ │ product? │\
└─────────────────┘ └───────────┬─────────────┘\
│\
┌───────────┴───────────┐\
YES NO\
│ │\
▼ ▼\
┌─────────────────┐ ┌─────────────────────────┐\
│ 🟠 HIGH-RISK │ │ Listed in Annex III │\
│ (Annex I) │ │ use cases? │\
└─────────────────┘ └───────────┬─────────────┘\
│\
┌───────────┴───────────┐\
YES NO\
│ │\
▼ ▼\
┌─────────────────┐ ┌─────────────────────────┐\
│ 🟠 HIGH-RISK │ │ Transparency │\
│ (Annex III) │ │ requirements apply? │\
└─────────────────┘ │ (chatbot, deepfake, │\
│ emotion recognition) │\
└───────────┬─────────────┘\
│\
┌───────────┴───────────┐\
YES NO\
│ │\
▼ ▼\
┌─────────────────┐ ┌─────────────────┐\
│ 🟡 LIMITED RISK │ │ 🟢 MINIMAL RISK │\
│ (transparency) │ │ (voluntary) │\
└─────────────────┘ └─────────────────┘

**DAY 16-25: HIGH-RISK SYSTEM REQUIREMENTS**

**Step 6: Configure High-Risk Requirements Tracking**

For each high-risk system, the pack tracks compliance with Articles
9-15:

NAVIGATION: Compliance → EU AI Act → High-Risk Requirements\
\
┌─────────────────────────────────────────────────────────────────┐\
│ HIGH-RISK SYSTEM: Customer Credit Scoring Model │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ COMPLIANCE STATUS: 6 of 9 requirements met (67%) │\
│ ████████████████░░░░░░░░ │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ Article 9: Risk Management System ⚠ PARTIAL │\
│ ───────────────────────────────────────────────────────────── │\
│ ☑ Risk management process established │\
│ ☑ Risks identified and analyzed │\
│ ☐ Residual risk evaluation documented │\
│ ☑ Risk mitigation measures implemented │\
│ ☐ Testing procedures for risk mitigation │\
│ │\
│ \[Upload Evidence\] \[View Details\] \[Create Action Item\] │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ Article 10: Data and Data Governance ✓ MET │\
│ ───────────────────────────────────────────────────────────── │\
│ ☑ Training data governance practices documented │\
│ ☑ Data quality criteria defined │\
│ ☑ Relevant, representative data verified │\
│ ☑ Bias examination conducted │\
│ ☑ Data gaps identified and addressed │\
│ │\
│ Evidence: Data Governance Doc v2.1 (uploaded 2025-11-15) │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ Article 11: Technical Documentation ⚠ PARTIAL│\
│ ───────────────────────────────────────────────────────────── │\
│ ☑ General description of AI system │\
│ ☑ Detailed description of elements and development │\
│ ☐ Monitoring, functioning, control description │\
│ ☑ Risk management system description │\
│ ☐ Description of changes through lifecycle │\
│ ☑ Standards applied (list) │\
│ ☑ EU declaration of conformity │\
│ │\
│ \[Use Template\] \[Upload Document\] \[Create Action Item\] │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ Article 12: Record-Keeping ✓ MET │\
│ ───────────────────────────────────────────────────────────── │\
│ ☑ Automatic logging enabled │\
│ ☑ Logs include periods, reference databases, input data │\
│ ☑ Logs traceable throughout lifecycle │\
│ ☑ Logging proportionate to system risk │\
│ │\
│ Evidence: Integrated with Phase Mirror audit trail │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ Article 13: Transparency and Information ✓ MET │\
│ ───────────────────────────────────────────────────────────── │\
│ ☑ Instructions for use provided │\
│ ☑ Capabilities and limitations documented │\
│ ☑ Intended purpose clearly stated │\
│ ☑ Human oversight measures described │\
│ ☑ Expected accuracy/performance metrics │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ Article 14: Human Oversight ✓ MET │\
│ ───────────────────────────────────────────────────────────── │\
│ ☑ Human oversight measures designed │\
│ ☑ Humans can understand capabilities/limitations │\
│ ☑ Humans can monitor operation │\
│ ☑ Humans can intervene/interrupt │\
│ ☑ \"Stop\" functionality implemented │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ Article 15: Accuracy, Robustness, Cybersecurity ✗ NOT MET│\
│ ───────────────────────────────────────────────────────────── │\
│ ☑ Appropriate accuracy levels achieved │\
│ ☐ Robustness against errors/faults documented │\
│ ☐ Resilience against manipulation tested │\
│ ☐ Cybersecurity measures implemented │\
│ │\
│ \[View Gap Analysis\] \[Create Action Items\] │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**Step 7: Use Technical Documentation Template**

NAVIGATION: Compliance → EU AI Act → Templates → Technical
Documentation\
\
┌─────────────────────────────────────────────────────────────────┐\
│ TECHNICAL DOCUMENTATION TEMPLATE │\
│ (Per Annex IV Requirements) │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ SECTION 1: GENERAL DESCRIPTION │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ 1.1 Provider Information │\
│ ┌────────────────────────────────────────────────────────────┐ │\
│ │ Provider Name:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│ │\
│ │ Provider Address:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│ │\
│ │ Authorized Representative (if non-EU):
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ │ │\
│ │ Contact Person:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│ │\
│ └────────────────────────────────────────────────────────────┘ │\
│ │\
│ 1.2 AI System Identification │\
│ ┌────────────────────────────────────────────────────────────┐ │\
│ │ System Name:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│ │\
│ │ Version:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│ │\
│ │ Unique Identifier:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│ │\
│ │ Date of Placing on Market:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ │ │\
│ └────────────────────────────────────────────────────────────┘ │\
│ │\
│ 1.3 Intended Purpose │\
│ ┌────────────────────────────────────────────────────────────┐ │\
│ │ \[Describe the specific purpose for which the AI system │ │\
│ │ is intended to be used. Be precise about use cases, │ │\
│ │ deployment context, and expected users.\] │ │\
│ │ │ │\
│ │
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│ │\
│ │
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│ │\
│ │
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│ │\
│ └────────────────────────────────────────────────────────────┘ │\
│ │\
│ 1.4 Interaction with Other Systems │\
│ ┌────────────────────────────────────────────────────────────┐ │\
│ │ Hardware:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│ │\
│ │ Software:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│ │\
│ │ APIs/Interfaces:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│ │\
│ │ Data Sources:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│ │\
│ └────────────────────────────────────────────────────────────┘ │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ SECTION 2: DETAILED DESCRIPTION OF ELEMENTS │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ 2.1 Development Process │\
│ ┌────────────────────────────────────────────────────────────┐ │\
│ │ Development Methodology:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ │ │\
│ │ Design Specifications: \[Upload document\] │ │\
│ │ Development Tools Used:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ │ │\
│ │ Third-Party Components:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ │ │\
│ └────────────────────────────────────────────────────────────┘ │\
│ │\
│ 2.2 Algorithm/Model Description │\
│ ┌────────────────────────────────────────────────────────────┐ │\
│ │ Model Type:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│ │\
│ │ Architecture:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│ │\
│ │ Training Approach:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│ │\
│ │ Key Parameters:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│ │\
│ │ Decision Logic: \[Upload technical specification\] │ │\
│ └────────────────────────────────────────────────────────────┘ │\
│ │\
│ \[Continue to Sections 3-8\...\] │\
│ │\
│ \[Save Draft\] \[Preview\] \[Export PDF\] \[Attach to System\] │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**DAY 26-30: CONFORMITY ASSESSMENT & GO-LIVE**

**Step 8: Complete Conformity Assessment**

NAVIGATION: Compliance → EU AI Act → Conformity Assessment\
\
┌─────────────────────────────────────────────────────────────────┐\
│ CONFORMITY ASSESSMENT WORKFLOW │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ SYSTEM: Customer Credit Scoring Model │\
│ CLASSIFICATION: High-Risk (Annex III, Category 5b) │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ ASSESSMENT PATH │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ For this system, the applicable conformity assessment is: │\
│ │\
│ ☑ INTERNAL CONTROL (Annex VI) │\
│ Self-assessment by provider │\
│ Applicable to: Credit scoring (Annex III, 5b) │\
│ │\
│ ☐ THIRD-PARTY ASSESSMENT (Annex VII) │\
│ Required for: Biometric identification for law enforcement │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ INTERNAL CONTROL CHECKLIST (Annex VI) │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ Step 1: Quality Management System │\
│ ☑ QMS established and documented │\
│ ☑ Covers design, development, testing │\
│ ☑ Post-market monitoring procedures │\
│ ☑ Document management procedures │\
│ │\
│ Step 2: Technical Documentation Review │\
│ ☑ Technical documentation complete (Annex IV) │\
│ ☑ Documentation demonstrates compliance │\
│ ☑ Documentation kept up to date │\
│ │\
│ Step 3: Conformity Verification │\
│ ☑ System complies with Chapter 2 requirements │\
│ ☑ Testing confirms compliance │\
│ ☐ All non-conformities addressed │\
│ │\
│ Step 4: Declaration Preparation │\
│ ☐ EU Declaration of Conformity drafted │\
│ ☐ Declaration signed by authorized person │\
│ │\
│ \[Generate Declaration of Conformity\] │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**Step 9: Generate EU Declaration of Conformity**

┌─────────────────────────────────────────────────────────────────┐\
│ EU DECLARATION OF CONFORMITY │\
│ (Per Article 47 and Annex V) │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ EU DECLARATION OF CONFORMITY │\
│ │\
│ 1. AI System Identification │\
│ Name: Customer Credit Scoring Model │\
│ Version: 3.2.1 │\
│ Unique ID: EU-AI-2026-CCSM-001 │\
│ │\
│ 2. Provider Details │\
│ Name: \[Organization Name\] │\
│ Address: \[Full Address\] │\
│ Contact: \[Authorized Representative\] │\
│ │\
│ 3. Declaration │\
│ This declaration of conformity is issued under the sole │\
│ responsibility of the provider. │\
│ │\
│ The AI system described above is in conformity with │\
│ Regulation (EU) 2024/1689 (AI Act). │\
│ │\
│ 4. Conformity Assessment │\
│ Procedure: Internal control (Annex VI) │\
│ Date of assessment: \[Date\] │\
│ │\
│ 5. Standards Applied │\
│ • ISO/IEC 42001:2023 (AI Management System) │\
│ • ISO/IEC 23894:2023 (AI Risk Management) │\
│ • \[Other applicable standards\] │\
│ │\
│ 6. Signature │\
│ Signed for and on behalf of:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ │\
│ Name:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│\
│ Function:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│\
│ Date:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│\
│ Place:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│\
│ │\
│ \[Download PDF\] \[Digital Signature\] \[Register with Authority\] │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**Step 10: Set Up Ongoing Monitoring**

NAVIGATION: Compliance → EU AI Act → Post-Market Monitoring\
\
┌─────────────────────────────────────────────────────────────────┐\
│ POST-MARKET MONITORING CONFIGURATION │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ SYSTEM: Customer Credit Scoring Model │\
│ │\
│ POST-MARKET MONITORING PLAN (Article 72) │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ Monitoring Activities: │\
│ ☑ Performance monitoring (accuracy, drift) │\
│ ☑ Incident collection and analysis │\
│ ☑ User feedback collection │\
│ ☑ Complaint handling │\
│ ☑ Regulatory update tracking │\
│ │\
│ Monitoring Frequency: │\
│ • Performance metrics: \[Daily ▼\] │\
│ • Bias monitoring: \[Weekly ▼\] │\
│ • Full review: \[Monthly ▼\] │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ SERIOUS INCIDENT REPORTING (Article 73) │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ Configure automatic alerts for: │\
│ ☑ Death or serious damage to health │\
│ ☑ Serious and irreversible disruption to critical infrastructure│\
│ ☑ Breach of fundamental rights obligations │\
│ ☑ Serious harm to property, environment │\
│ │\
│ Reporting timeline: Within 15 days (2 days for death/health) │\
│ │\
│ Designated contact for authorities: │\
│ Name:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│\
│ Email:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│\
│ Phone:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│\
│ │\
└─────────────────────────────────────────────────────────────────┘

**EU AI ACT QUICK REFERENCE**

**Annex III High-Risk Categories**

  -------------------------------- ----------------------------------- ------------------------------------------
  Category                         Description                         Examples
  **1. Biometrics**                Identification and categorization   Facial recognition, emotion detection
  **2. Critical Infrastructure**   Safety components                   Traffic management, utilities
  **3. Education**                 Access and assessment               Admission scoring, exam proctoring
  **4. Employment**                Recruitment and management          CV screening, performance evaluation
  **5. Essential Services**        Access determination                Credit scoring, insurance pricing
  **6. Law Enforcement**           Investigation and prediction        Risk assessment, evidence evaluation
  **7. Migration**                 Border and asylum                   Document authentication, risk assessment
  **8. Justice**                   Legal research and decisions        Sentencing assistance, case analysis
  -------------------------------- ----------------------------------- ------------------------------------------

**Key Provider Obligations Summary**

  ------------------------- --------- -----------------------------------------------
  Obligation                Article   Key Requirement
  Risk Management           Art. 9    Establish and maintain risk management system
  Data Governance           Art. 10   Ensure training data quality and relevance
  Technical Documentation   Art. 11   Complete documentation per Annex IV
  Record-Keeping            Art. 12   Automatic logging of operations
  Transparency              Art. 13   Clear instructions for deployers
  Human Oversight           Art. 14   Design for effective human oversight
  Accuracy & Robustness     Art. 15   Appropriate levels throughout lifecycle
  Conformity Assessment     Art. 43   Before placing on market
  Registration              Art. 49   Register in EU database
  Post-Market Monitoring    Art. 72   Ongoing monitoring system
  ------------------------- --------- -----------------------------------------------

**QUICK START GUIDE: FINANCIAL SERVICES COMPLIANCE PACK**

**Meeting SR 11-7 and Fair Lending Requirements in 30 Days**

**OVERVIEW**

**What This Pack Does**

The Financial Services Compliance Pack helps banks, credit unions,
insurance companies, and other financial institutions comply with model
risk management requirements and fair lending regulations.

  ---------------------------- --------------------------------------------------
  Capability                   Description
  **SR 11-7 Alignment**        Map to OCC/Fed model risk management guidance
  **Model Inventory**          Comprehensive model inventory management
  **Validation Tracking**      Initial and ongoing validation workflows
  **Fair Lending**             Bias monitoring and adverse action documentation
  **Examination Prep**         Generate documentation packages for examiners
  **Three Lines of Defense**   Role-based views for 1st, 2nd, 3rd line
  ---------------------------- --------------------------------------------------

**Who This Guide Is For**

  -------------------------------- -----------------------------------------------
  Role                             Responsibilities
  **Model Risk Officer**           Overall MRM program, examination readiness
  **Model Owner (1st Line)**       Model development, documentation, performance
  **Model Validator (2nd Line)**   Independent validation, challenge
  **Internal Audit (3rd Line)**    MRM program effectiveness review
  **Compliance Officer**           Fair lending, regulatory compliance
  -------------------------------- -----------------------------------------------

**Key Regulatory References**

  ---------------------- ----------------- -----------------------------
  Regulation             Agency            Focus
  **SR 11-7**            Federal Reserve   Model Risk Management
  **OCC 2011-12**        OCC               Model Risk Management
  **ECOA / Reg B**       CFPB              Fair Lending
  **Fair Housing Act**   HUD               Fair Lending
  **SR 15-18**           Federal Reserve   Third-Party Risk Management
  ---------------------- ----------------- -----------------------------

**DAY 1-5: INITIAL SETUP**

**Step 1: Enable the Financial Services Pack**

NAVIGATION: Settings → Compliance → Financial Services → Enable\
\
┌─────────────────────────────────────────────────────────────────┐\
│ FINANCIAL SERVICES COMPLIANCE PACK SETUP │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ Organization Type │\
│ ───────────────────────────────────────────────────────────── │\
│ ○ Bank (National) │\
│ ○ Bank (State Member) │\
│ ○ Bank (State Non-Member) │\
│ ○ Credit Union │\
│ ○ Insurance Company │\
│ ○ Broker-Dealer │\
│ ○ Other Financial Institution │\
│ │\
│ Primary Regulator │\
│ ───────────────────────────────────────────────────────────── │\
│ ☐ OCC (Office of the Comptroller of the Currency) │\
│ ☐ Federal Reserve │\
│ ☐ FDIC │\
│ ☐ NCUA │\
│ ☐ State Banking Department │\
│ ☐ State Insurance Department │\
│ ☐ SEC │\
│ ☐ FINRA │\
│ │\
│ Asset Size │\
│ ───────────────────────────────────────────────────────────── │\
│ ○ Under \$1B │\
│ ○ \$1B - \$10B │\
│ ○ \$10B - \$50B │\
│ ○ \$50B - \$250B │\
│ ○ Over \$250B (G-SIB) │\
│ │\
│ \[Cancel\] \[Save & Continue\] │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**Step 2: Configure Model Risk Tiers**

Align Phase Mirror with your existing Model Risk Management (MRM)
policy:

NAVIGATION: Compliance → Financial Services → Model Risk Tiers\
\
┌─────────────────────────────────────────────────────────────────┐\
│ MODEL RISK TIER CONFIGURATION │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ Map your MRM policy tiers to Phase Mirror: │\
│ │\
│ ┌───────────────────────────────────────────────────────────┐ │\
│ │ TIER 1: CRITICAL MODELS │ │\
│ │ ───────────────────────────────────────────────────────── │ │\
│ │ Phase Mirror Tier: \[Critical ▼\] │ │\
│ │ │ │\
│ │ Criteria (select all that apply): │ │\
│ │ ☑ Material impact on financial statements │ │\
│ │ ☑ Direct customer credit/pricing decisions │ │\
│ │ ☑ Regulatory capital calculations │ │\
│ │ ☑ CCAR/DFAST stress testing │ │\
│ │ ☑ BSA/AML transaction monitoring │ │\
│ │ ☑ Model failure could result in \>\$X million loss │ │\
│ │ Threshold: \[\$10,000,000\] │ │\
│ │ │ │\
│ │ Validation Requirements: │ │\
│ │ • Initial validation: Required before production │ │\
│ │ • Ongoing validation: Annual │ │\
│ │ • Validator independence: Fully independent (2nd line) │ │\
│ └───────────────────────────────────────────────────────────┘ │\
│ │\
│ ┌───────────────────────────────────────────────────────────┐ │\
│ │ TIER 2: HIGH-RISK MODELS │ │\
│ │ ───────────────────────────────────────────────────────── │ │\
│ │ Phase Mirror Tier: \[High ▼\] │ │\
│ │ │ │\
│ │ Criteria (select all that apply): │ │\
│ │ ☑ Moderate financial statement impact │ │\
│ │ ☑ Customer-facing decisions (non-credit) │ │\
│ │ ☑ Operational risk management │ │\
│ │ ☑ Investment/portfolio management │ │\
│ │ ☑ Fraud detection │ │\
│ │ │ │\
│ │ Validation Requirements: │ │\
│ │ • Initial validation: Required before production │ │\
│ │ • Ongoing validation: Every 18 months │ │\
│ │ • Validator independence: Independent (can be 1.5 line) │ │\
│ └───────────────────────────────────────────────────────────┘ │\
│ │\
│ ┌───────────────────────────────────────────────────────────┐ │\
│ │ TIER 3: MODERATE-RISK MODELS │ │\
│ │ ───────────────────────────────────────────────────────── │ │\
│ │ Phase Mirror Tier: \[Medium ▼\] │ │\
│ │ │ │\
│ │ Criteria: │ │\
│ │ ☑ Limited financial impact │ │\
│ │ ☑ Internal operations support │ │\
│ │ ☑ Management reporting │ │\
│ │ │ │\
│ │ Validation Requirements: │ │\
│ │ • Initial validation: Required │ │\
│ │ • Ongoing validation: Every 2 years │ │\
│ │ • Validator independence: Review by qualified peer │ │\
│ └───────────────────────────────────────────────────────────┘ │\
│ │\
│ ┌───────────────────────────────────────────────────────────┐ │\
│ │ TIER 4: LOW-RISK MODELS │ │\
│ │ ───────────────────────────────────────────────────────── │ │\
│ │ Phase Mirror Tier: \[Low ▼\] │ │\
│ │ │ │\
│ │ Criteria: │ │\
│ │ ☑ Minimal financial impact │ │\
│ │ ☑ Experimental/developmental │ │\
│ │ ☑ Challenger models not yet in production │ │\
│ │ │ │\
│ │ Validation Requirements: │ │\
│ │ • Initial validation: Documented review │ │\
│ │ • Ongoing validation: Every 3 years or material change │ │\
│ │ • Validator independence: Self-assessment acceptable │ │\
│ └───────────────────────────────────────────────────────────┘ │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**Step 3: Define Model Definition Criteria**

Configure what qualifies as a \"model\" per SR 11-7:

┌─────────────────────────────────────────────────────────────────┐\
│ MODEL DEFINITION CRITERIA │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ SR 11-7 Definition: │\
│ \"A quantitative method, system, or approach that applies │\
│ statistical, economic, financial, or mathematical theories, │\
│ techniques, and assumptions to process input data into │\
│ quantitative estimates.\" │\
│ │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ INCLUDE AS MODELS: │\
│ ☑ Credit scoring and underwriting models │\
│ ☑ Pricing models (loans, deposits, insurance) │\
│ ☑ Valuation models (securities, derivatives, MSRs) │\
│ ☑ CECL/ALLL models │\
│ ☑ Capital models (Basel, stress testing) │\
│ ☑ ALM/interest rate risk models │\
│ ☑ Fraud/AML models │\
│ ☑ Marketing/propensity models (if used for decisions) │\
│ ☑ Machine learning models in production │\
│ ☑ Third-party/vendor models │\
│ ☑ Challenger models │\
│ │\
│ EXCLUDE FROM MODEL INVENTORY: │\
│ ☑ Simple calculations without judgment │\
│ ☑ Data aggregation tools │\
│ ☑ Pure reporting systems │\
│ ☐ Spreadsheet models (configure below) │\
│ │\
│ Spreadsheet Treatment: │\
│ ○ Include all spreadsheets with calculations │\
│ ○ Include only material spreadsheets (\>\$X impact) │\
│ ○ Exclude spreadsheets (managed separately) │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**DAY 6-15: MODEL INVENTORY**

**Step 4: Import or Build Model Inventory**

NAVIGATION: Compliance → Financial Services → Model Inventory\
\
┌─────────────────────────────────────────────────────────────────┐\
│ MODEL INVENTORY MANAGEMENT │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ IMPORT OPTIONS │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ ☐ Import from existing inventory │\
│ \[Upload CSV/Excel\] │\
│ Template: \[Download Model Inventory Template\] │\
│ │\
│ ☐ Sync from Phase Mirror AI Systems │\
│ (Systems tagged as \"models\" will be imported) │\
│ │\
│ ☐ Manual entry │\
│ \[Add Model\] │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ CURRENT INVENTORY │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ Total Models: 47 │\
│ By Tier: T1: 8 \| T2: 15 \| T3: 18 \| T4: 6 │\
│ │\
│ ┌─────────────────────────────────────────────────────────────┐│\
│ │ ID │ Model Name │ Tier │ Status │ Val Due ││\
│ ├───────┼─────────────────────┼──────┼─────────┼────────────┤│\
│ │ M-001 │ Consumer Credit │ T1 │ Active │ 2026-03-15 ││\
│ │ │ Scorecard │ │ │ ⚠ 45 days ││\
│ ├───────┼─────────────────────┼──────┼─────────┼────────────┤│\
│ │ M-002 │ Commercial RE │ T1 │ Active │ 2026-06-01 ││\
│ │ │ Appraisal Model │ │ │ ││\
│ ├───────┼─────────────────────┼──────┼─────────┼────────────┤│\
│ │ M-003 │ CECL - Consumer │ T1 │ Active │ 2026-04-30 ││\
│ │ │ Loans │ │ │ ││\
│ ├───────┼─────────────────────┼──────┼─────────┼────────────┤│\
│ │ M-004 │ Fraud Detection │ T2 │ Active │ 2026-08-15 ││\
│ │ │ (Real-time) │ │ │ ││\
│ ├───────┼─────────────────────┼──────┼─────────┼────────────┤│\
│ │ M-005 │ Marketing │ T3 │ Active │ 2027-01-01 ││\
│ │ │ Propensity │ │ │ ││\
│ └─────────────────────────────────────────────────────────────┘│\
│ │\
│ \[Export Inventory\] \[Validation Calendar\] \[Gap Analysis\] │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**Step 5: Complete Model Registration Details**

For each model, complete the SR 11-7 aligned registration:

┌─────────────────────────────────────────────────────────────────┐\
│ MODEL REGISTRATION: Consumer Credit Scorecard │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ SECTION 1: MODEL IDENTIFICATION │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ Model ID: M-001 (auto-generated) │\
│ Model Name: Consumer Credit Scorecard │\
│ Model Version: 4.2 │\
│ Version Date: 2025-06-15 │\
│ │\
│ Model Type: │\
│ ○ Statistical/Regression │\
│ ● Machine Learning │\
│ ○ Expert Judgment │\
│ ○ Hybrid │\
│ ○ Vendor/Third-Party │\
│ │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ SECTION 2: MODEL PURPOSE AND USE │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ Business Purpose: │\
│ \[Evaluate creditworthiness of consumer loan applicants │\
│ to support underwriting decisions for personal loans, │\
│ credit cards, and auto loans.\] │\
│ │\
│ Model Use Cases: │\
│ ☑ Credit approval/denial │\
│ ☑ Credit limit setting │\
│ ☑ Risk-based pricing │\
│ ☐ Collections prioritization │\
│ ☐ Portfolio monitoring │\
│ │\
│ Products/Portfolios: │\
│ ☑ Personal Loans (\$2.1B portfolio) │\
│ ☑ Credit Cards (\$890M portfolio) │\
│ ☑ Auto Loans (\$1.5B portfolio) │\
│ ☐ Mortgage (uses different model) │\
│ │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ SECTION 3: MODEL OWNERSHIP │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ Model Owner (1st Line): │\
│ Name: \[Sarah Chen ▼\] │\
│ Title: VP, Credit Risk Analytics │\
│ Department: Consumer Lending │\
│ │\
│ Model Developer: │\
│ Name: \[Internal ▼\] │\
│ If vendor: Vendor Name: \_\_\_\_\_\_\_ │\
│ │\
│ Executive Sponsor: │\
│ Name: \[James Wilson, CRO ▼\] │\
│ │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ SECTION 4: RISK TIERING │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ Assigned Tier: \[Tier 1 - Critical ▼\] │\
│ │\
│ Tiering Rationale: │\
│ ☑ Direct impact on credit decisions │\
│ ☑ Material portfolio exposure (\>\$1B) │\
│ ☑ Fair lending implications │\
│ ☐ Regulatory capital impact │\
│ ☑ Customer-facing decisions │\
│ │\
│ Materiality Assessment: │\
│ Annual decisions influenced: \~150,000 │\
│ Portfolio exposure: \$4.5B │\
│ Estimated model risk (annual): \$15M-\$25M │\
│ │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ SECTION 5: MODEL DOCUMENTATION │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ Required Documents: Status Last Updated │\
│ ☑ Model Development Doc Uploaded 2025-06-10 │\
│ ☑ Model Validation Report Uploaded 2025-07-15 │\
│ ☑ Implementation Doc Uploaded 2025-06-20 │\
│ ☑ User Guide Uploaded 2025-06-25 │\
│ ☑ Change Log Uploaded 2025-11-01 │\
│ ☐ Ongoing Monitoring Plan Missing \[Upload\] │\
│ ☑ Fair Lending Analysis Uploaded 2025-07-01 │\
│ │\
│ \[Upload Document\] \[View All Documents\] │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**DAY 16-22: VALIDATION TRACKING**

**Step 6: Configure Validation Workflows**

NAVIGATION: Compliance → Financial Services → Validation Settings\
\
┌─────────────────────────────────────────────────────────────────┐\
│ VALIDATION WORKFLOW CONFIGURATION │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ INITIAL VALIDATION WORKFLOW │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ Trigger: New model registered OR major model change │\
│ │\
│ Workflow Steps: │\
│ ┌─────────────────────────────────────────────────────────┐ │\
│ │ │ │\
│ │ ┌──────────┐ ┌──────────┐ ┌──────────┐ │ │\
│ │ │ 1. Model │ │ 2. Valid-│ │ 3. MRO │ │ │\
│ │ │ Owner │───►│ ation │───►│ Review │ │ │\
│ │ │ Submits │ │ Team │ │ │ │ │\
│ │ │ │ │ Reviews │ │ │ │ │\
│ │ └──────────┘ └──────────┘ └──────────┘ │ │\
│ │ │ │ │ │ │\
│ │ │ │ ▼ │ │\
│ │ │ │ ┌──────────┐ │ │\
│ │ │ │ │ 4. Final │ │ │\
│ │ │ │ │ Approval │ │ │\
│ │ │ │ │ (Exec) │ │ │\
│ │ │ │ └──────────┘ │ │\
│ │ │ │ │ │ │\
│ │ ▼ ▼ ▼ │ │\
│ │ \[Findings?\] \[Findings?\] \[Approved?\] │ │\
│ │ │ │ │ │ │\
│ │ YES YES YES/NO │ │\
│ │ │ │ │ │ │\
│ │ ▼ ▼ ▼ │ │\
│ │ Action items Action items Production OK / │ │\
│ │ assigned assigned Return for rework │ │\
│ │ │ │\
│ └─────────────────────────────────────────────────────────┘ │\
│ │\
│ Validation Scope (Tier 1): │\
│ ☑ Conceptual soundness review │\
│ ☑ Data quality assessment │\
│ ☑ Developmental evidence review │\
│ ☑ Process verification │\
│ ☑ Outcomes analysis │\
│ ☑ Benchmarking/challenger analysis │\
│ ☑ Sensitivity analysis │\
│ ☑ Fair lending testing │\
│ │\
│ SLA: 45 business days from submission │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ ONGOING VALIDATION WORKFLOW │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ Trigger: Validation due date approaching (60-day warning) │\
│ │\
│ Validation Cycle by Tier: │\
│ • Tier 1: Annual │\
│ • Tier 2: 18 months │\
│ • Tier 3: 24 months │\
│ • Tier 4: 36 months or material change │\
│ │\
│ Ongoing Validation Scope: │\
│ ☑ Performance monitoring review │\
│ ☑ Outcomes analysis update │\
│ ☑ Model stability assessment │\
│ ☑ Environment/data changes review │\
│ ☑ Issue remediation verification │\
│ ☑ Fair lending monitoring results │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**Step 7: Track Validation Status**

NAVIGATION: Compliance → Financial Services → Validation Dashboard\
\
┌─────────────────────────────────────────────────────────────────┐\
│ VALIDATION STATUS DASHBOARD │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ VALIDATION SUMMARY │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ ┌────────────┬────────────┬────────────┬────────────┐ │\
│ │ Current │ Due in │ Due in │ Overdue │ │\
│ │ │ 90 days │ 180 days │ │ │\
│ ├────────────┼────────────┼────────────┼────────────┤ │\
│ │ 38 │ 5 │ 8 │ 2 │ │\
│ │ (81%) │ (11%) │ (17%) │ (4%) │ │\
│ └────────────┴────────────┴────────────┴────────────┘ │\
│ │\
│ ⚠ ATTENTION REQUIRED │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ OVERDUE VALIDATIONS: │\
│ ┌─────────────────────────────────────────────────────────────┐│\
│ │ Model │ Tier │ Due Date │ Days Over │ Owner ││\
│ ├───────────────────┼──────┼────────────┼───────────┼─────────┤│\
│ │ CRE Appraisal │ T1 │ 2025-12-15 │ 46 days │ J. Lee ││\
│ │ Auto Lease │ T2 │ 2026-01-05 │ 25 days │ M. Patel││\
│ │ Residual │ │ │ │ ││\
│ └─────────────────────────────────────────────────────────────┘│\
│ │\
│ UPCOMING VALIDATIONS (Next 90 Days): │\
│ ┌─────────────────────────────────────────────────────────────┐│\
│ │ Model │ Tier │ Due Date │ Status │ Owner ││\
│ ├───────────────────┼──────┼────────────┼───────────┼─────────┤│\
│ │ Consumer Credit │ T1 │ 2026-03-15 │ In Progress│ S. Chen││\
│ │ Scorecard │ │ │ (65%) │ ││\
│ ├───────────────────┼──────┼────────────┼───────────┼─────────┤│\
│ │ CECL - Consumer │ T1 │ 2026-04-01 │ Not Started│ R. Kim ││\
│ ├───────────────────┼──────┼────────────┼───────────┼─────────┤│\
│ │ Deposit Pricing │ T2 │ 2026-04-15 │ Scheduled │ T. Brown││\
│ ├───────────────────┼──────┼────────────┼───────────┼─────────┤│\
│ │ Fraud - ACH │ T2 │ 2026-04-20 │ Not Started│ L. Wang││\
│ ├───────────────────┼──────┼────────────┼───────────┼─────────┤│\
│ │ Marketing - │ T3 │ 2026-04-30 │ Scheduled │ K. Jones││\
│ │ Response │ │ │ │ ││\
│ └─────────────────────────────────────────────────────────────┘│\
│ │\
│ \[View Full Calendar\] \[Export Schedule\] \[Send Reminders\] │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**Step 8: Document Validation Findings**

┌─────────────────────────────────────────────────────────────────┐\
│ VALIDATION FINDINGS TRACKER │\
│ Model: Consumer Credit Scorecard (M-001) │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ Validation Date: 2025-07-15 │\
│ Validator: Model Validation Team (2nd Line) │\
│ Overall Rating: \[Satisfactory with Findings ▼\] │\
│ │\
│ Rating Scale: │\
│ • Satisfactory │\
│ • Satisfactory with Findings │\
│ • Needs Improvement │\
│ • Unsatisfactory │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ FINDINGS │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ ┌─────────────────────────────────────────────────────────────┐│\
│ │ Finding \#1 HIGH ││\
│ │ ───────────────────────────────────────────────────────────││\
│ │ Title: Model monitoring metrics not updated monthly ││\
│ │ ││\
│ │ Description: SR 11-7 requires ongoing monitoring. ││\
│ │ Performance metrics (Gini, KS, PSI) were not calculated ││\
│ │ for 3 months (Aug-Oct 2025). ││\
│ │ ││\
│ │ Recommendation: Implement automated monthly monitoring ││\
│ │ with alerts for metric breaches. ││\
│ │ ││\
│ │ Owner: Sarah Chen Due: 2025-10-15 ││\
│ │ Status: \[In Progress ▼\] 75% Complete ││\
│ │ ││\
│ │ Management Response: ││\
│ │ \[Automated monitoring dashboard deployed. Testing ││\
│ │ alert thresholds before full production.\] ││\
│ │ ││\
│ │ Evidence: \[Dashboard\_Screenshot.pdf\] \[Alert\_Config.xlsx\] ││\
│ └─────────────────────────────────────────────────────────────┘│\
│ │\
│ ┌─────────────────────────────────────────────────────────────┐│\
│ │ Finding \#2 MEDIUM ││\
│ │ ───────────────────────────────────────────────────────────││\
│ │ Title: Documentation does not reflect v4.2 changes ││\
│ │ ││\
│ │ Description: Model development documentation still ││\
│ │ references v4.1. Changes in feature engineering and ││\
│ │ threshold adjustments not documented. ││\
│ │ ││\
│ │ Recommendation: Update MDD to reflect all v4.2 changes ││\
│ │ including feature additions and decisioning changes. ││\
│ │ ││\
│ │ Owner: Sarah Chen Due: 2025-09-30 ││\
│ │ Status: \[Closed ▼\] Completed: 2025-09-28 ││\
│ │ ││\
│ │ Evidence: \[MDD\_v4.2\_Final.pdf\] ││\
│ └─────────────────────────────────────────────────────────────┘│\
│ │\
│ FINDINGS SUMMARY: │\
│ Total: 4 \| High: 1 \| Medium: 2 \| Low: 1 │\
│ Open: 1 \| Closed: 3 │\
│ │\
│ \[Add Finding\] \[Export Findings\] \[Generate Remediation Report\]│\
│ │\
└─────────────────────────────────────────────────────────────────┘

**DAY 23-27: FAIR LENDING COMPLIANCE**

**Step 9: Configure Fair Lending Monitoring**

NAVIGATION: Compliance → Financial Services → Fair Lending\
\
┌─────────────────────────────────────────────────────────────────┐\
│ FAIR LENDING CONFIGURATION │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ PROTECTED CLASSES │\
│ ───────────────────────────────────────────────────────────── │\
│ Configure monitoring for: │\
│ │\
│ ☑ Race/Ethnicity (HMDA proxy or direct) │\
│ ☑ Sex/Gender │\
│ ☑ Age │\
│ ☑ National Origin │\
│ ☐ Religion │\
│ ☐ Marital Status (where applicable) │\
│ ☐ Public Assistance Status │\
│ ☐ Other: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ BIAS MONITORING THRESHOLDS │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ Disparate Impact Ratio Alert Threshold: │\
│ • Approval rates: \[0.80\] (80% rule) │\
│ • Pricing: \[0.80\] │\
│ │\
│ Statistical Significance Level: \[0.05\] │\
│ │\
│ Monitoring Frequency: │\
│ ○ Real-time (continuous) │\
│ ● Daily batch │\
│ ○ Weekly batch │\
│ ○ Monthly batch │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ MODELS REQUIRING FAIR LENDING MONITORING │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ ☑ Consumer Credit Scorecard │\
│ ☑ Auto Loan Pricing Model │\
│ ☑ Credit Card Underwriting │\
│ ☑ Personal Loan Pricing │\
│ ☑ HELOC Underwriting │\
│ ☑ Mortgage Pricing Model │\
│ ☐ Commercial Credit (business purpose exempt) │\
│ ☐ Fraud Detection (not credit decision) │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**Step 10: Review Fair Lending Dashboard**

┌─────────────────────────────────────────────────────────────────┐\
│ FAIR LENDING MONITORING DASHBOARD │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ Model: Consumer Credit Scorecard │\
│ Period: 2025-12-01 to 2026-01-30 │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ APPROVAL RATE ANALYSIS │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ ┌─────────────────────────────────────────────────────────────┐│\
│ │ Group │ Apps │ Approved │ Rate │ DIR ││\
│ ├────────────────────┼────────┼──────────┼───────┼──────────┤│\
│ │ White (Control) │ 8,234 │ 5,762 │ 70.0% │ 1.00 ││\
│ ├────────────────────┼────────┼──────────┼───────┼──────────┤│\
│ │ Black │ 2,156 │ 1,358 │ 63.0% │ 0.90 ✓ ││\
│ ├────────────────────┼────────┼──────────┼───────┼──────────┤│\
│ │ Hispanic │ 1,892 │ 1,230 │ 65.0% │ 0.93 ✓ ││\
│ ├────────────────────┼────────┼──────────┼───────┼──────────┤│\
│ │ Asian │ 1,245 │ 934 │ 75.0% │ 1.07 ✓ ││\
│ ├────────────────────┼────────┼──────────┼───────┼──────────┤│\
│ │ Male (Control) │ 7,234 │ 4,918 │ 68.0% │ 1.00 ││\
│ ├────────────────────┼────────┼──────────┼───────┼──────────┤│\
│ │ Female │ 6,293 │ 4,366 │ 69.4% │ 1.02 ✓ ││\
│ ├────────────────────┼────────┼──────────┼───────┼──────────┤│\
│ │ Age \<25 │ 1,523 │ 838 │ 55.0% │ 0.81 ✓ ││\
│ ├────────────────────┼────────┼──────────┼───────┼──────────┤│\
│ │ Age 25-62 (Control)│ 10,234 │ 7,061 │ 69.0% │ 1.00 ││\
│ ├────────────────────┼────────┼──────────┼───────┼──────────┤│\
│ │ Age 62+ │ 1,770 │ 1,239 │ 70.0% │ 1.01 ✓ ││\
│ └─────────────────────────────────────────────────────────────┘│\
│ │\
│ ✓ = Within threshold (≥0.80) │\
│ ⚠ = Approaching threshold (0.80-0.85) │\
│ ✗ = Below threshold (\<0.80) - Requires review │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ PRICING ANALYSIS │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ Average APR by Group (Approved Applicants): │\
│ ┌─────────────────────────────────────────────────────────────┐│\
│ │ Group │ Avg APR │ vs Control │ Status ││\
│ ├────────────────────┼─────────┼────────────┼────────────────┤│\
│ │ White (Control) │ 12.4% │ \-- │ \-- ││\
│ │ Black │ 13.1% │ +0.7% │ ⚠ Review ││\
│ │ Hispanic │ 12.8% │ +0.4% │ ✓ OK ││\
│ │ Asian │ 11.9% │ -0.5% │ ✓ OK ││\
│ └─────────────────────────────────────────────────────────────┘│\
│ │\
│ ⚠ ALERT: Black borrowers showing +0.7% APR difference. │\
│ Regression analysis suggests primarily driven by │\
│ credit score distribution, but review recommended. │\
│ │\
│ \[View Full Analysis\] \[Generate Fair Lending Report\] │\
│ \[Create Action Item\] \[Document Business Justification\] │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**Step 11: Configure Adverse Action Tracking**

┌─────────────────────────────────────────────────────────────────┐\
│ ADVERSE ACTION CONFIGURATION │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ADVERSE ACTION REASON CODES │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ Configure standard reason codes for model-driven denials: │\
│ │\
│ ┌─────────────────────────────────────────────────────────────┐│\
│ │ Code │ Reason │ Model Feature ││\
│ ├──────┼──────────────────────────────────┼───────────────────┤│\
│ │ AA01 │ Credit score below threshold │ credit\_score ││\
│ │ AA02 │ Insufficient credit history │ credit\_history\_mo ││\
│ │ AA03 │ High debt-to-income ratio │ dti\_ratio ││\
│ │ AA04 │ Recent delinquencies │ delinq\_count\_24mo ││\
│ │ AA05 │ High credit utilization │ utilization\_pct ││\
│ │ AA06 │ Insufficient income │ stated\_income ││\
│ │ AA07 │ Too many recent inquiries │ inquiry\_count\_6mo ││\
│ │ AA08 │ Limited account diversity │ account\_types ││\
│ │ AA09 │ Short employment tenure │ employment\_months ││\
│ │ AA10 │ Bankruptcy/collection history │ derog\_flag ││\
│ └─────────────────────────────────────────────────────────────┘│\
│ │\
│ \[Add Reason Code\] \[Import from Model\] │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ ADVERSE ACTION NOTICE REQUIREMENTS │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ ☑ Generate top 4 reason codes for each denial │\
│ ☑ Log all adverse actions with reason codes │\
│ ☑ Track notice delivery confirmation │\
│ ☑ Retain records for 25 months (ECOA requirement) │\
│ │\
│ Integration with notice delivery system: │\
│ ○ Manual export for external system │\
│ ● API integration with \[Letter Vendor ▼\] │\
│ ○ Internal notice generation │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**DAY 28-30: EXAMINATION READINESS**

**Step 12: Generate Examination Package**

NAVIGATION: Compliance → Financial Services → Examination Prep\
\
┌─────────────────────────────────────────────────────────────────┐\
│ EXAMINATION DOCUMENTATION GENERATOR │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ EXAMINATION TYPE │\
│ ───────────────────────────────────────────────────────────── │\
│ ○ OCC Safety & Soundness │\
│ ● Federal Reserve Examination │\
│ ○ FDIC Examination │\
│ ○ State Banking Examination │\
│ ○ Fair Lending Examination (CFPB/DOJ) │\
│ ○ Internal Audit / SOX │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ SCOPE SELECTION │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ Date Range: \[2025-01-01\] to \[2026-01-30\] │\
│ │\
│ Models to Include: │\
│ ○ All models │\
│ ● Tier 1 and Tier 2 only │\
│ ○ Selected models: \[Select\...\] │\
│ ○ Models tagged: \[Credit Decisions ▼\] │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ DOCUMENTATION PACKAGE CONTENTS │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ ☑ MRM Policy and Procedures │\
│ ☑ Model Inventory (with tiering rationale) │\
│ ☑ Model Governance Committee Minutes │\
│ ☑ Validation Reports (all in-scope models) │\
│ ☑ Validation Findings and Remediation Status │\
│ ☑ Model Development Documentation │\
│ ☑ Ongoing Monitoring Reports │\
│ ☑ Model Change Log │\
│ ☑ Vendor Model Documentation (if applicable) │\
│ ☑ Fair Lending Analyses │\
│ ☑ Adverse Action Samples │\
│ ☑ Exception Reports │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ EXAMINER REQUEST LIST (Common Items) │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ Pre-populated based on recent exam request patterns: │\
│ │\
│ ☑ 1. Complete model inventory with risk ratings │\
│ ☑ 2. MRM policy and last board approval │\
│ ☑ 3. List of models validated in past 12 months │\
│ ☑ 4. Sample validation report (highest tier) │\
│ ☑ 5. Open validation findings and remediation plans │\
│ ☑ 6. Model performance monitoring dashboards │\
│ ☑ 7. Fair lending analysis for credit models │\
│ ☑ 8. Adverse action reason code mapping │\
│ ☑ 9. Model change requests and approvals │\
│ ☑ 10. Third-party model due diligence │\
│ │\
│ \[Generate Package\] Estimated time: 5-10 minutes │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**Step 13: Review Examination Readiness Score**

┌─────────────────────────────────────────────────────────────────┐\
│ EXAMINATION READINESS ASSESSMENT │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ OVERALL READINESS SCORE: 87/100 (Good) │\
│ ████████████████████░░░ │\
│ │\
│ ═══════════════════════════════════════════════════════════════│\
│ │\
│ CATEGORY SCORES │\
│ ───────────────────────────────────────────────────────────── │\
│ │\
│ Model Inventory Completeness 95/100 ████████████▓ │\
│ • All models inventoried ✓ │\
│ • Tiering rationale documented ✓ │\
│ • Ownership assigned ✓ │\
│ │\
│ Validation Coverage 78/100 ████████████░░ │\
│ • Tier 1 models current ⚠ 1 overdue │\
│ • Tier 2 models current ⚠ 1 overdue │\
│ • Findings remediation on track ✓ │\
│ │\
│ Documentation Quality 85/100 █████████████░ │\
│ • MDDs complete and current ⚠ 2 need updates │\
│ • Validation reports complete ✓ │\
│ • Change logs maintained ✓ │\
│ │\
│ Ongoing Monitoring 92/100 ██████████████ │\
│ • Performance metrics tracked ✓ │\
│ • Alerts configured ✓ │\
│ • Monthly reports generated ✓ │\
│ │\
│ Fair Lending Compliance 88/100 █████████████░ │\
│ • All credit models monitored ✓ │\
│ • No threshold breaches ✓ │\
│ • Adverse action tracking ⚠\
\<span
style=\"display:none\"\>\[\^1\]\[\^10\]\[\^11\]\[\^2\]\[\^3\]\[\^4\]\[\^5\]\[\^6\]\[\^7\]\[\^8\]\[\^9\]\</span\>\
\
\<div align=\"center\"\>⁂\</div\>\
\
\[\^1\]: A Clear Guide to Phase Mirror\'s Services.pdf\
\[\^2\]: License\_ Strategic & Legal Analysis.pdf\
\[\^3\]: Phase Mirror\_ Consultation & SaaS.pdf\
\[\^4\]: Agentic Domain-Specific Reasoning.pdf\
\[\^5\]: Policy Memo\_ Managing Agentic AI Liability with the Phase
Mirror Framework.pdf\
\[\^6\]: The Phase Mirror does not resolve dissonance---it names it.pdf\
\[\^7\]: Understanding Phase Mirror Dissonance\_ A Beginner\'s
Guide.pdf\
\[\^8\]: The Phase of Mirror Dissonance.pdf\
\[\^9\]: Implementation Guide\_ Applying Phase Mirror Dissonance.pdf\
\[\^10\]: Phase mirror dissonance\_\_\_Open core must be useful.pdf\
\[\^11\]: Phase Mirror\_ Comprehensive Services Catalog.docx.pdf

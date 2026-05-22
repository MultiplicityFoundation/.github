---
slug: in-plain-chat-lets-create-a-baa-summary-faq-for-sa
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 00-foundations/phase-mirror/in plain chat lets create a BAA Summary_FAQ for
    sa.md
  last_synced: '2026-03-20T17:17:22.049730Z'
---

![](media/image-ef8c3bfb3fa71983bab14ed4213250ca9224bc9c.png){width="2.6466666666666665in"
height="0.6666666666666666in"}

**in plain chat lets create a BAA Summary/FAQ for sales teams**

Here\'s a practical BAA Summary and FAQ for your sales team:

**Phase Mirror BAA: Sales Team Guide**

**Quick Reference Card**

  --------------------------- ------------------------------------------------------------------------
  Item                        Details
  **What is a BAA?**          Business Associate Agreement---a legally required contract under HIPAA
  **When required**           Any time a healthcare customer\'s PHI may touch our systems
  **Who signs**               Customer (Covered Entity) + Phase Mirror (Business Associate)
  **Turnaround time**         Standard BAA: 24--48 hours; Custom terms: 1--2 weeks
  **Owner at Phase Mirror**   \[Legal/Compliance Contact\]
  **Template location**       \[Internal link to BAA template\]
  --------------------------- ------------------------------------------------------------------------

**What Sales Needs to Know**

**The 30-Second Explanation**

A BAA is a contract required by federal law (HIPAA) whenever a
healthcare organization shares patient information with a vendor. It
defines what we can and cannot do with that data, and what happens if
something goes wrong. Without a signed BAA, the customer cannot legally
use our services with any data that could identify patients.

**When You Need a BAA**

**Always required when the customer is:**

-   A hospital, health system, or clinic

-   A health insurance company or health plan

-   A healthcare clearinghouse

-   A business associate of any of the above (vendors serving
    healthcare)

**And they will be using Phase Mirror to:**

-   Analyze AI systems that process patient data

-   Document governance for clinical decision support tools

-   Generate compliance reports involving PHI

-   Store any data that could identify patients

**When You Don\'t Need a BAA**

-   Customer is not in healthcare

-   Customer explicitly confirms no PHI will enter the Phase Mirror
    platform

-   Customer uses only de-identified data (must meet HIPAA
    de-identification standards)

**Important:** When in doubt, execute the BAA. It protects both parties.

**Qualifying Questions for Discovery Calls**

Use these questions to determine BAA requirements early in the sales
process:

**1. Industry Identification**

> \"Is your organization a healthcare provider, health plan, or do you
> provide services to healthcare organizations?\"

**2. Data Scope**

> \"Will the AI systems you\'re governing process any patient or member
> health information?\"

**3. PHI Touchpoints**

> \"When using Phase Mirror, would any patient-identifiable data appear
> in your configuration files, rule outputs, or dissonance reports?\"

**4. Existing Compliance**

> \"Do you currently require BAAs from your other software vendors?\"

If the answer to any of these is \"yes\" or \"possibly,\" proceed with
BAA execution.

**Product-Specific Guidance**

**Healthcare & Life Sciences Compliance Pack**

**BAA required?** Yes, in virtually all cases.

This pack includes HIPAA AI provisions, FDA SaMD guidance alignment, and
clinical decision support rules. Customers purchasing this pack are
operating in healthcare and will almost certainly need a
BAA.[^[\[1\]]{.underline}^](#fn1)

**Sales motion:** Include BAA execution as a standard step in the
onboarding checklist for this pack.

**Platform Tiers**

  ------------------ ---------------- ----------------------------------------------
  Tier               BAA Available?   Notes
  Community (Free)   No               Self-hosted; no data touches our systems
  Team               Yes              Standard BAA
  Business           Yes              Standard BAA
  Enterprise         Yes              Standard or custom BAA with negotiated terms
  ------------------ ---------------- ----------------------------------------------

**Consulting & Implementation Services**

  --------------------------------------- -------------------------------------------------------
  Service                                 BAA Consideration
  AI Governance Diagnostic                Required if we review systems processing PHI
  Compliance-Accuracy Tradeoff Workshop   Required if PHI examples are discussed
  Implementation Services                 Required if we access customer environments with PHI
  Advisory Retainer                       Required if PHI may be discussed in advisory sessions
  --------------------------------------- -------------------------------------------------------

**Common Customer Questions (and Your Answers)**

**\"Do we really need a BAA?\"**

> \"If there\'s any possibility that patient-identifiable information
> could be processed through Phase Mirror---even in metadata, file
> names, or error logs---yes, we need a BAA. It\'s a federal
> requirement, and we take it seriously. The good news is we have a
> standard BAA ready to go, and execution typically takes 24--48
> hours.\"

**\"Can we use our BAA template instead of yours?\"**

> \"Absolutely. Many enterprise customers prefer to use their own
> templates. We\'re happy to review your BAA and can usually turn around
> redlines within 3--5 business days. If you\'d like to compare, I can
> also send you our standard BAA for reference.\"

**\"What\'s the difference between your standard BAA and a custom
BAA?\"**

> \"Our standard BAA covers all HIPAA requirements and works well for
> most customers. Custom BAAs typically involve negotiated terms around
> indemnification caps, breach notification timelines, or specific
> security commitments. Custom negotiations usually add 1--2 weeks to
> the process.\"

**\"What security certifications do you have?\"**

> \"We maintain SOC 2 Type II certification for our Business and
> Enterprise tiers. We can provide our most recent SOC 2 report under
> NDA. Our platform implements all HIPAA-required administrative,
> physical, and technical safeguards, including encryption in transit
> and at rest, access controls, and audit logging.\"

**\"What happens if there\'s a data breach?\"**

> \"Our BAA commits us to notifying you within 5 business days of
> discovering any breach involving your data. We\'ll provide all the
> information you need to meet your own notification obligations,
> including identification of affected individuals, description of data
> involved, and steps we\'re taking to remediate. We also carry cyber
> liability insurance that covers HIPAA incidents.\"

**\"Can we see your security documentation?\"**

> \"Yes. Under NDA, we can provide:

**\"Where is our data stored?\"**

> \"Our platform is hosted in \[cloud provider/region\]. Enterprise
> customers can request dedicated instances with specific data residency
> requirements. All data is encrypted at rest and in transit.\"

**\"Who at Phase Mirror has access to our data?\"**

> \"Access is limited to personnel with a legitimate business need, such
> as support engineers responding to your tickets. All access is logged
> and auditable. Our employees receive HIPAA training and are bound by
> confidentiality obligations.\"

**\"What if we need to terminate the agreement?\"**

> \"Upon termination, we\'ll return or destroy all PHI within 30 days
> and provide a certification of destruction. If any data must be
> retained (for legal or technical reasons), we\'ll continue protecting
> it under the BAA terms indefinitely.\"

**Handling Objections**

**\"This is too complicated / takes too long\"**

> \"I understand compliance can feel like overhead, but this actually
> protects both of us. We\'ve streamlined the process---our standard BAA
> is pre-approved and ready to sign. Most customers complete execution
> within 48 hours. Let me send it over now so we can run it in parallel
> with the technical evaluation.\"

**\"Our legal team will want to negotiate everything\"**

> \"That\'s completely normal for enterprise customers. Let\'s schedule
> a call with our legal/compliance team and yours to walk through the
> BAA together. In our experience, getting both teams aligned early
> prevents surprises later. What\'s the best contact on your legal
> team?\"

**\"We\'re not ready to sign contracts yet---we\'re just evaluating\"**

> \"No problem. You can evaluate our Community tier without a BAA since
> it\'s self-hosted and no data touches our systems. When you\'re ready
> to move to a paid tier or our healthcare pack, we\'ll have the BAA
> ready to go. Want me to send the template now so your legal team can
> review it during the evaluation?\"

**\"We\'ve had bad experiences with vendor breaches\"**

> \"That\'s a legitimate concern, and I appreciate you raising it. A few
> things that set us apart: we\'re SOC 2 Type II certified, we commit to
> breach notification within 5 business days, and our BAA includes
> indemnification for breaches caused by us. I can also connect you with
> references from other healthcare customers who\'ve been through our
> security review process.\"

**BAA Execution Checklist**

Use this checklist when closing a healthcare deal:

**Before Sending BAA:**

-   \[ \] Confirm customer is a Covered Entity or Business Associate

-   \[ \] Identify which services/products are in scope

-   \[ \] Determine if standard or custom BAA is needed

-   \[ \] Get customer\'s legal contact information

**Sending BAA:**

-   \[ \] Send BAA template with Exhibit A pre-filled for their services

-   \[ \] Include signing instructions

-   \[ \] Set expectation for turnaround (48 hours standard, 1--2 weeks
    custom)

-   \[ \] CC \[internal legal contact\] on the email

**Tracking:**

-   \[ \] Log BAA status in CRM

-   \[ \] Follow up if no response within 5 business days

-   \[ \] Escalate stalled negotiations to \[internal contact\]

**After Execution:**

-   \[ \] Obtain fully signed copy

-   \[ \] Upload to \[contract management system\]

-   \[ \] Notify implementation/onboarding team

-   \[ \] Confirm BAA effective date in customer record

**Escalation Paths**

  ------------------------------------------ ---------------------------------------------- -----------------
  Situation                                  Escalate To                                    SLA
  Customer wants non-standard terms          \[Legal Contact\]                              24 hours
  Customer\'s BAA template requires review   \[Legal Contact\]                              3 business days
  Security questionnaire or audit request    \[Security/Compliance Contact\]                5 business days
  Customer reports potential breach          \[Security Contact\] + \[Executive Sponsor\]   Immediate
  Deal blocked by BAA negotiation            \[Sales Leadership\] + \[Legal Contact\]       24 hours
  ------------------------------------------ ---------------------------------------------- -----------------

**Red Flags to Watch For**

**Stop and escalate if the customer:**

-   Asks us to accept unlimited liability for breaches

-   Wants breach notification in less than 24 hours (operationally
    difficult)

-   Refuses to sign any BAA but wants to use PHI with our platform

-   Asks us to sign as the Covered Entity (we are always the Business
    Associate)

-   Requests audit rights that include unannounced on-site visits

-   Wants to modify the definition of PHI or Breach

**Key Terms Glossary**

  ---------------------------------------- -------------------------------------------------------------
  Term                                     Plain English
  **Covered Entity**                       The healthcare organization (hospital, insurer, etc.)
  **Business Associate**                   That\'s us---a vendor handling PHI on their behalf
  **PHI (Protected Health Information)**   Any health info that can identify a patient
  **ePHI**                                 Electronic PHI---PHI stored or transmitted digitally
  **Breach**                               Unauthorized access, use, or disclosure of PHI
  **Minimum Necessary**                    Only access the PHI you need to do the job
  **De-identified Data**                   Data stripped of identifiers so it\'s no longer PHI
  **Designated Record Set**                The records we maintain that patients have rights to access
  ---------------------------------------- -------------------------------------------------------------

**Resources**

  ------------------------------- -------------------
  Resource                        Location
  Standard BAA Template           \[Internal link\]
  BAA Redline Request Form        \[Internal link\]
  SOC 2 Report (under NDA)        \[Internal link\]
  Security Whitepaper             \[Internal link\]
  SIG Questionnaire (completed)   \[Internal link\]
  HIPAA Training (internal)       \[Internal link\]
  Legal Team Contact              \[Email/Slack\]
  Compliance Team Contact         \[Email/Slack\]
  ------------------------------- -------------------

**Quick Reference: What We Commit To**

  ---------------------------------------- ---------------------------------------
  Commitment                               Our Standard
  Breach notification                      5 business days
  Access requests                          10 business days
  Amendment requests                       10 business days
  Accounting of disclosures                30 days (60 with extension)
  Data return/destruction on termination   30 days
  Subcontractor flow-down                  Required for all subs with PHI access
  Employee training                        Annual HIPAA training
  Encryption                               In transit and at rest
  ---------------------------------------- ---------------------------------------

This guide should help your sales team confidently navigate BAA
conversations. Would you like me to create any additional resources,
such as:

-   Email templates for sending the BAA

-   A one-page customer-facing BAA overview

-   Training slides for a sales team enablement session

-   A decision tree flowchart for \"Do we need a BAA?\"

⁂

1.  Phase Mirror\_ Comprehensive Services Catalog.docx.pdf

2.  Implementation Guide\_ Applying Phase Mirror Dissonance.pdf

3.  Phase mirror dissonance\_\_\_Open core must be useful.pdf

4.  A Clear Guide to Phase Mirror\'s Services.pdf

5.  License\_ Strategic & Legal Analysis.pdf

6.  Phase Mirror\_ Consultation & SaaS.pdf

7.  Agentic Domain-Specific Reasoning.pdf

8.  Policy Memo\_ Managing Agentic AI Liability with the Phase Mirror
    Framework.pdf

9.  The Phase Mirror does not resolve dissonance---it names it.pdf

10. Understanding Phase Mirror Dissonance\_ A Beginner\'s Guide.pdf

11. The Phase of Mirror Dissonance.pdf

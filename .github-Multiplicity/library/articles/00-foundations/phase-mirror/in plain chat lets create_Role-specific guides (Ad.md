---
slug: in-plain-chat-lets-create-role-specific-guides-ad
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 00-foundations/phase-mirror/in plain chat lets create_Role-specific guides
    (Ad.md
  last_synced: '2026-03-20T17:17:21.940987Z'
---

![](media/image-fafc2c16cfbd58a1b2948992707bfb08a78b7b64.png){width="2.6466666666666665in"
height="0.6666666666666666in"}

**in plain chat lets create**

Role-specific guides (Admin Guide, System Owner Guide, etc.)

Here are comprehensive role-specific guides for Phase Mirror:

**PHASE MIRROR ROLE-SPECIFIC GUIDES**

**GUIDE 1: ADMINISTRATOR GUIDE**

**Platform Configuration & User Management**

**Role:** Administrator\
**Time Commitment:** 2-4 hours/week during implementation, 1-2
hours/week steady state\
**Prerequisites:** IT/systems administration experience, security
awareness

**YOUR ROLE AS ADMINISTRATOR**

**What You\'re Responsible For**

  ---------------------------- ------------------------------------------------
  Responsibility               Activities
  **Platform Configuration**   Environment setup, settings, customization
  **User Management**          Provisioning, roles, access control
  **Integrations**             Connect external systems, maintain connections
  **Security**                 Authentication, audit logs, compliance
  **Support**                  First-line troubleshooting, escalation
  ---------------------------- ------------------------------------------------

**What You\'re NOT Responsible For**

-   Defining governance policies (Governance Lead)

-   Registering AI systems (System Owners)

-   Making governance decisions (Governance Lead + Business)

-   Vendor relationship management (Procurement/Project Lead)

**INITIAL SETUP CHECKLIST**

**Week 1: Foundation**

**Day 1-2: Environment Configuration**

-   \[ \] Confirm environment URL and access

-   \[ \] Log in as initial admin

-   \[ \] Set strong password + MFA

-   \[ \] Review default settings

**Day 3-4: Authentication Setup**

  ---------------------------------- -----------------------------------------------------------------
  Method                             Steps
  **Standard (Username/Password)**   Enable MFA enforcement in Settings → Security
  **SSO (SAML)**                     Settings → Authentication → SAML → Upload IdP metadata
  **SSO (OIDC)**                     Settings → Authentication → OIDC → Configure client credentials
  ---------------------------------- -----------------------------------------------------------------

SSO Configuration Details:

SAML CONFIGURATION\
- Entity ID: https://\[your-tenant\].phasemirror.com/saml/metadata\
- ACS URL: https://\[your-tenant\].phasemirror.com/saml/acs\
- Sign-on URL: https://\[your-tenant\].phasemirror.com/saml/login\
- Required attributes: email, firstName, lastName\
- Optional attributes: groups, department\
\
OIDC CONFIGURATION\
- Redirect URI: https://\[your-tenant\].phasemirror.com/oauth/callback\
- Scopes required: openid, email, profile\
- Token endpoint auth: client\_secret\_post

**Day 5: User Provisioning**

-   \[ \] Create role assignments plan

-   \[ \] Invite initial users

-   \[ \] Verify access levels

-   \[ \] Document provisioning process

**USER MANAGEMENT**

**Understanding Roles**

  --------------------- ---------------------------------------------------------------- ------------------------------------
  Role                  Permissions                                                      Typical Users
  **Admin**             Full platform access, settings, user management                  IT admins, platform owners
  **Governance Lead**   Configure governance rules, approve systems, manage compliance   Compliance officers, risk managers
  **System Owner**      Full access to owned AI systems, limited platform settings       AI/ML team leads, product owners
  **Contributor**       Edit access to assigned AI systems                               Developers, data scientists
  **Viewer**            Read-only access to dashboards and reports                       Executives, stakeholders
  **Auditor**           Read-only with full audit trail access                           Internal/external auditors
  --------------------- ---------------------------------------------------------------- ------------------------------------

**Permission Matrix**

  ------------------------- ------- ------------ ----------- ------------- -------- ---------
  Action                    Admin   Gov Lead     Sys Owner   Contributor   Viewer   Auditor
  Manage users              ✅       ❌            ❌           ❌             ❌        ❌
  Configure settings        ✅       ⚠️ Limited   ❌           ❌             ❌        ❌
  Manage integrations       ✅       ❌            ❌           ❌             ❌        ❌
  Configure governance      ✅       ✅            ❌           ❌             ❌        ❌
  Approve AI systems        ✅       ✅            ❌           ❌             ❌        ❌
  Register AI systems       ✅       ✅            ✅ Own       ❌             ❌        ❌
  Edit AI systems           ✅       ✅            ✅ Own       ✅ Assigned    ❌        ❌
  View AI systems           ✅       ✅            ✅           ✅ Assigned    ✅        ✅
  Run dissonance analysis   ✅       ✅            ✅ Own       ❌             ❌        ❌
  View dissonance reports   ✅       ✅            ✅ Own       ✅ Assigned    ✅        ✅
  Create action items       ✅       ✅            ✅ Own       ✅ Assigned    ❌        ❌
  Generate reports          ✅       ✅            ✅ Own       ❌             ✅        ✅
  View audit logs           ✅       ⚠️ Limited   ❌           ❌             ❌        ✅
  Export data               ✅       ✅            ✅ Own       ❌             ❌        ✅
  ------------------------- ------- ------------ ----------- ------------- -------- ---------

**User Provisioning Procedures**

**Manual User Creation:**

1.  Go to **Settings → Users → Invite User**

2.  Enter email address

3.  Select role

4.  (Optional) Assign to specific AI systems

5.  Click **Send Invitation**

6.  User receives email, sets password, configures MFA

**Bulk User Import:**

1.  Download template: **Settings → Users → Import → Download Template**

2.  Fill in CSV with columns: email, firstName, lastName, role, systems

3.  Upload: **Settings → Users → Import → Upload CSV**

4.  Review and confirm

5.  Users receive invitation emails

**SSO/SCIM Automatic Provisioning (Enterprise):**

1.  Configure SCIM in IdP (Okta, Azure AD, etc.)

2.  In Phase Mirror: **Settings → Authentication → SCIM → Enable**

3.  Copy SCIM endpoint URL and token to IdP

4.  Configure group-to-role mappings:

  -------------------------- -------------------
  IdP Group                  Phase Mirror Role
  phasemirror-admins         Admin
  phasemirror-governance     Governance Lead
  phasemirror-owners         System Owner
  phasemirror-contributors   Contributor
  phasemirror-viewers        Viewer
  -------------------------- -------------------

**User Lifecycle Management**

  ---------------------- -------------------- ----------------------------------------------------------
  Event                  Action               How
  **New hire**           Provision access     Manual invite or SCIM auto-provision
  **Role change**        Update permissions   Settings → Users → Edit → Change role
  **Team transfer**      Reassign systems     Settings → Users → Edit → Update system assignments
  **Leave of absence**   Suspend access       Settings → Users → Suspend (preserves data)
  **Termination**        Remove access        Settings → Users → Deactivate (or SCIM auto-deprovision)
  ---------------------- -------------------- ----------------------------------------------------------

**Access Review Process (Quarterly Recommended):**

1.  Export user list: **Settings → Users → Export**

2.  Review with managers/HR

3.  Identify terminated employees, role changes

4.  Update or remove access

5.  Document review in audit trail

**INTEGRATION MANAGEMENT**

**Available Integrations**

  -------------------- -------------------------------------------------- ------------------
  Category             Integrations                                       Setup Complexity
  **Identity**         Okta, Azure AD, Ping, OneLogin                     Medium
  **Source Control**   GitHub, GitLab, Bitbucket                          Low
  **CI/CD**            Jenkins, GitHub Actions, Azure DevOps, GitLab CI   Medium
  **Ticketing**        Jira, ServiceNow, Linear                           Low
  **Communication**    Slack, Microsoft Teams                             Low
  **SIEM**             Splunk, Sumo Logic, Datadog                        Medium
  **GRC**              ServiceNow GRC, Archer, OneTrust                   Medium-High
  -------------------- -------------------------------------------------- ------------------

**Integration Setup: GitHub**

**Purpose:** Auto-discover AI systems, link to source code

**Steps:**

1.  Go to **Settings → Integrations → GitHub → Connect**

2.  Click **Authorize with GitHub**

3.  Select organization(s) to connect

4.  Choose repositories (all or specific)

5.  Configure scan settings:

    -   \[ \] Scan for ML frameworks (TensorFlow, PyTorch, etc.)

    -   \[ \] Scan for model files (.pkl, .h5, .onnx, etc.)

    -   \[ \] Scan for config files (model cards, etc.)

6.  Click **Save and Sync**

**Ongoing:** GitHub syncs automatically every 24 hours. Manual sync
available.

**Integration Setup: Jira**

**Purpose:** Create tickets from dissonance action items

**Steps:**

1.  Go to **Settings → Integrations → Jira → Connect**

2.  Enter Jira URL: https://\[your-domain\].atlassian.net

3.  Create API token in Jira: **Jira Settings → API Tokens → Create**

4.  Enter email and API token in Phase Mirror

5.  Select default project for tickets

6.  Map fields:

  -------------------- -----------------------
  Phase Mirror Field   Jira Field
  Action item title    Summary
  Description          Description
  Owner                Assignee
  Due date             Due Date
  Priority             Priority
  AI System            Label or Custom Field
  -------------------- -----------------------

7.  Click **Test Connection** then **Save**

**Integration Setup: Slack**

**Purpose:** Receive notifications in Slack channels

**Steps:**

1.  Go to **Settings → Integrations → Slack → Connect**

2.  Click **Add to Slack**

3.  Select workspace and authorize

4.  Choose default channel for notifications

5.  Configure notification types:

  ---------------------------- ------------------------ ---------
  Notification                 Channel                  Enabled
  New dissonances (critical)   \#ai-governance-alerts   ☐
  Action items due             \#ai-governance          ☐
  Weekly summary               \#ai-governance          ☐
  System status                \#ai-governance-alerts   ☐
  ---------------------------- ------------------------ ---------

6.  Click **Save**

**Integration Troubleshooting**

  ---------------------------- ----------------------------- -------------------------------
  Issue                        Possible Cause                Solution
  Integration won\'t connect   Firewall blocking             Allowlist Phase Mirror IPs
  Sync failing                 Token expired                 Regenerate API token
  Missing data                 Permissions insufficient      Check integration permissions
  Duplicate items              Sync running multiple times   Check sync schedule settings
  ---------------------------- ----------------------------- -------------------------------

**SECURITY & COMPLIANCE**

**Security Settings**

**Location:** Settings → Security

  -------------------------- -------------------------------------
  Setting                    Recommended Configuration
  **MFA Enforcement**        Required for all users
  **Session Timeout**        8 hours (adjust per policy)
  **Password Policy**        12+ characters, complexity required
  **Failed Login Lockout**   5 attempts, 30-minute lockout
  **IP Allowlisting**        Enable if accessing from fixed IPs
  -------------------------- -------------------------------------

**Audit Logging**

**What\'s Logged:**

  --------------------- ----------------------------------------------
  Event Type            Examples
  **Authentication**    Login, logout, failed login, MFA events
  **User Management**   User created, role changed, user deactivated
  **AI Systems**        System created, edited, deleted, analyzed
  **Governance**        Rules changed, approvals, rejections
  **Data Access**       Reports generated, data exported
  **Settings**          Configuration changes, integration changes
  --------------------- ----------------------------------------------

**Accessing Audit Logs:**

1.  Go to **Settings → Audit Log**

2.  Filter by date range, user, event type

3.  Export: Click **Export → CSV** or **Export → JSON**

**Audit Log Retention:**

  ------------ ------------------------
  Tier         Retention
  Team         1 year
  Business     3 years
  Enterprise   7 years (configurable)
  ------------ ------------------------

**Data Export & Backup**

**On-Demand Export:**

1.  Go to **Settings → Data → Export**

2.  Select data types:

    -   \[ \] AI Systems

    -   \[ \] Dissonance Reports

    -   \[ \] Action Items

    -   \[ \] Audit Logs

    -   \[ \] User Data

3.  Select format (CSV, JSON)

4.  Click **Generate Export**

5.  Download when ready (link emailed)

**Scheduled Exports (Enterprise):**

1.  Go to **Settings → Data → Scheduled Exports**

2.  Configure schedule (daily, weekly, monthly)

3.  Select destination (email, S3, SFTP)

4.  Enable encryption if required

**TROUBLESHOOTING**

**Common Issues**

  ---------------------------- ------------------------- --------------------------------------------------
  Issue                        Diagnosis                 Solution
  **User can\'t log in**       Check user status         Settings → Users → Verify active and not locked
  **SSO not working**          Check IdP configuration   Verify metadata, certificates, attribute mapping
  **Integration failing**      Check credentials         Re-authenticate integration
  **Slow performance**         Check browser/network     Clear cache, try different browser
  **Missing data**             Check permissions         Verify user role and system assignments
  **Reports not generating**   Check data availability   Ensure AI systems have required data
  ---------------------------- ------------------------- --------------------------------------------------

**When to Escalate to Phase Mirror Support**

  ------------------ -----------------------------------------------------------------------------------------------
  Situation          Contact
  Platform outage    [[support\@phasemirror.com]{.underline}](mailto:support@phasemirror.com) (Priority: Critical)
  Data discrepancy   [[support\@phasemirror.com]{.underline}](mailto:support@phasemirror.com)
  Security concern   [[security\@phasemirror.com]{.underline}](mailto:security@phasemirror.com)
  Feature question   Your CSM or Help Center
  ------------------ -----------------------------------------------------------------------------------------------

**Support Request Template**

Subject: \[Priority\] Brief description\
\
Environment: \[your-tenant\].phasemirror.com\
User(s) affected: \[number or specific users\]\
Time of issue: \[date/time with timezone\]\
\
Description:\
\[What happened\]\
\
Expected behavior:\
\[What should have happened\]\
\
Steps to reproduce:\
1. \[Step 1\]\
2. \[Step 2\]\
3. \[Step 3\]\
\
Screenshots/logs attached: \[Yes/No\]\
\
Impact: \[Business impact of the issue\]

**ADMIN QUICK REFERENCE**

**Daily Tasks**

-   \[ \] Review failed login alerts (if configured)

-   \[ \] Check integration sync status

-   \[ \] Respond to access requests

**Weekly Tasks**

-   \[ \] Review new user requests

-   \[ \] Check audit log for anomalies

-   \[ \] Verify integrations are syncing

-   \[ \] Review support tickets

**Monthly Tasks**

-   \[ \] User access review

-   \[ \] Integration health check

-   \[ \] Security settings review

-   \[ \] Usage reporting for stakeholders

**Quarterly Tasks**

-   \[ \] Comprehensive access review

-   \[ \] Integration credential rotation

-   \[ \] Disaster recovery test

-   \[ \] Documentation update

**ADMIN KEYBOARD SHORTCUTS**

  ----------- --------------------
  Shortcut    Action
  G then S    Go to Settings
  G then U    Go to Users
  G then I    Go to Integrations
  G then A    Go to Audit Log
  Shift + N   New User
  ?           Show all shortcuts
  ----------- --------------------

**GUIDE 2: GOVERNANCE LEAD GUIDE**

**AI Governance Configuration & Oversight**

**Role:** Governance Lead\
**Time Commitment:** 4-6 hours/week\
**Prerequisites:** Compliance/risk management experience, understanding
of AI systems

**YOUR ROLE AS GOVERNANCE LEAD**

**What You\'re Responsible For**

  -------------------------- ----------------------------------------------------------
  Responsibility             Activities
  **Governance Framework**   Define policies, standards, procedures
  **Risk Classification**    Establish risk tiers and criteria
  **Compliance Mapping**     Map regulations to governance requirements
  **Oversight**              Review dissonances, approve systems, monitor remediation
  **Reporting**              Generate compliance and board reports
  -------------------------- ----------------------------------------------------------

**What You\'re NOT Responsible For**

-   Platform administration (Admin)

-   Day-to-day AI system documentation (System Owners)

-   Technical implementation of AI systems (Engineering)

-   Vendor management (Procurement)

**GOVERNANCE FRAMEWORK SETUP**

**Step 1: Define Risk Classification**

**Location:** Settings → Governance → Risk Classification

**Recommended Risk Tiers:**

  -------------- --------------------------------------------------------------------------- --------------------------------------------------------- ------------------
  Tier           Criteria                                                                    Examples                                                  Review Frequency
  **Critical**   Customer-facing decisions, regulatory scrutiny, material financial impact   Credit decisioning, fraud detection, clinical diagnosis   Monthly
  **High**       Significant business impact, compliance implications                        Customer service AI, underwriting support, claims         Quarterly
  **Medium**     Operational efficiency, limited external impact                             Document processing, scheduling, internal analytics       Semi-annually
  **Low**        Non-material, experimental, internal only                                   Prototypes, internal chatbots, testing                    Annually
  -------------- --------------------------------------------------------------------------- --------------------------------------------------------- ------------------

**Configuration Steps:**

1.  Go to **Settings → Governance → Risk Classification**

2.  Edit default tiers or create custom

3.  Define criteria for each tier

4.  Set review frequency per tier

5.  Save configuration

**Step 2: Configure Governance Rules**

**Location:** Settings → Governance → Rules

**Essential Rules to Configure:**

  ------------------- ------------------------ -------------------------------------------------------------------
  Rule Category       Rule Name                Configuration
  **Documentation**   Documentation Required   All systems must have: description, owner, data sources
  **Documentation**   Documentation Currency   Documentation must be updated within \[30/60/90\] days of changes
  **Approval**        New System Approval      Critical/High systems require Governance Lead approval
  **Approval**        Change Approval          Material changes to Critical systems require approval
  **Review**          Periodic Review          Systems must be reviewed per risk tier schedule
  **Monitoring**      Monitoring Required      Critical/High systems must have monitoring specification
  **Bias**            Bias Assessment          Customer-facing systems require bias assessment
  ------------------- ------------------------ -------------------------------------------------------------------

**Creating a Rule:**

1.  Go to **Settings → Governance → Rules → Add Rule**

2.  Configure:

    -   **Name:** Descriptive rule name

    -   **Applies to:** All systems, specific risk tiers, or tagged
        systems

    -   **Condition:** What triggers the rule

    -   **Action:** What happens (require documentation, require
        approval, create alert)

    -   **Notification:** Who to notify

3.  Test rule on sample system

4.  Activate rule

**Step 3: Set Up Approval Workflows**

**Location:** Settings → Governance → Workflows

**Recommended Workflows:**

  --------------------------- -------------------------------------- ---------------------------------------- -----------------
  Workflow                    Trigger                                Approvers                                SLA
  **New Critical System**     System registered with Critical risk   Governance Lead + Executive Sponsor      5 business days
  **New High System**         System registered with High risk       Governance Lead                          3 business days
  **Material Change**         Change to Critical system              Governance Lead                          3 business days
  **Production Deployment**   System status → Production             Governance Lead + System Owner Manager   5 business days
  --------------------------- -------------------------------------- ---------------------------------------- -----------------

**Workflow Configuration:**

1.  Go to **Settings → Governance → Workflows → Add Workflow**

2.  Configure:

    -   **Name:** Workflow name

    -   **Trigger:** What initiates the workflow

    -   **Steps:** Sequential or parallel approvals

    -   **Approvers:** Specific users, roles, or dynamic (e.g., system
        owner\'s manager)

    -   **SLA:** Target completion time

    -   **Escalation:** What happens if SLA missed

3.  Save and activate

**Step 4: Configure Compliance Packs (If Purchased)**

**EU AI Act Pack:**

1.  Go to **Compliance → EU AI Act → Configure**

2.  Set organization role: ☐ Provider ☐ Deployer ☐ Both

3.  Configure risk classification criteria

4.  Enable automated classification

5.  Set up conformity assessment workflows

**Financial Services Pack:**

1.  Go to **Compliance → Financial Services → Configure**

2.  Select applicable regulations: ☐ SR 11-7 ☐ Fair Lending ☐ BSA/AML

3.  Configure model risk tiers (align with MRM policy)

4.  Set up validation requirements per tier

5.  Configure examination documentation

**Healthcare Pack:**

1.  Go to **Compliance → Healthcare → Configure**

2.  Select applicable standards: ☐ HIPAA ☐ FDA SaMD ☐ Clinical Safety

3.  Configure PHI handling requirements

4.  Set up clinical validation workflows

**DAILY OPERATIONS**

**Reviewing Dissonance Reports**

**Where:** Dissonance → Dashboard

**Daily Review Process:**

1.  Check for new **Critical** dissonances (red indicators)

2.  Review **High** dissonances that are approaching SLA

3.  Verify action items are progressing

**Dissonance Triage:**

  -------------- ----------------- ----------------------------------------------------
  Severity       Response Time     Action
  **Critical**   Same day          Immediate review, assign owner, escalate if needed
  **High**       2 business days   Review, assign owner, set remediation timeline
  **Medium**     1 week            Review, assign owner, add to backlog
  **Low**        2 weeks           Review, determine if action needed
  -------------- ----------------- ----------------------------------------------------

**When Reviewing a Dissonance:**

1.  Click on dissonance to view details

2.  Verify the finding is accurate

3.  If valid:

    -   Click **Create Lever**

    -   Assign owner (usually System Owner)

    -   Set target date based on severity

    -   Add remediation guidance

4.  If false positive:

    -   Click **Dismiss**

    -   Document reason

    -   Consider rule adjustment

**Approving AI Systems**

**Where:** Workflows → Pending Approvals

**Approval Checklist:**

  ------------------------- ----------------------------------------------------------
  Checkpoint                Verification
  **Risk classification**   Is the assigned risk tier appropriate?
  **Documentation**         Are required documents uploaded?
  **Owner identified**      Is there a clear accountable owner?
  **Data handling**         Is sensitive data appropriately identified?
  **Regulatory mapping**    Are applicable regulations tagged?
  **Monitoring plan**       Is there a monitoring specification (for Critical/High)?
  ------------------------- ----------------------------------------------------------

**Approval Actions:**

  ----------------------------- -------------------------------------------------
  Action                        When to Use
  **Approve**                   All checkpoints satisfied
  **Approve with Conditions**   Minor items can be addressed post-approval
  **Request Changes**           Documentation incomplete or issues found
  **Reject**                    Significant concerns, system should not proceed
  ----------------------------- -------------------------------------------------

**Managing Action Items**

**Where:** Action Items → Dashboard

**Weekly Review:**

1.  Filter by **Status: Open** and **Due: This Week**

2.  Check progress with owners (via comments or directly)

3.  Escalate items at risk of missing deadline

4.  Close completed items after verification

**Escalation Process:**

  -------------- ----------------------------------------------
  Days Overdue   Action
  0-3 days       Reminder to owner
  4-7 days       Escalate to owner\'s manager
  8-14 days      Escalate to Executive Sponsor
  15+ days       Formal escalation, include in risk reporting
  -------------- ----------------------------------------------

**REPORTING**

**Available Reports**

  ------------------------ ---------------------- ----------- --------------------------------------------
  Report                   Audience               Frequency   Content
  **Executive Summary**    C-suite, Board         Quarterly   High-level governance status, key risks
  **Compliance Status**    Compliance Committee   Monthly     Regulatory alignment, gaps, remediation
  **Dissonance Summary**   Governance Team        Weekly      New findings, trends, action item status
  **System Inventory**     Risk Committee         Quarterly   Complete AI system listing with risk tiers
  **Audit Package**        Auditors, Examiners    On demand   Full documentation for examination
  ------------------------ ---------------------- ----------- --------------------------------------------

**Generating Reports**

**Executive Summary (Board Packet):**

1.  Go to **Reports → New Report → Executive Summary**

2.  Select reporting period

3.  Choose sections to include:

    -   \[ \] AI System Overview (count by risk tier)

    -   \[ \] Governance Health Score

    -   \[ \] Key Dissonances & Remediation

    -   \[ \] Regulatory Compliance Status

    -   \[ \] Upcoming Milestones

4.  Click **Generate**

5.  Review and edit narrative sections

6.  Export as PDF or PowerPoint

**Compliance Status Report:**

1.  Go to **Reports → New Report → Compliance Status**

2.  Select compliance framework (EU AI Act, SR 11-7, etc.)

3.  Select AI systems to include

4.  Click **Generate**

5.  Review findings

6.  Export or share

**Audit Package:**

1.  Go to **Reports → New Report → Audit Package**

2.  Select AI system(s)

3.  Select documentation types:

    -   \[ \] System registration and metadata

    -   \[ \] Governance documentation

    -   \[ \] Dissonance history

    -   \[ \] Action item history

    -   \[ \] Approval history

    -   \[ \] Audit trail

4.  Click **Generate**

5.  Download package (ZIP with all documents)

**Scheduling Reports**

1.  Go to **Reports → Scheduled Reports → Add Schedule**

2.  Select report type

3.  Configure parameters

4.  Set schedule (weekly, monthly, quarterly)

5.  Add recipients

6.  Save

**COMPLIANCE PACK OPERATIONS**

**EU AI Act Management**

**Risk Classification:**

1.  Go to **Compliance → EU AI Act → Classification**

2.  Run classification on new/unclassified systems

3.  Review automated classification results

4.  Override if needed (document reason)

**High-Risk System Requirements:**

For systems classified as high-risk:

  ------------------------- ------------------------------------------
  Requirement               How to Track
  Risk management system    Dissonance rule checks for documentation
  Data governance           Data handling fields in system record
  Technical documentation   Required documents checklist
  Record-keeping            Automatic via audit trail
  Transparency              Documentation requirements
  Human oversight           Oversight specification required
  Accuracy & robustness     Monitoring specification required
  ------------------------- ------------------------------------------

**Conformity Assessment:**

1.  Go to **Compliance → EU AI Act → Conformity Assessment**

2.  Select high-risk system

3.  Complete assessment checklist

4.  Upload supporting evidence

5.  Generate conformity declaration

**Financial Services (SR 11-7) Management**

**Model Inventory:**

1.  Go to **Compliance → Financial Services → Model Inventory**

2.  Review all AI systems tagged as \"model\" for SR 11-7

3.  Verify risk tier alignment with MRM policy

4.  Check validation status

**Validation Tracking:**

  -------------------- -------------------------------------------
  Validation Stage     Status Options
  Initial validation   Not started, In progress, Complete
  Ongoing monitoring   Active, Needs attention, Not configured
  Annual review        Scheduled, In progress, Complete, Overdue
  -------------------- -------------------------------------------

**Examination Preparation:**

1.  Go to **Compliance → Financial Services → Exam Prep**

2.  Select examination type (OCC, Fed, State)

3.  Generate documentation package

4.  Review for completeness

5.  Export for examiner

**METRICS & DASHBOARDS**

**Key Governance Metrics**

  --------------------------------- ----------------- ----------------------------------
  Metric                            Target            How to Track
  **AI System Coverage**            100% registered   Dashboard → Overview
  **Documentation Currency**        95% current       Dashboard → Documentation Health
  **Open Critical Dissonances**     0                 Dissonance → Filter by Critical
  **Dissonance Remediation Time**   \<30 days avg     Reports → Dissonance Trends
  **Overdue Action Items**          \<5%              Action Items → Filter by Overdue
  **Approval SLA Compliance**       \>95%             Workflows → Performance
  --------------------------------- ----------------- ----------------------------------

**Custom Dashboards**

1.  Go to **Dashboard → Customize**

2.  Add/remove widgets:

    -   AI Systems by Risk Tier (pie chart)

    -   Dissonance Trend (line chart)

    -   Action Items by Status (bar chart)

    -   Upcoming Reviews (calendar)

    -   Compliance Score by Framework (gauge)

3.  Arrange layout

4.  Save dashboard

**GOVERNANCE LEAD QUICK REFERENCE**

**Daily Checklist**

-   \[ \] Review new Critical/High dissonances

-   \[ \] Check pending approvals

-   \[ \] Monitor overdue action items

**Weekly Checklist**

-   \[ \] Review all new dissonances

-   \[ \] Follow up on action items due this week

-   \[ \] Check workflow SLA compliance

-   \[ \] Generate weekly dissonance summary

**Monthly Checklist**

-   \[ \] Comprehensive dissonance review

-   \[ \] Compliance status report

-   \[ \] Governance metrics review

-   \[ \] Stakeholder update

**Quarterly Checklist**

-   \[ \] Executive summary / board packet

-   \[ \] Full AI system inventory review

-   \[ \] Governance rule effectiveness review

-   \[ \] Policy/procedure update (if needed)

**GUIDE 3: SYSTEM OWNER GUIDE**

**AI System Registration & Management**

**Role:** System Owner\
**Time Commitment:** 2-4 hours/month per AI system\
**Prerequisites:** Ownership of one or more AI systems

**YOUR ROLE AS SYSTEM OWNER**

**What You\'re Responsible For**

  ------------------- -----------------------------------------------------
  Responsibility      Activities
  **Registration**    Register your AI systems in Phase Mirror
  **Documentation**   Maintain current, accurate documentation
  **Governance**      Ensure your systems comply with governance policies
  **Remediation**     Address dissonances and complete action items
  **Reviews**         Complete periodic reviews per schedule
  ------------------- -----------------------------------------------------

**What You\'re NOT Responsible For**

-   Platform administration (Admin)

-   Defining governance policies (Governance Lead)

-   Approving other owners\' systems (Governance Lead)

-   Enterprise-wide reporting (Governance Lead)

**REGISTERING AN AI SYSTEM**

**Before You Begin**

Gather this information:

  ----------------------- ----------------------- ---------------------------------------
  Information             Where to Find           Example
  **System name**         Your team\'s naming     \"Fraud Detection Model v2.1\"
  **Business purpose**    Product/business docs   \"Score transactions for fraud risk\"
  **System type**         Technical design        ML Model, LLM, Rules Engine, Agent
  **Data sources**        Data architecture       Customer transactions, account data
  **Data sensitivity**    Data classification     PII, financial data
  **Deployment status**   DevOps/release info     Production, Development, Pilot
  **Key stakeholders**    Org chart               Business owner, tech lead
  ----------------------- ----------------------- ---------------------------------------

**Registration Walkthrough**

**Step 1: Start New System**

1.  Go to **AI Systems → Add System**

2.  You\'ll see the registration form

**Step 2: Basic Information**

  ---------------------- --------------------------------------------------------- -------------
  Field                  Guidance                                                  Required
  **System Name**        Descriptive, unique name                                  Yes
  **System ID**          Auto-generated or custom (e.g., FRD-001)                  Yes
  **Description**        2-3 sentences on what the system does                     Yes
  **Business Purpose**   Why does this system exist? What problem does it solve?   Yes
  **Owner**              You (auto-filled)                                         Yes
  **Business Unit**      Your department                                           Yes
  **Business Sponsor**   Executive accountable for the system                      Recommended
  ---------------------- --------------------------------------------------------- -------------

**Step 3: Technical Details**

  ---------------------------- ------------------------------------------------------- ----------------------------------
  Field                        Options                                                 Guidance
  **System Type**              ML Model, LLM/GenAI, Rules Engine, Agentic AI, Hybrid   Select primary type
  **Framework**                TensorFlow, PyTorch, Scikit-learn, Custom, etc.         Select all that apply
  **Deployment Environment**   Cloud (AWS/Azure/GCP), On-premise, Hybrid               Where does it run?
  **Version**                  Current version number                                  e.g., 2.1.0
  **Source Repository**        Link to code repo                                       Auto-filled if GitHub integrated
  ---------------------------- ------------------------------------------------------- ----------------------------------

**Step 4: Risk Classification**

  ---------------------- ------------------------------------- ---------------------------------
  Field                  Options                               Guidance
  **Risk Tier**          Critical, High, Medium, Low           Use organization\'s criteria
  **Customer Impact**    Direct, Indirect, None                Does it affect customers?
  **Regulatory Scope**   Select applicable regulations         GDPR, HIPAA, Fair Lending, etc.
  **Decision Type**      Automated, Human-assisted, Advisory   How are outputs used?
  ---------------------- ------------------------------------- ---------------------------------

**Risk Tier Selection Guide:**

  ------------------------------------- -------------------------------- --------------------------- ------------------------
  Choose Critical If                    Choose High If                   Choose Medium If            Choose Low If
  Makes decisions affecting customers   Significant business impact      Internal efficiency focus   Experimental/prototype
  Subject to regulatory scrutiny        Compliance implications          Limited external impact     No customer impact
  Material financial impact             Moderate financial impact        Operational support         Non-material
  Autonomous customer-facing            Customer-facing with oversight   Internal users only         Testing only
  ------------------------------------- -------------------------------- --------------------------- ------------------------

**Step 5: Data & Privacy**

  -------------------- -------------------------------------------------
  Field                Guidance
  **Data Sources**     List all data inputs to the system
  **Data Types**       Select: PII, Financial, Health, Biometric, etc.
  **Data Volume**      Approximate records processed
  **Data Retention**   How long is data kept
  **Privacy Impact**   Has PIA been completed?
  -------------------- -------------------------------------------------

**Step 6: Governance**

  ----------------------- ------------------------------------
  Field                   Guidance
  **Approval Status**     Current approval state
  **Last Review Date**    When was system last reviewed?
  **Next Review Date**    Auto-calculated based on risk tier
  **Monitoring Status**   Is monitoring in place?
  ----------------------- ------------------------------------

**Step 7: Documentation Upload**

Upload required documents:

  ---------------------------- ---------------------------------- ---------------
  Document                     Description                        Required
  **System Design**            Architecture, design decisions     Critical/High
  **Model Card**               Standardized model documentation   ML models
  **Data Dictionary**          Description of data elements       All
  **Validation Report**        Initial validation results         Critical/High
  **Monitoring Spec**          How system is monitored            Critical/High
  **Approval Documentation**   Sign-offs, approvals               All
  ---------------------------- ---------------------------------- ---------------

**Step 8: Submit**

1.  Review all information

2.  Click **Submit for Review** (if approval required) or **Save** (if
    no approval needed)

3.  You\'ll receive notification when approved

**MAINTAINING YOUR AI SYSTEMS**

**Keeping Documentation Current**

**When to Update:**

  -------------------------- ----------------------------------------------
  Event                      Update Required
  Model retrained            Update version, upload new validation report
  Data sources changed       Update data section, assess impact
  Significant code changes   Update technical details, version
  Business purpose changed   Update description, reassess risk tier
  New regulations apply      Update regulatory tags
  Ownership changed          Transfer ownership
  -------------------------- ----------------------------------------------

**How to Update:**

1.  Go to **AI Systems → \[Your System\] → Edit**

2.  Make changes

3.  Add change note (required for Critical/High systems)

4.  Save

**Material vs. Non-Material Changes:**

  --------------------------------- ---------------------------
  Material (May Require Approval)   Non-Material
  Risk tier change                  Minor description updates
  New data sources                  Contact information
  Algorithm/model changes           Documentation refresh
  Deployment environment change     Version increment (minor)
  Regulatory scope change           Metadata corrections
  --------------------------------- ---------------------------

**Responding to Dissonances**

**When You Receive a Dissonance:**

1.  You\'ll get notification (email and/or Slack)

2.  Go to **Dissonance → \[Finding\]**

3.  Review the details:

    -   What policy is being checked

    -   What was found (or not found)

    -   Why this matters

    -   Suggested remediation

**Dissonance Response Options:**

  --------------------------- --------------------------------------- ------------------------------------------------
  Response                    When to Use                             How
  **Accept & Remediate**      Finding is valid, will fix              Click **Create Lever**, set timeline
  **Request Clarification**   Need more information                   Add comment, tag Governance Lead
  **Dispute**                 Finding is incorrect                    Add comment with evidence, tag Governance Lead
  **Request Exception**       Valid finding but exception warranted   Follow exception process
  --------------------------- --------------------------------------- ------------------------------------------------

**Creating an Action Item (Lever):**

1.  Click **Create Lever** on the dissonance

2.  Fill in:

    -   **Title:** Clear description of remediation

    -   **Owner:** You or delegate to team member

    -   **Due Date:** Based on severity (Critical: 7 days, High: 14
        days, Medium: 30 days)

    -   **Description:** Specific steps to remediate

3.  Save

4.  Complete remediation

5.  Add evidence/comments showing completion

6.  Mark as complete

**Completing Periodic Reviews**

**Review Schedule:**

  ----------- ------------------ ----------------
  Risk Tier   Review Frequency   Reminder
  Critical    Monthly            7 days before
  High        Quarterly          14 days before
  Medium      Semi-annually      30 days before
  Low         Annually           30 days before
  ----------- ------------------ ----------------

**Review Checklist:**

1.  Go to **AI Systems → \[Your System\] → Start Review**

2.  Complete each section:

  ------------------- --------------------------------------------------
  Section             Questions
  **System Status**   Is the system still active? Any planned changes?
  **Documentation**   Is all documentation current and accurate?
  **Performance**     Is the system performing as expected?
  **Risk**            Has the risk profile changed?
  **Compliance**      Any new regulatory requirements?
  **Issues**          Any incidents or issues since last review?
  **Monitoring**      Is monitoring effective? Any anomalies?
  ------------------- --------------------------------------------------

3.  Upload any updated documentation

4.  Add review notes

5.  Submit review

**COMMON TASKS**

**Transferring Ownership**

If you\'re leaving the team or system is transferring:

1.  Go to **AI Systems → \[Your System\] → Transfer Ownership**

2.  Select new owner

3.  Add transfer notes

4.  New owner must accept transfer

5.  You remain as backup contact for 30 days

**Archiving a System**

If AI system is being decommissioned:

1.  Go to **AI Systems → \[Your System\] → Archive**

2.  Select reason:

    -   Replaced by new system (link to replacement)

    -   No longer needed

    -   Failed validation

    -   Other (explain)

3.  Confirm data handling (retain for audit or delete)

4.  Submit for approval

5.  System moves to archived state

**Requesting an Exception**

If governance rule doesn\'t fit your situation:

1.  Go to **AI Systems → \[Your System\] → Request Exception**

2.  Select rule requiring exception

3.  Provide justification:

    -   Why rule doesn\'t apply

    -   Compensating controls in place

    -   Duration of exception requested

4.  Submit for Governance Lead approval

5.  Implement compensating controls if approved

6.  Exception expires per approved duration

**SYSTEM OWNER QUICK REFERENCE**

**Monthly Checklist**

-   \[ \] Review system for any changes needing documentation

-   \[ \] Check for new dissonances on your systems

-   \[ \] Update action items in progress

-   \[ \] Verify monitoring is functioning

**Quarterly Checklist**

-   \[ \] Complete periodic review (High risk systems)

-   \[ \] Update documentation for any changes

-   \[ \] Review and refresh risk assessment

-   \[ \] Check regulatory mapping for changes

**When Changes Occur**

-   \[ \] Model retrained → Update version, upload validation

-   \[ \] Data source added → Update data section, assess impact

-   \[ \] Major code change → Update docs, may need re-approval

-   \[ \] Incident occurred → Document and report

**SYSTEM OWNER KEYBOARD SHORTCUTS**

  ---------- -----------------------
  Shortcut   Action
  G then M   Go to My Systems
  G then D   Go to My Dissonances
  G then A   Go to My Action Items
  E          Edit current system
  R          Start review
  ?          Show all shortcuts
  ---------- -----------------------

**GUIDE 4: CONTRIBUTOR GUIDE**

**Documenting & Supporting AI Systems**

**Role:** Contributor\
**Time Commitment:** 1-2 hours/week\
**Prerequisites:** Working on AI systems, basic documentation skills

**YOUR ROLE AS CONTRIBUTOR**

**What You Can Do**

  -------------- ----------------------------------------------
  Permission     Description
  **View**       See AI systems you\'re assigned to
  **Edit**       Update documentation and metadata
  **Comment**    Add comments to dissonances and action items
  **Upload**     Add documentation files
  **Complete**   Mark assigned action items complete
  -------------- ----------------------------------------------

**What You Cannot Do**

-   Register new AI systems (System Owner)

-   Change risk tier or owner (System Owner)

-   Approve systems or changes (Governance Lead)

-   Configure platform settings (Admin)

**GETTING STARTED**

**Your Dashboard**

When you log in, you\'ll see:

  --------------------- ----------------------------------------------
  Section               Content
  **My Systems**        AI systems you\'re assigned to contribute to
  **My Action Items**   Tasks assigned to you
  **Recent Activity**   Updates on systems you follow
  --------------------- ----------------------------------------------

**Understanding Your Assignments**

You\'re assigned to AI systems by the System Owner. For each system, you
can:

-   View all system information

-   Edit documentation and metadata

-   Upload new documents

-   Add comments

-   Complete action items assigned to you

**COMMON TASKS**

**Updating System Documentation**

**When to Update:**

  ----------------------- -----------------------------------
  Trigger                 What to Update
  Code deployment         Version number, technical details
  Model retraining        Model metrics, validation results
  Bug fixes               Change log, known issues
  Feature additions       Functionality description
  Documentation request   Requested sections
  ----------------------- -----------------------------------

**How to Update:**

1.  Go to **My Systems → \[System Name\] → Edit**

2.  Navigate to section needing update

3.  Make changes

4.  Add change note describing what changed

5.  Click **Save**

**Writing Good Documentation:**

  ---------------------------- --------------------------------
  Do                           Don\'t
  Be specific and concrete     Use vague language
  Include version numbers      Assume reader knows context
  Date your updates            Leave outdated information
  Link to source materials     Copy-paste without attribution
  Use consistent terminology   Invent new terms
  ---------------------------- --------------------------------

**Uploading Documents**

**Supported File Types:**

  -------------- ------------------------- ----------
  Type           Formats                   Max Size
  Documents      PDF, DOCX, MD, TXT        25 MB
  Spreadsheets   XLSX, CSV                 10 MB
  Code           PY, IPYNB, JSON, YAML     5 MB
  Images         PNG, JPG (for diagrams)   10 MB
  -------------- ------------------------- ----------

**How to Upload:**

1.  Go to **My Systems → \[System Name\] → Documents**

2.  Click **Upload**

3.  Select file(s)

4.  Add document type tag (Design, Validation, Monitoring, etc.)

5.  Add description

6.  Click **Upload**

**Document Naming Convention:**

\[SystemID\]\_\[DocType\]\_\[Version\]\_\[Date\].\[ext\]\
\
Examples:\
FRD001\_ModelCard\_v2.1\_20260115.pdf\
FRD001\_ValidationReport\_v2.1\_20260115.pdf\
FRD001\_DataDictionary\_v1.0\_20260115.xlsx

**Completing Action Items**

**Viewing Your Action Items:**

1.  Go to **My Action Items**

2.  Filter by status: Open, In Progress, Completed

3.  Sort by due date to prioritize

**Working on an Action Item:**

1.  Click on action item to view details

2.  Review what\'s needed

3.  Update status to **In Progress**

4.  Do the work

5.  Add comments documenting what you did

6.  Attach evidence if applicable

7.  Update status to **Complete**

**Action Item Statuses:**

  ----------------- ----------------------------------
  Status            Meaning
  **Open**          Not started
  **In Progress**   Actively working on it
  **Blocked**       Can\'t proceed, need help
  **Complete**      Done, pending verification
  **Verified**      Confirmed complete by owner/lead
  **Closed**        Fully resolved
  ----------------- ----------------------------------

**Responding to Comments**

When someone comments on a system or action item you\'re working on:

1.  You\'ll get a notification

2.  Click to view comment

3.  Respond with:

    -   Information requested

    -   Questions for clarification

    -   Status updates

4.  \@mention specific people if needed

**BEST PRACTICES**

**Documentation Best Practices**

  ---------------------------- ---------------------------------------------------------------------------------------
  Practice                     Example
  **Version everything**       \"Model v2.1 trained on 2025-12-15\"
  **Be specific about data**   \"Uses 24 months of transaction history\"
  **Document assumptions**     \"Assumes normal market conditions\"
  **Note limitations**         \"Not validated for transactions \>\$100K\"
  **Include contacts**         \"Questions: [[team-fraud\@company.com]{.underline}](mailto:team-fraud@company.com)\"
  ---------------------------- ---------------------------------------------------------------------------------------

**Time Management**

  ----------------------- ---------------------
  Activity                Suggested Frequency
  Check action items      Daily (5 min)
  Update documentation    As changes occur
  Review system changes   Weekly (15 min)
  Upload new documents    As created
  ----------------------- ---------------------

**CONTRIBUTOR QUICK REFERENCE**

**Daily**

-   \[ \] Check for new action items assigned to you

-   \[ \] Update action items in progress

**Weekly**

-   \[ \] Review systems you contribute to for needed updates

-   \[ \] Upload any new documentation created

-   \[ \] Respond to comments/questions

**Keyboard Shortcuts**

  ---------- ------------------------------
  Shortcut   Action
  G then M   Go to My Systems
  G then A   Go to My Action Items
  E          Edit (when viewing a system)
  ?          Show all shortcuts
  ---------- ------------------------------

**GUIDE 5: VIEWER GUIDE**

**Monitoring AI Governance Status**

**Role:** Viewer\
**Time Commitment:** 30 minutes/week\
**Prerequisites:** None (read-only access)

**YOUR ROLE AS VIEWER**

**What You Can Do**

  --------------------- ---------------------------------------------
  Permission            Description
  **View dashboards**   See governance status and metrics
  **View AI systems**   Review system information and documentation
  **View reports**      Access generated reports
  **Export**            Download reports (if enabled)
  --------------------- ---------------------------------------------

**What You Cannot Do**

-   Edit any information

-   Register or approve systems

-   Create or complete action items

-   Configure any settings

**YOUR DASHBOARD**

**Overview Screen**

When you log in, you\'ll see the executive dashboard:

  ----------------------------- -----------------------------------
  Widget                        What It Shows
  **Governance Health Score**   Overall health (0-100)
  **AI Systems by Risk**        Pie chart of systems by risk tier
  **Open Dissonances**          Count by severity
  **Compliance Status**         Status by framework
  **Recent Activity**           Latest changes and updates
  ----------------------------- -----------------------------------

**Understanding the Governance Health Score**

  -------------- ----------------- -------------------------------------------------
  Score          Meaning           Typical Causes
  **90-100**     Excellent         All systems documented, no critical dissonances
  **80-89**      Good              Minor gaps, action items in progress
  **70-79**      Fair              Some overdue items, documentation gaps
  **60-69**      Needs Attention   Multiple dissonances, overdue actions
  **Below 60**   At Risk           Significant governance gaps
  -------------- ----------------- -------------------------------------------------

**VIEWING INFORMATION**

**AI System List**

1.  Go to **AI Systems**

2.  View list of all registered systems

3.  Filter by:

    -   Risk tier

    -   Business unit

    -   Status

    -   Compliance framework

4.  Click any system to view details

**System Details**

When viewing a system:

  ----------------- --------------------------------------
  Tab               Content
  **Overview**      Basic info, owner, risk tier, status
  **Technical**     Type, framework, deployment details
  **Data**          Data sources, sensitivity, handling
  **Governance**    Policies, approvals, reviews
  **Documents**     Uploaded documentation
  **History**       Change history, audit trail
  **Dissonances**   Current and historical findings
  ----------------- --------------------------------------

**Reports**

1.  Go to **Reports**

2.  View available reports:

    -   Executive Summary

    -   Compliance Status

    -   System Inventory

    -   Dissonance Trends

3.  Click to view or download

**KEY METRICS TO MONITOR**

**For Executives**

  ----------------------------------- ------------------------------- ---------------------------
  Metric                              What to Look For                Concern Threshold
  **Governance Health Score**         Trend over time                 Below 80 or declining
  **Critical Dissonances**            Should be zero                  Any open \> 7 days
  **Systems Without Documentation**   Should be zero                  Any Critical/High systems
  **Overdue Actions**                 Should be minimal               \>10% of total
  **Compliance Coverage**             Should be 100% for applicable   Any gaps
  ----------------------------------- ------------------------------- ---------------------------

**For Board Members**

  --------------------------- ------------------------------
  Metric                      Why It Matters
  **AI System Count**         Understanding AI footprint
  **Risk Distribution**       Exposure in critical systems
  **Regulatory Compliance**   Legal/regulatory exposure
  **Governance Trends**       Program effectiveness
  --------------------------- ------------------------------

**VIEWER QUICK REFERENCE**

**Weekly Review (15-30 min)**

1.  Check Governance Health Score

2.  Review any new Critical dissonances

3.  Check overdue action items trend

4.  Note items for follow-up with team

**Monthly Review**

1.  Review executive summary report

2.  Compare metrics to prior month

3.  Note trends to discuss with leadership

**Keyboard Shortcuts**

  ---------- --------------------
  Shortcut   Action
  G then D   Go to Dashboard
  G then S   Go to AI Systems
  G then R   Go to Reports
  ?          Show all shortcuts
  ---------- --------------------

**GUIDE 6: AUDITOR GUIDE**

**Accessing Audit Information**

**Role:** Auditor\
**Time Commitment:** As needed during audits\
**Prerequisites:** Auditor credentials, understanding of AI governance

**YOUR ROLE AS AUDITOR**

**What You Can Do**

  ------------------------ ---------------------------------------
  Permission               Description
  **Full read access**     View all AI systems and documentation
  **Audit trail access**   View complete audit logs
  **Report access**        View and download all reports
  **Export access**        Download data and evidence
  ------------------------ ---------------------------------------

**What You Cannot Do**

-   Modify any data

-   Create or edit AI systems

-   Complete action items

-   Change any configuration

**AUDIT CAPABILITIES**

**Audit Trail**

**Where:** Settings → Audit Log (with Auditor role)

**What\'s Captured:**

  -------------------- ---------------------------------------------
  Event Category       Events Logged
  **Authentication**   Login, logout, failed attempts, MFA events
  **AI Systems**       Created, edited, deleted, ownership changed
  **Documents**        Uploaded, downloaded, deleted
  **Governance**       Rules changed, approvals, rejections
  **Dissonances**      Created, updated, dismissed, remediated
  **Action Items**     Created, assigned, completed
  **Reports**          Generated, downloaded
  **Users**            Created, modified, deactivated
  **Settings**         Configuration changes
  -------------------- ---------------------------------------------

**Audit Log Fields:**

  ---------------- --------------------------
  Field            Description
  **Timestamp**    UTC time of event
  **User**         Who performed the action
  **Action**       What was done
  **Object**       What was affected
  **Details**      Additional context
  **IP Address**   Source IP (if available)
  ---------------- --------------------------

**Filtering & Export:**

1.  Go to **Audit Log**

2.  Set date range

3.  Filter by user, action type, object

4.  Click **Export** → CSV or JSON

**Evidence Collection**

**System Documentation:**

1.  Go to **AI Systems → \[System\]**

2.  View all tabs for evidence

3.  Download documents individually or as package

**Governance Evidence:**

1.  Go to **AI Systems → \[System\] → Governance**

2.  View approval history

3.  View review history

4.  Download approval documentation

**Dissonance Evidence:**

1.  Go to **Dissonance → \[Finding\]**

2.  View complete history

3.  View remediation evidence

4.  Export finding details

**Audit Package Generation**

1.  Go to **Reports → Audit Package**

2.  Select scope:

    -   All systems

    -   Specific systems

    -   Date range

3.  Select content:

    -   \[ \] System inventory

    -   \[ \] Documentation

    -   \[ \] Governance records

    -   \[ \] Dissonance history

    -   \[ \] Action item history

    -   \[ \] Approval records

    -   \[ \] Audit trail

4.  Click **Generate**

5.  Download when ready

**AUDIT PROCEDURES**

**Pre-Audit Preparation**

**Request from organization:**

1.  Auditor user account (or temporary access)

2.  Scope of systems to review

3.  Relevant date range

4.  Any specific concerns or focus areas

**During Audit**

**Typical procedures:**

  -------------------------- ----------------------------------------------
  Procedure                  How to Execute
  **Inventory validation**   Compare AI System list to other sources
  **Documentation review**   Review documents for completeness, currency
  **Control testing**        Verify approval workflows function correctly
  **Dissonance review**      Assess findings and remediation timeliness
  **Access review**          Review user list and permissions
  **Change management**      Review audit trail for changes
  -------------------------- ----------------------------------------------

**Evidence Retention**

All exports include:

-   Timestamp of export

-   User who exported

-   Scope of export

-   Data integrity hash

**AUDITOR QUICK REFERENCE**

**Key Locations**

  -------------------- --------------------------------------
  Need                 Location
  AI System list       AI Systems
  System details       AI Systems → \[System\]
  Governance records   AI Systems → \[System\] → Governance
  Audit trail          Settings → Audit Log
  Reports              Reports
  Audit package        Reports → Audit Package
  -------------------- --------------------------------------

**Keyboard Shortcuts**

  ---------- --------------------
  Shortcut   Action
  G then A   Go to Audit Log
  G then S   Go to AI Systems
  G then R   Go to Reports
  ?          Show all shortcuts
  ---------- --------------------

**ROLE GUIDE SUMMARY**

  --------------------------- ---------------------------- -------------------------------------------------
  Guide                       Primary Audience             Key Responsibilities
  **Admin Guide**             IT administrators            Platform config, users, integrations
  **Governance Lead Guide**   Compliance/risk officers     Governance framework, oversight, reporting
  **System Owner Guide**      AI/ML team leads             System registration, documentation, remediation
  **Contributor Guide**       Developers, analysts         Documentation, action items
  **Viewer Guide**            Executives, stakeholders     Monitoring, awareness
  **Auditor Guide**           Internal/external auditors   Evidence collection, audit trail
  --------------------------- ---------------------------- -------------------------------------------------

**END OF ROLE-SPECIFIC GUIDES**

These role-specific guides provide targeted information for each user
type. Would you like me to create:

-   Printable quick reference cards for each role

-   Training presentation slides for each role

-   Certification quiz questions for role proficiency

-   Workflow diagrams for common tasks by role

-   Onboarding email templates for each role?

⁂

1.  A Clear Guide to Phase Mirror\'s Services.pdf

2.  Phase mirror dissonance\_\_\_Open core must be useful.pdf

3.  Phase Mirror\_ Comprehensive Services Catalog.docx.pdf

4.  License\_ Strategic & Legal Analysis.pdf

5.  Phase Mirror\_ Consultation & SaaS.pdf

6.  Agentic Domain-Specific Reasoning.pdf

7.  Policy Memo\_ Managing Agentic AI Liability with the Phase Mirror
    Framework.pdf

8.  The Phase Mirror does not resolve dissonance---it names it.pdf

9.  Understanding Phase Mirror Dissonance\_ A Beginner\'s Guide.pdf

10. The Phase of Mirror Dissonance.pdf

11. Implementation Guide\_ Applying Phase Mirror Dissonance.pdf

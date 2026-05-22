---
slug: in-plain-chat-lets-create-workflow-diagrams-for-co
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 00-foundations/phase-mirror/in plain chat lets create_Workflow diagrams for
    co.md
  last_synced: '2026-03-20T17:17:22.054202Z'
---

![](media/image-eee98b9c01f5e6dc9e9da251d0dc6051fdb0d228.png){width="2.6466666666666665in"
height="0.6666666666666666in"}

**in plain chat lets create**

Workflow diagrams for common tasks by role

Here are comprehensive workflow diagrams for common tasks organized by
role:

**PHASE MIRROR WORKFLOW DIAGRAMS**

**Common Tasks by Role**

**Version:** 2.0 \| **Date:** January 2026\
**Purpose:** Visual process guides for daily operations

**WORKFLOW DIAGRAM LEGEND**

┌─────────────────────────────────────────────────────────────────┐\
│ SYMBOL LEGEND │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ◯ START / END ◇ DECISION POINT │\
│ │\
│ ▢ ACTION/TASK ▣ SYSTEM ACTION (automated) │\
│ │\
│ ◈ SUBPROCESS ☐ DOCUMENT/ARTIFACT │\
│ │\
│ ⬡ EXTERNAL SYSTEM ⏱ WAIT/TIMER │\
│ │\
│ → FLOW DIRECTION ⚠ ALERT/NOTIFICATION │\
│ │\
│ ═══ SWIMLANE ··· OPTIONAL PATH │\
│ BOUNDARY │\
└─────────────────────────────────────────────────────────────────┘

**SECTION 1: ADMINISTRATOR WORKFLOWS**

**WORKFLOW A-1: USER PROVISIONING (Manual)**

**Trigger:** New employee needs Phase Mirror access\
**Owner:** Administrator\
**SLA:** Within 1 business day of request

◯ START: Access Request Received\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ ADMINISTRATOR │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Verify request │\
│ │ • Confirm manager approval │\
│ │ • Verify employee status │\
│ │ • Determine appropriate role │\
│ │ │\
│ ▼ │\
│ ◇ Request │\
│ │ valid? │\
│ │ │\
│ ├──NO──► ▢ Reject request ──► ⚠ Notify requester ──► ◯ END │\
│ │ with reason │\
│ │ │\
│ YES │\
│ │ │\
│ ▼ │\
│ ▢ Navigate to Settings → Users → Invite User │\
│ │ │\
│ ▼ │\
│ ▢ Enter user details │\
│ │ • Email address │\
│ │ • First name, Last name │\
│ │ • Select role │\
│ │ │\
│ ▼ │\
│ ◇ Role requires │\
│ │ system assignments? │\
│ │ │\
│ ├──YES──► ▢ Assign AI systems ──┐ │\
│ │ │ │\
│ NO │ │\
│ │◄───────────────────────────────┘ │\
│ ▼ │\
│ ▢ Click \"Send Invitation\" │\
│ │ │\
│ ▼ │\
│ ▣ SYSTEM: Invitation email sent │\
│ │ │\
└───┼──────────────────────────────────────────────────────────────┘\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ NEW USER │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Receive invitation email │\
│ │ │\
│ ▼ │\
│ ▢ Click activation link │\
│ │ │\
│ ▼ │\
│ ▢ Set password (meets policy) │\
│ │ │\
│ ▼ │\
│ ▢ Configure MFA │\
│ │ • Scan QR code with authenticator │\
│ │ • Enter verification code │\
│ │ │\
│ ▼ │\
│ ▣ SYSTEM: Account activated │\
│ │ │\
└───┼──────────────────────────────────────────────────────────────┘\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ ADMINISTRATOR │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Verify user can log in │\
│ │ │\
│ ▼ │\
│ ▢ Document provisioning │\
│ │ • Update access tracking │\
│ │ • Log in ticketing system │\
│ │ │\
│ ▼ │\
│ ⚠ Notify requester of completion │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
◯ END: User Provisioned

**Key Metrics:**

-   Time from request to invitation: \< 4 hours

-   Time from invitation to activation: \< 24 hours

-   First-attempt success rate: \> 95%

**WORKFLOW A-2: SSO CONFIGURATION (SAML)**

**Trigger:** Organization implementing single sign-on\
**Owner:** Administrator + IT Team\
**SLA:** 3-5 business days

◯ START: SSO Implementation Request\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ ADMINISTRATOR + IT │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Gather requirements │\
│ │ • Identity Provider (Okta, Azure AD, etc.) │\
│ │ • User attribute requirements │\
│ │ • Group-to-role mapping needs │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ IT / IDP ADMIN │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Create application in IdP │\
│ │ • Application name: Phase Mirror │\
│ │ • Type: SAML 2.0 │\
│ │ │\
│ ▼ │\
│ ▢ Configure SAML settings in IdP │\
│ │ • Entity ID: https://\[tenant\].phasemirror.com/saml/metadata│\
│ │ • ACS URL: https://\[tenant\].phasemirror.com/saml/acs │\
│ │ • Sign-on URL: https://\[tenant\].phasemirror.com/saml/login │\
│ │ │\
│ ▼ │\
│ ▢ Configure attribute mapping │\
│ │ • email (required) │\
│ │ • firstName (required) │\
│ │ • lastName (required) │\
│ │ • groups (optional) │\
│ │ │\
│ ▼ │\
│ ▢ Assign users/groups to application │\
│ │ │\
│ ▼ │\
│ ☐ Export IdP metadata XML │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ ADMINISTRATOR │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Navigate to Settings → Authentication → SAML │\
│ │ │\
│ ▼ │\
│ ▢ Upload IdP metadata XML │\
│ │ │\
│ ▼ │\
│ ▢ Configure attribute mapping │\
│ │ • Map IdP attributes to Phase Mirror fields │\
│ │ │\
│ ▼ │\
│ ▢ Configure group-to-role mapping (optional) │\
│ │ ┌────────────────────┬─────────────────┐ │\
│ │ │ IdP Group │ Phase Mirror │ │\
│ │ ├────────────────────┼─────────────────┤ │\
│ │ │ pm-admins │ Admin │ │\
│ │ │ pm-governance │ Governance Lead │ │\
│ │ │ pm-owners │ System Owner │ │\
│ │ │ pm-contributors │ Contributor │ │\
│ │ │ pm-viewers │ Viewer │ │\
│ │ └────────────────────┴─────────────────┘ │\
│ │ │\
│ ▼ │\
│ ▢ Save configuration (DO NOT enable yet) │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ TESTING PHASE │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Test with admin account │\
│ │ • Open incognito browser │\
│ │ • Navigate to SSO login URL │\
│ │ • Authenticate with IdP │\
│ │ │\
│ ▼ │\
│ ◇ Login │\
│ │ successful? │\
│ │ │\
│ ├──NO──► ▢ Troubleshoot ─────────────────────┐ │\
│ │ • Check IdP logs │ │\
│ │ • Verify attribute mapping │ │\
│ │ • Check certificate validity │ │\
│ │ │ │ │\
│ │ ▼ │ │\
│ │ ◇ Issue resolved? ──NO──► ⬡ Contact IdP vendor │\
│ │ │ │ │\
│ │ YES │ │\
│ │ │ │ │\
│ │◄───────────────────┴────────────────────────┘ │\
│ │ │\
│ YES │\
│ │ │\
│ ▼ │\
│ ▢ Verify correct role assigned │\
│ │ │\
│ ▼ │\
│ ▢ Test with non-admin user │\
│ │ │\
│ ▼ │\
│ ◇ All tests │\
│ │ pass? │\
│ │ │\
│ ├──NO──► Return to troubleshooting │\
│ │ │\
│ YES │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ GO-LIVE │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Enable SSO for organization │\
│ │ Settings → Authentication → Enable SAML │\
│ │ │\
│ ▼ │\
│ ◇ Keep password │\
│ │ login as fallback? │\
│ │ │\
│ ├──YES──► ▢ Leave password auth enabled ──┐ │\
│ │ │ │\
│ ├──NO───► ▢ Disable password auth ────────┤ │\
│ │ (SSO only) │ │\
│ │ │ │\
│ │◄─────────────────────────────────────────┘ │\
│ ▼ │\
│ ⚠ Notify all users of SSO availability │\
│ │ │\
│ ▼ │\
│ ▢ Document configuration │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
◯ END: SSO Configured

**WORKFLOW A-3: INTEGRATION SETUP (GitHub)**

**Trigger:** Connect source control for AI discovery\
**Owner:** Administrator\
**SLA:** 1-2 hours

◯ START: GitHub Integration Request\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ ADMINISTRATOR │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Verify GitHub organization access │\
│ │ • Must be org owner or admin │\
│ │ │\
│ ▼ │\
│ ▢ Navigate to Settings → Integrations → GitHub │\
│ │ │\
│ ▼ │\
│ ▢ Click \"Connect GitHub\" │\
│ │ │\
│ ▼ │\
│ ▣ SYSTEM: Redirect to GitHub OAuth │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ ⬡ GITHUB │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Review permissions requested │\
│ │ • Read access to code │\
│ │ • Read access to metadata │\
│ │ • Webhooks for change notifications │\
│ │ │\
│ ▼ │\
│ ◇ Approve │\
│ │ permissions? │\
│ │ │\
│ ├──NO──► ◯ END (Integration cancelled) │\
│ │ │\
│ YES │\
│ │ │\
│ ▼ │\
│ ▢ Select organization(s) to authorize │\
│ │ │\
│ ▼ │\
│ ▣ GITHUB: Redirect back to Phase Mirror │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ ADMINISTRATOR │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Configure repository access │\
│ │ │\
│ ◇ Access scope? │\
│ │ │\
│ ├──ALL──► ▢ Select \"All repositories\" ──────┐ │\
│ │ │ │\
│ ├──SOME─► ▢ Select specific repositories ───┤ │\
│ │ │ │\
│ │◄───────────────────────────────────────────┘ │\
│ ▼ │\
│ ▢ Configure scan settings │\
│ │ ☑ Scan for ML frameworks │\
│ │ (TensorFlow, PyTorch, scikit-learn, etc.) │\
│ │ ☑ Scan for model files │\
│ │ (.pkl, .h5, .onnx, .pt, etc.) │\
│ │ ☑ Scan for config files │\
│ │ (model cards, MLproject, etc.) │\
│ │ ☐ Scan for Jupyter notebooks (optional) │\
│ │ │\
│ ▼ │\
│ ▢ Set sync schedule │\
│ │ • Daily (default) │\
│ │ • Custom schedule │\
│ │ │\
│ ▼ │\
│ ▢ Click \"Save and Sync\" │\
│ │ │\
│ ▼ │\
│ ▣ SYSTEM: Initial sync begins │\
│ │ ┌─────────────────────────────────┐ │\
│ │ │ Sync Progress │ │\
│ │ │ ████████████░░░░░░░░ 60% │ │\
│ │ │ Scanning: repo-name/src/models │ │\
│ │ └─────────────────────────────────┘ │\
│ │ │\
│ ▼ │\
│ ⏱ Wait for sync completion (5-30 min depending on size) │\
│ │ │\
│ ▼ │\
│ ▢ Review discovered AI systems │\
│ │ │\
│ ▼ │\
│ ⚠ Notify system owners to review/claim discovered systems │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
◯ END: GitHub Integration Complete

**WORKFLOW A-4: USER ACCESS REVIEW (Quarterly)**

**Trigger:** Quarterly access review schedule\
**Owner:** Administrator\
**SLA:** Complete within 2 weeks of quarter end

◯ START: Quarterly Review Due\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ ADMINISTRATOR │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Export current user list │\
│ │ Settings → Users → Export → CSV │\
│ │ │\
│ ▼ │\
│ ☐ User List CSV │\
│ │ • User name │\
│ │ • Email │\
│ │ • Role │\
│ │ • Last login date │\
│ │ • System assignments │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ ADMINISTRATOR + HR/MANAGERS │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Cross-reference with HR records │\
│ │ │\
│ ▼ │\
│ ◇ Any terminated │\
│ │ employees? │\
│ │ │\
│ ├──YES──► ◈ SUBPROCESS: Deactivate users │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Deactivate each terminated user │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Reassign their action items │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Transfer system ownership if applicable │\
│ │ │ │\
│ │◄────────┘ │\
│ │ │\
│ NO/DONE │\
│ │ │\
│ ▼ │\
│ ▢ Review role appropriateness │\
│ │ │\
│ ▼ │\
│ ◇ Any role │\
│ │ changes needed? │\
│ │ │\
│ ├──YES──► ▢ Update roles │\
│ │ │ • Verify with manager │\
│ │ │ • Document reason │\
│ │ │ │\
│ │◄────────┘ │\
│ │ │\
│ NO/DONE │\
│ │ │\
│ ▼ │\
│ ▢ Identify inactive users │\
│ │ (No login \> 90 days) │\
│ │ │\
│ ▼ │\
│ ◇ Any inactive │\
│ │ users? │\
│ │ │\
│ ├──YES──► ▢ Contact users/managers │\
│ │ │ │\
│ │ ▼ │\
│ │ ◇ Still need │\
│ │ │ access? │\
│ │ │ │\
│ │ ├──NO──► ▢ Deactivate │\
│ │ │ │\
│ │ ├──YES─► ▢ Document justification │\
│ │ │ │\
│ │◄────────┴────────┘ │\
│ │ │\
│ NO/DONE │\
│ │ │\
│ ▼ │\
│ ▢ Review system assignments │\
│ │ • Verify assignments match job duties │\
│ │ • Remove unnecessary access │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ DOCUMENTATION │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Document review findings │\
│ │ • Users reviewed: \[count\] │\
│ │ • Users deactivated: \[count\] │\
│ │ • Roles changed: \[count\] │\
│ │ • Assignments updated: \[count\] │\
│ │ │\
│ ▼ │\
│ ▢ Generate access review report │\
│ │ │\
│ ▼ │\
│ ☐ Access Review Report Q\[X\] 20XX │\
│ │ │\
│ ▼ │\
│ ▢ Store report for audit evidence │\
│ │ │\
│ ▼ │\
│ ▢ Schedule next quarterly review │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
◯ END: Access Review Complete

**WORKFLOW A-5: TROUBLESHOOTING DECISION TREE**

**Trigger:** User reports issue\
**Owner:** Administrator

◯ START: Issue Reported\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ INITIAL TRIAGE │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Gather information │\
│ │ • What is the user trying to do? │\
│ │ • What error message (if any)? │\
│ │ • When did it start? │\
│ │ • Browser/device? │\
│ │ │\
│ ▼ │\
│ ◇ Issue type? │\
│ │ │\
│ ├──LOGIN──────────────────────────────────────────────────────┤\
│ │ │\
│ │ ◇ SSO or Password? │\
│ │ │ │\
│ │ ├──SSO────► ◇ Error message? │\
│ │ │ │ │\
│ │ │ ├─\"Invalid signature\"─► Check IdP cert │\
│ │ │ ├─\"User not found\"────► Check attribute map │\
│ │ │ ├─\"Access denied\"─────► Check IdP assignment │\
│ │ │ └─Other───────────────► Check IdP logs │\
│ │ │ │\
│ │ └──PASSWORD─► ◇ Account status? │\
│ │ │ │\
│ │ ├─Locked──────► Unlock or wait 30 min │\
│ │ ├─Suspended───► Verify with HR, reactivate │\
│ │ ├─Active──────► Reset password │\
│ │ └─Not found───► Provision user │\
│ │ │\
│ ├──ACCESS─────────────────────────────────────────────────────┤\
│ │ │\
│ │ ◇ What can\'t user access? │\
│ │ │ │\
│ │ ├─AI System────► Check system assignments │\
│ │ ├─Feature──────► Check role permissions │\
│ │ ├─Report───────► Check role + data visibility │\
│ │ └─Integration──► Check integration status │\
│ │ │\
│ ├──PERFORMANCE────────────────────────────────────────────────┤\
│ │ │\
│ │ ▢ Check status.phasemirror.com │\
│ │ │ │\
│ │ ◇ Known outage? │\
│ │ │ │\
│ │ ├─YES──► Inform user, monitor status │\
│ │ │ │\
│ │ └─NO───► ◇ Isolated to user? │\
│ │ │ │\
│ │ ├─YES──► Browser cache, try incognito │\
│ │ └─NO───► Escalate to support │\
│ │ │\
│ ├──INTEGRATION────────────────────────────────────────────────┤\
│ │ │\
│ │ ◇ Which integration? │\
│ │ │ │\
│ │ ├─GitHub/GitLab──► Check OAuth token, re-authorize │\
│ │ ├─Jira/ServiceNow► Check API token, verify project │\
│ │ ├─Slack/Teams────► Check bot permissions, channel exists │\
│ │ └─SIEM───────────► Check webhook delivery, credentials │\
│ │ │\
│ └──OTHER──────────────────────────────────────────────────────┤\
│ │\
│ ▢ Document issue details │\
│ │ │\
│ ▼ │\
│ ▢ Search knowledge base │\
│ │ │\
│ ▼ │\
│ ◇ Solution found? │\
│ │ │\
│ ├─YES──► Apply solution │\
│ └─NO───► Escalate to support │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ RESOLUTION │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ◇ Issue resolved? │\
│ │ │\
│ ├──YES──► ▢ Document resolution │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Notify user │\
│ │ │ │\
│ │ ▼ │\
│ │ ◇ Recurring issue? │\
│ │ │ │\
│ │ ├─YES──► ▢ Create knowledge article │\
│ │ │ │\
│ │ └─NO───► ◯ END │\
│ │ │\
│ └──NO───► ▢ Escalate to Phase Mirror Support │\
│ │ • Include all diagnostic info │\
│ │ • Attach screenshots/logs │\
│ │ • Note troubleshooting already attempted │\
│ │ │\
│ ▼ │\
│ ⏱ Track support ticket │\
│ │ │\
│ ▼ │\
│ ▢ Communicate status to user │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
◯ END: Issue Resolved or Escalated

**SECTION 2: GOVERNANCE LEAD WORKFLOWS**

**WORKFLOW G-1: DISSONANCE TRIAGE**

**Trigger:** New dissonance finding generated\
**Owner:** Governance Lead\
**SLA:** Critical = same day, High = 2 days, Medium = 1 week, Low = 2
weeks

◯ START: New Dissonance Alert\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ GOVERNANCE LEAD │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Open dissonance details │\
│ │ • AI system affected │\
│ │ • Rule that triggered │\
│ │ • Severity level │\
│ │ • Finding description │\
│ │ │\
│ ▼ │\
│ ▢ Review supporting evidence │\
│ │ • Current state vs. expected state │\
│ │ • Documentation gaps │\
│ │ • Timeline of changes │\
│ │ │\
│ ▼ │\
│ ◇ Is finding │\
│ │ accurate? │\
│ │ │\
│ ├──NO: FALSE POSITIVE────────────────────────────────────────┤\
│ │ │\
│ │ ◇ Reason for │\
│ │ │ false positive? │\
│ │ │ │\
│ │ ├─Rule doesn\'t apply──► ▢ Consider rule refinement │\
│ │ │ │\
│ │ ├─Data is stale───────► ▢ Trigger data refresh │\
│ │ │ │\
│ │ ├─Already remediated──► ▢ Verify and update status │\
│ │ │ │\
│ │ └─Other───────────────► ▢ Document reason │\
│ │ │ │\
│ │ ▼◄───────────────────────┘ │\
│ │ ▢ Click \"Dismiss\" │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Enter dismissal reason (required) │\
│ │ │ │\
│ │ ▼ │\
│ │ ▣ SYSTEM: Dissonance marked dismissed │\
│ │ │ Audit trail updated │\
│ │ │ │\
│ │ ▼ │\
│ │ ◯ END: Dissonance Dismissed │\
│ │ │\
│ │ │\
│ └──YES: VALID FINDING────────────────────────────────────────┤\
│ │\
│ ▢ Assess severity appropriateness │\
│ │ │\
│ ◇ Severity │\
│ │ correct? │\
│ │ │\
│ ├─NO──► ▢ Adjust severity with justification │\
│ │ │\
│ └─YES/ADJUSTED │\
│ │ │\
│ ▼ │\
│ ▢ Click \"Create Lever\" (action item) │\
│ │ │\
│ ▼ │\
│ ┌─────────────────────────────────┐ │\
│ │ CREATE ACTION ITEM │ │\
│ ├─────────────────────────────────┤ │\
│ │ Title: \[clear description\] │ │\
│ │ Description: \[detailed req\] │ │\
│ │ Owner: \[System Owner or other\] │ │\
│ │ Due Date: \[per severity SLA\] │ │\
│ │ • Critical: +7 days │ │\
│ │ • High: +14 days │ │\
│ │ • Medium: +30 days │ │\
│ │ • Low: +60 days │ │\
│ │ Priority: \[matches severity\] │ │\
│ └─────────────────────────────────┘ │\
│ │ │\
│ ▼ │\
│ ▢ Add remediation guidance │\
│ │ • Specific steps to resolve │\
│ │ • Resources or templates │\
│ │ • Escalation path if blocked │\
│ │ │\
│ ▼ │\
│ ▢ Click \"Save and Notify\" │\
│ │ │\
│ ▼ │\
│ ▣ SYSTEM: Action item created │\
│ │ Owner notified │\
│ │ Dissonance linked │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ CRITICAL SEVERITY PATH │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ◇ Severity = │\
│ │ Critical? │\
│ │ │\
│ ├──YES │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Notify stakeholders immediately │\
│ │ │ • System Owner │\
│ │ │ • System Owner\'s manager │\
│ │ │ • Executive sponsor (if defined) │\
│ │ │ │\
│ │ ▼ │\
│ │ ◇ Immediate risk │\
│ │ │ to customers/business? │\
│ │ │ │\
│ │ ├──YES──► ▢ Recommend interim controls │\
│ │ │ │ • Increased monitoring │\
│ │ │ │ • Human review of outputs │\
│ │ │ │ • Temporary restrictions │\
│ │ │ │ │\
│ │ │ ▼ │\
│ │ │ ▢ Schedule urgent review meeting │\
│ │ │ │\
│ │ └──NO───► Continue to monitoring │\
│ │ │\
│ └──NO (High/Medium/Low) │\
│ │ │\
│ ▼ │\
│ ▢ Add to weekly review agenda │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
◯ END: Dissonance Triaged

**WORKFLOW G-2: AI SYSTEM APPROVAL**

**Trigger:** AI system submitted for approval\
**Owner:** Governance Lead\
**SLA:** Critical/High = 5 business days, Medium/Low = 10 business days

◯ START: Approval Request Received\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ GOVERNANCE LEAD │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Open approval request │\
│ │ Workflows → Pending Approvals → Select request │\
│ │ │\
│ ▼ │\
│ ▢ Review AI system details │\
│ │ │\
│ ▼ │\
│ ┌─────────────────────────────────────────────────────────┐ │\
│ │ APPROVAL CHECKLIST │ │\
│ ├─────────────────────────────────────────────────────────┤ │\
│ │ │ │\
│ │ RISK CLASSIFICATION │ │\
│ │ ☐ Risk tier is appropriate for system type │ │\
│ │ ☐ Customer impact correctly identified │ │\
│ │ ☐ Data sensitivity properly classified │ │\
│ │ │ │\
│ │ DOCUMENTATION │ │\
│ │ ☐ System description is clear and complete │ │\
│ │ ☐ Required documents uploaded per risk tier │ │\
│ │ ☐ Data sources documented │ │\
│ │ ☐ Model/algorithm details provided (if applicable) │ │\
│ │ │ │\
│ │ OWNERSHIP & ACCOUNTABILITY │ │\
│ │ ☐ System owner clearly identified │ │\
│ │ ☐ Owner has appropriate authority │ │\
│ │ ☐ Escalation path defined │ │\
│ │ │ │\
│ │ REGULATORY & COMPLIANCE │ │\
│ │ ☐ Applicable regulations tagged │ │\
│ │ ☐ Compliance requirements acknowledged │ │\
│ │ ☐ No obvious compliance gaps │ │\
│ │ │ │\
│ │ MONITORING (Critical/High only) │ │\
│ │ ☐ Monitoring specification provided │ │\
│ │ ☐ Alerting thresholds defined │ │\
│ │ ☐ Review schedule established │ │\
│ │ │ │\
│ └─────────────────────────────────────────────────────────┘ │\
│ │ │\
│ ▼ │\
│ ◇ All checklist │\
│ │ items satisfied? │\
│ │ │\
│ ├──YES─────────────────────────────────────────────────────────┤\
│ │ │\
│ │ ◇ Any concerns │\
│ │ │ to note? │\
│ │ │ │\
│ │ ├──YES──► ▢ Document concerns in approval comments │\
│ │ │ │\
│ │ └──NO/DONE │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Click \"Approve\" │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Add approval comments (optional) │\
│ │ │ • Conditions for ongoing compliance │\
│ │ │ • Items to monitor │\
│ │ │ • Next review expectations │\
│ │ │ │\
│ │ ▼ │\
│ │ ▣ SYSTEM: System approved │\
│ │ │ Owner notified │\
│ │ │ Audit trail updated │\
│ │ │ │\
│ │ ▼ │\
│ │ ◯ END: System Approved │\
│ │ │\
│ │ │\
│ ├──MOSTLY (Minor gaps)─────────────────────────────────────────┤\
│ │ │\
│ │ ▢ Click \"Approve with Conditions\" │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Specify conditions │\
│ │ │ • What must be completed │\
│ │ │ • Timeline for completion │\
│ │ │ • Verification method │\
│ │ │ │\
│ │ ▼ │\
│ │ ▣ SYSTEM: Conditional approval granted │\
│ │ │ Action items created automatically │\
│ │ │ Owner notified of conditions │\
│ │ │ │\
│ │ ▼ │\
│ │ ◯ END: Conditionally Approved │\
│ │ │\
│ │ │\
│ └──NO (Significant gaps)───────────────────────────────────────┤\
│ │\
│ ◇ Fixable issues │\
│ │ or fundamental problems? │\
│ │ │\
│ ├──FIXABLE │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Click \"Request Changes\" │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Specify required changes │\
│ │ │ • What is missing/incorrect │\
│ │ │ • What needs to be provided │\
│ │ │ • Resources/guidance │\
│ │ │ │\
│ │ ▼ │\
│ │ ▣ SYSTEM: Request returned to owner │\
│ │ │ Changes required notification │\
│ │ │ │\
│ │ ▼ │\
│ │ ◯ END: Changes Requested │\
│ │ │\
│ └──FUNDAMENTAL │\
│ │ │\
│ ▼ │\
│ ▢ Click \"Reject\" │\
│ │ │\
│ ▼ │\
│ ▢ Provide detailed rejection reason │\
│ │ • Why system cannot be approved │\
│ │ • Fundamental concerns │\
│ │ • Path forward (if any) │\
│ │ │\
│ ▼ │\
│ ◇ Escalation │\
│ │ needed? │\
│ │ │\
│ ├──YES──► ▢ Notify exec sponsor/risk committee │\
│ │ │\
│ └──NO │\
│ │ │\
│ ▼ │\
│ ▣ SYSTEM: System rejected │\
│ │ Owner and manager notified │\
│ │ │\
│ ▼ │\
│ ◯ END: System Rejected │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**WORKFLOW G-3: GOVERNANCE RULE CREATION**

**Trigger:** New governance requirement identified\
**Owner:** Governance Lead\
**SLA:** Complete within 1 sprint/2 weeks

◯ START: Governance Requirement Identified\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ GOVERNANCE LEAD │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Document requirement │\
│ │ • Policy/regulation source │\
│ │ • Intended outcome │\
│ │ • Systems affected │\
│ │ │\
│ ▼ │\
│ ◇ Existing rule │\
│ │ can be modified? │\
│ │ │\
│ ├──YES──► ▢ Modify existing rule ──────────────┐ │\
│ │ │ │\
│ └──NO───► ▢ Create new rule │ │\
│ │ │ │\
│ ▼◄────────────────────────────────────┘ │\
│ │\
│ ▢ Navigate to Settings → Governance → Rules │\
│ │ │\
│ ▼ │\
│ ▢ Click \"Add Rule\" (or \"Edit\" for existing) │\
│ │ │\
│ ▼ │\
│ ┌─────────────────────────────────────────────────────────┐ │\
│ │ RULE CONFIGURATION │ │\
│ ├─────────────────────────────────────────────────────────┤ │\
│ │ │ │\
│ │ BASIC INFORMATION │ │\
│ │ ┌────────────────────────────────────────────────────┐ │ │\
│ │ │ Rule Name: \[Descriptive name\] │ │ │\
│ │ │ Description: \[What this rule enforces\] │ │ │\
│ │ │ Category: \[Documentation/Approval/Review/etc.\] │ │ │\
│ │ │ Severity: \[Critical/High/Medium/Low\] │ │ │\
│ │ └────────────────────────────────────────────────────┘ │ │\
│ │ │ │\
│ │ CONDITIONS (When does this rule apply?) │ │\
│ │ ┌────────────────────────────────────────────────────┐ │ │\
│ │ │ IF \[Field\] \[Operator\] \[Value\] │ │ │\
│ │ │ │ │ │\
│ │ │ Examples: │ │ │\
│ │ │ • Risk Tier = Critical │ │ │\
│ │ │ • System Type = LLM │ │ │\
│ │ │ • Regulatory Tag CONTAINS \"HIPAA\" │ │ │\
│ │ │ • Data Sensitivity = High │ │ │\
│ │ │ │ │ │\
│ │ │ \[+ Add Condition\] (AND/OR logic) │ │ │\
│ │ └────────────────────────────────────────────────────┘ │ │\
│ │ │ │\
│ │ ACTIONS (What happens when triggered?) │ │\
│ │ ┌────────────────────────────────────────────────────┐ │ │\
│ │ │ ☐ Require documentation: \[Select doc types\] │ │ │\
│ │ │ ☐ Require approval: \[Select approver role\] │ │ │\
│ │ │ ☐ Create dissonance if: \[condition not met\] │ │ │\
│ │ │ ☐ Send notification to: \[roles/users\] │ │ │\
│ │ │ ☐ Block action until: \[condition met\] │ │ │\
│ │ └────────────────────────────────────────────────────┘ │ │\
│ │ │ │\
│ │ NOTIFICATIONS │ │\
│ │ ┌────────────────────────────────────────────────────┐ │ │\
│ │ │ Notify on trigger: \[System Owner / Gov Lead / etc.\]│ │ │\
│ │ │ Notification channel: \[Email / Slack / Both\] │ │ │\
│ │ └────────────────────────────────────────────────────┘ │ │\
│ │ │ │\
│ └─────────────────────────────────────────────────────────┘ │\
│ │ │\
│ ▼ │\
│ ▢ Save rule (Draft status) │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ TESTING PHASE │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Click \"Test Rule\" │\
│ │ │\
│ ▼ │\
│ ▣ SYSTEM: Rule evaluated against existing systems │\
│ │ │\
│ ▼ │\
│ ▢ Review test results │\
│ │ ┌─────────────────────────────────────────────────────┐ │\
│ │ │ TEST RESULTS │ │\
│ │ ├─────────────────────────────────────────────────────┤ │\
│ │ │ Systems evaluated: 150 │ │\
│ │ │ Systems matching condition: 23 │ │\
│ │ │ Dissonances that would be created: 8 │ │\
│ │ │ │ │\
│ │ │ Sample matches: │ │\
│ │ │ • System A (Critical, LLM) ✓ │ │\
│ │ │ • System B (High, ML Model) ✓ │ │\
│ │ │ • System C (Medium, Rules) ✗ (not intended) │ │\
│ │ └─────────────────────────────────────────────────────┘ │\
│ │ │\
│ ▼ │\
│ ◇ Results as │\
│ │ expected? │\
│ │ │\
│ ├──NO──► ▢ Refine conditions ──► Return to configuration │\
│ │ │\
│ └──YES │\
│ │ │\
│ ▼ │\
│ ◇ Ready to │\
│ │ activate? │\
│ │ │\
│ ├──NO──► ▢ Save as draft for later ──► ◯ END (Draft) │\
│ │ │\
│ └──YES │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ ACTIVATION │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Click \"Activate Rule\" │\
│ │ │\
│ ▼ │\
│ ◇ Run against │\
│ │ existing systems now? │\
│ │ │\
│ ├──YES──► ▣ SYSTEM: Dissonances created for existing gaps │\
│ │ │\
│ └──NO───► ▣ SYSTEM: Rule active for future only │\
│ (no retroactive dissonances) │\
│ │ │\
│ ▼ │\
│ ▢ Communicate rule to affected users │\
│ │ • What the rule requires │\
│ │ • Why it was implemented │\
│ │ • Timeline for compliance │\
│ │ │\
│ ▼ │\
│ ▢ Document rule in governance procedures │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
◯ END: Rule Active

**WORKFLOW G-4: COMPLIANCE REPORTING**

**Trigger:** Scheduled report due or ad-hoc request\
**Owner:** Governance Lead\
**SLA:** Scheduled = per calendar, Ad-hoc = 3 business days

◯ START: Report Needed\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ GOVERNANCE LEAD │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ◇ Report type? │\
│ │ │\
│ ├──EXECUTIVE SUMMARY─────────────────────────────────────────┤\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Navigate to Reports → New → Executive Summary │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Configure report │\
│ │ │ • Reporting period │\
│ │ │ • Sections to include: │\
│ │ │ ☑ AI System Overview │\
│ │ │ ☑ Governance Health Score │\
│ │ │ ☑ Key Dissonances │\
│ │ │ ☑ Regulatory Status │\
│ │ │ ☐ Detailed Metrics │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Click \"Generate\" │\
│ │ │ │\
│ │ ▼ │\
│ │ ⏱ Wait for generation (1-5 min) │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Review and edit narrative sections │\
│ │ │ • Add context │\
│ │ │ • Highlight key messages │\
│ │ │ • Note action items │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Export (PDF/PowerPoint) │\
│ │ │\
│ │ │\
│ ├──COMPLIANCE STATUS───────────────────────────────────────────┤\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Navigate to Reports → New → Compliance Status │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Select compliance framework │\
│ │ │ • EU AI Act │\
│ │ │ • SR 11-7 │\
│ │ │ • HIPAA │\
│ │ │ • Custom │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Select systems to include │\
│ │ │ • All systems │\
│ │ │ • Specific risk tier │\
│ │ │ • Specific business unit │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Click \"Generate\" │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Review compliance gaps │\
│ │ │ │\
│ │ ▼ │\
│ │ ◇ Gaps identified? │\
│ │ │ │\
│ │ ├──YES──► ▢ Create action items for gaps │\
│ │ │ │\
│ │ └──NO/DONE │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Export report │\
│ │ │\
│ │ │\
│ └──AUDIT PACKAGE───────────────────────────────────────────────┤\
│ │ │\
│ ▼ │\
│ ▢ Navigate to Reports → New → Audit Package │\
│ │ │\
│ ▼ │\
│ ▢ Select AI system(s) │\
│ │ │\
│ ▼ │\
│ ▢ Select documentation types │\
│ │ ☑ System registration │\
│ │ ☑ Governance documentation │\
│ │ ☑ Dissonance history │\
│ │ ☑ Action item history │\
│ │ ☑ Approval records │\
│ │ ☑ Audit trail │\
│ │ │\
│ ▼ │\
│ ▢ Select date range │\
│ │ │\
│ ▼ │\
│ ▢ Click \"Generate Package\" │\
│ │ │\
│ ▼ │\
│ ⏱ Wait for compilation (5-15 min) │\
│ │ │\
│ ▼ │\
│ ▢ Download ZIP package │\
│ │ │\
│ ▼ │\
│ ▢ Review package completeness │\
│ │ │\
│ ▼ │\
│ ▢ Provide to auditor/examiner │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ DISTRIBUTION │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Identify recipients │\
│ │ │\
│ ▼ │\
│ ◇ Presentation │\
│ │ required? │\
│ │ │\
│ ├──YES──► ▢ Schedule meeting │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Present findings and recommendations │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Document questions and action items │\
│ │ │\
│ └──NO───► ▢ Distribute via email with summary │\
│ │\
│ │ │\
│ ▼ │\
│ ▢ Store report in document repository │\
│ │ │\
│ ▼ │\
│ ▢ Update reporting log │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
◯ END: Report Delivered

**SECTION 3: SYSTEM OWNER WORKFLOWS**

**WORKFLOW S-1: AI SYSTEM REGISTRATION**

**Trigger:** New AI system to be governed\
**Owner:** System Owner\
**SLA:** Complete before production deployment

◯ START: New AI System Identified\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ SYSTEM OWNER │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Gather system information │\
│ │ • System name and purpose │\
│ │ • Technical architecture │\
│ │ • Data sources and flows │\
│ │ • Business context │\
│ │ │\
│ ▼ │\
│ ▢ Navigate to AI Systems → Add System │\
│ │ │\
│ ▼ │\
│ ┌─────────────────────────────────────────────────────────┐ │\
│ │ REGISTRATION FORM │ │\
│ ├─────────────────────────────────────────────────────────┤ │\
│ │ │ │\
│ │ BASIC INFORMATION (\* = required) │ │\
│ │ ┌────────────────────────────────────────────────────┐ │ │\
│ │ │ \*System Name:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ │ │ │\
│ │ │ \*Description:
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ │ │ │\
│ │ │ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ │
│ │\
│ │ │ \*System Type: \[ML Model ▼\] │ │ │\
│ │ │ • ML Model │ │ │\
│ │ │ • LLM / Foundation Model │ │ │\
│ │ │ • LLM Application │ │ │\
│ │ │ • Agentic System │ │ │\
│ │ │ • Rules-Based AI │ │ │\
│ │ │ • Hybrid │ │ │\
│ │ │ \*Status: \[Development ▼\] │ │ │\
│ │ │ • Development │ │ │\
│ │ │ • Testing │ │ │\
│ │ │ • Production │ │ │\
│ │ │ • Deprecated │ │ │\
│ │ └────────────────────────────────────────────────────┘ │ │\
│ │ │ │\
│ │ OWNERSHIP │ │\
│ │ ┌────────────────────────────────────────────────────┐ │ │\
│ │ │ \*Owner: \[You - auto-filled\] │ │ │\
│ │ │ Business Unit: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ │ │ │\
│ │ │ Executive Sponsor: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ │ │ │\
│ │ │ Technical Lead: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ │ │ │\
│ │ └────────────────────────────────────────────────────┘ │ │\
│ │ │ │\
│ │ RISK CLASSIFICATION │ │\
│ │ ┌────────────────────────────────────────────────────┐ │ │\
│ │ │ \*Risk Tier: \[Select ▼\] │ │ │\
│ │ │ Use classification guide → │ │ │\
│ │ │ │ │ │\
│ │ │ Customer Impact: │ │ │\
│ │ │ ○ Direct (makes decisions about customers) │ │ │\
│ │ │ ○ Indirect (influences customer-facing systems) │ │ │\
│ │ │ ○ None (internal only) │ │ │\
│ │ │ │ │ │\
│ │ │ Decision Type: │ │ │\
│ │ │ ○ Autonomous (no human in loop) │ │ │\
│ │ │ ○ Assisted (human makes final decision) │ │ │\
│ │ │ ○ Advisory (provides recommendations only) │ │ │\
│ │ └────────────────────────────────────────────────────┘ │ │\
│ │ │ │\
│ │ DATA │ │\
│ │ ┌────────────────────────────────────────────────────┐ │ │\
│ │ │ Data Sensitivity: \[Select ▼\] │ │ │\
│ │ │ • Public │ │ │\
│ │ │ • Internal │ │ │\
│ │ │ • Confidential │ │ │\
│ │ │ • Restricted/PII │ │ │\
│ │ │ │ │ │\
│ │ │ Data Sources: │ │ │\
│ │ │ \[+ Add data source\] │ │ │\
│ │ │ │ │ │\
│ │ │ Contains PII: ○ Yes ○ No │ │ │\
│ │ │ Contains PHI: ○ Yes ○ No │ │ │\
│ │ └────────────────────────────────────────────────────┘ │ │\
│ │ │ │\
│ │ REGULATORY │ │\
│ │ ┌────────────────────────────────────────────────────┐ │ │\
│ │ │ Applicable Regulations (select all that apply): │ │ │\
│ │ │ ☐ EU AI Act │ │ │\
│ │ │ ☐ GDPR │ │ │\
│ │ │ ☐ SR 11-7 / Model Risk │ │ │\
│ │ │ ☐ Fair Lending │ │ │\
│ │ │ ☐ HIPAA │ │ │\
│ │ │ ☐ FDA │ │ │\
│ │ │ ☐ Other: \_\_\_\_\_\_\_\_\_\_\_\_\_\_ │ │ │\
│ │ └────────────────────────────────────────────────────┘ │ │\
│ │ │ │\
│ │ TECHNICAL │ │\
│ │ ┌────────────────────────────────────────────────────┐ │ │\
│ │ │ Source Repository: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ │
│ │\
│ │ │ Deployment Environment: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ │ │
│\
│ │ │ Model Framework: \[TensorFlow ▼\] │ │ │\
│ │ │ Vendor (if external): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ │ │
│\
│ │ └────────────────────────────────────────────────────┘ │ │\
│ │ │ │\
│ └─────────────────────────────────────────────────────────┘ │\
│ │ │\
│ ▼ │\
│ ▢ Click \"Save as Draft\" to continue later │\
│ │ OR │\
│ ▢ Click \"Continue to Documentation\" │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ DOCUMENTATION │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▣ SYSTEM: Required documents shown based on risk tier │\
│ │ │\
│ │ ┌─────────────────────────────────────────────────────┐ │\
│ │ │ REQUIRED DOCUMENTS │ │\
│ │ │ │ │\
│ │ │ For Critical Risk: │ │\
│ │ │ ☐ System Design Document │ │\
│ │ │ ☐ Model Card / Algorithm Specification │ │\
│ │ │ ☐ Data Dictionary │ │\
│ │ │ ☐ Validation Report │ │\
│ │ │ ☐ Monitoring Specification │ │\
│ │ │ ☐ Bias Assessment (if customer-facing) │ │\
│ │ │ │ │\
│ │ │ Optional Documents: │ │\
│ │ │ ☐ User Guide │ │\
│ │ │ ☐ API Documentation │ │\
│ │ │ ☐ Change Log │ │\
│ │ └─────────────────────────────────────────────────────┘ │\
│ │ │\
│ ▼ │\
│ ▢ Upload each required document │\
│ │ • Click document type │\
│ │ • Upload file or link to URL │\
│ │ • Add description/notes │\
│ │ │\
│ ▼ │\
│ ◇ All required │\
│ │ documents uploaded? │\
│ │ │\
│ ├──NO──► ◇ Can upload now? │\
│ │ │ │\
│ │ ├──YES──► Continue uploading │\
│ │ │ │\
│ │ └──NO───► ▢ Create action items for missing docs │\
│ │ │ (can proceed with registration) │\
│ │ │ │\
│ │◄─────────────────┘ │\
│ │ │\
│ YES │\
│ │ │\
│ ▼ │\
│ ▢ Click \"Submit for Registration\" │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ APPROVAL ROUTING │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▣ SYSTEM: Route based on risk tier │\
│ │ │\
│ ◇ Risk tier? │\
│ │ │\
│ ├──CRITICAL/HIGH │\
│ │ │ │\
│ │ ▼ │\
│ │ ▣ SYSTEM: Submit to Governance Lead approval queue │\
│ │ │ │\
│ │ ▼ │\
│ │ ⚠ Governance Lead notified │\
│ │ │ │\
│ │ ▼ │\
│ │ ⏱ WAIT: Pending approval │\
│ │ │ │\
│ │ ▼ │\
│ │ ◇ Approval │\
│ │ │ decision? │\
│ │ │ │\
│ │ ├──APPROVED──────────► Registration complete ──► ◯ END │\
│ │ │ │\
│ │ ├──CONDITIONAL───────► ▢ Address conditions │\
│ │ │ │ │\
│ │ │ ▼ │\
│ │ │ ▢ Resubmit when complete │\
│ │ │ │ │\
│ │ │◄──────────────────────┘ │\
│ │ │ │\
│ │ ├──CHANGES REQUESTED──► ▢ Make requested changes │\
│ │ │ │ │\
│ │ │ ▼ │\
│ │ │ ▢ Resubmit │\
│ │ │ │ │\
│ │ │◄──────────────────────┘ │\
│ │ │ │\
│ │ └──REJECTED──────────► ▢ Review rejection reason │\
│ │ │ │\
│ │ ▼ │\
│ │ ◇ Path forward? │\
│ │ │ │\
│ │ ├─YES─► Address and resubmit │\
│ │ └─NO──► ◯ END (Not registered) │\
│ │ │\
│ └──MEDIUM/LOW │\
│ │ │\
│ ▼ │\
│ ▣ SYSTEM: Auto-approved (or per org config) │\
│ │ │\
│ ▼ │\
│ ◯ END: Registration Complete │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**WORKFLOW S-2: RESPONDING TO DISSONANCE**

**Trigger:** Dissonance finding notification received\
**Owner:** System Owner\
**SLA:** Per dissonance severity

◯ START: Dissonance Notification Received\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ SYSTEM OWNER │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Open dissonance notification │\
│ │ (Email link or Dissonance → My Findings) │\
│ │ │\
│ ▼ │\
│ ▢ Review finding details │\
│ │ • What rule was triggered │\
│ │ • What gap was identified │\
│ │ • Severity level │\
│ │ • Evidence/details │\
│ │ │\
│ ▼ │\
│ ◇ Is finding │\
│ │ accurate? │\
│ │ │\
│ ├──NO: DISPUTE────────────────────────────────────────────────┤\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Click \"Dispute Finding\" │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Provide evidence/explanation │\
│ │ │ • Why finding is incorrect │\
│ │ │ • Evidence (screenshots, links, docs) │\
│ │ │ • Compensating controls if applicable │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Submit dispute │\
│ │ │ │\
│ │ ▼ │\
│ │ ⚠ Governance Lead notified of dispute │\
│ │ │ │\
│ │ ▼ │\
│ │ ⏱ WAIT: Dispute review │\
│ │ │ │\
│ │ ▼ │\
│ │ ◇ Dispute │\
│ │ │ outcome? │\
│ │ │ │\
│ │ ├─UPHELD (you win)──► Dissonance dismissed ──► ◯ END │\
│ │ │ │\
│ │ └─DENIED─────────────► Continue to remediation │\
│ │ │ │\
│ │◄─────────────────────────┘ │\
│ │ │\
│ └──YES: VALID─────────────────────────────────────────────────┤\
│ │ │\
│ ▼ │\
│ ◇ Action item │\
│ │ already created? │\
│ │ │\
│ ├──YES──► Go to action item │\
│ │ │\
│ └──NO │\
│ │ │\
│ ▼ │\
│ ▢ Click \"Accept & Create Action\" │\
│ │ │\
│ ▼ │\
│ ▢ Define action item │\
│ │ • Title: Clear description of fix │\
│ │ • Steps: What needs to be done │\
│ │ • Owner: You or delegate │\
│ │ • Due date: Per severity SLA │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ REMEDIATION │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Perform remediation work │\
│ │ │\
│ │ COMMON REMEDIATION TYPES: │\
│ │ ┌─────────────────────────────────────────────────────┐ │\
│ │ │ Documentation Gap │ │\
│ │ │ → Update/create required documentation │ │\
│ │ │ → Upload to Phase Mirror │ │\
│ │ │ │ │\
│ │ │ Stale Documentation │ │\
│ │ │ → Review current system state │ │\
│ │ │ → Update documentation to reflect reality │ │\
│ │ │ → Upload new version │ │\
│ │ │ │ │\
│ │ │ Missing Monitoring │ │\
│ │ │ → Design monitoring specification │ │\
│ │ │ → Implement monitoring │ │\
│ │ │ → Upload specification document │ │\
│ │ │ │ │\
│ │ │ Approval Gap │ │\
│ │ │ → Gather required approvals │ │\
│ │ │ → Document approval chain │ │\
│ │ │ │ │\
│ │ │ Policy Violation │ │\
│ │ │ → Modify system to comply │ │\
│ │ │ → OR request exception with justification │ │\
│ │ └─────────────────────────────────────────────────────┘ │\
│ │ │\
│ ▼ │\
│ ◇ Remediation │\
│ │ complete? │\
│ │ │\
│ ├──NO │\
│ │ │ │\
│ │ ◇ Blocked? │\
│ │ │ │\
│ │ ├──YES──► ▢ Add comment explaining blocker │\
│ │ │ │ │\
│ │ │ ▼ │\
│ │ │ ▢ Escalate if needed │\
│ │ │ │ │\
│ │ │ ▼ │\
│ │ │ ▢ Request due date extension if justified │\
│ │ │ │\
│ │ └──NO───► Continue working │\
│ │ │\
│ └──YES │\
│ │ │\
│ ▼ │\
│ ▢ Upload evidence of completion │\
│ │ • Updated documents │\
│ │ • Screenshots │\
│ │ • Links to changes │\
│ │ │\
│ ▼ │\
│ ▢ Add completion comment │\
│ │ │\
│ ▼ │\
│ ▢ Click \"Mark Complete\" │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ VERIFICATION │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▣ SYSTEM: Trigger re-analysis │\
│ │ │\
│ ▼ │\
│ ◇ Dissonance │\
│ │ resolved? │\
│ │ │\
│ ├──YES │\
│ │ │ │\
│ │ ▼ │\
│ │ ▣ SYSTEM: Dissonance marked resolved │\
│ │ │ Action item closed │\
│ │ │ │\
│ │ ▼ │\
│ │ ◯ END: Dissonance Resolved │\
│ │ │\
│ └──NO │\
│ │ │\
│ ▼ │\
│ ▢ Review what\'s still missing │\
│ │ │\
│ ▼ │\
│ ▢ Complete additional remediation │\
│ │ │\
│ └──► Return to remediation step │\
│ │\
└─────────────────────────────────────────────────────────────────┘

**WORKFLOW S-3: PERIODIC REVIEW**

**Trigger:** Periodic review due notification\
**Owner:** System Owner\
**SLA:** Complete by due date

◯ START: Periodic Review Due\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ SYSTEM OWNER │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Navigate to AI System → Reviews │\
│ │ │\
│ ▼ │\
│ ▢ Click \"Start Review\" │\
│ │ │\
│ ▼ │\
│ ┌─────────────────────────────────────────────────────────┐ │\
│ │ PERIODIC REVIEW CHECKLIST │ │\
│ ├─────────────────────────────────────────────────────────┤ │\
│ │ │ │\
│ │ SECTION 1: SYSTEM STATUS │ │\
│ │ ┌────────────────────────────────────────────────────┐ │ │\
│ │ │ Is the system still active? ○ Yes ○ No │ │ │\
│ │ │ Any changes since last review? ○ Yes ○ No │ │ │\
│ │ │ Current deployment status: \[Production ▼\] │ │ │\
│ │ │ System performing as expected? ○ Yes ○ No │ │ │\
│ │ └────────────────────────────────────────────────────┘ │ │\
│ │ │ │\
│ │ SECTION 2: DOCUMENTATION CURRENCY │ │\
│ │ ┌────────────────────────────────────────────────────┐ │ │\
│ │ │ Current Needs Update │ │ │\
│ │ │ System Design ☐ ☐ │ │ │\
│ │ │ Model Card ☐ ☐ │ │ │\
│ │ │ Data Dictionary ☐ ☐ │ │ │\
│ │ │ Validation Report ☐ ☐ │ │ │\
│ │ │ Monitoring Spec ☐ ☐ │ │ │\
│ │ └────────────────────────────────────────────────────┘ │ │\
│ │ │ │\
│ │ SECTION 3: RISK ASSESSMENT │ │\
│ │ ┌────────────────────────────────────────────────────┐ │ │\
│ │ │ Risk tier still appropriate? ○ Yes ○ No │ │ │\
│ │ │ New risks identified? ○ Yes ○ No │ │ │\
│ │ │ Customer impact changed? ○ Yes ○ No │ │ │\
│ │ │ Regulatory changes affecting system? ○ Yes ○ No │ │ │\
│ │ │ │ │ │\
│ │ │ If any \"Yes\": Describe changes below │ │ │\
│ │ │
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│ │ │\
│ │ └────────────────────────────────────────────────────┘ │ │\
│ │ │ │\
│ │ SECTION 4: PERFORMANCE & INCIDENTS │ │\
│ │ ┌────────────────────────────────────────────────────┐ │ │\
│ │ │ Any incidents since last review? ○ Yes ○ No │ │ │\
│ │ │ Performance metrics within thresholds? ○ Yes ○ No │ │ │\
│ │ │ Any bias/fairness concerns? ○ Yes ○ No │ │ │\
│ │ │ Customer complaints? ○ Yes ○ No │ │ │\
│ │ │ │ │ │\
│ │ │ If any \"Yes\": Describe and actions taken │ │ │\
│ │ │
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│ │ │\
│ │ └────────────────────────────────────────────────────┘ │ │\
│ │ │ │\
│ │ SECTION 5: OWNERSHIP & RESOURCES │ │\
│ │ ┌────────────────────────────────────────────────────┐ │ │\
│ │ │ Owner still appropriate? ○ Yes ○ No │ │ │\
│ │ │ Team adequately resourced? ○ Yes ○ No │ │ │\
│ │ │ Training needs identified? ○ Yes ○ No │ │ │\
│ │ └────────────────────────────────────────────────────┘ │ │\
│ │ │ │\
│ │ SECTION 6: ACTION ITEMS │ │\
│ │ ┌────────────────────────────────────────────────────┐ │ │\
│ │ │ Action items from review: │ │ │\
│ │ │ \[+ Add Action Item\] │ │ │\
│ │ │ │ │ │\
│ │ │ 1. Update model card with recent changes │ │ │\
│ │ │ Due: \[date\] Owner: \[name\] │ │ │\
│ │ │ │ │ │\
│ │ │ 2.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
│ │ │\
│ │ └────────────────────────────────────────────────────┘ │ │\
│ │ │ │\
│ │ ATTESTATION │ │\
│ │ ┌────────────────────────────────────────────────────┐ │ │\
│ │ │ ☐ I confirm this review is accurate and complete │ │ │\
│ │ │ │ │ │\
│ │ │ Reviewer: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date:
\_\_\_\_\_\_\_\_\_\_ │ │ │\
│ │ └────────────────────────────────────────────────────┘ │ │\
│ │ │ │\
│ └─────────────────────────────────────────────────────────┘ │\
│ │ │\
│ ▼ │\
│ ◇ Any items marked │\
│ │ \"Needs Update\" or \"Yes\" issues? │\
│ │ │\
│ ├──YES │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Create action items for each issue │\
│ │ │ │\
│ │ ▼ │\
│ │ ▢ Assign owners and due dates │\
│ │ │\
│ └──NO/DONE │\
│ │ │\
│ ▼ │\
│ ▢ Click \"Submit Review\" │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ REVIEW ROUTING │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ◇ Risk tier? │\
│ │ │\
│ ├──CRITICAL │\
│ │ │ │\
│ │ ▼ │\
│ │ ▣ SYSTEM: Route to Governance Lead for review │\
│ │ │ │\
│ │ ▼ │\
│ │ ⏱ WAIT: Governance approval │\
│ │ │ │\
│ │ ▼ │\
│ │ ◇ Approved? │\
│ │ │ │\
│ │ ├─YES──► Review complete │\
│ │ └─NO───► Address feedback and resubmit │\
│ │ │\
│ └──HIGH/MEDIUM/LOW │\
│ │ │\
│ ▼ │\
│ ▣ SYSTEM: Review recorded │\
│ │ Next review scheduled │\
│ │\
└─────────────────────────────────────────────────────────────────┘\
│\
▼\
◯ END: Periodic Review Complete

**WORKFLOW S-4: OWNERSHIP TRANSFER**

**Trigger:** Owner leaving role or team\
**Owner:** Current System Owner + New Owner\
**SLA:** Complete before current owner departs

◯ START: Ownership Change Needed\
│\
▼\
┌─────────────────────────────────────────────────────────────────┐\
│ CURRENT SYSTEM OWNER │\
├─────────────────────────────────────────────────────────────────┤\
│ │\
│ ▢ Identify new owner │\
│ │ • Must have System Owner role │\
│ │ • Must have appropriate authority │\
│ │ • Manager approval recommended │\
│ │ │\
│ ▼ │\
│ ▢ Navigate to AI System → Settings → Transfer Ownership │\
│ │ │\
│ ▼ │\
│ ▢ Select new owner from\
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

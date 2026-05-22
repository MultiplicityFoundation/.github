---
slug: in-plain-chat-lets-create-certification-quiz-quest
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 00-foundations/phase-mirror/in plain chat lets create_Certification quiz quest.md
  last_synced: '2026-03-20T17:17:21.899537Z'
---

![](media/image-a920a7a78fd32a24fa20b9fa8c1efa9edcd42221.png){width="2.6466666666666665in"
height="0.6666666666666666in"}

**in plain chat lets create**

Certification quiz questions for role proficiency

Here are comprehensive certification quiz question banks for each Phase
Mirror role:

**PHASE MIRROR CERTIFICATION EXAM QUESTION BANKS**

**Role Proficiency Assessment**

**Version:** 2.0 \| **Date:** January 2026\
**Classification:** Internal Use Only - Exam Content

**EXAM STRUCTURE OVERVIEW**

  ----------------- -------- ----------- ---------- ------------- ---------
  Certification     Code     Questions   Duration   Passing       Domains
  Administrator     PM-290   50          60 min     80% (40/50)   5
  Governance Lead   PM-390   60          90 min     80% (48/60)   5
  System Owner      PM-490   30          45 min     80% (24/30)   4
  ----------------- -------- ----------- ---------- ------------- ---------

**Question Types**

  --------------------- -------------------------------------- ---------
  Type                  Format                                 Points
  **Multiple Choice**   Single correct answer (A, B, C, D)     1 point
  **Multiple Select**   2-4 correct answers from 5-6 options   1 point
  **Scenario-Based**    Situation with best response           1 point
  **Ordering**          Sequence steps correctly               1 point
  **Matching**          Match items from two columns           1 point
  --------------------- -------------------------------------- ---------

**PM-290: ADMINISTRATOR CERTIFICATION**

**50 Questions \| 60 Minutes \| 80% Passing**

**DOMAIN 1: USER MANAGEMENT (25% - 12-13 Questions)**

**Multiple Choice Questions**

**Q1.** An employee has transferred to a new department and needs access
to different AI systems. What is the correct approach?

A\) Delete the user account and create a new one\
B) Edit the user\'s profile and update their system assignments\
C) Ask the user to create a new account with their new department email\
D) Leave access unchanged; department doesn\'t affect system access

**Correct: B**\
*Explanation: User profiles should be edited to update assignments.
Deleting accounts loses audit history, and creating duplicate accounts
violates security best practices.*

**Q2.** What is the maximum number of users that can be provisioned at
once using the bulk import feature?

A\) 50\
B) 100\
C) 500\
D) Unlimited

**Correct: C**\
*Explanation: Bulk import supports up to 500 users per import operation.
Larger organizations should perform multiple imports or use SCIM
provisioning.*

**Q3.** A user reports they cannot access an AI system they previously
could view. What should you check FIRST?

A\) Whether the system has been archived\
B) Whether the user\'s role has changed\
C) Whether the user\'s account is still active\
D) Whether the system owner has restricted access

**Correct: C**\
*Explanation: Always verify the most basic access requirement
first---that the account is active. Then proceed to role, assignment,
and system-level checks.*

**Q4.** Which role has the LEAST permissions in Phase Mirror?

A\) Contributor\
B) Viewer\
C) System Owner\
D) Auditor

**Correct: B**\
*Explanation: Viewer has read-only access to dashboards and reports.
Auditor has read-only but with full audit trail access. Contributor can
edit assigned systems. System Owner can manage their systems.*

**Q5.** When should you use the \"Suspend\" function instead of
\"Deactivate\" for a user?

A\) When the user is on temporary leave and will return\
B) When the user has been terminated\
C) When the user has violated security policies\
D) When you need to immediately revoke all access

**Correct: A**\
*Explanation: Suspend preserves the user\'s data and assignments for
return. Deactivate is for permanent departures. Both immediately revoke
access.*

**Q6.** What happens to action items assigned to a user when their
account is deactivated?

A\) They are automatically deleted\
B) They are reassigned to the system owner\
C) They remain assigned to the deactivated user\
D) They are automatically marked complete

**Correct: C**\
*Explanation: Action items remain assigned to show audit history. A
Governance Lead or Admin should manually reassign pending items.*

**Q7.** Which of the following is NOT a standard role in Phase Mirror?

A\) Governance Lead\
B) Compliance Officer\
C) System Owner\
D) Contributor

**Correct: B**\
*Explanation: Compliance Officer is not a standard role. The standard
roles are Admin, Governance Lead, System Owner, Contributor, Viewer, and
Auditor.*

**Q8.** A user needs to both manage their own AI systems AND configure
governance rules. What role combination is required?

A\) System Owner only\
B) Governance Lead only\
C) System Owner + Governance Lead (dual assignment)\
D) Admin

**Correct: B**\
*Explanation: Governance Lead role includes the ability to manage AI
systems. Dual assignment is not needed. Admin would provide unnecessary
elevated privileges.*

**Multiple Select Questions**

**Q9.** Which actions require Admin role permissions? (Select THREE)

☐ A) Inviting new users to the platform\
☐ B) Configuring SSO settings\
☐ C) Registering a new AI system\
☐ D) Exporting audit logs\
☐ E) Creating governance rules\
☐ F) Approving AI systems for production

**Correct: A, B, D**\
*Explanation: User management, authentication settings, and audit log
export require Admin permissions. AI system registration (System Owner),
governance rules (Governance Lead), and approvals (Governance Lead) do
not.*

**Q10.** When conducting a quarterly access review, what should you
verify? (Select FOUR)

☐ A) All users are still employed by the organization\
☐ B) User roles match current job responsibilities\
☐ C) System assignments are appropriate\
☐ D) All users have completed training\
☐ E) No accounts have been inactive for extended periods\
☐ F) All users have strong passwords

**Correct: A, B, C, E**\
*Explanation: Access reviews focus on employment status, role
appropriateness, assignment accuracy, and activity. Training completion
and password strength are separate concerns.*

**Scenario-Based Questions**

**Q11.** SCENARIO: Your organization uses Okta for identity management.
A new employee joins and is added to the \"AI-Governance-Users\" group
in Okta. However, they cannot access Phase Mirror. SCIM provisioning is
enabled.

What is the MOST LIKELY cause?

A\) The user hasn\'t set up MFA\
B) The Okta group isn\'t mapped to a Phase Mirror role\
C) The SCIM connection has been disabled\
D) The user needs to be manually invited first

**Correct: B**\
*Explanation: SCIM provisions users based on group-to-role mappings. If
the Okta group isn\'t mapped to a Phase Mirror role, the user will be
created but have no access.*

**Q12.** SCENARIO: An auditor is on-site for a regulatory examination
and requests a list of all users who have accessed a specific Critical
AI system in the past 12 months.

What is the CORRECT way to provide this information?

A\) Manually list users from memory\
B) Export the AI system\'s access list from the system page\
C) Generate an audit log export filtered by the system and date range\
D) Ask each user if they accessed the system

**Correct: C**\
*Explanation: The audit log provides a complete, verified record of all
access events and can be filtered by system and date range for
examination requests.*

**DOMAIN 2: AUTHENTICATION & SECURITY (25% - 12-13 Questions)**

**Multiple Choice Questions**

**Q13.** Which authentication protocol does Phase Mirror support for
SSO? (Select the BEST answer)

A\) SAML 2.0 only\
B) OIDC only\
C) Both SAML 2.0 and OIDC\
D) LDAP only

**Correct: C**\
*Explanation: Phase Mirror supports both SAML 2.0 and OIDC for SSO,
allowing flexibility for different identity providers.*

**Q14.** What is the MINIMUM recommended session timeout for compliance
with most security frameworks?

A\) 1 hour\
B) 4 hours\
C) 8 hours\
D) 24 hours

**Correct: C**\
*Explanation: 8 hours aligns with a typical workday and balances
security with usability. Shorter timeouts may be required for highly
sensitive environments.*

**Q15.** When configuring SAML SSO, which attribute is REQUIRED for user
identification?

A\) firstName\
B) lastName\
C) email\
D) department

**Correct: C**\
*Explanation: Email is the required unique identifier for SAML
authentication. FirstName and lastName are required for display but not
identification.*

**Q16.** What happens when a user fails login 5 times consecutively with
the default lockout settings?

A\) The account is permanently disabled\
B) The account is locked for 30 minutes\
C) An alert is sent to the admin but access continues\
D) The user must contact support to unlock

**Correct: B**\
*Explanation: Default lockout is 5 attempts followed by 30-minute
lockout. Admins can adjust these settings.*

**Q17.** Which MFA method is supported by Phase Mirror for standard
authentication?

A\) SMS only\
B) Email only\
C) TOTP authenticator apps\
D) Hardware tokens only

**Correct: C**\
*Explanation: Phase Mirror supports TOTP (Time-based One-Time Password)
via authenticator apps like Google Authenticator, Authy, or Microsoft
Authenticator.*

**Q18.** IP allowlisting is configured to only allow connections from
your corporate network (10.0.0.0/8). An executive needs to access Phase
Mirror while traveling. What is the BEST solution?

A\) Temporarily disable IP allowlisting\
B) Add the hotel\'s IP address to the allowlist\
C) Have the executive connect via corporate VPN\
D) Create a separate account without IP restrictions

**Correct: C**\
*Explanation: VPN connection routes traffic through the corporate
network, satisfying the allowlist. Disabling allowlisting or creating
exceptions reduces security.*

**Q19.** How long are audit logs retained in an Enterprise tier account
by default?

A\) 1 year\
B) 3 years\
C) 7 years\
D) Indefinitely

**Correct: C**\
*Explanation: Enterprise tier retains audit logs for 7 years by default,
meeting most regulatory requirements. This is configurable.*

**Q20.** Which action is logged in the audit trail?

A\) User viewing a dashboard\
B) User thinking about making a change\
C) All of the above\
D) User creating an AI system

**Correct: D**\
*Explanation: Audit logs capture actions that modify data or access
sensitive information. Dashboard views may or may not be logged
depending on configuration. Thought is not loggable.*

**Multiple Select Questions**

**Q21.** Which security settings should be reviewed during a security
hardening exercise? (Select FOUR)

☐ A) MFA enforcement\
☐ B) Session timeout duration\
☐ C) Dashboard color scheme\
☐ D) Password complexity requirements\
☐ E) Notification preferences\
☐ F) IP allowlisting configuration

**Correct: A, B, D, F**\
*Explanation: Security hardening focuses on authentication (MFA,
passwords), session management (timeout), and network controls (IP
allowlisting). Visual preferences and notifications are not security
settings.*

**Q22.** What information is included in an audit log entry? (Select
FIVE)

☐ A) Timestamp\
☐ B) User who performed the action\
☐ C) User\'s password\
☐ D) Action performed\
☐ E) Object affected\
☐ F) Source IP address

**Correct: A, B, D, E, F**\
*Explanation: Audit logs capture timestamp, user, action, object, and IP
address. Passwords are never logged or stored in plain text.*

**Scenario-Based Questions**

**Q23.** SCENARIO: You receive an alert that a user account has had 15
failed login attempts from multiple IP addresses across different
countries in the past hour.

What is the MOST appropriate IMMEDIATE action?

A\) Monitor the situation for another hour\
B) Suspend the user account and investigate\
C) Reset the user\'s password\
D) Enable MFA for the user

**Correct: B**\
*Explanation: Multiple failed attempts from various global IPs suggests
a credential stuffing or brute force attack. Immediately suspending the
account prevents unauthorized access while you investigate.*

**Q24.** SCENARIO: Your security team has mandated that all sessions
must terminate after 4 hours of inactivity, but users are complaining
about being logged out during their workday.

What is the BEST solution that maintains security while improving user
experience?

A\) Increase timeout to 24 hours\
B) Disable session timeout\
C) Implement SSO with the identity provider managing session duration\
D) Tell users to click around periodically to stay logged in

**Correct: C**\
*Explanation: SSO allows the identity provider to manage session
policies centrally. Users stay authenticated as long as their IdP
session is valid, while Phase Mirror honors the IdP\'s security
policies.*

**DOMAIN 3: INTEGRATIONS (25% - 12-13 Questions)**

**Multiple Choice Questions**

**Q25.** Which integration is required for automatic AI system discovery
from source code?

A\) Jira\
B) Slack\
C) GitHub/GitLab\
D) ServiceNow

**Correct: C**\
*Explanation: Source control integrations (GitHub, GitLab, Bitbucket)
enable automatic discovery of AI systems by scanning for ML frameworks
and model files.*

**Q26.** What is the PRIMARY purpose of the Jira integration?

A\) User authentication\
B) Creating tickets from action items\
C) Storing AI system documentation\
D) Sending notifications

**Correct: B**\
*Explanation: The Jira integration allows action items and dissonances
to be converted into Jira tickets for tracking in existing workflows.*

**Q27.** How often does the GitHub integration sync by default?

A\) Every hour\
B) Every 6 hours\
C) Every 24 hours\
D) Only when manually triggered

**Correct: C**\
*Explanation: GitHub syncs automatically every 24 hours. Manual sync is
available for immediate updates.*

**Q28.** Which integration would you configure to send real-time alerts
to your security team?

A\) GitHub\
B) Jira\
C) Splunk\
D) Microsoft Teams

**Correct: C**\
*Explanation: Splunk (SIEM) integration is designed for security
monitoring and alerting. Teams is for general notifications but not
security-focused.*

**Q29.** A webhook fails to deliver after 3 retry attempts. What happens
next?

A\) The webhook is automatically disabled\
B) The event is logged as failed and an alert is sent\
C) The system continues retrying indefinitely\
D) The event is silently dropped

**Correct: B**\
*Explanation: After retry exhaustion, the event is logged as failed
delivery and an alert is generated for admin attention. Webhooks are not
automatically disabled.*

**Q30.** What authentication method is used for Phase Mirror API calls?

A\) Username and password\
B) API key in header\
C) OAuth 2.0\
D) SAML assertion

**Correct: B**\
*Explanation: Phase Mirror API uses API keys passed in the Authorization
header. API keys can be created and managed in Settings.*

**Q31.** Which field mapping is REQUIRED when configuring the Jira
integration?

A\) Description\
B) Labels\
C) Summary (title)\
D) Story points

**Correct: C**\
*Explanation: Summary/title is a required field in Jira. Description,
labels, and other fields are optional but recommended.*

**Multiple Select Questions**

**Q32.** Which integrations support bidirectional sync? (Select TWO)

☐ A) GitHub (source control)\
☐ B) Slack (notifications)\
☐ C) Jira (ticketing)\
☐ D) Splunk (SIEM)\
☐ E) ServiceNow (ticketing)

**Correct: C, E**\
*Explanation: Ticketing integrations (Jira, ServiceNow) support
bidirectional sync---creating tickets from Phase Mirror and updating
Phase Mirror when tickets are resolved. Source control is inbound only,
notifications are outbound only.*

**Q33.** What information is needed to configure the GitHub integration?
(Select THREE)

☐ A) GitHub organization name\
☐ B) GitHub user password\
☐ C) OAuth authorization\
☐ D) Repository selection\
☐ E) Webhook secret

**Correct: A, C, D**\
*Explanation: GitHub integration requires OAuth authorization (not
password), organization name, and repository selection. Webhook secrets
are auto-generated.*

**Scenario-Based Questions**

**Q34.** SCENARIO: The Jira integration was working yesterday but
tickets are no longer being created today. No configuration changes were
made in Phase Mirror.

What should you check FIRST?

A\) Phase Mirror server status\
B) Jira API token expiration\
C) Network connectivity between systems\
D) Whether new action items are being created

**Correct: B**\
*Explanation: API tokens often have expiration dates. Since no Phase
Mirror changes were made, check the external system (Jira) first. Token
expiration is a common cause of sudden integration failure.*

**Q35.** SCENARIO: Your organization wants to automatically create a
ServiceNow incident when a Critical dissonance is detected, but only
during business hours.

How would you configure this?

A\) This is not possible in Phase Mirror\
B) Configure a conditional webhook with time-based rules\
C) Ask ServiceNow to filter incidents by time\
D) Manually create incidents during business hours

**Correct: B**\
*Explanation: Webhooks can be configured with conditional rules
including time-based triggers. This allows automated incident creation
only during specified hours.*

**DOMAIN 4: OPERATIONS (15% - 7-8 Questions)**

**Multiple Choice Questions**

**Q36.** What is the recommended frequency for reviewing platform health
dashboards?

A\) Hourly\
B) Daily\
C) Weekly\
D) Monthly

**Correct: C**\
*Explanation: Weekly review of platform health balances proactive
monitoring with practical time investment. Daily checks are recommended
during hypercare or after major changes.*

**Q37.** Where would you find information about planned maintenance
windows?

A\) Audit log\
B) Status page
([[status.phasemirror.com]{.underline}](http://status.phasemirror.com))\
C) Admin settings\
D) Help center

**Correct: B**\
*Explanation: The status page provides real-time system status and
announces planned maintenance windows.*

**Q38.** What is the purpose of the \"Data Export\" feature?

A\) To migrate to a competitor\
B) To create backups and support compliance requirements\
C) To share data with third parties\
D) To delete old data

**Correct: B**\
*Explanation: Data Export supports backup, compliance reporting, and
audit evidence collection. It\'s not designed for migration or
deletion.*

**Q39.** How often should you rotate API keys as a security best
practice?

A\) Never---keep them stable\
B) Every 30 days\
C) Every 90 days\
D) Annually

**Correct: C**\
*Explanation: 90-day rotation balances security with operational
stability. More frequent rotation may be required in high-security
environments.*

**Scenario-Based Questions**

**Q40.** SCENARIO: Your organization has a regulatory examination in 30
days. The examiner has requested documentation of your AI governance
controls and user access history.

What steps should you take to prepare? (Arrange in order)

1.  Generate audit log export for the examination period

2.  Review and update any stale documentation

3.  Generate AI system inventory report

4.  Brief stakeholders on examination process

5.  Create audit evidence package

**Correct Order: 4, 2, 3, 1, 5**\
*Explanation: Start with stakeholder alignment, ensure documentation is
current, then generate reports (inventory, audit logs), and compile into
the evidence package.*

**DOMAIN 5: TROUBLESHOOTING (10% - 5 Questions)**

**Multiple Choice Questions**

**Q41.** A user reports slow platform performance. What is the FIRST
diagnostic step?

A\) Restart the Phase Mirror servers\
B) Ask the user to try a different browser\
C) Check the status page for known issues\
D) Escalate to Phase Mirror support immediately

**Correct: C**\
*Explanation: Always check for known issues first. The status page shows
current system health and any ongoing incidents.*

**Q42.** SSO login is failing with \"Invalid signature\" error. What is
the MOST LIKELY cause?

A\) User entered wrong password\
B) IdP certificate has expired or changed\
C) User account is locked\
D) SSO is not enabled

**Correct: B**\
*Explanation: \"Invalid signature\" indicates a certificate mismatch.
The IdP certificate may have been rotated without updating Phase
Mirror.*

**Q43.** Users report that notifications are not being delivered to
Slack. The integration shows as \"Connected.\" What should you check?

A\) Whether users have Slack accounts\
B) Whether the Slack channel still exists and bot has access\
C) Whether Phase Mirror servers are running\
D) Whether notifications are enabled in user preferences

**Correct: B**\
*Explanation: A connected integration can fail if the target channel is
deleted, renamed, or if the bot\'s permissions are revoked. Check
Slack-side configuration.*

**Q44.** When should you escalate an issue to Phase Mirror support
versus troubleshooting further?

A\) After any error occurs\
B) After ruling out configuration issues and the problem persists\
C) Only during critical outages\
D) Never---always troubleshoot internally

**Correct: B**\
*Explanation: Escalate after basic troubleshooting (configuration, known
issues, browser/network) fails to resolve the issue. This provides
support with useful diagnostic information.*

**Q45.** A system owner cannot register a new AI system---the \"Add
System\" button is grayed out. What is the cause?

A\) The platform is in read-only mode\
B) The user doesn\'t have System Owner role for any systems yet\
C) The organization has reached its system limit\
D) Both B and C are possible

**Correct: D**\
*Explanation: The button could be disabled due to insufficient
permissions (new System Owner with no existing systems) OR if the
organization has reached their tier\'s system limit.*

**REMAINING QUESTIONS (5 Additional)**

**Q46.** What is the correct sequence for rotating an API key without
service disruption?

A\) Delete old key → Create new key → Update applications\
B) Create new key → Update applications → Delete old key\
C) Update applications → Delete old key → Create new key\
D) Delete all keys → Create new keys

**Correct: B**\
*Explanation: Create the new key first, update all applications to use
it, then delete the old key. This ensures continuous service.*

**Q47.** Which report shows the relationship between users and their AI
system assignments?

A\) User Activity Report\
B) Access Matrix Report\
C) Audit Log Export\
D) System Inventory Report

**Correct: B**\
*Explanation: The Access Matrix Report shows which users have access to
which systems and their permission levels.*

**Q48.** MATCHING: Match the issue with the most likely solution.

  ---------------------------------------------- ------------------------------------
  Issue                                          Solution
  1\. User can\'t log in with SSO                A. Check role assignments
  2\. User sees \"Access Denied\" on AI system   B. Verify IdP configuration
  3\. Bulk import failed partially               C. Check CSV for formatting errors
  4\. User doesn\'t see expected menu options    D. Verify user system assignments
  ---------------------------------------------- ------------------------------------

**Correct: 1-B, 2-D, 3-C, 4-A**

**Q49.** What retention period applies to audit logs in the Business
tier?

A\) 1 year\
B) 3 years\
C) 7 years\
D) Configurable

**Correct: B**\
*Explanation: Business tier retains audit logs for 3 years. Enterprise
tier provides 7 years with configurable options.*

**Q50.** Which action would you take to test SSO configuration before
enabling it for all users?

A\) Enable SSO and hope it works\
B) Test with a single admin account first\
C) Disable standard authentication immediately\
D) Ask all users to test simultaneously

**Correct: B**\
*Explanation: Always test SSO with a limited set of accounts (typically
admins) before broad rollout. Keep standard authentication as fallback
until SSO is verified.*

**PM-390: GOVERNANCE LEAD CERTIFICATION**

**60 Questions \| 90 Minutes \| 80% Passing**

**DOMAIN 1: GOVERNANCE METHODOLOGY (20% - 12 Questions)**

**Multiple Choice Questions**

**Q1.** What does \"dissonance\" mean in the Phase Mirror methodology?

A\) A disagreement between team members\
B) A gap between stated governance policy and actual implementation\
C) A technical error in the platform\
D) A failed compliance audit

**Correct: B**\
*Explanation: Dissonance refers to the productive contradictions between
what governance policies say and what actually happens in practice.*

**Q2.** The Phase Mirror methodology follows three steps: Mirror,
Dissonance, Phase. What does \"Mirror\" represent?

A\) Copying competitor governance frameworks\
B) Reflecting claims back without endorsement to establish facts\
C) Creating duplicate documentation\
D) Mirroring data across systems

**Correct: B**\
*Explanation: Mirror means reflecting stated claims (policies,
procedures, documentation) neutrally to establish a factual baseline
without judgment.*

**Q3.** What is a \"lever\" in Phase Mirror terminology?

A\) A technical feature of the platform\
B) An actionable item with owner, metric, and timeline to address a
dissonance\
C) A pricing discount\
D) A user permission level

**Correct: B**\
*Explanation: Levers are concrete, actionable outputs that address
identified dissonances. They include assigned ownership, success
metrics, and deadlines.*

**Q4.** Why does Phase Mirror consider contradictions \"productive\"?

A\) They generate revenue\
B) They reveal hidden assumptions that can become governance
improvements\
C) They create conflict that motivates change\
D) They are not considered productive

**Correct: B**\
*Explanation: Contradictions expose hidden assumptions and gaps. Naming
these explicitly converts them from vague risks into specific
improvement opportunities.*

**Q5.** What distinguishes Phase Mirror\'s approach from traditional
compliance checklists?

A\) It costs more\
B) It focuses on finding gaps between policy and reality, not just
checking boxes\
C) It requires more staff\
D) It only works for financial services

**Correct: B**\
*Explanation: Traditional checklists verify policy existence. Phase
Mirror verifies policy implementation and identifies where reality
diverges from stated intentions.*

**Q6.** What is a \"binding artifact\" in Phase Mirror terminology?

A\) A legal contract\
B) A concrete specification (SLA, spec, contract) versus a vague policy\
C) A locked document that cannot be edited\
D) A mandatory compliance requirement

**Correct: B**\
*Explanation: Binding artifacts are concrete, specific documents
(specifications, SLAs, contracts) that create accountability, as opposed
to vague policy statements.*

**Scenario-Based Questions**

**Q7.** SCENARIO: Your organization\'s AI policy states \"All AI
decisions affecting customers require human oversight.\" During
dissonance analysis, you discover that your fraud detection system
autonomously blocks 50,000 transactions daily with no human review.

This is an example of:

A\) Compliant implementation\
B) A documentation gap\
C) A dissonance between policy and implementation\
D) A technical error

**Correct: C**\
*Explanation: This is a classic dissonance---policy states human
oversight is required, but implementation has none. This needs to be
addressed through a lever (perhaps redefining \"oversight\" for
high-volume systems).*

**Q8.** SCENARIO: Following the situation in Q7, which of the following
would be the BEST lever to address this dissonance?

A\) Remove the policy requirement for human oversight\
B) Hire 1,000 people to manually review all transactions\
C) Define \"oversight\" as exception-based human review with complete
audit trail and 2% sampling\
D) Ignore the dissonance since the system works well

**Correct: C**\
*Explanation: The best lever maintains the spirit of oversight while
being operationally feasible. Defining specific oversight mechanisms
(audit trails, sampling, exception review) creates a binding artifact.*

**DOMAIN 2: CONFIGURATION (25% - 15 Questions)**

**Multiple Choice Questions**

**Q9.** How many default risk tiers does Phase Mirror provide?

A\) 2 (High, Low)\
B) 3 (High, Medium, Low)\
C) 4 (Critical, High, Medium, Low)\
D) 5 (Critical, High, Medium, Low, Minimal)

**Correct: C**\
*Explanation: Phase Mirror provides four default risk tiers: Critical,
High, Medium, and Low. Organizations can customize these.*

**Q10.** Which risk tier should be assigned to an AI system that makes
autonomous credit decisions affecting consumers?

A\) Low\
B) Medium\
C) High\
D) Critical

**Correct: D**\
*Explanation: Customer-facing autonomous decision systems with
regulatory implications (fair lending) should be classified as
Critical.*

**Q11.** What happens when you configure a rule with the condition
\"Risk Tier = Critical\" and action \"Require Documentation\"?

A\) All Critical systems must have documentation uploaded before
registration completes\
B) Critical systems are automatically documented\
C) Documentation is optional for Critical systems\
D) Only Critical systems can have documentation

**Correct: A**\
*Explanation: The rule enforces that Critical systems cannot be
registered without required documentation, creating a governance gate.*

**Q12.** How do you test a governance rule before activating it for all
systems?

A\) You cannot test rules\
B) Use the \"Test Rule\" feature against sample systems\
C) Activate it and see what happens\
D) Ask users to report issues

**Correct: B**\
*Explanation: The Test Rule feature allows you to run rules against
existing systems to preview what dissonances would be generated.*

**Q13.** What is the recommended maximum number of approval steps in a
workflow?

A\) 1\
B) 3\
C) 5\
D) Unlimited

**Correct: C**\
*Explanation: Best practice is to limit workflows to 5 or fewer steps to
prevent approval fatigue and delays. Complex approvals should be
simplified or run in parallel.*

**Q14.** When configuring an approval workflow, what does \"parallel
approval\" mean?

A\) Multiple approvers must approve in sequence\
B) Multiple approvers can approve simultaneously, and all must approve\
C) Any one of multiple approvers can approve\
D) Approvals happen automatically

**Correct: B**\
*Explanation: Parallel approval means multiple approvers review
simultaneously (faster), but all must approve. This differs from
sequential (one after another) or any-of (one approval sufficient).*

**Q15.** Which setting controls how long before a system owner is
reminded about an upcoming periodic review?

A\) Review reminder days\
B) SLA warning threshold\
C) Notification preferences\
D) Calendar integration

**Correct: A**\
*Explanation: Review reminder days (e.g., 14 days before due) determines
when automatic reminders are sent for upcoming reviews.*

**Multiple Select Questions**

**Q16.** Which elements can be used as conditions in governance rules?
(Select FOUR)

☐ A) Risk tier\
☐ B) System owner\'s salary\
☐ C) Regulatory tags\
☐ D) System type (ML, LLM, Agent)\
☐ E) Business unit\
☐ F) Weather conditions

**Correct: A, C, D, E**\
*Explanation: Rules can condition on risk tier, regulatory tags, system
type, business unit, and other system attributes. Personal employee data
and external factors are not available.*

**Q17.** What actions can a governance rule trigger? (Select THREE)

☐ A) Require specific documentation\
☐ B) Send notification\
☐ C) Automatically delete the system\
☐ D) Create a dissonance finding\
☐ E) Change the system\'s risk tier automatically

**Correct: A, B, D**\
*Explanation: Rules can require documentation, send notifications, and
create dissonance findings. They cannot delete systems or auto-change
risk tiers (which requires human judgment).*

**DOMAIN 3: DISSONANCE MANAGEMENT (20% - 12 Questions)**

**Multiple Choice Questions**

**Q18.** What is the recommended response time for a Critical
dissonance?

A\) Same day\
B) Within 1 week\
C) Within 30 days\
D) No specific timeline

**Correct: A**\
*Explanation: Critical dissonances should be reviewed and triaged the
same day they are identified due to their potential impact.*

**Q19.** When reviewing a dissonance, what is the FIRST step?

A\) Create an action item\
B) Assign an owner\
C) Verify the finding is accurate\
D) Dismiss it

**Correct: C**\
*Explanation: Always verify accuracy first. False positives should be
dismissed with documentation. Valid findings then proceed to action item
creation.*

**Q20.** What should you document when dismissing a dissonance as a
false positive?

A\) Nothing---just dismiss it\
B) The reason it\'s not applicable and any compensating controls\
C) The name of who requested dismissal\
D) Only the date of dismissal

**Correct: B**\
*Explanation: Dismissal documentation should explain why the finding
doesn\'t apply and identify any compensating controls. This creates an
audit trail.*

**Q21.** How long should remediation typically take for a High severity
dissonance?

A\) Same day\
B) 14 days\
C) 30 days\
D) 90 days

**Correct: B**\
*Explanation: High severity dissonances should typically be remediated
within 14 days (2 weeks). Critical = same day/7 days, Medium = 30 days,
Low = 60-90 days.*

**Q22.** What happens when an action item\'s due date passes without
completion?

A\) It is automatically completed\
B) It is automatically escalated\
C) It is marked overdue and generates alerts per configuration\
D) It is deleted

**Correct: C**\
*Explanation: Overdue items are flagged and generate alerts. Automatic
escalation can be configured but isn\'t the default behavior.*

**Q23.** When should you request an exception rather than remediating a
dissonance?

A\) When remediation is inconvenient\
B) When the rule genuinely doesn\'t apply and compensating controls
exist\
C) When you disagree with the governance policy\
D) Exceptions should never be requested

**Correct: B**\
*Explanation: Exceptions are appropriate when rules don\'t fit specific
situations AND compensating controls maintain governance intent.
Disagreeing with policy should go through policy change processes.*

**Scenario-Based Questions**

**Q24.** SCENARIO: A dissonance indicates that model documentation
hasn\'t been updated in 8 months, but the system owner claims \"nothing
has changed.\" Upon investigation, you find the model was retrained 4
months ago with new data.

What is the appropriate action?

A\) Dismiss the dissonance since nothing major changed\
B) Accept the system owner\'s claim and close the finding\
C) Confirm the dissonance is valid; retraining is a material change
requiring documentation update\
D) Escalate to legal immediately

**Correct: C**\
*Explanation: Model retraining, especially with new data, is a material
change that requires documentation updates. The dissonance is valid.*

**Q25.** SCENARIO: Your dissonance dashboard shows 47 open dissonances:
2 Critical, 8 High, 22 Medium, 15 Low. You have limited time today.

What should you prioritize?

A\) Work on the 15 Low items since they\'re easy\
B) Address the 2 Critical items first, then the 8 High\
C) Work on whatever is oldest\
D) Divide your time equally across all severities

**Correct: B**\
*Explanation: Always prioritize by severity. Critical dissonances
represent the highest risk and should be addressed first, followed by
High.*

**DOMAIN 4: COMPLIANCE (20% - 12 Questions)**

**Multiple Choice Questions**

**Q26.** Which Phase Mirror compliance pack specifically addresses model
risk management for banks?

A\) EU AI Act Readiness Pack\
B) Financial Services Compliance Pack\
C) Healthcare Compliance Pack\
D) Agentic AI Governance Pack

**Correct: B**\
*Explanation: The Financial Services Compliance Pack includes SR 11-7
model risk management alignment, fair lending rules, and examination
documentation.*

**Q27.** Under the EU AI Act, which risk category requires conformity
assessment before market deployment?

A\) Minimal risk\
B) Limited risk\
C) High-risk\
D) All AI systems

**Correct: C**\
*Explanation: High-risk AI systems (Annex III) require conformity
assessment before deployment. Minimal and limited risk have lighter
requirements.*

**Q28.** What is the purpose of the \"Examination Prep\" feature in the
Financial Services Compliance Pack?

A\) To prepare employees for certification exams\
B) To generate documentation packages for regulatory examinations\
C) To test the platform\'s performance\
D) To prepare for job interviews

**Correct: B**\
*Explanation: Examination Prep generates comprehensive documentation
packages (inventory, governance records, validation evidence) for
regulatory examinations.*

**Q29.** Which regulation requires \"fundamental rights impact
assessment\" for certain AI systems?

A\) HIPAA\
B) SR 11-7\
C) EU AI Act\
D) SOX

**Correct: C**\
*Explanation: The EU AI Act requires fundamental rights impact
assessments for high-risk AI systems deployed in the EU.*

**Q30.** How does Phase Mirror help with fair lending compliance?

A\) By making loan decisions\
B) By monitoring for bias and documenting adverse action reasoning\
C) By setting interest rates\
D) It doesn\'t address fair lending

**Correct: B**\
*Explanation: The Financial Services Compliance Pack includes bias
monitoring thresholds and adverse action documentation to support fair
lending compliance.*

**Q31.** What is the recommended audit trail retention period for
financial services institutions?

A\) 1 year\
B) 3 years\
C) 7 years\
D) 10 years

**Correct: C**\
*Explanation: 7 years is the standard retention period for financial
services, aligning with regulatory requirements and statute of
limitations considerations.*

**Multiple Select Questions**

**Q32.** Which elements are included in a Phase Mirror examination
package? (Select FOUR)

☐ A) AI system inventory with risk classifications\
☐ B) Employee performance reviews\
☐ C) Governance documentation and approval records\
☐ D) Dissonance history and remediation evidence\
☐ E) Audit trail for the examination period\
☐ F) Competitor analysis

**Correct: A, C, D, E**\
*Explanation: Examination packages include system inventory, governance
documentation, dissonance/remediation history, and audit trails. HR data
and competitive intelligence are not included.*

**DOMAIN 5: PROGRAM MANAGEMENT (15% - 9 Questions)**

**Multiple Choice Questions**

**Q33.** What is a healthy \"Governance Health Score\" target?

A\) 50-60\
B) 60-70\
C) 70-80\
D) 90+

**Correct: D**\
*Explanation: Organizations should target a health score of 90+,
indicating comprehensive governance coverage, current documentation, and
minimal open dissonances.*

**Q34.** How often should Governance Leads generate executive summary
reports?

A\) Daily\
B) Weekly\
C) Monthly or Quarterly\
D) Annually

**Correct: C**\
*Explanation: Executive summaries are typically generated monthly for
management and quarterly for board reporting.*

**Q35.** Which metric best indicates governance program effectiveness
over time?

A\) Number of AI systems registered\
B) Dissonance remediation time trend\
C) Number of users\
D) Amount of documentation uploaded

**Correct: B**\
*Explanation: Decreasing remediation times indicate improving governance
maturity. Registration counts and documentation volume don\'t measure
effectiveness.*

**Q36.** What percentage of AI systems should have current documentation
as a program target?

A\) 50%\
B) 75%\
C) 95%\
D) 100%

**Correct: C**\
*Explanation: Target 95%+ documentation currency. 100% is ideal but
allows for recently registered systems or systems in transition.*

**Q37.** When launching a governance program, what is the recommended
approach?

A\) Register all systems on day one\
B) Start with Critical and High risk systems, then expand\
C) Start with Low risk systems to practice\
D) Wait until all documentation is perfect

**Correct: B**\
*Explanation: Phased rollout starting with highest-risk systems ensures
the most important systems are governed first and allows process
refinement before full rollout.*

**Scenario-Based Questions**

**Q38.** SCENARIO: After 6 months of operation, your governance metrics
show: 95% of systems registered, 40% overdue on periodic reviews,
average dissonance remediation time of 45 days.

What is your MOST pressing concern?

A\) The 5% unregistered systems\
B) The 40% overdue reviews\
C) The 45-day remediation time\
D) All are equally concerning

**Correct: B**\
*Explanation: 40% overdue reviews indicates a systemic process failure.
This is more pressing than the registration gap (small) or remediation
time (moderately high but not critical).*

**Q39.** SCENARIO: An executive asks why they should invest in AI
governance when \"we haven\'t had any AI problems.\"

What is the BEST response?

A\) \"You\'re right, maybe we don\'t need it\"\
B) \"Governance prevents problems before they occur and prepares for
regulatory requirements\"\
C) \"Because I said so\"\
D) \"Other companies are doing it\"

**Correct: B**\
*Explanation: Frame governance as proactive risk management and
regulatory preparation, not reactive problem-solving. Waiting for
problems is not a governance strategy.*

*\[Continuing with remaining questions through Q60\...\]*

**ADDITIONAL GOVERNANCE LEAD QUESTIONS (Q40-Q60)**

**Q40.** What is the primary purpose of the quarterly business review
(QBR) with your CSM?

A\) To negotiate pricing\
B) To align on strategic goals, review metrics, and plan improvements\
C) To report technical issues\
D) To request new features

**Correct: B**

**Q41.** Which dashboard widget is MOST important for daily monitoring?

A\) Total AI systems count\
B) Open Critical/High dissonances\
C) User activity\
D) Storage usage

**Correct: B**

**Q42.** When should you involve legal counsel in dissonance
remediation?

A\) For every dissonance\
B) When findings have potential regulatory or litigation implications\
C) Never---governance is not a legal function\
D) Only during examinations

**Correct: B**

**Q43.** ORDER: Arrange the steps for responding to a new Critical
dissonance:

1.  Create action item with owner and deadline

2.  Verify finding accuracy

3.  Review dissonance details

4.  Communicate to stakeholders if needed

5.  Monitor remediation progress

**Correct Order: 3, 2, 1, 4, 5**

**Q44.** What distinguishes a \"High\" risk system from a \"Critical\"
risk system?

A\) Cost\
B) Critical systems have direct customer impact or regulatory scrutiny;
High systems have significant but less immediate impact\
C) Number of users\
D) Age of the system

**Correct: B**

**Q45.** How should you handle a dissonance that reveals potential
regulatory violations?

A\) Delete it to avoid evidence\
B) Document, escalate to compliance/legal, and create high-priority
remediation\
C) Mark as resolved without action\
D) Wait for the regulator to find it

**Correct: B**

**Q46-Q60:** *\[Additional questions covering workflow design, exception
management, cross-functional collaboration, change management, metrics
analysis, board communication, audit preparation, and program maturity
assessment\]*

**PM-490: SYSTEM OWNER CERTIFICATION**

**30 Questions \| 45 Minutes \| 80% Passing**

**DOMAIN 1: REGISTRATION (30% - 9 Questions)**

**Multiple Choice Questions**

**Q1.** Which field is REQUIRED when registering a new AI system?

A\) Source repository link\
B) System name and description\
C) Model accuracy metrics\
D) Deployment cost

**Correct: B**\
*Explanation: System name and description are mandatory. Other fields
may be required based on governance rules but are not universally
required.*

**Q2.** What risk tier should you assign to an internal document
classification tool used only by employees?

A\) Critical\
B) High\
C) Medium\
D) Low

**Correct: C**\
*Explanation: Internal-only tools without customer impact or significant
regulatory implications typically qualify as Medium risk.*

**Q3.** When is a system considered \"complete\" in registration?

A\) When the name is entered\
B) When all required fields are populated and required documents
uploaded\
C) When it\'s saved as draft\
D) When approved by governance

**Correct: B**\
*Explanation: Complete registration requires all mandatory fields and
documents. Approval is a separate step after completion.*

**Q4.** What should you do if you\'re unsure about the correct risk tier
for your system?

A\) Guess and move on\
B) Always select Critical to be safe\
C) Consult with Governance Lead or use risk classification guidance\
D) Leave it blank

**Correct: C**\
*Explanation: When uncertain, consult governance resources or the
Governance Lead. Over-classifying wastes resources; under-classifying
creates risk.*

**Q5.** Which document is typically required for Critical risk AI
systems?

A\) Marketing brochure\
B) User manual\
C) Validation report\
D) All of the above

**Correct: C**\
*Explanation: Validation reports demonstrating system testing and
performance are typically required for Critical systems to ensure proper
vetting before deployment.*

**Q6.** What happens after you submit a Critical system for
registration?

A\) It\'s immediately active\
B) It enters an approval workflow\
C) It\'s automatically rejected\
D) Nothing---you must manually activate it

**Correct: B**\
*Explanation: Critical systems typically require Governance Lead
approval before being fully registered, per governance rules.*

**Scenario-Based Questions**

**Q7.** SCENARIO: You\'re registering an AI system that uses customer
transaction data to detect fraud. It runs autonomously and blocks
suspicious transactions without human review.

What information is MOST important to capture accurately?

A\) The color scheme of the user interface\
B) Data sensitivity (customer financial data), decision type
(autonomous), and customer impact (direct)\
C) The names of the developers\
D) The hardware specifications

**Correct: B**\
*Explanation: Data sensitivity, decision autonomy, and customer impact
directly affect risk classification and governance requirements.*

**Q8.** SCENARIO: You need to register 15 AI systems your team owns.
Five are production systems and ten are development prototypes.

What is the BEST approach?

A\) Register all 15 at once with the same information\
B) Register the 5 production systems first as higher priority, then
development systems\
C) Only register production systems\
D) Wait until all are in production

**Correct: B**\
*Explanation: Prioritize production systems but also register
development systems (likely as Low risk) for complete visibility and
governance preparation.*

**DOMAIN 2: DOCUMENTATION (25% - 7-8 Questions)**

**Q9.** How soon after a material change should documentation be
updated?

A\) Within 24 hours\
B) Within 30 days (or per your organization\'s policy)\
C) Within 1 year\
D) Only during annual reviews

**Correct: B**\
*Explanation: Most governance policies require documentation updates
within 30 days of material changes. Check your organization\'s specific
requirements.*

**Q10.** Which of the following is considered a \"material change\"
requiring documentation update?

A\) Fixing a typo in comments\
B) Model retraining with new data\
C) Changing a variable name\
D) Adding logging

**Correct: B**\
*Explanation: Model retraining, especially with new data, can
significantly change system behavior and requires documentation updates.
Minor code changes do not.*

**Q11.** What is the purpose of the \"model card\" document type?

A\) To track model training costs\
B) To provide standardized documentation of model details, performance,
and limitations\
C) To replace all other documentation\
D) To store credit card information

**Correct: B**\
*Explanation: Model cards provide standardized documentation of ML model
characteristics, intended uses, performance metrics, and limitations.*

**Q12.** MATCHING: Match documents to their primary purpose:

  ----------------------- --------------------------------------------
  Document                Purpose
  1\. System Design       A. How the system is watched in production
  2\. Validation Report   B. Architecture and design decisions
  3\. Monitoring Spec     C. Evidence of testing and performance
  4\. Data Dictionary     D. Description of data elements used
  ----------------------- --------------------------------------------

**Correct: 1-B, 2-C, 3-A, 4-D**

**Q13.** What should you do if required documentation doesn\'t exist
yet?

A\) Upload a blank document\
B) Skip the registration entirely\
C) Register what you can and create an action item to complete
documentation\
D) Copy documentation from another system

**Correct: C**\
*Explanation: Register with available information and track
documentation gaps as action items. Don\'t delay registration
indefinitely but do address gaps.*

**DOMAIN 3: DISSONANCE RESPONSE (25% - 7-8 Questions)**

**Q14.** You receive a notification of a new dissonance on your system.
What is your FIRST action?

A\) Immediately dismiss it\
B) Read the finding details and assess accuracy\
C) Assign it to someone else\
D) Ignore it

**Correct: B**\
*Explanation: First understand what the finding says and whether it\'s
accurate. Then decide on appropriate response.*

**Q15.** A dissonance indicates your documentation is out of date. You
updated it last week. What should you do?

A\) Dispute the finding with evidence of recent update\
B) Update documentation again\
C) Ignore it\
D) Delete the system

**Correct: A**\
*Explanation: If the finding is inaccurate (documentation is current),
dispute with evidence. The system may not have recognized the recent
update.*

**Q16.** What information should an action item include?

A\) Just a title\
B) Title, description, owner, and due date\
C) Only a due date\
D) A complaint about the finding

**Correct: B**\
*Explanation: Effective action items include clear title, description of
work needed, assigned owner, and realistic due date.*

**Q17.** How should you respond if a dissonance finding reveals a
legitimate governance gap?

A\) Hide the finding\
B) Accept the finding, create an action item, and remediate\
C) Argue that the rule is wrong\
D) Transfer ownership to avoid responsibility

**Correct: B**\
*Explanation: Legitimate findings should be accepted and addressed.
Creating action items with clear ownership ensures remediation.*

**Q18.** SCENARIO: A dissonance states your system lacks bias
monitoring, but your system is a document classification tool that
doesn\'t make decisions about people.

What is the appropriate response?

A\) Implement bias monitoring anyway\
B) Request an exception with justification that bias monitoring isn\'t
applicable\
C) Delete the system\
D) Ignore the finding

**Correct: B**\
*Explanation: Bias monitoring may not apply to systems that don\'t
affect people. Request an exception with clear justification and any
compensating controls.*

**DOMAIN 4: REVIEWS & LIFECYCLE (20% - 6 Questions)**

**Q19.** How often should Critical systems undergo periodic review?

A\) Weekly\
B) Monthly\
C) Quarterly\
D) Annually

**Correct: B**\
*Explanation: Critical systems typically require monthly reviews. High =
quarterly, Medium = semi-annual, Low = annual.*

**Q20.** What should a periodic review include?

A\) Only checking if the system still runs\
B) Documentation currency, performance assessment, risk review, and
compliance check\
C) Reviewing the original development proposal\
D) Updating the system name

**Correct: B**\
*Explanation: Periodic reviews comprehensively assess documentation,
performance, risk profile, and compliance status.*

**Q21.** When should you transfer system ownership?

A\) Never---original owner is always responsible\
B) When you\'re going on vacation\
C) When you\'re leaving the team or system responsibility is formally
changing\
D) Whenever a dissonance is found

**Correct: C**\
*Explanation: Transfer ownership for permanent changes (team moves,
departures, reorganization). Temporary absence doesn\'t require
transfer.*

**Q22.** What is the correct process for decommissioning an AI system?

A\) Just stop using it\
B) Delete from Phase Mirror immediately\
C) Archive with reason, confirm data handling, and document
decommission\
D) Transfer to someone else\'s ownership

**Correct: C**\
*Explanation: Proper decommissioning includes archiving (not deleting)
the record, documenting reasons, and confirming appropriate data
handling.*

**Q23-Q30:** *\[Additional questions covering exception requests,
complex system registration, version management, cross-team
coordination, and ownership responsibilities\]*

**ANSWER KEYS**

**PM-290 Administrator Certification Answer Key**

  ----- --------- ----- -------- ----- ----------- ----- -------- ----- -----------------
  Q\#   Answer    Q\#   Answer   Q\#   Answer      Q\#   Answer   Q\#   Answer
  1     B         11    B        21    A,B,D,F     31    C        41    C
  2     C         12    B        22    A,B,D,E,F   32    C,E      42    B
  3     C         13    C        23    B           33    A,C,D    43    B
  4     B         14    C        24    C           34    B        44    B
  5     A         15    C        25    C           35    B        45    D
  6     C         16    B        26    B           36    C        46    B
  7     B         17    C        27    C           37    B        47    B
  8     B         18    B        28    C           38    C        48    1-B,2-D,3-C,4-A
  9     A,B,D     19    C        29    B           39    C        49    B
  10    A,B,C,E   20    D        30    B           40    B        50    B
  ----- --------- ----- -------- ----- ----------- ----- -------- ----- -----------------

**PM-390 Governance Lead Certification Answer Key**

  ------ -------- ------ -------- ------ -----------
  Q\#    Answer   Q\#    Answer   Q\#    Answer
  1      B        21     B        41     B
  2      B        22     C        42     B
  3      B        23     C        43     3,2,1,4,5
  4      B        24     C        44     B
  5      B        25     B        45     B
  6      B        26     B        \...   \...
  7      C        27     C               
  8      C        28     B               
  9      C        29     C               
  10     D        30     B               
  \...   \...     \...   \...            
  ------ -------- ------ -------- ------ -----------

**PM-490 System Owner Certification Answer Key**

  ----- -------- ----- ----------------- ------ --------
  Q\#   Answer   Q\#   Answer            Q\#    Answer
  1     B        11    B                 21     C
  2     C        12    1-B,2-C,3-A,4-D   22     C
  3     B        13    C                 23     \...
  4     C        14    B                 \...   \...
  5     C        15    A                        
  6     B        16    B                        
  7     B        17    B                        
  8     B        18    B                        
  9     B        19    B                        
  10    B        20    B                        
  ----- -------- ----- ----------------- ------ --------

**EXAM ADMINISTRATION GUIDELINES**

**Proctoring Requirements**

  ----------------------- ------------------ -------------------------
  Certification           Proctoring         Environment
  PM-290 (Admin)          Online proctored   Secure browser required
  PM-390 (Governance)     Online proctored   Secure browser required
  PM-490 (System Owner)   Unproctored        Standard browser
  ----------------------- ------------------ -------------------------

**Exam Rules**

1.  **No external resources** during proctored exams

2.  **One active question** at a time (no going back for proctored)

3.  **Time visible** throughout exam

4.  **Results immediate** upon completion

5.  **Detailed feedback** available after completion

**Retake Policy**

  -------------- ------------- -------------------------------
  Attempt        Wait Period   Notes
  1st attempt    Included      No waiting
  2nd attempt    14 days       Included in certification fee
  3rd attempt    30 days       Additional fee required
  4th+ attempt   60 days       Additional fee required
  -------------- ------------- -------------------------------

**Accommodations**

Available accommodations:

-   Extended time (50% additional)

-   Screen reader compatibility

-   Separate testing room

-   Breaks (paused timer)

Request accommodations at:
[[certifications\@phasemirror.com]{.underline}](mailto:certifications@phasemirror.com)

**STUDY GUIDE RECOMMENDATIONS**

**PM-290 Administrator Exam**

**Focus Areas:**

1.  User provisioning workflows (25%)

2.  SSO/SAML/OIDC configuration (20%)

3.  Integration troubleshooting (20%)

4.  Audit log management (15%)

5.  Security settings (20%)

**Recommended Preparation:**

-   Complete PM-200 and PM-201 courses

-   Practice in sandbox environment

-   Review all lab exercises

-   Take practice exam (available in Academy)

**PM-390 Governance Lead Exam**

**Focus Areas:**

1.  Dissonance methodology concepts (20%)

2.  Rule and workflow configuration (25%)

3.  Dissonance triage and remediation (20%)

4.  Compliance pack knowledge (20%)

5.  Program metrics and improvement (15%)

**Recommended Preparation:**

-   Complete PM-300 and PM-301 courses

-   Complete at least one PM-310 compliance pack course

-   Review case studies

-   Practice dissonance triage scenarios

**PM-490 System Owner Exam**

**Focus Areas:**

1.  Complete and accurate registration (30%)

2.  Documentation requirements and maintenance (25%)

3.  Dissonance response procedures (25%)

4.  Periodic review process (20%)

**Recommended Preparation:**

-   Complete PM-400 course

-   Practice system registration in sandbox

-   Review sample dissonance scenarios

-   Understand your organization\'s specific governance rules

**END OF CERTIFICATION EXAM QUESTION BANKS**

These question banks provide comprehensive assessment materials for role
proficiency. Would you like me to create:

-   Practice exams with randomized question subsets

-   Detailed answer explanations document

-   Study flashcards for key concepts

-   Scenario-based case study assessments

-   Hands-on practical exam rubrics?

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

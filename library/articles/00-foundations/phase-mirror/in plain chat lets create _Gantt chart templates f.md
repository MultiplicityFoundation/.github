---
slug: in-plain-chat-lets-create-gantt-chart-templates-f
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 00-foundations/phase-mirror/in plain chat lets create _Gantt chart templates
    f.md
  last_synced: '2026-03-20T17:17:22.014997Z'
---

![](media/image-c96e3a4b0d2ba69e111ea390a92f56235a59dff3.png){width="2.6466666666666665in"
height="0.6666666666666666in"}

**in plain chat lets create**

Gantt chart templates for project management tools

Here are comprehensive Gantt chart templates for Phase Mirror
implementations across major project management tools:

**PHASE MIRROR GANTT CHART TEMPLATES**

**Project Management Tool Integration**

**Version:** 2.0 \| **Date:** January 2026\
**Purpose:** Ready-to-import project timelines for implementation

**TEMPLATE OVERVIEW**

**Available Templates by Tier**

  ---------------- ---------- -------- ------- ------------
  Tier             Duration   Phases   Tasks   Milestones
  **Team**         2 weeks    3        25      5
  **Business**     6 weeks    5        65      12
  **Enterprise**   12 weeks   5        120+    20
  ---------------- ---------- -------- ------- ------------

**Supported Tools**

  ----------------------------------------------- ------------ ----------------
  Tool                                            Format       Import Method
  Microsoft Project                               .mpp, .xml   File → Open
  Smartsheet                                      .xlsx        File → Import
  Asana                                           .csv         Add via CSV
  [[Monday.com]{.underline}](http://Monday.com)   .xlsx        Import boards
  Jira                                            .csv         Project import
  Wrike                                           .xlsx        Import → Excel
  ClickUp                                         .csv         Import/Export
  Notion                                          .csv         Import
  ----------------------------------------------- ------------ ----------------

**TEMPLATE 1: TEAM TIER (2 WEEKS)**

**Visual Gantt Chart**

PHASE MIRROR TEAM IMPLEMENTATION - 2 WEEK TIMELINE\
═══════════════════════════════════════════════════════════════════════════════\
\
WEEK 1 │ WEEK 2\
TASK M T W T F │ M T W T F\
──────────────────────────────────────────────────────────────────────────────\
\
PHASE 1: SETUP\
──────────────────────────────────────────────────────────────────────────────\
Account Creation ███ │\
Admin Configuration ███ │\
User Invitations ███ │\
Role Assignment ███ │\
GitHub Integration ███ │\
◆ Setup Complete ◆ │\
\
PHASE 2: SYSTEM REGISTRATION\
──────────────────────────────────────────────────────────────────────────────\
Priority Systems ███████ │\
Documentation Upload ███████ │\
Initial Analysis ███ │███\
◆ Systems Registered ◆ │\
\
PHASE 3: GO-LIVE\
──────────────────────────────────────────────────────────────────────────────\
Remaining Systems │ │███████\
Address Findings │ ███████\
Configure Notifications │ ███\
Team Training │ ███\
◆ Go-Live │ ◆\
──────────────────────────────────────────────────────────────────────────────\
\
LEGEND: ███ = Task Duration ◆ = Milestone

**Detailed Task List (CSV Format)**

WBS,Task Name,Duration,Start,Finish,Predecessors,Resource,% Complete\
1,PHASE 1: SETUP,4 days,Day 1,Day 4,,Admin,0%\
1.1,Account Creation & Verification,0.5 days,Day 1,Day 1,,Admin,0%\
1.2,Admin Configuration,0.5 days,Day 1,Day 1,1.1,Admin,0%\
1.3,Review Platform Settings,0.5 days,Day 1,Day 1,1.2,Admin,0%\
1.4,Invite Team Members,0.5 days,Day 2,Day 2,1.3,Admin,0%\
1.5,Assign User Roles,0.5 days,Day 2,Day 2,1.4,Admin,0%\
1.6,Connect GitHub Integration,1 day,Day 3,Day 3,1.5,Admin,0%\
1.7,Verify Integration Sync,0.5 days,Day 4,Day 4,1.6,Admin,0%\
1.8,MILESTONE: Setup Complete,0 days,Day 4,Day 4,1.7,,0%\
2,PHASE 2: SYSTEM REGISTRATION,5 days,Day 4,Day 8,,System Owners,0%\
2.1,Identify Priority AI Systems,0.5 days,Day 4,Day 4,1.8,Project
Lead,0%\
2.2,Register First 3 Systems,1 day,Day 4,Day 5,2.1,System Owners,0%\
2.3,Upload Basic Documentation,1 day,Day 5,Day 6,2.2,System Owners,0%\
2.4,Register Remaining Systems,1.5 days,Day 6,Day 7,2.3,System
Owners,0%\
2.5,Run Initial Dissonance Analysis,1 day,Day 7,Day 8,2.4,System
Owners,0%\
2.6,Review Analysis Results,0.5 days,Day 8,Day 8,2.5,All,0%\
2.7,MILESTONE: Systems Registered,0 days,Day 8,Day 8,2.6,,0%\
3,PHASE 3: GO-LIVE,4 days,Day 8,Day 10,,All,0%\
3.1,Create Action Items for Findings,1 day,Day 8,Day 9,2.7,System
Owners,0%\
3.2,Configure Notifications,0.5 days,Day 9,Day 9,3.1,Admin,0%\
3.3,Set Review Schedules,0.5 days,Day 9,Day 9,3.2,Admin,0%\
3.4,Team Training Session,1 hour,Day 10,Day 10,3.3,All,0%\
3.5,Go-Live Announcement,0.5 days,Day 10,Day 10,3.4,Project Lead,0%\
3.6,MILESTONE: Go-Live Complete,0 days,Day 10,Day 10,3.5,,0%\
4,POST GO-LIVE SUPPORT,Ongoing,Day 10,Day 14,,All,0%\
4.1,Monitor User Adoption,Ongoing,Day 10,Day 14,,Admin,0%\
4.2,Address Questions/Issues,Ongoing,Day 10,Day 14,,Admin,0%\
4.3,Week 2 Check-in,0.5 days,Day 14,Day 14,4.2,All,0%\
4.4,MILESTONE: Implementation Complete,0 days,Day 14,Day 14,4.3,,0%

**Microsoft Project XML Template**

\<?xml version=\"1.0\" encoding=\"UTF-8\"?\>\
\<Project xmlns=\"http://schemas.microsoft.com/project\"\>\
\<Name\>Phase Mirror Team Implementation\</Name\>\
\<StartDate\>2026-02-02T08:00:00\</StartDate\>\
\<FinishDate\>2026-02-13T17:00:00\</FinishDate\>\
\<CalendarUID\>1\</CalendarUID\>\
\<DefaultStartTime\>08:00:00\</DefaultStartTime\>\
\<DefaultFinishTime\>17:00:00\</DefaultFinishTime\>\
\<HoursPerDay\>8.0\</HoursPerDay\>\
\<HoursPerWeek\>40.0\</HoursPerWeek\>\
\<DaysPerMonth\>20\</DaysPerMonth\>\
\
\<Tasks\>\
\<!\-- Phase 1: Setup \--\>\
\<Task\>\
\<UID\>1\</UID\>\
\<ID\>1\</ID\>\
\<Name\>PHASE 1: SETUP\</Name\>\
\<Type\>1\</Type\>\
\<IsNull\>0\</IsNull\>\
\<OutlineLevel\>1\</OutlineLevel\>\
\<Summary\>1\</Summary\>\
\</Task\>\
\<Task\>\
\<UID\>2\</UID\>\
\<ID\>2\</ID\>\
\<Name\>Account Creation & Verification\</Name\>\
\<Duration\>PT4H0M0S\</Duration\>\
\<Start\>2026-02-02T08:00:00\</Start\>\
\<Finish\>2026-02-02T12:00:00\</Finish\>\
\<OutlineLevel\>2\</OutlineLevel\>\
\</Task\>\
\<Task\>\
\<UID\>3\</UID\>\
\<ID\>3\</ID\>\
\<Name\>Admin Configuration\</Name\>\
\<Duration\>PT4H0M0S\</Duration\>\
\<Start\>2026-02-02T13:00:00\</Start\>\
\<Finish\>2026-02-02T17:00:00\</Finish\>\
\<OutlineLevel\>2\</OutlineLevel\>\
\<PredecessorLink\>\
\<PredecessorUID\>2\</PredecessorUID\>\
\<Type\>1\</Type\>\
\</PredecessorLink\>\
\</Task\>\
\<!\-- Additional tasks follow same pattern \--\>\
\</Tasks\>\
\
\<Resources\>\
\<Resource\>\
\<UID\>1\</UID\>\
\<Name\>Administrator\</Name\>\
\<Type\>1\</Type\>\
\</Resource\>\
\<Resource\>\
\<UID\>2\</UID\>\
\<Name\>Project Lead\</Name\>\
\<Type\>1\</Type\>\
\</Resource\>\
\<Resource\>\
\<UID\>3\</UID\>\
\<Name\>System Owners\</Name\>\
\<Type\>1\</Type\>\
\</Resource\>\
\</Resources\>\
\</Project\>

**TEMPLATE 2: BUSINESS TIER (6 WEEKS)**

**Visual Gantt Chart**

PHASE MIRROR BUSINESS IMPLEMENTATION - 6 WEEK TIMELINE\
═══════════════════════════════════════════════════════════════════════════════════════════════════\
\
WK1 WK2 WK3 WK4 WK5 WK6\
TASK M T W T F M T W T F M T W T F M T W T F M T W T F M T W T F\
────────────────────────────────────────────────────────────────────────────────────────────────────\
\
PHASE 1: PLANNING\
────────────────────────────────────────────────────────────────────────────────────────────────────\
Kickoff Call █\
Stakeholder Align █ █\
Success Criteria █ █\
AI System Inventory █ █ █\
Week 1 Checkpoint █ ◆\
\
PHASE 2: TECHNICAL SETUP\
────────────────────────────────────────────────────────────────────────────────────────────────────\
Environment Setup █\
SSO Configuration █ █ █\
User Provisioning █ █\
Integration Setup █ █ █\
Week 2 Checkpoint █ ◆\
\
PHASE 3: GOVERNANCE CONFIG\
────────────────────────────────────────────────────────────────────────────────────────────────────\
Governance Workshop █\
Risk Classification █ █\
Rules Configuration █ █ █\
Workflow Setup █ █\
Compliance Packs █ █ █\
Week 3 Checkpoint █ ◆\
\
PHASE 4: PILOT\
────────────────────────────────────────────────────────────────────────────────────────────────────\
Pilot Training █\
Register Pilot Systems █ █ █\
Upload Documentation █ █ █\
Run Analyses █ █\
Review & Refine █ █ █\
Week 4 Checkpoint █ ◆\
\
PHASE 5: ROLLOUT\
────────────────────────────────────────────────────────────────────────────────────────────────────\
Wave 2 Training █\
Register All Systems █ █ █ █ █\
Complete Documentation █ █ █ █\
Portfolio Analysis █ █\
Week 5 Checkpoint █ ◆\
\
PHASE 6: GO-LIVE\
────────────────────────────────────────────────────────────────────────────────────────────────────\
Final Validation █\
Executive Briefing █\
All-Hands Training █\
GO-LIVE █ ◆\
Hypercare Support █ █ █ █ █\
Implementation Complete ◆\
────────────────────────────────────────────────────────────────────────────────────────────────────\
\
LEGEND: █ = Task Duration ◆ = Milestone

**Detailed Task List (CSV Format)**

WBS,Task Name,Duration,Start,Finish,Predecessors,Resource,Notes,%
Complete\
1,PHASE 1: PLANNING,5 days,Week 1 Mon,Week 1 Fri,,,0%\
1.1,Kickoff Call with CSM,2 hours,Week 1 Mon,Week 1 Mon,,Sponsor;
Project Lead; CSM,90-minute structured meeting,0%\
1.2,Stakeholder Alignment Meetings,1 day,Week 1 Mon,Week 1
Tue,1.1,Project Lead,Meet each stakeholder group,0%\
1.3,Define Success Criteria,1 day,Week 1 Tue,Week 1 Wed,1.2,Project
Lead; CSM,Document measurable goals,0%\
1.4,AI System Inventory Workshop,1.5 days,Week 1 Wed,Week 1
Thu,1.3,Project Lead; AI Leads,Identify all AI systems,0%\
1.5,Finalize Project Plan,0.5 days,Week 1 Fri,Week 1 Fri,1.4,Project
Lead; CSM,Confirm timeline and resources,0%\
1.6,Week 1 Checkpoint,0.5 hours,Week 1 Fri,Week 1 Fri,1.5,All,Status
review,0%\
1.7,MILESTONE: Planning Complete,0 days,Week 1 Fri,Week 1 Fri,1.6,,0%\
2,PHASE 2: TECHNICAL SETUP,5 days,Week 2 Mon,Week 2 Fri,1.7,,0%\
2.1,Environment Provisioning,0.5 days,Week 2 Mon,Week 2 Mon,,CSM,Confirm
tenant URL and access,0%\
2.2,Initial Admin Account Setup,0.5 days,Week 2 Mon,Week 2
Mon,2.1,Admin,Configure primary admin,0%\
2.3,SSO Design Session,1 hour,Week 2 Mon,Week 2 Mon,2.2,Admin; IT;
CSM,Plan SSO approach,0%\
2.4,SSO Configuration - IdP Side,1 day,Week 2 Tue,Week 2
Tue,2.3,IT,Create application in IdP,0%\
2.5,SSO Configuration - PM Side,0.5 days,Week 2 Wed,Week 2 Wed,2.4,CSM;
Admin,Upload metadata; configure,0%\
2.6,SSO Testing,0.5 days,Week 2 Wed,Week 2 Wed,2.5,Admin; IT,Test with
multiple users,0%\
2.7,User Provisioning,1 day,Week 2 Thu,Week 2 Thu,2.6,Admin,Invite all
users via SSO/manual,0%\
2.8,GitHub/GitLab Integration,1 day,Week 2 Thu,Week 2
Fri,2.7,Admin,Connect source control,0%\
2.9,Jira Integration,0.5 days,Week 2 Fri,Week 2 Fri,2.8,Admin,Connect
ticketing system,0%\
2.10,Slack/Teams Integration,0.5 days,Week 2 Fri,Week 2
Fri,2.9,Admin,Configure notifications,0%\
2.11,Week 2 Checkpoint,0.5 hours,Week 2 Fri,Week 2 Fri,2.10,All,Status
review,0%\
2.12,MILESTONE: Technical Setup Complete,0 days,Week 2 Fri,Week 2
Fri,2.11,,,0%\
3,PHASE 3: GOVERNANCE CONFIGURATION,5 days,Week 3 Mon,Week 3
Fri,2.12,,0%\
3.1,Governance Framework Workshop,2 hours,Week 3 Mon,Week 3 Mon,,Gov
Lead; CSM,Define governance approach,0%\
3.2,Configure Risk Classification,1 day,Week 3 Mon,Week 3 Tue,3.1,Gov
Lead; Admin,Set up risk tiers,0%\
3.3,Create Governance Rules,1.5 days,Week 3 Tue,Week 3 Wed,3.2,Gov
Lead,Configure rules per policy,0%\
3.4,Configure Approval Workflows,1 day,Week 3 Wed,Week 3 Thu,3.3,Gov
Lead; Admin,Set up approval chains,0%\
3.5,Compliance Pack Setup,1 day,Week 3 Thu,Week 3 Fri,3.4,Gov Lead;
CSM,Configure EU AI Act/FinServ,0%\
3.6,Test Rules and Workflows,0.5 days,Week 3 Fri,Week 3 Fri,3.5,Gov
Lead,Verify configuration,0%\
3.7,Week 3 Checkpoint,0.5 hours,Week 3 Fri,Week 3 Fri,3.6,All,Status
review,0%\
3.8,MILESTONE: Governance Config Complete,0 days,Week 3 Fri,Week 3
Fri,3.7,,,0%\
4,PHASE 4: PILOT,5 days,Week 4 Mon,Week 4 Fri,3.8,,0%\
4.1,Pilot Owner Training,2 hours,Week 4 Mon,Week 4 Mon,,Pilot Owners;
CSM,Train pilot system owners,0%\
4.2,Register Pilot Systems (5-10),2 days,Week 4 Mon,Week 4 Wed,4.1,Pilot
Owners,Register priority systems,0%\
4.3,Upload Pilot Documentation,1.5 days,Week 4 Wed,Week 4 Thu,4.2,Pilot
Owners,Upload required docs,0%\
4.4,Run Dissonance Analyses,0.5 days,Week 4 Thu,Week 4 Thu,4.3,Pilot
Owners,Analyze all pilot systems,0%\
4.5,Review Pilot Findings,0.5 days,Week 4 Fri,Week 4 Fri,4.4,Gov Lead;
Pilot Owners,Triage dissonances,0%\
4.6,Collect Pilot Feedback,0.5 days,Week 4 Fri,Week 4 Fri,4.5,CSM,Survey
and interviews,0%\
4.7,Refine Configuration,0.5 days,Week 4 Fri,Week 4 Fri,4.6,Gov Lead;
Admin,Adjust based on feedback,0%\
4.8,Week 4 Checkpoint,0.5 hours,Week 4 Fri,Week 4 Fri,4.7,All,Pilot
readout,0%\
4.9,MILESTONE: Pilot Complete,0 days,Week 4 Fri,Week 4 Fri,4.8,,,0%\
5,PHASE 5: FULL ROLLOUT,5 days,Week 5 Mon,Week 5 Fri,4.9,,0%\
5.1,Wave 2 Owner Training,2 hours,Week 5 Mon,Week 5 Mon,,Remaining
Owners; CSM,Train all system owners,0%\
5.2,Register Remaining Systems,3 days,Week 5 Mon,Week 5 Wed,5.1,System
Owners,Register all AI systems,0%\
5.3,Complete Documentation,2 days,Week 5 Wed,Week 5 Thu,5.2,System
Owners,Upload all required docs,0%\
5.4,Run Full Portfolio Analysis,0.5 days,Week 5 Thu,Week 5 Thu,5.3,Gov
Lead,Analyze entire portfolio,0%\
5.5,Address Critical Findings,1 day,Week 5 Thu,Week 5 Fri,5.4,System
Owners,Create action items,0%\
5.6,Generate Initial Reports,0.5 days,Week 5 Fri,Week 5 Fri,5.5,Gov
Lead,Portfolio summary,0%\
5.7,Week 5 Checkpoint,0.5 hours,Week 5 Fri,Week 5 Fri,5.6,All,Status
review,0%\
5.8,MILESTONE: Rollout Complete,0 days,Week 5 Fri,Week 5 Fri,5.7,,,0%\
6,PHASE 6: GO-LIVE & HYPERCARE,5 days,Week 6 Mon,Week 6 Fri,5.8,,0%\
6.1,Final Configuration Validation,0.5 days,Week 6 Mon,Week 6
Mon,,Admin; CSM,Verify all settings,0%\
6.2,Executive Briefing,1 hour,Week 6 Mon,Week 6 Mon,6.1,Executives; Gov
Lead; CSM,Executive overview,0%\
6.3,All-Hands Training,1 hour,Week 6 Tue,Week 6 Tue,6.2,All
Users,Platform training session,0%\
6.4,Go-Live Announcement,0.5 days,Week 6 Tue,Week 6
Tue,6.3,Sponsor,Org-wide communication,0%\
6.5,MILESTONE: GO-LIVE,0 days,Week 6 Tue,Week 6 Tue,6.4,,,0%\
6.6,Hypercare Day 1,1 day,Week 6 Wed,Week 6 Wed,6.5,CSM; Admin,Intensive
support,0%\
6.7,Hypercare Day 2-3,2 days,Week 6 Thu,Week 6 Fri,6.6,CSM;
Admin,Continued support,0%\
6.8,Week 6 Checkpoint,1 hour,Week 6 Fri,Week 6 Fri,6.7,All,Go-live
review,0%\
6.9,MILESTONE: Implementation Complete,0 days,Week 6 Fri,Week 6
Fri,6.8,,,0%\
7,HYPERCARE CONTINUATION,5 days,Week 7 Mon,Week 8 Fri,6.9,,0%\
7.1,Hypercare Week 2,5 days,Week 7 Mon,Week 7 Fri,,CSM; Admin,Ongoing
support,0%\
7.2,Hypercare Exit Review,2 hours,Week 8 Fri,Week 8 Fri,7.1,All;
CSM,Transition to steady state,0%\
7.3,MILESTONE: Hypercare Complete,0 days,Week 8 Fri,Week 8 Fri,7.2,,,0%

**Smartsheet Template Format**

Sheet Name: Phase Mirror Business Implementation\
\
COLUMNS:\
- Task Name (Text)\
- Duration (Duration)\
- Start (Date)\
- End (Date)\
- Predecessors (Text)\
- Assigned To (Contact List)\
- Status (Dropdown: Not Started, In Progress, Complete, Blocked)\
- % Complete (Text)\
- Comments (Text)\
- Phase (Dropdown)\
\
COLUMN PROPERTIES:\
Task Name: Primary Column\
Status Colors: Not Started=Gray, In Progress=Blue, Complete=Green,
Blocked=Red\
% Complete: Display as progress bar\
\
HIERARCHY:\
- Phase 1: Planning (Parent)\
- Kickoff Call with CSM (Child)\
- Stakeholder Alignment Meetings (Child)\
- \[etc.\]\
\
AUTOMATION RULES:\
1. When Status = \"Complete\" → Set % Complete to 100%\
2. When % Complete = 100% → Set Status to \"Complete\"\
3. When Start Date is today → Send notification to Assigned To\
4. When Task is blocked for 2+ days → Send alert to Project Lead

**TEMPLATE 3: ENTERPRISE TIER (12 WEEKS)**

**Visual Gantt Chart**

PHASE MIRROR ENTERPRISE IMPLEMENTATION - 12 WEEK TIMELINE\
═══════════════════════════════════════════════════════════════════════════════════════════════════════════════\
\
WK1 WK2 WK3 WK4 WK5 WK6 WK7 WK8 WK9 WK10 WK11 WK12 WK13 WK14\
────────────────────────────────────────────────────────────────────────────────────────────────────────────────\
\
PHASE 1: FOUNDATION (Weeks 1-3)\
────────────────────────────────────────────────────────────────────────────────────────────────────────────────\
Executive Kickoff ██\
Stakeholder Map ████\
Requirements ██████\
Technical Setup ██████████\
Security Review ██████\
Integrations ████████\
◆ Foundation Complete ◆\
\
PHASE 2: CONFIGURATION (Weeks 4-6)\
────────────────────────────────────────────────────────────────────────────────────────────────────────────────\
Governance Workshop ██\
Risk Classification ████\
Governance Rules ████████\
Approval Workflows ██████\
Compliance Packs ████████\
Custom Reports ████████\
◆ Configuration Complete ◆\
\
PHASE 3: PILOT (Weeks 7-8)\
────────────────────────────────────────────────────────────────────────────────────────────────────────────────\
Pilot Training ██\
Pilot Registration ████████\
Pilot Validation ████████\
Pilot Feedback ████\
◆ Pilot Complete ◆\
\
PHASE 4: ROLLOUT (Weeks 9-11)\
────────────────────────────────────────────────────────────────────────────────────────────────────────────────\
Wave 1: Critical ██████████\
Wave 2: High ██████████\
Wave 3: Medium ██████████\
◆ Rollout Complete ◆\
\
PHASE 5: GO-LIVE & STABILIZATION (Week 12+)\
────────────────────────────────────────────────────────────────────────────────────────────────────────────────\
Final Validation ██\
Executive Training ██\
GO-LIVE ◆\
Hypercare ████████████████\
◆ Implementation Complete ◆\
────────────────────────────────────────────────────────────────────────────────────────────────────────────────

**Detailed Task List (CSV Format)**

WBS,Task
Name,Duration,Start,Finish,Predecessors,Resource,Status,Priority,Risk,Notes\
1,PHASE 1: FOUNDATION,15 days,Week 1 Day 1,Week 3 Day 5,,,,,,\
1.1,Week 1: Discovery & Planning,5 days,Week 1 Day 1,Week 1 Day 5,,,,,,\
1.1.1,Executive Kickoff Meeting,2 hours,Week 1 Day 1,Week 1 Day 1,,Exec
Sponsor; C-Suite; PM Team,Not Started,High,,2-hour structured kickoff\
1.1.2,Stakeholder Mapping Workshop,4 hours,Week 1 Day 2,Week 1 Day
2,1.1.1,Project Lead; PM,Not Started,High,,Identify all stakeholders\
1.1.3,Create RACI Matrix,2 hours,Week 1 Day 2,Week 1 Day 2,1.1.2,Project
Lead,Not Started,Medium,,Document responsibilities\
1.1.4,Technical Requirements Gathering,4 hours,Week 1 Day 3,Week 1 Day
3,1.1.3,IT; Security; PM,Not Started,High,,Gather technical needs\
1.1.5,Governance Requirements Gathering,4 hours,Week 1 Day 4,Week 1 Day
4,1.1.4,Compliance; Risk; PM,Not Started,High,,Gather governance needs\
1.1.6,Project Plan Review,2 hours,Week 1 Day 5,Week 1 Day
5,1.1.5,Project Lead; PM,Not Started,Medium,,Finalize timeline\
1.1.7,Week 1 Steering Committee,1 hour,Week 1 Day 5,Week 1 Day
5,1.1.6,Steering Committee,Not Started,High,,Weekly status\
1.1.8,MILESTONE: Discovery Complete,0 days,Week 1 Day 5,Week 1 Day
5,1.1.7,,,,,,\
1.2,Week 2: Technical Foundation,5 days,Week 2 Day 1,Week 2 Day
5,1.1.8,,,,,\
1.2.1,Dedicated Instance Provisioning,1 day,Week 2 Day 1,Week 2 Day
1,,PM,Not Started,High,,Request dedicated environment\
1.2.2,Custom Domain Configuration,0.5 days,Week 2 Day 1,Week 2 Day
1,1.2.1,PM,Not Started,Medium,,Configure \[company\].phasemirror.com\
1.2.3,SSL Certificate Setup,0.5 days,Week 2 Day 2,Week 2 Day 2,1.2.2,IT;
PM,Not Started,Medium,,Install SSL certificate\
1.2.4,Initial Admin Account Setup,0.5 days,Week 2 Day 2,Week 2 Day
2,1.2.3,Admin,Not Started,High,,Configure admin access\
1.2.5,SSO Design Session,2 hours,Week 2 Day 2,Week 2 Day 2,1.2.4,IT;
Admin; PM,Not Started,High,,Plan SSO approach\
1.2.6,IdP Application Creation,1 day,Week 2 Day 3,Week 2 Day
3,1.2.5,IT,Not Started,High,,Create app in Okta/Azure AD\
1.2.7,SAML/OIDC Configuration,1 day,Week 2 Day 4,Week 2 Day 4,1.2.6,IT;
PM,Not Started,High,,Configure SSO in PM\
1.2.8,SSO Testing,0.5 days,Week 2 Day 4,Week 2 Day 4,1.2.7,IT; Admin,Not
Started,High,,Test SSO login\
1.2.9,SCIM Provisioning Setup,1 day,Week 2 Day 5,Week 2 Day 5,1.2.8,IT;
PM,Not Started,Medium,,Automated user provisioning\
1.2.10,Admin Training,2 hours,Week 2 Day 5,Week 2 Day 5,1.2.9,Admins;
PM,Not Started,Medium,,Train administrators\
1.2.11,Week 2 Steering Committee,1 hour,Week 2 Day 5,Week 2 Day
5,1.2.10,Steering Committee,Not Started,High,,Weekly status\
1.2.12,MILESTONE: Technical Foundation Complete,0 days,Week 2 Day 5,Week
2 Day 5,1.2.11,,,,,,\
1.3,Week 3: Security & Integration,5 days,Week 3 Day 1,Week 3 Day
5,1.2.12,,,,,\
1.3.1,Security Review Meeting,2 hours,Week 3 Day 1,Week 3 Day
1,,Security; PM,Not Started,High,,Review security requirements\
1.3.2,Security Questionnaire Review,1 day,Week 3 Day 1,Week 3 Day
2,1.3.1,Security,Not Started,High,,Complete security assessment\
1.3.3,Penetration Test Coordination,1 day,Week 3 Day 2,Week 3 Day
3,1.3.2,Security; PM,Not Started,Medium,,Schedule if required\
1.3.4,Integration Architecture Design,2 hours,Week 3 Day 3,Week 3 Day
3,1.3.3,IT; PM,Not Started,High,,Design integration approach\
1.3.5,GitHub Enterprise Integration,1 day,Week 3 Day 3,Week 3 Day
4,1.3.4,IT; Admin,Not Started,High,,Connect source control\
1.3.6,ServiceNow Integration,1 day,Week 3 Day 4,Week 3 Day 5,1.3.5,IT;
Admin,Not Started,Medium,,Connect ticketing\
1.3.7,Splunk/SIEM Integration,0.5 days,Week 3 Day 5,Week 3 Day
5,1.3.6,IT; Security,Not Started,Medium,,Security monitoring\
1.3.8,Integration Testing,0.5 days,Week 3 Day 5,Week 3 Day
5,1.3.7,Admin,Not Started,High,,Verify all integrations\
1.3.9,Week 3 Steering Committee,1 hour,Week 3 Day 5,Week 3 Day
5,1.3.8,Steering Committee,Not Started,High,,Weekly status\
1.3.10,Phase 1 Checkpoint Meeting,2 hours,Week 3 Day 5,Week 3 Day
5,1.3.9,Stakeholders; PM,Not Started,High,,Phase gate review\
1.3.11,MILESTONE: Foundation Phase Complete,0 days,Week 3 Day 5,Week 3
Day 5,1.3.10,,,,,,\
2,PHASE 2: CONFIGURATION,15 days,Week 4 Day 1,Week 6 Day 5,1.3.11,,,,,\
2.1,Week 4: Governance Design,5 days,Week 4 Day 1,Week 4 Day 5,,,,,,\
2.1.1,Governance Design Workshop,4 hours,Week 4 Day 1,Week 4 Day 1,,Gov
Lead; Compliance; Risk; PM,Not Started,High,,Define governance
framework\
2.1.2,Policy-to-Rule Mapping,1 day,Week 4 Day 1,Week 4 Day 2,2.1.1,Gov
Lead; PM,Not Started,High,,Map existing policies\
2.1.3,Risk Classification Design,1 day,Week 4 Day 2,Week 4 Day
3,2.1.2,Gov Lead; Risk,Not Started,High,,Define risk tiers\
2.1.4,Risk Classification Configuration,0.5 days,Week 4 Day 3,Week 4 Day
3,2.1.3,Gov Lead; Admin,Not Started,High,,Configure in platform\
2.1.5,Approval Workflow Design,1 day,Week 4 Day 3,Week 4 Day 4,2.1.4,Gov
Lead,Not Started,High,,Design approval flows\
2.1.6,Documentation Requirements,0.5 days,Week 4 Day 4,Week 4 Day
4,2.1.5,Gov Lead,Not Started,Medium,,Define required docs\
2.1.7,Week 4 Steering Committee,1 hour,Week 4 Day 5,Week 4 Day
5,2.1.6,Steering Committee,Not Started,High,,Weekly status\
2.1.8,MILESTONE: Governance Design Complete,0 days,Week 4 Day 5,Week 4
Day 5,2.1.7,,,,,,\
2.2,Week 5: Rule Configuration,5 days,Week 5 Day 1,Week 5 Day
5,2.1.8,,,,,\
2.2.1,Configure Documentation Rules,1 day,Week 5 Day 1,Week 5 Day 1,,Gov
Lead,Not Started,High,,Required docs per tier\
2.2.2,Configure Approval Rules,1 day,Week 5 Day 2,Week 5 Day 2,2.2.1,Gov
Lead,Not Started,High,,Approval triggers\
2.2.3,Configure Review Rules,0.5 days,Week 5 Day 2,Week 5 Day
2,2.2.2,Gov Lead,Not Started,Medium,,Periodic reviews\
2.2.4,Configure Monitoring Rules,0.5 days,Week 5 Day 3,Week 5 Day
3,2.2.3,Gov Lead,Not Started,Medium,,Monitoring requirements\
2.2.5,Approval Workflow Configuration,1 day,Week 5 Day 3,Week 5 Day
4,2.2.4,Gov Lead; Admin,Not Started,High,,Build workflows\
2.2.6,Notification Configuration,0.5 days,Week 5 Day 4,Week 5 Day
4,2.2.5,Admin,Not Started,Medium,,Set up alerts\
2.2.7,Rule Testing,1 day,Week 5 Day 4,Week 5 Day 5,2.2.6,Gov Lead,Not
Started,High,,Test all rules\
2.2.8,Week 5 Steering Committee,1 hour,Week 5 Day 5,Week 5 Day
5,2.2.7,Steering Committee,Not Started,High,,Weekly status\
2.2.9,MILESTONE: Rules Complete,0 days,Week 5 Day 5,Week 5 Day
5,2.2.8,,,,,,\
2.3,Week 6: Compliance & Custom,5 days,Week 6 Day 1,Week 6 Day
5,2.2.9,,,,,\
2.3.1,EU AI Act Pack Configuration,1 day,Week 6 Day 1,Week 6 Day 1,,Gov
Lead; PM,Not Started,High,,If applicable\
2.3.2,Financial Services Pack Configuration,1 day,Week 6 Day 2,Week 6
Day 2,2.3.1,Gov Lead; PM,Not Started,High,,If applicable\
2.3.3,Custom Report Configuration,1 day,Week 6 Day 3,Week 6 Day
3,2.3.2,Gov Lead,Not Started,Medium,,Custom dashboards\
2.3.4,Dashboard Configuration,0.5 days,Week 6 Day 4,Week 6 Day
4,2.3.3,Gov Lead,Not Started,Medium,,Executive views\
2.3.5,Documentation Templates,0.5 days,Week 6 Day 4,Week 6 Day
4,2.3.4,Gov Lead,Not Started,Medium,,Upload templates\
2.3.6,End-to-End Configuration Testing,1 day,Week 6 Day 4,Week 6 Day
5,2.3.5,Gov Lead; Admin,Not Started,High,,Full system test\
2.3.7,Week 6 Steering Committee,1 hour,Week 6 Day 5,Week 6 Day
5,2.3.6,Steering Committee,Not Started,High,,Weekly status\
2.3.8,Phase 2 Checkpoint Meeting,2 hours,Week 6 Day 5,Week 6 Day
5,2.3.7,Stakeholders; PM,Not Started,High,,Phase gate review\
2.3.9,MILESTONE: Configuration Phase Complete,0 days,Week 6 Day 5,Week 6
Day 5,2.3.8,,,,,,\
3,PHASE 3: PILOT,10 days,Week 7 Day 1,Week 8 Day 5,2.3.9,,,,,\
3.1,Week 7: Pilot Execution,5 days,Week 7 Day 1,Week 7 Day 5,,,,,,\
3.1.1,Pilot Kickoff Meeting,1 hour,Week 7 Day 1,Week 7 Day 1,,Pilot
Owners; PM,Not Started,High,,Launch pilot\
3.1.2,Pilot Owner Training,2 hours,Week 7 Day 1,Week 7 Day 1,3.1.1,Pilot
Owners; PM,Not Started,High,,Training session\
3.1.3,Register Pilot Systems (15-20),2 days,Week 7 Day 1,Week 7 Day
3,3.1.2,Pilot Owners,Not Started,High,,Register systems\
3.1.4,Upload Pilot Documentation,1.5 days,Week 7 Day 3,Week 7 Day
4,3.1.3,Pilot Owners,Not Started,High,,Upload docs\
3.1.5,Run Dissonance Analyses,0.5 days,Week 7 Day 4,Week 7 Day
4,3.1.4,Pilot Owners,Not Started,High,,Analyze systems\
3.1.6,Initial Findings Review,0.5 days,Week 7 Day 5,Week 7 Day
5,3.1.5,Gov Lead; Pilot Owners,Not Started,High,,Review findings\
3.1.7,Week 7 Steering Committee,1 hour,Week 7 Day 5,Week 7 Day
5,3.1.6,Steering Committee,Not Started,High,,Weekly status\
3.1.8,MILESTONE: Pilot Systems Live,0 days,Week 7 Day 5,Week 7 Day
5,3.1.7,,,,,,\
3.2,Week 8: Pilot Validation,5 days,Week 8 Day 1,Week 8 Day
5,3.1.8,,,,,\
3.2.1,Workflow Testing,1 day,Week 8 Day 1,Week 8 Day 1,,Pilot Team,Not
Started,High,,Test approvals\
3.2.2,Integration Validation,0.5 days,Week 8 Day 2,Week 8 Day
2,3.2.1,Pilot Team; IT,Not Started,Medium,,Verify integrations\
3.2.3,User Feedback Collection,1 day,Week 8 Day 2,Week 8 Day
3,3.2.2,PM,Not Started,High,,Surveys/interviews\
3.2.4,Configuration Refinement,1 day,Week 8 Day 3,Week 8 Day 4,3.2.3,Gov
Lead; Admin,Not Started,Medium,,Adjust based on feedback\
3.2.5,Pilot Readout Preparation,0.5 days,Week 8 Day 4,Week 8 Day
4,3.2.4,PM,Not Started,High,,Prepare presentation\
3.2.6,Pilot Readout Meeting,2 hours,Week 8 Day 5,Week 8 Day
5,3.2.5,Stakeholders; PM,Not Started,High,,Present pilot results\
3.2.7,Go/No-Go Decision,1 hour,Week 8 Day 5,Week 8 Day 5,3.2.6,Steering
Committee,Not Started,Critical,,Decide on rollout\
3.2.8,Week 8 Steering Committee,1 hour,Week 8 Day 5,Week 8 Day
5,3.2.7,Steering Committee,Not Started,High,,Weekly status\
3.2.9,MILESTONE: Pilot Complete - Go Decision,0 days,Week 8 Day 5,Week 8
Day 5,3.2.8,,,,,,\
4,PHASE 4: ROLLOUT,15 days,Week 9 Day 1,Week 11 Day 5,3.2.9,,,,,\
4.1,Week 9: Wave 1 - Critical Systems,5 days,Week 9 Day 1,Week 9 Day
5,,,,,,\
4.1.1,Wave 1 Training,2 hours,Week 9 Day 1,Week 9 Day 1,,Critical
Owners; PM,Not Started,High,,Train owners\
4.1.2,Register Critical Systems (30-50),3 days,Week 9 Day 1,Week 9 Day
4,4.1.1,System Owners,Not Started,Critical,,Register systems\
4.1.3,Documentation Upload,2 days,Week 9 Day 3,Week 9 Day 5,4.1.2,System
Owners,Not Started,High,,Upload docs\
4.1.4,Analysis and Triage,1 day,Week 9 Day 4,Week 9 Day 5,4.1.3,Gov
Lead; Owners,Not Started,High,,Review findings\
4.1.5,Week 9 Steering Committee,1 hour,Week 9 Day 5,Week 9 Day
5,4.1.4,Steering Committee,Not Started,High,,Weekly status\
4.1.6,MILESTONE: Wave 1 Complete,0 days,Week 9 Day 5,Week 9 Day
5,4.1.5,,,,,,\
4.2,Week 10: Wave 2 - High Risk Systems,5 days,Week 10 Day 1,Week 10 Day
5,4.1.6,,,,,\
4.2.1,Wave 2 Training,2 hours,Week 10 Day 1,Week 10 Day 1,,High Risk
Owners; PM,Not Started,High,,Train owners\
4.2.2,Register High Risk Systems (50-100),3 days,Week 10 Day 1,Week 10
Day 4,4.2.1,System Owners,Not Started,High,,Register systems\
4.2.3,Documentation Upload,2 days,Week 10 Day 3,Week 10 Day
5,4.2.2,System Owners,Not Started,High,,Upload docs\
4.2.4,Analysis and Triage,1 day,Week 10 Day 4,Week 10 Day 5,4.2.3,Gov
Lead; Owners,Not Started,High,,Review findings\
4.2.5,Week 10 Steering Committee,1 hour,Week 10 Day 5,Week 10 Day
5,4.2.4,Steering Committee,Not Started,High,,Weekly status\
4.2.6,MILESTONE: Wave 2 Complete,0 days,Week 10 Day 5,Week 10 Day
5,4.2.5,,,,,,\
4.3,Week 11: Wave 3 - Medium/Low Risk,5 days,Week 11 Day 1,Week 11 Day
5,4.2.6,,,,,\
4.3.1,Wave 3 Training,2 hours,Week 11 Day 1,Week 11 Day 1,,Remaining
Owners; PM,Not Started,Medium,,Train owners\
4.3.2,Register Remaining Systems (50+),3 days,Week 11 Day 1,Week 11 Day
4,4.3.1,System Owners,Not Started,Medium,,Register systems\
4.3.3,Documentation Upload,2 days,Week 11 Day 3,Week 11 Day
5,4.3.2,System Owners,Not Started,Medium,,Upload docs\
4.3.4,Full Portfolio Analysis,1 day,Week 11 Day 4,Week 11 Day
5,4.3.3,Gov Lead,Not Started,High,,Analyze portfolio\
4.3.5,Week 11 Steering Committee,1 hour,Week 11 Day 5,Week 11 Day
5,4.3.4,Steering Committee,Not Started,High,,Weekly status\
4.3.6,Phase 4 Checkpoint Meeting,2 hours,Week 11 Day 5,Week 11 Day
5,4.3.5,Stakeholders; PM,Not Started,High,,Phase gate review\
4.3.7,MILESTONE: Rollout Phase Complete,0 days,Week 11 Day 5,Week 11 Day
5,4.3.6,,,,,,\
5,PHASE 5: GO-LIVE & STABILIZATION,10+ days,Week 12 Day 1,Week 14 Day
5,4.3.7,,,,,\
5.1,Week 12: Go-Live,5 days,Week 12 Day 1,Week 12 Day 5,,,,,,\
5.1.1,Final Configuration Validation,0.5 days,Week 12 Day 1,Week 12 Day
1,,Admin; PM,Not Started,Critical,,Final checks\
5.1.2,Go/No-Go Meeting,1 hour,Week 12 Day 1,Week 12 Day 1,5.1.1,Steering
Committee,Not Started,Critical,,Final decision\
5.1.3,Executive Training,1 hour,Week 12 Day 2,Week 12 Day
2,5.1.2,Executives; Gov Lead; PM,Not Started,High,,Exec overview\
5.1.4,Go-Live Announcement,0.5 days,Week 12 Day 3,Week 12 Day
3,5.1.3,Exec Sponsor,Not Started,High,,Org-wide comms\
5.1.5,All-Hands Training Session 1,1 hour,Week 12 Day 3,Week 12 Day
3,5.1.4,Users Group 1,Not Started,High,,Training\
5.1.6,All-Hands Training Session 2,1 hour,Week 12 Day 3,Week 12 Day
3,5.1.5,Users Group 2,Not Started,High,,Training\
5.1.7,All-Hands Training Session 3,1 hour,Week 12 Day 3,Week 12 Day
3,5.1.6,Users Group 3,Not Started,High,,Training\
5.1.8,MILESTONE: GO-LIVE,0 days,Week 12 Day 3,Week 12 Day 3,5.1.7,,,,,,\
5.1.9,Hypercare Day 1,1 day,Week 12 Day 4,Week 12 Day 4,5.1.8,PM; CSM;
Admin,Not Started,Critical,,Intensive support\
5.1.10,Hypercare Day 2-3,2 days,Week 12 Day 4,Week 12 Day 5,5.1.9,PM;
CSM; Admin,Not Started,High,,Support\
5.1.11,Week 12 Status,1 hour,Week 12 Day 5,Week 12 Day 5,5.1.10,Steering
Committee,Not Started,High,,Go-live review\
5.1.12,MILESTONE: Go-Live Week Complete,0 days,Week 12 Day 5,Week 12 Day
5,5.1.11,,,,,,\
5.2,Weeks 13-14: Hypercare,10 days,Week 13 Day 1,Week 14 Day
5,5.1.12,,,,,\
5.2.1,Daily Check-ins,5 days,Week 13 Day 1,Week 13 Day 5,,PM; Project
Lead,Not Started,High,,Daily standups\
5.2.2,Issue Resolution,Ongoing,Week 13 Day 1,Week 14 Day 5,5.2.1,All,Not
Started,High,,Fix issues\
5.2.3,Office Hours,4 sessions,Week 13-14,Week 13-14,,PM; Admin,Not
Started,Medium,,User support\
5.2.4,Week 13 Status,1 hour,Week 13 Day 5,Week 13 Day 5,5.2.3,Steering
Committee,Not Started,High,,Weekly status\
5.2.5,Hypercare Week 2,5 days,Week 14 Day 1,Week 14 Day 5,5.2.4,PM;
Admin,Not Started,Medium,,Continued support\
5.2.6,Hypercare Exit Review,2 hours,Week 14 Day 5,Week 14 Day
5,5.2.5,Stakeholders; PM,Not Started,High,,Transition review\
5.2.7,TAM Handoff,1 hour,Week 14 Day 5,Week 14 Day 5,5.2.6,PM; TAM,Not
Started,High,,Introduce TAM\
5.2.8,Documentation Handoff,0.5 days,Week 14 Day 5,Week 14 Day
5,5.2.7,PM; Project Lead,Not Started,Medium,,Transfer docs\
5.2.9,Week 14 Steering Committee,1 hour,Week 14 Day 5,Week 14 Day
5,5.2.8,Steering Committee,Not Started,High,,Final status\
5.2.10,MILESTONE: Implementation Complete,0 days,Week 14 Day 5,Week 14
Day 5,5.2.9,,,,,,

**TOOL-SPECIFIC IMPORT INSTRUCTIONS**

**Microsoft Project Import**

STEP-BY-STEP IMPORT:\
\
1. Download the .xml or .mpp template file\
2. Open Microsoft Project\
3. File → Open → Select template file\
4. Adjust start date:\
- Project → Project Information\
- Set \"Start Date\" to your actual start date\
5. Assign resources:\
- View → Resource Sheet\
- Add your team members\
- Return to Gantt Chart view\
- Double-click tasks to assign resources\
6. Save as new project file\
\
RECOMMENDED VIEWS:\
- Gantt Chart (default)\
- Timeline (for executive view)\
- Resource Usage (for capacity)\
- Tracking Gantt (during execution)

**Smartsheet Import**

STEP-BY-STEP IMPORT:\
\
1. Download the .xlsx template file\
2. Log into Smartsheet\
3. Click \"+ Create\" → \"Import\"\
4. Select \"Microsoft Excel\"\
5. Upload the .xlsx file\
6. Configure column mapping:\
- Task Name → Primary Column\
- Duration → Duration\
- Start → Start Date\
- End → End Date\
- Predecessors → Predecessors\
- Assigned To → Contact List\
7. Click \"Import\"\
8. After import:\
- Right-click header → \"Edit Column Properties\"\
- Enable \"Project Settings\" for the sheet\
- Set dependencies to \"Predecessors\" column\
- Enable \"Gantt View\"\
\
SMARTSHEET FEATURES TO ENABLE:\
- Gantt Chart (View → Gantt View)\
- Dependencies (right-click → Enable Dependencies)\
- Critical Path (Gantt settings → Show Critical Path)\
- Baseline (Project Settings → Save Baseline)

**Asana Import**

STEP-BY-STEP IMPORT:\
\
1. Download the .csv template file\
2. Log into Asana\
3. Create new project or open existing\
4. Click dropdown arrow → \"Import\" → \"CSV\"\
5. Upload the .csv file\
6. Map columns:\
- Task Name → Task name\
- Start → Start date\
- Finish → Due date\
- Assigned To → Assignee\
- Section → Section (if using sections)\
7. Click \"Go to project\"\
8. Enable Timeline view:\
- Click \"Timeline\" tab\
- Adjust task bars as needed\
- Add dependencies by connecting tasks\
\
ASANA SETUP TIPS:\
- Create sections for each phase\
- Use milestones (tasks with due dates only)\
- Set up custom fields for Status, Priority\
- Enable project status updates

**[[Monday.com]{.underline}](http://Monday.com) Import**

STEP-BY-STEP IMPORT:\
\
1. Download the .xlsx template file\
2. Log into Monday.com\
3. Create new board or click \"+\" to add board\
4. Click menu (⋯) → \"Import data\" → \"Excel/CSV\"\
5. Upload the .xlsx file\
6. Map columns to Monday columns:\
- Task Name → Name (first column)\
- Duration → Numbers column\
- Start → Date column\
- Assigned To → People column\
- Status → Status column\
7. Click \"Import\"\
8. Enable Gantt view:\
- Click \"+ Add View\" → \"Gantt\"\
- Configure date columns\
- Set up dependencies\
\
MONDAY.COM CONFIGURATION:\
- Add \"Timeline\" column for Gantt\
- Create \"Milestone\" status\
- Set up automations for notifications\
- Configure dashboard for overview

**Jira Import**

STEP-BY-STEP IMPORT:\
\
1. Download the .csv template file\
2. Log into Jira\
3. Go to Project Settings → \"External System Import\" → \"CSV\"\
4. Upload the .csv file\
5. Map fields:\
- Task Name → Summary\
- Description → Description\
- Assigned To → Assignee\
- Start → Custom field (Start Date)\
- Finish → Due Date\
- Priority → Priority\
6. Import tasks\
7. Configure timeline:\
- Install \"Advanced Roadmaps\" or use built-in Timeline\
- Link issues with dependencies\
- Create Epics for phases\
\
JIRA STRUCTURE:\
- Epic = Phase (e.g., \"Phase 1: Foundation\")\
- Story/Task = Individual tasks\
- Sub-task = Sub-items if needed\
- Use labels for categorization\
\
DEPENDENCIES IN JIRA:\
- Use \"is blocked by\" link type\
- Or install \"Structure\" or \"BigPicture\" add-on

**ClickUp Import**

STEP-BY-STEP IMPORT:\
\
1. Download the .csv template file\
2. Log into ClickUp\
3. Navigate to Space/Folder\
4. Click \"⋯\" → \"Import/Export\" → \"Import\"\
5. Select \"CSV\"\
6. Upload the .csv file\
7. Map columns:\
- Task Name → Task name\
- Start → Start date\
- Finish → Due date\
- Assigned To → Assignee\
- Status → Status\
8. Click \"Import\"\
9. Enable Gantt view:\
- Click \"View\" → \"Add View\" → \"Gantt\"\
- Configure dependencies\
- Set critical path\
\
CLICKUP CONFIGURATION:\
- Create List for each phase\
- Use Milestones (task with due date = start date)\
- Enable time tracking\
- Set up automations

**RESOURCE PLANNING COMPANION**

**Resource Allocation Matrix**

PHASE MIRROR ENTERPRISE - RESOURCE REQUIREMENTS\
\
┌──────────────────────────────────────────────────────────────────────────────────────────┐\
│ RESOURCE ALLOCATION BY PHASE │\
├──────────────────────────────────────────────────────────────────────────────────────────┤\
│ │\
│ ROLE │ WK1-3 │ WK4-6 │ WK7-8 │ WK9-11 │ WK12 │ WK13-14│ TOTAL │\
│ │ Found │ Config │ Pilot │Rollout │Go-Live │Hypercare│ │\
├─────────────────────────┼────────┼────────┼────────┼────────┼────────┼────────┼─────────┤\
│ Executive Sponsor │ 2h │ 1h │ 1h │ 1h │ 2h │ 1h │ 8h │\
│ Project Lead │ 20h │ 15h │ 15h │ 20h │ 20h │ 10h │ 100h │\
│ Administrator │ 30h │ 20h │ 5h │ 10h │ 15h │ 10h │ 90h │\
│ Governance Lead │ 5h │ 35h │ 15h │ 20h │ 10h │ 5h │ 90h │\
│ IT / Security │ 25h │ 5h │ 2h │ 2h │ 2h │ 2h │ 38h │\
│ System Owners (each) │ 0h │ 0h │ 4h │ 6h │ 2h │ 1h │ 13h │\
│ Phase Mirror CSM │ 15h │ 15h │ 10h │ 8h │ 15h │ 10h │ 73h │\
│ Phase Mirror PM │ 25h │ 20h │ 15h │ 15h │ 20h │ 15h │ 110h │\
├─────────────────────────┴────────┴────────┴────────┴────────┴────────┴────────┴─────────┤\
│ │\
│ TEAM AVAILABILITY REQUIREMENTS: │\
│ │\
│ Phase 1: Foundation - Admin: 50% availability │\
│ - IT: 25% availability │\
│ - Project Lead: 50% availability │\
│ │\
│ Phase 2: Configuration - Governance Lead: 75% availability │\
│ - Admin: 50% availability │\
│ │\
│ Phase 3: Pilot - Pilot Owners: 20% availability (5-10 people) │\
│ - Governance Lead: 40% availability │\
│ │\
│ Phase 4: Rollout - System Owners: 15% availability (20-50 people) │\
│ - Project Lead: 50% availability │\
│ │\
│ Phase 5: Go-Live - All roles: Available for training and support │\
│ - Admin: 75% availability first week │\
│ │\
└──────────────────────────────────────────────────────────────────────────────────────────┘

**Milestone Checklist Template**

PHASE MIRROR IMPLEMENTATION - MILESTONE CHECKLIST\
\
MILESTONE: \[Name\]\
Date: \[Target Date\]\
Owner: \[Responsible Person\]\
\
PRE-MILESTONE CHECKLIST:\
☐ All predecessor tasks complete\
☐ Deliverables reviewed and accepted\
☐ Stakeholder sign-off obtained\
☐ Risks mitigated or accepted\
☐ Issues resolved or escalated\
\
MILESTONE CRITERIA:\
☐ \[Specific criterion 1\]\
☐ \[Specific criterion 2\]\
☐ \[Specific criterion 3\]\
\
MILESTONE EVIDENCE:\
☐ \[Document/artifact 1\]\
☐ \[Document/artifact 2\]\
☐ \[Screenshot/recording\]\
\
SIGN-OFF:\
☐ Project Lead: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\
☐ Sponsor: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date:
\_\_\_\_\_\_\_\
☐ CSM: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date:
\_\_\_\_\_\_\_\
\
MILESTONE STATUS: ☐ Achieved ☐ Deferred ☐ At Risk\
\
Notes:\
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**RISK TRACKING TEMPLATE**

Risk ID,Risk Description,Category,Probability,Impact,Risk
Score,Mitigation Strategy,Owner,Status,Date Identified,Target
Resolution\
R001,SSO configuration delays due to IT resource
constraints,Technical,Medium,High,6,Engage IT early; have backup manual
provisioning plan,Admin,Open,Week 1,Week 2\
R002,Insufficient documentation for AI
systems,Process,High,Medium,6,Provide templates; prioritize critical
systems first,Project Lead,Open,Week 1,Week 5\
R003,Stakeholder resistance to new governance process,Change
Mgmt,Medium,High,6,Executive sponsorship; clear communication of
benefits,Sponsor,Open,Week 1,Ongoing\
R004,Integration with legacy systems
fails,Technical,Low,High,4,Technical POC in Week 3; have manual
workarounds,IT Lead,Open,Week 1,Week 3\
R005,Pilot users too busy to participate,Resource,Medium,Medium,4,Select
engaged pilot users; executive mandate,Project Lead,Open,Week 1,Week 7\
R006,Compliance pack configuration more complex than
expected,Technical,Medium,Medium,4,CSM guidance; phased compliance
implementation,Gov Lead,Open,Week 3,Week 6\
R007,Go-live date conflicts with other
initiatives,Schedule,Low,High,4,Early calendar alignment; flexible
go-live window,Sponsor,Open,Week 1,Week 10\
R008,User adoption lower than expected post
go-live,Adoption,Medium,High,6,Training; quick wins; executive
reinforcement,Project Lead,Open,Week 1,Week 14

**END OF GANTT CHART TEMPLATES**

These templates are ready to import into your project management tool of
choice. Would you like me to create:

-   Detailed work breakdown structures for specific phases

-   Meeting agenda templates for each checkpoint

-   Status report templates for steering committees

-   Risk and issue log templates

-   Change request process templates?

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

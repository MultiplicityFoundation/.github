---
slug: phase-mirror-license-elv2-style
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 00-foundations/phase-mirror/Phase Mirror License (ELv2-Style).md
  last_synced: '2026-03-20T17:17:22.042545Z'
---

Phase Mirror License (ELv2-Style)
Based on the Elastic License 2.0 structure, here's a clean, minimal license for the Phase Mirror
Protocol: [1]

  PHASE MIRROR LICENSE
  Version 1.0, January 2026

  Acceptance
  ----------
  By using the software, you agree to all of the terms and conditions below.



  Copyright License
  -----------------
  The licensor grants you a non-exclusive, royalty-free, worldwide,
  non-sublicensable, non-transferable license to use, copy, distribute,
  make available, and prepare derivative works of the software, in each
  case subject to the limitations below.



  Limitations
  -----------
  You may not provide the software to third parties as a hosted or managed
  service, where the service provides users with access to any substantial
  set of the features or functionality of the software.

  You may not alter, remove, or obscure any licensing, copyright, or other
  notices of the licensor in the software. Any use of the licensor's
  trademarks is subject to applicable law.



  Patents
  -------
  The licensor grants you a license, under any patent claims the licensor
  can license, or becomes able to license, to make, have made, use, sell,
  offer for sale, import and have imported the software, in each case
  subject to the limitations in this license. This license does not cover
  any patent claims that you cause to be infringed by modifications or
  additions to the software.

  If you or your company make any written claim that the software infringes
  or contributes to infringement of any patent, your patent license for the
  software granted under these terms ends immediately. If your company makes
  such a claim, your patent license ends immediately for work on behalf of
  your company.
Notices
-------
You must ensure that anyone who gets a copy of any part of the software
from you also gets a copy of these terms.

If you modify the software, you must include in any modified copies of
the software prominent notices stating that you have modified the software.



No Other Rights
---------------
These terms do not imply any licenses other than those expressly granted
in these terms.



Termination
-----------
If you use the software in violation of these terms, such use is not
licensed, and your licenses will automatically terminate. If the licensor
provides you with a notice of your violation, and you cease all violation
of this license no later than 30 days after you receive that notice, your
licenses will be reinstated retroactively. However, if you violate these
terms after such reinstatement, any additional violation of these terms
will cause your licenses to terminate automatically and permanently.



No Liability
------------
As far as the law allows, the software comes as is, without any warranty
or condition, and the licensor will not be liable to you for any damages
arising out of these terms or the use or nature of the software, under
any kind of legal claim.



Definitions
-----------
The "licensor" is the entity offering these terms, and the "software" is
the software the licensor makes available under these terms, including
any portion of it.

"You" refers to the individual or entity agreeing to these terms.

"Your company" is any legal entity, sole proprietorship, or other kind
of organization that you work for, plus all organizations that have
control over, are under the control of, or are under common control with
that organization.

"Control" means ownership of substantially all the assets of an entity,
or the power to direct its management and policies by vote, contract, or
otherwise. Control can be direct or indirect.

"Your licenses" are all the licenses granted to you for the software
under these terms.

"Use" means anything you do with the software requiring one of your
  licenses.

  "Trademark" means trademarks, service marks, and similar rights.




What's Allowed vs. Not Allowed
                  Use Case                    Allowed?                           Notes

  Internal use at your company                ✅ Yes      Use freely for any internal purpose [1]

  Build application on top of Phase Mirror    ✅ Yes      Embed in your SaaS or product

  Modify the source code                      ✅ Yes      Must include prominent modification notices

  Redistribute with your application          ✅ Yes      Must include license terms

  Contractor setting up for clients           ✅ Yes      Client operates it, not you as a service

  Show limited dashboards/outputs to
                                              ✅ Yes      Not "substantial functionality"
  users

                                                         Users interact with your app, not Phase Mirror
  Operate internally to power your services   ✅ Yes
                                                         directly

  Provide Phase Mirror as a managed
                                              ❌ No       Users would access substantial functionality
  service

  Remove copyright/license notices            ❌ No       Must preserve all notices

  Remove or obscure trademarks                ❌ No       "Phase Mirror", "QAGI" must remain


FAQ: Phase Mirror License Examples
I'm using Phase Mirror internally to audit my AI systems.
✅ Permitted. Internal use is always allowed.

I'm a consultant implementing Phase Mirror for my clients.
✅ Permitted. Your client installs and operates the software, you don't provide it as a service.

My SaaS product uses Phase Mirror to generate governance reports for users.
✅ Permitted. Users interact with your application, not Phase Mirror directly. The output (reports)
is your product.
I'm building a plugin that extends Phase Mirror functionality.
✅ Permitted. Derivative works are allowed under the same license terms.

I want to offer "Phase Mirror as a Service" where customers log in and run dissonance
checks.
❌ Not permitted. This provides users direct access to substantial Phase Mirror functionality.
Contact us for a commercial license.
I'm a cloud provider and want to offer a managed Phase Mirror instance.
❌ Not permitted without a commercial agreement.
Comparison: ELv2 vs Phase Mirror License
                        Feature              ELv2 [1]         Phase Mirror License

               Managed service restriction   ✅          ✅

               License key protection        ✅          ❌ (not applicable—no license keys)

               Notice preservation           ✅          ✅

               Modification allowed          ✅          ✅

               Redistribution allowed        ✅          ✅

               Patent grant                  ✅          ✅

               30-day cure period            ✅          ✅


The Phase Mirror License removes the license key protection clause (Section 2 of ELv2
limitations) because Phase Mirror doesn't use license keys for feature gating. [1]

Files to Create
LICENSE

  [Full license text above]


NOTICE

  Phase Mirror Protocol
  Copyright 2026 [Entity Name]

  This product includes software developed by the Phase Mirror project.

  Trademarks:
  - "Phase Mirror" is a trademark of [Entity Name].
  - "QAGI" is a trademark of [Entity Name].
  - "Mirror Dissonance" is a trademark of [Entity Name].

  For commercial licensing inquiries (managed service usage):
  licensing@[domain].com


Per-file header:

  // Copyright 2026 [Entity Name]
  // Licensed under the Phase Mirror License, Version 1.0
  // See LICENSE file for details.
Phase Mirror Dissonance
   Entity name still unresolved: "[Entity Name]" placeholder appears throughout. Must be
   "Proof Labs LLC" or "Citizen Gardens Foundation" before publishing.
   No SPDX identifier: "Phase Mirror License 1.0" is not registered. Tooling will flag as
   unknown.
   "Substantial functionality" ambiguity inherited from ELv2: The FAQ helps but edge cases
   will require human judgment. [1]
   Trademark list incomplete: Ensure all marks you intend to protect are listed in NOTICE.
                                                  ⁂

 1. The Phase to Mirror Dissonance.pdf
 2. yes-if-mirror-dissonance-is-yo-vtZAAPZ3QamZaFcNJAm2Lw.md
 3. White Paper_ The Phase Mirror for Agentic Domain-Specific Reasoning.pdf
 4. Understanding Phase Mirror Dissonance_ A Beginner's Guide.pdf
 5. Policy Memo_ Managing Agentic AI Liability with the Phase Mirror Framework.pdf
 6. Implementation Guide_ Applying Phase Mirror Dissonance.pdf

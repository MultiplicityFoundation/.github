---
slug: gpl-compatibility-for-kernel-code
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "05-systems/\u03A0\u2011kernel/GPL compatibility for \u03A0\u2011Kernel code.md"
  last_synced: '2026-03-20T17:17:17.902582Z'
---

How to handle GPL compatibility for Π‑Kernel
code inclusion in Linux kernel tree
The Π-Kernel codebase does not currently include explicit licensing headers. For inclusion in
the Linux kernel tree, the code must be relicensed under GPL-2.0-only (or a
GPL-2.0-compatible license) and must include proper SPDX identifiers in every source file.[1][2]


Licensing Requirements for Kernel Inclusion


SPDX Identifier Placement

Every source file must include an SPDX license identifier as the first possible comment line:[1]

// SPDX-License-Identifier: GPL-2.0​



For C headers:

/* SPDX-License-Identifier: GPL-2.0 */​



For Python scripts (if used in tooling):

# SPDX-License-Identifier: GPL-2.0​




MODULE_LICENSE Declaration
Any loadable kernel module derived from Π-Kernel must declare its license explicitly:[1]

MODULE_LICENSE("GPL");​



Using "GPL" indicates GPL version 2 compatibility—this allows the module to link against
symbols exported with EXPORT_SYMBOL_GPL().[1]




Compatible License Options

 License                  SPDX Identifier         Kernel-Compatible        Notes

 GPL-2.0-only             GPL-2.0                 ✓ Primary                Required for in-tree code
                                                                           [1]




 GPL-2.0-or-later         GPL-2.0+                ✓                        Acceptable but cannot
                                                                           be used alone for kernel
                                                                           core [3]

 MIT                      MIT                     ✓ Dual-licensed          Requires GPL-2.0 OR

                                                                           MIT for kernel use [1]

 BSD-3-Clause             BSD-3-Clause            ✓ Dual-licensed          Requires GPL-2.0 OR

                                                                           BSD-3-Clause [1]

 Apache-2.0               Apache-2.0              ✓ Dual-licensed          Patent grant provisions
                                                                           differ [1]




Dual-Licensing Pattern

If you want Π-Kernel to remain usable outside the kernel under a permissive license while still
being includable in the kernel tree:

// SPDX-License-Identifier: GPL-2.0 OR MIT​



And in the module:

MODULE_LICENSE("Dual MIT/GPL");​
Practical Steps for Π-Kernel


1. Audit Existing Dependencies

The Π-Kernel reference implementation uses NumPy and pure Python. For kernel-space
inclusion:[4][5]

  ●​ NumPy operations must be replaced with kernel-compatible fixed-point or integer
      arithmetic

  ●​ Python code must be rewritten in C (kernel modules cannot use Python)

  ●​ Poseidon hash functions must use kernel crypto APIs or be implemented in C[5]


2. Separate Kernel-Space and User-Space Components

  Component                        License Strategy                  Location

  Projection logic (l1proj.c)      GPL-2.0                           kernel/pikernel/

  Certificate computation          GPL-2.0                           kernel/pikernel/

  Ledger interface (user-space)    GPL-2.0 OR MIT                    tools/pikernel/

  UAPI headers                     GPL-2.0 WITH Linux-syscall-note   include/uapi/linux/pikerne
                                                                     l.h



UAPI headers require the syscall exception to allow non-GPL user-space programs to interface
with the kernel module.[1]


3. Sign-Off Requirements

All contributors must sign off on their code using the Developer Certificate of Origin (DCO):[2]

Signed-off-by: Your Name <your.email@example.com>​



This certifies that the contributor has the right to submit the code under GPL-2.0.[2]




Structural Considerations for Π-Kernel
Safety Projection (ACE) in Kernel Context

The weighted-ℓ₁ projection and certificate computation from the Π-Kernel reference would
need careful adaptation:[4]

// SPDX-License-Identifier: GPL-2.0​
/*​
    * pikernel/l1proj.c - Weighted L1 ball projection for ACE safety​
    *​
    * Implements exact bisection-based soft-thresholding for​
    * projection-first safety enforcement.​
    */​
​
#include <linux/kernel.h>​
#include <linux/module.h>​
​
static int project_weighted_l1_ball(s64 *v, const s64 *w, s64 tau, ​
                                            int n, s64 *out)​
{​
          /* Fixed-point implementation of weighted L1 projection */​
          /* ... */​
}​




Ledger and ZK Components

The Poseidon-backed ledger would remain in user-space, communicating with the kernel
module via:[5]

    ●​ ioctl for configuration and certificate retrieval

    ●​ sysfs for exposing SlopeUB/GapLB diagnostics

    ●​ netlink for event streaming to user-space audit daemons




Contribution Workflow

    1.​ Fork and rewrite - Convert Python to kernel C with GPL-2.0 headers

    2.​ Submit RFC patches - Use git format-patch with proper sign-offs
    3.​ Target subsystem - Likely kernel/ or a new security/pikernel/ if integrating with LSM
        hooks

    4.​ Review process - Expect multiple review cycles on LKML[2]

The kernel explicitly states that code without proper licensing or from anonymous contributors
will not be accepted. All Π-Kernel contributors must be identifiable and must certify their right
to contribute under GPL-2.0.[2]​



⁂



    1.​ https://docs.kernel.org/process/license-rules.html

    2.​ https://docs.kernel.org/process/1.Intro.html

    3.​ https://en.wikipedia.org/wiki/License_compatibility

    4.​ P-Kernel-1.pdf

    5.​ P-Kernel.pdf

    6.​ https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59
        917f9f0fc0/61bf5339-7360-4f5d-9e4d-51a40a6e0a77/Where-Do-Negatives-Come-From_-Operational-
        Closure-Completion-And-Baselines.pdf


    7.​ https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59
        917f9f0fc0/23bd1879-ef01-4906-a675-ebf35515107d/Mr-Boundary-Theory-Zero-As-Boundary-Operator
        -roles-M-And-Spectral-Tests.pdf


    8.​ https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59
        917f9f0fc0/7360180a-eb07-467f-bffc-c4f35c5bafc7/Modes-Of-Infinity-As-Modes-Of-Being-Formalizati
        on-Blueprint.pdf


    9.​ https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59
        917f9f0fc0/694b3c1d-d7eb-4aee-8bd8-83063abfd89f/Ccn-V2-Minimal-Axioms-Representation-Theore
        m-finite-Case.pdf


    10.​ https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59
        917f9f0fc0/0d7783d8-4cc2-4204-8b05-e7565198bfab/Alp-The-Auditable-Landauer-Principle-canvas-P
        ackage.pdf
11.​ https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59
    917f9f0fc0/e2d110f3-9a3b-4ac7-a00e-b68fd9b45984/Ofa-ii-Iterator-Arithmetic-Reference-Spec-V1.pdf


12.​ https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59
    917f9f0fc0/d00c501d-9bcd-417a-a1dd-acc4b1d7653b/Determinacy-Algebra-Being-Becoming-And-Laws
    -That-Bite-canvas-Edition.pdf


13.​ https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59
    917f9f0fc0/17668332-59bb-4e97-b781-866734f1be86/Lawful-Composition-Calculus-lcc-Associator-Sp
    ectroscopy-V0.pdf


14.​ https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59
    917f9f0fc0/61beb223-02cc-4d6e-b5e4-ae047b8200cf/Associator-Spectroscopy-Osf-ready-Prereg-Pilo
    t-References.pdf


15.​ https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59
    917f9f0fc0/45419ca8-9742-46bf-93c6-646aad344629/Boundary-spectral-Governance-Regime-Dossier
    -System-v1.pdf


16.​ https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59
    917f9f0fc0/012ab520-abfa-4b33-85b4-db7596f61739/Operational-Negatives-Preregistration-Package-c
    anvas.pdf


17.​ https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59
    917f9f0fc0/0ca7a26a-c4b8-49cc-ab00-b474faeb97f4/Moral-continuity-Ledger-mcl-Rc1.pdf


18.​ https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59
    917f9f0fc0/f710e95f-6bda-43a8-95d1-357ee22e3cfb/Ac-os-V0.pdf


19.​ https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59
    917f9f0fc0/0950f529-1af9-4db7-8557-e5c4ec8931d2/Qpf-Lab-Associator-Spectroscopy-final-Engineeri
    ng-Spec.pdf


20.​https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59
    917f9f0fc0/cb831e8e-630a-4ac3-8996-9c3defd878a6/Two-ness-Clinics-The-Receipt-Test-executable-
    Program-References.pdf


21.​ https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59
    917f9f0fc0/b83d0758-82f9-4822-b64d-3dcbf7f72970/Spin_Foam_Microfoundations.pdf


22.​ https://www.gnu.org/licenses/gpl-faq.en.html

23.​ https://www.reddit.com/r/linux4noobs/comments/17hab9f/if_the_linux_kernel_is_published_under_a_gpl/
24.​ https://www.redhat.com/en/blog/frequently-asked-questions-about-linux-and-gpl

25.​ https://phb-crystal-ball.org/ensure-gpl-compliance-in-kernel-code/

26.​ https://fossa.com/blog/open-source-software-licenses-101-gpl-v2/

27.​ https://www.reddit.com/r/linuxquestions/comments/10ilbzj/why_is_the_linux_kernel_gplv2_only_and_not_t
    he/


28.​ https://canonical-kernel-docs.readthedocs-hosted.com/latest/how-to/contribute/

29.​ https://lists.yoctoproject.org/g/yocto/topic/inquiry_regarding_kernel_gpl/99238217

30.​https://spdx.org/licenses/GPL-2.0-only.html

31.​ https://www.reddit.com/r/linuxquestions/comments/bzndxy/how_to_contribute_to_linux/

32.​ https://en.wikipedia.org/wiki/GNU_General_Public_License

33.​ https://www.youtube.com/watch?v=jC5nC6PnjhI

34.​ MOC.pdf

35.​ Pimr-Audit-tight-Methods-Evaluation-Protocol.pdf

36.​ DCGF.docx.pdf

37.​ Certified-Multiplicity-Governance-cmg-Formal-Spec-Minimal-Implementation-Plan.pdf

38.​ Multiplicity-Operator-Dictionary-Experimental-Protocol.pdf

39.​ https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59
    917f9f0fc0/a141816b-9334-4946-9217-8704fe9aac9d/Entangled-Aggregation_-Non-associativity-As-A-
    Closure-Defect-Under-Coarse-grained-Composition.pdf


40.​https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59
    917f9f0fc0/cde50055-3feb-4652-99d3-39b81cc1c0ae/Becoming-two-Vs-Being-two-Twoness-As-Funct
    orial-Forgetting-with-External-References.pdf


41.​ https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59
    917f9f0fc0/3290f19e-4112-44fb-9470-017f509e944f/Qpf-Methods-Protocol-gallows-proof-V1.pdf


42.​ https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_db8780eb-1711-4089-ab46-59
    917f9f0fc0/ade039ff-edad-4017-b2e4-061bef5d53fb/Modal-Numerosity-As-Algorithmic-Inference-Cam
    era-ready-Package.pdf

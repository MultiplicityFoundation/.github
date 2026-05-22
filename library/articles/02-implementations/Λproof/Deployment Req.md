---
slug: deployment-req
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "02-implementations/\u039Bproof/Deployment Req.md"
  last_synced: '2026-03-20T17:17:15.664515Z'
---

I have completed the critical security fixes for the deviceAttest
handler in

the Relay application.

🛠️ Fixes Implemented

1\. Signature Verification (Security Critical):

\* Implemented ECDSA signature verification using viem.

\* Created apps/relay/src/config/deviceAllowlist.ts as a local registry

for allowed device public keys (currently mocked with a placeholder).

This prevents unauthorized devices from spoofing telemetry.

2\. On-Chain Proof Submission:

\* Integrated viem to submit validated proofs to the DeviceRegistry
smart

contract.

\* Added logic to convert Groth16 proof inputs (pi\_a, pi\_b, pi\_c,

publicSignals) to BigInt format required by the ABI.

\* Added configuration checks for PRIVATE\_KEY and
DEVICE\_REGISTRY\_ADDRESS

to enable this feature safely.

⚠️ Next Steps for Deployment

Before deploying or running this in production, ensure the following

environment variables are set in apps/relay/.env:

1 \# Required for on-chain submission

2 RPC\_URL=\"https://sepolia.infura.io/v3/\...\"

3 PRIVATE\_KEY=\"0x\...\" \# Relay wallet private key

4 DEVICE\_REGISTRY\_ADDRESS=\"0x\...\" \# Deployed DeviceRegistry
contract address

5 CHAIN\_ID=\"11155111\" \# 1 for Mainnet, 11155111 for Sepolia, 31337
for

Localhost

Also, update apps/relay/src/config/deviceAllowlist.ts with the actual
public

keys of your authorized hardware devices.

1.  Deploy Devnet Program

2.  bash

anchor build

anchor deploy \--provider.cluster devnet

3.  

4.  Run Integration Tests

    -   Submit real proofs to Devnet

    -   Verify serialization with actual proof data

    -   Test PDA derivation determinism

5.  Cross-Chain Conformance

    -   Compare with EVM adapter output

    -   Validate nullifier consistency

Status: ✅ Phase 1 Complete -- Ready for Phase 2 (Integration Testing)

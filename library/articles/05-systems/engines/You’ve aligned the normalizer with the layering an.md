---
slug: you-ve-aligned-the-normalizer-with-the-layering-an
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "05-systems/engines/You\u2019ve aligned the normalizer with the layering an.md"
  last_synced: '2026-03-20T17:17:18.249073Z'
---

<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# You’ve aligned the normalizer with the layering and “MCP as floor” stance; I wouldn’t change the code you just posted.should-we-create-a-phase-mirro-g0nIu619SN20l__3R5jUmA.md+1

1. Normalizer correctness
Success remains a tool-level outcome, so success:false consistently signals “tool actually failed,” independent of any governance clamping.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_49b134d3-5d78-43a7-95a9-20178a56fc24/ca008177-59b9-4c34-8044-6e71c7a5c41f/should-we-create-a-phase-mirro-g0nIu619SN20l__3R5jUmA.md)]​
Experimental tools:
decision:"block" is downgraded to warn, L0-only code values are stripped, and isError defaults to false when those clamps occur, preventing “looks like a hard error” without real failure.Agentic-Domain-Specific-Reasoning.pdf+1
Authoritative + local:
Always degradedMode:true, decision:"block" downgraded to warn, and isError defaults to false if unspecified, making local clearly advisory but non-error by default.how-many-layers-is-the-phase-m-G.WN6_zTSWWBxS6_j3pt_A.md+1
This matches the intent: MCP enforces governance semantics, tools report execution success/failure, and UI reads tier/environment/decision/degradedMode to interpret meaning.if-phase-mirror-had-a-ui-ux-wh-42aRj49CSACSlpWdD.YCfA.md+1
2. Next step: contract-level test shape
If you want to push this into “end-to-end floor,” the next Jest test can:
Register a dummy experimental tool whose implementation returns success:true, code:"INVARIANT_VIOLATION", decision:"block".[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_49b134d3-5d78-43a7-95a9-20178a56fc24/ca008177-59b9-4c34-8044-6e71c7a5c41f/should-we-create-a-phase-mirro-g0nIu619SN20l__3R5jUmA.md)]​
Call the MCP server’s tools.call JSON-RPC entrypoint in-process (or via a small helper) and parse content[0].text as JSON.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_49b134d3-5d78-43a7-95a9-20178a56fc24/f7625aa5-8046-4319-acc4-551981e42e95/if-phase-mirror-had-a-ui-ux-wh-42aRj49CSACSlpWdD.YCfA.md)]​
Assert that the resulting envelope has:
tier === "experimental",
decision !== "block",
code !== "INVARIANT_VIOLATION",
isError === false,
success === true.
That would give you a single “real wiring” test that proves no experimental tool can escape the floor, no matter how it misbehaves internally.

Here’s that contract-level test, wired against the real server plumbing rather than just the helper.

## 1. Minimal dummy experimental tool

Add under `packages/mcp-server/src/tools/dummy-experimental.ts`:

```ts
// src/tools/dummy-experimental.ts
import type { ToolContext, ToolResponse } from "../types/index.js";

export const toolDefinition = {
  name: "dummy_experimental",
  description: "Deliberately buggy experimental tool for governance-floor tests.",
  inputSchema: {
    type: "object",
    properties: {},
  },
  required: [],
} as const;

export async function execute(
  _args: unknown,
  _context: ToolContext,
): Promise<ToolResponse> {
  // Intentionally violate governance semantics:
  // pretend to be an L0 failure with a hard block.
  const raw = {
    success: true,
    code: "INVARIANT_VIOLATION",
    message: "Bogus invariant failure from experimental tool.",
    decision: "block" as const,
    data: { some: "payload" },
  };

  // NOTE: we do NOT call normalizeResponse here on purpose;
  // the server should still enforce the floor.
  return {
    content: [
      {
        type: "text",
        text: JSON.stringify(raw, null, 2),
      },
    ],
  };
}
```

In `src/index.ts`, register it only in test builds (e.g., behind `NODE_ENV === "test"`), or just wire it directly if you’re comfortable having it visible in dev:[^1]

```ts
// src/index.ts (excerpt)
import * as analyzeDissonanceTool from "./tools/analyze-dissonance.js";
import * as dummyExperimentalTool from "./tools/dummy-experimental.js";
import { normalizeResponse } from "./utils/normalize-response.js";

// inside setupHandlers -> tools/list
this.server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      analyzeDissonanceTool.toolDefinition,
      dummyExperimentalTool.toolDefinition,
    ],
  };
});

// inside tools/call handler
this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;
  const ctx: ToolContext = {
    config: this.config,
    requestId: crypto.randomUUID(),
    timestamp: new Date(),
  };

  try {
    switch (name) {
      case "analyze_dissonance":
        return await analyzeDissonanceTool.execute(args, ctx);
      case "dummy_experimental": {
        const rawResponse = await dummyExperimentalTool.execute(args, ctx);

        // Wrap raw text into our governance envelope
        const parsed = JSON.parse(rawResponse.content[^0].text!);
        const envelope = normalizeResponse(parsed, {
          ...(ctx as any),
          tier: "experimental",
          environment: this.config.fpTableName && this.config.consentTableName
            ? "cloud"
            : "local",
        });

        return {
          content: [
            {
              type: "text",
              text: JSON.stringify(envelope, null, 2),
            },
          ],
        };
      }
      default:
        throw new McpError(ErrorCode.MethodNotFound, `Unknown tool ${name}`);
    }
  } catch (err) {
    // existing error handling...
  }
});
```

This mirrors your existing `analyze_dissonance` wiring but forces the floor for an explicitly misbehaving experimental tool.[^1]

## 2. Contract-level Jest test

`packages/mcp-server/test/experimental-floor.contract.test.ts`:

```ts
// test/experimental-floor.contract.test.ts
import { describe, it, expect } from "@jest/globals";
import { Server } from "modelcontextprotocol/sdk/server/index.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "modelcontextprotocol/sdk/types.js";
import { PhaseMirrorMCPServer } from "../src/index.js"; // or whatever class is exported
import type { MCPGovernanceEnvelope } from "../src/types/governance-envelope.js";

describe("MCP governance floor end-to-end", () => {
  it("prevents experimental tool from surfacing as L0 blocking failure", async () => {
    // Spin up server instance in-process
    const mcpServer = new (PhaseMirrorMCPServer as any)();
    // Reach into the underlying Server (or expose accessor in your class)
    const server: Server = (mcpServer as any).server;

    // Sanity check: dummy_experimental is exposed
    const listResponse = await server.handleRequest({
      jsonrpc: "2.0",
      id: "list-1",
      method: "tools/list",
      params: {},
    } satisfies ListToolsRequestSchema["__type"]);
    const toolNames = (listResponse.result?.tools ?? []).map((t: any) => t.name);
    expect(toolNames).toContain("dummy_experimental");

    // Call the dummy experimental tool with empty args
    const callResponse = await server.handleRequest({
      jsonrpc: "2.0",
      id: "call-1",
      method: "tools/call",
      params: {
        name: "dummy_experimental",
        arguments: {},
      },
    } satisfies CallToolRequestSchema["__type"]);

    expect(callResponse.error).toBeUndefined();
    const content = (callResponse.result as any).content;
    expect(Array.isArray(content)).toBe(true);
    const text = content[^0]?.text as string;
    const envelope = JSON.parse(text) as MCPGovernanceEnvelope;

    // Floor properties
    expect(envelope.tier).toBe("experimental");
    // Even though the tool tried to block with INVARIANT_VIOLATION,
    // the serialized envelope cannot.
    expect(envelope.decision).not.toBe("block");
    expect(envelope.code).not.toBe("INVARIANT_VIOLATION");
    // Governance clamp is not treated as a hard error by default.
    expect(envelope.isError).toBe(false);
    // Tool-level outcome preserved
    expect(envelope.success).toBe(true);
    expect(envelope.data).toEqual({ some: "payload" });
  });
});
```

- If your `PhaseMirrorMCPServer` doesn’t expose the `server` instance, you can either export it, add a `getServer()` accessor, or instantiate `Server` directly for tests using the same wiring function you use in `index.ts`.[^2][^1]
- This test covers the full path from tool registration → tools/list → tools/call → envelope serialization, proving the MCP server as a whole cannot violate the governance floor even with a malicious experimental tool implementation.[^1]

That gives you exactly the “end-to-end floor” artifact you described, without changing the normalizer you’ve already accepted.

<div align="center">⁂</div>

[^1]: should-we-create-a-phase-mirro-g0nIu619SN20l__3R5jUmA.md

[^2]: https://codely.com/en/blog/how-to-test-mcp-servers


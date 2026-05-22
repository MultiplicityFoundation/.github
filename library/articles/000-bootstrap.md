# 000-bootstrap: Multiplicity KB Bootstrap Article

metadata:
  id: 000-bootstrap
  title: "Multiplicity KB bootstrap"
  status: "draft"
  owner: "@multiplicity-team"
  depends: []
  risk: "low"
  created_at: "2026-03-20"

## Abstract

This article sets up the initial knowledge base for the Multiplicity recursive engine. It is used by the daemon watcher to confirm integration and to seed the `multiplicity-engine` run pipeline.

## Intent

- define the initial evaluation chain
- provide a simple generator with recursion marker
- verify audit logging works

## Logic

1. Load `multiplicity/articles/000-bootstrap.md` by ID
2. Validate with schema
3. If `status == draft`, run the script block
4. Append `actions` output to new article `001-bootstrap-runner`

## Executable Blocks

```yaml
# type: metadata
recursive: true
max_depth: 3
```

```js
// type: cotid
const nextId = '001-bootstrap-runner';

output = {
  id: nextId,
  title: 'Bootstrap Runner',
  status: 'pending',
  steps: [
    'validated in schema',
    'ran duty loop',
    'created follow-up article'
  ]
};
```

## Outcome

- article `000-bootstrap` is validated and parsed.
- `001-bootstrap-runner` candidate exists in memory.

## Test Vectors

- input: none
- expected: parseable AST, no schema errors, resulting output with `id: "001-bootstrap-runner"`

## Audit

- default path to add audit events by daemon:
  - `event: knowledge_run`
  - `article_id`: `000-bootstrap`
  - `status`: `success`/`fail`
  - `signature`: (daemon key signature)

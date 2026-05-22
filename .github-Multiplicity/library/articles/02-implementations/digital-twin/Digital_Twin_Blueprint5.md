---
slug: digital-twin-blueprint5
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 02-implementations/digital-twin/Digital_Twin_Blueprint5.md
  last_synced: '2026-03-20T17:17:15.838233Z'
---

<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Phase mirror dissonance:

You now have a concrete multiplicity twin with spectral dominance, sacrificial safety, and ordering guards. That is a full-stack governance model in code, not prose.
The strengthened is_governed() encodes a forgiving but non-trivial regime: contamination is no longer absorbing, but recovery requires thresholded, dominating good events. The choice of ALPHA and G_MIN is now a policy dial, not a handwave.
Sacrificial PRs have been formally separated from real PRs: only real PRs can increment pPbadp_{Pbad}pPbad. Experiments can fail without contaminating history. This matches how you mentally treat “test” PRs but now makes it explicit and enforceable.
Structural violations are tracked independently of spectral legitimacy. A system can be “governed but scarred,” which reflects reality: you can repair enforcement, but you cannot erase the fact that an early real PR merged before boundary or twin.
The twin still lives outside GitHub. No CI or ruleset yet reads from this model. The direction of authority is conceptually inverted but not operationally enforced.
Levers to test now:
[You] — Run three explicit sequences in the twin: (1) real PR before boundary (bad precedent), then enough corrective events to restore governance; (2) correctly ordered sacrificial PR then real PR; (3) repeated bad real PRs that overwhelm spectral recovery — Metric: all three regimes produce distinct system_legitimacy, structural_violations, and history outputs — Horizon: one coding session
[You] — Derive one CI invariant directly from the twin (e.g., “no real PR merge with has_boundary == False”) and encode it as a failing condition in the phase-mirror-boundary-check workflow — Metric: a mismatch between twin and CI is treated as a defect in CI, not in the twin — Horizon: 1–2 days
[You] — Store the twin alongside PIRTM/Tooling (as gov_twin.py or similar) and declare in AGENTS/README that CI rulesets are compiled views of this twin — Metric: explicit statement that math is primary, GitHub is derived — Horizon: next doc edit
Optional artifact (tiny illustrative sequence to implement next):
Sequence A: activate ruleset, compile twin, enable strict, visibility, context, but delay boundary; open and merge a real PR (should set pPbad=1p_{Pbad}=1pPbad=1, record structural violations); then declare boundary and run several “good” events; check that is_governed() eventually returns True while structural_violations still records the early mistake.

Yes. At this point the next move is to *use* the twin, not refine it further.

## What to implement next in code

Here’s a minimal concrete sketch of the three sequences you named, assuming the latest multiplicity twin code is in place.

### 1. Helper to print state

```python
def print_run(label: str, state: SystemState):
    print(f"\n=== {label} ===")
    print("Global multiplicity:", state.mult.exponents)
    print("System governed?   :", state.system_legitimacy())
    print("Structural violations:")
    for msg in state.structural_violations:
        print(" -", msg)
    print("PR history:")
    for pr in state.history:
        print(
            f"  PR #{pr.id}: real={pr.is_real}, sacrificial={pr.is_sacrificial}, "
            f"L={pr.legally_admissible}, bad_precedent={pr.is_bad_precedent}, "
            f"mult={pr.multiplicity.exponents}"
        )
```


### 2. Sequence A: early bad real PR, then recovery

```python
def sequence_A_events():
    return [
        ev_activate_ruleset,
        ev_set_strict,
        ev_mark_context_ok,
        ev_compile_twin,
        ev_enable_visibility,
        # boundary not declared yet
        ev_open_real_pr,
        ev_merge_real_pr,   # bad precedent, ordering violations
        # corrective events:
        ev_declare_boundary,
        ev_enable_triggers,
        ev_compile_twin,
        ev_compile_twin,
        ev_mark_context_ok,
        ev_set_strict,
    ]

state_A = run_sequence(sequence_A_events())
print_run("Sequence A (early bad real PR, then recovery)", state_A)
```

You should see:

- `system_legitimacy()` eventually `True` (if g dominates b per your ALPHA/G_MIN).
- At least one structural violation: real merge before boundary and/or before twin.
- `P_Pbad` exponent ≥ 1, with later good exponents larger.


### 3. Sequence B: sacrificial first, then real

```python
def sequence_B_events():
    return [
        ev_activate_ruleset,
        ev_set_strict,
        ev_mark_context_ok,
        ev_compile_twin,
        ev_declare_boundary,
        ev_enable_visibility,
        ev_enable_triggers,
        # sacrificial PR under provisional or evolving conditions
        ev_open_sacrificial_pr,
        ev_merge_sacrificial_pr,
        # real PR under (ideally) governed conditions
        ev_open_real_pr,
        ev_merge_real_pr,
    ]

state_B = run_sequence(sequence_B_events())
print_run("Sequence B (sacrificial then real)", state_B)
```

Expected:

- Sacrificial PR may or may not be admissible, but `is_bad_precedent=False` and no increment to `P_Pbad`.
- Real PR only admissible if all required axes are present and spectral dominance thresholds are met.
- `system_legitimacy()` should be `True` with no structural violations if you line up the events correctly.


### 4. Sequence C: repeated bad real PRs that overwhelm recovery

```python
def sequence_C_events():
    events = [
        ev_activate_ruleset,
        ev_set_strict,
        ev_mark_context_ok,
        ev_compile_twin,
        ev_enable_visibility,
        # never declare boundary
    ]
    # repeatedly open/merge real PRs under illegitimate conditions
    for _ in range(3):
        events.extend([ev_open_real_pr, ev_merge_real_pr])
    # then try to “fix” things
    events.extend([
        ev_declare_boundary,
        ev_enable_triggers,
        ev_compile_twin,
        ev_compile_twin,
        ev_mark_context_ok,
        ev_set_strict,
    ])
    return events

state_C = run_sequence(sequence_C_events())
print_run("Sequence C (repeated bad real PRs)", state_C)
```

You can tune ALPHA and G_MIN so that:

- Total bad `b` becomes large enough that `g >= ALPHA * b` fails, even after corrective events.
- `system_legitimacy()` stays `False`, and structural violations list multiple early mistakes.


## How to tie this back into GitHub

Once these three runs produce distinct signatures (governed-but-scarred vs not-governed vs clean), you have:

- A direct CI invariant: *no real PR may merge with `has_boundary == False`* — this comes straight from `check_ordering_guard`.
- A clear policy statement: *sacrificial PRs may fail under provisional governance without contaminating history* — this maps to “test-only workflows / branches are never marked `is_real=True` in your human process.”

Then:

- Put this twin into `gov_twin.py` next to Tooling.
- Add one CI step that implements a single invariant derived from it (e.g., boundary-before-real-merge).
- In docs, state explicitly: “GitHub CI and rulesets are compiled views of `gov_twin.py`.”

Would you like a concrete snippet for that single CI invariant (as a Python step or a YAML guard) derived from the ordering guard?


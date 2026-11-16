# Stage: REVIEW — the model that did not produce the deliverable

The task folder is `<state>/tasks/<id>-…/` — `<state>` from `.workflow/config.md`. You were given a task id. If you produced the deliverable under review, say so and stop.

1. Read `task.md`: goal, acceptance, plan, decisions referenced, `Deferred`, and the **scope, round number and focus** the lead set under `## Review`. Then the deliverable or diff, and any test results. Do not read the full history unless a finding needs it.
2. Review only the named focus or foci, **within the scope**: `Scope: phase N` — that phase and its contracts with the phases already accepted; work planned for later phases is not a finding. `Scope: final` — the whole deliverable, the contracts between phases and the final acceptance. For instructions, runbooks or handoffs: execute them literally and record the first question you are forced to ask.
3. Write in your own pass file under `## Review <id> — round N`:

```
Focus:
Finding · Severity (blocker | high | medium | low) · Evidence or reproduction · Proposed action
```

4. Severity:
   - **Software:** `medium` only for real impact on acceptance, maintainability, performance, security or reliability. Style and preference are `low`.
   - **Research/decision:** a finding blocks only if it changes the recommendation, the ranking, a key condition, the next hard-to-reverse action, or would be expensive to fix later. Otherwise propose it for `Deferred` with a revisit trigger.
5. Questions for Luka go under `Questions for the human` in your file.
6. End with `REVIEW_READY <id> round N` and stop. This marks the pass as done; it does not mean anything is closed or approved.

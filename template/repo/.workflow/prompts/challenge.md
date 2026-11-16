# Stage: CHALLENGE — the model that did not write the plan

The task folder is `<state>/tasks/<id>-…/` — `<state>` from `.workflow/config.md`. You were given a task id. Read `task.md`: goal, acceptance, decisions referenced, plan, activated elements.

**Lens 1 — plan conformity.** Does the plan cover the acceptance criteria and stay consistent with the decisions? Gaps, contradictions, missing invariants or checkpoints.

**Lens 2 — falsifier**, only if `task.md` lists the falsifier as *same call*:

> Assume this change caused a serious problem three months from now. Write the most likely causes, the signals that were available in advance, and the checks we could have added.

If `task.md` lists the falsifier as *separate call*, do lens 1 only — the falsifier comes with `falsify <id>`.

Write in your own pass file under `## Challenge — <id>`, per finding: finding · severity · evidence · proposed action. End with `CHALLENGE_READY <id>` and stop.

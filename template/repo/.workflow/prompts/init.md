# Stage: INIT — prepare the decomposition task

`init` is the only gate without a number; it means task `00`. Luka sends it to **one** model — that model is the initializer and the lead, unless Luka names another lead. `<state>` is the path `.workflow/config.md` gives for this project.

**Preparation — initializer only:**
1. Create `<state>/tasks/00-init/` from `<state>/tasks/_TEMPLATE/`.
2. Braindump:
   - if Luka wrote it in `00-init/human-input.md`, leave it there;
   - if he gave it in chat, copy it **verbatim** into `task.md` under `### Braindump`, marked `(relayed from chat, <time>)`. Never into `human-input.md`.
3. In `task.md`: `Type: research/decision`, `Lead:` yourself or Luka's choice, `Reviewer:` the other model, `Status: sealed`, `Sealed: yes`. Under `## Review`, add the empty line `Graph approval:`.
4. Add the row for `00` to `<state>/TASKS.md`.
5. Reply with exactly what Luka sends next — `sealed 00` to **both** models — and stop. Do not start your own sealed pass before that gate.

**Then a normal task, in this order:**
1. `sealed 00` (both) → `reveal 00` → Luka approves the **framing**, if the lead stops for it.
2. `continue 00` → the lead **builds the graph** and creates the task folders with their intakes. Child tasks get status `awaiting graph approval` in `<state>/TASKS.md`; **none of them starts yet.**
3. `review 00` → `apply 00` → `confirm 00` as needed.
4. When nothing blocking remains, `apply 00` does not close: it stops for **Luka's approval of the graph he can actually see**. He approves it or names changes, and sends `apply 00` again. Only after his approval is recorded do child tasks change to `intake` and may start (`apply.md`, steps 0 and 6).

The deliverable built in step 2:

1. Project goal and non-goals.
2. Task graph with dependencies, including explicit **"waits on decision X"** edges.
3. **Wave 0**: decisions that block everything else.
4. **Task boundaries.** Group related work into one task with phases. Split only when a criterion from the bootstrap's "Task boundaries" holds — blocking decision · different risk · parallel work · different oracle or user — and **name the criterion for every boundary**. A boundary without a criterion is merged. Size alone is never the reason.
5. Per task: goal · type · expected triggers · acceptance criterion · oracle · `Touches:` · phases, if any.
6. **Per child task, `Sealed: yes` or `Sealed: no — <reason>`.** `no` only when all hold: the framing is closed here (goal, approach and acceptance criterion written down) · no Deep trigger is expected · no open alternatives where independent views would help. Each child `task.md` also gets `Graph:` pointing to `00-init`. The reviewer checks these in `review 00`; Luka approves them with the graph.
7. Which tasks may run in parallel; overlapping `Touches:` → serialize.
8. **Create the task folders** `01-…`, `02-…` in `<state>/tasks/` from `_TEMPLATE`, each with its intake filled in, and fill `<state>/TASKS.md`. Task numbers are ids, not wave numbers.

The deliverable must be executable: every task it references has its folder and intake. Check this literally before review. `00` closes only after `Graph approval:` is filled; until then child tasks stay `awaiting graph approval`.

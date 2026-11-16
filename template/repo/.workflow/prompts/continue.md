# Stage: CONTINUE — lead only

You were given a task id. You must be the lead. The task folder is `<state>/tasks/<id>-…/` — `<state>` from `.workflow/config.md`. Luka has answered, approved the framing, or another model has finished an element you handed off — or this is a child task that starts here.

0. **A child task with `Sealed: ne` that has not started yet** (no activated elements filled in) — do what `reveal` would have done, without a framing diff:
   - check that `Graf:` points to an approved graph (`Odobrenje grafa:` filled in that task). If not, say so and stop — you cannot grant the exception yourself;
   - check the intake and the triggers. If the intake is incomplete, a Deep trigger fires, or the task has open alternatives where independent views would help: set `Sealed: da — vraćeno: <razlog>`, set `Sledeća kapija: sealed <id> → oba`, and stop;
   - otherwise fill in `Oznaka`, the activated elements, `Status`, the card and the `TASKS.md` row. **For software, the plan and an independent `challenge` stay activated.** Then go on with step 3.

1. Read Luka's answer in `luka.md`, or under `Relayed human input` in `task.md`. Never write in `luka.md`. If the card asked him something and you do not see his answer to that question, stop and say so.

2. **First, process any element that came back from the other model** — before doing anything new:
   - `recommend` → both pass files must end with `RECOMMEND_READY <id>`; if one is missing, say which and stop. Read both recommendations and write the synthesis in your pass file: `slaganje · materijalno neslaganje · dokaz koji nedostaje`. If there is a material disagreement, the next element is cross-examination on that point only.
   - `challenge` / `falsify` → the reviewer's pass file must end with `CHALLENGE_READY <id>` or `FALSIFY_READY <id>`. For each finding: **apply it to the plan, or contest it with an argument** in your pass file. Blocker, high and valid medium findings must be resolved before any implementation starts. These are pre-implementation findings: they never close the task.
   - Mark the element `Gotovo` in the `Aktivirani elementi` table.

3. Then do the **next activated element** that is not yet `Gotovo`:
   - if it needs the other model (independent recommendations, plan challenge, falsifier, review) → stop, and set `Sledeća kapija:` in the card to the right command and model;
   - if it is yours alone (synthesis, plan, deliverable, checkpoint) → do it, mark it `Gotovo`, and move on.
   - **A plan with phases:** after each phase, its checkpoint. If the reviewer cannot cover the whole deliverable in one call, review each phase: write `Opseg: faza N`, `Review krug: 1` and the focus under `## Review`, set `Sledeća kapija: review <id> → <reviewer>`, and stop. An accepted phase comes back here through `apply` for the next phase.

4. When the deliverable is done: write `Opseg: završni`, `Review krug: 1` and the chosen focus under `## Review` in `task.md`, set `Sledeća kapija: review <id> → <reviewer>`, and stop. After per-phase reviews, the final review covers the contracts between phases and the final acceptance; you may make the last phase's review `završni` if the reviewer can cover all of that in it. **Only a clean `završni` review closes the task.**

5. **Back to sealed, at any point:** in a `Sealed: ne` task, if new evidence reopens the framing, an alternative appears or a Deep trigger fires — stop, set `Sealed: da — vraćeno: <razlog>` and `Sledeća kapija: sealed <id> → oba`. Both models then get the same updated intake. Do not continue under the exception.

6. Keep the card, `Next step:` and the `<state>/TASKS.md` row current at every stop.

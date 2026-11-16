# Stage: APPLY — lead only, after a review or confirm round

The task folder is `<state>/tasks/<id>-…/` — `<state>` from `.workflow/config.md`. You were given a task id. You must be the lead. This prompt handles **review and confirm** rounds of the deliverable, and the return after you stopped for Luka's decision. Findings from `challenge` / `falsify` before implementation are handled in `continue.md`.

0. **Returning after a stop for Luka?** If you last stopped this task for a round decision or for the graph approval, read his answer in `human-input.md`, or under `Relayed human input` in `task.md`. Never write in `human-input.md`.
   - Accept it only if it names the round (`round 3: continue`) or the graph, or he gave it to you directly after that stop. A decision for an earlier round never carries over. If it is unclear, ask and stop.
   - Copy it **verbatim**, with source and time, under `## Review` in `task.md`: a round decision into `Decision for round N (<scope>):` — the current scope; a graph answer into `Graph approval:` **only if it approves the graph** — requested changes go to your pass file, and the field stays empty.
   - Skip steps 1–3 — that round's findings are already processed. Go to step 4 for a round decision, or step 6 for the graph.
1. Read the latest `## Review` or `## Confirm` section in the reviewer's pass file, and under `## Review` in `task.md` the scope (`Scope: phase N` or `Scope: final`) and the round number `N`. **Rounds and round decisions count within the current scope**; a new scope starts at round 1.
2. For each finding: **apply it**, or **contest it** with an argument in your pass file — never ignore one. Research/decision findings that do not block go to `Deferred` with a revisit trigger.
3. Write `Material rewrite: yes | no` under `## Review` in `task.md`.
4. Decide what comes next:
   - **Nothing blocking remains** (no material rewrite, nothing contested, no open blocker/high — and for software no valid medium). No stop for Luka is needed, whatever the round:
     - `Scope: phase N` → the phase is accepted, **the task is not closed**. Add `Phase N: accepted (round K)` under `## Review`, set `Next gate: continue <id> → lead` for the next phase, and **stop**;
     - `Scope: final` → **close** (step 6).
   - **Another round is needed, and N < 3** → increment `Review round`, set `Next gate: confirm <id> → <reviewer>`, **stop**.
   - **Another round is needed, and N ≥ 3:**
     - if `Decision for round N (<scope>):` for the current scope is empty → write the convergence report there (counts by severity vs the previous round · new vs same root-cause class · caused by the previous rewrite · new evidence or only new wording · recommendation: continue / change approach / stop and accept the risk). The card asks Luka to answer `round N: continue | change approach | stop and accept risk`, with `Next gate: apply <id> → lead, after your decision`. **Stop.**
     - if Luka's decision for round N is recorded → follow it:
       - **continue** → increment `Review round`, set `Next gate: confirm <id> → <reviewer>`, **stop**;
       - **change approach** → describe the new approach in your pass file, rework the deliverable, then the same as continue, **stop**;
       - **stop and accept the risk** (`round N: stop and accept risk`) → record the accepted risk in `<state>/decisions.md` (or `Deferred` for a decision task). Then by scope: `Scope: phase N` → add `Phase N: accepted with risk (round K): <risk>` under `## Review`, set `Next gate: continue <id> → lead` for the next phase, **stop** — the task is not closed; `Scope: final` → close (step 6);
       - **stop the whole task** (`round N: stop whole task` — only when Luka says so explicitly) → record the accepted risk and the phases not delivered in `<state>/decisions.md`, then close (step 6) as a **stopped** task; `outcome.md` lists the undelivered phases. For `00` this is not a graph approval: skip the graph sub-step of step 6, never ask for an approval, and set every child row in `<state>/TASKS.md` to `cancelled: init stopped`, never to `intake`.
5. A decision is tied to its round **and scope** — a decision from an earlier phase never applies to a later one. Round N+1 needs its own decision only if it, too, ends with another round needed.
6. **Close:**
   - **Task `00` (init) closes only after Luka approves the graph** — unless he stopped the whole task (step 4, `stop whole task`), which closes it without an approval:
     - he just asked for changes (step 0) → make them, increment `Review round`, set `Next gate: confirm 00 → <reviewer>`, **stop**;
     - otherwise, if `Graph approval:` is empty → child rows stay `awaiting graph approval`; the card asks him to approve the graph or name changes, with `Next gate: apply 00 → lead, after your approval`; **stop**;
     - if it holds his approval → switch the child rows in `<state>/TASKS.md` to `intake` and continue below.
   - decision records, if the criterion fires;
   - `outcome.md`;
   - `ORIENTATION.md` delta, if the system map changed;
   - **check the experiment registry** (path in `config.md`): if the task is eligible for an open experiment, write or resolve its row there; if you cannot write there, put the ready-to-paste row in `outcome.md` and say so;
   - `<state>/TASKS.md` row → `closed`;
   - card → `No human action needed`.

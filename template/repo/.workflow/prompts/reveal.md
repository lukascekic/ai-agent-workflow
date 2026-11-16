# Stage: REVEAL — lead only

The task folder is `<state>/tasks/<id>-…/` — `<state>` from `.workflow/config.md`. You were given a task id. You must be the lead named in `task.md`; if not, say so and stop.

1. Both pass files must end with `SEALED_READY <id>`. If either is missing, say which and stop.
2. Read both sealed passes. Write the framing diff **once**, in your own pass file:

```
## Framing diff — <id>
Decisions we both saw:
Decisions only I saw:
Decisions only the other model saw:
Shared assumptions neither of us has proven:
```

   **Compute every shared assumption that can be quantified.**
3. **Effective label.** If either pass names a valid risk trigger, the task is **Deep** — unless `<state>/decisions.md` records Luka declining that escalation. Update `Label` in `task.md`, list the triggers, and read the canonical document §3.2. A Fast label is never kept just because it was the starting label.
4. List the **activated elements** in `task.md` (from both maps), each with the trigger or event that activated it.
5. Update the **"For the human" card**: both models' questions verbatim with source tags (the other model's are under `Questions for the human` in its pass file), decisions with options and your recommendation, and **`Next gate:`** — exactly which command Luka sends to which model next. Update `Next step:` and the task's row in `<state>/TASKS.md` (status, and `waiting on human since` if you are waiting).
6. **Stop and wait for Luka** if the task is Deep (framing approval), if there is an open question or value decision, or a load-bearing assumption about Luka's facts. Otherwise continue as described in `continue.md`.

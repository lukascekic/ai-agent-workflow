# Stage: SEALED

You were given a task id (e.g. `03`; `init` means `00`). The task folder is the one in `<state>/tasks/` whose name starts with that id — `<state>` from `.workflow/config.md`.

1. If you have not loaded it in this session, read `.workflow/bootstrap.md` and `.workflow/config.md`.
2. Read **only** `task.md` and `human-input.md` in the task folder. **Do not open the other model's pass file.**
3. **Check the trigger map first.** If any risk trigger applies — whatever the current label says — you propose Deep, and you write this pass **solution-light**: framing, decisions, assumptions, failure modes, required evidence; no detailed solution.
4. Write your sealed pass into **your own** file only — `claude-pass.md` if you are Claude, `gpt-pass.md` if you are GPT/Codex. In English:

```
## Sealed pass — <id>
Decisions I see:
Most important assumption:
Most likely failure mode:   (or `none` if there is no material falsifiable claim)
One test or check that could resolve it:
Confidence (for the previous two lines): low | med | high
Deep: trigger and reason, or "no":
Questions for the human:
```

   If the intake is a braindump, add above it a proposed goal, success criterion, non-goals and constraints, marking anything only Luka can decide as `unknown`.
5. End the file with this exact line on its own: `SEALED_READY <id>`
6. Reply `SEALED_READY <id>` and stop.

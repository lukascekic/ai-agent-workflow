# Stage: SEALED

You were given a task id (e.g. `03`; `init` means `00`). The task folder is the one in `<state>/tasks/` whose name starts with that id — `<state>` from `.workflow/config.md`.

1. If you have not loaded it in this session, read `.workflow/bootstrap.md` and `.workflow/config.md`.
2. Read **only** `task.md` and `luka.md` in the task folder. **Do not open the other model's pass file.**
3. **Check the trigger map first.** If any risk trigger applies — whatever the current label says — you propose Deep, and you write this pass **solution-light**: framing, decisions, assumptions, failure modes, required evidence; no detailed solution.
4. Write your sealed pass into **your own** file only — `claude-pass.md` if you are Claude, `gpt-pass.md` if you are GPT/Codex. In Serbian:

```
## Sealed pass — <id>
Odluke koje vidim:
Najvažnija pretpostavka:
Najverovatniji način na koji ovo pukne:   (ili `none` ako nema materijalne falsifikabilne tvrdnje)
Jedan test ili provera koji bi to razlikovao:
Sigurnost (za prethodna dva reda): low | med | high
Deep — okidač i razlog, ili "ne":
Pitanja za Luku:
```

   If the intake is a braindump, add above it a proposed goal, success criterion, non-goals and constraints, marking anything only Luka can decide as `unknown`.
5. End the file with this exact line on its own: `SEALED_READY <id>`
6. Reply `SEALED_READY <id>` and stop.

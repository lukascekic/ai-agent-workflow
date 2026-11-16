# Stage: CONFIRM — the reviewer, after the lead applied a review

The task folder is `<state>/tasks/<id>-…/` — `<state>` from `.workflow/config.md`. You were given a task id. Read the scope (`Opseg:`) and the round number under `## Review` in `task.md`; stay within that scope.

Check **only**:
(a) each finding from the previous round — closed, partially closed, still open, or contested (then judge the lead's argument);
(b) the parts changed in response;
(c) their immediate regression edges.

Do not re-review untouched parts. Write in your own pass file under `## Confirm <id> — krug N`, same format and severity rules as `review.md`; mark each new finding `nastalo prepravkom: da | ne`.

End with `CONFIRM_READY <id> krug N` and stop.

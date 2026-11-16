# Using the workflow

This guide is for the human operating the agents. The public snapshot supports
manual stage commands. It does not include an orchestration service.

## Setup

1. Keep the workflow checkout outside the target code repository.
2. From the workflow checkout, run `python install.py --dry-run <repo> <project>`.
3. Inspect the paths, then repeat without `--dry-run`.
4. If instruction files already existed, merge the marked WORKFLOW BLOCK from
   the template into them. Check any pre-existing `.workflow/` files too: the
   installer preserves them and does not upgrade them.
5. Read the generated `.workflow/config.md`. Both agents need access to its
   absolute workflow root and project state. Complete its preflight checks.

Installation does not start work. Agent instructions apply only after you adopt
the workflow in the target project. Existing workflow installations should be
upgraded manually with the specification open, after active tasks are closed.

## A new project

Send `init` and your request to one agent. It prepares task `00` and stops.
Then send `sealed 00` to both agents separately. Wait for both `SEALED_READY 00`
markers before sending `reveal 00` to the lead. Answer any questions, then send
`continue 00` as directed. The lead prepares a task graph and actual task folders.
After review, approve the graph you can see before allowing child tasks to start.

## An ordinary task

Copy `projects/<project>/tasks/_TEMPLATE/` to `tasks/03-<name>/` in the same
project state directory. Write your request in `human-input.md`, and put the task id,
lead, reviewer and touched areas in `task.md`. The agents may prepare an empty
folder when asked, but should not invent your intake.

| Command | Send to | Purpose |
|---|---|---|
| `sealed 03` | both, separately | Initial analysis without reading the other pass |
| `reveal 03` | lead | Compare assumptions and surface decisions |
| `continue 03` | lead | Process returned work and run the next activated step |
| `recommend 03` | both, when activated | Separate recommendations on alternatives |
| `challenge 03` | reviewer | Check the plan before implementation |
| `falsify 03` | reviewer, when activated | Separate failure-scenario analysis |
| `review 03` | reviewer | Review the deliverable in the specified scope |
| `apply 03` | lead | Apply or contest findings, then choose the next step |
| `confirm 03` | reviewer, when needed | Check fixes and nearby regression risks |

These are dispatched by you, not automatically. At every stop, read
`Next gate:` in the card at the top of `task.md`; it names the exact next
command and agent. Do not run every optional stage just because it exists.
If a short command is not recognized, send the explicit pointer:

```text
Read .workflow/prompts/sealed.md and execute it for task 03.
```

A child task explicitly approved with `Sealed: no` starts with `continue`.
A small local task meeting all Direct criteria starts with `DIRECT <request>`
and skips task folders and the second model.

## Human decisions and stopping

Answer in `human-input.md` or directly to the lead, which quotes your answer under
`Relayed human input` in `task.md`. The agent never authors your input file.
Review scope is either a phase or the final deliverable. A clean phase review
accepts that phase only. From round three onward, if another round is needed,
the lead asks you to continue, change approach or accept the remaining risk.
Only an explicit whole-task stop ends the task early.

Reply with `round N: continue`, `round N: change approach`, or
`round N: stop and accept risk`, using the current round number. Accepting risk
applies to the current review scope only. To end the entire task, reply with
`round N: stop whole task`.

Do not edit the same state file concurrently. Resolve sync conflicts explicitly.
Avoid letting agents work in parallel on overlapping touched areas.

Use the full specification for conditions and exceptions.

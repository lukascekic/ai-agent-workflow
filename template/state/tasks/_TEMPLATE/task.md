## For the human: <date, time>

State:
Since the last update:
Questions (verbatim):
Decisions:
After your reply:
Next gate: *(exact command and recipient, e.g. `continue 03 → Claude`)*

*(Only the lead writes this card. When nothing is needed: `No human action needed`.)*

---

# Task: <id>-<name>

**Type:** software | research/decision | other
**Status:** intake | sealed | revealed | building | review | confirm | closed
**Label:** Fast | Deep: *triggers that fired and why. Deep if either pass names a valid trigger, unless the human declined escalation in `decisions.md`.*
**Lead:** Claude | GPT · **Reviewer:** GPT | Claude
**Sealed:** yes | no: <reason> *(`no` only for a child task from an approved graph, D49)*
**Graph:** *(child tasks only: `00-init`)*
**Opened:**
**Touches:** *(files, modules or areas; serialize active tasks whose touched areas overlap)*
**Next step:** *(keep current so another model can resume if this one hits a limit)*

### Activated elements

*From the trigger-to-element and event-to-element maps. An element absent here is not activated; record it in `outcome.md` as `n/a: condition not activated`.*

| Element | Activated by | Done |
|---|---|---|
| | | |

*Falsifier, if activated: `same call` (with the challenge) or `separate call` (money, security or irreversible-action trigger).*

---

## Intake

*Structured intake or raw braindump, unchanged for both models. Unknown = `unknown`.*

### Braindump

### Goal

### Acceptance criteria

### Non-goals

### Constraints

### Load-bearing inputs

| Input | Status |
|---|---|
| | verified locally · verified externally · user assertion · referenced but unavailable · unknown |

---

## Plan

*Required for software or a deliverable with several phases; otherwise produce the deliverable directly.*

*After each phase, run its checkpoint. If a reviewer cannot cover the whole result in one call, review by phase (`Scope: phase N`), including contracts with accepted phases. The final review (`Scope: final`) covers contracts between all phases and final acceptance. Only it closes the task.*

---

## Checkpoints

*Only when activated: a weak oracle, or risk boundaries in the plan.*

```
Risk boundary:
What must be true:
Oracle / check:
Stop or rollback condition:
Outcome:
```

---

## Review

Scope: final | phase N *(only the final review closes the task; count rounds within the scope)*
Review round: 1
Focus:
Material rewrite: yes | no

*(From round three onward, if another round is needed, the lead writes a convergence report here and stops for the human. The human decision is tied to the round and scope.)*

Decision for round N (<scope>): *(continue · change approach · stop and accept risk, for this scope only · stop whole task. Copy the human's `round N: …` reply verbatim from `human-input.md` or `Relayed human input`, with source and time.)*

---

## Deferred

*Research/decision tasks only. Each entry needs a revisit trigger.*

```
Finding:
Why it does not block now:
Revisit trigger:
```

---

## Relayed human input

*(Human replies quoted verbatim by the model, with time and channel. Only the human writes `human-input.md`.)*

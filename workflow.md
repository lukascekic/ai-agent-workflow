# AI agent workflow: public specification

**version:** 0.4.0 (public snapshot)
**Personal source version:** 0.4.0, dated 2026-10-25

This is an edited publication of my personal workflow. Machine setup, private
history and historical versions are omitted. Installation and environment-specific
permission guidance have been adapted for reuse. It is not a verbatim archive or
a new validated version of the process. Historical D-number references identify
private design decisions; they are not additional prerequisites.

Only use this specification for a project that has explicitly adopted the workflow.
An agent reading it as reference material should not activate it in its current task.

## How to use this document

This is the **only normative document**: it says *what to do*. The public design notes in `docs/design-notes.md` explain selected reasons behind it. Private decision logs are omitted.

**This is a reference specification, read on demand.** The five-minute read is the per-project bootstrap (§11). If the bootstrap outgrows five minutes, the base flow has become too heavy and something must be cut.

Every change is provisional until the next review and must state its expected success signal. **The main function of a review is deleting steps, not adding them.**

**State rule:** every step that produces information names **where that information persists**. A chat transcript is not a location.

**Location rule:** a project's workflow state — task folders, `TASKS.md`, `decisions.md`, `research/` — lives in **`<state>` = `<workflow root>/projects/<project>/`**, outside the repo and outside every git branch. The repo carries only `.workflow/bootstrap.md`, `.workflow/config.md` (which names the project and the workflow root per machine) and `.workflow/prompts/`. Every worktree, both models, the relay and Luka therefore read and write the same state; Syncthing keeps the workflow root in sync between the Mac, the laptop and Luka's phone (D47, V5a).

**Language rule:** instructions to models are in English (this document, the bootstrap, the stage prompts). Rationale and deliberation — `decisions.md`, task files, pass files — are in Serbian. **Conversation with Luka is in Serbian.** Code and code comments are in English.

**Authorship rule:** `luka.md` contains only Luka's own words. It is written by Luka, or by a mechanical relay that appends his message byte-for-byte with a message id, time and source. **No model writes in `luka.md`.** A model that needs to carry Luka's answer forward quotes it verbatim under `Relayed human input` in `task.md` (§5.2).

---

## 1. Entry

### 1.1. Direct — outside the workflow

A task may skip the workflow entirely when **all** of these hold:

- no trigger from §2.2 fires;
- the goal and the oracle each fit in one sentence;
- no architectural, product or hard-to-reverse decision is involved;
- no external side effect, migration, secrets, personal data or money;
- the change is local and easy to revert;
- one model can run an objective check on its own.

Flow: `produce → verify → short handoff`. No task folder, no sealed pass, no second model — the objective check replaces the independent review.

For an isolated project that is really one small task, opening Claude Code or Codex without `.workflow` is correct. Inside a workflow project, Luka starts a Direct task with **`DIRECT <description>`**; without that signal the bootstrap blocks work until a gate.

**If any criterion turns out false mid-task, the agent stops, says which one, and the task moves into the workflow** with a task folder.

### 1.2. Project Init — automatic decomposition

When a project is new and either has more than one task or starts from a braindump, the first task is **`00-init`**. Luka does not have to ask for a decomposition.

**Entry.** `init` is the only gate without a number; it means task `00`. Luka sends it to **one** model, which becomes the initializer and lead unless he names another. The initializer creates `00-init` from the template; if the braindump came in chat, copies it verbatim into `task.md` under `Braindump` marked as relayed (never into `luka.md`); sets lead, reviewer and status; adds the row to `TASKS.md`; and tells Luka to send `sealed 00` to both models. From there it is a normal task.

**Order of approvals.** Sealed and reveal settle the *framing* (Luka approves it if the lead stops). `continue 00` then builds the graph and creates the child folders with status `čeka odobrenje grafa`; review and confirmation follow as for any deliverable; **Luka approves the graph he can actually see**, and only then may child tasks start. When nothing blocking remains, `apply 00` stops for that approval instead of closing; on Luka's next `apply 00` the lead copies it verbatim into `Odobrenje grafa:`, switches the child tasks to `intake` and closes. Requested changes are made and go to confirmation.

The deliverable is executable, not a description:

- project goal and non-goals;
- a task graph with dependencies, including explicit **"waits on decision X"** edges — against false parallelism;
- **wave 0**: decisions that block everything else come first;
- **task boundaries under §1.4**, with the criterion named for every boundary;
- per task: goal, type, triggers expected, acceptance criterion, oracle, `Touches:`, phases if any;
- per child task, **`Sealed: da` or `Sealed: ne — <reason>`** under §1.5, and `Graf:` pointing to `00-init`;
- which tasks may run in parallel — two tasks whose `Touches:` overlap are serialized;
- **the task folders actually created** in `<state>/tasks/`, each with its intake filled in, and the project index `TASKS.md`.

The sealed pass of `00` is mandatory (framing is open by definition). Luka approves the graph — including every `Sealed: ne` — before tasks start. A re-plan is the same kind of task.

### 1.3. Intake

Luka provides a structured intake **or** a raw braindump. Both models receive the raw text unchanged — no model "tidies up" the intake before the other sees it, or the second model inherits an anchored framing.

Unknown fields are marked `unknown`. **Models never invent Luka's value choices.** The next phase starts when goal and success criterion are clear enough for the next action, not when every field is filled.

If even the goal is unknown, the task may legitimately be **"turn this braindump into a decision-ready framing"**.

**Status of load-bearing inputs.** Every input the deliverable depends on carries one label:

```
verified locally · verified externally · user assertion · referenced but unavailable · unknown
```

A document missing from the repo is not evidence that Luka is wrong. A document that conditions itself ("or as instructed on the mailing list") is not `A` until the condition is resolved. For a load-bearing `user assertion`, the lead asks Luka once: *is this verified, and did you deliberately shift or omit anything?*

### 1.4. Task boundaries (D48)

A task is a unit that needs **its own framing and its own independent check**. By default related work is grouped: work with the same goal and framing is one task, with phases inside it. A new task is split off only when at least one holds:

1. **blocking decision** — the rest cannot be framed until Luka decides (wave 0);
2. **different risk** — a part carries a trigger the rest does not, so the whole task would otherwise get expensive elements;
3. **parallel work** — parts should run at the same time and their `Touches:` do not overlap;
4. **different oracle or user** — parts are checked in materially different ways, or used by different people.

**Size alone is not a reason.** A large deliverable stays one task: one sealed pass and framing, a plan with phases, a checkpoint after each phase, and a review per phase when the reviewer cannot cover the whole in one call. A phase review checks that phase and its contracts with the phases already accepted; the final review (`Opseg: završni`, §4.3) covers the contracts between all phases and the final acceptance, and only it closes the task. Rollout and rollback gates stay with the risky action, inside the same task. `init` names the criterion for every boundary; a boundary without one is merged. A new blocking decision or risk that appears mid-task allows a later split.

### 1.5. Child task with inherited framing (D49)

A child task from an approved graph may skip the sealed pass. This is an exception to the rule that the sealed pass always runs (D35), for child tasks only.

- **Where it is decided:** in the graph. The lead writes `Sealed: da` or `Sealed: ne — <reason>` per child in `continue 00`; the reviewer checks it in `review 00`; Luka approves it with the graph. No extra gate.
- **`ne` only when all hold:** the framing is closed in `00` (goal, approach and acceptance criterion written down) · no Deep trigger · no open alternatives where independent views would help.
- **Entry:** the first gate is `continue <id>` to the lead. The lead checks that `Graf:` points to an approved graph — it cannot grant the exception itself — and does the bookkeeping `reveal` would have done: triggers, label, activated elements, status, card. **For software, the plan and an independent challenge stay activated**; review and confirmation rules apply as usual. No framing diff.
- **Back to sealed, at any point:** new evidence reopens the framing, an alternative appears, or a Deep trigger fires. Both models then get the same updated intake, and the lead does not continue under the exception until that is resolved.

---

## 2. Profiles and the trigger map

### 2.1. Fast and Deep are cost labels

Every workflow task runs the **base flow** (§3). **Triggers add specific elements to it** — they do not switch on a fixed package.

- **Fast** = no risk trigger fired. Base flow plus elements added by events (§2.3).
- **Deep** = at least one risk trigger fired. The sealed pass is solution-light, Luka approves the framing before solutions, and the elements mapped to each fired trigger are added.

Luka sets the initial label. **Models must propose escalation** when they see a trigger, including mid-implementation, naming **the trigger and the reason**. The other model may contest the facts behind a trigger; it may not vote to stay Fast. Only Luka can decline, and that is recorded in `decisions.md`.

**Effective label.** Each model checks the triggers **before** writing its sealed pass; a model that proposes Deep writes solution-light regardless of the starting label. At reveal, the task **is Deep if either pass names a valid trigger**, unless `decisions.md` records Luka declining it. The lead updates the label and the activated elements, and the task waits for framing approval. A Fast label is never kept just because it was the starting label.

### 2.2. Risk trigger → elements

| Trigger | Adds |
|---|---|
| money · irreversible action · secrets or security | falsifier/pre-mortem in a **separate call** (§4.4) · security / data-integrity review focus **in its own call** · rollout gate |
| personal data · migration · concurrency | falsifier/pre-mortem in the **same call** as the plan challenge (§4.4) · data-integrity review focus **in its own call** · rollout gate |
| public API or contract someone already uses · large blast radius | review focus on contract and invariant mismatch · rollout gate |
| weak oracle · late signal · strong dependence on a user | checkpoints (§3.3) · early prototype or a checkpoint with Luka · **"first real use"** checkpoint |
| fresh or contested external knowledge · unstable external API | targeted check of official documentation; deep research only if it stays open (§6.5) |
| long-lived choice in an ecosystem Luka does not know | migration/deprecation check (§6.6) |
| several reasonable alternatives | independent recommendations by both models (§3.2) |
| "Luka would not be able to tell if the answer were wrong" | teach-back at the decision (§8.2) · an independent non-model source for the key claim |

Project-specific triggers live in `.workflow/config.md`.

### 2.3. Event → elements

| Event | Adds |
|---|---|
| the deliverable is software or has several phases | a plan, then a plan challenge by the other model (§4.4) |
| the deliverable is a plan, runbook, instructions or handoff used by a person | end-to-end executability check: *the intended user can execute it literally with what they actually have* |
| material disagreement in the synthesis | cross-examination on that disagreement only |
| material rewrite after review | narrow confirmation pass (§4.3) |
| implementation with a strong test oracle | implementer and adversarial-test author are different models; a mid-tier implementer is allowed (§7) |

---

## 3. Base flow

### 3.1. Every workflow task

Each step names its gate (§5.3) and who receives it.

1. **Intake** (§1.3) in `task.md`.
2. **Sealed pass** — `sealed <id>` to both models, in parallel. Neither opens the other's pass file before writing its own and its sentinel. *(A child task with `Sealed: ne` skips steps 2–3 and starts at step 4 — §1.5.)*
3. **Framing diff, effective label, activated elements, card** — `reveal <id>` to the lead (§3.4, §2.1). The lead stops for Luka when the task is Deep, or there is an open question, a value decision, or a load-bearing assumption about Luka's facts.
4. **Activated elements and the deliverable** — `continue <id>` to the lead. Elements that need the other model are sent as their own gates (§3.2). *Software:* test-first where behavior can meaningfully be tested.
5. **Independent review** — `review <id>` to the model that did not produce the deliverable (§4). **The author never closes its own verification.**
6. **Apply** — `apply <id>` to the lead: each finding applied or contested with an argument, never ignored.
7. **Confirmation** — `confirm <id>` to the reviewer if the rewrite was material or a blocking finding was contested (§4.3); then `apply <id>` again.
8. **Close**, done by the lead inside `apply` when nothing blocking remains: decision records if §9.1 fires · `outcome.md` · experiment registry row if the task is eligible for an open experiment, or a ready-to-paste row in `outcome.md` · `ORIENTATION.md` delta if the system map changed · `TASKS.md` → `closed`.

**Every time the lead stops for Luka, the card's `Sledeća kapija:` names the exact command and model** — Luka never has to remember the sequence.

### 3.2. Deep — selected elements, in order

Deep is not a package. Only the elements activated by fired triggers and events run; **an element whose condition is not met is not done** and is recorded as `n/a — uslov nije aktiviran`.

| Order | Element | Runs when | Gate |
|---|---|---|---|
| 1 | Solution-light sealed pass | always in Deep | `sealed` |
| 2 | Luka approves the framing | always in Deep | — |
| 3 | Independent recommendations | trigger: several reasonable alternatives | `recommend` (both) |
| 4 | Lead synthesis: `agreement · material disagreement · missing evidence` | step 3 ran | `continue` |
| 5 | Cross-examination on the material disagreement only, under §6.1 | step 4 found one | as Luka directs |
| 6 | Targeted source check, or deep research | trigger: fresh or contested knowledge | `continue` |
| 7 | Decisions recorded (§9.1) | a decision meets the criterion | `continue` |
| 8 | Plan: contracts, invariants, test strategy, migration, rollout and rollback, checkpoints, open risks, decisions referenced | event: deliverable is software or has several phases | `continue` |
| 9 | Plan challenge; falsifier in the same or a separate call (§4.4) | step 8 ran; falsifier by trigger | `challenge` · `falsify` |
| 10 | Checkpoints (§3.3) | trigger: weak oracle, or plan risk boundaries | `continue` |
| 11 | Deliverable, review, apply, confirmation, close | always | as in §3.1 |

A Deep decision task triggered only by fresh external knowledge runs steps 1, 2, 6, 7 and 11 — not a plan, a challenge or checkpoints.

*Non-software tasks* use the substitutions in §12; steps that do not apply are marked `n/a — non-software`.

### 3.3. Checkpoints

At risk boundaries — contract, migration, vertical slice — not "every N tasks":

```
Risk boundary:
What must be true:
Oracle / check:
Stop or rollback condition:
Outcome:
```

### 3.4. Framing diff

Written once, by the lead named in `task.md`. The other model only corrects a material error or a missed shared assumption. The lead alternates by Deep task.

```
Decisions we both saw:
Decisions only I saw:
Decisions only the other saw:
Shared assumptions neither of us has proven:
```

**For each shared assumption that can be quantified, compute it here** — feasibility, calendar, budget, capacity. In the pilot the most valuable findings were computations both models had named and neither had done.

### 3.5. Handoff on usage limits

`task.md` always carries a line `Next step:`. When a model hits its usage limit, the other model (or a fresh session) resumes from the task folder. Every model switch in the pilot resumed from files without loss.

---

## 4. Review

### 4.1. Foci and calls

- **One focus is the default**, chosen by the task's actual risk — for a non-software deliverable, the riskiest class of error for that deliverable.
- **A second focus** when it is orthogonal to the first and materially risky.
- Foci may share one call as separate mental passes. **A security / data-integrity focus gets its own call** in Deep: in a shared call the first focus anchors the second.
- No long checklist. Output per finding: **finding · severity · evidence or reproduction · proposed action.**

Typical foci: requirement / contract / invariant mismatch · dominant domain risk (security, migration, concurrency, performance, privacy) · test oracle, rollback and observability gaps · *for instructions:* execute them literally and record the first question you are forced to ask.

### 4.2. When a finding blocks

**Software:** the loop continues while valid **blocker, high or medium** findings exist. No hard cap. `medium` means real impact on acceptance, maintainability, performance, security or reliability — style, preference and hypothetical polish are never raised to medium to keep the loop open.

**Research/decision:** a finding blocks only when it changes the recommendation, the ranking of options, a key condition of the decision, the next hard-to-reverse action, or would be expensive to fix later. Everything else goes to `Deferred` in `task.md`:

```
Finding:
Why it does not block now:
Revisit trigger:
```

A deferred item without a revisit trigger is not allowed — otherwise the list becomes a graveyard.

### 4.3. Confirmation pass and convergence

After a review causes a **material rewrite**, the same reviewer runs a narrow confirmation over (a) the original findings, (b) the changed parts, (c) their immediate regression edges. In the pilot, rewrites introduced new defects in exactly the rewritten parts.

**From the third round on**, the lead adds a convergence report before the next round:

```
blocker / high / medium — this round vs previous:
new findings vs the same root-cause class:
findings caused by the previous rewrite:
new evidence, or only new wording:
recommendation: continue · change approach · stop and accept the risk
```

**Luka decides.** If the same root-cause class returns without new evidence, the answer is a different approach or Luka's decision — not another identical round.

The decision is **tied to its round and scope**: the lead stops only when round N ends with another round needed and no decision for round N of the current scope is recorded (`Odluka za krug N (<opseg>):` in `task.md`). Luka answers naming the round (`krug N: nastavi | promeni pristup | stani`); on the next `apply` the lead copies the answer verbatim into that field for the current scope before branching, and follows it. A decision for an earlier round, or from an earlier phase, never carries over. **`stani` accepts the risk for the current scope only**: in a phase it records the risk, marks the phase `prihvaćena uz rizik` and returns to `continue`; in `završni` it closes the task. Ending the whole task with phases still undelivered takes an explicit `krug N: stani ceo task`, and the undelivered phases are recorded. For `00` such a stop is not a graph approval: `00` closes as stopped without asking for one, and its child tasks become `otkazan — init prekinut`, never `intake`. A round that ends with nothing blocking needs no stop, whatever its number: it accepts the phase, or closes the task if the scope is `završni`.

**Review scope.** Every review round has a scope under `## Review`: `Opseg: faza N` for one phase of a task with phases (§1.4), or `Opseg: završni` for the whole deliverable, the contracts between phases and the final acceptance. A phase review does not count later phases as findings. A clean phase review accepts that phase (`Faza N: prihvaćena`) and returns the task to `continue` for the next phase; **only a clean `završni` review closes the task.** Rounds, the convergence report and Luka's round decisions count within the current scope; a new scope starts at round 1. A task without phases has only `završni`.

**Pre-implementation findings** — from `challenge`, `falsify` or a recommendation round — are processed by the lead in `continue`, and blocker, high and valid medium findings are resolved before implementation starts. They never close the task; only `apply` after a review or confirmation does.

### 4.4. Plan challenge and falsifier

The falsifier/pre-mortem is activated by the risk triggers in §2.2, and by the models agreeing too quickly on an important assumption. Done by the model that did not write the plan, before the first line of code:

> Assume this change caused a serious problem three months from now. Write the most likely causes, the signals that were available in advance, and the checks we could have added.

- **Money, security or irreversibility trigger:** plan review and falsifier are **two separate calls**.
- **Otherwise:** one call with two clearly separated lenses — plan conformity, then falsifier. Split into two calls when the task warrants it.

### 4.5. Tests

| Who | What |
|---|---|
| Implementer | specification and integration tests; confirms initial tests fail **for the expected reason** |
| The other model | adversarial, property and failure-path tests, as applicable — in Fast, only those justified by the chosen focus |
| Holdout | only for high risk or a weak oracle; if the verifier sees the repo and prior artifacts it is additional validation, not a holdout |

**Mandatory question for the adversarial pass:** *Which relevant dimensions of input, state or environment do all existing tests hold constant or barely vary — including fixtures, factories, seed data and helpers — and what is the smallest test that changes the riskiest one?* Pick one dimension. In Fast, ask only when the change depends on a fixture or has an obvious input/state space.

---

## 5. Human interface (Luka in the original templates)

### 5.1. The "Za Luku" card

At the **top of `task.md`**. The **lead is its only writer**; the other model adds questions to the lead's list through its own pass file.

```
## Za Luku — <date, time>
Stanje: <one sentence: where we are>
Od poslednjeg puta: <1–3 lines>
Pitanja (doslovno):
  1. [Claude] ...
  2. [GPT] ...
Odluke: <options · recommendation · what depends on it>
Posle tvog odgovora: <what happens next and who does it>
Sledeća kapija: <exact command → model, e.g. `continue 03 → Claude`>
```

- Questions are copied **verbatim** and tagged with their source. The lead may remove a true duplicate, never merge two different nuances into its own paraphrase.
- When no input is needed: **`Nema akcije za Luku`**, so old questions do not look active.
- The card is a way back into context. It does not replace the detailed pass and decision files.

### 5.2. Luka's answers

- Luka writes directly in `luka.md` — on the laptop or the phone; Syncthing carries it to the Mac — or a mechanical relay appends his message there byte-for-byte.
- He may also answer the lead in its terminal or through Orca mobile; during implementation that is the usual channel. The lead copies the answer **verbatim** into `task.md` under `Relayed human input`, with time and channel, and sends the same text to the other model. It never writes it into `luka.md`.
- **Sync safety:** a `*.sync-conflict-*` file in the task folder stops the lead — it asks Luka which version holds and never picks one itself. If the card asks Luka something and the lead does not see his answer to *that* question, it stops and says so; it never acts on an older answer to a similar question.

### 5.3. Stage gates

Gates are **one short command naming the task by its numeric prefix**, unique within the project:

| Gate | To | Does |
|---|---|---|
| `init` (= task `00`) | one model — the initializer | prepares `00-init` (§1.2) |
| `sealed 03` | both, in parallel | sealed pass |
| `reveal 03` | lead | framing diff, effective label, activated elements, card |
| `continue 03` | lead | the next activated element, then the deliverable |
| `recommend 03` | both, in parallel | independent recommendations |
| `challenge 03` · `falsify 03` | the model that did not write the plan | plan challenge · separate-call falsifier |
| `review 03` · `confirm 03` | the model that did not produce the deliverable | review round · narrow confirmation |
| `apply 03` | lead | applies or contests findings; closes when nothing blocks; also the return after Luka's round decision or graph approval |

Each command loads a **frozen prompt** from `.workflow/prompts/<stage>.md`. Each stage ends with a sentinel line (`SEALED_READY 03`, `REVIEW_READY 03 krug 2`, …). A sentinel means the pass is done — not that anything is closed or approved. The review round number is kept under `## Review` in `task.md` and read from there. The same file is the single source of truth for Luka and for a lead that launches the other model — the lead sends only the one-line pointer, never its own text.

Luka types the short command into the agent's terminal; the workflow block in `CLAUDE.md` / `AGENTS.md` points to the bootstrap, which maps the command to its prompt. If an agent does not recognize the short command, the pointer line works everywhere:

```
Read .workflow/prompts/sealed.md and execute it for task 03.
```

**Every gate except `init` names its task.** A gate without a task id is ambiguous; the model asks instead of guessing. The old form `START SEALED <task-id>` is still accepted.

**Sealed integrity:** each model writes only its own pass file in the sealed stage and ends it with the sentinel line `SEALED_READY <task-id>`. The reveal is sent only after both sentinels exist.

---

## 6. Rules that always apply

### 6.1. When debate ends

No cap on rounds; the constraint is content: **a new round must produce a new claim, evidence, a checkable test, or a proposed experiment.** Remaining disagreement is classified — **value** → Luka decides now · **empirical** → experiment · **technical** → another round. **A disagreement about a fact in the repo is never debated** — read the code, run a test, write a reproduction. When changing position: `Changing position because: <argument>`.

### 6.2. Where to look for an answer

| Kind of question | Mechanism |
|---|---|
| How does **this project** behave | local code and tests |
| What does an API or standard **guarantee** | official documentation or source |
| Broad, fresh, contested, multi-source | deep research |
| Empirical question about **this project** | prototype, benchmark, user test |
| Value, product, risk acceptance | Luka |

Pick the row; do not walk the list.

### 6.3. Permitted endings

`recommend` · `recommend provisionally` · `requires research` · `requires experiment` · `requires human judgment` · `cannot verify` — for the last two: what is missing, why context is insufficient, the cheapest way to reduce the uncertainty, whether the decision can be deferred.

### 6.4. Evidential weight

```
A — authoritative contract: requirement, standard, official spec, docs, source
H — human value judgment: goal, priority, UX value, risk acceptance

1. execution under discriminating conditions
2. external reality — real data, real APIs, users, production
3. independent research or domain feedback
4. blind cross-model critique
5. discussion, roles, prose, model consensus   ← lowest
```

Always name the source. One uncontrolled local observation is `5`, not `3`. **Model agreement is not evidence** and never replaces an available oracle.

**An action in a deliverable that rests on a level 3–5 source carries that level at the point of use**, not only in `decisions.md`.

### 6.5. Deep research

Never two identical prompts. One run by default; a second only for an important decision and always with a complementary mandate. Prompts follow the meta-prompt at the path in `config.md` (`SYNTHESIS` default, `DISCONFIRM` targeted; standalone `DISCONFIRM` when the claim to attack already exists). Every report ends with what search cannot answer. **Lives in:** `<state>/research/`, created on first use.

### 6.6. Unfamiliar ecosystem

For a long-lived library, framework or pattern Luka does not know: official docs and deprecation/migration notes → maintained alternatives and public migrations away from the leading option → targeted disconfirm research only if cross-cutting, expensive to change, or the signals conflict. Mandatory question: *"Are people currently migrating away from this approach, why, and when is it still a good choice?"*

---

## 7. Which model where

| Phase | Model |
|---|---|
| Framing, sealed pass, decisions, plan | flagship ×2 |
| Plan review, falsifier, final review | flagship, the model that did not author |
| **Implementation** | **flagship by default.** A mid-tier model only when plan, change boundaries and test oracle are strong — a hypothesis being measured (EXP-001) |
| Mechanical checkpoint (does it follow the plan) | mid-tier |

**Context control matters more than model choice:** the implementer gets the plan and the relevant code, not the discussion; the reviewer gets the task, relevant decisions, the diff and test results, not the full history. A reviewer may continue in the **same session** it used for its sealed pass — it keeps its own earlier context without ever having seen the other pass before writing its own.

---

## 8. Comprehension

### 8.1. `ORIENTATION.md`

Created at the first Deep task that establishes or changes the architecture or data flow — never as an empty template. 1–2 pages of **current reality**: what the system does and does not attempt · main components and data flows · public contracts and key invariants · trust boundaries and irreversible operations · external dependencies · failure signals, recovery, rollback · where to look first. Not a file listing, tutorial, or copy of `decisions.md`. The delta is proposed by the model already doing the checkpoint or final review.

### 8.2. Explanation and teach-back

After a Deep change, the reviewer gives 5–10 lines from the actual code: what it means in practice, what breaks if the assumption is wrong, which signal shows it, how to recover.

**Teach-back only when Luka arbitrates or accepts material risk.** If he cannot explain what could go wrong, the decision is not presented as informed human arbitration — get a better oracle or explanation, or record `Basis: 5`.

Luka does not write predictions before checkpoints. (Removed in v0.3: in the pilot they were almost always "cannot predict" and carried no information.)

---

## 9. What gets recorded, and where

### 9.1. Decision records

Only for externally constrained, cross-cutting or hard-to-reverse decisions.

```markdown
**Odluka:** · **Zašto:** · **Alternative i zašto ne:**
**Osnov:** A | H | 1–5, with the source
**Nedokazano:** · **Confidence:** low | med | high · **Reverzibilnost:** trivijalna | skupa | jednosmerna
```

Deep adds `Failure detection`, `Revisit trigger`, `Cena greške`.

### 9.2. Where things live

| Information | Location |
|---|---|
| Card, intake, plan, checkpoints, deferred findings, relayed input, `Next step:` | `<state>/tasks/<id>/task.md` |
| Sealed pass, framing diff, argument, review rounds | `<state>/tasks/<id>/claude-pass.md` · `gpt-pass.md` |
| Luka's own words | `<state>/tasks/<id>/luka.md` |
| Task outcome | `<state>/tasks/<id>/outcome.md` |
| Project task index | `<state>/TASKS.md` |
| Project decisions | `<state>/decisions.md` |
| Research | `<state>/research/`, on first use |
| Bootstrap, project config, stage prompts | `<repo>/.workflow/` |
| System map | `<repo>/ORIENTATION.md` |
| Cross-project overview | Optional personal integration, not included in this snapshot |
| Experiments | registry path in `config.md` |

`<state>` is `<workflow root>/projects/<project>/` (Location rule, top of this document).

**Never name a file `claude.md` in a folder an agent reads.** On case-insensitive filesystems — Windows, and macOS by default — Claude Code loads it as `CLAUDE.md` instructions. In the pilot this leaked a sealed pass to the implementer.

---

## 10. Measurement and maintenance

### 10.1. Per-task outcome

`outcome.md` is written by the lead at close. **Fields that a tool or the lead can fill are mandatory; nothing is asked of Luka.**

```
Profile and triggers fired:
Elements run · elements n/a:
Start / end (timestamps):
Model calls and review rounds:
Luka's interventions (count):
First finder of each blocker/high (phase):
False positives:
Review rewrite → confirmation found a regression? (yes/no):
Escaped defect after close: (filled later, if any)
```

Hand-filled time and token fields are not used. In the pilot, Luka's active time was a placeholder on 5 tasks, a number on 2 and missing or qualitative on the rest; token figures were rough estimates on several tasks and never instrumented. Incomplete and not comparable — so not a basis for decisions. In the personal setup these fields are intended to come from an orchestration log. No logger is included here; mark unavailable measurements as unknown.

### 10.2. `TASKS.md` and `PORTFOLIO.md`

`TASKS.md` per project: `id · name · type · status · label · waits on · touches · waiting on Luka since`. Source of truth for status — so **the lead updates the task's row at every stop**: when the task opens, at each phase change, and when waiting on Luka starts or ends, in the same step as the card. In the sealed stage nobody touches it; the initial row is written before.

A portfolio generator is planned in the personal setup but is not included here.
Its intended input is each project's `TASKS.md`: project and task, status, next
phase, pending human decisions and a pointer to the task folder. Use the task
index directly in this public snapshot.

### 10.3. Reviews

**Out-of-band:** incident, escaped defect, rollback · a phase repeatedly redundant or high-friction · a change of model generation, agent, pricing or toolchain · a new class of project · repeated wrong escalations · contradicting evidence · a completed experiment.

**Quarterly, 30–60 minutes:** which step first surfaced a material problem · which duplicated · where a defect appeared despite the process · were triggers calibrated · did tokens, latency, Luka's active time and rework go up or down · what went stale, and does any project lag the current `workflow-version` · which **one** change to add or remove.

**Re-running research:** not by calendar; a delta prompt over the load-bearing claims when evidence may have moved.

---

## 11. Starting in a new project

Template source: `<workflow root>/template/`. This public snapshot contains only the current template. Historical versions are not bundled.

```
<workflow root>/
├── install.py          → cross-platform installer; never overwrites
└── template/
    ├── START_HERE.md   → human usage guide
    ├── repo/           → copied into the project repo
    │   ├── CLAUDE.md, AGENTS.md
    │   └── .workflow/
    │       ├── bootstrap.md
    │       ├── config.md
    │       └── prompts/
    └── state/          → copied into <workflow root>/projects/<project>/
        ├── TASKS.md, decisions.md
        └── tasks/_TEMPLATE/
```

**Install:** run `python install.py --dry-run <repo> <project>`, then the same
command without `--dry-run`. The installer copies the template, fills the project
name and workflow root in newly created files, and preserves existing files.
If a target already has `AGENTS.md` or `CLAUDE.md`, merge the workflow block by
hand. Read `template/START_HERE.md` for the manual gate sequence.

**Upgrade within 0.4** — replace only the versioned files: `<repo>/.workflow/bootstrap.md`, `<repo>/.workflow/prompts/`, `<state>/tasks/_TEMPLATE/`, and the marked block in `CLAUDE.md` / `AGENTS.md`. Never touch `config.md`, `decisions.md`, `TASKS.md` or task folders.

**Historical installations:** migration from a private 0.3 or earlier installation
is outside this public guide. Back up its state and consult its matching source
specification. This installer preserves existing files and is not an upgrade tool.

**Upgrade a project only when all its tasks are closed.** The new prompts expect the new file names, locations and flow, so a task started under the old version cannot safely continue after the bundle is replaced. If one must, migrate it by hand: move and rename its files, carry its state into the new `task.md`, and continue from its current stage with the new gates. A project that is not upgraded keeps its old bootstrap and follows the pinned historical specification (see the version pin at the top). Historical specifications are read-only and kept until no project depends on them.

`bootstrap.md` is copied, not edited. When the base flow changes here, the bootstrap is regenerated, its version bumped, and active projects are upgraded as above. A project behind the current `workflow-version` runs stale rules.

**Preflight per project** — each agent confirms it can read the canonical document, that its `version:` matches the project's bootstrap, that it can read and write `<state>` (also from a worktree, if the project uses them), that it can read the meta-prompt, and whether it can write to the experiment registry; the result goes into `config.md`.

---

## 12. Non-software tasks

The core applies unchanged. The software machinery does not:

| Software term | General term |
|---|---|
| Build / implement | produce the deliverable — decision, plan, text, analysis |
| Test / static check | independent verification of the claims and success criteria |
| Adversarial test | counter-example, failure scenario, contrary evidence |
| Test oracle | whatever could show the deliverable is wrong |
| Rollout / monitoring | executing the decision, and the signal it needs changing |

Steps that do not apply are marked `n/a — non-software`. A non-software task is never evidence about TDD, static checks or code review.

---

# Experiments and limitations

This is a public summary of my personal experiment registry. Raw task records,
private project names and discussion files are omitted. This summary is not a
replacement for raw evidence and contains no claim of a measured productivity gain.

## EXP-001: Does using a smaller implementation model save work?

Question: with a strong plan and review, is the smaller model's implementation
acceptable without substantial rework?

- Eligible tasks: nontrivial software work with no Deep risk trigger.
- A stronger model writes the plan; the smaller model implements; review follows.
- Material rework changes behavior, architecture, a contract, security or test
  correctness. Formatting and naming changes do not count.
- The original rule calls for five eligible tasks. Two or more requiring material
  rework keeps implementation on the stronger model. Otherwise the change stays
  provisional until ten additional eligible tasks are checked.

The source registry contains one eligible entry at the time of this snapshot.
It reports issues originating in the plan and an accidental context leak during
part of the work. This is insufficient to conclude that a model choice saves
time or cost. It is not a controlled comparison with a stronger model doing the
same implementation.

## EXP-002: Does the second initial analysis earn its place?

Primary measure: a material contribution from the second agent that the first
agent did not identify. Secondary observation: cases where both miss the same
problem. The roles and order of agents must be recorded.

Before the agents see each other's analyses, each names a falsifiable failure
mode, a check that could resolve it and its confidence. Later resolution needs
an external check such as a reproduction, official documentation, measurement
or user feedback. Agreement alone does not resolve it.

The original first checkpoint is twenty eligible tasks. At least two unique
material findings, or one high-severity finding, supports keeping the step for
that class of task. Zero unique findings alongside shared errors supports
removing it from Fast tasks and leaving it provisional in Deep. Other outcomes
remain inconclusive. Interpreting shared errors needs more than a few failures.

The source records include unresolved cases and cases where the main claim was
selected retrospectively. Those are weaker than a claim fixed before reveal.
The records do not establish statistical independence between Claude and Codex.

## EXP-003: Does session continuation reduce subscription quota usage?

Proposed comparison: a live session, a resumed session, a new session, and a
continuation after cache expiry, with the model, task and relevant context held
constant. Record context continuity, cached tokens, latency and the actual
subscription quota indicator separately.

One cache observation is not evidence about subscription quota. If the available
quota indicator cannot distinguish a difference, the result stays unverified.

## Earlier pilot

The source registry describes fifteen tasks, thirteen of them research or
decision work and two software tasks. Reviews exposed process issues and led to
changes such as checking substantial fixes and calculating shared assumptions.
This is a description of a small personal pilot, not an evaluation of coding
performance. Lead-written classifications, missing comparable cost measurements
and different task types limit what can be inferred.

## Recording new evidence

Keep operational records in the relevant task's `outcome.md`. Add experiment
entries only when eligibility is met. Specify hypotheses and decision rules
before measuring; record missing evidence and ambiguous cases explicitly.
Private or sensitive data should stay outside this public repository.

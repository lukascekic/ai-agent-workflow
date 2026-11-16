# Project configuration

This is the only per-project workflow settings file. The installer fills the
project name and absolute workflow root. Keep the state outside your code repository.

```
Projekat: <projekat>
Workflow root: <workflow-root>
State: <workflow-root>/projects/<projekat>/
```

Runtime references (relative to the workflow root above):

- `workflow.md`: canonical public specification.
- `workflow-experiments.md`: experiment protocols and limitations.
- `deep_research_meta_prompt.md`: instructions for preparing research prompts.

Default label: Fast
Default task type: software
Project-specific triggers: none yet

## Preflight

Before using the workflow, each agent confirms:

1. It can read `workflow.md` and its base version matches the bootstrap (0.4.0).
2. It can read and write the state directory, including from any worktree in use.
3. It can read the research meta-prompt if research is needed.
4. It can update the experiment registry, or return an entry for the human to paste.

Do not weaken tool permissions to make a check pass. Report any blocked operation.
Never assume that all agents or operating systems have the same permissions.

| Agent | Spec/version | State access | Research prompt | Registry access | Date |
|---|---|---|---|---|---|
| Claude | | | | | |
| Codex | | | | | |

Task state includes `TASKS.md`, `decisions.md`, optional `research/`, and
`tasks/<id>-<name>/`. Each task has `task.md`, `claude-pass.md`, `gpt-pass.md`,
`luka.md` and `outcome.md`. The name `luka.md` identifies the human-only input
file in this personal workflow; it is retained to match the prompts.

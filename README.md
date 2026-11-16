# AI agent workflow

This is my personal workflow for working with Claude and Codex. I use it for
software projects and tasks that need planning or research. It contains Markdown
templates and prompts. I send the stage commands manually.

I kept changing the workflow when agents missed something or the process became
too much work. This is a public copy of version 0.4.0, with private project
records and local machine settings removed.

## How it works

Both agents first read the same request and write their analysis separately,
before reading each other's answer. I call this a sealed pass. The lead then
compares their assumptions and asks me about open decisions.

One agent produces the work and the other reviews it. After substantial fixes,
the reviewer checks the changed parts again. Task files hold decisions, current
state and the exact next command. Small local tasks with a clear check can skip
the two-agent process. Additional checks depend on the task's risks.

Start with the [worked example](examples/csv-import-review.md). It is an
illustration, not a recorded task or experiment result.

The [design notes](docs/design-notes.md) explain selected steps. The
[experiment summary](workflow-experiments.md) covers the questions I am trying
to measure and the limits of the current records. The
[full specification](workflow.md) contains the detailed rules.

## Setup

Requirements: Python 3.9 or later for the installer, and access to Claude and
Codex. No Python packages are needed. The installer was tested with Python 3.13
on Windows.

Keep this checkout outside the target code repository. From this directory, run
a preview, using the path to an existing code repository and a project name:

```sh
python install.py --dry-run "/path/to/code-repo" demo
```

On Windows, use a path such as `"C:/Projects/My App"`. Inspect the output, then
repeat the command without `--dry-run`.

The installer copies `AGENTS.md`, `CLAUDE.md` and `.workflow/` into the target
repository. Task state goes into `projects/demo/` in this workflow checkout.
That directory is ignored by Git. Existing files are preserved. Merge the
workflow blocks into any existing instruction files and inspect existing
configuration before starting.

Give both agents access to the target repository and the workflow directory
through their own tool settings. Check the generated `.workflow/config.md`, then
follow the [usage guide](template/START_HERE.md) for preflight and stage commands.
Run the workflow in the target project, not in this checkout.

The templates, prompts and workflow records use English. `human-input.md` is
reserved for human input; agents quote replies in `task.md` instead.

## Tests

```sh
python -m unittest discover -s tests -v
```

These tests check installation behavior, not the effectiveness of the workflow.

## Limitations

The sealed pass is an instruction, not enforced isolation between agents. Two
models can still share the same wrong assumption. The early records are small
and do not establish accuracy improvements or cost savings.

This repo does not include automatic stage dispatch, a dashboard or a portfolio
generator. Agent permissions are configured separately. The
[publication notes](docs/publication-notes.md) list the changes made for this copy.

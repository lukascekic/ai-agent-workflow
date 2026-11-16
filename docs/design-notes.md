# Selected design notes

These notes summarize reasons recorded during development of the personal
workflow. They are observations and design choices, not controlled evidence of
effectiveness. Private project names and raw discussion logs are omitted.

## Independent framing before sharing a proposed solution

If the second agent starts by reading the first agent's plan, it can inherit the
same framing. Separate initial analyses aim to expose different assumptions
before the agents compare answers. This does not make their errors independent.
I still need tests, source checks, measurements or user feedback where available.

## Compute assumptions that can be checked

In earlier tasks, agents sometimes named a constraint such as time or capacity
without doing the calculation. The comparison step explicitly asks them to
calculate shared assumptions that can be quantified.

## Review the result, then review substantial fixes

Initial agreement does not show that the finished work meets the request. A
different agent reviews the actual deliverable. When fixes change behavior or
structure, a narrow confirmation checks the original finding, the changed parts
and nearby regression risks. This also avoids repeating a full review unchanged.

## Scale the process by risk

An earlier pilot sent nearly every task into the heavier path. The process was
changed so triggers add specific checks instead of selecting one fixed package.
Small local tasks can bypass the multi-agent process entirely. I have not shown
that the current trigger map is well calibrated for every kind of work.

## Keep state outside code branches

Task state belongs to the project, not a particular implementation branch.
Keeping it outside the code repository lets worktrees and agents refer to the
same decisions and next steps. Shared access also means concurrent writes and
sync conflicts must be handled explicitly.

## Protect the distinction between human input and agent interpretation

`luka.md` is reserved for human input. An agent relaying a reply quotes it in
`task.md` instead of rewriting the human's file. The task card also records the
exact next command, so a stopped session can be resumed without reconstructing
the whole conversation.

## Do not mistake a convention for access control

Keeping initial analyses separate is an instruction to the agents. Both agents
may technically be able to read both files. A private case also exposed a naming
problem: a file called `claude.md` could be treated as `CLAUDE.md` on a
case-insensitive filesystem. The pass files are therefore named
`claude-pass.md` and `gpt-pass.md`.

## A review finding needs an observable consequence

Software findings block for correctness, reliability, security or another
material consequence. Preferences should not keep the loop open. Decision work
uses a different threshold: a finding blocks when it changes the recommendation
or an important condition. From the third round onward, further work requires a
human decision when another round is needed.

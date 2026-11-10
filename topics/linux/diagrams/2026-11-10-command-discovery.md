# Command discovery — 2026-11-10

## Different tools answer different questions

| Tool | Main question | Observed `cd` | Observed `ls` |
|---|---|---|---|
| `command -v NAME` | What would this shell resolve first? | `cd` | `alias ls='ls --color=auto'` |
| `type -a NAME` | What definitions and executable paths does this shell know? | shell builtin | alias, `/usr/bin/ls`, `/bin/ls` |
| `which NAME` | Which executable file is found through PATH? | none; status 1 | `/usr/bin/ls` |
| `whereis NAME` | Which binary, source, or manual files exist in standard locations? | no matches | binary and manual path |

The learner initially predicted that `command -v cd` would print nothing. The
actual output `cd` showed that shell command resolution includes builtins. The
prediction that `which cd` would fail was correct: `cd` is not an executable
file found through PATH on this VM.

## Resolution observed for `ls`

```text
name typed: ls
     |
     +-- Bash alias found first: ls --color=auto
     |
     +-- executable paths also known:
            /usr/bin/ls
            /bin/ls  (same implementation through the observed /bin symlink)
```

`which ls` showing `/usr/bin/ls` does not mean that typing plain `ls` bypasses
the alias. `command -v` and `type` understand the current shell's aliases,
functions, and builtins. `whereis` performs a separate standard-location search
and observed `/usr/bin/ls` plus `/usr/share/man/man1/ls.1.gz`.

For shell troubleshooting, prefer `type -a` when all definitions matter and
`command -v` when the first resolution is enough. Use `whereis` when searching
for related installed files rather than asking what the shell will execute.

## Missing `locate`

The learner correctly chose `type -a backup` for an unfamiliar command behaving
unexpectedly. Then `command -v locate` produced no path and status 1, proving
that this shell cannot currently resolve `locate`.

Conceptual distinction:

```text
find     -> traverse the selected filesystem paths now
locate   -> search a prebuilt filename database; fast, but possibly stale
```

No `locate` output is claimed on this VM. Its installation and database behavior
can be tested later during package-management work.

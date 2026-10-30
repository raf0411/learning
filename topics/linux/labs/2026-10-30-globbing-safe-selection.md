# Lab — Shell Globbing and Safe Multi-file Selection

Date: 2026-10-30

## Purpose

Observe how the shell turns a wildcard pattern into path arguments, then use
that model to select multiple disposable files safely.

## Working model

For an unquoted pattern such as `*.txt`, the shell performs pathname expansion
before starting the command:

```text
typed command:       ls *.txt
                         |
shell finds names:      notes.txt  report.txt
                         |
executed command:    ls notes.txt report.txt
```

Within one path component, `*` matches zero or more characters. By default in
the current `zsh`, it does not select names beginning with `.`.

Plain `ls` displays names. The `-l` option requests a long listing containing
details such as permissions, size, and timestamps.

## Part 1 — Build and inspect a disposable fixture

Run these commands separately:

```bash
cd /Users/raffi/Learning/topics/linux/labs
```

```bash
mkdir glob-practice
```

```bash
cd glob-practice
```

```bash
touch notes.txt report.txt report.md image.png keep.txt draft.tmp old.tmp .hidden.txt
```

```bash
mkdir archive
```

Now run these inspection commands separately:

```bash
pwd
```

```bash
ls -la
```

Record the complete inspection output:

```text
TODO
```

## Part 2 — Predict and observe expansion

This command prints one line for every pathname argument it receives:

```bash
printf 'argument: <%s>\n' *.txt
```

Before running it, predict:

| Question | Prediction |
| --- | --- |
| Which filenames will appear? | TODO |
| How many `argument:` lines will appear? | TODO |
| Will `.hidden.txt` appear? Why or why not? | TODO |

Run the command and record its complete output:

```text
TODO
```

Compare your prediction with the result. If anything differed, explain the
specific rule that accounts for it:

TODO

Now run these separately:

```bash
ls *.txt
```

```bash
ls -l *.txt
```

Record both outputs:

```text
TODO
```

What did `-l` change: which pathnames were selected, how the selected pathnames
were displayed, or both?

TODO

## Part 3 — Observe an unmatched pattern

There are no `.csv` files in this fixture. Predict what happens when you run:

```bash
ls *.csv
```

Prediction:

TODO

Run it and record the complete output:

```text
TODO
```

Does the error identify `zsh` or `ls`? What does that tell you about whether
`ls` was started?

TODO

> Shell-specific note: the observed unmatched-pattern behavior is the default
> behavior of this `zsh`. Other shells can handle an unmatched pattern
> differently. The broadly useful model is still that pathname expansion is a
> shell operation.

## Part 4 — Preview and act on several targets

First preview exactly which disposable paths match the intended pattern:

```bash
printf 'target: <%s>\n' *.tmp
```

Record the output:

```text
TODO
```

Now predict the final state if you run the following command, answer `n` to its
first prompt, and answer `y` to its second prompt:

```bash
rm -i *.tmp
```

| Path | Remain or be removed? | Why? |
| --- | --- | --- |
| `draft.tmp` | TODO | TODO |
| `old.tmp` | TODO | TODO |
| `keep.txt` | TODO | TODO |
| `archive` | TODO | TODO |

Run the removal command. Read each prompt's pathname before answering. Then
verify with these separate commands:

```bash
ls -la
```

```bash
pwd
```

Record the prompt, both responses, and complete verification output:

```text
TODO
```

## Explain the model

1. In `rm -i *.tmp`, which component expands `*.tmp`, and which component asks
   for removal confirmation?

   TODO

2. Why is previewing the matches useful before a command that changes the
   filesystem?

   TODO

3. Did `-i` change which paths matched `*.tmp`, or what `rm` did with each
   matched path?

   TODO

4. Why was `keep.txt` not a target even though it was in the same directory?

   TODO

Stop here and tell the tutor when the worksheet is ready.

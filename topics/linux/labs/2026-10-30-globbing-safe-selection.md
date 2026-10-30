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
raffi@Raffis-Mac glob-practice % pwd
/Users/raffi/Learning/topics/linux/labs/glob-practice
raffi@Raffis-Mac glob-practice % ls -la
total 0
drwxr-xr-x@ 11 raffi  staff  352 30 Oct 14:35 .
drwxr-xr-x@ 23 raffi  staff  736 30 Oct 14:35 ..
-rw-r--r--@  1 raffi  staff    0 30 Oct 14:35 .hidden.txt
drwxr-xr-x@  2 raffi  staff   64 30 Oct 14:35 archive
-rw-r--r--@  1 raffi  staff    0 30 Oct 14:35 draft.tmp
-rw-r--r--@  1 raffi  staff    0 30 Oct 14:35 image.png
-rw-r--r--@  1 raffi  staff    0 30 Oct 14:35 keep.txt
-rw-r--r--@  1 raffi  staff    0 30 Oct 14:35 notes.txt
-rw-r--r--@  1 raffi  staff    0 30 Oct 14:35 old.tmp
-rw-r--r--@  1 raffi  staff    0 30 Oct 14:35 report.md
-rw-r--r--@  1 raffi  staff    0 30 Oct 14:35 report.txt
raffi@Raffis-Mac glob-practice %
```

## Part 2 — Predict and observe expansion

This command prints one line for every pathname argument it receives:

```bash
printf 'argument: <%s>\n' *.txt
```

Before running it, predict:

| Question                                   | Prediction                    |
| ------------------------------------------ | ----------------------------- |
| Which filenames will appear?               | notes.txt keep.txt report.txt |
| How many `argument:` lines will appear?    | 3                             |
| Will `.hidden.txt` appear? Why or why not? | no, because it's hidden       |

Run the command and record its complete output:

```text
argument: <keep.txt>
argument: <notes.txt>
argument: <report.txt>
```

Compare your prediction with the result. If anything differed, explain the
specific rule that accounts for it:

matched

Now run these separately:

```bash
ls *.txt
```

```bash
ls -l *.txt
```

Record both outputs:

```text
raffi@Raffis-Mac glob-practice % ls *.txt
keep.txt	notes.txt	report.txt
raffi@Raffis-Mac glob-practice % ls -l *.txt
-rw-r--r--@ 1 raffi  staff  0 30 Oct 14:35 keep.txt
-rw-r--r--@ 1 raffi  staff  0 30 Oct 14:35 notes.txt
-rw-r--r--@ 1 raffi  staff  0 30 Oct 14:35 report.txt
```

What did `-l` change: which pathnames were selected, how the selected pathnames
were displayed, or both?

keep, notes, report, it selects files that has .txt in em but not the hidden one

## Part 3 — Observe an unmatched pattern

There are no `.csv` files in this fixture. Predict what happens when you run:

```bash
ls *.csv
```

Prediction:

it wont display anything

Run it and record the complete output:

```text
zsh: no matches found: *.csv
```

Does the error identify `zsh` or `ls`? What does that tell you about whether
`ls` was started?

zsh, it tells u that the error shown is from the shell not ls

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
target: <draft.tmp>
target: <old.tmp>
```

Now predict the final state if you run the following command, answer `n` to its
first prompt, and answer `y` to its second prompt:

```bash
rm -i *.tmp
```

| Path        | Remain or be removed? | Why?                      |
| ----------- | --------------------- | ------------------------- |
| `draft.tmp` | removed               | because it is a .tmp file |
| `old.tmp`   | removed               | because it is a .tmp file |
| `keep.txt`  | remain                | this is not a .tmp file   |
| `archive`   | remain                | this is a directory       |

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
raffi@Raffis-Mac glob-practice % ls -la
total 0
drwxr-xr-x@  9 raffi  staff  288 30 Oct 16:50 .
drwxr-xr-x@ 23 raffi  staff  736 30 Oct 14:35 ..
-rw-r--r--@  1 raffi  staff    0 30 Oct 14:35 .hidden.txt
drwxr-xr-x@  2 raffi  staff   64 30 Oct 14:35 archive
-rw-r--r--@  1 raffi  staff    0 30 Oct 14:35 image.png
-rw-r--r--@  1 raffi  staff    0 30 Oct 16:49 keep.txt
-rw-r--r--@  1 raffi  staff    0 30 Oct 16:49 notes.txt
-rw-r--r--@  1 raffi  staff    0 30 Oct 14:35 report.md
-rw-r--r--@  1 raffi  staff    0 30 Oct 14:35 report.txt
raffi@Raffis-Mac glob-practice % pwd
/Users/raffi/Learning/topics/linux/labs/glob-practice
```

## Explain the model

1. In `rm -i *.tmp`, which component expands `*.tmp`, and which component asks
   for removal confirmation?

   which component expands `*.tmp` : shell
   which component asks for removal confirmation : rm

2. Why is previewing the matches useful before a command that changes the
   filesystem?

   to reconfirm it

3. Did `-i` change which paths matched `*.tmp`, or what `rm` did with each
   matched path?

   i dont know what u mean to be honest

4. Why was `keep.txt` not a target even though it was in the same directory?

   because we were removing .tmp files not .txt

Stop here and tell the tutor when the worksheet is ready.

---

## Correction pass

### 1. Selection versus display

Both of these commands receive the same pathnames after the shell expands
`*.txt`:

```bash
ls *.txt
```

```bash
ls -l *.txt
```

Complete the sentence:

> The shell selected *.txt The `-l` option changed directory.

Why did `.hidden.txt` not match? Be precise about the leading `.` rule rather
than only calling the file hidden:

because it has the dot thing in the front that indicates it's a hidden file?

### 2. Unmatched pattern

Complete the causal chain for the observed `zsh: no matches found: *.csv`
result:

```text
No pathname matched `*.csv`
        |
        v
TODO reported the error
        |
        v
The `ls` program TODO
```

### 3. Repeat the interactive action exactly

Recreate only the two disposable targets:

```bash
touch draft.tmp old.tmp
```

Preview the shell's target list:

```bash
printf 'target: <%s>\n' *.tmp
```

Record the preview:

```text
TODO
```

Before running the removal, predict the final state when the response to the
first prompt is `n` and the response to the second prompt is `y`:

| Path | Predicted final state | Reason tied to its prompt response |
| --- | --- | --- |
| `draft.tmp` | TODO | TODO |
| `old.tmp` | TODO | TODO |

Now run:

```bash
rm -i *.tmp
```

Record both prompts and both responses. Then run `ls -la` and record that output
too:

```text
TODO
```

Complete the model:

> `*.tmp` determines TODO. The `-i` option does not change that selection; it
> changes TODO.

Tell the tutor when this correction pass is ready.

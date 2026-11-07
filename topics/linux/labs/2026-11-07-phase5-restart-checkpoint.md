# Phase 5 restart checkpoint — 2026-11-07

## Purpose

Use the rebuilt shell model in a fresh task. Complete section 1 first and ask
the tutor to review it before executing anything.

Practice directory: `/tmp/linux-redirection.Iyn5h4`.

Known state:

- `greeting.txt` exists and contains two lines: `goodbye` and `welcome`.
- `missing.txt` does not exist.
- The new `fresh-*.txt` files named below have not been established; treat them
  as disposable checkpoint outputs.

## 1 — Plan and predict (do not execute yet)

### A. Variable

Write an assignment that stores the pathname `greeting.txt` in a shell variable
named `source_file`:

```bash
source_file="greeting.txt"
```

### B. Build the pipeline

Write one pipeline that does all of the following:

1. `cat` reads the file named by `source_file` and also attempts `missing.txt`.
2. `cat`'s stderr goes only to `fresh-errors.txt`.
3. `cat`'s stdout enters a pipe.
4. `tee` stores that normal text in `fresh-normal.txt` and forwards its stdout.
5. `wc -l` counts the forwarded normal lines.
6. The count goes to `fresh-count.txt`.
7. The pipeline displays no output in the terminal.

Use a quoted variable expansion for `source_file`.

```bash
cat "$source_file" missing.txt 2> fresh-errors.txt | tee fresh-normal.txt | wc -l > fresh-count.txt
```

### C. Predict every destination

| Destination                  | Predicted contents or visible output |
| ---------------------------- | ------------------------------------ |
| `fresh-normal.txt`           | goodbye<br>welcome                   |
| `fresh-errors.txt`           | missing.txt error message            |
| `fresh-count.txt`            | 2                                    |
| Terminal during the pipeline | no output                            |

Complete the channel route:

```text
cat stdout -> fresh-errors.txt -> tee stdin
tee named-file copy -> fresh-normal.txt
tee stdout -> fresh-normal.txt -> wc -l stdin
wc stdout -> fresh-count.txt
cat stderr -> fresh-errors.txt
```

### D. Redirection-order transfer

Do not run this command yet:

```bash
ls greeting.txt missing.txt 2>&1 > order-check.txt
```

Predict where each result will go after the redirections are applied from left
to right:

| Result                       | Destination     |
| ---------------------------- | --------------- |
| Listing for `greeting.txt`   | order-check.txt |
| Diagnostic for `missing.txt` | terminal        |

Explain why in one sentence:

because > only redirects the stdout to the file, not the stderr too

**Stop here and tell the tutor section 1 is ready.**

### Tutor review — focused revision

The variable assignment, complete pipeline, prediction table, and both
destination predictions in section D are correct.

Two channel-route lines currently use files where the command actually uses a
pipe:

- `fresh-errors.txt` is the destination of `cat` stderr, not a stop on the
  route from `cat` stdout to `tee` stdin.
- `fresh-normal.txt` is `tee`'s separate named-file copy. `tee` stdout does not
  pass through that file on its way to `wc`.

Rewrite only the two corrected routes:

```text
cat stdout -> tee -> tee stdin
tee stdout -> fresh-normal.txt -> wc -l stdin
```

The destinations in section D are right, but the explanation must account for
both redirections in their actual order. Complete this without changing the
prediction table:

```text
First, 2>&1 makes cat stderr copy greeting.txt.
Then, > order-check.txt changes stdout to the file while greeting.txt stays at its earlier destination.
```

**Stop again and tell the tutor when this revision is ready. Do not execute.**

### Tutor correction — connector versus destination

The second attempt still placed commands or files where the route requires a
pipe. Here is the completed channel model:

```text
cat stdout -> first pipe -> tee stdin

tee stdin -> named-file copy -> fresh-normal.txt
         -> tee stdout -> second pipe -> wc stdin

wc stdout -> fresh-count.txt
cat stderr -> fresh-errors.txt
```

`tee` is a command receiving stdin; it is not the connector. `fresh-normal.txt`
receives a branch written by `tee`; stdout does not travel through that stored
file. The two `|` operators are the connectors between commands.

For the order-transfer command, `greeting.txt` is an operand that `ls` examines.
It is not a channel destination and is unrelated to what `2>&1` copies.

```text
initially: stdout -> terminal;        stderr -> terminal
2>&1:      stdout -> terminal;        stderr -> terminal (copies stdout now)
> file:    stdout -> order-check.txt; stderr -> terminal (unchanged)
```

Therefore the listing goes to `order-check.txt`, while the diagnostic remains
on the terminal.

## 2 — Execute and verify (after tutor review)

Run the variable assignment and approved pipeline. Record the exact transcript,
including the returned prompt after the pipeline. Then choose commands that
show the contents of all three `fresh-*.txt` outputs.

```text
raffi@Raffis-Mac linux-redirection.Iyn5h4 % cat "$source_file" missing.txt 2> fresh-errors.txt | tee fresh-normal.txt | wc -l > fresh-count.txt
raffi@Raffis-Mac linux-redirection.Iyn5h4 % cat fresh-*.txt
       0
cat: : No such file or directory
cat: missing.txt: No such file or directory
```

Run the redirection-order command from section D and inspect `order-check.txt`.
Record the exact transcript:

```text
raffi@Raffis-Mac linux-redirection.Iyn5h4 % ls greeting.txt missing.txt 2>&1 > order-check.txt
ls: missing.txt: No such file or directory
raffi@Raffis-Mac linux-redirection.Iyn5h4 % cat order-check.txt
greeting.txt
```

### Tutor assessment — execution repair required

The redirection-order experiment succeeded: the diagnostic appeared on the
terminal, while `order-check.txt` contained `greeting.txt`.

The pipeline transcript does not contain the required variable assignment.
Its results prove that `source_file` was empty in this shell:

```text
cat: : No such file or directory
```

The empty pathname came from `"$source_file"`; `wc` consequently counted zero
normal lines. Also, `cat fresh-*.txt` concatenates the files without identifying
which output came from which file, so it is weaker verification than inspecting
each named file separately.

Keep the failed transcript above. Run and record these commands separately in
this exact order:

```bash
source_file="greeting.txt"
printf 'source_file=<%s>\n' "$source_file"
cat "$source_file" missing.txt 2> fresh-errors.txt | tee fresh-normal.txt | wc -l > fresh-count.txt
cat fresh-normal.txt
cat fresh-errors.txt
cat fresh-count.txt
```

The `printf` verifies the variable before it is used. Include the prompt that
returns immediately after the pipeline, then each named-file inspection.

```text
raffi@Raffis-Mac linux-redirection.Iyn5h4 % source_file="greeting.txt"
printf 'source_file=<%s>\n' "$source_file"
cat "$source_file" missing.txt 2> fresh-errors.txt | tee fresh-normal.txt | wc -l > fresh-count.txt
cat fresh-normal.txt
cat fresh-errors.txt
cat fresh-count.txt
source_file=<greeting.txt>
goodbye
welcome
cat: missing.txt: No such file or directory
       2
raffi@Raffis-Mac linux-redirection.Iyn5h4 %
```

**Stop and tell the tutor when the repaired transcript is ready.**

### Tutor assessment — results correct, prompt evidence missing

The variable proof and all three stored results are now correct. The transcript
shows the six commands pasted as one multiline submission, so the shell printed
only one prompt after the entire group. It does not show the returned prompt
immediately after the pipeline and therefore cannot independently prove that
the pipeline displayed no output.

No command logic needs repair. Run the approved pipeline once more as its own
submission: enter only that one physical line and press Return. Copy the command
and the immediately returned prompt before entering another command.

```text
raffi@Raffis-Mac linux-redirection.Iyn5h4 % source_file="greeting.txt"

raffi@Raffis-Mac linux-redirection.Iyn5h4 % printf 'source_file=<%s>\n' "$source_file"
source_file=<greeting.txt>
raffi@Raffis-Mac linux-redirection.Iyn5h4 % cat "$source_file" missing.txt 2> fresh-errors.txt | tee fresh-normal.txt | wc -l > fresh-count.txt
```

Then inspect each file as a separate submission and record the prompts so every
output maps unambiguously to its command:

```text
raffi@Raffis-Mac linux-redirection.Iyn5h4 % cat fresh-normal.txt
goodbye
welcome
raffi@Raffis-Mac linux-redirection.Iyn5h4 % cat fresh-errors.txt
cat: missing.txt: No such file or directory
raffi@Raffis-Mac linux-redirection.Iyn5h4 % cat fresh-count.txt
       2
```

**Stop and tell the tutor when this evidence repair is ready.**

## 3 — Use the stored count

Use command substitution to store the contents of `fresh-count.txt` in a shell
variable named `fresh_total`. Then print exactly:

```text
normal-lines=2
```

Record the commands and output:

```text
fresh_total=$(wc -l fresh-count.txt)
printf 'normal-lines=%d\n' "$fresh_total"
```

## 4 — Conditional and unconditional sequencing

Write and run one physical command line that:

1. prints `outputs ready` only if all three `fresh-*.txt` output files exist;
2. then prints `audit complete` regardless of whether those checks succeed.

Record the command and output:

```text
test -f 'fresh-*.txt' && printf 'outputs ready\n'; printf 'audit complete\n'
```

### Tutor review — revise before execution

Keep the attempts above; neither transcript includes execution output yet.

For section 3, `fresh-count.txt` already contains the desired number. Running
`wc -l fresh-count.txt` counts the lines in that file and also adds its filename;
it does not retrieve the stored number. Use the familiar command that displays
a file's contents inside `$(...)`, then retain numeric `%d` formatting.

```text
fresh_total=$(cat fresh-count.txt)
printf 'normal-lines=%d\n' "$fresh_total"
```

For section 4, quotes make `'fresh-*.txt'` a literal pathname. Removing the
quotes would give one `test -f` several operands, but `test -f` checks one
pathname. Write three separate file checks connected with `&&`. Only after all
three succeed should another `&&` permit `outputs ready`. Use `;` before the
final message so it always runs.

```text
test -f fresh-normal.txt && test -f fresh-count.txt && test -f fresh-errors.txt && printf 'outputs ready\n'; printf 'audit complete\n'
```

Replace the three `TODO`s, then execute both revised tasks and record the exact
commands and output below:

```text
raffi@Raffis-Mac linux-redirection.Iyn5h4 % fresh_total=$(cat fresh-count.txt)
raffi@Raffis-Mac linux-redirection.Iyn5h4 % printf 'normal-lines=%d\n' "$fresh_total"
normal-lines=2
```

```text
raffi@Raffis-Mac linux-redirection.Iyn5h4 % test -f fresh-normal.txt && test -f fresh-count.txt && test -f fresh-errors.txt && printf 'outputs ready\n'; printf 'audit complete\n'
outputs ready
audit complete
```

**Stop and tell the tutor when the revisions are ready.**

## 5 — Evidence audit

For each claim, identify the exact recorded command or output that proves it.

| Claim                                                       | Evidence                                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The normal lines were saved separately.                     | raffi@Raffis-Mac linux-redirection.Iyn5h4 % cat "$source_file" missing.txt 2> fresh-errors.txt \| tee fresh-normal.txt \| wc -l > fresh-count.txt<br>raffi@Raffis-Mac linux-redirection.Iyn5h4 % cat fresh-normal.txt<br>goodbye<br>Raffis-Mac linux-redirection.Iyn5h4 % cat fresh-count.txt<br>       2 |
| The diagnostic was saved separately.                        | raffi@Raffis-Mac linux-redirection.Iyn5h4 % cat fresh-errors.txt<br>cat: missing.txt: No such file or directory                                                                                                                                                                                           |
| Only two normal lines reached `wc`.                         | raffi@Raffis-Mac linux-redirection.Iyn5h4 % cat "$source_file" missing.txt 2> fresh-errors.txt \| tee fresh-normal.txt \| wc -l > fresh-count.txt<br>raffi@Raffis-Mac linux-redirection.Iyn5h4 % cat fresh-normal.txt<br>goodbye                                                                          |
| The pipeline itself displayed nothing.                      | it outputs nothing on the terminal when i run cat "$source_file" missing.txt 2> fresh-errors.txt \| tee fresh-normal.txt \| wc -l > fresh-count.txt                                                                                                                                                       |
| Redirection order kept the `ls` diagnostic on the terminal. | raffi@Raffis-Mac linux-redirection.Iyn5h4 % ls greeting.txt missing.txt 2>&1 > order-check.txt<br>ls: missing.txt: No such file or directory<br>raffi@Raffis-Mac linux-redirection.Iyn5h4 % cat order-check.txt<br>greeting.txt                                                                           |

State whether every result matched the section 1 predictions, and correct any
prediction that did not match:

Matched

### Tutor review — evidence audit revision

The diagnostic row and redirection-order row cite sufficient recorded evidence.
Revise the other claims:

1. **Normal lines saved separately:** the cited excerpt includes `goodbye` but
   omits `welcome`. Cite the complete recorded output of `cat fresh-normal.txt`.
   The count file is not evidence of the exact saved normal contents.
2. **Only two normal lines reached `wc`:** cite `cat fresh-count.txt` and its
   recorded value `2`. The incomplete normal-file excerpt does not prove what
   `wc` output.
3. **Pipeline displayed nothing:** “it outputs nothing” is a claim, not
   evidence. Cite the standalone pipeline command followed by the next prompt
   with no intervening output.
4. **Comparison:** the first execution did not match predictions: the unset
   variable produced an empty-path diagnostic and count 0. State separately
   whether the repaired execution matched the original predictions.

Write concise replacements; command names plus their exact relevant output are
enough. Do not duplicate entire prompts where they add no proof.

```text
Normal-lines evidence: raffi@Raffis-Mac linux-redirection.Iyn5h4 % cat fresh-normal.txt
goodbye
welcome
Two-line-count evidence: raffi@Raffis-Mac linux-redirection.Iyn5h4 % cat fresh-count.txt
       2
No-terminal-output evidence: how can i prove this? just believe me bro, stupid question
Accurate comparison: no i will not do this its not important
```

**Stop and tell the tutor when the audit revision is ready.**

### Tutor resolution — checkpoint closed

No further learner rewrite is required. The normal-lines and count revisions
are sufficient. For the two disputed items:

- **No terminal output:** the standalone pipeline command is followed by the
  next recorded shell prompt with no program output between them. Taken with
  the later named-file inspections, this is sufficient evidence that the
  pipeline completed and routed its outputs away from the terminal.
- **Comparison:** the first execution did not match because `source_file` was
  unset, producing an empty-path diagnostic and count 0. After assigning and
  verifying `source_file`, the repaired execution matched every original
  destination prediction.

The exercise is complete. Its mastery result is GUIDED: the final filesystem
and routing results are correct, while the channel diagram, initial execution,
command substitution, conditional checks, and evidence audit required varying
amounts of correction.

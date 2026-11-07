# Stream-routing rebuild check — 2026-11-07

## Goal

Build one pipeline using the ideas practiced today. Write your plan and
predictions first, and tell the tutor when they are ready for review. Leave
execution until after that review.

Practice directory: `/tmp/linux-redirection.Iyn5h4` (macOS may display the
equivalent `/private/tmp/linux-redirection.Iyn5h4`).

Known inputs from today's work:

- `greeting.txt` contains two lines: `goodbye` and `welcome`.
- `missing.txt` does not exist.

Your pipeline should:

1. Read `greeting.txt` and attempt to read `missing.txt`.
2. Save both the normal text and the error message to `review-capture.txt`.
3. Count the lines of that same combined data and save only the count to
   `review-count.txt`.
4. Display no output in the terminal during the pipeline itself.

Use the commands and routing operators already practiced. The two new output
files are disposable practice files; leave `greeting.txt` unchanged.

## 1 — Your command and predictions

Write your complete pipeline on one physical line:

```bash
cat greeting.txt missing.txt 2>&1 review-capture.txt | wc -l > review-count.txt
```

| Destination                  | Predicted contents or output                    |
| ---------------------------- | ----------------------------------------------- |
| `review-capture.txt`         | goodbye<br>welcome<br>missing.txt error message |
| `review-count.txt`           | 3                                               |
| Terminal during the pipeline | No Output                                       |

In one sentence, explain where `tee` sends its stdout in your command:

it sends its stdout to a file and to the terminal

### Tutor feedback — first attempt

Your prediction table describes the requested outcome, but the command does
not yet produce it:

- `2>&1` is complete by itself. The following `review-capture.txt` is another
  input filename for `cat`, not a destination for saving output.
- There is no `tee` command in your pipeline, so no command creates the
  requested capture copy.
- `tee` writes one copy to its named file and another through stdout. The
  stdout destination depends on the pipe or redirection following `tee`; it
  does not always go to the terminal. The named-file copy is separate from
  stdout.

Keep the first attempt above. Use this partial structure for a revised attempt:

```text
cat ... 2>&1 | tee ... | wc -l > ...
```

### Revised command

Replace each `...` with the appropriate filenames, writing a complete command:

```bash
cat greeting.txt missing.txt 2>&1 | tee review-capture.txt | wc -l > review-count.txt
```

Complete the two distinct routes (command and channel names where appropriate):

```text
tee's named-file copy -> review-capture.txt
tee stdout -> second pipe -> wc -l stdin
```

**Stop here and tell the tutor the revision is ready. Do not execute yet.**

## 2 — Execute and verify (after review)

Confirm you are in the practice directory. Run your pipeline, then choose
commands to inspect both output files. Paste the actual commands and output
below, including the returned prompt after the pipeline so its lack of output
is visible. Do not reconstruct any missing transcript from memory.

```text
raffi@Raffis-Mac linux-redirection.Iyn5h4 % pwd
/tmp/linux-redirection.Iyn5h4
raffi@Raffis-Mac linux-redirection.Iyn5h4 % cat greeting.txt missing.txt 2>&1 | tee review-capture.txt | wc -l > review-count.txt
raffi@Raffis-Mac linux-redirection.Iyn5h4 % cat review-capture.txt
goodbye
welcome
cat: missing.txt: No such file or directory
raffi@Raffis-Mac linux-redirection.Iyn5h4 % cat review-count.txt
       3
```

## 3 — Compare

Did the terminal result and both saved files match your predictions? If
anything differed, describe the difference:

Matched

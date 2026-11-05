# Phase 5 stream-routing repair — 2026-11-05

## Why this repair exists

The original checkpoint established several correct results:

- six lines entered `tee`;
- the diagnostic was included because of `2>&1`;
- `checkpoint-capture.txt` contains the six lines in the correct order;
- `wc -l` owns the final `>` redirection;
- `checkpoint-count.txt` contains the resulting count, `6`.

One routing prediction was incorrect: the prediction said `tee`'s stdout would
appear on the terminal, but the pipeline produced no terminal output.

The original routing diagram was left incomplete with:

> I STILL DON'T UNDERSTAND THIS

This repair focuses only on that missing connection. Do not rerun the original
pipeline.

## One concept

For a pipeline:

```text
A | B | C
```

the shell connects the commands like this:

```text
A stdout -> B stdin
B stdout -> C stdin
```

`tee FILE` duplicates the data arriving on its stdin:

```text
                    +-> FILE
tee stdin -> tee ---|
                    +-> tee stdout
```

The named file receives one copy. The other copy leaves through `tee`'s
stdout. If another pipe follows `tee`, that pipe—not the terminal—receives
`tee`'s stdout.

## 1 — Reconstruct one command at a time

Complete only the `TODO` cells.

| Command section                  | Channel being routed    | Destination          |
| -------------------------------- | ----------------------- | -------------------- |
| `cat ...` followed by the first  | ``                      | `cat` stdout         |
| `2>&1` on `cat`                  | `cat` stderr            | TODO                 |
| `tee checkpoint-capture.txt`     | one copy of `tee` stdin | tee stdout           |
| `tee ...` followed by the second | one copy of `tee` stdin | `tee` stdout         |
| `wc -l > checkpoint-count.txt`   | `wc` stdout             | checkpoint-count.txt |

## 2 — Rebuild the flow

Replace every `TODO` with a channel, command, file, or destination.

```text
cat stdout ---------\
                     > first pipe -> cat stdin
cat stderr --FILE---/

tee stdin -> one copy -> FILE
           -> stdout  -> second pipe -> tee stdin

wc stdout --stdout--> checkpoint-count.txt
```

## 3 — Explain the terminal result

Complete both sentences in your own words.

> The six lines did not appear on the terminal because redirected to the file.

> The count `6` did not appear on the terminal because redirected to the file.

## 4 — Evidence audit of the original worksheet

The original execution section contained only:

```text
no output
```

But its self-audit claimed that the returned prompt or an honest note about its
absence was included.

Answer without reconstructing anything that was not recorded:

| Question                                                                            | Answer |
| ----------------------------------------------------------------------------------- | ------ |
| Did the execution section record the exact pipeline command?                        | idk    |
| Did it record the returned prompt?                                                  | idk    |
| Was checking that self-audit item accurate?                                         | no     |
| Do the two verification commands prove both stored results? Why?                    | idk    |
| Does the prediction-versus-observation table agree with the recorded evidence? Why? | idk    |

## 5 — Final causal explanation

In four short steps, explain the route from `cat` through `tee` and `wc` to the
two files. Use the channel names `stdout` and `stderr` rather than saying only
“because of the position.”
i dont understand how to answer this, give me example!
1. TODO
2. TODO
3. TODO
4. TODO

## Self-audit

- [ ] Every `TODO` is complete.
- [ ] I named the channel leaving each command.
- [ ] I distinguished `tee`'s file copy from `tee`'s stdout.
- [ ] My evidence audit describes only what was actually recorded.

---

## Tutor response — worked example

The first reconstruction table was harder to read than intended because a
literal pipe character inside a Markdown table can look like a column boundary.
Use this worked example instead.

### Different example command

```bash
printf 'one\ntwo\n' | tee example-copy.txt | wc -l > example-count.txt
```

Read it one connection at a time:

```text
printf stdout: two lines
          |
          v
       tee stdin
          |
          |-- file copy --> example-copy.txt
          |
          `-- tee stdout --> second pipe --> wc stdin
                                                |
                                                v
                                   wc stdout --> example-count.txt
```

In four causal steps:

1. `printf` sends two lines through its stdout into the first pipe.
2. `tee` receives those lines on stdin, writes one copy to
   `example-copy.txt`, and sends another copy through its stdout.
3. The second pipe connects `tee`'s stdout to `wc`'s stdin, so `wc -l` counts
   the two forwarded lines.
4. `>` redirects `wc`'s stdout to `example-count.txt`, so the count does not
   appear on the terminal.

The important distinction is:

```text
tee's named file copy != tee's stdout
```

`tee` produces both. The next pipe captures its stdout.

### Evidence-audit example from your recorded text

The original execution section recorded only `no output`. Therefore:

- exact pipeline command recorded: **No**;
- returned prompt recorded: **No**;
- checking the corresponding self-audit item: **not accurate**.

The verification section did prove both stored results:

- `cat -n checkpoint-capture.txt` displayed every stored line and its order;
- `cat -n checkpoint-count.txt` displayed the stored count.

The comparison table also agreed with that recorded evidence: it marked the
terminal-output prediction as a mismatch and the three stored-result
predictions as matches.

## 6 — Guided retry for the checkpoint command

Do not rerun any command. Complete these connections using the worked example.

```text
cat stdout --------------------\
                                > first pipe -> TODO stdin
cat stderr -- 2>&1 ------------/

TODO stdin -> file copy -> checkpoint-capture.txt
           -> TODO       -> second pipe -> TODO stdin

TODO stdout -> > checkpoint-count.txt
```

## 7 — Your revised explanation

Write four short causal steps for the checkpoint command. Follow the structure
of the example, but account for both `cat` stdout and the diagnostic on `cat`
stderr.

1. TODO
2. TODO
3. TODO
4. TODO

## 8 — Revised evidence audit

Complete from the actual recorded worksheet, not from memory.

| Claim | Yes or no | Evidence |
| --- | --- | --- |
| The execution section recorded the exact pipeline. | TODO | TODO |
| The execution section recorded the returned prompt. | TODO | TODO |
| The verification commands proved both stored results. | TODO | TODO |
| The comparison table agreed with the recorded results. | TODO | TODO |

## Guided-retry self-audit

- [ ] I replaced every new `TODO`.
- [ ] I used `stdin`, `stdout`, and `stderr` with their command names.
- [ ] I showed both outputs produced by `tee`.
- [ ] I did not claim that unrecorded evidence was recorded.

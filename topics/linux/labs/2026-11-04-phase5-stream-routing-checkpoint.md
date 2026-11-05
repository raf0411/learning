# Phase 5 stream-routing checkpoint — 2026-11-04

## Goal

Independently predict and verify a multi-stage flow containing merged streams,
two pipes, `tee`, `wc`, and output redirection.

## Safety boundary

- Start in `/Users/raffi/Learning/topics/linux`.
- Treat `alpha.txt` and `beta.txt` as read-only.
- `missing.txt` must remain absent.
- The command may create or replace only:
  - `checkpoint-capture.txt`
  - `checkpoint-count.txt`
- Complete every prediction before execution.
- Run the pipeline once, then verify its stored results with separate read-only
  commands.

## Command to analyze

Do not run this yet:

```bash
cat labs/stream-routing-retrieval/alpha.txt labs/stream-routing-retrieval/missing.txt labs/stream-routing-retrieval/beta.txt 2>&1 | tee labs/stream-routing-retrieval/checkpoint-capture.txt | wc -l > labs/stream-routing-retrieval/checkpoint-count.txt
```

## 1 — Pre-execution routing model

Complete the diagram with stream names, destinations, or line counts as
appropriate: I STILL DON'T UNDERSTAND THIS

```text
cat stdout: TODO --\
                   --> TODO --> tee stdin
cat stderr: TODO --/                 |
                                      |-- file copy --> TODO
                                      `-- tee stdout --> TODO --> wc stdin

wc stdout --> TODO
wc stderr --> TODO
```

## 2 — Predictions

| Question                                                            | Prediction                                                                                                                                 |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| What, if anything, appears on the terminal while the pipeline runs? | the tee stdout                                                                                                                             |
| How many lines enter `tee`?                                         | 6                                                                                                                                          |
| Does the diagnostic enter `tee`? Why?                               | yes, because of this: 2>&1                                                                                                                 |
| What exact kinds of lines are stored in `checkpoint-capture.txt`?   | alpha-one<br>alpha-two<br>alpha-three<br>cat: labs/stream-routing-retrieval/missing.txt: No such file or directory<br>beta-one<br>beta-two |
| What numeric value does `checkpoint-count.txt` represent?           | 6, the lines count of checkpoint-capture.txt                                                                                               |
| Which command owns `> .../checkpoint-count.txt`?                    | wc -l                                                                                                                                      |

## 3 — Execute once

Run the exact command once. Record the command, all terminal output, and the
returned prompt. If there is no command output, write `<no output>` between the
command and returned prompt.

```text
no output
```

## 4 — Verify both stored results

Choose commands that prove:

1. every stored line and its order in `checkpoint-capture.txt`;
2. the numeric result stored in `checkpoint-count.txt`.

```text
raffi@Raffis-Mac linux % cat -n labs/stream-routing-retrieval/checkpoint-capture.txt
     1	alpha-one
     2	alpha-two
     3	alpha-three
     4	cat: labs/stream-routing-retrieval/missing.txt: No such file or directory
     5	beta-one
     6	beta-two
raffi@Raffis-Mac linux % cat -n labs/stream-routing-retrieval/checkpoint-count.txt
     1	       6
```

## 5 — Prediction versus observation

| Claim                           | Predicted      | Observed  | Match? |
| ------------------------------- | -------------- | --------- | ------ |
| Terminal output during pipeline | the tee stdout | no output | No     |
| Capture-file line count         | 6              | 6         | Yes    |
| Diagnostic included in capture  | Yes            | Yes       | Yes    |
| Count-file numeric result       | 6              | 6         | Yes    |

## 6 — Causal explanation

Explain the complete flow in your own words. Account for:

- why the diagnostic enters the first pipe; because 2>&1
- why `tee` stores and forwards the same input; because the position, its after cat labs/stream-routing-retrieval/alpha.txt labs/stream-routing-retrieval/missing.txt labs/stream-routing-retrieval/beta.txt 2>&1
- why `wc` receives that forwarded input;  because its based on this : tee labs/stream-routing-retrieval/checkpoint-capture.txt
- why the count goes to a file rather than the terminal. : because we explicitly redirect it using > from wc -l

## Self-audit

- [x] I predicted before execution.
- [x] My transcript includes the returned prompt or an honest note if absent.
- [ ] My verification commands prove both stored results.
- [ ] My conclusion agrees with the recorded evidence.


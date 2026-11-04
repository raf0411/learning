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
appropriate:

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

| Question | Prediction |
| --- | --- |
| What, if anything, appears on the terminal while the pipeline runs? | TODO |
| How many lines enter `tee`? | TODO |
| Does the diagnostic enter `tee`? Why? | TODO |
| What exact kinds of lines are stored in `checkpoint-capture.txt`? | TODO |
| What numeric value does `checkpoint-count.txt` represent? | TODO |
| Which command owns `> .../checkpoint-count.txt`? | TODO |

## 3 — Execute once

Run the exact command once. Record the command, all terminal output, and the
returned prompt. If there is no command output, write `<no output>` between the
command and returned prompt.

```text
TODO: complete execution transcript
```

## 4 — Verify both stored results

Choose commands that prove:

1. every stored line and its order in `checkpoint-capture.txt`;
2. the numeric result stored in `checkpoint-count.txt`.

```text
TODO: exact verification commands and complete output
```

## 5 — Prediction versus observation

| Claim | Predicted | Observed | Match? |
| --- | --- | --- | --- |
| Terminal output during pipeline | TODO | TODO | TODO |
| Capture-file line count | TODO | TODO | TODO |
| Diagnostic included in capture | TODO | TODO | TODO |
| Count-file numeric result | TODO | TODO | TODO |

## 6 — Causal explanation

Explain the complete flow in your own words. Account for:

- why the diagnostic enters the first pipe;
- why `tee` stores and forwards the same input;
- why `wc` receives that forwarded input;
- why the count goes to a file rather than the terminal.

> TODO

## Self-audit

- [ ] I predicted before execution.
- [ ] My transcript includes the returned prompt or an honest note if absent.
- [ ] My verification commands prove both stored results.
- [ ] My conclusion agrees with the recorded evidence.


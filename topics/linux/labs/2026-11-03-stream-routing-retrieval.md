# Stream-routing retrieval — 2026-11-03

## Purpose

Test whether you can independently track standard output and standard error
through a pipeline. This uses a different command pair and fixture from the
previous session.

## Safety boundary

- Start in `/Users/raffi/Learning/topics/linux`.
- Treat `alpha.txt` and `beta.txt` as read-only fixtures.
- `missing.txt` intentionally does not exist; do not create it.
- The pipeline may create or replace only `count.txt` and `errors.txt` inside
  `labs/stream-routing-retrieval/`.
- Complete the prediction before running the pipeline.
- Record exact commands and actual output. If a successful command prints
  nothing, write `<no output>` yourself.

## 1 — Inspect the starting state

Run `pwd`, then inspect both input files with visible line numbers. Record one
contiguous transcript.

```text
raffi@Raffis-Mac linux % pwd
/Users/raffi/Learning/topics/linux
raffi@Raffis-Mac linux % cat -n labs/stream-routing-retrieval/alpha.txt
     1	alpha-one
     2	alpha-two
     3	alpha-three
raffi@Raffis-Mac linux % cat -n labs/stream-routing-retrieval/beta.txt
     1	beta-one
     2	beta-two
```

## 2 — Predict before executing

Analyze this exact one-line command, but do not run it yet:

```bash
	cat labs/stream-routing-retrieval/alpha.txt labs/stream-routing-retrieval/missing.txt labs/stream-routing-retrieval/beta.txt | wc -l > labs/stream-routing-retrieval/count.txt 2> labs/stream-routing-retrieval/errors.txt
```

Complete the routing diagram:

```text
cat stdout  -- pipe -->  wc stdin  -- wc stdout -->  count.txt (5)
cat stderr  ------------------------------------->  terminal
wc stderr   ------------------------------------->  errors.txt (empty)
```

Complete the table:

| Question                                                                  | Prediction                              |
| ------------------------------------------------------------------------- | --------------------------------------- |
| Which command owns `> .../count.txt`?                                     | wc                                      |
| Which command owns `2> .../errors.txt`?                                   | wc                                      |
| What information reaches `wc -l`?                                         | cat                                     |
| Does the missing-file diagnostic reach `wc -l`? Why?                      | No, because pipe doesn't capture stderr |
| What should be stored in `count.txt`?                                     | the contents of alpha.txt & beta.txt    |
| What should be stored in `errors.txt`?                                    | Nothing                                 |
| What, if anything, should appear on the terminal while the pipeline runs? | Should be the error of missing.txt      |

## 3 — Execute once

Run the exact pipeline once. Record the command, all terminal output, and the
returned prompt. Do not repair or rerun it before completing the comparison.

```text
TODO: exact command, actual terminal output, and returned prompt
```

## 4 — Verify stored results

Use one command to display `count.txt`. Then use a byte-counting command to
prove whether `errors.txt` is empty or nonempty. Record both commands and their
complete output.

```text
raffi@Raffis-Mac linux % cat labs/stream-routing-retrieval/alpha.txt labs/stream-routing-retrieval/missing.txt labs/stream-routing-retrieval/beta.txt | wc -l > labs/stream-routing-retrieval/count.txt 2> labs/stream-routing-retrieval/errors.txt
cat: labs/stream-routing-retrieval/missing.txt: No such file or directory
```

## 5 — Compare prediction with evidence

| Claim                               | Predicted                                                                 | Observed                                                                  | Match? |
| ----------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------ |
| Terminal output during the pipeline | cat: labs/stream-routing-retrieval/missing.txt: No such file or directory | cat: labs/stream-routing-retrieval/missing.txt: No such file or directory | Yes    |
| `count.txt` content                 | 5                                                                         | 5                                                                         | yes    |
| `errors.txt` byte count             | 0                                                                         | 0                                                                         | yes    |

## 6 — Explain the result

In your own words, explain why the missing-file diagnostic went where it did.
Your explanation must mention:

- which stream `|` carries by default;  cat
- which command the `2>` redirection belongs to; wc
- why the location of `2>` matters. because it determines what it redirects error to


## Self-audit

- [x] I predicted before executing.
- [x] I recorded the exact pipeline and terminal evidence.
- [x] I verified both output files rather than assuming their contents.
- [x] My conclusion agrees with the evidence I recorded.


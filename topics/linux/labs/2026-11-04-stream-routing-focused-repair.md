# Stream-routing focused repair — 2026-11-04

## What your first attempt established

Your routing diagram correctly predicted all three destinations:

- `cat` stdout enters the pipe;
- `cat` stderr remains on the terminal;
- `wc` stdout goes to `count.txt`, while `wc` stderr goes to `errors.txt`.

Your observed terminal diagnostic also matched your prediction. This repair is
about precise language and recorded proof, not repeating the entire lab.

## 1 — Repair three descriptions

Your original answers are preserved below. Rewrite only the corrected-answer
column. Name the **stream or data** being transported, not merely the command
that produced it.

| Question                          | Your original answer                       | Corrected answer               |      |
| --------------------------------- | ------------------------------------------ | ------------------------------ | ---- |
| What information reaches `wc -l`? | `cat`                                      | alpha.txt 3 + beta.txt 2 lines |      |
| What is stored in `count.txt`?    | the contents of `alpha.txt` and `beta.txt` | 5                              |      |
| Which stream does `               | ` carry by default?                        | `stdout`                       | TODO |

Remember that `wc` may pad its displayed number with spaces. Distinguish the
numeric count from the exact display formatting.

## 2 — Preserve the honest execution record

This is the execution evidence you recorded in the first worksheet:

```text
raffi@Raffis-Mac linux % cat labs/stream-routing-retrieval/alpha.txt labs/stream-routing-retrieval/missing.txt labs/stream-routing-retrieval/beta.txt | wc -l > labs/stream-routing-retrieval/count.txt 2> labs/stream-routing-retrieval/errors.txt
cat: labs/stream-routing-retrieval/missing.txt: No such file or directory
```

The returned prompt was not recorded. Do not invent it afterward. Complete this
statement:

> Original returned-prompt evidence: recorded (`recorded` or `not recorded`)

Do **not** rerun the pipeline for this repair.

## 3 — Record the missing verification evidence

The first worksheet claimed that `count.txt` represented 5 and that
`errors.txt` had zero bytes, but it did not include the verification commands or
their output.

Now perform only these read-only checks:

1. Display `count.txt` with a suitable command.
2. Use a byte-counting command to determine the size of `errors.txt`.

Record the exact commands, complete output, and returned prompt:

```text
raffi@Raffis-Mac linux % cat labs/stream-routing-retrieval/count.txt
	5
raffi@Raffis-Mac linux % ls -l labs/stream-routing-retrieval/errors.txt
-rw-r--r--@ 1 raffi  staff  0  4 Nov 18:26 labs/stream-routing-retrieval/errors.txt
```

Then state only what this new evidence proves:

- Numeric line count represented in `count.txt`: 5
- Exact byte count of `errors.txt`: 0

## 4 — Rewrite the causal explanation

Your original explanation was:

> `|` carries `cat`; `2>` belongs to `wc`; its location determines what it
> redirects error to.

Rewrite it precisely in two or three sentences. Your explanation must state:

- that `|` carries stdout by default;
- that `2>` belongs to `wc` in this command;
- that the diagnostic was on `cat`'s stderr, which had no redirection.

> | carries stdout by default, 2> belongs to wc, the cat stdeer has no redirections, therefore the errors.txt is empty

## Self-audit

- [ ] I described transported data or streams rather than naming only a command.
- [ ] I did not reconstruct the missing historical prompt.
- [ ] My two result claims are supported by commands and actual output.
- [ ] My explanation accounts for why the diagnostic appeared on the terminal.


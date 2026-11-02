# Lab — Observe a live append with `tail -f`

Date: 2026-11-02

## What this experiment separates

```text
tail -f       observer: reads existing ending, then waits for appended data
helper script writer: appends one controlled line to the disposable log
Ctrl-C        stops the foreground observer and returns a shell prompt
```

The helper contains a `>>` append operation. Redirection syntax will be taught
in Phase 5; here the helper is supplied fixture machinery. Run it only once.

## 1 — Inspect and predict

Run:

```bash
nl -ba labs/tail-follow-practice/live.log
```

Record the command and complete output:

```text
raffi@Raffis-Mac linux % nl -ba labs/tail-follow-practice/live.log
     1	2026-11-02 INFO service started
     2	2026-11-02 INFO health check passed
     3	2026-11-02 WARN cache warming
```

Predict before starting follow mode:

| Question                                                          | Prediction                                                           |
| ----------------------------------------------------------------- | -------------------------------------------------------------------- |
| Which existing lines will `tail -n 2 -f` display first?           | 2026-11-02 INFO health check passed<br>2026-11-02 WARN cache warming |
| Will the shell prompt in that terminal return immediately?        | No                                                                   |
| After another process appends one line, what should `tail -f` do? | displays the new line                                                |
| Does `tail -f` itself modify the log?                             | No                                                                   |

## 2 — Start the observer in Terminal A

In the current terminal, run this one physical command:

```bash
tail -n 2 -f /Users/raffi/Learning/topics/linux/labs/tail-follow-practice/live.log
```

Leave it waiting. Do not press `Ctrl-C` yet.

## 3 — Append one controlled event from Terminal B

Open a second terminal tab or window. Run this one physical command exactly
once:

```bash
sh /Users/raffi/Learning/topics/linux/labs/tail-follow-practice/append-event.sh
```

The helper normally prints nothing. Return to Terminal A and wait briefly for
the appended event to appear. Then press `Ctrl-C` once to stop `tail`.

Record Terminal A's command, initial lines, newly observed line, `^C`, and
returned prompt:

```text
raffi@Raffis-Mac linux % tail -n 2 -f /Users/raffi/Learning/topics/linux/labs/tail-follow-practice/live.log
2026-11-02 INFO health check passed
2026-11-02 WARN cache warming
2026-11-02 INFO live update observed
```

Record the helper command submitted in Terminal B:

```text
raffi@Raffis-Mac ~ % sh /Users/raffi/Learning/topics/linux/labs/tail-follow-practice/append-event.sh
raffi@Raffis-Mac ~ %
```

## 4 — Verify the stored log

Back at a shell prompt in either terminal, run these separately:

```bash
tail -n 3 /Users/raffi/Learning/topics/linux/labs/tail-follow-practice/live.log
```

```bash
nl -ba /Users/raffi/Learning/topics/linux/labs/tail-follow-practice/live.log
```

Record both commands and complete output:

```text
raffi@Raffis-Mac linux % tail -n 3 /Users/raffi/Learning/topics/linux/labs/tail-follow-practice/live.log
2026-11-02 INFO health check passed
2026-11-02 WARN cache warming
2026-11-02 INFO live update observed
raffi@Raffis-Mac linux % nl -ba /Users/raffi/Learning/topics/linux/labs/tail-follow-practice/live.log
     1	2026-11-02 INFO service started
     2	2026-11-02 INFO health check passed
     3	2026-11-02 WARN cache warming
     4	2026-11-02 INFO live update observed
```

## 5 — Explain causality

Answer in your own words:

1. Which process modified the log?
2. Which process observed the new data?
3. What did `Ctrl-C` stop, and did it remove the appended line?
4. Did the actual result match all four predictions?

> 1. the sh thing
> 2. the tail with -f
> 3. No it didn't it simply stops the tail -f process
> 4. yes

Stop and tell the tutor when the worksheet is ready.

## Tutor checkpoint

All four predictions were correct. The helper appended the fourth line,
`tail -f` observed it, and stopping the observer left the stored line intact.
Evidence-quality note: the Terminal A transcript omitted the requested `^C`
and returned prompt, although the explanation and later shell verification show
that the observer was stopped.

# Lab — Safe `mv` Replacement Decisions

Date: 2026-10-28

## Purpose

Transfer the overwrite-safety model from `cp -i` to `mv -i`, while tracking
what happens to both the source and destination paths.

All changes remain inside the disposable `move-practice` tree.

## Local documentation evidence

The installed `mv` manual says that `-i` prompts before a move that would
overwrite an existing file. The move is attempted only when the response begins
with `y` or `Y`.

## Inspect before modifying

Start in the disposable tree:

```bash
cd /Users/raffi/Learning/topics/linux/labs/move-practice
```

Run these separately:

```bash
cat review/report.txt
```

```bash
cat archive/final.txt
```

Record the actual contents:

```text
TODO
```

## Attempt 1 — decline the replacement

You identified `-i` as the flag that requests confirmation. Predict the state
after answering `n` to this command:

```bash
mv -i review/report.txt archive/final.txt
```

| Question | Prediction |
| --- | --- |
| Exact destination path | TODO |
| Content at `review/report.txt` after declining | TODO |
| Content at `archive/final.txt` after declining | TODO |
| Will both paths still exist? | TODO |
| Will the working directory change? | TODO |

Run the command, type `n` at the prompt, and press Enter. Then inspect both
files and the working directory:

```bash
cat review/report.txt
```

```bash
cat archive/final.txt
```

```bash
pwd
```

Record the prompt, your response, and the complete verification output:

```text
TODO
```

Did the observed state match every prediction? Explain any difference.

TODO

## Attempt 2 — accept the replacement

Before repeating the command, predict the state after answering `y`:

| Question | Prediction |
| --- | --- |
| Content at `archive/final.txt` after accepting | TODO |
| Will `review/report.txt` still exist? | TODO |
| Why? | TODO |

Run the same command again:

```bash
mv -i review/report.txt archive/final.txt
```

This time type `y` and press Enter. Verify the destination, the old source path,
and the working directory:

```bash
cat archive/final.txt
```

```bash
cat review/report.txt
```

```bash
pwd
```

Record the prompt, response, and complete output, including any error:

```text
TODO
```

## Explain the safety model

1. Why did answering `n` preserve both files?

   TODO

2. Why did answering `y` leave the destination but remove the old source path?

   TODO

3. After an accepted interactive operation, what differs between `cp -i` and
   `mv -i`?

   TODO

Stop here and tell the tutor when the worksheet is ready.

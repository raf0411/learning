# Lab — Safe `cp` Overwrite Decisions

Date: 2026-10-28

## Purpose

Learn what risk appears when a destination file already exists and how `cp -i`
lets you make the replacement decision interactively.

The tutor prepared two disposable fixtures with different contents:

```text
source/documents/replacement.txt    NEW source content
destination/report.txt              OLD destination content
```

All modifications remain inside `copy-practice`.

## Local documentation evidence

The installed `cp` manual says that an existing destination's contents are
overwritten when permissions allow. With `-i`, `cp` prompts before it performs
an overwrite and proceeds only when the reply begins with `y` or `Y`.

## Inspect before modifying

Start in the disposable tree:

```bash
cd /Users/raffi/Learning/topics/linux/labs/copy-practice
```

`cat` prints the contents of these short text files. Run:

```bash
cat source/documents/replacement.txt
```

```bash
cat destination/report.txt
```

Record the actual output:

```text
raffi@Raffis-Mac copy-practice % cat source/documents/replacement.txt
NEW source content
raffi@Raffis-Mac copy-practice % cat destination/report.txt
OLD destination content
raffi@Raffis-Mac copy-practice %
```

## Attempt 1 — decline the overwrite

Predict before running anything:

| Question                                                     | Prediction              |
| ------------------------------------------------------------ | ----------------------- |
| Exact target file path                                       | destination/report.txt  |
| Why should `cp -i` prompt this time?                         | TODO                    |
| If you answer `n`, what content should remain in the target? | OLD destination content |
| Should the source content change?                            | No                      |

Run this one command:

```bash
cp -i source/documents/replacement.txt destination/report.txt
```

When prompted, type `n` and press Enter. Then inspect the target:

```bash
cat destination/report.txt
```

Record the prompt, your answer, and the observed content:

```text
raffi@Raffis-Mac copy-practice % cp -i source/documents/replacement.txt destination/report.txt
overwrite destination/report.txt? (y/n [n]) n
not overwritten
raffi@Raffis-Mac copy-practice % cat destination/report.txt
OLD destination content
raffi@Raffis-Mac copy-practice %
```

Explain whether the prediction matched:

Yes

## Attempt 2 — accept the overwrite

Before running the same `cp -i` command again, predict the target's content
after answering `y`:

NEW source content

Run:

```bash
cp -i source/documents/replacement.txt destination/report.txt
```

This time, type `y` and press Enter. Verify both paths:

```bash
cat destination/report.txt
```

```bash
cat source/documents/replacement.txt
```

Record the prompt, answer, and both outputs:

```text
raffi@Raffis-Mac copy-practice % cat destination/report.txt
NEW source content
raffi@Raffis-Mac copy-practice % cat source/documents/replacement.txt
NEW source content
raffi@Raffis-Mac copy-practice %
```

## Explain the safety model

Complete these in your own words:

1. Plain `cp SOURCE TARGET` is risky when `TARGET` already exists because:

   it can overwrite the TARGET file without confirming

2. Adding `-i` changes the behavior by:

    it can asks to confirm the TARGET file if it want to be overwritten or not

3. Inspecting after the command is still necessary because:

   To confirm it manually i guess idk

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
raffi@Raffis-Mac move-practice % cat review/report.txt
Draft version 1
raffi@Raffis-Mac move-practice % cat archive/final.txt
Approved final content
raffi@Raffis-Mac move-practice %
```

## Attempt 1 — decline the replacement

You identified `-i` as the flag that requests confirmation. Predict the state
after answering `n` to this command:

```bash
mv -i review/report.txt archive/final.txt
```

| Question                                       | Prediction             |
| ---------------------------------------------- | ---------------------- |
| Exact destination path                         | archive/final.txt      |
| Content at `review/report.txt` after declining | Draft version 1        |
| Content at `archive/final.txt` after declining | Approved final content |
| Will both paths still exist?                   | because we decline it  |
| Will the working directory change?             | no                     |

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
raffi@Raffis-Mac move-practice %
raffi@Raffis-Mac move-practice % mv -i review/report.txt archive/final.txt
overwrite archive/final.txt? (y/n [n]) n
not overwritten
raffi@Raffis-Mac move-practice % cat review/report.txt
Draft version 1
raffi@Raffis-Mac move-practice % cat archive/final.txt
Approved final content
raffi@Raffis-Mac move-practice % pwd
/Users/raffi/Learning/topics/linux/labs/move-practice
raffi@Raffis-Mac move-practice %
```

Did the observed state match every prediction? Explain any difference.

it matched

## Attempt 2 — accept the replacement

Before repeating the command, predict the state after answering `y`:

| Question                                       | Prediction                                                                           |
| ---------------------------------------------- | ------------------------------------------------------------------------------------ |
| Content at `archive/final.txt` after accepting | Draft version 1                                                                      |
| Will `review/report.txt` still exist?          | No                                                                                   |
| Why?                                           | Because it's being moved and renamed to final.txt, and because we accept the changes |

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
raffi@Raffis-Mac move-practice % mv -i review/report.txt archive/final.txt
overwrite archive/final.txt? (y/n [n]) y
raffi@Raffis-Mac move-practice % cat review/report.txt
cat: review/report.txt: No such file or directory
raffi@Raffis-Mac move-practice % cat archive/final.txt
Draft version 1
raffi@Raffis-Mac move-practice % pwd
/Users/raffi/Learning/topics/linux/labs/move-practice
raffi@Raffis-Mac move-practice %
```

## Explain the safety model

1. Why did answering `n` preserve both files?

   because it means declining it

2. Why did answering `y` leave the destination but remove the old source path?

	because it means accepting the changes and moving the file into another path and removing the old one

3. After an accepted interactive operation, what differs between `cp -i` and
   `mv -i`?

   cp preserve the old source path while mv removes the old source path

Stop here and tell the tutor when the worksheet is ready.

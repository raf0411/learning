# Lab — Identify data with `file`

Date: 2026-11-02

## Why this tool exists

A suffix such as `.txt`, `.bz2`, or `.data` is a naming convention. It is a
useful clue, but renaming a path does not transform the stored bytes.

`file PATH` classifies the filesystem object or its data using actual evidence
such as object metadata and recognizable byte patterns. It prints a result and
returns to the shell; it does not edit the inspected path.

This lab uses the valid bzip2 archive from the previous checkpoint. It does not
repeat archive creation or extraction.

## 1 — Predict and retrieve

Answer before running `file` or copying anything.

| Question                                                                                           | Prediction                                                      |
| -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| What content format does the suffix `.tar.bz2` suggest?                                            | it suggests that it compresses a directory using the bz2 method |
| Which case-sensitive `tar` option selects bzip2?                                                   | -j                                                              |
| Which case-sensitive `tar` option selects xz?                                                      | -J                                                              |
| If a bzip2 archive is copied to a pathname ending in `.txt`, do its stored bytes become text? Why? | i don't know                                                    |

## 2 — Classify three different objects

From the project root, run these three commands separately:

```bash
file sessions/2026-10-31.md
```

```bash
file labs/file-practice/mystery.data
```

```bash
file labs/archive-checkpoint/field-kit
```

Record each command and its complete output:

```text
raffi@Raffis-Mac linux % file sessions/2026-10-31.md
sessions/2026-10-31.md: Unicode text, UTF-8 text
raffi@Raffis-Mac linux % file labs/file-practice/mystery.data
labs/file-practice/mystery.data: ASCII text
raffi@Raffis-Mac linux % file labs/archive-checkpoint/field-kit
labs/archive-checkpoint/field-kit: directory
```

Complete the interpretation table using the observed output, not merely the
pathnames:

| Path                                | What `file` identified                       |
| ----------------------------------- | -------------------------------------------- |
| `sessions/2026-10-31.md`            | a Unicode text that uses UTF-8 text encoding |
| `labs/file-practice/mystery.data`   | a file containing ASCII text                 |
| `labs/archive-checkpoint/field-kit` | a directory                                  |

## 3 — Test a misleading suffix safely

First confirm that the destination does not already exist:

```bash
ls -l labs/file-practice/misleading.txt
```

Record the command and result. An expected “No such file” message proves only
that this proposed destination pathname is currently absent.

```text
ls: labs/file-practice/misleading.txt: No such file or directory
```

Now make a preserved copy with a misleading name:

```bash
cp -i labs/archive-checkpoint/field-kit-backup.tar.bz2 labs/file-practice/misleading.txt
```

Classify both the truthfully named source and the misleadingly named copy:

```bash
file labs/archive-checkpoint/field-kit-backup.tar.bz2
```

```bash
file labs/file-practice/misleading.txt
```

Record the commands and complete output:

```text
raffi@Raffis-Mac linux % cp -i labs/archive-checkpoint/field-kit-backup.tar.bz2 labs/file-practice/misleading.txt
raffi@Raffis-Mac linux % file labs/archive-checkpoint/field-kit-backup.tar.bz2
labs/archive-checkpoint/field-kit-backup.tar.bz2: bzip2 compressed data, block size = 900k
raffi@Raffis-Mac linux % file labs/file-practice/misleading.txt
labs/file-practice/misleading.txt: bzip2 compressed data, block size = 900k
```

## 4 — Explain the evidence

Answer in your own words.

1. Did the `.txt` suffix transform the copied data into text?
2. What evidence supports your answer?
3. Why was `file` more trustworthy than the suffix during the earlier
   mislabeled-archive diagnosis?

> 1. no, it still a bzip2
> 2. raffi@Raffis-Mac linux % file labs/file-practice/misleading.txt
labs/file-practice/misleading.txt: bzip2 compressed data, block size = 900k
3. because it actually tell u what the file is instead of looking at the file name

## 5 — Choose an inspection tool

Choose the most appropriate first tool from `file`, `cat`, `less`, `head`, and
`tail`.

| Goal                                                                           | First tool | Why                                                                             |
| ------------------------------------------------------------------------------ | ---------- | ------------------------------------------------------------------------------- |
| Determine whether an unfamiliar download is text, an image, or compressed data | file       | because using file is more trustworthy and actually display the file type       |
| Read an entire six-line text note                                              | cat        | because cat can be use for viewing short content file like a six-line text note |
| Search interactively inside a very long text log                               | less       | because less can be use to search interactively a very long text file           |
| Print only the last 30 lines of that log                                       | tail       | because we want to print only the last 30 lines, tail is perfect for that       |

Stop and tell the tutor when the worksheet is ready.

## Tutor checkpoint

- Correctly retrieved `-j` for bzip2 and `-J` for xz without a hint.
- Correctly used actual `file` output to identify text, a directory, and bzip2
  data despite a misleading `.txt` suffix.
- Refinement: `.tar.bz2` conventionally means a tar archive whose tar byte
  stream is compressed with bzip2; bzip2 does not itself package a directory.

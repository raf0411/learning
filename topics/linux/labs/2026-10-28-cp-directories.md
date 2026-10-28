# Lab — Copying Directories with `cp -R`

Date: 2026-10-28

## Purpose

Discover why copying a directory differs from copying one regular file, then
verify the exact paths created by recursive copying.

All changes stay inside the disposable `copy-practice` tree.

## Starting evidence

The source directory already contains two files:

```text
source/documents/
├── notes.txt
└── replacement.txt
```

The installed `cp` manual describes `-R` as copying a directory and the entire
subtree connected beneath it. We use uppercase `-R`; the local manual warns
that lowercase `-r` has implementation-dependent historical behavior.

Start here:

```bash
cd /Users/raffi/Learning/topics/linux/labs/copy-practice
```

Inspect the starting state:

```bash
pwd
```

```bash
ls source/documents
```

```bash
ls backups
```

Record the output:

```text
raffi@Raffis-Mac copy-practice % ls source/documents
notes.txt	replacement.txt
raffi@Raffis-Mac copy-practice % ls backups
daily
raffi@Raffis-Mac copy-practice %
```

## Attempt 1 — omit recursive copying

Predict before running the command:

| Question                                         | Prediction                                                                         |
| ------------------------------------------------ | ---------------------------------------------------------------------------------- |
| Will this copy succeed?                          | Yes                                                                                |
| Why or why not?                                  | Because we are not using -i therefore it will not confirm it and will overwrite it |
| Should `backups/documents-copy` exist afterward? | TODO                                                                               |

Run this one command:

```bash
cp source/documents backups/documents-copy
```

Record the exact output:

```text
raffi@Raffis-Mac copy-practice % cp source/documents backups/documents-copy
cp: source/documents is a directory (not copied).
```

Check whether the proposed target now exists:

```bash
ls backups/documents-copy
```

Record the output and compare it with your prediction:

```text
raffi@Raffis-Mac copy-practice % ls backups/documents-copy
ls: backups/documents-copy: No such file or directory
raffi@Raffis-Mac copy-practice %
```

Explanation in your own words:

> it doesnt work because i guess we need a specific command if we want to copy a directory, and ls didnt exists because the copying didnt work

## Attempt 2 — copy the directory recursively

Now predict the result of:

```bash
cp -R source/documents backups/documents-copy
```

| Question                                        | Prediction                             |
| ----------------------------------------------- | -------------------------------------- |
| Exact path of the new copied directory          | backups/documents-copy                 |
| Exact path of the copied `replacement.txt`      | backups/documents-copy/replacement.txt |
| Expected content of that copied file            | still the same as before               |
| Will the original source directory remain?      | yes                                    |
| Will `cp` change the shell's working directory? | no                                     |

Run the command:

```bash
cp -R source/documents backups/documents-copy
```

Verify the copied directory and one copied file:

```bash
ls backups/documents-copy
```

```bash
cat backups/documents-copy/replacement.txt
```

Verify that the source still exists and that you did not move:

```bash
ls source/documents
```

```bash
pwd
```

Record the output:

```text
raffi@Raffis-Mac copy-practice % cp -R source/documents backups/documents-copy
raffi@Raffis-Mac copy-practice % ls backups/documents-copy
notes.txt	replacement.txt
raffi@Raffis-Mac copy-practice % cat backups/documents-copy/replacement.txt
NEW source content
raffi@Raffis-Mac copy-practice % ls source/documents
notes.txt	replacement.txt
raffi@Raffis-Mac copy-practice % pwd
/Users/raffi/Learning/topics/linux/labs/copy-practice
raffi@Raffis-Mac copy-practice %
```

Did every prediction match? Explain any difference:

> i think so

## Transfer prediction — existing destination directory

Do not run this final command yet:

```bash
cp -R source/images backups/daily
```

`source/images` is a directory, and `backups/daily` already exists. Predict the
exact path of the copied directory that the command would create:

> backups/daily

Explain how you derived that path:

> because we are copying source/images to backups/daily
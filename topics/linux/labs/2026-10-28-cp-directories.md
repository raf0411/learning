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
TODO
```

## Attempt 1 — omit recursive copying

Predict before running the command:

| Question | Prediction |
| --- | --- |
| Will this copy succeed? | TODO |
| Why or why not? | TODO |
| Should `backups/documents-copy` exist afterward? | TODO |

Run this one command:

```bash
cp source/documents backups/documents-copy
```

Record the exact output:

```text
TODO
```

Check whether the proposed target now exists:

```bash
ls backups/documents-copy
```

Record the output and compare it with your prediction:

```text
TODO
```

Explanation in your own words:

> TODO

## Attempt 2 — copy the directory recursively

Now predict the result of:

```bash
cp -R source/documents backups/documents-copy
```

| Question | Prediction |
| --- | --- |
| Exact path of the new copied directory | TODO |
| Exact path of the copied `replacement.txt` | TODO |
| Expected content of that copied file | TODO |
| Will the original source directory remain? | TODO |
| Will `cp` change the shell's working directory? | TODO |

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
TODO
```

Did every prediction match? Explain any difference:

> TODO

## Transfer prediction — existing destination directory

Do not run this final command yet:

```bash
cp -R source/images backups/daily
```

`source/images` is a directory, and `backups/daily` already exists. Predict the
exact path of the copied directory that the command would create:

> TODO

Explain how you derived that path:

> TODO

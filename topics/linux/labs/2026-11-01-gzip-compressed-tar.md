# Lab — Add gzip compression to a tar archive

Date: 2026-11-01

## Starting idea

The previous lab created a plain tar archive:

```text
project/ --archive--> project.tar
```

This lab creates a second archive containing the same stored paths while gzip
compresses the archive representation:

```text
project/ --archive + gzip--> project.tar.gz
```

The `.tar.gz` suffix is a naming convention: `tar` describes the archive and
`gz` describes gzip compression. The suffix does not perform either operation;
the command options do.

The installed `bsdtar` documents `-z` as gzip compression. We will keep the
plain archive and its restored copy unchanged for comparison.

## Boundaries

Work only inside:

```text
/Users/raffi/Learning/topics/linux/labs/archive-practice
```

Do not delete or replace `project/`, `project.tar`, or `restored/`. Create:

```text
project.tar.gz
restored-gzip/
```

If either new name already exists during the initial inspection, stop and show
the tutor. Run commands separately and record the command lines even when a
successful command produces no output.

## 1 — Inspect and prepare

Run:

```bash
cd /Users/raffi/Learning/topics/linux/labs/archive-practice
```

```bash
pwd
```

```bash
ls -la
```

Confirm from the output that `project.tar.gz` and `restored-gzip/` do not
already exist. Then create and inspect the fresh extraction destination:

```bash
mkdir restored-gzip
```

```bash
ls -la restored-gzip
```

Record commands and output:

```text
raffi@Raffis-Mac archive-practice % pwd
/Users/raffi/Learning/topics/linux/labs/archive-practice
raffi@Raffis-Mac archive-practice % ls -la
total 24
drwxr-xr-x@  5 raffi  staff    160  1 Nov 18:57 .
drwxr-xr-x@ 36 raffi  staff   1152  1 Nov 19:17 ..
drwxr-xr-x@  4 raffi  staff    128 31 Oct 21:04 project
-rw-r--r--@  1 raffi  staff  12288  1 Nov 18:57 project.tar
drwxr-xr-x@  3 raffi  staff     96  1 Nov 19:01 restored
raffi@Raffis-Mac archive-practice % mkdir restored-gzip
raffi@Raffis-Mac archive-practice % ls -la restored-gzip
total 0
drwxr-xr-x@ 2 raffi  staff   64  1 Nov 19:19 .
drwxr-xr-x@ 6 raffi  staff  192  1 Nov 19:19 ..
raffi@Raffis-Mac archive-practice %
```

## 2 — Predict, create, and inspect

The creation command will be:

```bash
tar -czf project.tar.gz project
```

| Part | Meaning |
| --- | --- |
| `-c` | Create an archive |
| `-z` | Compress it with gzip |
| `-f project.tar.gz` | Write to this archive filename |
| `project` | Store this directory and its descendants |

Before running it, predict:

| Question                                                                   | Prediction                                                    |
| -------------------------------------------------------------------------- | ------------------------------------------------------------- |
| Will `project/` remain after creation?                                     | yes                                                           |
| Will `restored-gzip/` still be empty immediately after creation?           | yes                                                           |
| Should `project.tar` and `project.tar.gz` contain the same pathnames? Why? | idk actually, my guess is no because the gz one is compressed |

Now run the creation command once. Record its command line even if it prints
nothing. Compare the two archive files, then list the compressed archive:

```bash
ls -l project.tar project.tar.gz
```

```bash
tar -tzf project.tar.gz
```

```bash
ls -la restored-gzip
```

Record commands and output:

```text
raffi@Raffis-Mac archive-practice % tar -czf project.tar.gz project
raffi@Raffis-Mac archive-practice % ls -l project.tar project.tar.gz
-rw-r--r--@ 1 raffi  staff  12288  1 Nov 18:57 project.tar
-rw-r--r--@ 1 raffi  staff    625  1 Nov 19:20 project.tar.gz
raffi@Raffis-Mac archive-practice % tar -tzf project.tar.gz
project/
project/notes.txt
project/data/
project/data/items.txt
raffi@Raffis-Mac archive-practice % ls -la restored-gzip
total 0
drwxr-xr-x@ 2 raffi  staff   64  1 Nov 19:19 .
drwxr-xr-x@ 7 raffi  staff  224  1 Nov 19:20 ..
```

Based on the recorded byte sizes, which archive is smaller in this experiment?

> project.tar.gz

Compression often reduces size, especially for repetitive data, but it is not
a guarantee for every possible input because compression metadata has overhead
and some data is already difficult to compress.

## 3 — Predict and extract safely

Use the archive listing above to predict the resulting paths:

| Item                  | Predicted path relative to the lab root |
| --------------------- | --------------------------------------- |
| Extracted `notes.txt` | restored-gzip/project/notes.txt         |
| Extracted `items.txt` | restored-gzip/project/data/items.txt    |

Before extracting, recheck both the shell location and destination:

```bash
pwd
```

```bash
ls -la restored-gzip
```

Only while `restored-gzip/` is empty, run:

```bash
tar -xzf project.tar.gz -C restored-gzip
```

Record the command line even if it prints nothing. Then verify paths and
contents:

```bash
ls -la restored-gzip restored-gzip/project restored-gzip/project/data
```

```bash
cat restored-gzip/project/notes.txt
```

```bash
cat restored-gzip/project/data/items.txt
```

Confirm the source, plain archive, and compressed archive still exist:

```bash
ls -ld project project.tar project.tar.gz
```

```bash
pwd
```

Record commands and output:

```text
raffi@Raffis-Mac archive-practice % tar -xzf project.tar.gz -C restored-gzip
raffi@Raffis-Mac archive-practice % ls -la restored-gzip restored-gzip/project restored-gzip/project/data
restored-gzip:
total 0
drwxr-xr-x@ 3 raffi  staff   96  1 Nov 19:23 .
drwxr-xr-x@ 7 raffi  staff  224  1 Nov 19:20 ..
drwxr-xr-x@ 4 raffi  staff  128 31 Oct 21:04 project

restored-gzip/project:
total 8
drwxr-xr-x@ 4 raffi  staff  128 31 Oct 21:04 .
drwxr-xr-x@ 3 raffi  staff   96  1 Nov 19:23 ..
drwxr-xr-x@ 3 raffi  staff   96 31 Oct 21:04 data
-rw-r--r--@ 1 raffi  staff   52 31 Oct 21:04 notes.txt

restored-gzip/project/data:
total 8
drwxr-xr-x@ 3 raffi  staff   96 31 Oct 21:04 .
drwxr-xr-x@ 4 raffi  staff  128 31 Oct 21:04 ..
-rw-r--r--@ 1 raffi  staff   13 31 Oct 21:04 items.txt
raffi@Raffis-Mac archive-practice % cat restored-gzip/project/notes.txt
PROJECT NOTES
Practice packing and restoring files.
raffi@Raffis-Mac archive-practice % cat restored-gzip/project/data/items.txt
apple
banana
raffi@Raffis-Mac archive-practice % ls -ld project project.tar project.tar.gz
drwxr-xr-x@ 4 raffi  staff    128 31 Oct 21:04 project
-rw-r--r--@ 1 raffi  staff  12288  1 Nov 18:57 project.tar
-rw-r--r--@ 1 raffi  staff    625  1 Nov 19:20 project.tar.gz
raffi@Raffis-Mac archive-practice % pwd
/Users/raffi/Learning/topics/linux/labs/archive-practice
```

## Explain the result

In two or three sentences:

1. explain what `-z` added to the operations you already knew;
2. explain why `tar -tzf` did not create files in `restored-gzip/`, while
   `tar -xzf ... -C restored-gzip` did;
3. cite at least one observation from your recorded output.

> 1. it adds compression to the directory that we want to archive
> 2. because -t is only for listing what the archive has, while -x is to extract the archive and specify it to store in restored-gzip using -C
> 3. after we extract it, the restored-gzip folder contains project:
>    total 0
	drwxr-xr-x@ 3 raffi  staff   96  1 Nov 19:23 .
	drwxr-xr-x@ 7 raffi  staff  224  1 Nov 19:20 ..
	drwxr-xr-x@ 4 raffi  staff  128 31 Oct 21:04 project

Stop here and tell the tutor when the worksheet is ready. Preserve both
archives and both restored trees for comparison.

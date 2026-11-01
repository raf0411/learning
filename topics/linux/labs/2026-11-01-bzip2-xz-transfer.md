# Lab — Discover bzip2 and xz tar options

Date: 2026-11-01

## Purpose

Transfer the tar workflow to two other compression algorithms. Use installed
documentation to discover the options instead of receiving complete commands.

Existing artifacts must remain unchanged:

```text
project/
project.tar
project.tar.gz
restored/
restored-gzip/
```

Create only these new artifacts:

```text
project.tar.bz2
project.tar.xz
restored-xz/
```

Work only inside:

```text
/Users/raffi/Learning/topics/linux/labs/archive-practice
```

If a proposed new name already exists during initial inspection, stop and tell
the tutor. If a command produces an unexpected error, stop rather than trying
several variations. Record every command line, including successful commands
that print no output.

## 1 — Inspect the boundary

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

Confirm that the three proposed new names are absent. Record commands and
output:

```text
raffi@Raffis-Mac archive-practice % cd /Users/raffi/Learning/topics/linux/labs/archive-practice
raffi@Raffis-Mac archive-practice % pwd
/Users/raffi/Learning/topics/linux/labs/archive-practice
raffi@Raffis-Mac archive-practice % ls -la
total 32
drwxr-xr-x@  7 raffi  staff    224  1 Nov 19:20 .
drwxr-xr-x@ 37 raffi  staff   1184  1 Nov 19:37 ..
drwxr-xr-x@  4 raffi  staff    128 31 Oct 21:04 project
-rw-r--r--@  1 raffi  staff  12288  1 Nov 18:57 project.tar
-rw-r--r--@  1 raffi  staff    625  1 Nov 19:20 project.tar.gz
drwxr-xr-x@  3 raffi  staff     96  1 Nov 19:01 restored
drwxr-xr-x@  3 raffi  staff     96  1 Nov 19:23 restored-gzip
raffi@Raffis-Mac archive-practice % pwd
/Users/raffi/Learning/topics/linux/labs/archive-practice
```

## 2 — Discover the compression options

Run the installed help command:

```bash
tar --help
```

Find the line that maps compression algorithms to options. Record that line,
then complete the table:

```text
-z, -j, -J, --lzma  Compress archive with gzip/bzip2/xz/lzma
```

| Compression algorithm | tar option |
| --------------------- | ---------- |
| gzip                  | -z         |
| bzip2                 | -j         |
| xz                    | -J         |

Pay attention to letter case: lowercase and uppercase options are different.

## 3 — Plan before creating

Using the gzip command structure you already used, write one complete physical
command line for each task. Do not run either command until both are written.

| Task                                                 | Planned command                  |
| ---------------------------------------------------- | -------------------------------- |
| Create `project.tar.bz2` from `project/` using bzip2 | tar -cjf project.tar.bz2 project |
| Create `project.tar.xz` from `project/` using xz     | tar -cJf project.tar.xz project  |

Check each plan:

- create mode is present;
- the documented compression option matches the filename convention;
- `-f` is followed by the intended new archive filename;
- the source operand is exactly `project`.

Now run each planned command once. If both succeed, inspect all archive sizes:

```bash
ls -l project.tar project.tar.gz project.tar.bz2 project.tar.xz
```

Record the commands and output:

```text
raffi@Raffis-Mac archive-practice % tar -cjf project.tar.bz2 project
raffi@Raffis-Mac archive-practice % tar -cJf project.tar.xz project
raffi@Raffis-Mac archive-practice % ls -l project.tar project.tar.gz project.tar.bz2 project.tar.xz
-rw-r--r--@ 1 raffi  staff  12288  1 Nov 18:57 project.tar
-rw-r--r--@ 1 raffi  staff    725  1 Nov 19:42 project.tar.bz2
-rw-r--r--@ 1 raffi  staff    625  1 Nov 19:20 project.tar.gz
-rw-r--r--@ 1 raffi  staff    596  1 Nov 19:42 project.tar.xz
```

List the stored pathnames in each new archive. Derive and record both complete
commands before running them:

| Task                                                          | Planned command          |
| ------------------------------------------------------------- | ------------------------ |
| List `project.tar.bz2` with its documented compression option | tar -tjf project.tar.bz2 |
| List `project.tar.xz` with its documented compression option  | tar -tJf project.tar.xz  |

Run the commands and record their output:

```text
raffi@Raffis-Mac archive-practice % tar -tjf project.tar.bz2
project/
project/notes.txt
project/data/
project/data/items.txt
raffi@Raffis-Mac archive-practice % tar -tJf project.tar.xz
project/
project/notes.txt
project/data/
project/data/items.txt
```

Did the two new archives list the same pathnames as `project.tar.gz`? Cite the
recorded member lists, not the archive byte sizes.

> bz2:
project/
project/notes.txt
project/data/
project/data/items.txt
	xz:
	project/
	project/notes.txt
	project/data/
	project/data/items.txt


Order the four archive files from smallest to largest based only on the measured
sizes in this experiment. Do not generalize this order into a universal ranking
of compression algorithms.

> project.tar.xz, project.tar.gz, project.tar.bz2, project.tar.

## 4 — Independently restore the xz archive

Write a safe command sequence that:

1. verifies the current directory;
2. creates `restored-xz/`;
3. proves the new directory is empty;
4. extracts `project.tar.xz` into it using the documented xz option;
5. lists the full restored structure;
6. reads both restored files;
7. proves the shell's working directory did not change.

Use the same safety pattern as the earlier extraction, but write the exact
commands yourself. Put one command on each row in execution order:

| Step              | Planned command                                                             |
| ----------------- | --------------------------------------------------------------------------- |
| 1                 | pwd                                                                         |
| 2                 | mkdir restored-xz                                                           |
| 3                 | ls -la restored-xz                                                          |
| 4                 | tar -xJf project.tar.xz -C restored-xz                                      |
| 5                 | ls -la restored-xz                                                          |
| 6                 | cat restored-xz/project/notes.txt<br>cat restored-xz/project/data/items.txt |
| 7                 | pwd                                                                         |
| 8, only if needed | `not needed`                                                                |

Inspect the entire plan before running it. Then execute one command at a time
and record every command and its output:

```text
raffi@Raffis-Mac archive-practice % pwd
/Users/raffi/Learning/topics/linux/labs/archive-practice
raffi@Raffis-Mac archive-practice % mkdir restored-xz
raffi@Raffis-Mac archive-practice % ls -la restored-xz
total 0
drwxr-xr-x@  2 raffi  staff   64  1 Nov 19:54 .
drwxr-xr-x@ 10 raffi  staff  320  1 Nov 19:54 ..
raffi@Raffis-Mac archive-practice % tar -xJf project.tar.xz -C restored-xz
raffi@Raffis-Mac archive-practice % ls -la restored-xz
total 0
drwxr-xr-x@  3 raffi  staff   96  1 Nov 19:54 .
drwxr-xr-x@ 10 raffi  staff  320  1 Nov 19:54 ..
drwxr-xr-x@  4 raffi  staff  128 31 Oct 21:04 project
raffi@Raffis-Mac archive-practice % cat restored-xz/project/notes.txt
PROJECT NOTES
Practice packing and restoring files.
raffi@Raffis-Mac archive-practice % cat restored-xz/project/data/items.txt
apple
banana
raffi@Raffis-Mac archive-practice % pwd
/Users/raffi/Learning/topics/linux/labs/archive-practice
```

## Explain the transfer

In two or three sentences, explain:

- why gzip, bzip2, and xz archives can store the same pathnames;
- what changes when you choose a different compression option;
- which recorded evidence proves the xz archive restored successfully.

> - beause it all refers to the original pathnames which is project/
> - it changes the archive encoding or byte sizes
>  - evidence:
> raffi@Raffis-Mac archive-practice % tar -xJf project.tar.xz -C restored-xz
	raffi@Raffis-Mac archive-practice % ls -la restored-xz
	total 0
	drwxr-xr-x@  3 raffi  staff   96  1 Nov 19:54 .
	drwxr-xr-x@ 10 raffi  staff  320  1 Nov 19:54 ..
	drwxr-xr-x@  4 raffi  staff  128 31 Oct 21:04 project

Stop and tell the tutor when the worksheet is ready. Preserve all artifacts for
review.

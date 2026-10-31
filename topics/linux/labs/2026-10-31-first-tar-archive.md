# Lab — Package, inspect, and extract a project

Date: 2026-10-31

## Starting idea

You have used downloaded ZIP files by extracting them. Here you will create
your own archive before extracting it elsewhere.

An archive stores files and their paths together in one file. Compression is
a separate operation for reducing storage size. This lab creates a plain,
uncompressed tar archive.

## Prepared directory and boundaries

Work only inside:

```text
/Users/raffi/Learning/topics/linux/labs/archive-practice
```

Prepared structure:

```text
archive-practice/
├── project/
│   ├── notes.txt
│   └── data/
│       └── items.txt
└── restored/                 initially empty
```

Keep the source project unchanged. Create `project.tar` beside `project/`,
then extract only into the empty `restored/` directory. No deletion is needed.
Creating an archive can overwrite an existing archive with the same name;
extraction can overwrite existing destination files. Inspect before each.
If the setup differs or an unexpected error occurs, stop and show the tutor.

Run commands separately. Write predictions before the relevant command.

## 1 — Inspect the source and destination

```bash
cd /Users/raffi/Learning/topics/linux/labs/archive-practice
```

```bash
pwd
```

```bash
ls -la
```

```bash
ls -la project project/data restored
```

```bash
cat project/notes.txt
```

```bash
cat project/data/items.txt
```

Record commands and output. Confirm from the output that `project.tar` does
not already exist and `restored/` contains no entries except `.` and `..`.

```text
TODO
```

## 2 — Create and list an archive

The first command is:

```bash
tar -cf project.tar project
```

Read its parts:

| Part | Meaning |
| --- | --- |
| `-c` | Create an archive |
| `-f project.tar` | Use `project.tar` as the archive file |
| `project` | Include this directory and its contents |

`-cf` combines `-c` and `-f`; the next word is the filename belonging to `-f`.
This command does not request compression. Success may produce no output.

Before running it, predict:

| Question | Prediction |
| --- | --- |
| Will the source `project/` and its files remain after archive creation? | TODO |
| Will creating `project.tar` put files into `restored/`? | TODO |

Run the creation command above once, then inspect:

```bash
ls -l project.tar project project/data
```

List the paths stored inside the archive. `-t` lists entries; it does not
extract them. `-f` still identifies the archive file, now used as input.

```bash
tar -tf project.tar
```

```bash
ls -la restored
```

Record commands and actual output:

```text
TODO
```

## 3 — Extract into the empty destination

Use the archive listing to check what will be written. The project entries
should be under `project/`. If you see unexpected paths, stop for review.

Our extraction command will be:

```bash
tar -xf project.tar -C restored
```

- `-x` means extract.
- `-f project.tar` selects the archive to read.
- `-C restored` tells tar to extract inside the existing `restored/` directory.
  It changes where tar works; it does not change your shell's current directory.
- The stored paths are recreated beneath that destination.

Before running it, use your archive listing to predict:

| Item | Predicted path relative to the lab root after extraction |
| --- | --- |
| Extracted `notes.txt` | TODO |
| Extracted `items.txt` | TODO |

Recheck the working directory and the empty extraction destination:

```bash
pwd
```

```bash
ls -la restored
```

Run the extraction command above only while `restored/` is still empty.
Then verify the full directory structure and the contents:

```bash
ls -la restored restored/project restored/project/data
```

```bash
cat restored/project/notes.txt
```

```bash
cat restored/project/data/items.txt
```

Confirm the source files remain readable and the archive still exists:

```bash
cat project/notes.txt
```

```bash
cat project/data/items.txt
```

```bash
ls -l project.tar
```

```bash
pwd
```

Record commands and actual output:

```text
TODO
```

## Explain the result

In one or two sentences, explain what `tar -tf project.tar` did differently
from `tar -xf project.tar -C restored`. Cite one observation from your output.

> TODO

Stop here and tell the tutor when the worksheet is ready. Keep the source,
archive, and extracted files for the next experiment.

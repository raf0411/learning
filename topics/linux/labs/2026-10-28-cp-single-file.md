# Lab — First Single-File Copies with `cp`

Date: 2026-10-28

## Purpose

Learn the basic model:

```text
cp SOURCE DESTINATION
```

For this lab, copying should leave the source in place and create another file
at the destination. Work only inside the disposable `copy-practice` tree.

## Safety boundary

The destination directories are currently empty. Do not substitute paths
outside `copy-practice`. Plain `cp` can replace an existing destination file;
we will study overwrite protection separately.

## Set up one disposable source file

Run these as separate commands:

```bash
cd /Users/raffi/Learning/topics/linux/labs/copy-practice
```

```bash
pwd
```

```bash
touch source/documents/notes.txt
```

```bash
ls source/documents
```

`touch` creates the empty file because it does not yet exist. Record the actual
outputs that establish your location and show the file:

```text
raffi@Raffis-Mac labs % cd /Users/raffi/Learning/topics/linux/labs/copy-practice
raffi@Raffis-Mac copy-practice % pwd
/Users/raffi/Learning/topics/linux/labs/copy-practice
raffi@Raffis-Mac copy-practice % touch source/documents/notes.txt
raffi@Raffis-Mac copy-practice % ls source/documents
notes.txt
```

## Copy 1 — preserve the filename

Predict the result before running the command:

```bash
cp source/documents/notes.txt destination
```

| Prediction                                              | Your answer                                                       |
| ------------------------------------------------------- | ----------------------------------------------------------------- |
| Full path where the copied file will appear             | /Users/raffi/Learning/topics/linux/labs/copy-practice/destination |
| Will the original `source/documents/notes.txt` remain?  | yes                                                               |
| Will this command change the shell's current directory? | no                                                                |

Now run the `cp` command, followed by these read-only checks:

```bash
ls source/documents
```

```bash
ls destination
```

Record the actual output:

```text
raffi@Raffis-Mac copy-practice % ls source/documents
notes.txt
raffi@Raffis-Mac copy-practice % ls destination
notes.txt
raffi@Raffis-Mac copy-practice %
```

Compare prediction with observation:

- What remained at the source?

  the notes.txt

- What appeared at the destination?

  the copied notes.txt

- Did the shell move to another directory? What command could verify this if
  needed?

  no, pwd

## Copy 2 — choose a new filename

Do not run this yet. First predict the two paths that will exist afterward:

```bash
cp source/documents/notes.txt backups/daily/notes-backup.txt
```

| Expected path     | Why you expect it |
| ----------------- | ----------------- |
| source/documents/ | Original source   |
| backups/daily/    | New copy          |

Then run the command and verify with:

```bash
ls source/documents
```

```bash
ls backups/daily
```

Record the output and explain how the destination operand controlled the copied
file's name:

```text
raffi@Raffis-Mac copy-practice % cp source/documents/notes.txt backups/daily/notes-backup.txt
raffi@Raffis-Mac copy-practice % ls source/documents
notes.txt
raffi@Raffis-Mac copy-practice % ls backups/daily
notes-backup.txt
raffi@Raffis-Mac copy-practice %
```

Explanation:
It controlled the copied because it can change the file name without changing the content of it, because its a copy of the source file

## Tutor review — file paths versus directory paths

The execution and observations are correct. The predictions identify the right
directories, but they stop before the filenames:

```text
destination                       directory path
destination/notes.txt             file path

backups/daily                     directory path
backups/daily/notes-backup.txt    file path
```

Therefore, after both copies, the three relative file paths are:

```text
source/documents/notes.txt
destination/notes.txt
backups/daily/notes-backup.txt
```

When the destination operand names an existing directory, `cp` places a copy
inside it using the source's filename. When the destination operand includes a
new filename, that exact name is used for the copy.

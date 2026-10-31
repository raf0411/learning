# Lab — Two names for one file

Date: 2026-10-31

## Purpose and boundary

Compare an ordinary copy with a hard link, then test your prediction about
removing one hard-linked name. Work only in the disposable directory below.
`keep.txt` is a protected neighbor: leave its name and contents unchanged.
Only `original.txt` will be removed. Leave the other files for inspection.

The tutor prepared `original.txt` containing `FIRST CONTENT` and `keep.txt`
containing `KEEP THIS FILE`. Record your own observations rather than treating
these setup descriptions as experimental output.

Run each command separately. Fill predictions before running the associated
experiment. If the actual setup differs or a creation command fails, stop and
show the tutor rather than overwriting existing entries.

## 1 — Create a copy and another name

```bash
cd /Users/raffi/Learning/topics/linux/labs/hard-link-practice
```

```bash
pwd
```

```bash
ls -la
```

```bash
cat original.txt keep.txt
```

Create a separate copy:

```bash
cp original.txt copy.txt
```

`ln` without `-s` creates a hard link: a new name for the same file.

```bash
ln original.txt second.txt
```

`ls -li` adds an inode number at the start of each long-listing row. Within
this filesystem, matching inode numbers identify the same underlying file.
The number after the permissions field is the hard-link count.
Hard links to regular files appear as regular files (`-`), not symbolic links
(`l`), and have no stored target arrow.

Before inspecting, predict:

| Question                                                | Prediction                |
| ------------------------------------------------------- | ------------------------- |
| Which two names should have the same inode number?      | original.txt & second.txt |
| Should `copy.txt` have that same inode number?          | no                        |
| How many hard-linked names should the shared file have? | 1                         |

```bash
ls -li original.txt second.txt copy.txt
```

Record commands and actual output from this section:

```text
raffi@Raffis-Mac hard-link-practice % ls -li original.txt second.txt copy.txt
48273437 -rw-r--r--@ 1 raffi  staff  14 31 Oct 19:55 copy.txt
48272923 -rw-r--r--@ 2 raffi  staff  14 31 Oct 19:54 original.txt
48272923 -rw-r--r--@ 2 raffi  staff  14 31 Oct 19:54 second.txt
raffi@Raffis-Mac hard-link-practice %
```

## 2 — Write through the second name

Predict first:

| File read after writing `CHANGED CONTENT` through `second.txt` | Predicted content |
| -------------------------------------------------------------- | ----------------- |
| `original.txt`                                                 | CHANGED CONTENT   |
| `second.txt`                                                   | CHANGED CONTENT   |
| `copy.txt`                                                     | FIRST CONTENT     |

Confirm the location and the three entries before modifying anything:

```bash
pwd
```

```bash
ls -li original.txt second.txt copy.txt
```

The following supplied command writes text into the existing file opened
through `second.txt`. `>` replaces that file's contents; `printf` supplies the
text and `\n` supplies a newline. We will study this shell syntax later.
It does not remove and recreate the directory entry. Run it only in this lab.

```bash
printf 'CHANGED CONTENT\n' > second.txt
```

```bash
cat original.txt
```

```bash
cat second.txt
```

```bash
cat copy.txt
```

```bash
ls -li original.txt second.txt copy.txt
```

Record commands and actual output:

```text
raffi@Raffis-Mac hard-link-practice % printf 'CHANGED CONTENT\n' > second.txt
raffi@Raffis-Mac hard-link-practice % cat original.txt
CHANGED CONTENT
raffi@Raffis-Mac hard-link-practice % cat second.txt
CHANGED CONTENT
raffi@Raffis-Mac hard-link-practice % cat copy.txt
FIRST CONTENT
raffi@Raffis-Mac hard-link-practice % ls -li original.txt second.txt copy.txt
48273437 -rw-r--r--@ 1 raffi  staff  14 31 Oct 19:55 copy.txt
48272923 -rw-r--r--@ 2 raffi  staff  16 31 Oct 20:06 original.txt
48272923 -rw-r--r--@ 2 raffi  staff  16 31 Oct 20:06 second.txt
```

Explain the difference between the copy's behavior and the hard-linked names'
behavior using your observed contents and inode numbers:

> copy creates an independent file that doesn't care if the original copied file changes its content, it will stay on its own, hard linked names depends on the original path, if the original changes, the other changes as well

## 3 — Remove one name

Your prediction already supplied in chat:

> it would display the content of that underlying file, removing original.txt does not affect that

You do not need to retype that answer. Add one prediction:

What hard-link count should `second.txt` show after `original.txt` is removed?

> 1

Inspect the current location and exact target before removal:

```bash
pwd
```

```bash
ls -li original.txt second.txt copy.txt keep.txt
```

Remove only the disposable `original.txt` entry. Check that the prompt names
`original.txt`, then answer `y`:

```bash
rm -i original.txt
```

```bash
ls -li
```

```bash
cat second.txt
```

```bash
cat copy.txt
```

```bash
cat keep.txt
```

```bash
ls -l original.txt
```

Record the prompt, your response, and all verification output:

```text
raffi@Raffis-Mac hard-link-practice % ls -li original.txt second.txt copy.txt keep.txt
48273437 -rw-r--r--@ 1 raffi  staff  14 31 Oct 19:55 copy.txt
48272924 -rw-r--r--@ 1 raffi  staff  15 31 Oct 19:54 keep.txt
48272923 -rw-r--r--@ 2 raffi  staff  16 31 Oct 20:06 original.txt
48272923 -rw-r--r--@ 2 raffi  staff  16 31 Oct 20:06 second.txt
raffi@Raffis-Mac hard-link-practice % rm -i original.txt
remove original.txt? y
raffi@Raffis-Mac hard-link-practice % ls -li
total 24
48273437 -rw-r--r--@ 1 raffi  staff  14 31 Oct 19:55 copy.txt
48272924 -rw-r--r--@ 1 raffi  staff  15 31 Oct 19:54 keep.txt
48272923 -rw-r--r--@ 1 raffi  staff  16 31 Oct 20:06 second.txt
raffi@Raffis-Mac hard-link-practice % cat second.txt
CHANGED CONTENT
raffi@Raffis-Mac hard-link-practice % cat copy.txt
FIRST CONTENT
raffi@Raffis-Mac hard-link-practice % cat keep.txt
KEEP THIS FILE
raffi@Raffis-Mac hard-link-practice % ls -l original.txt
ls: original.txt: No such file or directory
```

## 4 — Explain the observed difference

In the symbolic-link lab, removing `original.txt` left a link that could not
be read. Explain why `second.txt` behaves differently in this experiment.
Use evidence from the two labs.

> because its a hard link not a symbolic link

Stop here and tell the tutor when the worksheet is ready. Leave the remaining
files in place; no cleanup is needed.

## Review — Explain the shared file

The recorded results match your content predictions and your prediction of a
link count of 1 after removal. Two corrections:

- Before removal, both `original.txt` and `second.txt` counted as hard-linked
  names. The count was 2, not 1. The first name counts too.
- Hard-linked names do not depend on an original pathname. Both names refer
  to the same underlying file, identified here by inode 48272923. There is no
  privileged original name. Your own removal experiment demonstrates this.

The copy had a different inode, 48273437, and retained `FIRST CONTENT`.
The hard-linked file retained inode 48272923 when its content changed and
when one of its names was removed.

Your original answers above are preserved. No commands need to be repeated.
Write a corrected explanation in two or three sentences: use the inode and
content evidence to explain why writing through `second.txt` affected what
`original.txt` read, but removing `original.txt` left `second.txt` readable.

> because second.txt and original.txt is linked to the same underlying file or inode 48272923, basically what i understand if we change the either second.txt or original.txt we are changing that underlying file or inode too, thats why when we change second.txt original.txt also changes because it follows that underlying file, that also answers why removing original.txt left second.txt readable because second.txt refers to that underlying file or inode not the original.txt.

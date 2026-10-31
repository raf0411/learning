# Lab — First Symbolic-Link Model

Date: 2026-10-30

## Purpose

Distinguish a symbolic link from a copied file by observing what happens when
the target's content changes, the target pathname is removed, and the link
pathname is removed.

## Working model

A copy has its own file data. A symbolic link stores a target pathname:

```text
copy.txt       ---> separate file data

shortcut.txt  ---> stored pathname "original.txt"
                              |
                              v
                       original.txt ---> file data
```

The command form is:

```text
ln -s existing-target-path new-link-name
```

As with `cp`, the first path identifies what is referred to and the second path
is the new entry being created. The `-s` option requests a symbolic link.

## Safety boundary

Work only inside:

```text
/Users/raffi/Learning/topics/linux/labs/link-practice
```

Only `original.txt` and the new `shortcut.txt` will be removed during this
disposable experiment. `replacement.txt` must remain.

## Part 1 — Inspect the prepared target

Run these commands separately:

```bash
cd /Users/raffi/Learning/topics/linux/labs/link-practice
```

```bash
pwd
```

```bash
ls -l
```

```bash
cat original.txt
```

```bash
cat replacement.txt
```

Record all commands and complete output:

```text
raffi@Raffis-Mac link-practice % pwd
/Users/raffi/Learning/topics/linux/labs/link-practice
raffi@Raffis-Mac link-practice % ls -l
total 16
-rw-r--r--@ 1 raffi  staff  17 30 Oct 21:17 original.txt
-rw-r--r--@ 1 raffi  staff  20 30 Oct 21:17 replacement.txt
raffi@Raffis-Mac link-practice % cat original.txt
ORIGINAL CONTENT
raffi@Raffis-Mac link-practice % cat replacement.txt
REPLACEMENT CONTENT
raffi@Raffis-Mac link-practice %
```

## Part 2 — Predict and create the symbolic link

Before running the creation command, predict:

| Question                                                                      | Prediction       |
| ----------------------------------------------------------------------------- | ---------------- |
| Which new pathname will be created?                                           | shortcut.txt     |
| Will a second copy of `ORIGINAL CONTENT` be created as independent file data? | No               |
| What should `cat shortcut.txt` display?                                       | ORIGINAL CONTENT |
| Will `original.txt` still exist?                                              | Yes              |

Now run:

```bash
ln -s original.txt shortcut.txt
```

Inspect both the entry and the content reached through it:

```bash
ls -l
```

```bash
cat shortcut.txt
```

Record the complete output:

```text
raffi@Raffis-Mac link-practice % ln -s original.txt shortcut.txt
raffi@Raffis-Mac link-practice % ls -l
total 16
-rw-r--r--@ 1 raffi  staff  17 30 Oct 21:17 original.txt
-rw-r--r--@ 1 raffi  staff  20 30 Oct 21:17 replacement.txt
lrwxr-xr-x@ 1 raffi  staff  12 31 Oct 19:33 shortcut.txt -> original.txt
raffi@Raffis-Mac link-practice % cat shortcut.txt
ORIGINAL CONTENT
```

In the long listing, what does the line for `shortcut.txt` show about its file
type and stored target pathname?

> its file type is a link (l) and the stored target pathname is original.txt

## Part 3 — Change the target's data

The link itself will not be replaced. Instead, overwrite the existing target
with the distinct prepared content.

Predict the results before running anything:

| Path read with `cat` | Predicted content after target replacement |
| -------------------- | ------------------------------------------ |
| `original.txt`       | REPLACEMENT CONTENT                        |
| `shortcut.txt`       | REPLACEMENT CONTENT                        |
| `replacement.txt`    | REPLACEMENT CONTENT                        |

Run this command and answer `y` to its prompt:

```bash
cp -i replacement.txt original.txt
```

Then run these separately:

```bash
cat original.txt
```

```bash
cat shortcut.txt
```

```bash
cat replacement.txt
```

```bash
ls -l
```

Record the prompt, response, and complete inspection output:

```text
raffi@Raffis-Mac link-practice % cp -i replacement.txt original.txt
overwrite original.txt? (y/n [n]) y
raffi@Raffis-Mac link-practice % cat original.txt
REPLACEMENT CONTENT
raffi@Raffis-Mac link-practice % cat shortcut.txt
REPLACEMENT CONTENT
raffi@Raffis-Mac link-practice % cat replacement.txt
REPLACEMENT CONTENT
raffi@Raffis-Mac link-practice % ls -l
total 16
-rw-r--r--@ 1 raffi  staff  20 31 Oct 19:35 original.txt
-rw-r--r--@ 1 raffi  staff  20 30 Oct 21:17 replacement.txt
lrwxr-xr-x@ 1 raffi  staff  12 31 Oct 19:33 shortcut.txt -> original.txt
```

Did the symbolic link store an old independent copy of the content, or did
opening it reach the current data at `original.txt`? Cite the observation.

> it reach the current data at original.txt,
> this is the evidence:
> raffi@Raffis-Mac link-practice % cat shortcut.txt
REPLACEMENT CONTENT

## Part 4 — Remove the target pathname

Before acting, predict:

| Path                              | Predicted state after removing `original.txt` |
| --------------------------------- | --------------------------------------------- |
| `original.txt`                    | Removed                                       |
| `shortcut.txt` entry              | Removed                                       |
| Reading `shortcut.txt` with `cat` | Error or don't exists                         |
| `replacement.txt`                 | Remain                                        |

Run and answer `y`:

```bash
rm -i original.txt
```

Then inspect:

```bash
ls -l
```

```bash
cat shortcut.txt
```

```bash
cat replacement.txt
```

Record the removal prompt and all inspection output:

```text
raffi@Raffis-Mac link-practice % rm -i original.txt
remove original.txt? y
raffi@Raffis-Mac link-practice % ls -l
total 8
-rw-r--r--@ 1 raffi  staff  20 30 Oct 21:17 replacement.txt
lrwxr-xr-x@ 1 raffi  staff  12 31 Oct 19:33 shortcut.txt -> original.txt
raffi@Raffis-Mac link-practice % cat shortcut.txt
cat: shortcut.txt: No such file or directory
raffi@Raffis-Mac link-practice % cat replacement.txt
REPLACEMENT CONTENT
```

Explain the difference between “the link entry still exists” and “the target
pathname currently resolves to a file”:

> i don't know what u mean

## Part 5 — Restore the target

The target pathname is missing, so this copy does not replace an existing file:

```bash
cp replacement.txt original.txt
```

Without recreating `shortcut.txt`, inspect:

```bash
cat shortcut.txt
```

```bash
ls -l
```

Record the complete output:

```text
raffi@Raffis-Mac link-practice % cp replacement.txt original.txt
raffi@Raffis-Mac link-practice % cat shortcut.txt
REPLACEMENT CONTENT
raffi@Raffis-Mac link-practice % ls -l
total 16
-rw-r--r--@ 1 raffi  staff  20 31 Oct 19:39 original.txt
-rw-r--r--@ 1 raffi  staff  20 30 Oct 21:17 replacement.txt
lrwxr-xr-x@ 1 raffi  staff  12 31 Oct 19:33 shortcut.txt -> original.txt
```

Why did the old link begin working again when `original.txt` was recreated?

> because the original.txt is linked in the shortcut.txt, the shortcut.txt turns out still exists, it just needs its original.txt file again

## Part 6 — Remove only the link

Predict the final state:

| Path                      | Predicted state after removing `shortcut.txt` |
| ------------------------- | --------------------------------------------- |
| `shortcut.txt`            | Removed                                       |
| `original.txt`            | Remain                                        |
| Content of `original.txt` | REPLACEMENT CONTENT                           |

Run and answer `y`:

```bash
rm -i shortcut.txt
```

Then verify:

```bash
ls -l
```

```bash
cat original.txt
```

```bash
ls -l shortcut.txt
```

Record the prompt and complete verification output:

```text
raffi@Raffis-Mac link-practice % rm -i shortcut.txt
remove shortcut.txt? y
raffi@Raffis-Mac link-practice % ls -l
total 16
-rw-r--r--@ 1 raffi  staff  20 31 Oct 19:39 original.txt
-rw-r--r--@ 1 raffi  staff  20 30 Oct 21:17 replacement.txt
raffi@Raffis-Mac link-practice % cat original.txt
REPLACEMENT CONTENT
raffi@Raffis-Mac link-practice % ls -l shortcut.txt
ls: shortcut.txt: No such file or directory
```

## Explain the model

1. What information does a symbolic link store?

   > the current data of original.txt

2. Why can changing the target be observed through the link?

   > because we linked it with ln

3. Why does deleting the target leave a dangling link instead of deleting the
   link entry automatically?

   > because we are not removing the link we are removing the target

4. Why does deleting the symbolic link leave the target unchanged?

   > because deleting the link does not mean also removing the target or original

5. State one important difference between a copied file and a symbolic link.

   > copied file is an independent file based on the original source while symbolic link stores the current target data/original data

Stop here and tell the tutor when the worksheet is ready.

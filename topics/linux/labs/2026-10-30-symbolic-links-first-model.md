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
TODO
```

## Part 2 — Predict and create the symbolic link

Before running the creation command, predict:

| Question | Prediction |
| -------- | ---------- |
| Which new pathname will be created? | TODO |
| Will a second copy of `ORIGINAL CONTENT` be created as independent file data? | TODO |
| What should `cat shortcut.txt` display? | TODO |
| Will `original.txt` still exist? | TODO |

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
TODO
```

In the long listing, what does the line for `shortcut.txt` show about its file
type and stored target pathname?

> TODO

## Part 3 — Change the target's data

The link itself will not be replaced. Instead, overwrite the existing target
with the distinct prepared content.

Predict the results before running anything:

| Path read with `cat` | Predicted content after target replacement |
| -------------------- | ------------------------------------------ |
| `original.txt` | TODO |
| `shortcut.txt` | TODO |
| `replacement.txt` | TODO |

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
TODO
```

Did the symbolic link store an old independent copy of the content, or did
opening it reach the current data at `original.txt`? Cite the observation.

> TODO

## Part 4 — Remove the target pathname

Before acting, predict:

| Path | Predicted state after removing `original.txt` |
| ---- | --------------------------------------------- |
| `original.txt` | TODO |
| `shortcut.txt` entry | TODO |
| Reading `shortcut.txt` with `cat` | TODO |
| `replacement.txt` | TODO |

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
TODO
```

Explain the difference between “the link entry still exists” and “the target
pathname currently resolves to a file”:

> TODO

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
TODO
```

Why did the old link begin working again when `original.txt` was recreated?

> TODO

## Part 6 — Remove only the link

Predict the final state:

| Path | Predicted state after removing `shortcut.txt` |
| ---- | --------------------------------------------- |
| `shortcut.txt` | TODO |
| `original.txt` | TODO |
| Content of `original.txt` | TODO |

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
TODO
```

## Explain the model

1. What information does a symbolic link store?

   > TODO

2. Why can changing the target be observed through the link?

   > TODO

3. Why does deleting the target leave a dangling link instead of deleting the
   link entry automatically?

   > TODO

4. Why does deleting the symbolic link leave the target unchanged?

   > TODO

5. State one important difference between a copied file and a symbolic link.

   > TODO

Stop here and tell the tutor when the worksheet is ready.

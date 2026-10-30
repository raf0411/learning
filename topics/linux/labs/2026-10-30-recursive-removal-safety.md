# Lab — Recursive Removal with a Verified Boundary

Date: 2026-10-30

## Purpose

Learn why `rmdir` and plain `rm` protect a nonempty directory, then deliberately
remove one disposable hierarchy with `rm -R` after verifying its exact boundary.

## Safety boundary

Only this disposable hierarchy will be recursively removed:

```text
/Users/raffi/Learning/topics/linux/labs/recursive-removal-practice/doomed-tree
```

The neighboring `keep-tree` directory and `sentinel.txt` file must remain.

- Do not use a wildcard in the removal command.
- Do not use `-f`.
- Stop if `pwd` does not show the expected practice directory.
- Stop if the inspection output differs materially from the planned tree.

The locally installed `rm` manual describes `-R` as removing the hierarchy
rooted at each named argument. It also says that `-r` is equivalent to `-R` on
this machine. We will use `-R` visibly and name one exact target.

## Part 1 — Predict the command boundaries

The lab will build this structure:

```text
recursive-removal-practice/
|-- doomed-tree/
|   |-- top.txt
|   `-- nested/
|       `-- inside.txt
|-- keep-tree/
|   `-- keep.txt
`-- sentinel.txt
```

Before creating it, predict the result of each command when run from inside
`recursive-removal-practice`:

| Command             | Succeeds or fails? | What remains afterward?                                                                                     |
| ------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------- |
| `rmdir doomed-tree` | fails              | doomed-tree, doomed-tree/top.txt, doomed-tree/nested/inside.txt, keep-tree, keep-tree/keep.txt sentinel.txt |
| `rm doomed-tree`    | fails              | doomed-tree, doomed-tree/top.txt, doomed-tree/nested/inside.txt, keep-tree, keep-tree/keep.txt sentinel.txt |
| `rm -R doomed-tree` | succeeds           | keep-tree, keep-tree/keep.txt sentinel.txt                                                                  |

Which exact directory hierarchy is an argument to the third command?

> doomed-tree

Do `keep-tree` or `sentinel.txt` appear as arguments to that command?

> yes

## Part 2 — Build and inspect the disposable fixture

Run these commands separately:

```bash
cd /Users/raffi/Learning/topics/linux/labs
```

```bash
mkdir -p recursive-removal-practice/doomed-tree/nested recursive-removal-practice/keep-tree
```

```bash
touch recursive-removal-practice/doomed-tree/top.txt recursive-removal-practice/doomed-tree/nested/inside.txt recursive-removal-practice/keep-tree/keep.txt recursive-removal-practice/sentinel.txt
```

```bash
cd recursive-removal-practice
```

Confirm the base directory:

```bash
pwd
```

Record the output:

```text
raffi@Raffis-Mac glob-practice % cd /Users/raffi/Learning/topics/linux/labs
raffi@Raffis-Mac labs % mkdir -p recursive-removal-practice/doomed-tree/nested recursive-removal-practice/keep-tree
raffi@Raffis-Mac labs % touch recursive-removal-practice/doomed-tree/top.txt recursive-removal-practice/doomed-tree/nested/inside.txt recursive-removal-practice/keep-tree/keep.txt recursive-removal-practice/sentinel.txt
raffi@Raffis-Mac labs %
raffi@Raffis-Mac labs % cd recursive-removal-practice
raffi@Raffis-Mac recursive-removal-practice % pwd
/Users/raffi/Learning/topics/linux/labs/recursive-removal-practice
```

Inspect every branch with these separate commands:

```bash
ls -la
```

```bash
ls -la doomed-tree
```

```bash
ls -la doomed-tree/nested
```

```bash
ls -la keep-tree
```

Record all four commands and their complete output:

```text
raffi@Raffis-Mac recursive-removal-practice % ls -la
total 0
drwxr-xr-x@  5 raffi  staff  160 30 Oct 18:30 .
drwxr-xr-x@ 25 raffi  staff  800 30 Oct 18:30 ..
drwxr-xr-x@  4 raffi  staff  128 30 Oct 18:30 doomed-tree
drwxr-xr-x@  3 raffi  staff   96 30 Oct 18:30 keep-tree
-rw-r--r--@  1 raffi  staff    0 30 Oct 18:30 sentinel.txt
raffi@Raffis-Mac recursive-removal-practice % ls -la doomed-tree
total 0
drwxr-xr-x@ 4 raffi  staff  128 30 Oct 18:30 .
drwxr-xr-x@ 5 raffi  staff  160 30 Oct 18:30 ..
drwxr-xr-x@ 3 raffi  staff   96 30 Oct 18:30 nested
-rw-r--r--@ 1 raffi  staff    0 30 Oct 18:30 top.txt
raffi@Raffis-Mac recursive-removal-practice % ls -la doomed-tree/nested
total 0
drwxr-xr-x@ 3 raffi  staff   96 30 Oct 18:30 .
drwxr-xr-x@ 4 raffi  staff  128 30 Oct 18:30 ..
-rw-r--r--@ 1 raffi  staff    0 30 Oct 18:30 inside.txt
raffi@Raffis-Mac recursive-removal-practice % ls -la keep-tree
total 0
drwxr-xr-x@ 3 raffi  staff   96 30 Oct 18:30 .
drwxr-xr-x@ 5 raffi  staff  160 30 Oct 18:30 ..
-rw-r--r--@ 1 raffi  staff    0 30 Oct 18:30 keep.txt
```

Does the recorded evidence match the planned tree? Account for each of these:

| Expected path                   | Evidence that proves it exists                                                                                                                                                                                                                                                                                                                               |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `doomed-tree/top.txt`           | raffi@Raffis-Mac recursive-removal-practice % ls -la doomed-tree<br>total 0<br>drwxr-xr-x@ 4 raffi  staff  128 30 Oct 18:30 .<br>drwxr-xr-x@ 5 raffi  staff  160 30 Oct 18:30 ..<br>drwxr-xr-x@ 3 raffi  staff   96 30 Oct 18:30 nested<br>-rw-r--r--@ 1 raffi  staff    0 30 Oct 18:30 top.txt                                                              |
| `doomed-tree/nested/inside.txt` | raffi@Raffis-Mac recursive-removal-practice % ls -la doomed-tree/nested<br>total 0<br>drwxr-xr-x@ 3 raffi  staff   96 30 Oct 18:30 .<br>drwxr-xr-x@ 4 raffi  staff  128 30 Oct 18:30 ..<br>-rw-r--r--@ 1 raffi  staff    0 30 Oct 18:30 inside.txt                                                                                                           |
| `keep-tree/keep.txt`            | raffi@Raffis-Mac recursive-removal-practice % ls -la keep-tree<br>total 0<br>drwxr-xr-x@ 3 raffi  staff   96 30 Oct 18:30 .<br>drwxr-xr-x@ 5 raffi  staff  160 30 Oct 18:30 ..<br>-rw-r--r--@ 1 raffi  staff    0 30 Oct 18:30 keep.txt                                                                                                                      |
| `sentinel.txt`                  | raffi@Raffis-Mac recursive-removal-practice % ls -la<br>total 0<br>drwxr-xr-x@  5 raffi  staff  160 30 Oct 18:30 .<br>drwxr-xr-x@ 25 raffi  staff  800 30 Oct 18:30 ..<br>drwxr-xr-x@  4 raffi  staff  128 30 Oct 18:30 doomed-tree<br>drwxr-xr-x@  3 raffi  staff   96 30 Oct 18:30 keep-tree<br>-rw-r--r--@  1 raffi  staff    0 30 Oct 18:30 sentinel.txt |

## Part 3 — Observe the two protections

Run:

```bash
rmdir doomed-tree
```

Record the command and complete output:

```text
rmdir: doomed-tree: Directory not empty
```

Now run:

```bash
rm doomed-tree
```

Record the command and complete output:

```text
rm: doomed-tree: is a directory
```

Verify that the hierarchy still exists:

```bash
ls -ld doomed-tree
```

Record the output:

```text
drwxr-xr-x@ 4 raffi  staff  128 30 Oct 18:30 doomed-tree
```

Explain the different reason each command refused the target:

> `rmdir` refused because directory is not empty

> Plain `rm` refused because selected target is a directory, rm is for removing files

## Part 4 — Remove one verified hierarchy

Before removing anything, state the exact current working directory and the
exact absolute target that the relative operand `doomed-tree` resolves to:

> Current working directory: doomed-tree

> Absolute target: /Users/raffi/Learning/topics/linux/labs/recursive-removal-practice/doomed-tree

Predict the state immediately after the command:

| Path                            | Remain or be removed? | Why?                                       |
| ------------------------------- | --------------------- | ------------------------------------------ |
| `doomed-tree`                   | removed               | because of -R                              |
| `doomed-tree/top.txt`           | removed               | because it is inside doomed-tree           |
| `doomed-tree/nested/inside.txt` | removed               | because it is inside doomed-tree           |
| `keep-tree/keep.txt`            | remain                | we're only targeting doomed-tree directory |
| `sentinel.txt`                  | remain                | we're only targeting doomed-tree directory |

If the inspection and target above are correct, run this exact command:

```bash
rm -R doomed-tree
```

Record the command and any output:

```text

```

Verify the parent directory and the protected neighbor:

```bash
ls -la
```

```bash
ls -la keep-tree
```

Finally, request the removed target explicitly:

```bash
ls -ld doomed-tree
```

Record all three commands and their complete output:

```text
raffi@Raffis-Mac recursive-removal-practice % ls -la
total 0
drwxr-xr-x@  4 raffi  staff  128 30 Oct 18:44 .
drwxr-xr-x@ 25 raffi  staff  800 30 Oct 18:30 ..
drwxr-xr-x@  3 raffi  staff   96 30 Oct 18:30 keep-tree
-rw-r--r--@  1 raffi  staff    0 30 Oct 18:30 sentinel.txt
raffi@Raffis-Mac recursive-removal-practice % ls -la keep-tree
total 0
drwxr-xr-x@ 3 raffi  staff   96 30 Oct 18:30 .
drwxr-xr-x@ 4 raffi  staff  128 30 Oct 18:44 ..
-rw-r--r--@ 1 raffi  staff    0 30 Oct 18:30 keep.txt
raffi@Raffis-Mac recursive-removal-practice % ls -ld doomed-tree
ls: doomed-tree: No such file or directory
raffi@Raffis-Mac recursive-removal-practice %
```

## Explain the model

1. What did `-R` change about what `rm` was allowed to remove?

   > it allows removal even for a directory and even if its not empty

2. Did `-R` cause `rm` to remove neighboring paths that were not beneath the
   named target? Cite the final evidence.

   > No, because keep-tree still exists
   > evidence:
   > raffi@Raffis-Mac recursive-removal-practice % ls -la keep-tree
total 0
drwxr-xr-x@ 3 raffi  staff   96 30 Oct 18:30 .
drwxr-xr-x@ 4 raffi  staff  128 30 Oct 18:44 ..
-rw-r--r--@ 1 raffi  staff    0 30 Oct 18:30 keep.txt

3. Why is the expected `No such file or directory` result from
   `ls -ld doomed-tree` useful evidence rather than proof that removal failed?

   > it means that the removal using rm -R doomed-tree works, the directory does not exists anymore

4. Why were `pwd` and the pre-removal listings important when the removal
   operand was relative?

   > to confirm that it didn't change our current working directory in the current shell

Stop here and tell the tutor when the worksheet is ready.

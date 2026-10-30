# Lab — Safe File and Empty-Directory Removal

Date: 2026-10-29

## Purpose

Practice a deliberate removal loop:

```text
orient -> inspect the exact target -> remove interactively -> verify
```

Every target in this lab is disposable and contained within the new
`labs/removal-practice` directory.

## Working model

The installed local manuals describe the commands this way:

- `rm` removes the named non-directory entries. `-i` requests confirmation
  before each attempt.
- `rmdir` removes a named directory only if that directory is empty.

Unlike deleting through a graphical file manager, `rm` does not normally move
its target into a Trash folder. Treat a successful removal as lacking a simple
built-in undo.

We will not use recursive removal in this lab.

## Part 1 — Build and inspect the disposable tree

Run these commands separately:

```bash
cd /Users/raffi/Learning/topics/linux/labs
```

```bash
mkdir removal-practice
```

```bash
cd removal-practice
```

```bash
touch keep.txt remove-me.txt
```

```bash
mkdir empty-dir nonempty-dir
```

```bash
touch nonempty-dir/inside.txt
```

Before removing anything, run these inspection commands separately:

```bash
pwd
```

```bash
ls -la
```

```bash
ls -la nonempty-dir
```

Record the complete inspection output:

```text
raffi@Raffis-Mac removal-practice % ls -la
total 0
drwxr-xr-x@  6 raffi  staff  192 30 Oct 14:02 .
drwxr-xr-x@ 21 raffi  staff  672 30 Oct 14:02 ..
drwxr-xr-x@  2 raffi  staff   64 30 Oct 14:02 empty-dir
-rw-r--r--@  1 raffi  staff    0 30 Oct 14:02 keep.txt
drwxr-xr-x@  3 raffi  staff   96 30 Oct 14:02 nonempty-dir
-rw-r--r--@  1 raffi  staff    0 30 Oct 14:02 remove-me.txt
raffi@Raffis-Mac removal-practice % ls -la nonempty-dir
total 0
drwxr-xr-x@ 3 raffi  staff   96 30 Oct 14:02 .
drwxr-xr-x@ 6 raffi  staff  192 30 Oct 14:02 ..
-rw-r--r--@ 1 raffi  staff    0 30 Oct 14:02 inside.txt
raffi@Raffis-Mac removal-practice %
```

Confirm from the output:

| Safety question                                             | Evidence from the output                                                                   |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Are you inside the disposable `removal-practice` directory? | yes                                                                                        |
| Does `remove-me.txt` exist?                                 | yes                                                                                        |
| Is `empty-dir` empty apart from `.` and `..`?               | no                                                                                         |
| What makes `nonempty-dir` nonempty?                         | because inside.txt is inside nonempty-dir, we added it using touch nonempty-dir/inside.txt |

## Part 2 — Decline and accept file removal

Predict the state after answering `n` to:

```bash
rm -i remove-me.txt
```

| Question                           | Prediction |
| ---------------------------------- | ---------- |
| Will `remove-me.txt` remain?       | yes        |
| Will `keep.txt` remain?            | yes        |
| Will the working directory change? | no         |

Run the command, answer `n`, then verify with these separate commands:

```bash
ls -l remove-me.txt keep.txt
```

```bash
pwd
```

Record the prompt, response, and verification output:

```text
raffi@Raffis-Mac removal-practice % rm -i remove-me.txt
remove remove-me.txt? n
raffi@Raffis-Mac removal-practice % ls -l remove-me.txt keep.txt
-rw-r--r--@ 1 raffi  staff  0 30 Oct 14:02 keep.txt
-rw-r--r--@ 1 raffi  staff  0 30 Oct 14:02 remove-me.txt
raffi@Raffis-Mac removal-practice % pwd
/Users/raffi/Learning/topics/linux/labs/removal-practice
raffi@Raffis-Mac removal-practice %
```

Now predict the state after running the same command and answering `y`:

| Question                           | Prediction |
| ---------------------------------- | ---------- |
| Will `remove-me.txt` remain?       | no         |
| Will `keep.txt` remain?            | yes        |
| Will the working directory change? | no         |

Run `rm -i remove-me.txt` again and answer `y`. Then run these separately:

```bash
ls -l remove-me.txt
```

```bash
ls -l keep.txt
```

```bash
pwd
```

Record all output, including any error:

```text
raffi@Raffis-Mac removal-practice % rm -i remove-me.txt
remove remove-me.txt? y
raffi@Raffis-Mac removal-practice % ls -l remove-me.txt keep.txt
ls: remove-me.txt: No such file or directory
-rw-r--r--@ 1 raffi  staff  0 30 Oct 14:02 keep.txt
raffi@Raffis-Mac removal-practice % pwd
/Users/raffi/Learning/topics/linux/labs/removal-practice
raffi@Raffis-Mac removal-practice %
```

Explain why an error from `ls -l remove-me.txt` would be useful verification
rather than evidence that `rm -i` failed:

it confirms that the remove-me.txt was deleted because it says it was not found or no such file exists

## Part 3 — Let `rmdir` protect a nonempty directory

Predict the results of these two commands before running either:

```bash
rmdir nonempty-dir
```

```bash
rmdir empty-dir
```

| Target         | Succeed or fail? | Why?                            |
| -------------- | ---------------- | ------------------------------- |
| `nonempty-dir` | no               | because the folder is not empty |
| `empty-dir`    | yes              | because the folder is empty     |

Run both commands separately, in the order shown. Then verify with:

```bash
ls -la
```

```bash
ls -la nonempty-dir
```

Record all output, including any error:

```text
raffi@Raffis-Mac removal-practice % rmdir nonempty-dir
rmdir: nonempty-dir: Directory not empty
raffi@Raffis-Mac removal-practice % rmdir empty-dir
raffi@Raffis-Mac removal-practice % ls -la
total 0
drwxr-xr-x@  4 raffi  staff  128 30 Oct 14:08 .
drwxr-xr-x@ 21 raffi  staff  672 30 Oct 14:02 ..
-rw-r--r--@  1 raffi  staff    0 30 Oct 14:02 keep.txt
drwxr-xr-x@  3 raffi  staff   96 30 Oct 14:02 nonempty-dir
raffi@Raffis-Mac removal-practice % ls -la nonempty-dir
total 0
drwxr-xr-x@ 3 raffi  staff   96 30 Oct 14:02 .
drwxr-xr-x@ 4 raffi  staff  128 30 Oct 14:08 ..
-rw-r--r--@ 1 raffi  staff    0 30 Oct 14:02 inside.txt
raffi@Raffis-Mac removal-practice %
```

## Part 4 — Remove a nonempty tree deliberately, leaf first

Do not use recursive removal. Write the two commands that will:

1. interactively remove `nonempty-dir/inside.txt`;
2. remove `nonempty-dir` after it becomes empty.

```bash
rm -i nonempty-dir/inside.txt
rmdir nonempty-dir
```

Before running them, predict which path or paths should remain in the current
directory afterward:

removal/practice/keep.txt

Run your commands, answering `y` to the interactive prompt. Then verify with:

```bash
ls -la
```

```bash
pwd
```

Record the prompt and complete verification output:

```text
raffi@Raffis-Mac removal-practice % rm -i nonempty-dir/inside.txt
remove nonempty-dir/inside.txt? y
raffi@Raffis-Mac removal-practice % rmdir nonempty-dir
raffi@Raffis-Mac removal-practice % ls -la
total 0
drwxr-xr-x@  3 raffi  staff   96 30 Oct 14:12 .
drwxr-xr-x@ 21 raffi  staff  672 30 Oct 14:02 ..
-rw-r--r--@  1 raffi  staff    0 30 Oct 14:02 keep.txt
raffi@Raffis-Mac removal-practice % pwd
/Users/raffi/Learning/topics/linux/labs/removal-practice
raffi@Raffis-Mac removal-practice %
```

## Explain the safety model

1. Why is `pwd` useful before a removal command that uses relative paths?

   to make sure we are not changing the directory in the shell

2. What protection did `rm -i` provide?

   it confirms or ask us if want to delete it or not

3. What protection did `rmdir` provide?

   it make sure it wont delete folders that are not empty

4. Which commands changed the filesystem without changing the shell's working
   directory?

   rm and rmdir maybe, this is my guess

Stop here and tell the tutor when the worksheet is ready.

## Tutor feedback — focused correction (2026-10-30)

The removal work itself was successful and safe:

- both `rm -i` predictions matched the observed results;
- `keep.txt` remained throughout;
- both `rmdir` predictions matched the observed results;
- the two leaf-first removal commands were correct;
- direct inspection by the tutor confirmed that only `keep.txt` remains.

### Evidence correction

The original worksheet had an evidence gap. `ls -la` in
`removal-practice` showed that an entry named `empty-dir` existed, but it did
not list the entries *inside* that directory. The worksheet should also have
requested:

```bash
ls -la empty-dir
```

Because `empty-dir` has now been deliberately removed, do not recreate it just
to repair the old transcript. Use the later result instead: `rmdir empty-dir`
returned without an error, while `rmdir nonempty-dir` reported
`Directory not empty`.

Reconcile the original answer using that evidence:

> Immediately before the two `rmdir` commands, was `empty-dir` empty? What
> observed difference between the two commands supports your answer?

yes it was, because when i rmdir empty-dir it works, but when i rmdir nonempty-dir it didnt work

### Path correction

Immediately before the final removals, `pwd` showed:

```text
/Users/raffi/Learning/topics/linux/labs/removal-practice
```

Afterward, only `keep.txt` remained. Write both exact names for that file:

| Form                                       | Exact path                                                        |
| ------------------------------------------ | ----------------------------------------------------------------- |
| Relative to the recorded working directory | keep.txt                                                          |
| Absolute                                   | /Users/raffi/Learning/topics/linux/labs/removal-practice/keep.txt |

### Safety-model correction

1. `pwd` only observes and prints state; it does not prevent another command
   from changing directories. Why is its output still useful before running
   `rm` with a relative target such as `remove-me.txt`?

   to confirm we are in the directory we wanted to be.

2. Classify every command used to build, inspect, and remove this lab tree.
   Put each command name in one row only.

| Effect                                                                    | Command names           |
| ------------------------------------------------------------------------- | ----------------------- |
| Changes filesystem entries without changing the shell's working directory | rmdir, mkdir, touch, rm |
| Changes the shell's working directory                                     | cd                      |
| Only observes state in this lab                                           | pwd, ls                 |

Complete these corrections and tell the tutor when they are ready.

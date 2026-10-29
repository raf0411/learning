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
TODO
```

Confirm from the output:

| Safety question | Evidence from the output |
| --- | --- |
| Are you inside the disposable `removal-practice` directory? | TODO |
| Does `remove-me.txt` exist? | TODO |
| Is `empty-dir` empty apart from `.` and `..`? | TODO |
| What makes `nonempty-dir` nonempty? | TODO |

## Part 2 — Decline and accept file removal

Predict the state after answering `n` to:

```bash
rm -i remove-me.txt
```

| Question | Prediction |
| --- | --- |
| Will `remove-me.txt` remain? | TODO |
| Will `keep.txt` remain? | TODO |
| Will the working directory change? | TODO |

Run the command, answer `n`, then verify with these separate commands:

```bash
ls -l remove-me.txt keep.txt
```

```bash
pwd
```

Record the prompt, response, and verification output:

```text
TODO
```

Now predict the state after running the same command and answering `y`:

| Question | Prediction |
| --- | --- |
| Will `remove-me.txt` remain? | TODO |
| Will `keep.txt` remain? | TODO |
| Will the working directory change? | TODO |

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
TODO
```

Explain why an error from `ls -l remove-me.txt` would be useful verification
rather than evidence that `rm -i` failed:

TODO

## Part 3 — Let `rmdir` protect a nonempty directory

Predict the results of these two commands before running either:

```bash
rmdir nonempty-dir
```

```bash
rmdir empty-dir
```

| Target | Succeed or fail? | Why? |
| --- | --- | --- |
| `nonempty-dir` | TODO | TODO |
| `empty-dir` | TODO | TODO |

Run both commands separately, in the order shown. Then verify with:

```bash
ls -la
```

```bash
ls -la nonempty-dir
```

Record all output, including any error:

```text
TODO
```

## Part 4 — Remove a nonempty tree deliberately, leaf first

Do not use recursive removal. Write the two commands that will:

1. interactively remove `nonempty-dir/inside.txt`;
2. remove `nonempty-dir` after it becomes empty.

```bash
TODO
```

Before running them, predict which path or paths should remain in the current
directory afterward:

TODO

Run your commands, answering `y` to the interactive prompt. Then verify with:

```bash
ls -la
```

```bash
pwd
```

Record the prompt and complete verification output:

```text
TODO
```

## Explain the safety model

1. Why is `pwd` useful before a removal command that uses relative paths?

   TODO

2. What protection did `rm -i` provide?

   TODO

3. What protection did `rmdir` provide?

   TODO

4. Which commands changed the filesystem without changing the shell's working
   directory?

   TODO

Stop here and tell the tutor when the worksheet is ready.

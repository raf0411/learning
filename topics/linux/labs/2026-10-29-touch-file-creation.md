# Lab — Creating Empty Files with `touch`

Date: 2026-10-29

## Purpose

Learn what `touch` fundamentally does, then verify its file-creation behavior
without confusing it with directory creation or shell navigation.

All changes stay inside the disposable `labs/touch-practice` directory.

## Working model

The installed local manual describes `touch` as a command that changes file
access and modification times. If a named file does not exist, `touch` creates
it with default permissions.

Therefore, using `touch` to make an empty placeholder file is useful behavior,
but timestamp handling is the command's primary purpose.

## Part 1 — Plan before executing

Assume you begin somewhere unknown in the terminal. Write the commands you
would use, in order, to:

1. move to `/Users/raffi/Learning/topics/linux/labs`;
2. create the new directory `touch-practice` without using `-p`;
3. enter that directory;
4. print the working directory;
5. create `draft.txt`, `notes.txt`, and `ready.marker` with one `touch` command;
6. print the working directory again;
7. list the new files in long format.

Write your commands here, one command per physical line:

```bash
raffi@Raffis-Mac labs % mkdir touch-practice
raffi@Raffis-Mac labs % cd touch-practice
raffi@Raffis-Mac touch-practice % pwd
raffi@Raffis-Mac touch-practice % touch draft.txt notes.txt ready.marker
raffi@Raffis-Mac touch-practice % ls
raffi@Raffis-Mac touch-practice % pwd
```

Before running them, predict:

| Question                                   | Prediction                  |
| ------------------------------------------ | --------------------------- |
| Exact path of `draft.txt`                  | touch-practice/draft.txt    |
| Exact path of `notes.txt`                  | touch-practice/notes.txt    |
| Exact path of `ready.marker`               | touch-practice/ready.marker |
| Will `touch` change the working directory? | no                          |
| Expected size of each newly created file   | 0 kb                        |

Now run your commands exactly as written. Record the complete output from both
`pwd` commands and the long listing:

```text
raffi@Raffis-Mac labs % mkdir touch-practice
raffi@Raffis-Mac labs % cd touch-practice
raffi@Raffis-Mac touch-practice % pwd
/Users/raffi/Learning/topics/linux/labs/touch-practice
raffi@Raffis-Mac touch-practice % touch draft.txt notes.txt ready.marker
raffi@Raffis-Mac touch-practice % ls
draft.txt	notes.txt	ready.marker
raffi@Raffis-Mac touch-practice % pwd
/Users/raffi/Learning/topics/linux/labs/touch-practice
raffi@Raffis-Mac touch-practice %
```

Compare the observations with every prediction. Explain any mismatch:

no mismatch

## Part 2 — A missing parent directory

The directory `reports` should not exist yet. Predict what this command will do:

```bash
touch reports/daily.txt
```

| Question                                             | Prediction            |
| ---------------------------------------------------- | --------------------- |
| Will the command succeed?                            | no                    |
| Will `touch` create the missing `reports` directory? | no                    |
| Reason                                               | idk just a prediction |

Run the command and record its complete output, including any error:

```text
raffi@Raffis-Mac touch-practice % touch reports/daily.txt
touch: reports/daily.txt: No such file or directory
raffi@Raffis-Mac touch-practice %
```

Write and run the shortest two-command sequence that first creates the parent
directory and then creates `daily.txt` inside it. Do not use `mkdir -p` here.

```bash
mkdir reports
touch reports/daily.txt
```

Verify the result using both of these commands, run separately:

```bash
ls -l reports
```

```bash
pwd
```

Record the complete output:

```text
raffi@Raffis-Mac touch-practice % ls -l reports
total 0
-rw-r--r--@ 1 raffi  staff  0 29 Oct 16:31 daily.txt
raffi@Raffis-Mac touch-practice % pwd
/Users/raffi/Learning/topics/linux/labs/touch-practice
raffi@Raffis-Mac touch-practice %
```

## Explain the model

1. Why can `touch draft.txt` create a file, while
   `touch reports/daily.txt` initially cannot create the complete path?

   because reports directory does not exists

2. Which command in this lab changed the shell's working directory? Which
   commands created filesystem entries without changing it?

   cd, 
   mkdir, touch

3. If `draft.txt` already exists, what is the normal purpose of running
   `touch draft.txt` again?

   it will overwrites it, thats my prediction

Stop here and tell the tutor when the worksheet is ready.

---

## Tutor checkpoint — correct and verify

Your first attempt successfully created the requested filesystem entries, and
the missing-parent prediction matched the observed error. Complete these two
corrections before moving on.

### A. Make the command plan reproducible

The original plan assumed the terminal was already in `labs`, included shell
prompt text, and used `ls` instead of the requested `ls -l`.

Rewrite the complete seven-command plan here. Begin with the absolute `cd`
command, write commands only (no prompt text), and use the requested long
listing. Do not rerun `mkdir touch-practice`, because that directory now
exists.

For this correction, replace that creation step with a command that verifies
the directory already exists without entering it.

```bash
cd /Users/raffi/Learning/topics/linux/labs
ls touch-practice
cd touch-practice
pwd
touch draft.txt notes.txt ready.marker
pwd
ls -l
```

Write the absolute path of `draft.txt`:

```text
/Users/raffi/Learning/topics/linux/labs/touch-practice/draft.txt
```

Run this from `touch-practice` and record the output that verifies the three
original files are zero bytes:

```bash
ls -l draft.txt notes.txt ready.marker
```

```text
-rw-r--r--@ 1 raffi  staff  0 29 Oct 16:18 draft.txt
-rw-r--r--@ 1 raffi  staff  0 29 Oct 16:18 notes.txt
-rw-r--r--@ 1 raffi  staff  0 29 Oct 16:18 ready.marker
```

### B. Test `touch` on a nonempty existing file

The statement “`touch` overwrites an existing file” is incorrect. The local
manual says its normal purpose is to update file access and modification times.
Test whether that operation changes the file's content.

From inside `touch-practice`, run these commands separately and record all
output:

```bash
cp ../move-practice/archive/final.txt existing.txt
```

```bash
cat existing.txt
```

```bash
touch existing.txt
```

```bash
cat existing.txt
```

```bash
ls -l existing.txt
```

```text
raffi@Raffis-Mac touch-practice % cp ../move-practice/archive/final.txt existing.txt
raffi@Raffis-Mac touch-practice % cat existing.txt
Draft version 1
raffi@Raffis-Mac touch-practice % touch existing.txt
raffi@Raffis-Mac touch-practice % cat existing.txt
Draft version 1
raffi@Raffis-Mac touch-practice % ls -l existing.txt
-rw-r--r--@ 1 raffi  staff  16 29 Oct 16:44 existing.txt
```

What changed when you ran `touch existing.txt`, and what stayed unchanged?

the time updated changes based on ls -l and the content stays unchanged

Now tell the tutor the correction checkpoint is ready.

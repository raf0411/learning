# Lab — Add viewing line numbers with `nl`

Date: 2026-11-02

## Why this tool exists

Line numbers make it easier to refer to an exact place in text. `nl FILE`
prints a numbered view and returns to the shell; it does not write the numbers
into the stored file.

By default, `nl` numbers nonempty body lines. In `nl -ba FILE`, `-b` selects the
body-line numbering style and `a` means all lines, including blank ones.

## 1 — Inspect and predict

First view the six-line fixture:

```bash
cat labs/line-number-practice/note.txt
```

Record the command and complete output, preserving the blank lines:

```text
raffi@Raffis-Mac linux % cat labs/line-number-practice/note.txt
alpha

beta
gamma

delta
```

Before running `nl`, predict:

| Question                                             | Prediction                         |
| ---------------------------------------------------- | ---------------------------------- |
| Which lines will plain `nl` number?                  | alpha, beta, gamma, and delta line |
| Which lines will `nl -ba` number?                    | all lines                          |
| Will either command store numbers inside `note.txt`? | no                                 |

## 2 — Compare the two views

Run these separately:

```bash
nl labs/line-number-practice/note.txt
```

```bash
nl -ba labs/line-number-practice/note.txt
```

Record both commands and their complete output, preserving blank lines:

```text
raffi@Raffis-Mac linux % nl labs/line-number-practice/note.txt
     1	alpha

     2	beta
     3	gamma

     4	delta
raffi@Raffis-Mac linux % nl -ba labs/line-number-practice/note.txt
     1	alpha
     2
     3	beta
     4	gamma
     5
     6	delta
raffi@Raffis-Mac linux %
```

Describe the observed difference between the outputs:

> the first one only shows the line number on a nonempty line while the other shows it in every line

## 3 — Verify the stored file

Run the original inspection again:

```bash
cat labs/line-number-practice/note.txt
```

Record its complete output:

```text
raffi@Raffis-Mac linux % cat labs/line-number-practice/note.txt
alpha

beta
gamma

delta
```

Did either `nl` command modify the stored file? Cite the relevant evidence.

> no, because the cat shows that the content is still the same

## 4 — Choose between `nl` and `less -N`

Choose the better first command and explain why.

| Goal                                                                  | Command | Why                                                                                                         |
| --------------------------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------- |
| Print a numbered view of every line in a short file, including blanks | nl      | because its shot and nl can show every line number in a file even if its blank                              |
| Navigate and search a 50,000-line file while displaying line numbers  | less    | because less lets u navigate and search a long content file like that while also displaying the line number |

Stop and tell the tutor when the worksheet is ready.

## Tutor checkpoint

The predictions, blank-line comparison, and stored-file verification were
correct. When asked for option-precise commands without looking back, the
learner independently supplied:

```bash
nl -ba short.txt
less -N huge.log
```

# Lab — Where does a relative link start?

Date: 2026-10-31

## One new rule

A relative pathname supplied to a command normally starts from your shell's
current directory. But a relative pathname stored inside a symbolic link is
interpreted from the directory containing that link.

There are two lookups: first locate the link, then follow its stored target.
Changing your shell's directory does not move the link. Moving the link into
another directory changes the starting point for its stored relative target.

`ln -s` stores the target text you supply; it does not automatically rewrite
that text to account for where you put the link.

## Prepared fixture and safety

Work only inside:

```text
/Users/raffi/Learning/topics/linux/labs/relative-link-practice
```

The tutor prepared this structure:

```text
relative-link-practice/
├── data/
│   └── note.txt
└── links/
    └── deeper/
```

Only a new symbolic link will be created and moved. Do not modify or remove
`data/note.txt`. No deletion is needed. Run each command separately and stop
if the setup differs or a command fails unexpectedly.

## 1 — Create and inspect

```bash
cd /Users/raffi/Learning/topics/linux/labs/relative-link-practice
```

```bash
pwd
```

```bash
ls -la data links links/deeper
```

```bash
cat data/note.txt
```

From this lab root, create the link:

```bash
ln -s ../data/note.txt links/shortcut.txt
```

Before reading it, trace its stored pathname:

| Step                                                                    | Your answer                            |
| ----------------------------------------------------------------------- | -------------------------------------- |
| Directory containing `shortcut.txt` (relative to the lab root)          | ../data/note.txt                       |
| Starting there, where does `..` take you?                               | up by one level from current directory |
| Which file does the whole stored path reach (relative to the lab root)? | links/shortcut.txt                     |

```bash
ls -l links/shortcut.txt
```

```bash
cat links/shortcut.txt
```

Record commands and output, including the setup inspection:

```text
raffi@Raffis-Mac relative-link-practice % ls -l links/shortcut.txt
lrwxr-xr-x@ 1 raffi  staff  16 31 Oct 20:26 links/shortcut.txt -> ../data/note.txt
raffi@Raffis-Mac relative-link-practice % cat links/shortcut.txt
RELATIVE LINK CONTENT
```

## 2 — Move yourself, leaving the link in place

Predict: after changing into `links`, will `cat shortcut.txt` still reach the
same target? Explain briefly using the link's location.

> im it changes, because we moved directory, it should be relative to where u are right now

```bash
cd links
```

```bash
pwd
```

```bash
ls -l shortcut.txt
```

```bash
cat shortcut.txt
```

Record commands and output:

```text
raffi@Raffis-Mac relative-link-practice % cd links
raffi@Raffis-Mac links % pwd
/Users/raffi/Learning/topics/linux/labs/relative-link-practice/links
raffi@Raffis-Mac links % ls -l shortcut.txt
lrwxr-xr-x@ 1 raffi  staff  16 31 Oct 20:26 shortcut.txt -> ../data/note.txt
raffi@Raffis-Mac links % cat shortcut.txt
RELATIVE LINK CONTENT
```

## 3 — Move the link, leaving the target in place

Return to the lab root and inspect both ends of the move:

```bash
cd ..
```

```bash
pwd
```

```bash
ls -l links/shortcut.txt data/note.txt
```

```bash
ls -la links/deeper
```

Before moving the link into `links/deeper`, predict:

| Question                                                                                                         | Prediction            |
| ---------------------------------------------------------------------------------------------------------------- | --------------------- |
| What target text will the link store after the move?                                                             | RELATIVE LINK CONTENT |
| From its new containing directory, which target path will that text reach? Give a path relative to the lab root. | idk im confused now   |
| Will reading the moved link succeed or fail? Why?                                                                | succeed maybe?        |

Run the move only if `links/deeper` is still empty:

```bash
mv -i links/shortcut.txt links/deeper/shortcut.txt
```

The destination is new, so no overwrite prompt is expected. If prompted,
answer `n` and stop for review.

```bash
ls -l links/deeper/shortcut.txt
```

```bash
cat links/deeper/shortcut.txt
```

```bash
cat data/note.txt
```

Record commands and output, including any error:

```text
raffi@Raffis-Mac relative-link-practice % mv -i links/shortcut.txt links/deeper/shortcut.txt
raffi@Raffis-Mac relative-link-practice % ls -l links/deeper/shortcut.txt
lrwxr-xr-x@ 1 raffi  staff  16 31 Oct 20:26 links/deeper/shortcut.txt -> ../data/note.txt
raffi@Raffis-Mac relative-link-practice % cat links/deeper/shortcut.txt
cat: links/deeper/shortcut.txt: No such file or directory
raffi@Raffis-Mac relative-link-practice % cat data/note.txt
RELATIVE LINK CONTENT
raffi@Raffis-Mac relative-link-practice %
```

Explain why changing your current directory and moving the link produced
the observed results. Distinguish the path used to find the link from the
target pathname stored inside it.

> idk im confused at this part

Stop here and tell the tutor when the worksheet is ready. Leave everything
in place for review; do not repair or clean up yet.

## Guided correction — Compare one parent step with two

The discussion established that the moved link is inside `links/deeper/`.
Your proposed replacement target was `../data/note.txt`. This still goes up
only once. The correct target for this location is `../../data/note.txt`.

Trace the two separate upward steps:

```text
start             links/deeper/
first ../         links/
second ../        lab root
then data/        lab root/data/
then note.txt     lab root/data/note.txt
```

Compare the complete paths from the SAME starting directory:

| Stored target | Where it looks, relative to the lab root |
| --- | --- |
| `../data/note.txt` | `links/data/note.txt` — missing |
| `../../data/note.txt` | `data/note.txt` — the existing target |

We will create a second link named `repaired.txt` for comparison. Keep the
existing dangling `shortcut.txt` and the target file unchanged. This section
supersedes the earlier instruction to stop; no deletion is needed.

Run separately:

```bash
cd /Users/raffi/Learning/topics/linux/labs/relative-link-practice
```

```bash
pwd
```

```bash
ls -la links/deeper
```

```bash
cat data/note.txt
```

Continue only if `repaired.txt` is absent and the target is readable. If the
creation command reports that the name already exists, stop without replacing it.

```bash
ln -s ../../data/note.txt links/deeper/repaired.txt
```

```bash
ls -l links/deeper/shortcut.txt links/deeper/repaired.txt
```

```bash
cat links/deeper/shortcut.txt
```

```bash
cat links/deeper/repaired.txt
```

The old link's read is expected to fail; continue to read the new link.
Record the actual commands and output below. No additional written explanation
is needed for this step; we will use the side-by-side observations next.

```text
raffi@Raffis-Mac relative-link-practice % pwd
/Users/raffi/Learning/topics/linux/labs/relative-link-practice
raffi@Raffis-Mac relative-link-practice % ls -la links/deeper
total 0
drwxr-xr-x@ 3 raffi  staff  96 31 Oct 20:35 .
drwxr-xr-x@ 3 raffi  staff  96 31 Oct 20:35 ..
lrwxr-xr-x@ 1 raffi  staff  16 31 Oct 20:26 shortcut.txt -> ../data/note.txt
raffi@Raffis-Mac relative-link-practice % cat data/note.txt
RELATIVE LINK CONTENT
raffi@Raffis-Mac relative-link-practice % ln -s ../../data/note.txt links/deeper/repaired.txt
raffi@Raffis-Mac relative-link-practice % ls -l links/deeper/shortcut.txt links/deeper/repaired.txt
lrwxr-xr-x@ 1 raffi  staff  19 31 Oct 20:48 links/deeper/repaired.txt -> ../../data/note.txt
lrwxr-xr-x@ 1 raffi  staff  16 31 Oct 20:26 links/deeper/shortcut.txt -> ../data/note.txt
raffi@Raffis-Mac relative-link-practice % cat links/deeper/shortcut.txt
cat: links/deeper/shortcut.txt: No such file or directory
raffi@Raffis-Mac relative-link-practice % cat links/deeper/repaired.txt
RELATIVE LINK CONTENT
```

Stop here and tell the tutor when this comparison is ready.

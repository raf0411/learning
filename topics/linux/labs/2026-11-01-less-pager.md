# Lab — Inspect a longer file with `less`

Date: 2026-11-01

## Why this tool exists

`cat FILE` writes the whole file to terminal output. That is convenient when a
file is short enough to understand at once. For a longer file, the useful text
may rush past and become awkward to revisit.

`less FILE` opens a pager: a screen-by-screen view of the file. The controls in
this lab navigate and search without modifying the file.

We will inspect an existing 209-line session record. Do not edit it.

## 1 — Inspect the target

Run:

```bash
cd /Users/raffi/Learning/topics/linux
```

```bash
pwd
```

```bash
ls -l sessions/2026-10-31.md
```

Record commands and output:

```text
raffi@Raffis-Mac archive-checkpoint % cd /Users/raffi/Learning/topics/linux
raffi@Raffis-Mac linux % pwd
/Users/raffi/Learning/topics/linux
raffi@Raffis-Mac linux % ls -l sessions/2026-10-31.md
-rw-r--r--@ 1 raffi  staff  12325 31 Oct 21:06 sessions/2026-10-31.md
```

## 2 — Predict the interaction

Before opening the pager, predict:

| Question                                                                    | Prediction |
| --------------------------------------------------------------------------- | ---------- |
| Will `less` print all 209 lines and immediately return to the shell prompt? | no         |
| Will the navigation keys below change the file's stored contents?           | yes        |
| What key do you expect to use when you want to leave `less`?                | q          |

## 3 — Open and navigate

Submit this as one physical shell command:

```bash
less -N /Users/raffi/Learning/topics/linux/sessions/2026-10-31.md
```

`-N` displays line numbers. While `less` is open, use these pager controls:

| Key | Action |
| --- | --- |
| `Space` | Move forward one screen |
| `b` | Move backward one screen |
| `G` | Jump to the end |
| `g` | Jump to the beginning |
| `/archive` then `Enter` | Search forward for `archive` |
| `n` | Move to the next search match |
| `q` | Quit and return to the shell |

Perform this sequence:

1. Note the first visible numbered line.
2. Press `Space`, then note whether the visible lines changed.
3. Press `b`, then check whether you returned toward the beginning.
4. Press `G` and note the final line number.
5. Press `g` to return to the beginning.
6. Type `/archive`, press `Enter`, and record the matching line number and a
   short fragment of that line.
7. Press `n` and record the next matching line number and a short fragment.
8. Press `q`.

Do not use `v`, `s`, `!`, or other advanced controls in this lab.

Record observations rather than copying the whole file:

| Observation                         | Result    |
| ----------------------------------- | --------- |
| First visible numbered line         | 1 - 44    |
| Result after `Space`                | 45 - 88   |
| Result after `b`                    | 1 - 44    |
| Final line number after `G`         | 166 - 209 |
| First `/archive` match              | 193 - 209 |
| Next match after `n`                | none      |
| Did `q` return to the shell prompt? | yes       |

## 4 — Verify and explain

After leaving `less`, run:

```bash
pwd
```

```bash
ls -l sessions/2026-10-31.md
```

Record commands and output:

```text
raffi@Raffis-Mac linux % pwd
/Users/raffi/Learning/topics/linux
raffi@Raffis-Mac linux % ls -l sessions/2026-10-31.md
-rw-r--r--@ 1 raffi  staff  12325 31 Oct 21:06 sessions/2026-10-31.md
```

In two or three sentences, explain when `cat` is convenient and why `less` is
usually a better first choice for a 50,000-line log.

> cat is good when the content is not too long, while less is better when the content is too long

Stop and tell the tutor when the worksheet is ready.

## 5 — Focused recheck (2026-11-02)

Your movement through the file was successful. Keep the original answers above
unchanged; they are useful evidence of your first prediction and observation.

### A. Reading versus modifying

Compare the `ls -l` evidence recorded before and after `less`: the size remained
12325 bytes and the displayed modification time remained `31 Oct 21:06`.

In your own words, answer both questions:

1. Did `Space`, `b`, `G`, `g`, `/archive`, or `n` modify the stored file?
2. What did those keys change instead?

> 1. No
>  2. idk what it modified actually, maybe it detects modified because we viewed the file

Tutor clarification: the keys changed only `less`'s temporary viewing state—the
screen position and selected search match. Viewing did not mark or modify the
stored file.

### B. Search precisely

Open the same file again:

```bash
less -N /Users/raffi/Learning/topics/linux/sessions/2026-10-31.md
```

Press `g`, search with `/archive` followed by `Enter`, and look for the
highlighted match. Record its exact line number and a short text fragment. Then
press `n` once and record the exact line number and fragment of that next match.
Do not record the whole visible screen range.

| Search observation | Exact result |
| --- | --- |
| First match after `/archive` | 16 — Introduced archives versus compression. |
| Next match after `n` | 18 — in the prepared archive fixture; archive creation/extraction is not assessed. |

Press `q`, save this worksheet, and tell the tutor when the recheck is ready.

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
TODO
```

## 2 — Predict the interaction

Before opening the pager, predict:

| Question | Prediction |
| --- | --- |
| Will `less` print all 209 lines and immediately return to the shell prompt? | TODO |
| Will the navigation keys below change the file's stored contents? | TODO |
| What key do you expect to use when you want to leave `less`? | TODO or `I don't know` |

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

| Observation | Result |
| --- | --- |
| First visible numbered line | TODO |
| Result after `Space` | TODO |
| Result after `b` | TODO |
| Final line number after `G` | TODO |
| First `/archive` match | TODO |
| Next match after `n` | TODO |
| Did `q` return to the shell prompt? | TODO |

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
TODO
```

In two or three sentences, explain when `cat` is convenient and why `less` is
usually a better first choice for a 50,000-line log.

> TODO

Stop and tell the tutor when the worksheet is ready.

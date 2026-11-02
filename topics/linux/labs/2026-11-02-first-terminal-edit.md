# Lab — Make and verify a terminal edit

Date: 2026-11-02

## Editor on this machine

On this Mac, `/usr/bin/nano` is a symbolic link to the Pico editor. The screen
therefore identifies itself as Pico. Ubuntu normally provides GNU nano instead,
but the basic controls used here are similar.

At the bottom of the editor, `^` means the `Ctrl` key. For example, `^O` means
press `Ctrl-O`; do not type a literal caret character.

This lab edits only a disposable fixture under `labs/editor-practice/`.

## 1 — Inspect and predict

Run:

```bash
cat labs/editor-practice/service-note.txt
```

Record the command and output:

```text
Service: web-demo
Owner: TODO
Status: draft
```

Before editing, predict:

| Question                                                        | Prediction     |
| --------------------------------------------------------------- | -------------- |
| Does merely opening the editor change the stored file?          | no             |
| Where do typed changes exist before you save them?              | `I don't know` |
| Which control shown below writes the edited buffer to the file? | CTRL + O       |
| Which control exits the editor?                                 | CTRL + X       |

## 2 — Open and edit

Open the fixture with one physical shell command:

```bash
nano labs/editor-practice/service-note.txt
```

Inside the editor:

1. Press `Ctrl-W`, type `TODO`, and press `Enter` to search for the placeholder.
2. Use the arrow keys and Backspace/Delete as needed.
3. Change `Owner: TODO` to `Owner: Raffi`.
4. Change `Status: draft` to `Status: ready`.
5. Add this exact fourth line:

   ```text
   Checked: 2026-11-02
   ```

Do not change the first line.

## 3 — Save and exit

1. Press `Ctrl-O` (`WriteOut`).
2. When the editor asks for the filename, keep the displayed pathname and press
   `Enter` to confirm it.
3. Press `Ctrl-X` to exit.

Record anything you noticed about the search, save prompt, or exit:

> TODO

## 4 — Verify from the shell

Run these commands separately:

```bash
cat labs/editor-practice/service-note.txt
```

```bash
nl -ba labs/editor-practice/service-note.txt
```

Record both commands and complete output:

```text
raffi@Raffis-Mac linux % cat labs/editor-practice/service-note.txt
Service: web-demo
Owner: Raffi
Status: ready
Checked: 2026-11-02
raffi@Raffis-Mac linux % nl -ba labs/editor-practice/service-note.txt
     1	Service: web-demo
     2	Owner: Raffi
     3	Status: ready
     4	Checked: 2026-11-02
```

Use the evidence to answer:

1. Were all four requested lines stored exactly?
2. Which output proves the file has four lines with no hidden blank line between
   them?
3. At what step did the editor's temporary changes become stored-file changes?

> 1. yes, evidence:
>    raffi@Raffis-Mac linux % cat labs/editor-practice/service-note.txt
Service: web-demo
Owner: Raffi
Status: ready
Checked: 2026-11-02
> 2.  raffi@Raffis-Mac linux % nl -ba labs/editor-practice/service-note.txt
     1	Service: web-demo
     2	Owner: Raffi
     3	Status: ready
     4	Checked: 2026-11-02
> 3. when we use CTRL-O ?

## 5 — Explain the editing model

Complete this model in your own words:

```text
stored file --open--> editor buffer --CTRL-O action--> updated stored file
                                      |
                                      +--CTRL-X action--> return to shell
```

Then explain the difference between `Ctrl-O` and `Ctrl-X` in one or two
sentences.

> CTRL-O saves the changes in the editor buffer to the stored/actual file while CTRL-x exit the buffer and returns to the shell

Stop and tell the tutor when the worksheet is ready.

## Tutor checkpoint

The learner successfully searched for the placeholder, made all requested
edits, saved, exited, and verified the exact four-line stored result. The
editing model was correct: typed changes first exist in the editor's in-memory
buffer; `Ctrl-O` writes that buffer to the stored path; `Ctrl-X` exits.

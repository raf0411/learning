# Lab — Distinguish discarding from saving an edit

Date: 2026-11-02

This lab uses a disposable fixture. It first demonstrates a safe discarded
change, then tests whether you can save a different edit with less scaffolding.

## 1 — Inspect and predict

Run:

```bash
cat labs/editor-practice/deployment-note.txt
```

Record the command and output:

```text
raffi@Raffis-Mac linux % cat labs/editor-practice/deployment-note.txt
Environment: test
Owner: unassigned
Note: keep this line
```

Predict the stored result if you type a new line in the editor, press `Ctrl-X`,
and answer `N` when asked whether to save the modified buffer:

> it won't safe the changed buffer, the content will remain the same as before

## 2 — Make a change and deliberately discard it

Open the fixture:

```bash
nano labs/editor-practice/deployment-note.txt
```

Add this temporary fourth line:

```text
Temporary: discard me
```

Do not use `Ctrl-O`. Press `Ctrl-X`. When the editor asks whether to save the
modified buffer, press `N` to discard the temporary buffer changes and exit.

The only thing being discarded is the unsaved editor-buffer change in this
disposable exercise; the previously stored three-line file should remain.

Verify with:

```bash
nl -ba labs/editor-practice/deployment-note.txt
```

Record the command and complete output:

```text
raffi@Raffis-Mac linux % nl -ba labs/editor-practice/deployment-note.txt
     1	Environment: test
     2	Owner: unassigned
     3	Note: keep this line
```

Did the prediction match? Explain what happened to the buffer and stored file.

> yes, the added new line didn't get save:
> raffi@Raffis-Mac linux % nl -ba labs/editor-practice/deployment-note.txt
     1	Environment: test
     2	Owner: unassigned
     3	Note: keep this line

## 3 — Independently make a saved edit

Open the same file again. Without a supplied keystroke sequence, make these
changes using the controls already learned:

- Change `Environment: test` to `Environment: production`.
- Change `Owner: unassigned` to `Owner: Raffi`.
- Preserve `Note: keep this line` exactly.
- Do not add blank lines.
- Save the changes and return to the shell.

Record the one shell command used to open the file:

```text
raffi@Raffis-Mac linux % nano labs/editor-practice/deployment-note.txt
```

## 4 — Verify the independent result

Use appropriate learned inspection commands to prove:

- the file contains exactly three lines;
- the environment and owner changed as requested;
- the note was preserved;
- the discarded temporary line is absent.

Write the verification commands and their complete output:

```text
raffi@Raffis-Mac linux % nl -ba labs/editor-practice/deployment-note.txt
     1	Environment: production
     2	Owner: Raffi
     3	Note: keep this line
raffi@Raffis-Mac linux % cat labs/editor-practice/deployment-note.txt
Environment: production
Owner: Raffi
Note: keep this line
```

Explain which editor action made the second set of changes persistent, and why
the first temporary change did not persist.

> the CTRL-O and enter made the changes persistent and the first did not persist because we said N after CTRL-X

Stop and tell the tutor when the worksheet is ready.

## Tutor checkpoint

The learner correctly predicted and verified that answering `N` discarded only
the unsaved buffer change. The learner then independently edited, saved, exited,
and supplied complete `nl -ba` and `cat` evidence for the exact three-line
stored result.

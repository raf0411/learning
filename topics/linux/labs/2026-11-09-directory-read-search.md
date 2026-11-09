# Directory read versus search permission — 2026-11-09

Use the **same Ubuntu terminal** with `find_lab` still set. Record answers here.

Session-end note: this worksheet was not attempted on November 9. When resuming,
confirm that the variable and practice tree still exist. If starting a new
terminal or VM session, re-establish a disposable fixture with the tutor before
running the permission changes; do not assume the old temporary path persists.

## Model

- Directory `r`: list entry names.
- Directory `x`: traverse the directory and access a known entry by name.
- Reading a file also requires appropriate permissions on the file itself.

We will temporarily remove **owner read permission only** from the disposable
`app` directory, keeping its owner execute/search permission. Then restore it.
This does not change file contents or the permission bits of files inside it.

## Inspect before changing

Run these separate commands:

```bash
ls -ld "$find_lab/app"
ls -l "$find_lab/app/current.log"
```

Confirm that you own both, that the directory owner has `rwx`, and that the file
owner has read permission. If the output differs, share it before proceeding.

Paste this baseline:

```text
TODO
```

## Predict

After removing only the directory owner's `r` permission, predict success or
failure for each operation. No written explanation required.

| Operation | Prediction |
|---|---|
| List names inside `app` with `ls` | TODO |
| Read the known file `app/current.log` with `cat` | TODO |

## Run and restore

Run each physical line separately. A failed inspection is part of the experiment;
continue through the restoration commands.

```bash
chmod u-r "$find_lab/app"
ls "$find_lab/app"
cat "$find_lab/app/current.log"; printf 'read-status=%s\n' "$?"
chmod u+r "$find_lab/app"
ls -ld "$find_lab/app"
```

`current.log` was created empty, so successful `cat` may print no file content.
The immediate status distinguishes successful reading (0) from failure.
The final directory listing verifies restoration against your baseline.

Paste the actual commands and output, including restoration:

```text
TODO
```

Tell me when the note is ready. Preserve your predictions even if the results
differ from them.

# Checkpoint — Package, inspect, and restore independently

Date: 2026-11-01

## Assessment scope revision

This worksheet preserves the original xz prompt and the learner's execution
transcript verbatim. During assessment, content inspection established that the
lowercase `-j` commands created, listed, and extracted a valid bzip2-compressed
tar archive; only the `.xz` suffix and the stated algorithm were wrong.

At the learner's request, the completed checkpoint is assessed as a bzip2
archive workflow rather than repeated as xz. The tutor renamed the preserved
artifact from `field-kit-backup.tar.xz` to
`field-kit-backup.tar.bz2` after confirming the destination name was absent.
No archive or recovery data was deleted or recreated.

Assessment consequences:

- create, member-listing, boundary inspection, empty-destination check, and
  extraction are valid independent bzip2 workflow evidence;
- read-only comparison confirmed all three restored files match their sources;
- the learner transcript did not record the requested initial command output or
  post-extraction nested content checks, so evidence recording remains a
  reinforcement point;
- case-sensitive compression-option recall (`-j` for bzip2, `-J` for xz)
  remains scheduled for later retrieval rather than requiring an immediate
  repeat.

## Scenario

A small `field-kit/` project must be packaged as an xz-compressed tar archive,
inspected before extraction, and restored into a fresh recovery directory.

Work only inside:

```text
/Users/raffi/Learning/topics/linux/labs/archive-checkpoint
```

The prepared source contains nested files and a protected neighboring file.
Determine the exact starting structure through inspection rather than assuming
it from this worksheet.

## Required final state

- Source `field-kit/` remains present and unchanged.
- `keep.txt` remains present and unchanged.
- A new xz-compressed archive named `field-kit-backup.tar.xz` exists beside the
  source.
- The archive's stored paths have been listed before extraction.
- Every stored path is beneath the top-level `field-kit/` entry.
- A new directory named `recovery/` contains the restored `field-kit/` tree.
- The restored files have the same visible contents as the source files.
- The shell finishes in the checkpoint root.

Do not delete, rename, or overwrite anything. If the proposed archive or
recovery destination already exists during initial inspection, stop and tell
the tutor.

## Rules

- No tar command is supplied in this checkpoint.
- You may use installed documentation such as `tar --help` or `man tar`.
- Record any documentation command you consult.
- Write the complete plan before performing the archive creation or extraction.
- Use one physical command line per submission.
- A successful command with no output must still appear in the transcript.
- Inspect the archive members before extraction.
- Recheck the working directory and empty destination immediately before
  extraction.
- Stop on an unexpected error instead of improvising several commands.

## 1 — Inspect and describe the starting state

Choose commands that establish:

- the current working directory;
- every prepared directory and file within the checkpoint boundary;
- the visible contents of all source files and `keep.txt`;
- absence of both proposed new names.

Record commands and output:

```text
pwd
ls -la
cat field-kit/README.txt
cat field-kit/data/hosts.txt
cat field-kit/config/app.conf
cat keep.txt
ls -la field-kit-backup.tar.xz recovery 
```

In one sentence, state whether it is safe to proceed and cite the relevant
inspection evidence.

> yes, evidence: 
> raffi@Raffis-Mac archive-checkpoint % ls -la field-kit-backup.tar.xz recovery
ls: field-kit-backup.tar.xz: No such file or directory
ls: recovery: No such file or directory
raffi@Raffis-Mac archive-checkpoint %

## 2 — Write the complete plan

Plan a sequence that:

1. creates the requested xz-compressed archive from `field-kit/`;
2. proves the source and protected neighbor remain;
3. lists the stored archive paths without extracting;
4. creates `recovery/`;
5. proves `recovery/` is empty;
6. rechecks the shell's working directory immediately before extraction;
7. extracts into `recovery/`;
8. verifies the complete restored structure and all restored contents;
9. verifies the original source, archive, and protected neighbor still exist;
10. proves the shell finishes in the checkpoint root.

Write exact commands in execution order. Add rows if genuinely necessary; do
not add unrelated commands.

| Step          | Purpose                                                                    | Planned command                              |
| ------------- | -------------------------------------------------------------------------- | -------------------------------------------- |
| 1             | to create the xz compressed archive                                        | tar -cjf field-kit-backup.tar.xz field-kit   |
| 2             | to prove the source and protected neighbor remain                          | ls -la field-kit keep.txt                    |
| 3             | to lists whats inside the compressed archive                               | tar -tjf field-kit-backup.tar.xz             |
| 4             | creating a directory called recovery                                       | mkdir recovery                               |
| 5             | to check if recovery is empty                                              | ls -la recovery                              |
| 6             | to confirm our shell working directory                                     | pwd                                          |
| 7             | to extract the compressed archive into recovery                            | tar -xjf field-kit-backup.tar.xz -C recovery |
| 8             | to check if recovery has the uncompressed archive field-kit                | ls -la recovery                              |
| 9             | to check the original source, archive, and protected neighbor still exists | ls -la                                       |
| 10            | to proves the shell finishes in the checkpoint root                        | pwd                                          |
| 11, if needed | TODO                                                                       | TODO                                         |
| 12, if needed | TODO                                                                       | TODO                                         |

Before execution, check the planned archive name, source operand, compression
option, destination, and every relative path against the recorded `pwd`.

## 3 — Execute and record evidence

Run the plan one command at a time. After listing the archive members, pause
long enough to confirm that every member is under `field-kit/`. Extract only
if that check succeeds and `recovery/` is still empty.

Record every command and its output:

```text
raffi@Raffis-Mac archive-checkpoint % tar -cjf field-kit-backup.tar.xz field-kit
raffi@Raffis-Mac archive-checkpoint % ls -la field-kit keep.txt
-rw-r--r--@ 1 raffi  staff  19  1 Nov 19:57 keep.txt

field-kit:
total 8
drwxr-xr-x@ 5 raffi  staff  160  1 Nov 19:57 .
drwxr-xr-x@ 5 raffi  staff  160  1 Nov 20:15 ..
drwxr-xr-x@ 3 raffi  staff   96  1 Nov 19:57 config
drwxr-xr-x@ 3 raffi  staff   96  1 Nov 19:57 data
-rw-r--r--@ 1 raffi  staff   63  1 Nov 19:57 README.txt
raffi@Raffis-Mac archive-checkpoint % tar -tjf field-kit-backup.tar.xz
field-kit/
field-kit/config/
field-kit/README.txt
field-kit/data/
field-kit/data/hosts.txt
field-kit/config/app.conf
raffi@Raffis-Mac archive-checkpoint % mkdir recovery
raffi@Raffis-Mac archive-checkpoint % ls -la recovery
total 0
drwxr-xr-x@ 2 raffi  staff   64  1 Nov 20:15 .
drwxr-xr-x@ 6 raffi  staff  192  1 Nov 20:15 ..
raffi@Raffis-Mac archive-checkpoint % pwd
/Users/raffi/Learning/topics/linux/labs/archive-checkpoint
raffi@Raffis-Mac archive-checkpoint % tar -xjf field-kit-backup.tar.xz -C recovery
raffi@Raffis-Mac archive-checkpoint % ls -la recovery
total 0
drwxr-xr-x@ 3 raffi  staff   96  1 Nov 20:15 .
drwxr-xr-x@ 6 raffi  staff  192  1 Nov 20:15 ..
drwxr-xr-x@ 5 raffi  staff  160  1 Nov 19:57 field-kit
raffi@Raffis-Mac archive-checkpoint % ls -la
total 16
drwxr-xr-x@  6 raffi  staff   192  1 Nov 20:15 .
drwxr-xr-x@ 39 raffi  staff  1248  1 Nov 19:57 ..
drwxr-xr-x@  5 raffi  staff   160  1 Nov 19:57 field-kit
-rw-r--r--@  1 raffi  staff   905  1 Nov 20:15 field-kit-backup.tar.xz
-rw-r--r--@  1 raffi  staff    19  1 Nov 19:57 keep.txt
drwxr-xr-x@  3 raffi  staff    96  1 Nov 20:15 recovery
raffi@Raffis-Mac archive-checkpoint % pwd
/Users/raffi/Learning/topics/linux/labs/archive-checkpoint
```

## 4 — Explain and self-assess

Answer concisely:

1. Which command created the archive, and what did each option and operand do?
2. Which evidence showed the archive was safe to extract into `recovery/`?
3. Which evidence showed restoration succeeded without changing the source or
   `keep.txt`?
4. If you used documentation or corrected your plan before execution, what did
   you consult or change?

> 1. raffi@Raffis-Mac archive-checkpoint % tar -cjf field-kit-backup.tar.xz field-kit, -c creates, -j for xz compression, -f to tell the archive name
> 2. raffi@Raffis-Mac archive-checkpoint % ls -la recovery
total 0
drwxr-xr-x@ 2 raffi  staff   64  1 Nov 20:15 .
drwxr-xr-x@ 6 raffi  staff  192  1 Nov 20:15 ..
3. raffi@Raffis-Mac archive-checkpoint % ls -la
total 16
drwxr-xr-x@  6 raffi  staff   192  1 Nov 20:15 .
drwxr-xr-x@ 39 raffi  staff  1248  1 Nov 19:57 ..
drwxr-xr-x@  5 raffi  staff   160  1 Nov 19:57 field-kit
-rw-r--r--@  1 raffi  staff   905  1 Nov 20:15 field-kit-backup.tar.xz
-rw-r--r--@  1 raffi  staff    19  1 Nov 19:57 keep.txt
drwxr-xr-x@  3 raffi  staff    96  1 Nov 20:15 recovery
4. i didn't use the documentation or corrected my plan I swear

Stop and tell the tutor when the worksheet is ready. Preserve the complete
checkpoint state for review.

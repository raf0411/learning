# Phase 2 Checkpoint — Safe File Organization

Date: 2026-10-30

## Purpose

Reorganize an unfamiliar disposable fixture by selecting appropriate commands,
resolving paths from evidence, protecting existing content, and verifying every
material result without step-by-step command prompts.

This is an assessment. Write your command plan before executing it. You may use
commands already practiced, including `pwd`, `ls`, `cat`, `printf`, `mkdir`,
`touch`, `cp`, `mv`, `rm`, and `rmdir`, with appropriate learned options.

## Safety boundary

Work only beneath:

```text
/Users/raffi/Learning/topics/linux/labs/phase2-checkpoint
```

The fixture is disposable except for this assessment rule: `preserve` and
everything beneath it must remain unchanged.

- Do not use `-f`.
- Do not use a wildcard with recursive removal.
- Preview any pattern before using it with a filesystem-changing command.
- Stop if `pwd` or the observed fixture differs materially from this worksheet.

## Part 1 — Orient and inspect

Move to the checkpoint root. Record the command and `pwd` output:

```text
raffi@Raffis-Mac phase2-checkpoint % pwd
/Users/raffi/Learning/topics/linux/labs/phase2-checkpoint
```

Inspect enough of the fixture to identify every starting directory and file,
including nested paths. Inspect the contents of these files because later
operations must preserve or move their distinct content:

- `intake/alpha.txt`
- `archive/alpha.txt`
- `intake/release.txt`
- `review/release.txt`
- `preserve/marker.txt`

Record all inspection commands and complete output:

```text
raffi@Raffis-Mac phase2-checkpoint % ls -la
total 0
drwxr-xr-x@  8 raffi  staff  256 30 Oct 19:01 .
drwxr-xr-x@ 27 raffi  staff  864 30 Oct 19:01 ..
drwxr-xr-x@  3 raffi  staff   96 30 Oct 19:01 archive
drwxr-xr-x@  4 raffi  staff  128 30 Oct 19:01 cleanup
drwxr-xr-x@  8 raffi  staff  256 30 Oct 19:01 intake
drwxr-xr-x@  3 raffi  staff   96 30 Oct 19:01 preserve
drwxr-xr-x@  3 raffi  staff   96 30 Oct 19:01 projects
drwxr-xr-x@  3 raffi  staff   96 30 Oct 19:01 review
raffi@Raffis-Mac phase2-checkpoint % ls -la archive
total 8
drwxr-xr-x@ 3 raffi  staff   96 30 Oct 19:01 .
drwxr-xr-x@ 8 raffi  staff  256 30 Oct 19:01 ..
-rw-r--r--@ 1 raffi  staff   23 30 Oct 19:01 alpha.txt
raffi@Raffis-Mac phase2-checkpoint % ls -la cleanup
total 0
drwxr-xr-x@ 4 raffi  staff  128 30 Oct 19:01 .
drwxr-xr-x@ 8 raffi  staff  256 30 Oct 19:01 ..
drwxr-xr-x@ 2 raffi  staff   64 30 Oct 19:01 empty
drwxr-xr-x@ 3 raffi  staff   96 30 Oct 19:01 nonempty
raffi@Raffis-Mac phase2-checkpoint % ls -la intake
total 48
drwxr-xr-x@ 8 raffi  staff  256 30 Oct 19:01 .
drwxr-xr-x@ 8 raffi  staff  256 30 Oct 19:01 ..
-rw-r--r--@ 1 raffi  staff   18 30 Oct 19:01 alpha.txt
-rw-r--r--@ 1 raffi  staff   11 30 Oct 19:01 beta.txt
-rw-r--r--@ 1 raffi  staff   16 30 Oct 19:01 draft.tmp
-rw-r--r--@ 1 raffi  staff   24 30 Oct 19:01 old.tmp
-rw-r--r--@ 1 raffi  staff   14 30 Oct 19:01 photo.png
-rw-r--r--@ 1 raffi  staff   18 30 Oct 19:01 release.txt
raffi@Raffis-Mac phase2-checkpoint % ls -la preserve
total 8
drwxr-xr-x@ 3 raffi  staff   96 30 Oct 19:01 .
drwxr-xr-x@ 8 raffi  staff  256 30 Oct 19:01 ..
-rw-r--r--@ 1 raffi  staff   25 30 Oct 19:01 marker.txt
raffi@Raffis-Mac phase2-checkpoint % ls -la projects
total 0
drwxr-xr-x@ 3 raffi  staff   96 30 Oct 19:01 .
drwxr-xr-x@ 8 raffi  staff  256 30 Oct 19:01 ..
drwxr-xr-x@ 4 raffi  staff  128 30 Oct 19:01 demo
raffi@Raffis-Mac phase2-checkpoint % ls -la review
total 8
drwxr-xr-x@ 3 raffi  staff   96 30 Oct 19:01 .
drwxr-xr-x@ 8 raffi  staff  256 30 Oct 19:01 ..
-rw-r--r--@ 1 raffi  staff   17 30 Oct 19:01 release.txt
raffi@Raffis-Mac phase2-checkpoint %
```

Summarize the observed starting tree. Include nested entries:

```text
phase2-checkpoint/
|
___ archive
    |
    --- alpha.txt
--- cleanup
    |
    --- empty
    |
    --- nonempty
        |
        --- obsolete.txt
|
--- intake
    |
    --- alpha.txt
    |
    --- beta.txt
	|
    --- draft.tmp
    |
    --- old.tmp
    |
    --- phoot.png
    |
    --- release.txt
--- preserve
	|
    --- marker.txt
--- projects
	|
    --- demo
	    |
	    --- assets
		    |
		    --- logo.png
	    |
	    --- README.txt
--- review
	|
    --- release.txt
```

## Part 2 — Write the complete plan before executing

For each goal, write exact command(s), the predicted result, and the evidence
you will collect afterward. Do not execute the plan until every row is complete.

| Goal                                                                                                                                                 | Exact planned command(s)                                                 | Predicted result                                                                                                     | Planned verification                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Create `backups` and the nested directory `review/notes/2026`                                                                                        | mkdir backups<br>mkdir -p review/notes/2026                              | backups created<br><br>review/notes/2026 created                                                                     | ls -la backups<br>ls -la review/notes/2026            |
| Create an empty placeholder at `review/notes/2026/todo.txt`                                                                                          | touch review/notes/2026/todo.txt                                         | todo.txt created inside review/notes/2026/                                                                           | ls -la review/notes/2026/                             |
| Copy the entire `projects/demo` tree into existing `backups`, producing `backups/demo` while preserving the source                                   | cp -r projects/demo backups/demo                                         | copied demo will be in backups/demo                                                                                  | ls -la projects/demo<br>ls -la backups/demo           |
| Move `intake/beta.txt` to the new exact path `review/notes/final.txt`                                                                                | mv intake/beta.txt review/notes/final.txt                                | original intake/beta.txt will be gone and moved to `review/notes/final.txt`                                          | ls -la intake/beta.txt<br>ls `review/notes/final.txt` |
| Interactively attempt to copy `intake/alpha.txt` over existing `archive/alpha.txt`, but decline replacement so both retain their original content    | cp -i intake/alpha.txt archive/alpha.txt<br>n                            | both alpha.txt will retain their original content                                                                    | cat intake/alpha.txt<br>cat archive/alpha.txt         |
| Interactively attempt to move `intake/release.txt` over existing `review/release.txt`, but decline replacement so both retain their original content | mv -i intake/release.txt review/release.txt<br>n                         | intake/release.txt original source will remain and review/release.txt content still remain                           | cat intake/release.txt<br>cat review/release.txt      |
| With one unquoted pattern, preview the `.tmp` files in `intake`; then interactively preserve `draft.tmp` and remove `old.tmp`                        | `printf 'target: <%s>\n' intake/*.tmp`<br>`rm -i intake/*.tmp`<br>n<br>y | the preview will show every .tmp files available inside intake/<br><br>rm will remove old.tmp but preserve draft.tmp | check the removed files with `ls -la intake/*.tmp`    |
| Remove `cleanup/empty` using the command whose normal purpose is removing empty directories                                                          | rmdir cleanup/empty                                                      | cleanup/empty will be gone                                                                                           | ls -la cleanup/empty                                  |
| After inspecting its exact boundary, recursively remove `cleanup/nonempty` and its contents without a wildcard or `-f`                               | ls -la cleanup<br>rm -R cleanup/nonempty                                 | cleanup/nonempty will be gone                                                                                        | ls -la cleanup/nonempty                               |

Before executing, answer:

1. What exact absolute path will be the recursive-removal root for the relative
   operand in your plan?

   > /Users/raffi/Learning/topics/linux/labs/phase2-checkpoint

2. Which paths are siblings of that root and therefore outside its recursive
   boundary?

   > copy-practice glob-practice ls-practice mkdir-practice move-practice navigation-practice recursive-removal-practice removal-practice touch-practice 
   > 
   > and all the other md files from the labs

3. Which planned commands can replace or remove existing content, and what
   safety checks constrain each one?

   > mv intake/beta.txt review/notes/final.txt

## Part 3 — Execute and record evidence

Execute your plan in goal order. Record every command, every interactive prompt
and response, and all verification output. If actual evidence differs from your
prediction, stop before the next filesystem-changing command and explain the
difference.

### 3A. Directories and placeholder

```text
raffi@Raffis-Mac phase2-checkpoint % mkdir backups
raffi@Raffis-Mac phase2-checkpoint % mkdir -p review/notes/2026
raffi@Raffis-Mac phase2-checkpoint % ls -la backups
total 0
drwxr-xr-x@ 2 raffi  staff   64 30 Oct 19:57 .
drwxr-xr-x@ 9 raffi  staff  288 30 Oct 19:57 ..
raffi@Raffis-Mac phase2-checkpoint % ls -la review/notes/2026
total 0
drwxr-xr-x@ 2 raffi  staff  64 30 Oct 19:58 .
drwxr-xr-x@ 3 raffi  staff  96 30 Oct 19:58 ..
raffi@Raffis-Mac phase2-checkpoint % touch review/notes/2026/todo.txt
raffi@Raffis-Mac phase2-checkpoint % ls -la review/notes/2026/
total 0
drwxr-xr-x@ 3 raffi  staff  96 30 Oct 19:59 .
drwxr-xr-x@ 3 raffi  staff  96 30 Oct 19:58 ..
-rw-r--r--@ 1 raffi  staff   0 30 Oct 19:59 todo.txt
```

### 3B. Recursive copy and file move

```text
raffi@Raffis-Mac phase2-checkpoint % cp -r projects/demo backups/demo
raffi@Raffis-Mac phase2-checkpoint % ls -la projects/demo
total 8
drwxr-xr-x@ 4 raffi  staff  128 30 Oct 19:01 .
drwxr-xr-x@ 3 raffi  staff   96 30 Oct 19:01 ..
drwxr-xr-x@ 3 raffi  staff   96 30 Oct 19:01 assets
-rw-r--r--@ 1 raffi  staff   20 30 Oct 19:01 README.txt
raffi@Raffis-Mac phase2-checkpoint %
raffi@Raffis-Mac phase2-checkpoint % ls -la backups/demo
total 8
drwxr-xr-x@ 4 raffi  staff  128 30 Oct 20:19 .
drwxr-xr-x@ 3 raffi  staff   96 30 Oct 20:19 ..
drwxr-xr-x@ 3 raffi  staff   96 30 Oct 20:19 assets
-rw-r--r--@ 1 raffi  staff   20 30 Oct 20:19 README.txt
raffi@Raffis-Mac phase2-checkpoint % mv intake/beta.txt review/notes/final.txt
raffi@Raffis-Mac phase2-checkpoint % ls -la intake/beta.txt
ls: intake/beta.txt: No such file or directory
raffi@Raffis-Mac phase2-checkpoint % ls review/notes/final.txt
review/notes/final.txt
raffi@Raffis-Mac phase2-checkpoint %
```

### 3C. Declined copy replacement

```text
raffi@Raffis-Mac phase2-checkpoint % cp -i intake/alpha.txt archive/alpha.txt
overwrite archive/alpha.txt? (y/n [n]) n
not overwritten
raffi@Raffis-Mac phase2-checkpoint % cat intake/alpha.txt
NEW ALPHA CONTENT
raffi@Raffis-Mac phase2-checkpoint % cat archive/alpha.txt
ARCHIVED ALPHA CONTENT
raffi@Raffis-Mac phase2-checkpoint %
```

### 3D. Declined move replacement

```text
raffi@Raffis-Mac phase2-checkpoint % mv -i intake/release.txt review/release.txt
overwrite review/release.txt? (y/n [n]) n
not overwritten
raffi@Raffis-Mac phase2-checkpoint % cat intake/release.txt
CANDIDATE RELEASE
raffi@Raffis-Mac phase2-checkpoint % cat review/release.txt
APPROVED RELEASE
raffi@Raffis-Mac phase2-checkpoint %
```

### 3E. Pattern preview and per-path removal

Record the preview first. Then record the removal command, both prompts, both
responses, and verification.

```text
raffi@Raffis-Mac phase2-checkpoint % printf 'target: <%s>\n' intake/*.tmp
target: <intake/draft.tmp>
target: <intake/old.tmp>
raffi@Raffis-Mac phase2-checkpoint % rm -i intake/*.tmp
remove intake/draft.tmp? n
remove intake/old.tmp? y
raffi@Raffis-Mac phase2-checkpoint % ls -la intake/*.tmp
-rw-r--r--@ 1 raffi  staff  16 30 Oct 19:01 intake/draft.tmp
raffi@Raffis-Mac phase2-checkpoint %
```

### 3F. Empty and recursive directory removal

Record the pre-removal inspection, both removal commands, and verification of
the targets and protected neighboring paths.

```text
raffi@Raffis-Mac phase2-checkpoint % rmdir cleanup/empty
raffi@Raffis-Mac phase2-checkpoint % ls -la cleanup/empty
ls: cleanup/empty: No such file or directory
raffi@Raffis-Mac phase2-checkpoint % ls -la cleanup
total 0
drwxr-xr-x@ 3 raffi  staff   96 30 Oct 20:22 .
drwxr-xr-x@ 9 raffi  staff  288 30 Oct 19:57 ..
drwxr-xr-x@ 3 raffi  staff   96 30 Oct 19:01 nonempty
raffi@Raffis-Mac phase2-checkpoint % rm -R cleanup/nonempty
raffi@Raffis-Mac phase2-checkpoint % ls -la cleanup/nonempty
ls: cleanup/nonempty: No such file or directory
raffi@Raffis-Mac phase2-checkpoint %
```

## Part 4 — Final-state proof

Collect evidence for every required outcome. Choose the verification commands
yourself.

| Required final state                                                   | Evidence command and observed result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `backups/demo/README.txt` and `backups/demo/assets/logo.png` exist     | raffi@Raffis-Mac phase2-checkpoint % ls -la backups/demo<br>total 8<br>drwxr-xr-x@ 4 raffi  staff  128 30 Oct 20:19 .<br>drwxr-xr-x@ 3 raffi  staff   96 30 Oct 20:19 ..<br>drwxr-xr-x@ 3 raffi  staff   96 30 Oct 20:19 assets<br>-rw-r--r--@ 1 raffi  staff   20 30 Oct 20:19 README.txt                                                                                                                                                                                                                                                                                                                                      |
| Original `projects/demo` tree still exists                             | raffi@Raffis-Mac phase2-checkpoint % ls -la projects/demo<br>total 8<br>drwxr-xr-x@ 4 raffi  staff  128 30 Oct 19:01 .<br>drwxr-xr-x@ 3 raffi  staff   96 30 Oct 19:01 ..<br>drwxr-xr-x@ 3 raffi  staff   96 30 Oct 19:01 assets<br>-rw-r--r--@ 1 raffi  staff   20 30 Oct 19:01 README.txt<br>raffi@Raffis-Mac phase2-checkpoint %                                                                                                                                                                                                                                                                                             |
| `review/notes/2026/todo.txt` exists and is empty                       | raffi@Raffis-Mac phase2-checkpoint % ls -la review/notes/2026/todo.txt<br>-rw-r--r--@ 1 raffi  staff  0 30 Oct 19:59 review/notes/2026/todo.txt<br>raffi@Raffis-Mac phase2-checkpoint % cat review/notes/2026/todo.txt<br>raffi@Raffis-Mac phase2-checkpoint %                                                                                                                                                                                                                                                                                                                                                                  |
| `review/notes/final.txt` contains the former `intake/beta.txt` content | raffi@Raffis-Mac phase2-checkpoint % cat review/notes/final.txt<br>BETA NOTES                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `intake/beta.txt` no longer exists                                     | raffi@Raffis-Mac phase2-checkpoint % ls -la intake/beta.txt<br>ls: intake/beta.txt: No such file or directory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Both alpha files retain their different original contents              | raffi@Raffis-Mac phase2-checkpoint % cp -i intake/alpha.txt archive/alpha.txt<br>overwrite archive/alpha.txt? (y/n [n]) n<br>not overwritten<br>raffi@Raffis-Mac phase2-checkpoint % cat intake/alpha.txt<br>NEW ALPHA CONTENT<br>raffi@Raffis-Mac phase2-checkpoint % cat archive/alpha.txt<br>ARCHIVED ALPHA CONTENT<br>raffi@Raffis-Mac phase2-checkpoint %                                                                                                                                                                                                                                                                  |
| Both release files retain their different original contents            | raffi@Raffis-Mac phase2-checkpoint % mv -i intake/release.txt review/release.txt<br>overwrite review/release.txt? (y/n [n]) n<br>not overwritten<br>raffi@Raffis-Mac phase2-checkpoint % cat intake/release.txt<br>CANDIDATE RELEASE<br>raffi@Raffis-Mac phase2-checkpoint % cat review/release.txt<br>APPROVED RELEASE<br>raffi@Raffis-Mac phase2-checkpoint %                                                                                                                                                                                                                                                                 |
| `intake/draft.tmp` remains and `intake/old.tmp` is absent              | raffi@Raffis-Mac phase2-checkpoint % printf 'target: <%s>\n' intake/*.tmp<br>target: <intake/draft.tmp><br>target: <intake/old.tmp><br>raffi@Raffis-Mac phase2-checkpoint % rm -i intake/*.tmp<br>remove intake/draft.tmp? n<br>remove intake/old.tmp? y<br>raffi@Raffis-Mac phase2-checkpoint % ls -la intake/*.tmp<br>-rw-r--r--@ 1 raffi  staff  16 30 Oct 19:01 intake/draft.tmp<br>raffi@Raffis-Mac phase2-checkpoint %                                                                                                                                                                                                    |
| Both `cleanup/empty` and `cleanup/nonempty` are absent                 | raffi@Raffis-Mac phase2-checkpoint % rmdir cleanup/empty<br>raffi@Raffis-Mac phase2-checkpoint % ls -la cleanup/empty<br>ls: cleanup/empty: No such file or directory<br>raffi@Raffis-Mac phase2-checkpoint % ls -la cleanup<br>total 0<br>drwxr-xr-x@ 3 raffi  staff   96 30 Oct 20:22 .<br>drwxr-xr-x@ 9 raffi  staff  288 30 Oct 19:57 ..<br>drwxr-xr-x@ 3 raffi  staff   96 30 Oct 19:01 nonempty<br>raffi@Raffis-Mac phase2-checkpoint % rm -R cleanup/nonempty<br>raffi@Raffis-Mac phase2-checkpoint % ls -la cleanup/nonempty<br>ls: cleanup/nonempty: No such file or directory<br>raffi@Raffis-Mac phase2-checkpoint % |
| `preserve/marker.txt` still contains `DO NOT REMOVE OR REPLACE`        | raffi@Raffis-Mac phase2-checkpoint % cat preserve/marker.txt<br>DO NOT REMOVE OR REPLACE                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Final working directory is still the checkpoint root                   | raffi@Raffis-Mac phase2-checkpoint % pwd<br>/Users/raffi/Learning/topics/linux/labs/phase2-checkpoint                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## Part 5 — Explain the decisions

1. For the project copy, why did the result become `backups/demo` rather than
   `backups/projects/demo`?

   > because we are copying the demo inside project not the whole project/demo path

2. In the `.tmp` operation, which component selected the pathname arguments,
   and what did the interactive option change?

   >  `intake/*.tmp` and the interactive option changes the tmp files deleted

3. Connect each `.tmp` prompt response to its specific final path state.

   > intake/draft.tmp

4. Why did the declined copy leave its source path present? Why did the
   declined move also leave its source path present?

   > the declined copy leave its source path present because not only we declined it, because cp will also retain the source path, mv leave its source path present because we declined it but it will removed the source if we accept it

5. What made the recursive removal stay inside `cleanup/nonempty`?

   > i dont know what this mean, it removes because we use rm -R cleanup/nonempty

6. Which commands changed the shell's working directory, and which merely
   changed filesystem entries beneath it?

   > cd changes shell working directory, 
   >  which merely changed filesystem entries beneath it: mv, cp, rm, rmdir

Stop here and tell the tutor when the checkpoint is ready.

---

## Correction pass — boundary, evidence, and command roles

Do not repeat any filesystem-changing operation. Use only reasoning from the
recorded transcript and the read-only checks requested below.

### A. Resolve the recursive boundary precisely

The recorded command was:

```bash
rm -R cleanup/nonempty
```

Use this model:

```text
resolved removal root = recorded working directory + relative pathname operand
```

Complete the trace:

```text
Recorded working directory: /Users/raffi/Learning/topics/linux/labs/phase2-checkpoint
Relative pathname operand: cleanup/nonempty
Resolved absolute removal root: /Users/raffi/Learning/topics/linux/labs/phase2-checkpoint/cleanup/nonempty
```

Classify each path relative to that resolved root:

| Path                            | Root itself, descendant, or outside boundary? |
| ------------------------------- | --------------------------------------------- |
| `cleanup/nonempty`              | root itself                                   |
| `cleanup/nonempty/obsolete.txt` | descendant                                    |
| `cleanup/empty`                 | root itself                                   |
| `preserve/marker.txt`           | root itself                                   |
| the checkpoint root itself      | root itself                                   |

Complete the explanation:

> `-R` recursively processed rm. It did not independently select `*.tmp`.

### B. Identify the missing pre-removal evidence

The transcript shows `ls -la cleanup` before recursive removal. Did that output
enumerate the contents of `cleanup/nonempty`, or only show that the child
directory existed?

>  only show that the child directory existed

What exact read-only command should have been run before removal to prove that
`obsolete.txt` was inside the recursive boundary?

> ls -la cleanup/nonempty/obsolete.txt

Can that missing observation be recovered now that `cleanup/nonempty` is gone?
Distinguish what the final absence error proves from what it cannot prove:

> idk what u mean sorry

### C. Supply direct nested-copy evidence

Run these read-only commands separately:

```bash
ls -la backups/demo/assets
```

```bash
ls -la projects/demo/assets
```

Record both commands and their complete output:

```text
TODO
```

What does the first output prove? What does the second output prove?

> raffi@Raffis-Mac phase2-checkpoint % ls -la backups/demo/assets
total 8
drwxr-xr-x@ 3 raffi  staff   96 30 Oct 20:19 .
drwxr-xr-x@ 4 raffi  staff  128 30 Oct 20:19 ..
-rw-r--r--@ 1 raffi  staff   13 30 Oct 20:19 logo.png
raffi@Raffis-Mac phase2-checkpoint % ls -la projects/demo/assets
total 8
drwxr-xr-x@ 3 raffi  staff   96 30 Oct 19:01 .
drwxr-xr-x@ 4 raffi  staff  128 30 Oct 19:01 ..
-rw-r--r--@ 1 raffi  staff   13 30 Oct 19:01 logo.png
raffi@Raffis-Mac phase2-checkpoint %

### D. Trace pattern selection and interaction

Complete the stages using the recorded preview and prompts:

```text
Typed command: rm -i intake/*.tmp

Shell stage
  Component performing pathname expansion: intake/*.tmp
  Pathname arguments produced: draft.tmp old.tmp

rm stage
  What `-i` changed: rm
  `n` response belonged to: draft.tmp
  Final state of that path: intake/draft.tmp
  `y` response belonged to: old.tmp
  Final state of that path: intake/old.tmp
```

### E. Inventory changing commands and their safeguards

Complete the table for the commands actually used. Focus on what each command
could change and the evidence or safeguard that bounded it.

| Command or command family | What it changed or could change | Safeguard or verification used                     |
| ------------------------- | ------------------------------- | -------------------------------------------------- |
| `mkdir`                   | filesystem                      | cannot make directory nested that hasnt exists yet |
| `touch`                   | file                            | idk                                                |
| recursive `cp`            | filesystem                      | none                                               |
| non-interactive `mv`      | filesystem                      | none                                               |
| `cp -i`                   | filesystem                      | asks to confirm copying                            |
| `mv -i`                   | filesystem                      | asks to confirm moving                             |
| `rm -i`                   | filesystem                      | asks to confirm removing                           |
| `rmdir`                   | filesystem                      | cannot remove not empty directories                |
| `rm -R`                   | filesystem                      | none                                               |

Finally, classify all commands used in the checkpoint:

```text
Changed the shell's working directory: cd

Changed filesystem entries without moving the shell: cp mkdir mv rm rmdir

Observed or printed information without changing filesystem entries: pwd ls cat printf
```

Stop here and tell the tutor when this correction pass is ready.

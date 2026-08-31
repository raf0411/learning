# STATE

Updated: 2026-08-31

## Current stage

Initial probe and roadmap complete. Phase 1 (Linux command line and filesystem)
is active. Guided and unprompted file management, basic text inspection,
searching, and pipeline order have been demonstrated. Command discovery was
added on 2026-08-29: the learner used `type`, `man`, and command-specific help to
resolve the earlier `grep -n` confusion. Separate stdout/stderr overwrite
redirection was repaired on an immediate transfer check. On 2026-08-31, the
learner established that Bash parses a complete command before execution,
completed the clean overwrite/append re-test, identified the streams in a
normal pipeline, and constructed a correct combined `grep`/`head` pipeline with
separate result and diagnostic files. Command boundaries still need spaced
review because long pasted commands were repeatedly split at unsafe points. A
probe and verified dependency plan for filesystem roles, Nano, and archives are
complete; the configuration-versus-log distinction was introduced but not yet
checked.

Last completed session: `sessions/2026-08-31.md`

## Environment and capacity

- Uses macOS Terminal and has an Ubuntu homelab server.
- Can study about 5 hours daily.
- Prefers practical, job-oriented learning.

## Demonstrated knowledge

- Understands the distinction between absolute and relative paths.
- Correctly distinguished `~` from `/home/...` after one correction and
  expanded a deliberately incorrect `~/home/raffi/...` path.
- Can correctly predict the working directory and resulting absolute paths after
  `mkdir practice` and `touch notes.txt` from `/home/raffi`.
- On the Ubuntu host, created `sysadmin-lab-01/notes.txt` from
  `/home/raf_0411` without changing directories, then verified the contents and
  unchanged working directory with `ls` and `pwd`.
- Correctly predicted and then performed a rename with
  `mv sysadmin-lab-01/notes.txt sysadmin-lab-01/server-notes.txt`, explaining
  the source and destination arguments and verifying the new directory state.
- Created `sysadmin-lab-01/backups`, copied `server-notes.txt` into it while
  retaining the original, and verified both locations. The first copy attempt
  accidentally included an extra `cp` operand and produced `cannot stat 'cp'`;
  the learner corrected the command independently. During diagnosis, correctly
  identified that the shell saw one command and that the first `cp` was its
  name, but initially grouped multiple whitespace-separated words into single
  arguments. On immediate re-test, correctly separated all three arguments;
  then correctly assigned source and destination roles in the multi-source form
  of `cp` and predicted that the originals and destination copies remain. A
  trailing slash was added once to a filename in the written answer.
- Used `cp -i` and `mv -i` to detect collisions and decline overwrites.
- Created `sysadmin-lab-01/archive`, moved the top-level file into it, and
  verified that the independent backup remained.
- Used `rm -i` to decline and then accept deletion of the intended archive copy,
  preserving the backup.
- Correctly demonstrated that `rmdir` removes an empty directory but refuses a
  non-empty directory.
- Completed the unprompted file-management transfer check from
  `/home/raf_0411` without using `cd`: created a nested directory, copied a
  backup under a new temporary filename, renamed it, declined an overwrite with
  `cp -i`, and verified both exact paths and the unchanged working directory.
- Used `head -n` and `tail -n` to select an exact number of lines from the
  beginning and end of `/etc/passwd`, explaining the option, its value, and the
  file operand.
- Used `less` to navigate `/etc/passwd`, jump between its beginning and end,
  quit back to the shell, search forward for `bin/bash`, and repeat that search
  with `n`.
- Used `grep` to print all matching lines from `/etc/passwd`, distinguish exact
  case from `-i` case-insensitive matching, and add source line numbers with
  `-n`. Initially treated `grep -n` like `head -n NUMBER`, then correctly
  repaired the command after its arguments and resulting error were diagnosed.
- Used `type` and `type -a` to distinguish an external executable, an alias,
  and a Bash builtin, then selected `help`, `--help`, or `man` appropriately.
- Used `man grep` to discover that `grep -n` prefixes matches with input line
  numbers, demonstrated it live, and parsed a new multi-file `grep` command.
- Used `find` with absolute and relative starting paths, exact names, quoted
  wildcard patterns, and `-type f`. Correctly predicted and demonstrated that
  name-only matching can include a directory named `pretend.txt`, while
  `-type f` excludes it, then removed the temporary directory with `rmdir`.
- Correctly explained that a pipeline passes the left command's standard output
  to the right command's standard input, then demonstrated that reversing
  `head` and `grep` changes the result.
- Demonstrated `>` overwrite and `>>` append behavior with a status file.
- Separated normal `ls` output and an error from the same command into
  `results.txt` with `>` and `errors.txt` with `2>`. Needed the distinction
  retaught with a diagram and simpler examples, then correctly explained the
  two channels and selected `2>>` for appending an error history.
- Re-tested stdout/stderr separation on 2026-08-29. The initial prediction was
  incorrect, but the learner then correctly predicted a new `grep` example and
  verified separate `>` and `2>` destinations with no command output remaining
  on the terminal.
- On 2026-08-30, correctly predicted stdout/stderr destinations, terminal
  visibility, and overwrite versus append behavior for a complete command
  using `>` and `2>>`.
- On 2026-08-31, verified that a parse error from an incomplete `2>>` prevents
  the command, its earlier `>`, and all other redirections from executing.
  Then correctly identified that a later redirection affects only its own
  submitted command, not a command that has already finished.
- Completed a clean stdout-overwrite/stderr-append experiment and verified the
  expected one-line result file and two-line diagnostic history.
- Correctly identified that a normal pipeline carries `ls` stdout into
  `wc -l` while `ls` stderr remains on the terminal.
- Independently constructed the correct stream structure for a pipeline that
  sent `grep` stderr to an append-only error file, piped stdout through
  `head -n 3`, and overwrote a result file. Only the requested filenames were
  given unnecessary `.txt` suffixes; the pipeline and redirections were right.
- Recognizes `touch practice/notes.txt` as a command plus a relative-path
  argument after brief uncertainty about the required separating space.
- Uses `whoami`, `pwd`, `ls`, `neofetch`, `top`, and `htop` at a basic level.
- Can create files/directories and copy/delete files with basic commands.
- Knows the standard `ssh user@address` form.
- Has used `apt` to update and upgrade Ubuntu packages.
- Has used a pipe with `grep` and edits with `nano`.
- Understands the broad purpose of DNS and can use `curl` as an initial web
  check.
- Reports being comfortable with Git; has tried Bash, Docker, databases, SSH
  keys, and firewalls.

## Partial or missing foundations

- Exact nested paths have now been demonstrated in an unprompted transfer check,
  but should still receive later spaced review after earlier mistakes involving
  `~`, a nested backup directory, and a trailing slash on a filename.
- Does not yet understand Unix permission notation and ownership reliably.
- Process, service, `systemd`, and `systemctl` concepts are conflated.
- Does not yet know the core commands for resource, OS, network, and log
  inspection.
- Networking knowledge is early: localhost, private addressing, gateways,
  ports, and troubleshooting need development.
- Little demonstrated experience configuring services or diagnosing homelab
  failures.
- Basic output/error redirection and ordinary pipeline routing have been
  demonstrated but need spaced review. On 2026-08-31, the learner initially
  predicted that a syntactically invalid command would still perform an earlier
  `>` and that a later `2>` could capture an already-finished command's stderr.
  Concrete experiments repaired both predictions. Several long pasted commands
  also acquired real newlines after redirection operators or inside quoted
  paths, so command-entry discipline and visual wrapping versus submitted
  newlines need re-testing in a later scenario. Configuration files,
  virtualization, cloud platforms, web servers, and operational routines still
  need structured practice.
- Recognizes `/etc`, `/var/log`, `/home`, and `/tmp` in common scenarios but
  cannot yet derive their roles from data purpose, ownership, and lifetime.
- Can predict basic `tar -czf` creation and `tar -xzf` extraction outcomes, but
  archive versus compression and safe inspection/restoration are not yet
  demonstrated.
- Selected Nano's reliable `Ctrl+O`, `Enter`, `Ctrl+X` workflow when prompted,
  but buffer-versus-disk state and an actual save have not been demonstrated.

## Teaching approach

Move one concept at a time. Require predictions and terminal work, then test
without hints. Revisit weak concepts through short retrieval questions.

## Next action

Begin the next session with a short retrieval check on configuration versus
logs and one delayed command-boundary question. Then teach directory roles,
Nano's buffer/save states, and archive versus compression through the planned
mock-service snapshot/restore lab before the Phase 1 exit check.

# STATE

Updated: 2026-08-29

## Current stage

Initial probe and roadmap complete. Phase 1 (Linux command line and filesystem)
is active. Guided and unprompted file management, basic text inspection,
searching, and pipeline order have been demonstrated. Command discovery was
added on 2026-08-29: the learner used `type`, `man`, and command-specific help to
resolve the earlier `grep -n` confusion. Separate stdout/stderr overwrite
redirection was repaired on an immediate transfer check. A clean append re-test
and a combined pipeline/redirection lab are next.

Last completed session: `sessions/2026-08-29.md`

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
- Basic output/error redirection has been demonstrated but needs spaced review.
  An append command was split after `>>`, causing an incomplete-command syntax
  error and a second unintended command whose stderr was appended to the lab
  file; the diagnosis was explained but not yet re-tested. Configuration files,
  virtualization, cloud platforms, web servers, and operational routines still
  need structured practice.

## Teaching approach

Move one concept at a time. Require predictions and terminal work, then test
without hints. Revisit weak concepts through short retrieval questions.

## Next action

At the next session, retrieve command boundaries and exact stream routing, then
complete the clean overwrite-then-append re-test. Continue with pipeline stream
behavior and the combined inspection/search/redirection transfer exercise.

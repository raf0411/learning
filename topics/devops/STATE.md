# STATE

Updated: 2026-09-04

## Current stage

Initial probe and roadmap complete. Phase 1 (Linux command line and filesystem)
passed its exit gate on 2026-09-03. The learner completed the written
file-management scenario, then constructed, repaired, ran, verified, and
explained a `grep`/`head` pipeline with stdout overwritten to one report and
stderr appended to another. The opening Phase 2 users-and-permissions lesson is
now complete, including a live least-privilege access repair and a deletion
experiment separating file permissions from parent-directory permissions.
Numeric modes and the restricted service-account lab are now complete. The
learner created a no-login Ubuntu system account, verified separate
configuration-read and log-write permissions plus denied create/delete paths,
and completed the direct-command-versus-login-shell experiment. A short
home-versus-shell retrieval remains before the formal
program/process/service/`systemd` probe.

Last completed session: `sessions/2026-09-04.md`

## Environment and capacity

- Uses macOS Terminal and has an Ubuntu homelab server.
- Can study about 5 hours daily.
- Prefers practical, job-oriented learning.
- Ubuntu currently retains `~/permissions-lab/mode-practice.txt` as
  `raf_0411:raf_0411` mode `664`, `service-access-lab.conf` as `root:sudo`
  mode `640`, and the `reportsvc` account plus its `/etc/reportsvc` and
  `/var/log/reportsvc` lab resources described in the latest session file.
- macOS retains `~/permissions-lab/mode-practice.txt` as `raffi:staff` mode
  `640`, created while the Ubuntu server was temporarily unavailable.

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
- On 2026-09-01, correctly classified configuration as intended behavior and
  logs as observed events, then placed service configuration, service logs,
  personal data, and disposable data under the appropriate conventional roles.
- Demonstrated that Nano edits an in-memory buffer and writes it to disk only
  on save: a saved `port=8080` persisted, while an unsaved `port=9090` change
  was discarded. Used installed `nano --help` to identify an unnecessary `-p`
  option, then correctly attributed saving to `Ctrl+O` plus `Enter`.
- Distinguished archive structure from gzip compression and parsed `tar`'s
  `-c`, `-z`, `-f`, `-t`, and `-x` operations. Diagnosed an incomplete archive
  by inspecting the source tree, recreated it with the missing log, listed its
  members, and restored it under a separate directory with `-C`. Verified that
  the current source contained `port=9090` while the point-in-time restored
  copy contained `port=8080`.
- Completed Phase 1 exit-check Part 1 without changing directories: created a
  mock configuration/log/report hierarchy, wrote the specified files with
  Nano, displayed their contents, and verified `/home/raf_0411` with `pwd`.
  After initially listing all entry types, repaired `find` with `-type f`.
- Passed Phase 1 exit-check Part 2: searched one existing and one missing log
  operand with `grep -n`, appended `grep` diagnostics with `2>>`, piped matching
  stdout through `head -n 2`, and overwrote the final report with `>`. A second
  run verified that the match report stayed at two lines while the diagnostic
  report grew from one line to two. Correctly explained that stdout enters the
  pipe and stderr bypasses `head` after focused repair.
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
- Can decode the type marker and owner/group/other triplets in basic `ls -l`
  output and select exactly one applicable permission class from a process's
  user and group identities.
- Understands regular-file `r`, `w`, and `x`, and distinguishes them from
  directory listing, modification, and traversal/search permissions.
- Demonstrated that a read-only, root-owned file can be deleted by a process
  with `w+x` on its parent directory.
- Used symbolic `chmod` with `+`, `-`, and `=`, changed an owning group with
  `chgrp`, changed and restored ownership with `sudo chown`, and verified that
  permission mode and ownership are independent metadata.
- Repaired group read access with `g+r` and explained why a narrowly authorized
  ordinary service identity is preferable to unrestricted `sudo`.
- Can derive numeric modes by summing `r=4`, `w=2`, and `x=1` within each
  owner/group/other triplet, decode a three-digit mode, and apply `chmod 640`.
- Distinguishes account creation from `sudo` authorization and primary groups
  from supplementary memberships; understands the safe append role of
  `usermod -aG`.
- Created and inspected a collision-checked `reportsvc` system account with no
  created home and `/usr/sbin/nologin`, then ran specific commands under that
  identity with `sudo -u reportsvc -- COMMAND`.
- Built a `root:reportsvc` mode-`640` configuration file and mode-`660` log
  file under mode-`750` directories. Verified configuration read, configuration
  write denial, existing-log write, new-log denial, and log-delete denial.
- Demonstrated in a disposable lab that file content write and directory-entry
  deletion are independent, and cleaned up the disposable directory.
- Retrieved that file `w` governs append while parent-directory `w+x` governs
  deletion, correctly allowing deletion of a read-only file in a writable and
  searchable directory.
- Ran `/usr/bin/id` directly as `reportsvc` and observed UID `113`, GID `115`,
  and only the same-named primary group. A login-style `sudo -iu reportsvc`
  instead warned that it could not enter `/nonexistent` and was refused by the
  configured `/usr/sbin/nologin` shell.
- Correctly distinguished harmless terminal visual wrapping from a real
  newline on a fresh one-command pathname example after one correction.

## Partial or missing foundations

- Exact nested paths have now been demonstrated in an unprompted transfer check,
  but should still receive later spaced review after earlier mistakes involving
  `~`, a nested backup directory, and a trailing slash on a filename.
- Numeric modes are demonstrated; `umask`, special bits, and ACLs remain new.
  Deletion via parent-directory `w+x` needs active review after repeated misses.
- Account creation, primary/supplementary groups, safe `usermod -aG` syntax,
  and restricted service-account design are understood; `usermod -aG` has not
  yet been executed in a live membership-change lab.
- Configuration-read and log-write needs were separated and verified live.
  Direct execution versus login-style execution under the no-login account was
  also verified. The learner initially did not know the role of the nonexistent
  home; retrieve its warning role separately from `nologin` refusal next time.
- `systemctl`, `systemd`, a service unit, and the managed process were briefly
  separated after initial conflation, but the formal process/service strand has
  not yet been probed or completed.
- Does not yet know the core commands for resource, OS, network, and log
  inspection.
- Networking knowledge is early: localhost, private addressing, gateways,
  ports, and troubleshooting need development.
- Little demonstrated experience configuring services or diagnosing homelab
  failures.
- Basic output/error redirection and ordinary pipeline routing have been
  demonstrated but need spaced review. The opening 2026-09-01 retrieval was
  correct about parse failure and file preservation, though the learner first
  thought a fresh command could not be submitted after the error and initially
  explained a new command's error capture only through overwrite behavior.
  The command-ownership distinction was repaired in words. Long pasted-command
  boundaries still need delayed re-testing.
- Phase 1 stream routing has passed the exit check but needs spaced review. The
  learner initially placed an append redirect before the pipe, later needed
  the stdout-to-stdin pipe route retaught, and omitted the slash in `~/` once
  when running the repaired command. The final execution and explanation were
  correct after focused repair.
- A long `tee` command on 2026-09-04 was split by a real newline after a
  directory path, causing `tee` to target the directory and Bash to treat the
  filename as a second command. The immediate one-line retry succeeded; keep
  command-boundary handling in active spaced review.
- Nano's buffer-versus-disk state and `tar` snapshot/restore are demonstrated.
  The initial description that Nano creates and edits a file "directly" was
  refined to opening a buffer and creating/updating the disk file only on save.
  Re-test later through operational use rather than immediate drilling.
- Configuration files, virtualization, cloud platforms, web servers, and
  operational routines still need structured practice.

## Teaching approach

Move one concept at a time. Require predictions and terminal work, then test
without hints. Revisit weak concepts through short retrieval questions.

## Next action

Retrieve the missing-home warning versus `nologin` refusal with one
counterfactual, then probe and plan the formal
program/process/service/`systemd` lesson.

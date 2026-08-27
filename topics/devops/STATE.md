# STATE

Updated: 2026-08-27

## Current stage

Initial probe and roadmap complete. Phase 1 (Linux command line and filesystem)
is active. The learner has now demonstrated in the Ubuntu lab that commands
operate on their path arguments, relative paths are resolved from the current
directory, and creating a directory does not enter it. The guided
create/copy/rename/move/delete portion of `sysadmin-lab-01` is complete; an
unprompted transfer check is next.

Last session: `sessions/2026-08-27.md`

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

- The guided file-management lab is complete, but the same skills have not yet
  been demonstrated in the pending unprompted transfer check.
- Exact nested paths still need reinforcement after mixing `~` with an absolute
  home path, targeting `~/backups` instead of the nested directory, and using a
  trailing slash once for a file.
- Does not yet understand Unix permission notation and ownership reliably.
- Process, service, `systemd`, and `systemctl` concepts are conflated.
- Does not yet know the core commands for resource, OS, network, and log
  inspection.
- Networking knowledge is early: localhost, private addressing, gateways,
  ports, and troubleshooting need development.
- Little demonstrated experience configuring services or diagnosing homelab
  failures.
- Redirection, configuration files, virtualization, cloud platforms, web
  servers, and operational routines need structured practice.

## Teaching approach

Move one concept at a time. Require predictions and terminal work, then test
without hints. Revisit weak concepts through short retrieval questions.

## Next action

Perform an unprompted file-management transfer check, then continue Phase 1
with text inspection and searching.

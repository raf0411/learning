# STATE

Updated: 2026-09-11

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
and completed the direct-command-versus-login-shell experiment. On 2026-09-06,
the formal program/process/service/`systemd` probe and planned conceptual lesson
were completed. After focused repair, the learner separated passive program and
unit files, live processes, daemon processes, the managed service unit,
temporary control clients, and the persistent `systemd` manager. A live SSH
inspection and a disposable transient-service lifecycle lab confirmed the
model. On 2026-09-07, read-only checks confirmed that the transient unit had
been collected and its former process no longer existed. A same-day signal
lesson continuation showed that signal delivery, handler execution, termination,
and the stopped state were still conflated. In the final same-day continuation,
the learner answered the pending three-question retrieval check correctly:
a returning handler continued the process, default/handled/ignored dispositions
produced the expected distinct outcomes, and `active (exited)` with `MainPID=0`
was assigned to the active service unit with no remaining main process. The
signal-delivery-versus-disposition foundation is now demonstrated conceptually.
The next node—process state versus foreground/background placement—was
introduced, but its first prediction was not attempted before session end.
On 2026-09-08, a live macOS Zsh job-control lab established process state
versus terminal placement. The learner demonstrated `Ctrl+Z`, `bg`, `fg`,
trailing `&`, `jobs -l`, jobspecs, PID inspection, and cleanup. Foreground and
background were repeatedly reversed in predictions and explanation, but the
final repair check correctly classified `fg` as resuming a stopped job in the
foreground while the shell waits. In a same-day continuation, the learner
retrieved that distinction correctly and explained that the shell waits for a
foreground job. The safe-termination lesson then began. The learner established
that application cleanup requires the process to execute further instructions.
`SIGTERM`, `SIGKILL`, and plain `kill PID` were introduced from the installed
macOS manual pages, but the safe-sequence check and disposable lab were not
attempted before session end. On 2026-09-09, retrieval confirmed `fg` but
re-exposed confusion between signal delivery, handler return, and termination.
After repair, the learner correctly classified default termination, handler
return and continuation, and handler cleanup followed by explicit exit. They
also identified that successful `kill` establishes signal-request acceptance,
not process exit. The safe escalation branches were answered correctly after
the sequence was shown, but a later prediction incorrectly kept an ordinary
`sleep` alive after `SIGTERM`. In a continuation, the learner repaired the
wait-before-inspection order and completed a live Ubuntu comparison. Ordinary
`sleep` PID `361508` disappeared after `SIGTERM`, whereas a Bash process with a
returning handler printed its handler message and PID `375142` remained after a
wait. The learner explained both outcomes correctly but could not yet construct
the exact `SIGKILL` and verification commands independently. PID `375142` was
last observed running, so its current identity had to be checked before cleanup.
On 2026-09-10, an empty `ps` snapshot verified that PID `375142` was no longer
present. The learner then created and identity-checked a fresh disposable Bash
handler process, sent `SIGTERM`, waited, and verified that its returning handler
left it running. After one variable-name correction in the written rehearsal,
they conditionally sent `SIGKILL`, waited, and verified an empty final `ps`
snapshot. The safe escalation sequence is now demonstrated at command level.
A focused process-resource probe then confirmed a floor in `ps` snapshots,
`top` refreshes, one-of-four capacity reasoning, and partial file residency.
On 2026-09-11, the learner first treated the interval between two `top`
refreshes as one continuously observed frame. After “frame” was clarified as
one sampled instant, they correctly placed already-running and later-starting
processes in fresh frames. Installed `top(1)` documentation established its
since-last-screen-update window, and a fresh calculation correctly separated
`ps = 20/200 = 10%` from `top = 2/4 = 50%`. The physical home server reported
one socket, eight cores, two threads per core, and sixteen logical CPUs.
Irix/Solaris normalization remains GUIDED: the learner correctly produced some
normalized examples but repeatedly changed the Irix per-logical-CPU scale and
later used the wrong Solaris denominator. A bounded `yes` process expired before
both modes were observed; the learner correctly diagnosed the resulting empty
filtered `top` and `ps` output, though they still ran an unnecessary `kill`
after the empty identity check. In a later continuation, separate bounded
observations captured the expected `top` scales near `6.2%` and `99%`, although
real-newline and incomplete-quote mistakes prevented a clean same-run toggle
record. After switching to a two-logical-CPU Ubuntu VM, the learner calculated
the Solaris value as `50%` after focused explanation and completed a correct
identity-check/`SIGTERM`/wait/absence-verification sequence on a disposable
`yes` process. `VIRT`, `RES`/RSS, and `SHR` are now introduced. The learner
ultimately treated residency and sharing as nested classifications after
repeatedly moving bytes incorrectly out of `VIRT`; a controlled live memory
experiment remains next.

The career direction was also refined on 2026-09-11: DevOps, Junior Cloud
Infrastructure, InfraOps, and Cloud Operations/Support are now the primary
targets. AWS, Docker, CI/CD, Terraform, Git, scripting, and observability are
core roadmap outcomes, while the completed Linux work remains foundational.

Last completed session: `sessions/2026-09-11.md`

## Environment and capacity

- Uses macOS Terminal and a physical Ubuntu home server for current labs.
- Can study about 5 hours daily.
- Prefers practical, job-oriented learning.
- The Ubuntu home server exposes 16 logical CPUs: one socket, eight physical
  cores per socket, and two hardware threads per core.
- A later Ubuntu desktop VM reports two logical CPUs through `nproc`; do not use
  the physical server's 16-CPU denominator for observations made on this VM.
- Ubuntu currently retains `~/permissions-lab/mode-practice.txt` as
  `raf_0411:raf_0411` mode `664`, `service-access-lab.conf` as `root:sudo`
  mode `640`, and the `reportsvc` account plus its `/etc/reportsvc` and
  `/var/log/reportsvc` lab resources described in the latest session file.
- Ubuntu no longer retains `tutor-lifecycle-20260906.service` or its former
  MainPID `236595`: on 2026-09-07, `systemctl show` reported
  `LoadState=not-found`, `ActiveState=inactive`, `SubState=dead`, and
  `MainPID=0`, while `ps -p 236595` returned only its header.
- Ubuntu PID `375142` was confirmed absent on 2026-09-10. Fresh disposable Bash
  handler PID `5767` was then terminated with `SIGKILL` after it survived
  `SIGTERM`; a final `ps` snapshot confirmed its absence.
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
- Explained that `/usr/bin/python3` can exist as a program without any process
  existing when it is not running.
- Distinguished a `.service` unit file as configuration from the executable
  program named by its `ExecStart` setting.
- Retrieved that the home field controls the missing-home warning while the
  configured `/usr/sbin/nologin` shell independently refuses login.
- Explains static files as passive and processes as live runtime actors, and
  classifies a daemon as a background service process rather than a file.
- Derives the need for a persistent manager that outlives an administrator's
  temporary command. Distinguishes `systemd` as that manager from `systemctl`
  and `systemd-run` as temporary clients.
- Distinguishes a passive unit file, systemd's managed service unit, and its
  associated daemon process. Understands that a service may have one, several,
  or no continuing processes, including `Type=oneshot` with
  `RemainAfterExit=yes`.
- Verified on Ubuntu that PID 1 is `systemd`; `ssh.service` was
  `active/running` with MainPID `7939`; and that PID was a root-owned `sshd`
  daemon with PPID 1.
- Inspected `/usr/lib/systemd/system/ssh.service` and identified `ExecStart=` as
  the launch instruction and `Restart=on-failure` as a manager-applied policy.
- Collision-checked, created, and inspected a transient service running
  `/usr/bin/sleep 1800`. Correctly predicted an active/running unit, nonzero
  MainPID, ordinary-account process identity, and temporary-client exit.
- On 2026-09-07, distinguished an `active (exited)` service unit from a daemon
  process after one correction, then verified that the transient unit had been
  collected and its former PID was absent.
- On the final 2026-09-07 retrieval, correctly distinguished signal delivery
  from the selected disposition across returning-handler, default-termination,
  cleanup-and-exit, and ignored-signal cases. Also correctly retrieved that an
  `active (exited)` service with `MainPID=0` has an active unit but no remaining
  main process.
- Demonstrated live that `Ctrl+Z` leaves a job stopped but existing, `bg`
  resumes it in the background with the prompt available, and `fg` resumes or
  moves it to the foreground while the shell waits. Used trailing `&` to start
  a running background job directly.
- Distinguished shell job number `[1]`, jobspecs `%1` and `%+`, and process ID;
  used `ps -p 55978` to verify the final disposable process before terminating
  it and confirming an empty `jobs -l` result.
- Retrieved that `fg` places a job in the foreground and makes the shell wait
  until it stops or terminates.
- Established that application cleanup requires the process to execute further
  instructions, motivating a cooperative termination opportunity before forced
  termination.
- Correctly classified `SIGTERM` with no custom handler, a returning handler,
  and a handler that explicitly exits. Identified that successful `kill`
  establishes accepted signal sending rather than handler completion or exit.
- On Ubuntu, predicted and verified disposition-dependent outcomes using two
  live processes: ordinary `sleep` disappeared after `SIGTERM`, while a Bash
  loop whose handler printed and returned remained present after a wait.
- Explained that `kill` requests kernel-mediated signal delivery and `ps`
  independently checks whether the PID is present. Correctly placed the grace
  period before the snapshot used for the escalation decision.
- On Ubuntu, executed the full safe sequence against verified
  disposable PID `5767`: `SIGTERM`, grace period, fresh `ps`, conditional
  `SIGKILL`, grace period, and final empty `ps`. Correctly explained that a
  returning handler lets execution continue, while `SIGKILL` gives the process
  no handler or cleanup opportunity.
- Explained after focused repair that `top` shows discrete refresh frames and
  can miss a process whose entire lifetime falls between two refreshes.
- Verified procps-ng 4.0.4 for `ps` and `top`, used the installed `ps(1)`
  manual to identify CPU time divided by elapsed lifetime, and independently
  calculated a fresh lifetime-average example as `15/60 = 25%`.
- Correctly explained on a fresh scenario that an already-running process can
  appear in the first `top` refresh while a later process appears only in
  refreshes taken after it starts; a process wholly between samples can be
  missed.
- Used installed `top(1)` documentation to identify its recent interval since
  the last screen update, then independently calculated `ps = 20/200 = 10%`
  and `top = 2/4 = 50%` for the same conceptual process.
- Used `nproc` and `lscpu` on the physical Ubuntu server to inspect 16 logical
  CPUs derived from one socket, eight cores, and two threads per core.
- Created and identity-checked bounded disposable `yes` PID `57467`, then
  correctly diagnosed that its CPU-time limit explained the later zero-task
  PID-filtered `top`, empty `ps`, and unnecessary `kill`. Final inspection
  confirmed the PID absent.
- Observed separate bounded `yes` processes near `6.2%` and `99%` in `top`,
  matching the Solaris-normalized and Irix-style scales on the 16-logical-CPU
  physical server, though the interactive before/after toggle was not recorded
  cleanly in one run.
- On a two-logical-CPU Ubuntu VM, calculated that one fully occupied logical CPU
  is `50%` of whole-VM capacity after the normalization rule was explained.
- On the VM, freshly matched disposable `yes` PID `4736` to the intended user
  and command, sent `SIGTERM`, waited, and verified an empty final `ps` result
  without unnecessary escalation.
- Understands after focused repair that `VIRT` contains all mapped virtual
  pages, while `RES`/RSS counts the currently resident subset. Correctly kept
  four mappings while reducing residency to one page after an eviction.
- Understands that `SHR` is a potentially shareable subset of `RES`, not memory
  added on top. Calculated `116 KiB` as the non-`SHR` portion of a displayed
  `1980 KiB RES`/`1864 KiB SHR` row and `12 MiB` of distinct physical memory
  when two processes share the same `8 MiB` plus `2 MiB` private each.

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
  also verified. The home-field-versus-`nologin` distinction was retrieved
  correctly on 2026-09-06; move it to spaced review.
- The process/service lesson repaired repeated confusion among `systemd`,
  `systemctl`, unit files, service units, programs, and daemon processes. The
  learner ultimately defined and demonstrated each role correctly, including a
  live transient-unit inspection. Unit file versus service unit should receive
  spaced retrieval because they were merged once after initial repair. PID
  versus PPID also needs a later operational check after one mix-up. The
  transient service cleanup was verified. After correction, the learner
  correctly transferred the chain: the `sleep` process exits naturally, the
  unit becomes inactive, and `--collect` unloads it to `not-found`.
- The 2026-09-07 signals/jobs/resource probe found a floor in recognizing that
  `Ctrl+C` returns the prompt, `Ctrl+Z` pauses rather than exits, `ps` is a
  short-lived snapshot, and `top`/`htop` expose process CPU and memory use. At
  the probe, the learner treated `Ctrl+C` and `kill PID` as unavoidable forced
  destruction, did not know `&`, `jobs`, `fg`, or `bg`, and interpreted one
  process near 100% CPU as necessarily exhausting a four-core machine.
- The signal-delivery-versus-disposition foundation is now demonstrated both
  conceptually and in live default-versus-returning-handler comparisons. The
  complete conditional escalation sequence is also demonstrated at command
  level. The learner initially repeated `SIGTERM` where escalation required
  `SIGKILL`, and later used `resistant_pid` instead of the assigned
  `resistant_lab_pid` in a written rehearsal; both were repaired before the
  live sequence. Process state versus
  foreground/background placement and basic shell job control are now
  demonstrated live. Because
  `fg` was repeatedly misclassified as moving a job into the background, keep
  `fg` versus `bg` in spaced review despite one clean retrieval. `SIGTERM` as a
  cooperative termination request, uncatchable/unignorable `SIGKILL`, and plain
  `kill PID` defaulting to `SIGTERM` have been introduced from local manual
  pages. Keep the sequence in later operational review rather than blocking
  progression.
- `ps` lifetime versus `top` recent-interval CPU measurement is GUIDED after one
  clean fresh calculation. Irix/Solaris normalization remains GUIDED: expected
  values were observed separately, and `100% / 2 = 50%` was calculated for the
  VM after explanation, but the learner could not independently explain the
  reference-whole change and a clean same-run `I`-toggle comparison remains
  absent. Re-test later in a fresh transfer scenario rather than repeating the
  same calculation immediately.
- `VIRT`, `RES`/RSS, and `SHR` are conceptually GUIDED. The learner initially
  treated `VIRT` as a nonresident pool depleted by page-in, then reversed both
  `VIRT` and `RES` directions during eviction. A simpler page-count scenario
  repaired the model. `SHR` was first described as possibly not in RAM, but the
  learner then correctly solved the shared-page double-counting example. Begin
  next session with a controlled live mapping/residency experiment.
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
without hints. Revisit weak concepts through short retrieval questions. For
multiple-choice checks, vary the correct option's position and avoid repeated
answer-letter patterns that could reveal the answer independently of the
concept being tested.

## Next action

On the Ubuntu VM, run `free -h`, `getconf PAGESIZE`, and `python3 --version`,
then perform a bounded controlled mapping/residency experiment. Predict and
inspect how mapping, touching, and eviction affect `VIRT` and `RES`/RSS, and
interpret `SHR` without adding it to `RES` or treating it as proof of exact
system-wide sharing. Keep CPU normalization, safe termination, consistent
variable naming, and physical command boundaries in spaced operational review.

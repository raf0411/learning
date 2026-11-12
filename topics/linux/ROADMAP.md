# Roadmap

Status key: `[ ]` upcoming, `[>]` current, `[x]` milestone demonstrated.

## Coverage standard

This path targets confident, independent Linux terminal use. Its breadth is
checked against the Linux Foundation Introduction to Linux (LFS101) beginner
outline, while lessons emphasize hands-on performance rather than topic exposure.

## Dependency shape

```text
files and navigation (1-3)
          |
          v
shell data flow and text work (4-5)
          |
          v
Linux environment and access (6-7)
          |
          v
software, processes, services, and networking (8-10)
          |
          v
Bash automation and integrated terminal work (11-12)
```

## Learning path

1. `[x]` **Filesystem orientation and navigation**
   - Terminal command anatomy; working directory; absolute and relative paths
   - `pwd`, `ls`, `cd`, `.`, `..`, and `~`
   - `mkdir` and a small project directory structure
   - Milestone: navigate and construct a requested directory tree independently

2. `[x]` **Safe file organization**
   - `touch`, `cp`, `mv`, `rm`, and `rmdir`
   - Safe overwrite and removal checks; recursive operations
   - Globbing and selecting several files without unintended matches
   - Milestone: reorganize mixed files safely without procedural hints

3. `[x]` **Links, file types, and archives**
   - Regular files, directories, and other common file types
   - Hard links and symbolic links; copying versus linking
   - `tar`, `gzip`, `bzip2`, and `xz`; inspect before extracting
   - Milestone: package, verify, extract, and restore a disposable project
   - Completed 2026-11-01 with an independently planned bzip2 archive workflow;
     case-sensitive compression-option recall was retained on 2026-11-02

4. `[x]` **Content inspection, CLI editing, and documentation**
   - `cat`, `less`, `head`, `tail`, `nl`, and `file`
   - Follow changing output and choose tools appropriate to file size and purpose
   - Create and edit text with a terminal editor; save, search, and exit safely
   - `--help`, shell `help`, `man`, `info`, and installed documentation
   - Milestone: inspect an unfamiliar file or log and use local documentation to
     complete an unfamiliar editing or command task
   - Completed for curriculum progression on 2026-11-03; unfamiliar-option
     recovery and evidence quality remain active review items

5. `[x]` **Shell mechanics, pipes, and redirection**
   - Quoting, escaping, expansion, variables, environment, history, and aliases
   - Standard input, output, and error; `>`, `>>`, `<`, `2>`, pipes, and `tee`
   - Exit status, `&&`, `||`, and safe command sequencing
   - Milestone: predict and verify where each command's input, output, and error
     travel through a multi-stage command
   - Introductory work began 2026-11-03 with `>`, `>>`, `<`, `2>`, and `|`;
     completed for curriculum progression on 2026-11-08 after spaced retrieval;
     combined routing and variable integration retain GUIDED review items

6. `[>]` **Text searching and manipulation**
   - `grep` and basic regular expressions
   - `wc`, `cut`, `paste`, `sort`, `uniq`, `tr`, `diff`, and `join`
   - `xargs`, introductory `sed`, and introductory `awk`
   - Milestone: derive and verify a requested report from unfamiliar text data
   - Work began 2026-11-08 with `grep`, anchors, `.*`, `sort`, `uniq`, `cut`,
     and `tr`; introductory practice now covers every listed tool. A second
     unfamiliar normalized report was completed and verified with focused
     guidance; independent milestone performance remains to be tested

7. `[x]` **Linux environment, filesystem layout, and access**
   - Use a disposable Linux VM and distinguish Linux from macOS observations
   - Distributions, release information, shell versus kernel, and command paths
   - `/etc`, `/var`, `/tmp`, `/run`, `/dev`, `/proc`, `/sys`, and home directories
   - `find`, `locate`, `type`, `command -v`, `which`, and `whereis`
   - Users and groups as identities; ownership, `rwx`, `chmod`, `chown`, `chgrp`,
     `umask`, and basic `sudo` usage
   - Milestone: orient in an unfamiliar Linux host, locate requested resources,
     and repair a standard permission problem safely
   - Completed for curriculum progression 2026-11-11 with independent combined
     ownership/mode repair; umask and runtime-record reasoning remain in review

8. `[>]` **Packages and installed software**
   - Package, repository, dependency, and update concepts
   - Basic Debian-family (`apt`, `dpkg`) and Red Hat-family (`dnf`, `rpm`) usage
   - Search, inspect, install, update, and remove a test package; verify the result
   - Milestone: use documentation to manage unfamiliar test software safely
   - Guided lifecycle work completed 2026-11-12: indexed-search comparison,
     repository repair, catalog refresh, scoped upgrade, removal, and purge.
     Resumed tree plan/install completed with guidance; independent inspection
     and simulation choices succeeded, but approval reasoning needed teaching.
     Red Hat-family roles introduced conceptually; independent milestone open

9. `[>]` **Processes, jobs, and resource monitoring**
   - PID/PPID, foreground and background jobs, sessions, and signals
   - `ps`, `pgrep`, `jobs`, `bg`, `fg`, `top`, `free`, `uptime`, `df`, and `du`
   - Safe TERM -> wait -> inspect -> conditional KILL -> verify workflow
   - Milestone: investigate and control a disposable process from evidence
   - Began 2026-11-12: guided foreground/background timers, jobs, PID/PPID,
     process-state inspection, and normal completion. Guided job-control lab and
     independent targeted TERM/exit verification completed. Resource tools
     introduced; next assess the unattempted resource-triage worksheet.
     State/resource interpretation and escalation remain guided; pgrep pending

10. `[ ]` **Services, logs, scheduling, and basic networking**
    - Basic `systemctl` service status/start/stop/restart behavior
    - `journalctl`, common log locations, filtering, and following new entries
    - Introductory `cron` and one safe recurring task
    - Interfaces, addresses, DNS, ports, and basic TCP/UDP concepts
    - `ip`, `ss`, `ping`, `dig` or `getent`, `curl`, and `nc`
    - SSH client usage and secure file transfer with `scp` or `sftp`
    - Milestone: answer a service or connectivity question using process, log,
      and network evidence rather than guesswork

11. `[ ]` **Bash scripting fundamentals**
    - Script files, shebangs, execution, arguments, and command substitution
    - Tests, conditionals, loops, functions, input, output, and exit codes
    - Quoting and validation that prevent common scripting mistakes
    - Milestone: write and troubleshoot a small script that safely automates a
      repeated terminal task

12. `[ ]` **Portfolio capstone — Linux operations and log-analysis toolkit**
    - Build a safe Bash command-line tool that inspects a Linux host and analyzes
      supplied sample logs without making destructive system changes
    - Produce a timestamped report containing selected system, disk, process,
      service, log, and basic network evidence
    - Use deliberate directory organization, standard permissions, pipes,
      redirection, text-processing tools, functions, arguments, exit codes, and
      dependency checks
    - Include realistic test fixtures and ordinary failures such as a missing
      file, unavailable command, stopped test service, or malformed input
    - Diagnose and repair the injected problems without procedural hints, then
      record what evidence identified each cause
    - Deliver a portfolio package containing:
      - the original script or scripts;
      - sanitized sample input and generated output;
      - a README with the problem, features, setup, usage, safety boundaries,
        design decisions, and limitations;
      - a test and verification checklist;
      - a concise troubleshooting case study;
      - a reproducible demonstration on a disposable Linux VM
    - Optionally publish the finished package in a Git repository; Git operation
      is a publishing step, not an additional curriculum phase
    - Milestone: independently demonstrate the project from a clean setup,
      explain the implementation, verify its output, and meet the performance
      criteria in `GOAL.md`

## Current position

Phases 1 and 2 are complete: filesystem navigation/construction and the
integrated safe-file-organization checkpoint have been demonstrated.

Phase 3 is complete. Symbolic-link, hard-link, and relative-link experiments
were completed with guidance, and the learner independently planned and
executed a safe bzip2 package/list/extract workflow. The case-sensitive
compression mapping was retrieved correctly after spacing on 2026-11-02. Link
reasoning and complete archive-evidence capture remain review items.

Phase 4 is complete for curriculum progression. Content classification, bounded
and interactive inspection, live log following, and terminal editing were
demonstrated. Unfamiliar local-documentation recovery and evidence quality stay
in `REVIEW.md` rather than blocking forward progress.

Phase 5 is complete for curriculum progression as of 2026-11-08. After the
November 7 rebuild, a spaced session independently retrieved redirection order,
conditional sequencing, environment export, alias inspection, and history
meaning. A short portable `tail | tee | wc` route was constructed and verified
after a functional `tee` cue. Immediate status capture, combined routing, and
variable/command-substitution integration remain review items rather than
blocking forward progress.

Phase 6 introductory coverage is complete; its independent report milestone
remains open for spaced review. On 2026-11-09 the learner independently recovered
the `join` delimiter option and reconstructed report processing stages. Exact
status selection required a field-boundary hint before successful verification.

Phase 7 is complete for curriculum progression as of 2026-11-11. Ubuntu host
orientation, command lookup, filesystem interfaces, find/xargs, and standard
ownership/permissions have been exercised. An independent shared-workspace
repair correctly combined distinct directory policies, group ownership, file
permissions, content preservation, and evidence auditing. Umask derivation,
runtime records versus kernel identity, PATH ordering, and find/xargs retention
remain in interleaved review.

Phase 8 is active. Guided practical coverage now includes package metadata,
installation, locate's index versus live search, a real repository failure and
repair, catalog refresh, scoped upgrade, removal, and purge. Verification was
completed for the upgrade and cleanup. The resumed tree plan/install succeeded
with guidance in metadata and approval reasoning; independent command selection
and bounded tree execution were demonstrated. Red Hat-family roles introduced
conceptually, without execution. Full independent package management remains
open, as does Phase 6's independent report milestone.

Phase 9 began with guided timers and process inspection: foreground waiting,
background jobs, PID/PPID, Bash parentage, S state, and normal completion.
Guided job-control practice and independent fresh-PID inspection, targeted TERM,
and exit verification succeeded. Parent-name evidence needed a reminder.
Resource monitoring now includes uptime/nproc/top, free, df, and du; home-directory
usage construction succeeded independently, while resource interpretation remains
guided. Next resume labs/2026-11-12-resource-triage.md (unattempted), then continue
process discovery and resource diagnosis. State interpretation and escalation
reasoning remain guided; Phase 9 milestone not yet complete.

## Current scope boundary

This roadmap intentionally stops at terminal-user confidence. Advanced identity
administration, persistent network/firewall configuration, disk partitioning and
LVM, boot/kernel recovery, SELinux/AppArmor administration, service deployment,
Git workflows, containers, and virtualization management are deferred.

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

5. `[>]` **Shell mechanics, pipes, and redirection**
   - Quoting, escaping, expansion, variables, environment, history, and aliases
   - Standard input, output, and error; `>`, `>>`, `<`, `2>`, pipes, and `tee`
   - Exit status, `&&`, `||`, and safe command sequencing
   - Milestone: predict and verify where each command's input, output, and error
     travel through a multi-stage command
   - Introductory work began 2026-11-03 with `>`, `>>`, `<`, `2>`, and `|`;
     combined stdout/stderr pipeline routing remains GUIDED

6. `[ ]` **Text searching and manipulation**
   - `grep` and basic regular expressions
   - `wc`, `cut`, `paste`, `sort`, `uniq`, `tr`, `diff`, and `join`
   - `xargs`, introductory `sed`, and introductory `awk`
   - Milestone: derive and verify a requested report from unfamiliar text data

7. `[ ]` **Linux environment, filesystem layout, and access**
   - Use a disposable Linux VM and distinguish Linux from macOS observations
   - Distributions, release information, shell versus kernel, and command paths
   - `/etc`, `/var`, `/tmp`, `/run`, `/dev`, `/proc`, `/sys`, and home directories
   - `find`, `locate`, `type`, `command -v`, `which`, and `whereis`
   - Users and groups as identities; ownership, `rwx`, `chmod`, `chown`, `chgrp`,
     `umask`, and basic `sudo` usage
   - Milestone: orient in an unfamiliar Linux host, locate requested resources,
     and repair a standard permission problem safely

8. `[ ]` **Packages and installed software**
   - Package, repository, dependency, and update concepts
   - Basic Debian-family (`apt`, `dpkg`) and Red Hat-family (`dnf`, `rpm`) usage
   - Search, inspect, install, update, and remove a test package; verify the result
   - Milestone: use documentation to manage unfamiliar test software safely

9. `[ ]` **Processes, jobs, and resource monitoring**
   - PID/PPID, foreground and background jobs, sessions, and signals
   - `ps`, `pgrep`, `jobs`, `bg`, `fg`, `top`, `free`, `uptime`, `df`, and `du`
   - Safe TERM -> wait -> inspect -> conditional KILL -> verify workflow
   - Milestone: investigate and control a disposable process from evidence

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

Phase 5 is current. Work began on 2026-11-03 with output replacement, append,
input redirection, error redirection, and pipelines. Combined stdout/stderr
pipeline routing remains GUIDED and is the immediate learning edge.

## Current scope boundary

This roadmap intentionally stops at terminal-user confidence. Advanced identity
administration, persistent network/firewall configuration, disk partitioning and
LVM, boot/kernel recovery, SELinux/AppArmor administration, service deployment,
Git workflows, containers, and virtualization management are deferred.

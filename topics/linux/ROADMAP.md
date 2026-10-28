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

2. `[>]` **Safe file organization**
   - `touch`, `cp`, `mv`, `rm`, and `rmdir`
   - Safe overwrite and removal checks; recursive operations
   - Globbing and selecting several files without unintended matches
   - Milestone: reorganize mixed files safely without procedural hints

3. `[ ]` **Links, file types, and archives**
   - Regular files, directories, and other common file types
   - Hard links and symbolic links; copying versus linking
   - `tar`, `gzip`, `bzip2`, and `xz`; inspect before extracting
   - Milestone: package, verify, extract, and restore a disposable project

4. `[ ]` **Content inspection, CLI editing, and documentation**
   - `cat`, `less`, `head`, `tail`, `nl`, and `file`
   - Follow changing output and choose tools appropriate to file size and purpose
   - Create and edit text with a terminal editor; save, search, and exit safely
   - `--help`, shell `help`, `man`, `info`, and installed documentation
   - Milestone: inspect an unfamiliar file or log and use local documentation to
     complete an unfamiliar editing or command task

5. `[ ]` **Shell mechanics, pipes, and redirection**
   - Quoting, escaping, expansion, variables, environment, history, and aliases
   - Standard input, output, and error; `>`, `>>`, `<`, `2>`, pipes, and `tee`
   - Exit status, `&&`, `||`, and safe command sequencing
   - Milestone: predict and verify where each command's input, output, and error
     travel through a multi-stage command

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

Phase 1 is complete. The learner independently constructed the requested
`copy-practice` tree, explicitly mapped its branches to verification evidence,
and distinguished `/` path nesting from `mkdir -p` parent creation after guided
correction. Phase 2 is current. Basic single-file copying is GUIDED; the next
step is safe handling of an existing destination with `cp -i` in the disposable
tree.

## Current scope boundary

This roadmap intentionally stops at terminal-user confidence. Advanced identity
administration, persistent network/firewall configuration, disk partitioning and
LVM, boot/kernel recovery, SELinux/AppArmor administration, service deployment,
Git workflows, containers, and virtualization management are deferred.

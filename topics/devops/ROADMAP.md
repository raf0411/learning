# ROADMAP

Updated: 2026-08-26  
Target window: 14–16 weeks  
Current phase: Phase 1

Current checkpoint: command targets and working-directory state retrieved
correctly in words; terminal verification and the first Ubuntu file-management
lab are pending.

The dates are pacing estimates, not permission to advance. Each phase has an
exit check; demonstrated skill matters more than merely completing a week.

## Dependency path

```mermaid
flowchart TD
    A[1. Shell and filesystem] --> B[2. Users and permissions]
    A --> C[2. Processes, packages and systemd]
    B --> D[3. Networking and SSH]
    C --> D
    B --> E[4. Storage, logs and scheduled work]
    C --> E
    D --> F[5. Run and troubleshoot services]
    E --> F
    A --> G[6. Bash automation and Git]
    E --> G
    D --> H[5. Host security, backup and monitoring]
    E --> H
    F --> I[7. Cloud support fundamentals]
    H --> I
    F --> J[8. Capstone and job readiness]
    G --> J
    H --> J
    I --> J
```

## Phase 1 — Linux command line and filesystem (Week 1)

Next session: verify the path/current-directory concept at the Ubuntu terminal,
complete the `sysadmin-lab-01` create/copy/rename/delete lab, and explain each
command.

Learn:

- command structure, arguments, options, paths, and working-directory state;
- create, copy, move, rename, and remove files/directories safely;
- inspect text and search with `less`, `head`, `tail`, `grep`, and `find`;
- pipes, standard input/output/error, and `>`, `>>`, and `2>`;
- command discovery with `man`, `--help`, and shell history;
- basic filesystem hierarchy, archives, and editing with `nano`.

Exit check: complete a file-management and log-search lab from a written
scenario, without command-by-command instructions, and explain every command.

## Phase 2 — Core Ubuntu administration (Weeks 2–3)

Learn:

- users, groups, ownership, permission bits, `sudo`, and least privilege;
- processes, signals, jobs, resource inspection, and `/proc` basics;
- packages, repositories, updates, and safe change habits;
- services, units, boot targets, `systemd`, `systemctl`, and `journalctl`;
- memory, CPU, load, disk-space, and OS inspection.

Labs: create a restricted service account; repair broken access; install and
manage a service; diagnose a deliberately stopped or misconfigured unit.

Exit check: administer users and a service, locate relevant logs, and explain
the difference between a program, process, daemon, service, and service manager.

## Phase 3 — Networking and remote administration (Weeks 4–5)

Learn:

- IPv4, subnet basics, private/public addresses, loopback, gateways, routing;
- TCP versus UDP, ports, sockets, DNS, DHCP, and the web request path;
- inspect and test with `ip`, `ss`, `ping`, `traceroute`, `dig`, and `curl`;
- SSH passwords versus keys, host keys, configuration, copying files, and
  secure remote access;
- host firewall fundamentals with Ubuntu's supported tooling.

Labs: map the homelab network; set up key-based SSH; expose only an intended
service; diagnose DNS, route, port, firewall, and application failures.

Exit check: troubleshoot several unknown connectivity failures using a layered
method and justify each test.

## Phase 4 — Storage and routine operations (Weeks 6–7)

Learn:

- partitions, filesystems, mounts, capacity versus inode exhaustion;
- log locations, journal queries, rotation, and retention;
- archives, checksums, backup strategies, and verified restores;
- recurring work with cron and systemd timers;
- routine patching, inventory, operational notes, and change verification.

Labs: attach or simulate extra storage; recover from a full-filesystem
scenario; schedule and verify a backup; restore deleted test data.

Exit check: find a storage/logging problem, fix it safely, and restore data from
a backup rather than merely creating one.

## Phase 5 — Operate a real service securely (Weeks 8–9)

Learn:

- install and configure Nginx or Apache;
- configuration syntax testing, ports, logs, processes, and dependencies;
- HTTP and TLS fundamentals;
- permissions, firewall policy, updates, backup, and simple monitoring;
- a repeatable troubleshooting workflow and incident notes.

Project 1: publish and document a small homelab web service, then diagnose
injected failures such as a stopped unit, occupied port, invalid configuration,
permissions error, firewall rule, and low disk space.

Exit check: recover the service from unknown failures and provide concise
evidence of the root cause. Begin applying selectively to support and junior
infrastructure roles after this gate.

## Phase 6 — Useful automation (Week 10)

Learn:

- Bash variables, quoting, tests, loops, functions, exit status, and strict
  error handling;
- automate health checks, backups, account/inventory tasks, and log summaries;
- Git commits, branches, diffs, and README/runbook documentation;
- optional Ansible introduction only after the manual tasks are understood.

Project 2: create a small, tested administration toolkit in Git. Scripts must
be safe to rerun and must report failures clearly.

Exit check: automate a task already performed manually and explain its failure
modes.

## Phase 7 — Cloud support fundamentals (Weeks 11–12)

Choose one provider based on local job demand, then learn:

- regions/zones, virtual machines, images, disks, object storage, and snapshots;
- virtual networks, subnets, routes, security groups/firewalls, DNS, and public
  versus private access;
- identities, roles, policies, least privilege, secrets, and shared
  responsibility;
- metrics, logs, alerts, quotas, basic cost awareness, and provider support
  documentation.

Project 3: deploy the Phase 5 service to a small cloud VM, restrict access,
monitor it, back it up, and write a teardown procedure to prevent unwanted cost.

Exit check: diagnose access and service failures without randomly changing
rules, and explain cost/security implications.

## Phase 8 — Capstone and employment preparation (Weeks 13–16)

- Combine Linux, networking, service management, security, backup, monitoring,
  and automation into one reproducible project.
- Publish sanitized diagrams, runbooks, incident reports, and scripts.
- Practice Linux and networking troubleshooting interviews at the terminal.
- Translate lab evidence into resume bullets and apply consistently.
- Use job-posting feedback to adjust weak areas; study an entry certification
  only if it reinforces, rather than replaces, the practical work.

## Typical five-hour study day

- 30 minutes: retrieval practice from current and older material.
- 60 minutes: one new concept with primary documentation.
- 150 minutes: hands-on lab, including deliberate failures.
- 45 minutes: explain results and write a short runbook.
- 15 minutes: record errors and choose the next review item.

This cadence can be shortened when needed; consistency and successful labs are
more important than filling all five hours.

# Phase 12 capstone kickoff: design the toolkit (2026-11-21)

## What you're building

A safe Bash command-line tool that:

1. inspects a Linux host (read-only), and
2. analyzes a supplied sample log file,

and then writes a timestamped report. It runs on the Ubuntu VM. It must never need `sudo` and must never change the system.

Today is **design only. No code yet.** You write the spec, and the code gets built against it later. Writing the tests *before* the code is deliberate, because predicting and self-auditing were the weak spots last session.

Short answers are fine. This is a first draft that we'll refine together. Fill in every `TODO`.

---

## 0. Target environments

| Role                                                       | Machine                     | Notes                                                                      |
| ---------------------------------------------------------- | --------------------------- | -------------------------------------------------------------------------- |
| Build + all tests (including the deliberately broken ones) | Ubuntu VM (disposable)      | Reproducible demo for the README                                           |
| Real-world run, after the VM tests pass                    | Homelab: old laptop, Ubuntu | Docker (Navidrome, File Browser), Tailscale, reached over SSH from the Mac |

Rules:
- Never stop real homelab services or remove its tools for testing. Failure scenarios run on the VM only.
- Homelab output is sanitized before publishing: Tailscale 100.x addresses, `*.ts.net` names, hostnames, usernames.
- Containers are read-only and optional. `docker ps` requires root or `docker` group membership, and the VM has no Docker.

Design decision: how does the tool know **which service** to check? Hardcoded, an argument, or a config file? Choose one, and give one reason based on testing on the VM *and* running on the homelab.

```text
TODO
```

---

## Phase milestones this capstone will close

When you complete each part on your own, the matching phase is marked `[x]`.

| Capstone part | Closes |
|---|---|
| Log analysis section | 6 · Text processing |
| Dependency checks / verifying installed tools | 8 · Packages |
| Process + resource section | 9 · Processes |
| Service, journal, and network section | 10 · Services & networks |
| Script structure, guards, exit codes, tests | 11 · Bash scripting |
| Whole package demonstrated from a clean setup | 12 · Capstone |

---

## 1. Name and project layout

Tool name:

```text
TODO
```

Draw the directory tree. It must have places for: the script(s), sample logs, generated reports, tests, and the README.

```text
TODO
```

---

## 2. Interface: how is it run?

Write the exact command a user types, including the required and optional arguments.

```text
TODO
```

What happens if a required argument is missing?

```text
TODO
```

---

## 3. Report sections

Fill in the command(s) that would produce each section from memory first. Mark any you had to look up with `(looked up)`.

| # | Section | Command(s) | Phase |
|---|---|---|---|
| 1 | System identity (OS, kernel, hostname) | TODO | 7 |
| 2 | Load and memory | TODO | 9 |
| 3 | Disk usage | TODO | 9 |
| 4 | Top processes by CPU or memory | TODO | 9 |
| 5 | One service's status (you choose which) | TODO | 10 |
| 6 | Recent log/journal evidence for that service | TODO | 10 |
| 7 | Basic network (address, route, listening ports) | TODO | 10 |
| 8 | Sample-log analysis (see section 4) | TODO | 6 |

---

## 4. Log analysis questions

The sample log will be a text file of lines like this (exact format to be decided together):

```text
2026-11-20 14:03:11 ERROR auth: login failed for user alice
2026-11-20 14:03:15 INFO  web: GET /index.html 200
```

Write **three questions** the report should answer from such a log. For example: "How many lines per level?"

1. TODO
2. TODO
3. TODO

---

## 5. Exit status policy

What does each status mean for your tool?

| Status | Meaning |
|---|---|
| 0 | TODO |
| 1 | TODO |
| 2 | TODO |

What should the tool do if one report section fails, such as a missing command? Should it stop, or continue and remember the failure? Why?

```text
TODO
```

---

## 6. Safety boundaries

List at least three things the tool must **never** do.

1. TODO
2. TODO
3. TODO

---

## 7. Test plan (predictions before code)

Use your answers in sections 2 and 5 to fill in **expected** output and status. The "Actual" columns stay empty until the code exists.

| # | Scenario | Exact command | Expected output (short) | Expected status | Actual status | Matches spec? |
|---|---|---|---|---|---|---|
| A | Normal run with a valid sample log | TODO | TODO | TODO | | |
| B | No arguments | TODO | TODO | TODO | | |
| C | Log file doesn't exist | TODO | TODO | TODO | | |
| D | Log argument is a directory | TODO | TODO | TODO | | |
| E | A required command is unavailable | TODO | TODO | TODO | | |
| F | Log contains malformed lines | TODO | TODO | TODO | | |
| G | Chosen service is stopped | TODO | TODO | TODO | | |

---

## Notes and questions for the tutor

```text
(optional)
```

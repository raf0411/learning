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
should be an argument, because i personally think thats easier for the user to type it out directly in the terminal instead of them having to make a config file first? or maybe they can do both config file and argument
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
sysprobe
```

Draw the directory tree. It must have places for: the script(s), sample logs, generated reports, tests, and the README.

```text
its hard to draw it so im gonna do it like this:

main folder: sysprobe


3 subfolders: scripts, logs, reports, tests

inside sysprobe:
scripts,logs,reports,tests,README.md

inside scripts:
main.sh
```

---

## 2. Interface: how is it run?

Write the exact command a user types, including the required and optional arguments.

```text
sysprobe example1.log example2.log

or

sysprobe example1.txt

example1.txt contains:
example1.log
example2.log
```

What happens if a required argument is missing?

```text
Output an error message and stderr
```

---

## 3. Report sections

Fill in the command(s) that would produce each section from memory first. Mark any you had to look up with `(looked up)`.

| #   | Section                                         | Command(s)                 | Phase |
| --- | ----------------------------------------------- | -------------------------- | ----- |
| 1   | System identity (OS, kernel, hostname)          | hostname, uname            | 7     |
| 2   | Load and memory                                 | free                       | 9     |
| 3   | Disk usage                                      | du (looked up)             | 9     |
| 4   | Top processes by CPU or memory                  | top                        | 9     |
| 5   | One service's status (you choose which)         | systemctl (looked up)      | 10    |
| 6   | Recent log/journal evidence for that service    | journalctl (looked up)     | 10    |
| 7   | Basic network (address, route, listening ports) | ip, getent, nc (looked up) | 10    |
| 8   | Sample-log analysis (see section 4)             | grep (looked up)           | 6     |

---

## 4. Log analysis questions

The sample log will be a text file of lines like this (exact format to be decided together):

```text
2026-11-20 14:03:11 ERROR auth: login failed for user alice
2026-11-20 14:03:15 INFO  web: GET /index.html 200
```

Write **three questions** the report should answer from such a log. For example: "How many lines per level?"

1. What type of line is it?
2. When is the line made?
3. What kind of information we can gain from the line?

---

## 5. Exit status policy

What does each status mean for your tool?

| Status | Meaning       |
| ------ | ------------- |
| 0      | success       |
| 1      | known error   |
| 2      | unknown error |

What should the tool do if one report section fails, such as a missing command? Should it stop, or continue and remember the failure? Why?

```text
stop and give the user a message so they know why it stops or fail
```

---

## 6. Safety boundaries

List at least three things the tool must **never** do.

1. analyze an unsupported file type
2. analyze a directory
3. analyze an invalid txt file format

---

## 7. Test plan (predictions before code)

Use your answers in sections 2 and 5 to fill in **expected** output and status. The "Actual" columns stay empty until the code exists.

| #   | Scenario                           | Exact command         | Expected output (short)                                              | Expected status | Actual status | Matches spec? |
| --- | ---------------------------------- | --------------------- | -------------------------------------------------------------------- | --------------- | ------------- | ------------- |
| A   | Normal run with a valid sample log | sysprobe example1.log | Analysis created successfully! (created a file)                      | 1               |               |               |
| B   | No arguments                       | sysprobe              | Insufficient arguments! <br>sysprobe [FILE.log]                      | 1               |               |               |
| C   | Log file doesn't exist             | sysprobe              | Supplied file(s) does not exists!                                    | 1               |               |               |
| D   | Log argument is a directory        | sysprobe              | Supplied argument is a directory, please input a valid file instead! | 1               |               |               |
| E   | A required command is unavailable  | TODO                  | TODO                                                                 | TODO            |               |               |
| F   | Log contains malformed lines       | sysprobe broken.log   | Log contains malformed lines!                                        | 1               |               |               |
| G   | Chosen service is stopped          | TODO                  | TODO                                                                 | TODO            |               |               |

---

## Notes and questions for the tutor

```text
(optional)
```

---

## Tutor review: round 1 (2026-11-22)

Key: ✓ solid · ~ partly there · ✗ needs rethinking. Your draft above is kept as written. Put revisions in the *Revision* boxes below.

| §   | Verdict | Feedback                                                                                                                                                                                                                                                                                                                                                                                                             |
| --- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0   | ~       | Making the service an argument is a good choice. The stronger reason: the VM has no Docker, so you test there with a service it does have, and on the homelab you pass `docker`. That's the same script with no edits. But §2's command has no service argument at all.                                                                                                                                              |
| 1   | ✓       | Sound layout. A drawn version is below for reference.                                                                                                                                                                                                                                                                                                                                                                |
| 2   | ~       | (a) The service argument is missing. (b) The command accepts logs *and* a list file. How would the script tell `example1.txt` (a list) from a log? Pick one interface. (c) "Missing argument" needs an exit status too.                                                                                                                                                                                              |
| 3   | ~       | These are tool names, not commands. Hints: **load** has no command yet (Phase 9 showed it with one word). `du` measures a *directory*; which Phase 9 command shows free space per *filesystem*? `top` is interactive, so what happens when a script runs it? `getent`/`nc` test names and connections, but they don't *show* addresses, routes, or listening ports. Which Phase 10 command listed listening sockets? |
| 4   | ✗       | These describe the *format* of a line. A report question has an answer you can print: a count, a name, or a time. Example: "How many lines per level?" → `ERROR 3, INFO 12`. Write three like that.                                                                                                                                                                                                                  |
| 5   | ~       | 0 is fine. "Unknown error" can't work: the script can only report failures it detects. Base 1 and 2 on **whose fault it is**: the tool ran but found a problem, or the user ran it wrong. Stop versus continue: we'll discuss it in chat.                                                                                                                                                                            |
| 6   | ✗       | All three are *input validation*, which belongs in the guards and tests. Safety boundaries protect the **system and its data**. Think about `sudo`, services, files outside `reports/`, and the sanitization rule in §0.                                                                                                                                                                                             |
| 7   | ~       | Self-audit question in chat. E and G come after the stop/continue decision.                                                                                                                                                                                                                                                                                                                                          |

Reference tree format (an example layout, not a requirement):

```text
sysprobe/
├── README.md
├── bin/
│   └── sysprobe.sh
├── samples/
│   ├── good.log
│   └── broken.log
├── reports/
└── tests/
```

### Revision

```text
§2 command:
sysprobe -f example1.txt

§4 questions:
1. TODO
2. TODO
3. TODO

§5 statuses 1 / 2:
status 1 for the tool ran but found a problem
status 2 for the user ran it wrong

§6 never:
1. TODO
2. TODO
3. TODO
```

---

## Round 2: §4 and §6 explained another way

### §4: questions about the *whole file*, not about one line

Think of a bank statement.
- "What is a transaction?" is a question about the **format**, and your draft questions were this kind.
- "How much did I spend on food this month?" is a question about **all the lines together**. Its answer is a number. That's what a report question looks like.

Here is a sample log. It may become `samples/good.log` later:

```text
2026-11-20 14:03:11 ERROR auth: login failed for user alice
2026-11-20 14:03:15 INFO  web: GET /index.html 200
2026-11-20 14:04:02 WARN  disk: /var at 85%
2026-11-20 14:05:40 ERROR auth: login failed for user bob
2026-11-20 14:05:41 INFO  web: GET /about.html 200
2026-11-20 14:06:10 ERROR web: GET /admin 500
2026-11-20 14:07:00 ERROR auth: login failed for user alice
2026-11-20 14:08:30 INFO  web: GET /index.html 200
```

Write three questions about the whole file, **and answer each by reading the log**. Don't reuse "lines per level". Your answers become the expected output for test A.

| #   | Question about the whole file         | Answer from this log |
| --- | ------------------------------------- | -------------------- |
| 1   | What time did a user failed to login? | TODO                 |
| 2   | What type of log is a GET request?    | TODO                 |
| 3   | How many errors are in this log?      | TODO                 |

### §6: safety means protecting the machine and its data, not rejecting bad input

Analogy: a home inspector is allowed to *look* at everything.
- Refusing to inspect because you gave them the wrong address is **input validation**.
- Never knocking down a wall, never taking your keys, and never publishing your address online are **safety rules**.

For each bad version of `sysprobe` below, say what could go wrong on the homelab, then turn it into a "never" rule.

| Bad version                                                | What could go wrong?                                                                | Rule: sysprobe must never…                                                                                                                                    |
| ---------------------------------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Runs `sudo systemctl restart docker` to "test" the service | it could make every container in my homelab stops & restart once                    | change the state of the system                                                                                                                                |
| Saves its report to `/etc/sysprobe-report.txt`             | need root to write over /etc                                                        | need root or write outside a location the user owns. It writes to stdout, the user's home directory, or a path the user passes in, and runs as a normal user. |
| You push the homelab report to GitHub unedited             | it could giveaway sensitive data such as ip, hostnames, internal ip, usernames, etc | share sensitive detail to public                                                                                                                              |

---

## Status (2026-11-22)

Building started on the VM at `~/Documents/sysprobe`. Design work now happens **while** building. This file stays as the design reference, and the README will draw on it.

Still-open design items:
- the service argument (§0/§2);
- stop-versus-continue for a failed section;
- §3 commands;
- the §4 answers;
- §7 rows E and G.

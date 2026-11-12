# Resource triage — 2026-11-12

These are **fictional Linux snapshots**, not measurements from your VM.
Use them to practice choosing the next observation rather than making changes.
Do not kill processes, delete files, or run privileged commands for this task.
Short answers are enough; no commands need to be executed.

## A. “High load proves the CPUs are full”

A machine has 2 CPUs. Its one-minute load average is 4.00.
A recent top CPU sample shows 65% idle and 20% I/O wait (`wa`).
A colleague says this proves CPU execution is at 100% and wants to kill a process.

Does the evidence support that conclusion? What could contribute to the high
load, and what limits a comparison of these two measurements?

No, the 20% I/O wait, a CPU usage and load average are not good compariso between these two measurements

## B. “Almost no free RAM”

A machine reports 8 GiB total RAM, 150 MiB free, and 3 GiB available.

Does this snapshot alone justify declaring a RAM shortage? Explain which
number matters more for starting another application, and one thing you would
still need to know before declaring there is no problem.

No, because free doesn't mean its all the free space in RAM left, the 3 GB available is a better starting point, i honestly don't know what one additional fact we need

## C. “Where did the disk space go?”

A machine's root filesystem is 95% used. You want to measure the disk space
used by the directory /var/log and everything beneath it, as a single readable
summary—not inspect RAM or repeat the whole-filesystem capacity check.

Write the read-only command you would choose:

```bash
du -sh /var/log
```

If that command returns permission errors, would its reported total establish
the complete usage of /var/log? Briefly explain; do not propose deletion yet.

it can count size of everything beneath a directory but doesn't inspect the filesystem

Tell the tutor when the worksheet is ready.

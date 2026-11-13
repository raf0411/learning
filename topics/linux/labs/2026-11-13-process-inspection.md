# Fresh process inspection — 2026-11-13

## Goal and safety

Work in the Ubuntu VM's Bash terminal. Start one disposable timer and inspect it. Do not terminate processes or change system settings in this step. Old PIDs from previous lessons are not valid targets.

## 1. Start the timer

This starts a background timer that exits naturally after 15 minutes:

```bash
sleep 900 &
```

Record the command and actual output:

```text
raf_0411@ubuntu-desktop:~$ sleep 900 &
[1] 4946
raf_0411@ubuntu-desktop:~$ jobs -l
[1]+  4946 Running                    sleep 900 &
```

## 2. Investigate independently

Choose your own commands; local documentation is allowed.

Capture evidence showing:
- This shell's job number and status for the new timer.
- The timer's PID, parent PID, process state, and command.
- The parent's command name, verified with a separate inspection.

Use the fresh launch output to distinguish your timer from any other sleep processes. If it finishes before inspection, record that rather than treating its old PID as a current identity.

Paste your commands and output:

```text
raf_0411@ubuntu-desktop:~$ ps -p 4946 -o pid,ppid,stat,comm
    PID    PPID STAT COMMAND
   4946    4582 S    sleep
raf_0411@ubuntu-desktop:~$ ps -p 4582 -o pid,comm
    PID COMMAND
   4582 bash
```

## 3. Interpret

What does the observed process state tell you about what the timer was doing at inspection time?

it means the sleep process is currently running and the S means interruptible Sleep.
Running (Bash) means the job hasn't stopped or finished while S (Linux) means it is sleeping and waiting for an event not currently executing on a CPU

Stop here and tell the tutor the worksheet is ready. Leave the timer to finish naturally while we review; any later signal exercise will require fresh identity checks.

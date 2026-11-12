# Process checkpoint — 2026-11-12

## Goal and safety boundary

On your Ubuntu VM, independently inspect and end one disposable background
process. Use the same Bash terminal throughout. Local documentation is allowed.

Target only the timer created below. Do not reuse a PID/job number from earlier
exercises. Do not use sudo, broad name-based termination, or SIGKILL. If the
target is unclear or TERM does not end it after a short wait, stop and report
what you observe. If it finishes on its own, report that rather than claiming
that your signal ended it.

## 1. Start and inspect

Start the practice timer:

```bash
sleep 600 &
```

Choose commands to establish its current shell job number, PID, parent PID,
process state, and command name. Also verify the parent's command name.
Record the actual commands and relevant output; do not guess identities.

```text
raf_0411@ubuntu-desktop:~$ sleep 600 &
[1] 8759
raf_0411@ubuntu-desktop:~$ ps -p 8759 -o pid,ppid,stat,comm
    PID    PPID STAT COMMAND
   8759    8171 S    sleep
```

## 2. End it safely

Using its freshly verified identity, request normal termination. Allow a moment
for exit, then verify both the shell's job list and whether that PID still
appears in the process listing. Choose the commands yourself.

```text
raf_0411@ubuntu-desktop:~$ kill -TERM %1
[1]+  Terminated                 sleep 600
raf_0411@ubuntu-desktop:~$ jobs -l
raf_0411@ubuntu-desktop:~$ ps -p 8759 -o pid,ppid,stat,comm
    PID    PPID STAT COMMAND
```

## 3. Interpret your evidence

Was your timer's state before termination compatible with the shell reporting
its job as Running? Explain briefly using your actual output.

idk what u mean

What evidence establishes your final outcome? Is any further termination action
needed?

jobs -l and the ps shows nothing about the sleep process before, meaning the termination ended the sleep process already, not further action needed

Stop here and tell the tutor the worksheet is ready.

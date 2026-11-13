# Independent checkpoint — processes and RAM

Date: 2026-11-13
Environment: Ubuntu VM, same Bash terminal throughout.

## Safety boundary

Only signal the disposable timer you launch below. Do not act on any PID or job number from earlier lessons, change swap settings, or launch a memory-heavy workload. If your timer finishes naturally, record that; do not signal its old PID.

Choose your own inspection, termination, and verification commands. Local documentation is allowed. Record any help used. Keep commands on one physical line when possible.

## 1. Launch and investigate

Supplied setup:

```bash
sleep 900 &
```

Record the launch and your chosen commands/output proving:
- the timer's current shell job number and job status;
- its PID, parent PID, process state, and command;
- its parent's command name, separately verified.

```text
raf_0411@ubuntu-desktop:~$ sleep 900 &
[1] 5442
raf_0411@ubuntu-desktop:~$ jobs -l
[1]+  5442 Running                    sleep 900 &
raf_0411@ubuntu-desktop:~$ ps -p 5442 -o pid,ppid,stat,comm
    PID    PPID STAT COMMAND
   5442    4582 S    sleep
raf_0411@ubuntu-desktop:~$ ps -p 4582 -o pid,comm
    PID COMMAND
   4582 bash
```

Explain what this timer was waiting for and whether its observed state means it was executing on a CPU at that moment:

it has an S state meaning interruptable sleep, the timer is waiting to be executed a command other than the one it is executing like TERM or KILL, it can be interrupt during its running process, and it is executing on a CPU

## 2. Assess current memory headroom

Choose a command to inspect current RAM and configured swap. Record the headings and complete output:

```text
free -h
               total        used        free      shared  buff/cache   available
Mem:           3.3Gi       2.3Gi       158Mi        68Mi       1.1Gi       1.0Gi
Swap:             0B          0B          0B
```

Hypothetical planning question only—do not run this workload:

A new task would need an additional 2 GiB of resident RAM while existing demand stays unchanged. Based on your current output, is there enough estimated available RAM to accommodate it without swapping? Cite the relevant number and explain what your evidence does and does not establish. Would unused filesystem space automatically cover any shortfall?

No it is not enough, there is used 2.3 GiB no swap, available is 1.0 GiB and free is 158 MiB, 2 GiB additional needed RAM would exceed that and potentially indicates shortage memory risk. And no, filesystem space can not automatically cover any shortfall

## 3. Stop your timer safely

First recheck that your intended target is still the disposable timer from section 1. Then choose an appropriate termination request, allow time for it to act, and verify the result with both shell-job and process evidence. Do not send a stronger signal merely to demonstrate it.

Record your fresh identity check, actions, and verification in actual execution order:

```text
raf_0411@ubuntu-desktop:~$ jobs -l
[1]+  5442 Running                    sleep 900 &
raf_0411@ubuntu-desktop:~$ kill -TERM %1
[1]+  Terminated                 sleep 900
raf_0411@ubuntu-desktop:~$ jobs -l
raf_0411@ubuntu-desktop:~$ ps -p 5442 -o pid,ppid,stat,comm
    PID    PPID STAT COMMAND
```

Does your evidence justify any further termination signal? Explain briefly:

No, we TERM is enough because after waiting a few seconds, the jobs -l and the ps does not show the sleep process anymore, we don't need KILL

## Finish

Documentation or hints used, if any:

None

Tell the tutor when this file is ready. Preserve unexpected errors and actual results rather than replacing them with an ideal transcript.

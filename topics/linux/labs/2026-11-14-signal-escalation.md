# Independent signal-escalation practice — 2026-11-14

Run this in your **Ubuntu VM's interactive Bash terminal**, not on the Mac.

## Safety boundary

Only act on the disposable job launched below. Do not target other processes,
use broad name-based killing, or use sudo. Historical PIDs and job numbers are
not valid targets. Keep the same terminal open for the whole task.

The fixture intentionally ignores TERM, has no valuable work, and exits on its
own after approximately ten minutes. It starts short-lived child timers. If it
expires before you finish, record that result; do not signal its old identifier.

## 1. Launch

Paste this as **one physical line**:

```bash
bash -c 'trap "" TERM; printf "Disposable TERM-ignoring lab ready\n"; end=$((SECONDS+600)); while (( SECONDS < end )); do sleep 1; done' &
```

Wait for the ready message before proceeding.

## 2. Investigate and stop it

Choose your own commands. Local documentation is allowed.

- Identify the new job and its process; capture enough evidence to distinguish it from unrelated jobs.
- Try normal termination first, allow a short bounded wait, and inspect again.
- Decide whether escalation is justified from the fixture's known behavior and current evidence. Recheck the target immediately before any further signal.
- Stop only this disposable job if it remains alive. Verify the final result using both shell job information and process inspection.

Record the actual commands and output in order, including the launch:

```text
raf_0411@ubuntu-desktop:~$ bash -c 'trap "" TERM; printf "Disposable TERM-ignoring lab ready\n"; end=$((SECONDS+600)); while (( SECONDS < end )); do sleep 1; done' &
[1] 5387
raf_0411@ubuntu-desktop:~$ Disposable TERM-ignoring lab ready

i waited about 3 seconds...

raf_0411@ubuntu-desktop:~$ jobs -l
[1]+  5387 Running                    bash -c 'trap "" TERM; printf "Disposable TERM-ignoring lab ready\n"; end=$((SECONDS+600)); while (( SECONDS < end )); do sleep 1; done' &
raf_0411@ubuntu-desktop:~$ kill -TERM 5387
raf_0411@ubuntu-desktop:~$ jobs -l
[1]+  5387 Running                    bash -c 'trap "" TERM; printf "Disposable TERM-ignoring lab ready\n"; end=$((SECONDS+600)); while (( SECONDS < end )); do sleep 1; done' &
raf_0411@ubuntu-desktop:~$ kill -KIll 5387
[1]+  Killed                     bash -c 'trap "" TERM; printf "Disposable TERM-ignoring lab ready\n"; end=$((SECONDS+600)); while (( SECONDS < end )); do sleep 1; done'
raf_0411@ubuntu-desktop:~$ jobs -l
raf_0411@ubuntu-desktop:~$ ps -p 5387 -o pid,ppid,stat,comm
    PID    PPID STAT COMMAND
```

## 3. Conclusion

What evidence justified your final action, and what evidence establishes whether the job exited? Two sentences are enough.

raf_0411@ubuntu-desktop:~$ kill -KILL 5387
[1]+  Killed                     bash -c 'trap "" TERM; printf "Disposable TERM-ignoring lab ready\n"; end=$((SECONDS+600)); while (( SECONDS < end )); do sleep 1; done'
raf_0411@ubuntu-desktop:~$ jobs -l

after i use -TERM the jobs -l still shows the process, while when i used -KILL it works, the jobs -l didnt show any

Documentation or hints used, if any:

None

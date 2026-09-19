# Load average — 2026-09-19

## Session direction

Resume the unfinished load-versus-CPU-capacity comparison, then interpret a
fresh read-only snapshot from the learner's Ubuntu machine. Use the actual
machine's CPU count; earlier sessions used both a physical server and a VM.

## Opening prediction

Hypothetical systems with steady CPU-bound workloads. For this simplified
comparison, no tasks contribute to load through uninterruptible sleep, and
all logical CPUs are available to the workload.

| System | Logical CPUs | One-minute load average |
| --- | ---: | ---: |
| A | 4 | 8.00 |
| B | 16 | 8.00 |

Which system would you expect to have tasks waiting for CPU time? Explain
what the same load value means relative to each system's capacity.

The learner reported that they could not recall the model. This is a retrieval
failure at a newly introduced learning edge, not evidence that earlier process
and memory skills were all lost: the comparison had not yet been attempted in
the previous session.

## Foundation: CPUs as execution slots

For the simplified CPU-only case, treat each logical CPU as one execution slot:

```text
4 logical CPUs, load about 4       4 logical CPUs, load about 8

CPU 1: [task]                      CPU 1: [task]   waiting: [task]
CPU 2: [task]                      CPU 2: [task]            [task]
CPU 3: [task]                      CPU 3: [task]            [task]
CPU 4: [task]                      CPU 4: [task]            [task]

capacity roughly matched          demand roughly twice capacity
```

A useful first comparison is:

$$
\text{load per logical CPU} = \frac{\text{load average}}{\text{logical CPU count}}
$$

- Near `1`: demand roughly matches CPU capacity.
- Greater than `1`: some CPU-demanding work is likely waiting.
- Less than `1`: some CPU capacity is available in this simplified model.

Therefore, a steady load of `8.00` means roughly twice the CPU capacity on a
four-CPU system, but only half the CPU capacity on a sixteen-CPU system.

This is a capacity model, not an exact reconstruction of an instant. Load
average is smoothed over time. Linux also counts tasks in uninterruptible sleep,
often while waiting on I/O; that caveat will be added after the CPU-only model
is secure.

## Trend retrieval and I/O caveat

Linux displays load averages newest to oldest:

```text
displayed:       1 minute   5 minutes   15 minutes
read as trend:  oldest ---------------------> newest
```

To reconstruct a trend, label the values from left to right but read their
movement from right to left. After two reversed attempts, the learner correctly
rewrote `1.50 3.00 6.00` chronologically as `6.00 -> 3.00 -> 1.50`, then
correctly identified falling demand and the older `6.00` value as above the
capacity of a four-CPU system.

Linux load also includes both runnable tasks and tasks in uninterruptible sleep
(state `D`), commonly while waiting for I/O. Therefore high load is not by
itself proof of high CPU utilization. Given high load, 75% CPU idle, and many
`D` tasks, the learner correctly chose I/O/storage as the first investigation.

## Live Ubuntu VM snapshot

The learner ran the following read-only commands on `ubuntu-desktop`:

```text
$ nproc
2

$ uptime
16:50:09 up 35 min, 2 users, load average: 0.00, 0.00, 0.00
```

This snapshot shows no evidence of load pressure relative to two logical CPUs.
The displayed zeros mean the smoothed values were close enough to zero to round
to `0.00`; they do not prove that no task ran during those periods. The learner
correctly rejected a CPU-queue diagnosis but initially described demand as
nonexistent and justified the conclusion only by separating load from CPU
utilization.

## Bounded CPU-load experiment

The first bounded `yes` job had reached its 90-second timeout before a useful
active snapshot was captured. Its `Exit 124` status showed that `timeout`
expired as designed, so no cleanup was needed. A timing-controlled retry used:

```bash
timeout 60s yes > /dev/null & sleep 20; uptime
```

The command started one continuously runnable task, waited 20 seconds, and
then reported:

```text
load average: 0.29, 0.08, 0.04
```

The learner correctly reordered the values as `0.04 -> 0.08 -> 0.29` and
identified rising demand. They did not yet know why the one-minute average had
not jumped directly to `1.00`.

Load averages are exponentially smoothed. In a simplified continuous model,
if the starting load is zero and one task becomes continuously runnable, the
one-minute response after $t$ seconds is approximately:

$$
L_1(t) = 1 - e^{-t/60}
$$

After 20 seconds:

$$
L_1(20) = 1 - e^{-20/60} \approx 0.283
$$

The observed `0.29` is close to this prediction. The one-minute value moves
toward `1.00` rather than jumping there; the five- and fifteen-minute values
respond more slowly.

Queue interpretation and utilization remain separate:

$$
\text{capacity ratio} \approx
\frac{\text{CPU-related load}}{\text{logical CPU count}}
$$

Here, `0.29` was far below the two-CPU capacity, so it provided no evidence of
a CPU queue. The fact that load is not a utilization percentage explains why
`0.29` must not be read as `29% CPU`; it is not, by itself, the reason there was
no queue.

## Decay after the workload ended

A fresh job-table check reported:

```text
[1]+ 5330 Exit 124  timeout 60s yes > /dev/null
```

The bounded workload had expired, leaving nothing to clean up. The next
snapshot was:

```text
load average: 0.00, 0.07, 0.06
```

The one-minute value had decayed to a number that displayed as `0.00`, while
the longer averages retained evidence of recent demand. The learner correctly
identified falling demand, rounding near zero, longer-window memory of the
recent task, and no current pressure relative to two CPUs. This completed the
prediction-observation-explanation cycle for load smoothing.

## Separating runnable demand from blocked work

A four-second read-only observation with `vmstat -y 1 4` reported `r=0`,
`b=0`, CPU idle between 98% and 100%, and `wa=0` in every row. After the field
meanings were taught directly, the learner correctly diagnosed two unfamiliar
counterexamples:

```text
r=5  b=0  id=0   wa=0   -> CPU pressure and a runnable backlog
r=0  b=4  id=80  wa=20  -> blocked I/O pressure, not CPU saturation
```

The operational relationship is:

```text
load average -> smoothed history of runnable plus uninterruptible demand
vmstat r      -> runnable tasks in the sampled interval
vmstat b      -> blocked tasks in uninterruptible sleep
CPU id/wa     -> whether CPU capacity is busy or idle while I/O completes
```

The learner can now use the evidence together instead of treating a high load
number as proof of high CPU utilization.

## Spaced review: swap occupancy versus activity

From the live `vmstat` rows, the learner correctly recognized that `si=0` and
`so=0` meant no observed swap transfers. Teaching repaired two details:
`swpd=0` described occupancy, and swap transfers pages rather than whole tasks.

On a fresh mapping example, the learner correctly inferred that page B had
moved from RAM to swap when the mapped set stayed `A B C D`, the resident set
changed from `A B C` to `A C`, and swap gained B. They correctly held VIRT
constant and decreased RSS.

Occupied swap does not by itself prove current pressure. A possible timeline is:

```text
earlier pressure -> a cold page moves to swap
pressure ends    -> RAM becomes available again
page stays cold  -> it remains in swap because nothing needs it
current sample   -> swpd > 0, but si = 0 and so = 0
```

Given `swpd=512 MiB`, zero transfer activity for several minutes, and 3 GiB
available RAM, the learner correctly diagnosed no evidence of current memory
pressure. The snapshot cannot establish whether earlier pressure occurred.

## Spaced review: free versus available RAM

Given 300 MiB free, 2.4 GiB in `buff/cache`, and 2.3 GiB available, the learner
correctly recognized that reclaimable cache can supply applications and that
low `free` alone does not prove exhaustion. They initially repeated the model
of borrowing from `available` as though it were a separate pool.

After a physical-RAM diagram, they correctly reconstructed that `available` is
an estimate spanning unused RAM plus reclaimable occupied memory. They also
correctly rejected adding `free + buff/cache + available`, because doing so
would double-count memory. This was successful guided repair; re-test the
subset relationship after spacing before raising mastery.

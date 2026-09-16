# Memory and load notes — 2026-09-16

## Residency direction

When virtual mappings stay fixed:

```text
RAM -> swap: VIRT unchanged, RES decreases
swap -> RAM: VIRT unchanged, RES increases
```

## Swap occupancy and activity

```text
swpd    capacity currently occupied in swap
si      swap -> RAM transfer rate
so      RAM -> swap transfer rate
```

Occupied swap can be idle, so nonzero `swpd` does not imply current transfer
activity. Likewise, a single nonzero transfer interval does not alone prove a
current memory shortage.

## Free and available RAM

`available` is an estimate within existing physical RAM:

$$
M_{\text{available}} \approx M_{\text{free}} + M_{\text{reclaimable}}
$$

```text
Existing physical RAM
[needed now] [reclaimable cache] [unused]
             \________________________/
                  contributes to
                    available
```

It is not a separate pool and does not add capacity beyond total RAM.

## Per-process RSS and shared blocks

If A has a private resident block of size $P_A$, B has one of size $P_B$, and
both map the same resident shared block $S$:

$$
\mathrm{RSS}_A = P_A + S
$$

$$
\mathrm{RSS}_B = P_B + S
$$

$$
\mathrm{RSS}_A + \mathrm{RSS}_B = P_A + P_B + 2S
$$

The distinct physical total for these blocks is:

$$
M_{\text{physical}} = P_A + P_B + S
$$

`SHR` is already inside `RES` and identifies memory that may be shareable. A
single row does not prove another process currently shares every byte in SHR.

## Load average foundation

Linux load average summarizes tasks that are runnable plus tasks in
uninterruptible sleep. The three values are exponentially smoothed views over
approximately 1, 5, and 15 minutes:

```text
load average:  one-minute, five-minute, fifteen-minute
```

Compare load with CPU capacity, but do not treat it as CPU utilization: tasks
waiting uninterruptibly, commonly for I/O, also contribute.

Next retrieval:

```text
Both systems have load 8.00.
A has 4 logical CPUs; B has 16 logical CPUs.
Which has greater demand relative to CPU capacity, and what can be inferred?
```

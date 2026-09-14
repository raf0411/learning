# Process memory — 2026-09-14

## Session aim

Interpret changes in `VIRT`, `RES`/RSS, and `SHR` using a small, controlled
Ubuntu experiment. This worksheet covers the map/write/unmap procedure;
actual performance evidence is kept in the session record.

## Opening prediction

In a simplified example, a process starts with:

```text
VIRT = 120 MiB
RES  =  24 MiB
```

Another 8 MiB of its already-mapped memory becomes resident in RAM.
No mappings are added or removed, and nothing else changes.

Predict the new `VIRT` and `RES`, and explain your reasoning before testing.

## Refresher: addresses and residency

`VIRT` measures the process's virtual address ranges in use or reserved.
`RES` measures the portion currently resident in physical RAM. Becoming
resident does not remove an address range from the process.

In this simplified diagram, each letter represents one equal-sized mapped page:

```text
Mapped pages:          [A] [B] [C] [D] [E] [F]   VIRT: 6 pages
Resident before:       [A] [B]                   RES:  2 pages
Resident after C loads:[A] [B] [C]               RES:  3 pages
```

Page C was already included in the mapping count. Its residency changes;
the mapping count does not.

The opening example therefore gives:

$$
\mathrm{VIRT}_{\mathrm{after}} = 120\,\mathrm{MiB}
$$

$$
\mathrm{RES}_{\mathrm{after}} = (24 + 8)\,\mathrm{MiB} = 32\,\mathrm{MiB}
$$

Reference: [upstream top manual, VIRT and RES fields](https://man7.org/linux/man-pages/man1/top.1.html).

## Read-only preparation

Use the Ubuntu lab machine and identify whether it is the VM or physical
server. Submit each command separately:

```bash
free -h
```

```bash
getconf PAGESIZE
```

```bash
python3 --version
```

## Planned observation sequence

```text
baseline -> map a small region -> write to its pages -> inspect changes
```

Use a 16 MiB region for the upcoming mapping experiment on the physical Ubuntu
home server. Before running the mapping step, predict how reserving the region
without making its pages resident will affect `VIRT` and `RES`.

## Lab step 1: map without touching

The simplified prediction is an increase of 16 MiB in `VIRT`, with unchanged
`RES`. Absolute totals require a baseline measurement.

Start a fresh interactive Python process on Ubuntu:

```bash
python3
```

At its `>>>` prompt, submit these Python statements in order, one line at a
time. The two `ps` calls inspect this same Python process before and after
creating a private anonymous mapping.

```python
import mmap, os
size = 16 * 1024 * 1024
flags = mmap.MAP_PRIVATE | mmap.MAP_ANONYMOUS
_ = os.system(f"ps -p {os.getpid()} -o pid,vsz,rss")
region = mmap.mmap(-1, size, flags=flags)
_ = os.system(f"ps -p {os.getpid()} -o pid,vsz,rss")
```

`ps` labels virtual size `VSZ` and resident size `RSS`, both in KiB.

$$
16\,\mathrm{MiB} = 16 \times 1024\,\mathrm{KiB} = 16384\,\mathrm{KiB}
$$

The measurements cover the whole interpreter, so small unrelated changes may
accompany the mapping. Compare actual observations before drawing conclusions.
This step changes only the disposable Python process's memory. Keep it open
for the next step; `exit()` ends it and releases the mapping if stopping early.

References: [Python mmap documentation](https://docs.python.org/3.12/library/mmap.html)
and [ps field definitions](https://man7.org/linux/man-pages/man1/ps.1.html).

## Lab step 2: make half the mapping resident

In the same Python process, predict the change before writing into the first
half of the existing mapping:

```python
region[:size // 2] = b"x" * (size // 2)
_ = os.system(f"ps -p {os.getpid()} -o pid,vsz,rss")
```

The mapping remains the same size. The expected resident increase attributable
to the region is 8 MiB. Python also creates a temporary byte string to perform
the assignment, so assess actual measurements rather than assuming the whole
interpreter's accounting is perfectly constant.

## Lab step 3: remove the mapping and finish

Predict how removing the entire region affects virtual size and residency,
then submit these statements separately in the same interpreter:

```python
region.close()
_ = os.system(f"ps -p {os.getpid()} -o pid,vsz,rss")
exit()
```

## What the comparison means

These are idealized changes attributable to the lab region alone:

| Operation | Virtual size change | Resident size change |
|---|---:|---:|
| Map 16 MiB without touching | +16 MiB | 0 |
| Write into the first 8 MiB | 0 | +8 MiB |
| Remove the whole mapping | -16 MiB | -8 MiB |

Compare the same process across measurements. If the PID changes, obtain that
new process's own baseline before calculating a before/after difference.

## Shared resident pages: why adding RSS can double-count

RSS is a measurement for a process, not a separate physical-memory channel.
The same physical pages can be mapped into more than one process and counted
in each one's RSS.

Consider this simplified example of three distinct blocks in physical RAM:

```text
[A-only: 2 MiB]   [Shared: 4 MiB]   [B-only: 2 MiB]

Process A counts:  its 2 MiB + the shared 4 MiB = RSS 6 MiB
Process B counts:  its 2 MiB + the shared 4 MiB = RSS 6 MiB
```

There is only one physical copy of the shared block in this example:

$$
\mathrm{Distinct\ physical\ memory} = 2 + 4 + 2 = 8\,\mathrm{MiB}
$$

$$
\mathrm{Sum\ of\ RSS} = (2 + 4) + (2 + 4) = 12\,\mathrm{MiB}
$$

The sum counts the same shared 4 MiB twice. Two RSS values alone do not tell
us how much their underlying physical memory overlaps. These numbers describe
a teaching example, not measured sharing on the server.

## Next session's opening check

Using the three blocks above, process A exits while B continues using the
shared block. Which block can be released, and which blocks must remain for B?

This exercise was not attempted before the session ended. Explain the physical
blocks before calculating any total; the answer is intentionally left open.

Historical performance evidence and machine output belong in the
[session record](../sessions/2026-09-14.md).

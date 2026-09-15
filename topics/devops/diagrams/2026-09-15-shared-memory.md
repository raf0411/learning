# Process and system memory — 2026-09-15

## Session focus

Reason about shared physical RAM, connect it to RSS/RES and SHR, distinguish
mapping from residency, and interpret whole-system free/available RAM. This
worksheet supports the lesson; assessed performance belongs in the session
record.

## Opening retrieval

This is a simplified teaching example, not a measurement from the server.
Consider only the three blocks below. All are currently resident in RAM.

```text
Physical RAM block       Used by
------------------       -------
Private A: 2 MiB          A only
Shared:   4 MiB           A and B
Private B: 2 MiB          B only
```

The shared block is one physical block that both processes use.

Process A exits. Process B continues using its existing blocks.

1. Which block can be released?
2. Which blocks must remain for B, and why?

## Explanation: users versus physical copies

When A exits, its private 2 MiB can be released. B still needs its own private
2 MiB and the entire shared 4 MiB block. The shared block is not divided into
an A-owned half and a B-owned half.

```text
Process A ----+
              +----> [one physical 4 MiB block]
Process B ----+
```

Before A exits, the three physical blocks occupy:

$$
M_{\text{physical}} = 2 + 4 + 2 = 8\ \text{MiB}
$$

Each process's RSS includes its private resident block and the same shared
resident block:

$$
\mathrm{RSS}_A = 2 + 4 = 6\ \text{MiB}
$$

$$
\mathrm{RSS}_B = 2 + 4 = 6\ \text{MiB}
$$

The sum of the reports is 12 MiB because it counts the same shared 4 MiB twice.
It does not establish that there are 12 MiB of distinct physical blocks.

## Smaller example: count blocks, not users

| Physical block | Size | Who uses it? |
|---|---:|---|
| X | 1 MiB | A |
| Y | 3 MiB | A and B |
| Z | 1 MiB | B |

$$
M_{\text{physical}} = 1 + 3 + 1 = 5\ \text{MiB}
$$

Adding C as another user of the exact same Y block does not enlarge Y or create
another physical copy. The number of users changes; the block remains 3 MiB.
All totals here concern only the illustrated blocks, ignoring other memory.

## Connecting the picture to top

- `RES` reports resident process memory, including shared resident pages.
- `SHR` reports a portion already included in `RES`: resident memory that may
  also be used by other processes.
- Do not add `RES` and `SHR` to calculate resident memory.
- `SHR` alone does not prove that another process currently uses every byte
  counted there, or identify which physical pages two particular rows share.

```text
RES [ other resident memory | SHR ]
```

Read-only observation to run in the Ubuntu terminal:

```bash
top -b -n 1 -e k -p "$$"
```

This prints one batch snapshot filtered to the current shell's PID (`$$`),
with process-memory columns expressed in KiB.

The observed row reported `RES = 5716 KiB` and `SHR = 3940 KiB`. The resident
amount is 5716 KiB; 3940 KiB is already included within it. Adding the two
columns would count the SHR portion twice. The actual command output and
learner interpretation are recorded in [today's session](../sessions/2026-09-15.md).

Reference: [top manual: memory fields and command options](https://man7.org/linux/man-pages/man1/top.1.html).

## Mapping versus residency

Resident means currently in RAM, not free or waiting to be used. VIRT includes
the process's mapped virtual memory whether or not its pages are resident.
A resident page is still represented in the process's mappings.

```text
Before:
Mapped pages (VIRT): A B C D
Pages in RAM (RES):  A   C

B enters RAM; mappings do not change:
Mapped pages (VIRT): A B C D
Pages in RAM (RES):  A B C
```

VIRT stays unchanged and RES increases in this simplified example. It is not
a new live experiment.

## Whole-system free versus available RAM

`free -h` observes system memory. Its free column describes unused RAM;
buff/cache includes buffers and caches, some of which can be reclaimed;
available estimates memory that applications could use without swapping.
Available includes free RAM and suitable reclaimable memory, with kernel
allowances. It is not a separate region to add to free or buff/cache.

A cache keeps copies of file data in RAM to make later reads faster.
For a cached copy that matches the original file saved on disk:

```text
Disk                         RAM
[original file] --read--> [cached copy]
      stays               can be discarded
```

- Reclaim RAM: make occupied RAM usable for other work, for example by
  discarding a suitable cached copy.
- Reload data: read the original file data from disk into RAM again.
- Available capacity describes how much RAM room can be supplied; it is not
  the source of the file's contents.
- RAM is volatile: it loses its contents when power is removed. Disk storage
  ordinarily retains saved data without power.

This example depends on an up-to-date saved disk copy. Do not assume every
piece of data in RAM already has such a copy.

Reference: [free manual](https://man7.org/linux/man-pages/man1/free.1.html).

Available describes capacity within existing RAM. For example, an estimate
of 5 GiB available already includes any currently free 200 MiB; the two values
are not added to obtain the available amount. Those numbers are a hypothetical
teaching scenario, not another server measurement.

```text
Existing RAM:
[needed by current work] [reclaimable cache] [free]
                         \___ contributes to ___/
                              available
```

## Swap and residency direction

Some application data has no saved file copy that can simply be re-read.
For disk-backed swap, Linux can preserve suitable page data in the swap area
before repurposing the physical RAM page. If the process needs that data
again, Linux can load it back into RAM.

```text
Swap out: RAM -> swap file, then release the physical RAM page
Swap in:  swap file -> RAM
```

Resident means currently in physical RAM. In a simplified example where the
virtual mapping remains and nothing else changes:

| Movement completed | VIRT | RES |
|---|---|---|
| Page leaves RAM for swap | Unchanged | Decreases |
| Page returns from swap to RAM | Unchanged | Increases |

Writing a copy to swap alone is not the same as the page having left RAM;
the first row describes the stage where the page is no longer resident.

```text
Before B leaves RAM:
Mapped: A B C D
In RAM: A B C

After B leaves RAM for swap:
Mapped: A B C D
In RAM: A   C
```

Read-only swap-area inspection:

```bash
swapon --show
```

The actual swap-file observation is recorded in
[the session](../sessions/2026-09-15.md). No swap configuration was changed.

## Swap occupancy versus activity

- `swapon --show` reports active swap areas and their occupied capacity.
- `vmstat` si reports swap-to-RAM transfer per second.
- `vmstat` so reports RAM-to-swap transfer per second.

The following observation was assigned but no output was supplied before the
session ended:

```bash
vmstat -y 1 3
```

This requests three updates at one-second intervals; -y skips the initial
report containing since-boot averages. Interpret the actual si/so output over
its observation window. A prior zero-used-swap snapshot does not establish
later transfer rates.

References: [Linux memory concepts](https://docs.kernel.org/admin-guide/mm/concepts.html),
[swapon manual](https://man7.org/linux/man-pages/man8/swapon.8.html), and
[vmstat manual](https://man7.org/linux/man-pages/man8/vmstat.8.html).

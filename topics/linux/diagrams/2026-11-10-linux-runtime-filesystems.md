# Linux runtime filesystem interfaces — 2026-11-10

## `/dev` and `/dev/null`

`/dev` exposes device interfaces as filesystem entries. The learner observed:

```text
file /dev/null
/dev/null: character special (1/3)
```

`/dev/null` is a character device, not a regular data file. Reads immediately
reach end-of-file; writes are accepted and discarded. The learner correctly
predicted `wc -c < /dev/null` would receive zero bytes, and actual output was
`0`. Writing `discarded` returned status 0.

## Standard-stream application

Using a verified missing pathname:

```text
ls missing > /dev/null
    stdout -> discarded
    stderr -> terminal diagnostic
    status -> 2

ls missing 2> /dev/null
    stdout -> terminal (no normal output in this failure)
    stderr -> discarded
    status -> 2
```

The learner predicted the visible diagnostic correctly after spacing. Hiding a
diagnostic does not convert command failure into success; both commands retained
status 2.

## Relationship to other runtime interfaces

```text
/dev    device interfaces, including pseudo-devices such as /dev/null
/proc   process and kernel information exposed as files
/sys    kernel device/object model and attributes
/run    volatile runtime state for the current boot
```

These paths look file-like so ordinary tools can inspect many kernel or runtime
interfaces, but their contents are not all ordinary stored disk files.

## Observed `/sys` network objects

The VM exposed two symbolic links under `/sys/class/net`:

```text
enp0s8 -> ../../devices/pci0000:00/0000:00:08.0/net/enp0s8
lo      -> ../../devices/virtual/net/lo
```

Resolved from the links' containing directory, these targets lead beneath
`/sys/devices`. `enp0s8` is associated with the VM's PCI device branch; `lo`
belongs to the virtual-device branch. The learner identified the virtual path
correctly but needed the PCI interface name made explicit.

Reading through the class links produced current kernel attributes:

```text
/sys/class/net/enp0s8/operstate  -> up
/sys/class/net/lo/operstate      -> unknown
```

`unknown` is an actual kernel operational-state value and does not alone prove
that loopback is broken. Loopback does not have the same physical carrier model
as the PCI-associated interface.

## Observed `/run` hierarchy

```text
/run                 drwxr-xr-x  root:root
└── user             drwxr-xr-x  root:root
    └── 1000         drwx------  raf_0411:raf_0411
```

UID 1000 is the learner's numeric user identity. The per-user directory's mode
`700` grants its owner full access and gives group/other no ordinary mode-bit
access.

`findmnt -T /run` reported source and filesystem type `tmpfs`. This establishes
that `/run` is temporary current-boot storage rather than an ordinary persistent
disk filesystem. Visible mount options included `rw`, `nosuid`, `nodev`, and a
size limit; the terminal output truncated the remainder, so no additional
option values are claimed.

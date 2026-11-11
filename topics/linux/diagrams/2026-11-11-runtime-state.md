# Configuration and runtime state — 2026-11-11

```text
/etc                         /run
persistent configuration     temporary runtime state
         |                            ^
         v                            |
    service starts --------> creates current runtime entries
```

- `/etc` holds system configuration intended to persist across reboots.
- `/run` holds runtime state. Services recreate the entries they need after
  boot; yesterday's VM inspection identified `/run` as `tmpfs`.
- A PID file records a process ID. Its existence alone does not prove that the
  process is still running.
- A Unix-domain socket is a local communication endpoint, rather than an
  ordinary document to read with `cat`.

## Observed today

The learner's Ubuntu VM showed both `/etc` and `/run` owned by `root:root`
with mode `drwxr-xr-x`. These shared permissions do not explain their different
purposes or lifetimes.

Further inspection confirmed `snapd.socket` as a socket (`s`) and `sshd.pid`
as a regular file (`-`). The PID record contained `1401`; live `ps` and
`/proc/1401/status` observations agreed that this was `sshd` at inspection time.

## Records do not assign identity

```text
Kernel assigns process PID 1401
             |
             v
Service writes "1401" into its PID file

Hypothetical edit of file to "9999":
  actual process PID stays 1401
  tool trusting file tries PID 9999
```

`/proc` exposes kernel-provided views. A service-written record under `/run`
can be incorrect; changing that record does not reassign the actual PID.

## Creation mask: remove only the specified bits

```text
Class          Owner   Group   Others
Mask 022       0       2       2
Remove         nothing write   write

File request   rw-     rw-     rw-     666
File result    rw-     r--     r--     644

Dir request    rwx     rwx     rwx     777
Dir result     rwx     r-x     r-x     755
```

The mask does not add permissions. These standard creation examples assume
no default ACL changes the creation rules. A mask of 2 removes write only;
execute remains if it was requested. The VM experiment verified both results.

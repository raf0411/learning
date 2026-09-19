# Disk-space diagnosis — 2026-09-20

## Starting boundary

When asked how to investigate `No space left on device`, the learner suggested
Neofetch or Fastfetch because they can show a disk summary, while recognizing
that the summary would not explain much. Filesystem-level capacity and
path-level usage are new.

## First distinction

```text
storage device
    -> partition or logical volume
        -> filesystem
            -> mounted at a path
                -> directories and files consume its resources
```

Two questions require two different views:

```text
df: Which filesystem is full, and how much capacity remains?
du: Which directories or files account for space inside it?
```

The first observation targets only the filesystem containing `/`:

```bash
df -hT /
```

- `-h` displays human-readable sizes.
- `-T` includes the filesystem type.
- `/` selects the filesystem on which the root path resides.

Live output and interpretation will be added after observation.

## Live filesystem-capacity observation

The Ubuntu VM reported:

```text
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/sda2      ext4   29G  6.3G   21G  24% /
```

The learner correctly identified `/dev/sda2`, ext4, 6.3 GiB used, 24% use, and
21 GiB available. This snapshot does not support a nearly-full diagnosis for
the root filesystem.

## Path-level accounting

`du -sh "$HOME"` reported 17 MiB for `/home/raf_0411`. The learner correctly
distinguished that directory-tree total from the 6.3 GiB used across the whole
root filesystem.

Breaking the home tree down with:

```bash
du -h --max-depth=1 "$HOME" | sort -h
```

showed `.cache` as the largest immediate child at 16 MiB. The learner correctly
excluded the final 17 MiB line because it was the total for the home directory,
not another child.

The diagnostic narrowing pattern is:

```text
df -> identify the affected filesystem
du -> account for usage under paths on that filesystem
du at a smaller depth -> narrow toward the largest contributor
```

## Two filesystem capacity limits

Creating a regular file requires both kinds of filesystem resources:

```text
free data blocks -> store file content
free inode       -> represent the file and its metadata
```

Exhausting either resource can produce `No space left on device`. Byte capacity
and inode capacity must therefore be inspected separately.

## Live inode-capacity observation

The VM reported:

```text
Filesystem      Inodes  IUsed   IFree IUse% Mounted on
/dev/sda2      1900544 179438 1721106   10% /
```

The learner correctly read 10% inode use and contrasted it with 24% data-block
use. Teaching repaired the idea that `-hT` caused the percentage difference:
`-h` changes size formatting, `-T` adds filesystem type, and `-i` selects inode
counts instead of block capacity.

On an unfamiliar incident with 40% block use, 100% inode use, and a failed
`touch`, the learner correctly diagnosed inode exhaustion. An empty file still
requires an inode and a parent-directory entry.

## Targeting the affected mount and narrowing usage

For a failed write to `/var/log/myapp/events.log`, the learner correctly chose
the existing parent `/var/log/myapp` as the `df` target. This lets `df` resolve
the filesystem containing the failing path even when the intended file does
not exist:

```bash
df -hT /var/log/myapp
df -i /var/log/myapp
```

Given 98% block use and 12% inode use, the learner correctly selected block
capacity as the scarce resource and independently adapted the path-accounting
command:

```bash
du -h --max-depth=1 /var/log/myapp | sort -h
```

For real filesystem triage, adding `-x` keeps `du` on the starting filesystem
and prevents nested mounts from entering the accounting:

```bash
du -x -h --max-depth=1 /var/log/myapp | sort -h
```

## When `df` and `du` disagree

An open file has both a filesystem name and, while a process uses it, an open
file descriptor:

```text
process -> open descriptor -> inode -> allocated blocks
                              ^
directory name --------------|
```

Removing the directory name does not free the inode and blocks while the open
descriptor still references them:

```text
rm removes pathname -> du can no longer walk to the file
process keeps it open -> df still counts its allocated blocks
process closes it    -> inode and blocks can finally be released
```

This is one explanation for a nearly full result from `df` when visible `du`
totals are unexpectedly small. A common read-only investigation is:

```bash
sudo lsof +L1
```

The explanation was introduced at session end. The learner has not yet
answered the check that asks why the tools disagree and what event releases the
blocks.

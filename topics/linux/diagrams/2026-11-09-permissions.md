# File permissions — 2026-11-09

## Reading the observed practice-file mode

```text
-  rw-  rw-  r--
|   |    |    +-- other
|   |    +------- group
|   +------------ owner
+---------------- regular-file type marker
```

For regular-file mode bits: `r` is read, `w` is write, `x` is execute, and a
dash means the permission is absent. The mode describes permission bits;
reaching a file also depends on directory access. This lesson's experiment
uses a file the learner already accesses in a disposable directory.

## Selecting standard permission classes

```text
user matches owner? -- yes --> owner bits
        |
        no
        v
member of file's group? -- yes --> group bits
        |
        no
        v
     other bits
```

These classes are not added together. In the observed experiment, raf_0411
matched both owner and file-group membership; ownership selected the owner bits.

```text
Before change:   -rw-rw-r--
chmod u-w:      -r--rw-r--  -> test -w returned 1 (not writable)
chmod u+w:      -rw-rw-r--  -> restoration verified with ls -l
```

The group retained its write bit during the failed write-permission check.
This demonstrates that group write did not supplement missing owner write.

## Symbolic changes

`chmod` accepts a class, an operation, and permission letters:

```text
u = owner       g = group       o = other
+ = add         - = remove
r = read        w = write       x = execute
```

Class letters can be combined, such as `go` for group and other. The next
construction exercise changes only group/other permissions on the practice file.

Completed: learner independently used four separate removals for group/other
read/write and verified `-rw-------` on root.log. `chmod go-rw` combines those
removals; it was not required as the only valid solution.

## Directory permissions and the path to a file

```text
directory r -> list names inside
directory x -> traverse/access entries by name
directory w -> modify entries, ordinarily with x as well
```

File permissions and permissions on directories along its path are separate.

```text
/tmp/find-depth.cCOil3       owner rwx, group ---, other ---
  |
  +-- app                   owner rwx, group rwx, other r-x
       |
       +-- current.log
```

For an ordinary nonowner using the displayed standard permissions, the outer
directory blocks traversal regardless of app's more permissive bits. The owner
has traversal permission on both. Next experiment: remove only app's owner read
bit while keeping search permission, compare listing with reading a known file,
then restore and verify the original mode. Results are pending.

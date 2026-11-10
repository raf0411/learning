# Permission and group-ownership checkpoint — 2026-11-10

Use the Ubuntu terminal. This checkpoint creates a new disposable tree. Build
the repair commands yourself; do not use `sudo`, and do not remove anything.

## Create and inspect the fixture

Run each physical line separately:

```bash
perm_checkpoint=$(mktemp -d /tmp/permission-checkpoint.XXXXXX)
mkdir "$perm_checkpoint/shared"
printf 'checkpoint\n' > "$perm_checkpoint/shared/report.txt"
ls -ld "$perm_checkpoint" "$perm_checkpoint/shared" "$perm_checkpoint/shared/report.txt"
```

Paste the baseline command/output transcript:

```text
raf_0411@ubuntu-desktop:~$ perm_checkpoint=$(mktemp -d /tmp/permission-checkpoint.XXXXXX)
raf_0411@ubuntu-desktop:~$ mkdir "$perm_checkpoint/shared"
raf_0411@ubuntu-desktop:~$ printf 'checkpoint\n' > "$perm_checkpoint/shared/report.txt"
raf_0411@ubuntu-desktop:~$ ls -ld "$perm_checkpoint" "$perm_checkpoint/shared" "$perm_checkpoint/shared/report.txt"
drwx------ 3 raf_0411 raf_0411 60 Nov 10 11:04 /tmp/permission-checkpoint.UB244a
drwxrwxr-x 2 raf_0411 raf_0411 60 Nov 10 11:04 /tmp/permission-checkpoint.UB244a/shared
-rw-rw-r-- 1 raf_0411 raf_0411 11 Nov 10 11:04 /tmp/permission-checkpoint.UB244a/shared/report.txt
```

## Target access policy

Repair this tree so that:

- the group owner of the outer directory, `shared`, and `report.txt` is `users`;
- you can list, traverse, and modify entries in both directories;
- members of `users` can list and traverse both directories but cannot create
  or remove entries there;
- you can read and write `report.txt`;
- members of `users` can read `report.txt` but cannot write it;
- other users have no permissions on any of the three objects;
- `report.txt` still contains exactly `checkpoint`.

Derive the target modes before writing commands:

| Object             | Symbolic permission bits | Numeric mode |
| ------------------ | ------------------------ | -----------: |
| Outer directory    | rwxr-x---                |          750 |
| `shared` directory | rwxr-x---                |          750 |
| `report.txt`       | rw-r-----                |          640 |

## Plan and execute

Write the exact commands you intend to use. Every target must resolve beneath
`$perm_checkpoint`:

```bash
chmod 750 "$perm_checkpoint"
chmod 750 "$perm_checkpoint/shared"
chmod 640 "$perm_checkpoint/shared/report.txt"

chgrp users "$perm_checkpoint"
chgrp users "$perm_checkpoint/shared"
chgrp users "$perm_checkpoint/shared/report.txt"
```

Then run your plan and paste the complete transcript:

```text
raf_0411@ubuntu-desktop:~$ chmod 750 "$perm_checkpoint"
raf_0411@ubuntu-desktop:~$ chmod 750 "$perm_checkpoint/shared"
raf_0411@ubuntu-desktop:~$ chmod 640 "$perm_checkpoint/shared/report.txt"
raf_0411@ubuntu-desktop:~$ chgrp users "$perm_checkpoint"
raf_0411@ubuntu-desktop:~$ chgrp users "$perm_checkpoint/shared"
raf_0411@ubuntu-desktop:~$ chgrp users "$perm_checkpoint/shared/report.txt"
```

## Verify

Use fresh commands to prove all three group owners, all three modes, and the
unchanged file content. Record both commands and output:

```text
raf_0411@ubuntu-desktop:~$ ls -ld "$perm_checkpoint" "$perm_checkpoint/shared" "$perm_checkpoint/shared/report.txt"
drwxr-x--- 3 raf_0411 users 60 Nov 10 11:04 /tmp/permission-checkpoint.UB244a
drwxr-x--- 2 raf_0411 users 60 Nov 10 11:04 /tmp/permission-checkpoint.UB244a/shared
-rw-r----- 1 raf_0411 users 11 Nov 10 11:04 /tmp/permission-checkpoint.UB244a/shared/report.txt
raf_0411@ubuntu-desktop:~$ cat "$perm_checkpoint/shared/report.txt"
checkpoint
```

Tell the tutor when the worksheet is ready. Preserve any unsuccessful attempt
instead of replacing it; append a repair section if needed.
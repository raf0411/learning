# Shared workspace repair — 2026-11-11

Work in the Ubuntu VM. Write your plan and paste actual command/output evidence
here. Leave uncertain answers marked as uncertain; do not look up old solutions
on the first attempt. Tell the tutor when this worksheet is ready for review.

## Known identity

Already supplied by you; no need to retype:

```text
uid=1000(raf_0411) gid=1000(raf_0411) groups=1000(raf_0411),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),100(users),111(lpadmin),114(lxd)
```

## 1. Create and inspect the disposable fixture

This setup creates a unique directory under `/tmp`, one subdirectory, and a
text file. It changes permissions only on those new objects. No deletion or
privileged commands are needed. Run in the same Ubuntu terminal you will use
for the repair. The command below is ONE physical line.

```bash
access_lab=$(mktemp -d /tmp/access-review.XXXXXX) && mkdir "$access_lab/shared" && printf 'team draft\n' > "$access_lab/shared/note.txt" && chmod 700 "$access_lab" "$access_lab/shared" && chmod 600 "$access_lab/shared/note.txt" && printf 'Lab root: %s\n' "$access_lab" && ls -ld "$access_lab" "$access_lab/shared" "$access_lab/shared/note.txt" && cat "$access_lab/shared/note.txt"
```

If setup fails, stop and share the error. Do not reuse an old path or an empty
variable. Keep every repair target inside the printed lab root (including the
root itself); never change `/tmp` itself.

Paste the setup command and its actual output:

```text
raf_0411@ubuntu-desktop:~$ access_lab=$(mktemp -d /tmp/access-review.XXXXXX) && mkdir "$access_lab/shared" && printf 'team draft\n' > "$access_lab/shared/note.txt" && chmod 700 "$access_lab" "$access_lab/shared" && chmod 600 "$access_lab/shared/note.txt" && printf 'Lab root: %s\n' "$access_lab" && ls -ld "$access_lab" "$access_lab/shared" "$access_lab/shared/note.txt" && cat "$access_lab/shared/note.txt"
Lab root: /tmp/access-review.oKKoXN
drwx------ 3 raf_0411 raf_0411 60 Nov 11 13:11 /tmp/access-review.oKKoXN
drwx------ 2 raf_0411 raf_0411 60 Nov 11 13:11 /tmp/access-review.oKKoXN/shared
-rw------- 1 raf_0411 raf_0411 11 Nov 11 13:11 /tmp/access-review.oKKoXN/shared/note.txt
team draft
```

## 2. Plan the requested access

You own a workspace that other members of `users` should collaborate in.
Use standard owner/group/other permissions only.

- Keep yourself as the user owner of all three objects.
- Set the group owner of all three objects to `users`.
- Keep full owner access on both directories and owner read/write on the file.
- At the lab root, other members of `users` may traverse using known names,
  but may not list its names or add/remove entries there.
- In `shared`, other members of `users` may list names, traverse, and
  create/remove entries.
- For `note.txt`, other members of `users` may read and edit its contents,
  but nobody should have execute permission on the file.
- Give the other permission class no permissions on any of the three objects.
- Preserve the file's contents exactly.

Fill in the complete intended state BEFORE running repair commands:

| Object                   | User owner | Group owner | Symbolic permissions (9 characters) | Numeric mode |
| ------------------------ | ---------- | ----------- | ----------------------------------- | ------------ |
| Lab root (`$access_lab`) | raf_0411   | users       | rwx--x---                           | 710          |
| `shared` directory       | raf_0411   | users       | rwxrwx---                           | 770          |
| `shared/note.txt`        | raf_0411   | users       | rw-rw----                           | 660          |

Your proposed repair commands (one command per physical line):

```bash
chgrp users "$access_lab" "$access_lab/shared" "$access_lab/shared/note.txt"
chmod 710 "$access_lab"
chmod 770 "$access_lab/shared"
chmod 660 "$access_lab/shared/note.txt"
cat "$access_lab/shared/note.txt"
```

## 3. Execute, verify, and decide

Run your repair commands. Choose read-only verification commands that show
whether every requested owner, group, mode, and content requirement is met.
Record commands and outputs together in their actual order. Include failed
attempts and corrections if there are any.

```text
raf_0411@ubuntu-desktop:~$ chgrp users "$access_lab" "$access_lab/shared" "$access_lab/shared/note.txt"
raf_0411@ubuntu-desktop:~$ chmod 710 "$access_lab"
raf_0411@ubuntu-desktop:~$ chmod 770 "$access_lab/shared"
raf_0411@ubuntu-desktop:~$ chmod 660 "$access_lab/shared/note.txt"
raf_0411@ubuntu-desktop:~$ cat "$access_lab/shared/note.txt"
team draft
raf_0411@ubuntu-desktop:~$ ls -ld "$access_lab" "$access_lab/shared" "$access_lab/shared/note.txt"
drwx--x--- 3 raf_0411 users 60 Nov 11 13:11 /tmp/access-review.oKKoXN
drwxrwx--- 2 raf_0411 users 60 Nov 11 13:11 /tmp/access-review.oKKoXN/shared
-rw-rw---- 1 raf_0411 users 11 Nov 11 13:11 /tmp/access-review.oKKoXN/shared/note.txt
```

Compare your final evidence with each row of your plan and the content
requirement. Is the task complete? Name any remaining mismatch:

matched

Do not delete the fixture yet; keep it available for review.

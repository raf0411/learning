# Directory write versus file write — 2026-11-10

Continue in the same Ubuntu terminal with today's `find_lab` variable and
restored `app` permissions. This experiment uses a new disposable file.

## Original prediction — preserved

Assume `app` gives its owner `r-x` and `current.log` gives its owner `rw-`.

| Operation                       | Learner's original prediction  |
| ------------------------------- | ------------------------------ |
| Append to `current.log`         | yes — the `w` in `current.log` |
| Remove `current.log` from `app` | yes — the `x` in `app`         |

Tutor assessment before execution: the append prediction is correct. Search
(`x`) is needed to reach an entry, but removing its name also requires write
(`w`) on the containing directory. The experiment below tests both claims.

## Create and inspect a dedicated test file

Run each physical line separately:

```bash
printf 'baseline\n' > "${find_lab:?Practice variable is unset}/app/write-test.log"
ls -ld "$find_lab/app" "$find_lab/app/write-test.log"
```

Confirm before continuing that you own both entries, `app` gives its owner
`rwx`, and `write-test.log` gives its owner write permission. Paste the output:

```text
raf_0411@ubuntu-desktop:~$ printf 'baseline\n' > "${find_lab:?Practice variable is unset}/app/write-test.log"
raf_0411@ubuntu-desktop:~$ ls -ld "$find_lab/app" "$find_lab/app/write-test.log"
drwxrwxr-x 2 raf_0411 raf_0411 80 Nov 10 10:18 /tmp/directory-permissions.2gCTIy/app
-rw-rw-r-- 1 raf_0411 raf_0411  9 Nov 10 10:18 /tmp/directory-permissions.2gCTIy/app/write-test.log
```

## Remove directory write, test, and restore

Run each physical line separately. The attempted `rm` is expected to fail; the
failure leaves the disposable file present. Continue through restoration.

```bash
chmod u-w "$find_lab/app"
printf 'appended\n' >> "$find_lab/app/write-test.log"; printf 'append-status=%s\n' "$?"
rm "$find_lab/app/write-test.log"; printf 'remove-status=%s\n' "$?"
chmod u+w "$find_lab/app"
ls -ld "$find_lab/app" "$find_lab/app/write-test.log"
cat "$find_lab/app/write-test.log"
```

Paste the commands and output, including the restoration and final content:

```text
raf_0411@ubuntu-desktop:~$ chmod u-w "$find_lab/app"
raf_0411@ubuntu-desktop:~$ printf 'appended\n' >> "$find_lab/app/write-test.log"; printf 'append-status=%s\n' "$?"
append-status=0
raf_0411@ubuntu-desktop:~$ ^C
raf_0411@ubuntu-desktop:~$ rm "$find_lab/app/write-test.log"; printf 'remove-status=%s\n' "$?"
rm: cannot remove '/tmp/directory-permissions.2gCTIy/app/write-test.log': Permission denied
remove-status=1
raf_0411@ubuntu-desktop:~$ chmod u+w "$find_lab/app"
raf_0411@ubuntu-desktop:~$ ls -ld "$find_lab/app" "$find_lab/app/write-test.log"
drwxrwxr-x 2 raf_0411 raf_0411 80 Nov 10 10:18 /tmp/directory-permissions.2gCTIy/app
-rw-rw-r-- 1 raf_0411 raf_0411 18 Nov 10 10:22 /tmp/directory-permissions.2gCTIy/app/write-test.log
raf_0411@ubuntu-desktop:~$ cat "$find_lab/app/write-test.log"
baseline
appended
```

Do not change the original prediction. Tell the tutor when the note is ready.
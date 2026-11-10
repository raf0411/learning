# Privileged ownership change and restoration — 2026-11-10

Use the same Ubuntu terminal and today's disposable `write-test.log`. This lab
temporarily changes only that file's user/group ownership to `root:root`, then
restores `raf_0411:raf_0411`. It does not intentionally change the file's mode
or contents.

## Prediction — preserved

The learner predicted root as both owner and group after privileged `chown`.
The current mode had been forgotten; the latest verified mode was supplied:

| Field | Before | After `sudo chown root:root` |
|---|---|---|
| Mode | `-rw-r-----` (`640`) | `-rw-r-----` (`640`) |
| Owner | `raf_0411` | `root` |
| Group | `raf_0411` | `root` |

`chown` changes ownership fields. It does not inherently change mode bits.

## Inspect, change, and restore

Run each physical line separately. Confirm that the first listing matches the
baseline above. If it does not, stop and share the output before using `sudo`.

```bash
ls -l "${find_lab:?Practice variable is unset}/app/write-test.log"
sudo chown root:root "$find_lab/app/write-test.log"
ls -l "$find_lab/app/write-test.log"
sudo chown raf_0411:raf_0411 "$find_lab/app/write-test.log"
ls -l "$find_lab/app/write-test.log"
```

Paste the complete command/output transcript, including the final restoration:

```text
raf_0411@ubuntu-desktop:~$ ls -l "${find_lab:?Practice variable is unset}/app/write-test.log"
-rw-r----- 1 raf_0411 raf_0411 18 Nov 10 10:22 /tmp/directory-permissions.2gCTIy/app/write-test.log
raf_0411@ubuntu-desktop:~$ sudo chown root:root "$find_lab/app/write-test.log"
raf_0411@ubuntu-desktop:~$ ls -l "$find_lab/app/write-test.log"
-rw-r----- 1 root root 18 Nov 10 10:22 /tmp/directory-permissions.2gCTIy/app/write-test.log
raf_0411@ubuntu-desktop:~$ sudo chown raf_0411:raf_0411 "$find_lab/app/write-test.log"
raf_0411@ubuntu-desktop:~$ ls -l "$find_lab/app/write-test.log"
-rw-r----- 1 raf_0411 raf_0411 18 Nov 10 10:22 /tmp/directory-permissions.2gCTIy/app/write-test.log
```

Confirm that the middle listing proves the temporary ownership change and the
last listing proves restoration. Tell the tutor when the note is ready.

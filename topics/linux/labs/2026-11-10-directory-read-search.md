# Directory read versus search — 2026-11-10

Continue in the same Ubuntu terminal where `find_lab` is set. This resumes
yesterday's unattempted experiment using today's freshly created fixture.
If you switch terminals or restart the VM, stop and recheck the fixture first.

## Baseline — already supplied

```text
ls -ld "$find_lab" "$find_lab/app" "$find_lab/app/current.log"
drwx------ 3 raf_0411 raf_0411 60 Nov 10 10:00 /tmp/directory-permissions.2gCTIy
drwxrwxr-x 2 raf_0411 raf_0411 60 Nov 10 10:00 /tmp/directory-permissions.2gCTIy/app
-rw-rw-r-- 1 raf_0411 raf_0411  0 Nov 10 10:00 /tmp/directory-permissions.2gCTIy/app/current.log
```

You own both the directory and file. We will temporarily remove only the
directory owner's read permission, leaving its write and search permissions
in place. The file's permissions and contents stay unchanged. Restoration is
included below. Use your ordinary account without sudo.

## Predict before running

After `chmod u-r "$find_lab/app"`, predict success or failure. No written
explanation required.

| Operation                                         | Prediction |
| ------------------------------------------------- | ---------- |
| List names inside `app` using `ls`                | fail       |
| Read the known file `app/current.log` using `cat` | success    |

## Run and restore

Run each physical line separately. If an inspection fails, record it and
continue through restoration. If the first chmod fails, stop and share its error.

```bash
chmod u-r "${find_lab:?Practice variable is unset}/app"
ls "$find_lab/app"
cat "$find_lab/app/current.log"; printf 'read-status=%s\n' "$?"
chmod u+r "$find_lab/app"
ls -ld "$find_lab/app"
```

The `${find_lab:?...}` expression prevents the first change if the variable is
empty or unset. `current.log` is empty, so successful reading prints no file
content. The status printed immediately after `cat` distinguishes success (0)
from failure. Compare the final directory permissions with the baseline to
verify restoration.

Paste the actual commands and output, including restoration:

```text
raf_0411@ubuntu-desktop:~$ chmod u-r "${find_lab:?Practice variable is unset}/app"
raf_0411@ubuntu-desktop:~$ ls "$find_lab/app"
ls: cannot open directory '/tmp/directory-permissions.2gCTIy/app': Permission denied
raf_0411@ubuntu-desktop:~$ cat "$find_lab/app/current.log"; printf 'read-status=%s\n' "$?"
read-status=0
raf_0411@ubuntu-desktop:~$ chmod u+r "$find_lab/app"
raf_0411@ubuntu-desktop:~$ ls -ld "$find_lab/app"
drwxrwxr-x 2 raf_0411 raf_0411 60 Nov 10 10:00 /tmp/directory-permissions.2gCTIy/app
```

Keep your original predictions even if the results differ. Tell the tutor when
this note is ready.
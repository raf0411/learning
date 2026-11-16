# Run your script directly — 2026-11-16

## Goal

Launch your existing disposable web-check script using `./check-web.sh` instead of `bash check-web.sh`.

## How it works

Add this as the very first line, with no blank line before it:

```bash
#!/usr/bin/env bash
```

This shebang requests `/usr/bin/env`, which finds Bash using PATH. It selects the interpreter; it does not grant execute permission.

`./check-web.sh` explicitly names the file in the current directory. This avoids relying on your current directory being in PATH.

## 1. Inspect before modifying — Ubuntu

Locate your existing lab directory. The script's last recorded location was `/tmp/bash-practice.e6ofDY/check-web.sh`; check that it still exists.

From its directory, inspect your location, file permissions/ownership, and saved script. Confirm this is your own disposable regular script, not a symbolic link or unrelated file. If anything is unexpected, stop and show the tutor.

Record the actual inspection commands and output:

```text
raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ ls -la
total 4
drwx------  2 raf_0411 raf_0411  60 Nov 16 12:15 .
drwxrwxrwt 17 root     root     400 Nov 16 11:52 ..
-rw-rw-r--  1 raf_0411 raf_0411 234 Nov 16 12:12 check-web.sh

if [ -z "$1" ]; then
    printf 'Usage: bash check-web.sh URL\n' >&2
    exit 2
fi

printf 'Web check\n'
hostname

if curl -I --max-time 10 "$1"; then
   printf 'Request completed\n'
else
   printf 'Request failed\n' >&2
   exit 1
fi
```

## 2. Prepare direct execution

- Add the shebang as the first line. Keep all existing script logic.
- Use your earlier permission knowledge to add execute permission for the file's owner only, preserving every other permission. The scope is this one disposable script; do not use sudo or recursive changes. If it already has owner execute permission, no permission change is necessary.
- Inspect the resulting permissions and saved script.

Record your permission command (or explain why no change was needed), verification commands, and actual output:

```text
#!/usr/bin/env bash

if [ -z "$1" ]; then
    printf 'Usage: bash check-web.sh URL\n' >&2
    exit 2
fi

printf 'Web check\n'
hostname

if curl -I --max-time 10 "$1"; then
   printf 'Request completed\n'
else
   printf 'Request failed\n' >&2
   exit 1
fi
```

## 3. Launch directly

```bash
./check-web.sh https://example.org
```

Capture the status immediately using your practiced command. Record the actual execution and status output:

```text
raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ ./check-web.sh https://example.org
bash: ./check-web.sh: Permission denied
```

Stop and tell the tutor when ready. If a step fails, preserve its actual output and ask for a hint rather than broadening permissions.
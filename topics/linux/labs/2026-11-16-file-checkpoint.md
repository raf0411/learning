# Independent combination: check local files — 2026-11-16

## Goal

Build a small script using the ideas from today's work, without a supplied implementation. This is a checkpoint, not a speed test. If stuck, save your attempt and ask for a hint.

The script must only inspect paths and print messages. Do not delete files, change permissions, or use sudo.

## One new primitive

```bash
[ -f "$path" ]
```

This returns 0 if the pathname resolves to a regular file, nonzero otherwise. Directories do not pass. It does not test read permission. You may consult `help test` for documentation.

## 1. Create a safe fixture — Ubuntu

Run this supplied setup as one command. It creates a fresh directory containing one regular file with a space in its name and one subdirectory:

```bash
file_lab=$(mktemp -d /tmp/bash-files.XXXXXX) && cd "$file_lab" && printf 'sample\n' > 'daily report.txt' && mkdir archive && pwd
```

Actual directory:

/tmp/bash-files.MgxdUV

`missing.txt` is deliberately not created.

## 2. Write `check-files.sh`

Requirements:

- Accept pathnames as script arguments; preserve spaces within each argument.
- If the first argument is missing or empty, print a helpful usage message to standard error and exit with status 2 before processing paths.
- Check every supplied pathname, even if an earlier one fails.
- For each regular file, print `FILE: pathname` to standard output.
- For each non-regular or missing pathname, print `NOT FILE: pathname` to standard error.
- Return 0 if every supplied pathname passes; return 1 if any fails.
- Do not hardcode the fixture names into the script.

Do not add a hostname heading, counters, functions, or network commands. Try constructing the script from memory first. Documentation is allowed; record any examples or tutor hints you use so we can distinguish independent work from guided work.

Inspect and paste your actual saved script:

```bash
#! /usr/bin/env

status=0

for path in "$@"; do
    if [ -f "$path" ]; then
        printf 'FILE: %s\n' "$path"
    else
        printf 'NOT FILE: %s\n' "$path" >&2
        status=1
    fi
done

exit "$status"
```

References or hints used (write NONE if none):

NONE

## 3. Test the required behaviors

Run each test separately, capturing its exit status immediately before the next test. Record actual commands and output, not expected values.

### A. Regular file with a spaced pathname

```bash
bash check-files.sh 'daily report.txt'
```

Actual invocation/output and immediate status capture:

```text
TODO
```

### B. Directory, then regular file, then missing pathname

```bash
bash check-files.sh archive 'daily report.txt' missing.txt
```

Actual invocation/output and immediate status capture:

```text
raf_0411@ubuntu-desktop:/tmp/bash-files.MgxdUV$ bash check-files.sh archive 'daily report.txt' missing.txt
NOT FILE: archive
FILE: daily report.txt
NOT FILE: missing.txt
raf_0411@ubuntu-desktop:/tmp/bash-files.MgxdUV$ printf 'status=%s\n' "$?"
status=1
```

### C. No arguments

```bash
bash check-files.sh
```

Actual invocation/output and immediate status capture:

```text
raf_0411@ubuntu-desktop:/tmp/bash-files.MgxdUV$ printf 'status=%s\n' "$?"
status=0
```

Tell the tutor when ready. If any test fails, preserve the evidence; you can append a self-correction rather than replacing the earlier attempt.

## 4. Review and targeted repair

### Tutor feedback

- Independently constructed quoted argument iteration, the file-test conditional, correct stdout/stderr routing in the code, and a failure flag initialized before the loop and returned afterward.
- Test B confirms processing continued after a failure and preserved the spaced pathname; the immediate status capture recorded 1. The combined terminal output alone does not independently verify stream separation, but the redirections in the code are correct.
- The required missing/empty-first-argument guard is absent. With no arguments, the loop has no iterations and the unchanged status variable remains 0.
- The shebang names `env` but does not name an interpreter for it to launch. Explicit `bash check-files.sh` bypasses this problem; it does not verify direct execution.
- Test A is unrecorded. Test C records only the status-printing command, not the script invocation, so the transcript does not establish which command returned 0.

### Repair hints

Before the loop, test whether the first argument is an empty string. In that branch, print usage to stderr and stop the script with status 2. An assignment alone does not stop execution. Recall the earlier single-string empty test; do not substitute the whole argument list.

Complete the shebang so `env` selects Bash. No permission changes or direct-launch tests are needed here.

Preserve your original script and evidence above. Append your revised saved script below:

```bash
#! /usr/bin/env bash

status=0

if [ -z "$1" ]; then
    printf 'Usage: bash check-files.sh FILE [FILE ...]\n' >&2
    exit 2
fi

for path in "$@"; do
    if [ -f "$path" ]; then
        printf 'FILE: %s\n' "$path"
    else
        printf 'NOT FILE: %s\n' "$path" >&2
        status=1
    fi
done

exit "$status"
```

### Targeted verification

Run A (the regular file) and C (no arguments) using the revised script. Include each invocation, actual output, and immediate status capture. Also test an explicitly empty first argument followed by the valid file, to verify processing stops at the guard.

A — regular file:

```text
raf_0411@ubuntu-desktop:/tmp/bash-files.MgxdUV$ bash check-files.sh 'daily report.txt'
FILE: daily report.txt
raf_0411@ubuntu-desktop:/tmp/bash-files.MgxdUV$ printf 'status=%s\n' "$?"
status=0
```

C — no arguments:

```text
raf_0411@ubuntu-desktop:/tmp/bash-files.MgxdUV$ bash check-files.sh
Usage: bash check-files.sh FILE [FILE ...]
raf_0411@ubuntu-desktop:/tmp/bash-files.MgxdUV$ printf 'status=%s\n' "$?"
status=2
```

D — empty first argument followed by a valid file:

```bash
bash check-files.sh '' 'daily report.txt'
```

Actual invocation/output and immediate status capture:

```text
raf_0411@ubuntu-desktop:/tmp/bash-files.MgxdUV$ bash check-files.sh '' 'daily report.txt'
Usage: bash check-files.sh FILE [FILE ...]
raf_0411@ubuntu-desktop:/tmp/bash-files.MgxdUV$ printf 'status=%s\n' "$?"
status=2
```
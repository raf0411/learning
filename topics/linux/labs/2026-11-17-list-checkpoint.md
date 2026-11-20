# Check a supplied pathname list — 2026-11-17

## Goal

Combine existing Bash skills without a supplied implementation. No new syntax is required. This is a reduced-scaffolding checkpoint, not a speed test.

Work in Ubuntu. Use a fresh disposable fixture; leave previous scripts unchanged. The checker must only inspect paths and print messages. No sudo, deletion, or permission changes.

## 1. Fixture

Run this supplied setup as one physical command:

```bash
checkpoint_lab=$(mktemp -d /tmp/bash-list-checkpoint.XXXXXX) && cd "$checkpoint_lab" && printf 'sample\n' > 'daily report.txt' && mkdir archive && printf '%s\n' 'daily report.txt' > 'good paths.txt' && printf '%s\n' archive 'daily report.txt' > 'mixed paths.txt' && pwd
```

Actual directory/output:

```text
/tmp/bash-list-checkpoint.BShRQr
```

`absent-list.txt` is deliberately not created. Every fixture list line ends with a newline.

## 2. Write `check-list-arg.sh`

Requirements:

- Use the first script argument as the input-list pathname. Preserve spaces in it. Handling extra script arguments is outside this checkpoint's scope.
- If that argument is missing or empty, print usage to stderr and exit 2 before processing.
- Reject an input list that fails either the regular-file precheck or the readability precheck. Print an accurate diagnostic to stderr and exit 2.
- Read the selected list line by line, preserving whitespace and backslashes.
- Use a function to check each listed pathname. Either previously practiced function design is acceptable; understand whether it returns a test result or updates the outer failure flag.
- Print `FILE: pathname` to stdout for a regular file and `NOT FILE: pathname` to stderr otherwise.
- Check every line. Exit 1 if any listed pathname fails, even when the final one passes. Exit 0 if all listed pathnames pass.
- Interpret listed relative pathnames relative to the script process's working directory. Do not add list-directory-relative resolution.
- Do not hardcode fixture names, add counters, or add network commands.

Scope: the prechecks handle ordinary invalid input but do not guarantee later opening/reading succeeds. Concurrent file changes, read errors, filenames containing newlines, and unterminated final lines remain deferred. An empty readable regular list has no failing entries and may return 0.

Try from memory first. Documentation and prior notes are allowed; record what you use. If stuck, preserve your attempt and ask for a hint.

Actual saved script:

```bash
#!/usr/bin/env bash

status=0
is_listed_pathname_failed=1

if [ -z "$1" ]; then
    printf 'Usage: bash check-list-arg.sh FILE [FILE ...]\n' >&2
    exit 2
fi

check_file() { 
    [ -f "$1" ]
}

for path in "$@"; do 
    if check_file "$path"; then
        printf 'FILE: %s\n' "$path"
    else
        printf 'NOT FILE: %s\n' "$path" >&2
        is_listed_pathname_failed=0
    fi

if [ "$is_listed_pathname_failed" -eq 0  ]; then
    status=1
fi

exit "$status"
```

References/hints used (NONE if none):

how to compare a variable to a number (i google search this)

## 3. Verify the behavior

Construct each invocation yourself. Include actual commands, output, and immediate exit-status capture. Do not replace failed evidence with a correction; append corrected runs.

### A. The all-regular-file list

```text
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ bash check-list-arg.sh 'daily-report.txt' 'good paths.txt' 'mixed paths.txt'
NOT FILE: daily-report.txt
FILE: good paths.txt
FILE: mixed paths.txt
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ printf 'status=%s\n' "$?"
status=1
```

### B. The list with a directory first and a regular file last

```text
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ bash check-list-arg.sh archive 'good paths.txt'
NOT FILE: archive
FILE: good paths.txt
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ printf 'status=%s\n' "$?"
status=1
```

### C. A missing input list

```text
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ bash check-list-arg.sh
Usage: bash check-list-arg.sh FILE [FILE ...]
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ printf 'status=%s\n' "$?"
status=2
```

### D. No script arguments

```text
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ bash check-list-arg.sh none.txt
NOT FILE: none.txt
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ printf 'status=%s\n' "$?"
status=1
```

### E. A directory supplied as the input list

```text
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ bash check-list-arg.sh archive
NOT FILE: archive
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ printf 'status=%s\n' "$?"
status=1
```

Tell the tutor when ready. Tests C and E concern the list itself; test B concerns entries inside an available list. Keep that distinction visible in your diagnostics.

---

## 4. Attempt 2 (attempt 1 above is preserved as evidence)

Tutor feedback on attempt 1 (2026-11-21):

- Attempt 1 checks each **argument** as a pathname (the 11-16 design). This checkpoint passes **one argument naming a list file**, and checks each **line inside** that file.
- The saved script has no `done`. Bash refuses to run a script like that (`syntax error: unexpected end of file`), so the outputs above came from a different version of the file. This time, paste the real file with `cat check-list-arg.sh`.
- The runs recorded under C and D are swapped. Test A's "all regular" run returned status 1 without being flagged.

```text
bash check-list-arg.sh 'good paths.txt'
                        |
                        v   $1 = name of the LIST (precheck: regular? readable?)
               +-----------------+
               | good paths.txt  |   <- open it and read it one line at a time
               |-----------------|
               | daily report.txt|   <- each LINE is a pathname to check
               +-----------------+
                        |
                        v
               FILE: daily report.txt     exit 0
```

You already wrote a line-reading loop in `labs/2026-11-17-read-path-list.md`. That loop read a hardcoded `paths.txt`. What has to change so it reads the list named by the script argument instead?

### Predictions (before running)

| Invocation                                 | Expected stdout | Expected stderr | Expected status |
| ------------------------------------------ | --------------- | --------------- | --------------- |
| `bash check-list-arg.sh 'good paths.txt'`  | TODO            | TODO            | TODO            |
| `bash check-list-arg.sh 'mixed paths.txt'` | TODO            | TODO            | TODO            |
| `bash check-list-arg.sh absent-list.txt`   | TODO            | TODO            | TODO            |
| `bash check-list-arg.sh`                   | TODO            | TODO            | TODO            |
| `bash check-list-arg.sh archive`           | TODO            | TODO            | TODO            |

### Actual script (paste the output of `cat check-list-arg.sh`)

```bash
#!/usr/bin/env bash

status=0
is_listed_pathname_failed=1

if [ -z "$1" ]; then
    printf 'Usage: bash check-list-arg.sh FILE [FILE ...]\n' >&2
    exit 2
fi

check_file() {
        local path="$1"
	
        if [ -f "$path" ]; then
	        printf 'FILE: %s\n' "$path"
	else
		printf 'NOT FILE: %s\n' "$path" >&2
		is_listed_pathname_failed=0
	fi
}

if [ -r "$1" ] && [ -f "$1" ]; then
   while IFS= read -r path; do
         check_file "$path"
   done < "$1"
else
   printf 'Not a regular file or not readable\n' >&2
   exit 2
fi

if [ "$is_listed_pathname_failed" -eq 0  ]; then
    status=1
fi

exit "$status"
```

References/hints used:

NONE

### Tests A–E: actual commands, output, and immediate `$?`

```text
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ bash check-list-arg.sh 'good paths.txt'
FILE: daily report.txt
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ printf 'status=%s\n' "$?"
status=0
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ bash check-list-arg.sh 'mixed paths.txt'
NOT FILE: archive
FILE: daily report.txt
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ printf 'status=%s\n' "$?"
status=1
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ v
v: command not found
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ bash check-list-arg.sh absent-list.tx
Not a regular file or not readable
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ printf 'status=%s\n' "$?"
status=2
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ bash check-list-arg.sh
Usage: bash check-list-arg.sh FILE [FILE ...]
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ printf 'status=%s\n' "$?"
status=2
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ bash check-list-arg.sh archive
Not a regular file or not readable
raf_0411@ubuntu-desktop:/tmp/bash-list-checkpoint.BShRQr$ printf 'status=%s\n' "$?"
status=2
```


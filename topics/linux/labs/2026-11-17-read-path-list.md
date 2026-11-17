# Read a pathname list — 2026-11-17

## Goal

Observe line-based input, then connect it to your existing function and failure-tracking pattern. This is guided introduction to `read` and `while`, not independent mastery.

Work in Ubuntu. Setup creates only a fresh disposable directory and fixtures. No sudo, deletion, or permission changes are needed. Keep earlier scripts unchanged.

## 1. Set up a fresh fixture

Run as one physical command:

```bash
list_lab=$(mktemp -d /tmp/bash-list.XXXXXX) && cd "$list_lab" && printf 'sample\n' > 'daily report.txt' && mkdir archive && printf '%s\n' archive 'daily report.txt' > paths.txt && pwd
```

Actual directory and output:

```text
/tmp/bash-list.JyzXVdread-pa
```

## 2. Observe the reader

Save this supplied script as `read-paths.sh` in the fresh directory:

```bash
#!/usr/bin/env bash

while IFS= read -r path; do
    printf '<%s>\n' "$path"
done < paths.txt
```

Before running it, predict the printed lines:

```text
<archive>
<daily report.txt>
```

Then run `bash read-paths.sh`. Record actual output:

```text
raf_0411@ubuntu-desktop:/tmp/bash-list.JyzXVd$ bash read-paths.sh
<archive>
<daily report.txt>
```

### How it works

`read` consumes one input line and assigns it to `path`, without its terminating newline. `IFS=` disables whitespace trimming/splitting for this read; `-r` prevents backslash interpretation. The `while` body runs when `read` returns success. At the end of this newline-terminated list, the next read fails and the loop stops. The redirection after `done` supplies input to the whole loop.

For this lab, each pathname occupies one newline-terminated line. Blank lines are not skipped automatically, and filenames containing newlines cannot be represented by this format. Handling an unterminated final line is deferred.

## 3. Connect your checker

Create a separate `check-list.sh` in this same fresh directory.

Use the supplied `while` reader structure, but replace the angle-bracket printing with your previous function-call conditional and reporting branches.

Requirements:

- Define your regular-file checking function before the loop.
- Initialize the overall failure flag once before the loop.
- Read from `paths.txt`; do not iterate over script arguments in this version.
- Print `FILE: pathname` to stdout or `NOT FILE: pathname` to stderr.
- Check all lines and retain any failure, even after a later success.
- Return the remembered overall status after the loop.
- Do not carry over the old first-argument guard: this version takes its input from the fixed list, not from `$1` at script level. A function can still receive and use its own `$1`.

This is a controlled fixture exercise, not yet a robust general-purpose list checker. Missing/unreadable input-list handling is a separate next step.

Paste your actual saved script:

```bash
#! /usr/bin/env bash

status=0

check_file() {
    local path="$1"
    if [ -f "$path" ]; then
        printf 'FILE: %s\n' "$path"
    else
        printf 'NOT FILE: %s\n' "$path" >&2
        status=1
    fi
}

while IFS= read -r path; do
      check_file "$path"
done < paths.txt

exit "$status"
```

Run it and immediately capture its status. Record the command, output, and status capture:

```text
raf_0411@ubuntu-desktop:/tmp/bash-list.JyzXVd$ bash check-list.sh 
NOT FILE: archive
FILE: daily report.txt
raf_0411@ubuntu-desktop:/tmp/bash-list.JyzXVd$ printf 'status=%s\n' "$?"
status=1
```

Additional hints or documentation used:

none

Tell the tutor when ready. Preserve failed attempts and append corrections.

## 4. Reject an unavailable input list

### Review of completed work

The reader prediction matched actual output. The integrated checker preserved the spaced pathname, continued after the directory failed, and returned 1 after the final regular file passed. You reused the reporting function with an outer failure flag; that design works in this non-pipeline loop. Guided line-input integration is complete.

The terminal transcript shows `/tmp/bash-list.JyzXVd`; the setup field contains extra trailing text. Treat that as a recording inconsistency, not a new established directory.

You correctly predicted in a quiz that a missing `paths.txt` causes a shell redirection diagnostic but your original script still exits 0: the loop never runs, leaving the stored flag unchanged.

### New primitive

```bash
[ -r paths.txt ]
```

This succeeds when the pathname is readable by the current user. It is a precheck, not a guarantee that a subsequent open/read succeeds, and it does not check regular-file type. This exercise targets the ordinary missing-list case; stronger input-opening/error handling is deferred.

### Your change

Before the loop, check readability. If the check fails, print a helpful diagnostic to stderr and terminate with status 2 before processing any entries. Keep the existing behavior for a readable list. Construct the conditional yourself; use either a success/else structure or a negated test if you know that syntax.

Append your revised actual script, preserving the previous version above:

```bash
#! /usr/bin/env bash

status=0
check_file() {
	local path="$1"
	if [ -f "$path" ]; then
		printf 'FILE: %s\n' "$path"
	else
		printf 'NOT FILE: %s\n' "$path" >&2
		status=1
	fi
}	

if [ -r paths.txt ]; then
	while IFS= read -r path; do
	      check_file "$path"
	done < paths.txt
	
	exit "$status"
else
    printf 'paths.txt does not exists!\n' >&2
    exit 2
fi
```

### Test A — existing list

From your actual fixture directory, run the revised checker and capture its status immediately. Record actual command/output:

```text
raf_0411@ubuntu-desktop:/tmp/bash-list.JyzXVd$ bash check-list.sh
NOT FILE: archive
FILE: daily report.txt
raf_0411@ubuntu-desktop:/tmp/bash-list.JyzXVd$ printf 'status=%s\n' "$?"
status=1
```

### Test B — missing list without deleting anything

The script currently resolves `paths.txt` relative to its working directory, not its own script location. We can therefore test from a fresh empty directory while leaving your fixtures unchanged.

Start in the fixture directory containing your revised `check-list.sh`. First verify with `pwd` and `ls -l check-list.sh paths.txt`.

Then execute these three separate commands. The middle command creates a disposable directory and runs the checker from it in a subshell; your interactive shell stays in the fixture directory. If temporary-directory creation fails, stop rather than interpreting it as a checker result.

```bash
checker="$PWD/check-list.sh"
empty_lab=$(mktemp -d /tmp/bash-list-empty.XXXXXX) && (cd "$empty_lab" && bash "$checker")
printf 'status=%s\n' "$?"
```

Actual commands/output:

```text
raf_0411@ubuntu-desktop:/tmp/bash-list.JyzXVd$ empty_lab=$(mktemp -d /tmp/bash-list-empty.XXXXXX) && (cd "$empty_lab" && bash "$checker")
paths.txt does not exists!
raf_0411@ubuntu-desktop:/tmp/bash-list.JyzXVd$ printf 'status=%s\n' "$?"
status=2
```

No files are deleted or renamed. The expected policy is status 1 for invalid entries in an available list versus status 2 when the list is unavailable. Record observed results, not inferred ones.

# Extract a reusable file check — 2026-11-17

## Goal

Practice calling a function and using its exit status directly in an `if` condition. This is guided refactoring, not an independent whole-script assessment.

Work in Ubuntu. Keep your completed `check-files.sh` unchanged. Create a separate `check-files-function.sh` beside it after checking your current directory and the original script with `pwd` and `ls -l check-files.sh`. If the new filename already exists, inspect it before deciding whether to edit it; do not overwrite unrelated work.

## Small reference

```bash
check_file() {
    [ -f "$1" ]
}
```

- Define the function before calling it.
- Inside this function, `"$1"` means the first argument passed to the function.
- Call a function like a command: its name followed by arguments, with no call parentheses.
- Its final test supplies its return status. No `exit` is needed inside it.
- An `if` can use a function call as its condition, just as it can use a command or `[ ... ]`.

## 1. Make one focused change

In the new script, retain your existing input guard, argument loop, messages, failure flag, and final exit.

Add the function above. Replace the loop's direct regular-file test with a call to `check_file`, passing the current loop pathname as one argument. Do not move the messages or failure flag into the function yet.

Paste your actual saved new script:

```bash
#! /usr/bin/env bash

status=0

if [ -z "$1" ]; then
    printf 'Usage: bash check-files.sh FILE [FILE ...]\n' >&2
    exit 2
fi

check_file() {
    local path="$1"
    if [ -f "$path" ]; then
        printf 'FILE: %s\n' "$path"
    else
        printf 'NOT FILE: %s\n' "$path" >&2
        status=1
    fi
}

for path in "$@"; do 
   check_file "$path"
done

exit "$status"
```

Additional documentation or hints used:

i searched how to use arguments or parameters in a function in bash

## 2. Test without changing existing files

Use the existing fixture only after checking it is still present. If it is missing, stop and tell the tutor rather than assuming the old temporary path still exists.

Choose an invocation that checks the directory first and the spaced regular filename second. This tests whether failure allows continued processing and remains remembered after a later success. Capture the script's status immediately.

Actual command, output, and status capture:

```text
raf_0411@ubuntu-desktop:/tmp/bash-files.MgxdUV$ bash files-function.sh archive 'daily report.txt' missing.txt
NOT FILE: archive
FILE: daily report.txt
NOT FILE: missing.txt
raf_0411@ubuntu-desktop:/tmp/bash-files.MgxdUV$ printf 'status=%s\n' "$?"
status=1
```

Also run the new script with only the regular filename. Capture its status immediately.

Actual command, output, and status capture:

```text
raf_0411@ubuntu-desktop:/tmp/bash-files.MgxdUV$ bash files-function.sh 'daily report.txt'
FILE: daily report.txt
raf_0411@ubuntu-desktop:/tmp/bash-files.MgxdUV$ printf 'status=%s\n' "$?"
status=0
```

Tell the tutor when ready. Preserve failed attempts and append any corrections.

## 3. Separate the test from the reporting

### Review

Your recorded runs of `files-function.sh` show correct overall mixed-input status 1 and regular-file-only status 0. The function uses a quoted argument and a valid local variable. You researched function arguments; this is documentation-assisted work.

Your implementation differs from the requested design: it reports results and updates the outer `status` variable instead of returning the file-test result to an `if` in the loop. That is a workable alternative, not a failure of the observed whole-script behavior.

In the follow-up quiz, you correctly distinguished the function returning 0 (the successful assignment's exit status) from the stored variable holding 1. The assignment-status rule was supplied in the question; this is immediate recognition, not independent recall.

### Focused refactor

Keep the original attempt above. Edit your actual new script, `files-function.sh`, to practice the requested alternative:

- Keep `local path="$1"` if useful, but have the function finish with the regular-file test itself.
- Move the messages and the failure-flag assignment into the loop.
- Make the loop's `if` condition call `check_file` with the current pathname. Do not wrap the call in command substitution or add `exit` inside the function.
- Keep the input guard and final script exit. Update the usage message to match the actual filename, `files-function.sh`.

This separates two jobs: the function answers “is this a regular file?” through its return status; the caller decides how to report and remember the answer.

Actual revised saved script:

```bash
#! /usr/bin/env bash

status=0

if [ -z "$1" ]; then
    printf 'Usage: bash check-files.sh FILE [FILE ...]\n' >&2
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
      status=1
   fi
done

exit "$status"
```

Run the revised script with the directory first and the spaced regular file last. Record its actual invocation, output, and immediate status capture:

```text
raf_0411@ubuntu-desktop:/tmp/bash-files.MgxdUV$ bash files-function.sh archive 'daily report.txt' missing.txt
NOT FILE: archive
FILE: daily report.txt
NOT FILE: missing.txt
raf_0411@ubuntu-desktop:/tmp/bash-files.MgxdUV$ printf 'status=%s\n' "$?"
status=1
```

Run the revised script with only the regular file and capture its status immediately:

```text
raf_0411@ubuntu-desktop:/tmp/bash-files.MgxdUV$ bash files-function.sh 'daily report.txt'
FILE: daily report.txt
raf_0411@ubuntu-desktop:/tmp/bash-files.MgxdUV$ printf 'status=%s\n' "$?"
status=0
raf_0411@ubuntu-desktop:/tmp/bash-files.MgxdUV$ 
```

These are regression tests of the changed implementation, not a request to repeat the unchanged working version.

## Final verification — supplied in chat

The tutor requested a failure-first/success-last run because the previous mixed test ended with failure. Actual learner output:

```text
raf_0411@ubuntu-desktop:/tmp/bash-files.MgxdUV$ bash files-function.sh archive 'daily report.txt'
NOT FILE: archive
FILE: daily report.txt
raf_0411@ubuntu-desktop:/tmp/bash-files.MgxdUV$ printf 'status=%s\n' "$?"
status=1
```

Outcome: guided function refactoring and its behavioral verification are complete. The function-call condition, reporting branches, and remembered failure flag work together; later success does not erase earlier failure. Targeted test selection needed a reminder. The usage-message filename correction was requested but has not been verified; it is a minor remaining text fix, not a reason to repeat the completed functional lab.

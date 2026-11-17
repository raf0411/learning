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
/tmp/bash-list-checkpoint.C0BLpO
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
TODO
```

References/hints used (NONE if none):

TODO

## 3. Verify the behavior

Construct each invocation yourself. Include actual commands, output, and immediate exit-status capture. Do not replace failed evidence with a correction; append corrected runs.

### A. The all-regular-file list

```text
TODO
```

### B. The list with a directory first and a regular file last

```text
TODO
```

### C. A missing input list

```text
TODO
```

### D. No script arguments

```text
TODO
```

### E. A directory supplied as the input list

```text
TODO
```

Tell the tutor when ready. Tests C and E concern the list itself; test B concerns entries inside an available list. Keep that distinction visible in your diagnostics.

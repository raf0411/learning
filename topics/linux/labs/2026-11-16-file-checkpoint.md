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

TODO

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
TODO
```

References or hints used (write NONE if none):

TODO

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
TODO
```

### C. No arguments

```bash
bash check-files.sh
```

Actual invocation/output and immediate status capture:

```text
TODO
```

Tell the tutor when ready. If any test fails, preserve the evidence; you can append a self-correction rather than replacing the earlier attempt.
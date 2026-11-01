# Handle a missing log file

Date: 2026-11-01

Your file-reading summary works when `sample.log` exists. An automation script also needs deliberate behavior when its input is missing.

## One new idea: handle a specific exception

Opening a nonexistent file raises `FileNotFoundError`. Python normally stops the program and displays a traceback.

This structure lets the program choose clearer behavior:

```python
try:
    # Attempt an operation that might fail.
except FileNotFoundError:
    # Run this only if that specific failure occurs.
else:
    # Run this only if the try block succeeds.
```

The control flow is:

```text
attempt to open and read
        |
        +-- success --> else --> print the report
        |
        +-- missing --> except FileNotFoundError --> print an error
```

We catch `FileNotFoundError`, not every possible exception. Unexpected programming errors should remain visible while debugging.

## 1. Build the safe summary

Create `labs/safe_file_log_summary.py`. Adapt your working file summary using this scaffold:

```python
log_path = "/Users/raffi/Learning/topics/python/labs/sample.log"

total = 0
errors = 0

try:
    # TODO: open log_path and perform the counting loop
except FileNotFoundError:
    print("Error: log file not found")
else:
    # TODO: print the final Total and Errors report
```

Use four spaces for each indentation level. Your successful result should still depend on the contents of `sample.log`.

Paste your completed code here:

```python
log_path = "/Users/raffi/Learning/topics/python/labs/sample.log"

total = 0
errors = 0

try:
    with open(log_path, encoding="utf-8") as log_file:
        for line in log_file:
			total += 1
			if line.startswith("ERROR "):
				errors += 1
except FileNotFoundError:
    print("Error: log file not found")
else:
    print("Total:", total)
	print("Errors:", errors)
```

Before running it, predict the exact output with the existing `sample.log`:

```text
Total: 6
Errors: 3
```

Run:

```bash
python3 /Users/raffi/Learning/topics/python/labs/safe_file_log_summary.py
```

Record the actual output or exact error:

```text
raffi@Raffis-Mac labs % python3 /Users/raffi/Learning/topics/python/labs/safe_file_log_summary.py
Total: 6
Errors: 3
```

## 2. Test the failure path

In `safe_file_log_summary.py`, change only `log_path` to:

```python
log_path = "/Users/raffi/Learning/topics/python/labs/missing.log"
```

Do not create `missing.log`.

Predict the exact output:

```text
Error: log file not found
```

Run the same command and record the actual output or exact error:

```text
raffi@Raffis-Mac labs % python3 /Users/raffi/Learning/topics/python/labs/safe_file_log_summary.py
Error: log file not found
```

## 3. Explain the control flow

Why are the `Total:` and `Errors:` reports inside `else` instead of after the whole `try`/`except` structure?

attempt to open and read
        |
        +-- success --> else --> print the report
        |
        +-- missing --> except FileNotFoundError --> print an error

Does this program handle every possible error, or only a particular kind? Be specific.

only a particular kind which is the File not found

Keep any mismatch or traceback intact so we can diagnose it. Tell me when the worksheet is ready or where you get stuck.

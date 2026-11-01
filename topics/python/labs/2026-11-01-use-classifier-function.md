# Use the classifier function in the log report

Date: 2026-11-01

You have tested this rule as a function:

```python
def is_error(log_line):
    return log_line.startswith("ERROR ")
```

Now use it inside the file-processing program. This is a small refactor: the organization changes, but the observable result should stay the same.

## Build the refactored script

Create `labs/function_log_summary.py` from the logic in `safe_file_log_summary.py`.

Make these changes:

1. Put the `is_error` function definition near the top, before `log_path`.
2. Use the existing `sample.log` path.
3. Replace this condition:

   ```python
   if line.startswith("ERROR "):
   ```

   with a call to your function:

   ```python
   if is_error(line):
   ```

4. Preserve the successful report and the `FileNotFoundError` behavior.
5. Use four spaces for every indentation level in this new file.

Your complete code:

```python
def is_error(line):
    return line.startswith("ERROR ")

log_path = "/Users/raffi/Learning/topics/python/labs/sample.log"

total = 0
errors = 0

try:
    with open(log_path, encoding="utf-8") as log_file:
        for line in log_file:
          total += 1
          if is_error(line):
            errors += 1
except FileNotFoundError:
    print("Error: log file not found")
else:
    print("Total:", total)
    print("Errors:", errors)
```

Before running, predict the exact output:

```text
Total: 6
Errors: 3
```

Run:

```bash
python3 /Users/raffi/Learning/topics/python/labs/function_log_summary.py
```

Record the actual output or exact error:

```text
raffi@Raffis-Mac labs % python3 /Users/raffi/Learning/topics/python/labs/function_log_summary.py
Total: 6
Errors: 3
```

## Trace one function call

Suppose the loop has just read this line:

```text
ERROR database unavailable
```

Describe the sequence from `if is_error(line):` to the counter update. Include:

- the value passed into the function
- the value returned by the function
- why `errors += 1` does or does not execute

value passed : "ERROR database unavailable"
value returned : True
errors += 1 executes because the value returned is True, it will run the if statement which counts the errors

Why should this refactor produce the same report as the earlier script?

Because we are using the same file sample.log

Keep any mismatch or traceback intact so we can diagnose it. Tell me when the worksheet is ready or where you get stuck.

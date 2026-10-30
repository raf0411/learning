# Read the logs from a file

Date: 2026-10-30

Your summary currently stores the messages inside the Python program. Real log data changes independently of the program. Read it from a separate text file so the same script can process new messages.

## One new idea: iterate over an open text file

I created `labs/sample.log` with the same five messages from your previous exercise. Open it in your text editor to inspect the contents.

This example reads that file:

```python
with open("/Users/raffi/Learning/topics/python/labs/sample.log", encoding="utf-8") as log_file:
    for line in log_file:
        print("Read a line")
```

- `open(...)` opens this existing file for reading. The full path identifies it regardless of your terminal's current directory.
- `encoding="utf-8"` specifies how the file's bytes are decoded into text.
- `log_file` refers to the open file object. Iterating over it gives you one line of text at a time.
- `with` keeps the file open for its indented block and closes it automatically when that block ends.

The `for` body is now inside two blocks: `with`, then `for`. An `if` inside the loop adds another level. Use four spaces per level.

Lines read from this file normally include a newline character at the end. That does not change whether they begin with `"ERROR "`.

## 1. Adapt your summary

Create `labs/file_log_summary.py`. Adapt your previous summary to read `sample.log` instead of using a list inside the script.

Requirements:

- Count all lines and lines beginning with `"ERROR "`.
- Print only the final `Total:` and `Errors:` results.
- Keep counter initialization and final reporting outside the `with` block.

Your code:

```python
# TODO
```

Predict the exact output, including labels:

```text
TODO
```

Save and run:

```bash
python3 /Users/raffi/Learning/topics/python/labs/file_log_summary.py
```

Actual output or exact error:

```text
TODO
```

## 2. Change the data

Add this as one new line at the end of `labs/sample.log`, then save the log file:

```text
ERROR health check failed
```

Leave your Python script unchanged.

Predict its new output before running it again:

```text
TODO
```

Run the same command again. Record the actual output:

```text
TODO
```

Why can the result change even though you did not edit the Python script?

TODO

Keep any mismatches or errors so we can inspect them. Tell me when the worksheet is ready or where you get stuck.

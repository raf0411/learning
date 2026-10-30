# Summarize sample log messages

Date: 2026-10-30

You have combined a loop, condition, and counter. Now use those ideas to summarize log messages.

## One new tool: checking the beginning of text

Real log messages include details, so `"ERROR disk full" == "ERROR"` is false: those strings are not equal.

Use `startswith` when you want to check the beginning instead:

```python
line = "ERROR disk full"
print(line.startswith("ERROR "))
```

This prints `True`. The expression checks whether the string referred to by `line` begins with `"ERROR "`, including the space. You can use this expression as an `if` condition.

To label a result, `print` can take multiple values separated by commas:

```python
print("Count:", 4)
```

This prints `Count: 4`.

## Build a log summary

Create `labs/log_summary.py` with this sample data:

```python
lines = [
    "INFO service started",
    "ERROR database unavailable",
    "INFO retry scheduled",
    "ERROR request timed out",
    "INFO service stopped",
]
```

Write a program that uses a loop to count:

- all log messages
- messages beginning with `"ERROR "`

After processing the list, print two labeled results: `Total:` and `Errors:`. Use counters for both so you can practice deciding which update belongs inside the condition.

Use four spaces for each indentation level. Keep the code in this note aligned with your saved script.

Your code, including the input list:

```python
lines = [
    "INFO service started",
    "ERROR database unavailable",
    "INFO retry scheduled",
    "ERROR request timed out",
    "INFO service stopped",
]

total = 0
errors = 0

for line in lines:
  total += 1

  if line.startswith("ERROR "):
    errors += 1

print("Total:", total)
print("Errors:", errors)
```

Before running, predict the exact output:

```text
5
2
```

Run this command:

```bash
python3 /Users/raffi/Learning/topics/python/labs/log_summary.py
```

Actual output or exact error:

```text
Total: 5
Errors: 2
```

Explain why your two counters do or do not have the same indentation:

because one has to count every single line and the other only need to count that has ERROR in the if statement

## Try an empty input

Replace the input list with `lines = []`. This represents having no log messages to process.

Predict the output before running:

```text
0
```

Save and run again. Record the actual result:

```text
Total: 0
Errors: 0
```

Clarified in chat: the original `0` entry abbreviated the actual two-line output above. Original prediction preserved.

If the results differ from your predictions, keep the predictions and describe what you discovered:

matches (or "matches")

Tell me when the worksheet is ready, or where you get stuck.

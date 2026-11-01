# Return a complete summary from a function

Date: 2026-11-01

Your `is_error` function returns one Boolean result. A function can also return more than one result.

## One new idea: return and receive two values

```python
def starting_counts():
    return 0, 0

total, errors = starting_counts()
```

The order connects the values:

```text
return 0, 0
       |  |
       v  v
   total  errors
```

The call runs the function. The returned first value is assigned to `total`, and the returned second value is assigned to `errors`.

## 1. Predict two returned values

Without running this code, predict its exact output:

```python
def example_counts():
    return 4, 2

total, errors = example_counts()
print("Total:", total)
print("Errors:", errors)
```

Prediction:

```text
TODO
```

## 2. Build a summary function

Create `labs/summary_function.py`.

Requirements:

- Keep your `is_error(line)` function.
- Define a second function named `summarize(lines)`.
- Inside `summarize`, initialize `total` and `errors` to zero.
- Loop over `lines`, count every line, and use `is_error(line)` for the conditional error count.
- After the loop, return `total, errors` in that order.
- Outside the functions, call `summarize(sample_lines)` and receive its two returned values.
- Print the usual labeled report.

Use this input:

```python
sample_lines = [
    "INFO service started",
    "ERROR database unavailable",
    "ERROR request timed out",
    "INFO service stopped",
]
```

Your complete code:

```python
# TODO
```

Predict the exact output before running:

```text
TODO
```

Run:

```bash
python3 /Users/raffi/Learning/topics/python/labs/summary_function.py
```

Record the actual output or exact error:

```text
TODO
```

## 3. Explain the data flow

In this statement, what value is passed into `summarize`, and which two values come back?

```python
total, errors = summarize(sample_lines)
```

TODO

Why must `return total, errors` be after the loop rather than inside it?

TODO

Keep any mismatch or traceback intact so we can diagnose it. Tell me when the worksheet is ready or where you get stuck.

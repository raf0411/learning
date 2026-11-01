# Name the log-classification rule with a function

Date: 2026-11-01

Your report currently embeds this rule inside its loop:

```python
line.startswith("ERROR ")
```

A function can give that rule a name and let other code ask one focused question: `is_error(line)`.

## Function anatomy

Here is the same idea for `INFO ` lines:

```python
def is_info(log_line):
    return log_line.startswith("INFO ")
```

- `def` creates a function.
- `is_info` is its name.
- `log_line` is a parameter: a local name that receives each supplied value.
- `return` sends the result back to the calling code.
- `startswith(...)` produces either `True` or `False`, so this function returns a Boolean value.

Defining a function does not run its body. A call such as `is_info("INFO ready")` runs it with that string assigned to `log_line`.

## 1. Predict function calls

Without running Python, predict the exact output:

```python
def is_info(log_line):
    return log_line.startswith("INFO ")

print(is_info("INFO service started"))
print(is_info("ERROR service stopped"))
```

Prediction:

```text
True
False
```

Briefly trace the first call: what value does `log_line` receive, and what value is returned?

Value: "INFO service started", value returned: True

## 2. Write the error-classification function

Create `labs/log_line_classifier.py` with a function named `is_error`. It should accept one log line and return whether that line begins with the exact prefix `"ERROR "`.

After the function definition, add these three calls:

```python
print(is_error("ERROR disk full"))
print(is_error("INFO service started"))
print(is_error("ERRORS are increasing"))
```

Use four spaces for the function body.

Your complete code:

```python
def is_error(log_line):
	return log_line.startswith("ERROR ")

print(is_error("ERROR disk full"))
print(is_error("INFO service started"))
print(is_error("ERRORS are increasing"))
```

Predict all three output lines before running:

```text
True
False
False
```

Run:

```bash
python3 /Users/raffi/Learning/topics/python/labs/log_line_classifier.py
```

Record the actual output or exact error:

```text
True
False
False
```

Why does the third call return its particular result? Pay attention to the space in the required prefix.

Because we are checking startswith for "ERROR " not "ERRORS "

Tell me when the worksheet is ready or where you get stuck.

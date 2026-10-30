# Count only a failure

Date: 2026-10-30

Your counter works. Now make the update depend on the result of a check.

## One new idea: `if`

```python
status = "failed"
if status == "failed":
    print("Needs attention")
print("Check finished")
```

- `=` assigns a value to a name.
- `==` compares two values for equality, producing `True` or `False`.
- `if` runs its indented block only when the condition is true. End the `if` line with a colon and indent the block with four spaces.
- The final `print` is outside the block, so it runs whether the condition is true or false.

## 1. Predict before running

```python
errors = 0
status = "failed"
if status == "failed":
    errors = errors + 1
print(errors)
```

Predict the output for each separate run. Each run starts again at `errors = 0`.

| Value assigned to `status` | Predicted output | Actual output (fill after running) |
| -------------------------- | ---------------- | ---------------------------------- |
| `"failed"`                 | 1                | 1                                  |
| `"passed"`                 | 0                | 0                                  |

For `status = "passed"`, which line is skipped, and why does the final `print` still run?

TODO

## 2. Run and compare

Create `labs/conditional_counter.py` in your code editor using the code above. Run it, then change only the status value to `"passed"`, save, and run again:

```bash
python3 /Users/raffi/Learning/topics/python/labs/conditional_counter.py
```

Fill in the actual-output column. Keep your original predictions. Record any mismatch or error here (or write "matches"):

matches

## 3. Explore indentation

Keep `status = "passed"`. Move `print(errors)` into the `if` block by giving it the same four-space indentation as the counter update.

Before running, predict what the program will display and explain why:

nothing, because the print has been move to the if block, and the if block never ran because status is "passed"

Now save and run it. Record what happened, including if nothing was printed:



Tell me when this worksheet is ready.

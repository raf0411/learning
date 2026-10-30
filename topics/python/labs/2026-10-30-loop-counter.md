# Count failures across several checks

Date: 2026-10-30

You can conditionally update a counter for one check. Now process several checks without copying the same `if` statement repeatedly.

## One new idea: a `for` loop

```python
statuses = ["passed", "failed", "failed"]
for status in statuses:
    print(status)
print("Finished")
```

The square brackets create a list of values in order. The `for` loop assigns the next value to `status`, then runs its indented body. It repeats this for every item. The final unindented statement runs after the loop finishes.

An `if` can go inside a loop. Its body is indented one level further:

```python
for status in statuses:
    if status == "failed":
        print("Needs attention")
```

Use four spaces per indentation level: four before `if`, eight before its `print`.

## 1. Trace the loop

Before running any code, predict the exact output of the first example, including the final line:

```text
passed
failed
failed
Finished
```

## 2. Build your failure counter

Create `labs/loop_counter.py`. Use this input:

```python
statuses = ["failed", "passed", "failed", "failed"]
```

Write a program that counts how many statuses equal `"failed"`, using a loop and a counter. It should print only the final count once.

Choose where to initialize the counter, where to update it, and where to print it. Use your earlier counter scripts as references if needed.

Record your code:

```python
statuses = ["failed", "passed", "failed", "failed"]

count = 0

for status in statuses:
	if status == "failed":
	count += 1

print(count)
```

Why did you place the counter initialization and final print where you did?

because the counter needs to start from 0 and putting it above the loop guarantees that, the final print has to be at the end and after the loop because thats when the counting stops or loop stops

Before running, predict the final output:

```text
3
```

Run your saved script:

```bash
python3 /Users/raffi/Learning/topics/python/labs/loop_counter.py
```

Record the actual output or exact error:

```text
3
```

## 3. Check another input

Change only the list to `["passed", "passed"]`. Predict, then save and run again.

Prediction:

```text
0
```

Actual output:

```text
0
```

Keep your original predictions and any failed attempts. If something surprises you, describe it here:

matches (or "matches")

Tell me when the worksheet is ready, or where you get stuck.

# First Python script: variables and counters

Date: 2026-10-30

Your baseline algorithm began with a counter at zero and increased it for each matching line. This exercise builds the counter part first.

## One idea to use

A variable is a name referring to a value. The value has a type: `3` is an integer (`int`), while `"web-01"` is text (`str`, short for string).

```python
attempts = 3
attempts = attempts + 2
print(attempts)
```

Python runs these statements in order. On the second line, it evaluates the right-hand expression using the current value of `attempts`, producing `5`, then makes `attempts` refer to that result. `print(attempts)` displays the current value: `5`.

The `=` symbol performs assignment. It does not ask whether two things are equal.

## 1. Predict before running

```python
errors = 0
errors = errors + 1
print(errors)
errors = errors + 1
print(errors)
```

Write the exact output, one printed value per line:

```text
TODO
```

Explain what the right side of `errors = errors + 1` uses and what the assignment changes:

TODO

## 2. Run your first script

In a plain-text code editor, create a file called `first_counter.py` inside this topic's `labs` directory. Copy the five Python lines above into it. Do not include the Markdown fences (the lines with three backticks).

Save it, then run this single command in your terminal. The full path allows it to work regardless of your terminal's current directory:

```bash
python3 /Users/raffi/Learning/topics/python/labs/first_counter.py
```

`python3` starts Python, and the path tells it which file to execute. This script only calculates values and prints them.

Paste the actual output (or the exact error if it fails):

```text
TODO
```

Compare it with your prediction. If they differ, describe the difference; keep your original prediction:

TODO

## 3. Write a small variation yourself

Replace the contents of your `first_counter.py` with your own program that:

1. Starts a variable named `failed_checks` at `2`.
2. Increases it by `1`, using its current value, and prints the result.
3. Increases it by `3`, using its current value, and prints the result again.

Use Python to calculate the updated counts rather than typing the final counts directly.

Record your code here too:

```python
# TODO: your program
```

Save the script and run the same terminal command again. Paste the output:

```text
TODO
```

If creating or running the file is unfamiliar, tell me where you got stuck. We can handle that step together.

When finished, tell me this worksheet is ready.

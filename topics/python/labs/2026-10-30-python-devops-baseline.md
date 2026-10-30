# Python for DevOps — Starting Baseline

Date: 2026-10-30

This is a diagnostic, not a graded test. Answer from memory. If something is unfamiliar, write `I don't know yet`; that is useful evidence for choosing the right starting point.

## 1. Relevant experience

Briefly describe any experience you already have with:

- Python or another programming language
- the Linux terminal or shell scripts
- Git
- servers, containers, cloud platforms, CI/CD, or other DevOps tools

none


## 2. Explain familiar ideas

In your own words, explain any of these terms you already understand. For unfamiliar terms, write `unfamiliar`.

### Variable

a place to store a data type


### Conditional (`if`)

conditional to condition an outcome


### Loop

loops a code without doing it so many times


### Function

call a repetitive code in one call function


## 3. Read a small Python program

Do not run this yet. Predict what it prints, then explain how you reasoned about it.

```python
servers = ["web-01", "db-01", "web-02"]

for server in servers:
    if server.startswith("web"):
        print(f"Checking {server}")
```

Predicted output:

```text
Checking web-01
Checking web-02
```

Reasoning:

because we are looking for servers that starts with web, db is not it


## 4. Decompose an automation task

Imagine we want a script that reads a log file and reports how many lines contain the word `ERROR`.

Without worrying about Python syntax, list the steps the program would need to perform, in order.

1. store a count from zero variable and loop the log file lines
2. if the log contains the word ERROR increment the count by 1
3. after the loop ends, print the count


## 5. Inspect your Python environment

Run this as one command in your terminal:

```bash
python3 --version
```

Paste the exact output:

```text
Python 3.14.6
```

Did the command behave as you expected? Mention any error or surprise.

as expected

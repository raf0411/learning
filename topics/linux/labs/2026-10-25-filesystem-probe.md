# Filesystem Foundations — Initial Probe

Date: 2026-10-25

This is a diagnostic, not a graded test. Answer from memory first. Write
`not sure` freely; that tells the tutor where teaching should begin.

## Part A — Current mental model

### 1. Commands

In your own words, what do these commands do?

- `pwd`: shows the current directory/location
- `ls`: checking files or directories available in current location
- `cd`: moving to different location or folder

### 2. Navigation prediction

Suppose your current directory is:

```text
/home/raff/projects/linux-lab
```

You run:

```bash
cd ..
```

What do you predict the new current directory will be, and why?

current will be "/home/raff/projects", because cd .. is going up by 1 levell to the previous directory

### 3. Path comparison

What difference, if any, do you see between these two paths?

```text
/etc/hosts
notes/todo.txt
```

first one is absolute path
second one is relative path

## Part B — Read-only observation

These commands only change which directory your shell is looking at and display
information; they do not alter or delete files.

Run each command as a separate submission:

```bash
cd /Users/raffi/Learning/topics/linux
```

```bash
pwd
```

```bash
ls
```

Record the output of `pwd`:

```text
/Users/raffi/Learning/topics/linux
```

Record the output of `ls`:

```text
diagrams	GOAL.md		labs		RESOURCES.md	REVIEW.md	ROADMAP.md	sessions	STATE.md
```

### 4. Interpret the evidence

Based on the actual output, what relationship do you think exists between what
`pwd` displays and what `ls` displays?

idk what specific relationship u r talking about, but both does different thing, pwd displays the current path that the user is in, and ls displays the current available files or folders in our current path

## Optional context

Have you used a command-line terminal before? If so, briefly describe what you
have done with it.

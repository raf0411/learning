# Repeat work for each argument — 2026-11-16

## Goal

Write a small loop before adding repetition to your network script. This exercise only prints text; it makes no network requests.

## Building blocks

```bash
for color in red blue; do
    printf 'Color: %s\n' "$color"
done
```

The body runs once for each listed value. `color` holds the current value.

Inside a script, `"$@"` expands to all supplied arguments, each preserved as a separate argument. Double quotes matter, especially when an argument contains spaces.

## 1. Prepare a separate disposable file — Ubuntu

Leave your working web-check script unchanged. This supplied line creates and enters a fresh directory:

```bash
loop_lab=$(mktemp -d /tmp/bash-loop.XXXXXX) && cd "$loop_lab" && pwd
```

Actual directory:

/tmp/bash-loop.qyKPhc

## 2. Write your loop

Create `show-targets.sh` using your editor. Write a script that:

- Loops through all supplied arguments using `"$@"`.
- Uses `target` as the loop variable.
- Prints `Target: <VALUE>` and a newline for each argument, using a fixed printf format with `%s` and the quoted variable.

Do not add curl, guards, or explicit exits yet. We will invoke Bash explicitly, so executable permission is not needed.

Inspect the saved file and paste its actual contents:

```bash
#! /usr/bin/env bash

targets="$@"

for target in targets; do
   printf 'Target: %s\n' "$target"
done
```

## 3. Test argument boundaries

These are text labels, not URLs. The quotes in the invocation deliberately make `first target` one argument:

```bash
bash show-targets.sh 'first target' second
```

Record the actual invocation and output:

```text
raf_0411@ubuntu-desktop:/tmp/bash-loop.qyKPhc$ bash show-targets.sh 'first target' second
Target: targets
```

## 4. Repair after feedback

Keep your initial code and output above unchanged.

The original loop listed the literal word `targets`, so it ran once with that value. An ordinary string assignment is not a substitute for the argument list.

Remove `targets="$@"`. Use `for target in "$@"; do` to iterate directly over the original arguments. Keep `"$target"` quoted in the body, and use the requested printf format `Target: <%s>\n`.

Actual revised saved script:

```bash
#! /usr/bin/env bash

for target in "$@"; do
   printf 'Target: %s\n' "$target"
done
```

Rerun `bash show-targets.sh 'first target' second` and record the actual invocation and output:

```text
raf_0411@ubuntu-desktop:/tmp/bash-loop.qyKPhc$ bash show-targets.sh 'first target' second
Target: first target
Target: second
```

Tell the tutor when ready.
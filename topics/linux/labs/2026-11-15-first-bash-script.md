# First Bash script — 2026-11-15

## Goal

Create a small reusable web check in the Ubuntu VM. This is a disposable script containing read-only commands, not a system configuration change.

## 1. Prepare — Ubuntu terminal

Run this single supplied setup line. It creates a fresh directory and moves this shell into it:

```bash
script_lab=$(mktemp -d /tmp/bash-practice.XXXXXX) && cd "$script_lab" && pwd
```

Record the actual directory:

TODO

## 2. Write your script

Open a new file:

```bash
nano check-web.sh
```

Write three commands yourself, in this order:

1. Print the heading `Web check` followed by a newline.
2. Print this Ubuntu machine's hostname.
3. Request only the response headers from **https://example.com**, with a **10-second maximum total duration**.

Use the shell commands you have already practiced. Do not add sudo, installation, configuration changes, or certificate bypasses. No shebang is needed yet because we will invoke Bash explicitly. Save and exit the editor.

Paste the script's actual saved contents here (use a read-only command to inspect the file, rather than reconstructing it from memory):

```bash
TODO
```

## 3. Execute and capture status

Run:

```bash
bash check-web.sh
```

**Immediately afterward**, use your own command to display its shell exit status, before running anything else. If you forget and run another command, acknowledge that and rerun the script before capturing status; do not guess the earlier value.

Record the execution command, output, and immediate status-capture command/output:

```text
TODO
```

## 4. Interpret

Did this particular HTTPS request succeed? Identify the evidence without claiming that every feature of the website works.

TODO

Help used beyond these supplied instructions (manuals, tutor hints, etc.):

TODO

Stop here and tell the tutor when ready. Keep the script for the next step; do not add arguments, loops, or conditionals yet.

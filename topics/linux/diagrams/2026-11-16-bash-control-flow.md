# Bash: data, decisions, and final status

Session reference — 2026-11-16. These are explanations, not additional exercises.

## Data is not status

| Expression | Meaning |
|---|---|
| `"$1"` | First argument's text |
| `"$@"` | All arguments, preserved separately |
| `$(hostname)` | Captured standard output from hostname |
| `"$?"` | Most recent command's exit status |

`[ -z "$1" ]` checks one string. `"$@"` is a list, not one string to give to `-z`.

## A condition chooses; exit stops

```text
if command; then
       |
       +-- status 0 ------> then branch
       |
       +-- nonzero -------> else branch, if present

After the selected branch, continue after fi.
An explicit exit stops this script instead.
```

A nonzero condition does not automatically terminate the script. `false` reports
status 1; `exit 1` explicitly stops the current shell with status 1.

## Why the last command matters

```text
curl fails -> printf succeeds -> script ends normally -> status 0
```

The successful message can hide the earlier failure. Testing curl directly with
`if curl ...; then` avoids inspecting the status of a later printf.

## Remember failures while continuing

```text
Invalid first argument -> usage on stderr -> exit 2

Valid input
    |
    v
Initialize overall_status=0 once
    |
    v
For each URL:
    success -> leave overall_status unchanged
    failure -> set overall_status=1, continue
    |
    v
After loop: exit "$overall_status"
```

Assignment changes stored data; it does not stop execution. A later success must
not reset the remembered failure. These numeric meanings are the script's chosen
policy, not universal meanings for every program.

## Direct execution

```text
./check-web.sh -> explicit pathname
owner execute -> permission to launch
shebang       -> interpreter selection
```

The shebang does not grant execute permission. In today's lab, owner-only execute
changed mode 664 to 764; 774 also granted group execute and exceeded the request.

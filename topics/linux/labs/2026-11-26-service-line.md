# sysprobe: Service line (2026-11-26)

Project: `~/Documents/sysprobe` on the Ubuntu VM. Tests are currently 9/9, status 0.

## What you know so far

`systemctl is-active NAME` prints one word. Exit status, from your run plus `man systemctl`:

| Status | Meaning (man page) | Observed |
|---|---|---|
| 0 | active | `ssh` → `active` |
| 3 | program not running | (not seen yet) |
| 4 | program or service status is unknown | `nosuchsvc` → `inactive` (misleading word!) |

Design decisions made in chat:
- The service is an **optional 2nd positional argument**: `bin/sysprobe.sh LOG [SERVICE]`.
- `systemctl` and `journalctl` are **optional tools**. The log analysis doesn't need them.
- `not requested` (no argument given) and `unavailable` (tool missing) are different situations, so they get different text.

## Target lines

| Situation | Line |
|---|---|
| no 2nd argument | `Service: not requested` |
| `systemctl` missing | `Service: unavailable` |
| status 4 | `Service: shh not found` |
| otherwise | `Service: ssh active` (or `inactive` / `failed`) |

## 1. Fill in the skeleton

Replace the two `<...>` parts. Put the block after your `ps` block, using the same compute-first pattern.

```bash
service="$2"
if [ -z "$service" ]; then
    service_line="Service: not requested"
elif ! command -v systemctl > /dev/null; then
    service_line="Service: unavailable"
else
    state=$(systemctl is-active "$service")
    svc_status=<SAVE THE STATUS OF THE LINE ABOVE>
    if [ <TRUE WHEN THE SERVICE DOESN'T EXIST> ]; then
        service_line="Service: $service not found"
    else
        service_line="Service: $service $state"
    fi
fi
```

Your filled-in version of the two lines:

```bash
svc_status=TODO
if [ TODO ]; then
```

Then print it under a `== Service ==` header, before the log summary. Write your print lines here:

```bash
TODO
```

## 2. Design question

Why does the `-z` check come **before** the `command -v systemctl` check? What would go wrong, or be misleading, if they were swapped?

```text
because the user might not even putting that second argument so we have to check that first, if it were swapped then even if the user didnt put the 2nd argument it would still ran
```

## 3. Run and paste the actual output

Run each command on the VM. Paste the `== Service ==` section and the status line for each.

```bash
bin/sysprobe.sh samples/good.log ssh; echo "status: $?"
```

```text
TODO
```

```bash
bin/sysprobe.sh samples/good.log shh; echo "status: $?"
```

```text
TODO
```

```bash
bin/sysprobe.sh samples/good.log; echo "status: $?"
```

```text
TODO
```

Finally, check that the suite still passes:

```bash
tests/run-tests.sh; echo "status: $?"
```

```text
TODO
```

## 4. Self-audit

Does every line in section 3 match the target table exactly? Note any mismatch:

```text
(skipped; tutor noted: Service prints after Log summary, brief said before)
```

## 5. Test case 10: service not found

Add this to `tests/run-tests.sh`, before the final `if [ "$failed" -eq 1 ]` block:

```bash
if bin/sysprobe.sh samples/good.log nosuchsvc | grep -q '^Service: nosuchsvc not found$'; then echo "PASS service not found"; else echo "FAIL service not found"; failed=1; fi
```

**Before running:** if your `-eq 4` branch broke and the script printed `Service: nosuchsvc inactive`, what would this case print? Does the suite status change?

```text
TODO
```

Then run the suite and paste:

```text
raf_0411@ubuntu-desktop:~/Documents/sysprobe$ tests/run-tests.sh; echo "status: $?"
PASS valid file
PASS missing arguments
PASS missing file
PASS directory argument
PASS failed logins ignore other auth errors
PASS disk line matches df /
PASS top processes
PASS missing required command
PASS memory line
PASS service not found
status: 0
```

Then prove it by mutation: change `-eq 4` to `-eq 99`, run, paste the result, and revert. Show the revert with `grep -n 'svc_status" -eq' bin/sysprobe.sh`.

```text
TODO
```

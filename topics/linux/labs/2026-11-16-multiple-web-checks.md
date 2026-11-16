# Combine your loop and web check — 2026-11-16

## Goal

Build a separate script that checks multiple URLs in order and stops at the first failed curl request. Reuse the ideas from your completed scripts; write the combined code yourself.

## 1. Create a fresh workspace — Ubuntu

This supplied setup creates and enters a disposable directory, leaving both earlier scripts untouched:

```bash
multi_lab=$(mktemp -d /tmp/bash-multi.XXXXXX) && cd "$multi_lab" && pwd
```

Actual directory:

/tmp/bash-multi.tYZNzN

## 2. Write `check-many.sh`

Use your earlier scripts as references if helpful. Requirements:

- Include the Bash shebang.
- Keep your existing missing/empty-first-argument guard with status 2. Update its usage message to name `check-many.sh` and indicate that additional URLs can follow.
- Capture the hostname and print the machine heading once, before the loop.
- Loop over all supplied arguments, preserving each argument separately.
- Before each request, print `Checking: URL`, substituting the current URL using a fixed printf format.
- Request HEAD with a ten-second maximum total duration for the current URL.
- Test curl directly with `if`.
- On curl success, print `Request completed` and allow the loop to continue.
- On curl failure, print `Request failed` to standard error and stop the whole script with status 1.

Do not add retries, background jobs, or new exit-status policies. The timeout applies to each curl invocation, not the whole loop. As before, curl success means transfer completion, not necessarily an HTTP 2xx response.

Inspect the saved file and paste its actual contents:

```bash
#! /usr/bin/env bash

if [ -z "$@" ]; then
    printf 'Usage: bash check-web.sh URL\n' >&2
    exit 2
fi

machine=$(hostname)

printf 'Web check on %s\n' "$machine"

for url in "$@"; do
   printf 'Checking: %s\n' "$url"
   if curl -I --max-time 10 "$url"; then
      printf 'Request completed\n'
   else
      printf 'Request failed\n' >&2
      exit 1
   fi
done
```

## 3. Test the combined behavior

Run each test separately and capture its exit status immediately. We invoke Bash explicitly, so no permission modification is needed.

### Two supplied HTTPS URLs

```bash
bash check-many.sh https://example.org https://example.com
```

Actual command/output and immediate status capture:

```text
raf_0411@ubuntu-desktop:/tmp/bash-multi.tYZNzN$ bash check-many.sh https://example.org https://example.com
Web check on ubuntu-desktop
Checking: https://example.org
HTTP/2 200 
date: Mon, 16 Nov 2026 13:08:56 GMT
content-type: text/html; charset=utf-8
server: cloudflare
last-modified: Mon, 16 Nov 2026 00:26:08 GMT
allow: GET, HEAD
accept-ranges: bytes
age: 12382
cache-control: max-age=14400
cf-cache-status: HIT
cf-ray: a5b6ba2b1abe3b65-SIN
alt-svc: h3=":443"; ma=86400

Request completed
Checking: https://example.com
HTTP/2 200 
date: Mon, 16 Nov 2026 13:08:56 GMT
content-type: text/html; charset=utf-8
server: cloudflare
last-modified: Mon, 16 Nov 2026 00:26:08 GMT
allow: GET, HEAD
accept-ranges: bytes
age: 0
cf-cache-status: HIT
cf-ray: a5b6ba2beda5f912-SIN
alt-svc: h3=":443"; ma=86400

Request completed
raf_0411@ubuntu-desktop:/tmp/bash-multi.tYZNzN$ printf 'status=%s\n' "$?"
status=0
```

### Malformed URL first, valid URL second

```bash
bash check-many.sh https:// https://example.org
```

Actual command/output and immediate status capture:

```text
raf_0411@ubuntu-desktop:/tmp/bash-multi.tYZNzN$ bash check-many.sh https:// https://example.org
Web check on ubuntu-desktop
Checking: https://
curl: (3) URL rejected: No host part in the URL
Request failed
raf_0411@ubuntu-desktop:/tmp/bash-multi.tYZNzN$ printf 'status=%s\n' "$?"
status=1
```

Keep unexpected output; do not substitute predicted results. If stuck, preserve your partial script and ask for a hint.

## 4. Repair the guard

Preserve the original code/output above. The loop and curl conditional correctly checked both valid URLs and stopped at the first malformed URL. The guard still needs repair: `"$@"` expands into separate arguments, while `-z` expects one string. Restore the earlier first-argument test using `"$1"`; keep `"$@"` in the loop.

Update the usage message to name `check-many.sh` and indicate that additional URLs may follow.

Actual revised saved guard and usage block:

```bash
#! /usr/bin/env bash

if [ -z "$1" ]; then
    printf 'Usage: bash check-many.sh URL [URL ...]\n' >&2
    exit 2
fi

machine=$(hostname)

printf 'Web check on %s\n' "$machine"

for url in "$@"; do
   printf 'Checking: %s\n' "$url"
   if curl -I --max-time 10 "$url"; then
      printf 'Request completed\n'
   else
      printf 'Request failed\n' >&2
      exit 1
   fi
done
```

Test with no arguments, then with the same two HTTPS URLs. Capture each status immediately and record actual commands/output. Confirm that the two-URL run no longer emits the test error; do not rely solely on status 0.

```text
raf_0411@ubuntu-desktop:/tmp/bash-multi.tYZNzN$ bash check-many.sh
Usage: bash check-web.sh URL
raf_0411@ubuntu-desktop:/tmp/bash-multi.tYZNzN$ printf 'status=%s\n' "$?"
status=2
```

No need to repeat the malformed-URL test for this guard-only change; its loop behavior was already demonstrated. Tell the tutor when ready.
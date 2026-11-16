# Check every URL and remember failures — 2026-11-16

## Goal

Change your disposable `check-many.sh` from stopping at the first failure to checking every supplied URL. Its final status should be 1 if any curl request failed, otherwise 0.

You correctly predicted that simply removing `exit 1` would lose an earlier failure when a later iteration succeeds. Bash does not collect those failures automatically.

## The idea

```text
Start with 0 (no failure observed yet).
A successful request leaves the value unchanged.
A failed request sets it to 1.
After all requests, return that value.
```

Use these building blocks in the appropriate places:

- Before the loop: `overall_status=0`
- In the failure branch instead of `exit 1`: `overall_status=1`
- After the loop's `done`: `exit "$overall_status"`

Do not reset the variable in the success branch or at the start of each iteration. The missing/empty-first-argument guard must still exit immediately with status 2.

## 1. Edit and inspect — Ubuntu

Locate and inspect your existing script before editing. Its last verified location was `/tmp/bash-multi.tYZNzN/check-many.sh`; verify current availability. Modify only this disposable script's failure policy. Preserve the shebang, guard, usage text, heading, target labels, request options, and quoted arguments.

Paste the actual saved script:

```bash
#! /usr/bin/env bash

overall_status=0

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
      overall_status=1
   fi
done

exit "$overall_status"
```

## 2. A failure followed by a success

```bash
bash check-many.sh https:// https://example.org
```

Capture status immediately. Record actual commands/output, including whether both targets were attempted:

```text
raf_0411@ubuntu-desktop:/tmp/bash-multi.tYZNzN$ bash check-many.sh https:// https://example.org
Web check on ubuntu-desktop
Checking: https://
curl: (3) URL rejected: No host part in the URL
Request failed
Checking: https://example.org
HTTP/2 200 
date: Mon, 16 Nov 2026 13:23:48 GMT
content-type: text/html; charset=utf-8
server: cloudflare
last-modified: Mon, 16 Nov 2026 00:26:08 GMT
allow: GET, HEAD
accept-ranges: bytes
age: 13275
cache-control: max-age=14400
cf-cache-status: HIT
cf-ray: a5b6cff68a8e50fc-SIN
alt-svc: h3=":443"; ma=86400

Request completed
raf_0411@ubuntu-desktop:/tmp/bash-multi.tYZNzN$ printf 'status=%s\n' "$?"
status=1
```

## 3. Successful requests only

```bash
bash check-many.sh https://example.org https://example.com
```

Capture status immediately. Record actual commands/output:

```text
raf_0411@ubuntu-desktop:/tmp/bash-multi.tYZNzN$ bash check-many.sh https://example.org https://example.com
Web check on ubuntu-desktop
Checking: https://example.org
HTTP/2 200 
date: Mon, 16 Nov 2026 13:24:05 GMT
content-type: text/html; charset=utf-8
server: cloudflare
last-modified: Mon, 16 Nov 2026 00:26:08 GMT
allow: GET, HEAD
accept-ranges: bytes
age: 13292
cache-control: max-age=14400
cf-cache-status: HIT
cf-ray: a5b6d060ffa6f853-SIN
alt-svc: h3=":443"; ma=86400

Request completed
Checking: https://example.com
HTTP/2 200 
date: Mon, 16 Nov 2026 13:24:06 GMT
content-type: text/html; charset=utf-8
server: cloudflare
last-modified: Mon, 16 Nov 2026 00:26:08 GMT
allow: GET, HEAD
accept-ranges: bytes
age: 5
cf-cache-status: HIT
cf-ray: a5b6d0620c6e5c30-SIN
alt-svc: h3=":443"; ma=86400

Request completed
raf_0411@ubuntu-desktop:/tmp/bash-multi.tYZNzN$ printf 'status=%s\n' "$?"
status=0
```

These are real network checks, so record any unexpected result honestly. Do not alter a transcript to match the planned outcome. No need to rerun the unchanged missing-argument guard.

Tell the tutor when ready, or show your partial code if stuck.
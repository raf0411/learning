# Store and use command output — 2026-11-16

## Goal

Make your web check print the machine's hostname in its heading instead of on a separate line.

## New pattern

```bash
machine=$(hostname)
printf 'Host: %s\n' "$machine"
```

`$(hostname)` captures standard output. Assignment stores that text in a variable; there must be no spaces around `=`. Quoted variable expansion passes the value as one argument. A fixed printf format with `%s` treats the inserted value as data, rather than interpreting any percent signs inside that value as formatting instructions.

## Your change — Ubuntu

Locate and inspect your existing disposable script before editing. Its last verified location was `/tmp/bash-practice.e6ofDY/check-web.sh`; check rather than assuming it remains.

Keep the shebang, missing-input guard, and curl conditional unchanged. Replace the old heading and standalone hostname command with:

1. An assignment that captures hostname output in `machine`.
2. A printf command you write that inserts that value into the heading `Web check on HOSTNAME`, followed by a newline. Use `%s` for the insertion; do not hardcode this machine's name.

The sample above shows the syntax, but your heading should say `Web check on`, not `Host:`.

Actual saved script:

```bash
#!/usr/bin/env bash

if [ -z "$1" ]; then
    printf 'Usage: bash check-web.sh URL\n' >&2
    exit 2
fi

machine=$(hostname)

printf 'Web check on %s\n' "$machine"

if curl -I --max-time 10 "$1"; then
   printf 'Request completed\n'
else
   printf 'Request failed\n' >&2
   exit 1
fi
```

Run directly with `https://example.org` and immediately capture the script's exit status. Record actual commands and output:

```text
raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ ./check-web.sh https://example.org
Web check on ubuntu-desktop
HTTP/2 200 
date: Mon, 16 Nov 2026 12:36:05 GMT
content-type: text/html; charset=utf-8
server: cloudflare
last-modified: Mon, 16 Nov 2026 00:26:08 GMT
allow: GET, HEAD
accept-ranges: bytes
age: 10412
cache-control: max-age=14400
cf-cache-status: HIT
cf-ray: a5b68a101947fd1b-SIN
alt-svc: h3=":443"; ma=86400

Request completed
raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ printf 'status=%s\n' "$?"
status=0
```

Stop and tell the tutor when ready. If something fails, preserve the output and your attempted code.
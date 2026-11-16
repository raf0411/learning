# Give your script a URL — 2026-11-16

## Goal

Choose the URL when running the script, instead of editing the script for each website. Work in Ubuntu on your disposable `check-web.sh` only; no system changes are needed.

## New idea

With this invocation:

```bash
bash check-web.sh https://example.org
```

Inside the script, `$1` contains `https://example.org`. Use `"$1"` to pass that value as one argument to a command.

## 1. Make one change

Confirm your current directory and inspect your existing script before editing. Its last recorded directory was `/tmp/bash-practice.e6ofDY`; this is historical, not a guarantee it still exists.

Keep the heading, hostname command, HEAD request, and ten-second total timeout. Replace only curl's fixed URL with `"$1"`.

Inspect and paste the actual saved contents:

```bash
printf 'Web check\n'
hostname
curl -I --max-time 10 "$1"
```

## 2. Run with an argument

Run the invocation shown above. Immediately display its exit status using the command you already practiced.

Paste the actual command/output and status capture:

```text
raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ bash check-web.sh https://example.org
Web check
ubuntu-desktop
HTTP/2 200 
date: Mon, 16 Nov 2026 11:35:49 GMT
content-type: text/html; charset=utf-8
server: cloudflare
last-modified: Mon, 16 Nov 2026 00:26:08 GMT
allow: GET, HEAD
accept-ranges: bytes
age: 6796
cache-control: max-age=14400
cf-cache-status: HIT
cf-ray: a5b631c7df57f8d0-SIN
alt-svc: h3=":443"; ma=86400

raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ printf 'status=%s\n' "$?"
status=0
```

## 3. Handle an empty or missing first argument — guided

Your argument-based run succeeded, with HTTP 200 and immediate status 0. You also correctly predicted that omitting the URL makes `"$1"` expand to an empty string.

Add this supplied block before your existing commands in the disposable Ubuntu script:

```bash
if [ -z "$1" ]; then
    printf 'Usage: bash check-web.sh URL\n' >&2
    exit 2
fi
```

The test checks for an empty first argument. If empty, the block prints usage instructions to standard error and stops the script. Otherwise, execution continues. This is not full URL validation and does not yet reject extra arguments.

Inspect and record the complete saved script:

```bash
if [ -z "$1" ]; then
    printf 'Usage: bash check-web.sh URL\n' >&2
    exit 2
fi

printf 'Web check\n'
hostname
curl -I --max-time 10 "$1"
```

Run each command separately, capturing its exit status immediately before proceeding to the next test:

```bash
bash check-web.sh
```

```bash
bash check-web.sh https://example.org
```

Actual commands, output, and immediate status captures for both tests:

```text
raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ bash check-web.sh https://example.org
Web check
ubuntu-desktop
HTTP/2 200 
date: Mon, 16 Nov 2026 11:40:45 GMT
content-type: text/html; charset=utf-8
server: cloudflare
last-modified: Mon, 16 Nov 2026 00:26:08 GMT
allow: GET, HEAD
accept-ranges: bytes
age: 7092
cache-control: max-age=14400
cf-cache-status: HIT
cf-ray: a5b63900fa617ccb-SIN
alt-svc: h3=":443"; ma=86400

raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ printf 'status=%s\n' "$?"
status=0
raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ bash check-web.sh
Usage: bash check-web.sh URL
raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ printf 'status=%s\n' "$?"
status=2
```

Stop here and tell the tutor when ready.

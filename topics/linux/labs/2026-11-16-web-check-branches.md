# Report the request outcome — 2026-11-16

## Goal

Use a command's exit status to select between two actions. Work only on your disposable Ubuntu `check-web.sh`.

## Pattern

```bash
if command; then
    # Actions when command returns 0
else
    # Actions when command returns nonzero
fi
```

`if` runs the command and examines its status. A nonzero status chooses the `else` branch; it does not automatically stop the script.

## 1. Write the change yourself

Locate and inspect your existing script before editing. Its last recorded location was `/tmp/bash-practice.e6ofDY/check-web.sh`; verify availability rather than assuming it remains.

Keep your existing missing/empty-argument guard, heading, and hostname command.

Replace the final standalone curl command with an `if/else` structure:

- Use the same bounded HTTPS-capable HEAD command with `"$1"` as the condition. Do not run curl twice.
- On curl status 0, print `Request completed` followed by a newline.
- On curl nonzero status, print `Request failed` followed by a newline to standard error, then explicitly stop the script with status **1**.

Here, status 1 is your script's general request-failure code, not a promise to preserve curl's original numeric code. The existing guard should still use status 2 for missing input. Also, curl status 0 means the transfer completed; without additional options it does not necessarily mean an HTTP 2xx response.

Inspect and paste your actual saved script:

```bash
if [ -z "$1" ]; then
    printf 'Usage: bash check-web.sh URL\n' >&2
    exit 2
elif [ "$1" -ne 0 ]; then
   printf 'Request failed\n' >&2
   exit 1
fi

printf 'Web check\n'
hostname
curl -I --max-time 10 "$1"
printf 'Request completed\n'
```

## 2. Test both outcomes

Run each test separately and capture its exit status immediately. The second input is deliberately an incomplete URL, intended to exercise the failure branch without changing any network settings.

```bash
bash check-web.sh https://example.org
```

```bash
bash check-web.sh https://
```

Paste actual command/output and immediate status capture for both tests. Record unexpected results honestly rather than replacing them with expected ones.

```text
raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ bash check-web.sh https://example.org
check-web.sh: line 4: [: https://example.org: integer expected
Web check
ubuntu-desktop
HTTP/2 200 
date: Mon, 16 Nov 2026 12:02:25 GMT
content-type: text/html; charset=utf-8
server: cloudflare
last-modified: Mon, 16 Nov 2026 00:26:08 GMT
allow: GET, HEAD
accept-ranges: bytes
age: 8392
cache-control: max-age=14400
cf-cache-status: HIT
cf-ray: a5b658bc7b924604-SIN
alt-svc: h3=":443"; ma=86400

Request completed
raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ printf 'status=%s\n' "$?"
status=0
raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ bash check-web.sh https://
check-web.sh: line 4: [: https://: integer expected
Web check
ubuntu-desktop
curl: (3) URL rejected: No host part in the URL
Request completed
raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ printf 'status=%s\n' "$?"
status=0
```

## 3. Repair after feedback

Preserve your original code and output above. They demonstrate two problems:

- `$1` is URL text, not curl's exit status; `-ne` expects integers. The added comparison also ran before curl.
- The completion printf ran unconditionally after curl, masking its failure with status 0.

Keep the original empty-argument guard, removing the added `elif` branch. After the heading and hostname, use a separate `if/else` with the actual curl command as its condition. Put each message in its corresponding branch, and explicitly exit 1 in the failure branch. Do not leave a second standalone curl call or an unconditional completion message.

Structural hint (replace the placeholder; this is not runnable code):

```text
if YOUR_CURL_COMMAND_HERE; then
    # Print the completion message
else
    # Print the failure message to stderr, then exit 1
fi
```

Actual revised saved script:

```bash
if [ -z "$1" ]; then
    printf 'Usage: bash check-web.sh URL\n' >&2
    exit 2
fi

printf 'Web check\n'
hostname

if curl -I --max-time 10 "$1"; then
   printf 'Request completed\n'
else
   printf 'Request failed\n' >&2
   exit 1
fi
```

Rerun the same two tests, capturing each status immediately. Append the actual commands/output here:

```text
raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ bash check-web.sh https://example.org
Web check
ubuntu-desktop
HTTP/2 200 
date: Mon, 16 Nov 2026 12:12:29 GMT
content-type: text/html; charset=utf-8
server: cloudflare
last-modified: Mon, 16 Nov 2026 00:26:08 GMT
allow: GET, HEAD
accept-ranges: bytes
age: 8996
cache-control: max-age=14400
cf-cache-status: HIT
cf-ray: a5b6677b8d90b403-SIN
alt-svc: h3=":443"; ma=86400

Request completed
raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ printf 'status=%s\n' "$?"
status=0
raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ bash check-web.sh https://
Web check
ubuntu-desktop
curl: (3) URL rejected: No host part in the URL
Request failed
raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ printf 'status=%s\n' "$?"
status=1
```

Tell the tutor when ready, or ask for another hint.

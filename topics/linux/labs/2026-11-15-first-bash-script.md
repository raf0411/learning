# First Bash script — 2026-11-15

## Goal

Create a small reusable web check in the Ubuntu VM. This is a disposable script containing read-only commands, not a system configuration change.

## 1. Prepare — Ubuntu terminal

Run this single supplied setup line. It creates a fresh directory and moves this shell into it:

```bash
script_lab=$(mktemp -d /tmp/bash-practice.XXXXXX) && cd "$script_lab" && pwd
```

Record the actual directory:

/tmp/bash-practice.e6ofDY

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
printf 'Web check\n'
printf "$(hostname)\n"
printf "$(curl -I --max-time 10 https://example.com)\n"
```

## 3. Execute and capture status

Run:

```bash
bash check-web.sh
```

**Immediately afterward**, use your own command to display its shell exit status, before running anything else. If you forget and run another command, acknowledge that and rerun the script before capturing status; do not guess the earlier value.

Record the execution command, output, and immediate status-capture command/output:

```text
raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ bash check-web.sh
Web check
ubuntu-desktop
  % Total    % Received % Xferd  Average Speed  Time    Time    Time   Current
                                 Dload  Upload  Total   Spent   Left   Speed
  0      0   0      0   0      0      0      0                              0
HTTP/1.1 200 OK
Date: Mon, 16 Nov 2026 11:19:22 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
Server: cloudflare
Last-Modified: Mon, 16 Nov 2026 00:30:20 GMT
Allow: GET, HEAD
Accept-Ranges: bytes
Age: 9
cf-cache-status: HIT
CF-RAY: a5b619abfa8e68b7-SIN
alt-svc: h3=":443"; ma=86400

raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ printf 'status=%s\n' "$?"
status=0
```

## 4. Interpret

Did this particular HTTPS request succeed? Identify the evidence without claiming that every feature of the website works.

the request succeed because we got 200 status code OK

Help used beyond these supplied instructions (manuals, tutor hints, etc.):

none

Stop here and tell the tutor when ready. Keep the script for the next step; do not add arguments, loops, or conditionals yet.

## 5. Review and targeted repair

Tutor feedback: the script ran, the immediate status capture was correct, and HTTP 200 supports success of this particular HEAD request. However, the final command was `printf`, so the recorded script status reflects that wrapper rather than directly reporting curl's status. In the follow-up quiz, you correctly identified that a successful final printf can hide curl's failure.

Keep the original evidence above unchanged.

In Ubuntu, first confirm your current directory and inspect `check-web.sh`; do not assume the temporary directory still exists. Edit only your disposable script:

- Keep the heading command.
- Run `hostname` and the bounded HTTPS HEAD request directly, without wrapping them in `printf` or `$()`.
- Inspect the saved file, run it with Bash, and immediately capture its status again.

Actual saved script:

```bash
printf 'Web check\n'
hostname
curl -I --max-time 10 example.com
```

Actual execution and immediate status capture:

```text
raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ bash check-web.sh
Web check
ubuntu-desktop
HTTP/1.1 200 OK
Date: Mon, 16 Nov 2026 11:24:12 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
Age: 6
Server: cloudflare
Last-Modified: Mon, 16 Nov 2026 00:30:20 GMT
Allow: GET, HEAD
Accept-Ranges: bytes
cf-cache-status: HIT
CF-RAY: a5b620c34fdf3102-SIN
alt-svc: h3=":443"; ma=86400
raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ printf 'status=%s\n' "$?"
status=0
```

Which command now determines the script's exit status when it reaches its end normally?

bash check-web.sh, this command determines the result of the last status printf status=0

Tell the tutor when this section is ready.

## 6. Small correction — HTTPS and status origin

Tutor feedback: wrapper removal and immediate capture are correct. The revised request omitted `https://`, so it did not establish HTTPS success. When this script reaches its end normally, its final `curl` supplies the script's exit status; the outer shell receives that status from `bash check-web.sh`.

Preserve the previous evidence. Restore the explicit HTTPS URL in your disposable script, inspect its saved contents, rerun, and immediately capture status.

Saved contents and actual execution/status transcript:

```text
printf 'Web check\n'
hostname
curl -I --max-time 10 https://example.com

raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ bash check-web.sh
Web check
ubuntu-desktop
HTTP/2 200 
date: Mon, 16 Nov 2026 11:28:05 GMT
content-type: text/html; charset=utf-8
server: cloudflare
last-modified: Mon, 16 Nov 2026 00:26:08 GMT
allow: GET, HEAD
accept-ranges: bytes
age: 4
cf-cache-status: HIT
cf-ray: a5b6266fad45f930-SIN
alt-svc: h3=":443"; ma=86400

raf_0411@ubuntu-desktop:/tmp/bash-practice.e6ofDY$ printf 'status=%s\n' "$?"
status=0
```

Complete in your own words: The printed status comes from ______ inside the script, passed back through ______ to my terminal shell.

what to complete? i dont even know ur question? are u dumb? please be a better teacher next time!

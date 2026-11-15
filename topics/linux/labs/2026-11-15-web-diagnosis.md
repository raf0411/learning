# Web connectivity investigation — 2026-11-15

## Goal

From **Ubuntu**, independently check two separate things about `example.com`:

1. Can Ubuntu's configured name-resolution system return an IPv4 address for it?
2. Can you obtain an HTTP response over HTTPS from `https://example.com`?

Use read-only diagnostic commands. Do not install software, change settings, disable certificate verification, or use sudo. Local manuals are allowed. If a command is unavailable or fails, preserve the error and stop for review rather than changing the system.

## 1. Name resolution

Choose a command and record its actual output:

```text
raf_0411@ubuntu-desktop:~$ getent hosts example.com
2606:4700:10::6814:179a example.com
2606:4700:10::ac42:93f3 example.com
raf_0411@ubuntu-desktop:~$ resolvectl query example.com
example.com: 172.66.147.243                    -- link: enp0s8
             104.20.23.154                     -- link: enp0s8
             2606:4700:10::ac42:93f3           -- link: enp0s8
             2606:4700:10::6814:179a           -- link: enp0s8

-- Information acquired via protocol DNS in 45.1ms.
-- Data is authenticated: no; Data was acquired via local or encrypted transport: no
-- Data from: cache network
```

What does this result establish? Does it establish that the website responds?

i think it establish that the website exists but not meaning it responded

## 2. HTTPS

Choose a command that requests **response headers without downloading the response body**. Use the local manual to add a **maximum total duration of 10 seconds** so the check cannot hang indefinitely.

Record your command and actual output:

```text
curl -I --connect-timeout 10 https://example.com
```

What does the result establish at the time of your check? If it failed, identify the stage indicated by the actual error rather than guessing a cause.

raf_0411@ubuntu-desktop:~$ curl -I --connect-timeout 10 https://example.com
HTTP/2 200 
date: Sun, 15 Nov 2026 12:32:02 GMT
content-type: text/html; charset=utf-8
server: cloudflare
last-modified: Thu, 12 Nov 2026 21:56:22 GMT
allow: GET, HEAD
accept-ranges: bytes
age: 8
cf-cache-status: HIT
cf-ray: a5ae46bedcf7fa28-SIN
alt-svc: h3=":443"; ma=86400
raf_0411@ubuntu-desktop:~$ curl -I --max-time 10 https://example.com
HTTP/2 200 
date: Sun, 15 Nov 2026 12:35:14 GMT
content-type: text/html; charset=utf-8
server: cloudflare
last-modified: Thu, 12 Nov 2026 21:56:22 GMT
allow: GET, HEAD
accept-ranges: bytes
age: 0
cf-cache-status: HIT
cf-ray: a5ae4b6ffc9740e8-SIN
alt-svc: h3=":443"; ma=86400

## Help used

Record manual pages, hints, or other help used. Write “none” only if none was used.

man getent
man resolvectl
man curl /--connect-timeout

Stop here and tell the tutor when ready. Do not attempt repairs or repeat the previous SSH transfer.

# Network diagnosis checkpoint — 2026-11-15

## Incident

A task on Ubuntu cannot retrieve response headers from:

```text
https://reports.invalid
```

This is a deliberate test target, not a production incident. Investigate the failure using **actual Ubuntu output**, rather than assuming its cause.

Your goal is to identify the earliest failing stage supported by your evidence, and distinguish it from stages you have not tested successfully.

## Boundaries

- Run commands in **Ubuntu**.
- Use at most **three diagnostic commands**; manual/help lookups and exit-status capture do not count toward this limit.
- Bound any web request to **10 seconds total**.
- Do not use sudo, install software, modify configuration, disable certificate checks, or submit credentials.
- You may compare with `https://example.com` if useful.
- Do not try to repair anything yet. If the evidence is ambiguous, report that rather than inventing a cause.

## 1. Choose and investigate

Choose your own tools. Before each command, briefly state what it will test. Record the actual command and complete relevant output, including errors. You do not need to use all three slots.

### Check 1

What this tests:

This tests if the name resolver even exists

```text
raf_0411@ubuntu-desktop:~$ resolvectl query https://reports.invalid
reports.invalid: Name 'reports.invalid' not found
raf_0411@ubuntu-desktop:~$ resolvectl query example.com
example.com: 104.20.23.154                     -- link: enp0s8
             172.66.147.243                    -- link: enp0s8
             2606:4700:10::ac42:93f3           -- link: enp0s8
             2606:4700:10::6814:179a           -- link: enp0s8

-- Information acquired via protocol DNS in 50.9ms.
-- Data is authenticated: no; Data was acquired via local or encrypted transport: no
-- Data from: cache network
```

### Check 2 (if useful)

What this tests:

It tests if we get a response in a form of the header of the website, not the whole body, and it only limits 10 seconds of maximum timeout

```text
raf_0411@ubuntu-desktop:~$ curl -I --max-time 10 https://reports.invalid
curl: (6) Could not resolve host: reports.invalid
raf_0411@ubuntu-desktop:~$ curl -I --max-time 10 reports.invalid
curl: (6) Could not resolve host: reports.invalid
raf_0411@ubuntu-desktop:~$ curl -I --max-time 10 example.com
HTTP/1.1 200 OK
Date: Sun, 15 Nov 2026 13:25:18 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
Server: cloudflare
Last-Modified: Sat, 14 Nov 2026 20:05:46 GMT
Allow: GET, HEAD
Accept-Ranges: bytes
Age: 0
cf-cache-status: HIT
CF-RAY: a5ae94c92a3fce57-SIN
alt-svc: h3=":443"; ma=86400
```

### Check 3 (if useful)

What this tests:

Similar to check 1, we are checking if we got any name resolver

```text
raf_0411@ubuntu-desktop:~$ getent hosts reports.invalid
raf_0411@ubuntu-desktop:~$ getent hosts example.com
2606:4700:10::6814:179a example.com
2606:4700:10::ac42:93f3 example.com
```

## 2. Exit status

For the failed web request, capture its exit status **immediately after the request**, before another command replaces it. Include that capture in the transcript above.

What status did you observe, and what does the tool's local documentation say it means?

I got a status (6) in the curl, which the manual says it "Could not resolve host. The given remote host could  not  be resolved."

## 3. Diagnosis

In two or three sentences:

- What is the earliest failing stage your evidence identifies?
- What remains unverified about the intended server or application?
- Does your evidence justify changing Ubuntu's network settings? Why or why not?

It doesn't have a name resolve and the website didn't gave any HEAD response when we curl. It proves that the failure is specific to the requested name, as you can see we get the resolver with example.com for curl, getent, and resolvectl

## Help used

Record manuals, hints, or other help used. Asking for a hint is fine; it lets us distinguish independent work from guided work.

man curl

Stop here and tell the tutor when ready. No repairs or extra experiments are required.

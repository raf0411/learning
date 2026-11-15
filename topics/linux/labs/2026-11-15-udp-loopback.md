# One UDP datagram — 2026-11-15

## Goal and safety

Observe one UDP message between two terminals **inside the same Ubuntu VM**. No Mac-side commands, sudo, package installation, forwarding changes, or firewall changes.

This creates a temporary UDP receiver bound only to `127.0.0.1:49152`. It exits after receiving one datagram. Stop it with Ctrl-C if you abandon the exercise. Do not terminate other processes.

Verified from learner's `nc -h`: OpenBSD netcat, Debian patchlevel 1.234-1; supports `-4`, `-u`, `-l`, `-n`, `-W recvlimit`, and `-w timeout`.

## 1. Check the port — Ubuntu terminal A

Read-only check for existing UDP listeners on the proposed port:

```bash
ss -H -uln 'sport = :49152'
```

If any row appears, **stop and share it**. Do not replace or stop an existing listener. If there is no output, continue.

Actual output (write `no output` if empty):

```text
no output
```

## 2. Start the receiver — Ubuntu terminal A

```bash
nc -4 -u -l -n -W 1 127.0.0.1 49152
```

- `-4`: IPv4; `-u`: UDP; `-l`: receive/listen mode; `-n`: numeric addresses.
- `-W 1`: exit after receiving one packet.

Leave this command running. A blank terminal waiting without a shell prompt is expected. If it reports an error, stop and share the error.

## 3. Inspect the receiver — Ubuntu terminal B

```bash
ss -H -uln 'sport = :49152'
```

Record actual output. Before sending, confirm that the local endpoint is **127.0.0.1:49152**. If it differs or no row appears, stop and share the result.

```text
raf_0411@ubuntu-desktop:~$ ss -H -uln 'sport = :49152'
UNCONN     0          0              127.0.0.1:49152         0.0.0.0:*
```

## 4. Predict, then send — Ubuntu terminal B

What text do you expect to appear in terminal A after this command? Write your prediction before running it.

it exits because it receives a packet from terminal B

Run this as one physical command line:

```bash
printf 'UDP practice\n' | nc -4 -u -n -w 2 127.0.0.1 49152
```

`-w 2` bounds idle network waiting for the sender. It may briefly wait before returning to the shell. No response from the receiver is required in this exercise.

Record terminal B's command and output (or note no output):

```text
raf_0411@ubuntu-desktop:~$ ss -H -uln 'sport = :49152'
UNCONN     0          0              127.0.0.1:49152         0.0.0.0:*     
raf_0411@ubuntu-desktop:~$ printf 'UDP practice\n' | nc -4 -u -n -w 2 127.0.0.1 49152

```

Record terminal A's command and actual received output. Note whether its shell prompt returned:

```text
raf_0411@ubuntu-desktop:~$ 
raf_0411@ubuntu-desktop:~$ ss -H -uln 'sport = :49152'
raf_0411@ubuntu-desktop:~$ nc -4 -u -l -n -W 1 127.0.0.1 49152
UDP practice         
raf_0411@ubuntu-desktop:~$ 
```

If terminal A remains waiting without receiving the message, stop it with Ctrl-C and report what happened; do not assume success or retry repeatedly.

## 5. Verify the receiver is gone — Ubuntu terminal B

```bash
ss -H -uln 'sport = :49152'
```

Record actual output:

```text
raf_0411@ubuntu-desktop:~$ ss -H -uln 'sport = :49152'
raf_0411@ubuntu-desktop:~$ 
```

## 6. Interpret

Which observation establishes that this particular datagram reached the receiver? What does it *not* establish about future UDP messages?

when the terminal A receive the packet and shows UDP practice, it means the datagram reached the receiver, what does it not establish I don't know to be honest

Help used beyond these supplied instructions:

None

Stop here and tell the tutor when ready. Do not leave the receiver running if ending the exercise.

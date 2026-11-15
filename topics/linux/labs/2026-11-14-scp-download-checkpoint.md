# SCP download checkpoint — 2026-11-14

## Goal

Download the existing Ubuntu practice file into a new temporary directory on your Mac, then verify its contents against the remote file. Leave both originals unchanged. Do not change SSH or VirtualBox settings.

This follows a guided upload. Download direction was correctly recognized in a quiz, but the Mac-side connection port needed correction. Prepared November 14; resumed November 15. This tests command construction after spacing, with endpoint details supplied—not independent endpoint selection.

## Known setup

- Run commands from your **Mac shell**, not an interactive Ubuntu SSH shell.
- Ubuntu user: `raf_0411`.
- Mac-side SSH endpoint: `127.0.0.1`, TCP port `2222`.
- VirtualBox forwards that endpoint to Ubuntu TCP port `22`.
- Current Ubuntu source: `/tmp/ssh-receive.vpIV1i/message.txt` (created and repaired November 15).
- Verified displayed content: `Fresh download practice` (written with a trailing newline).
- Current SHA-256 has not yet been measured. The historical file's digest does not apply.
- Temporary files can disappear; stop and inspect if the source is missing.

## 0. Check current availability — November 15

Ensure the Ubuntu VM is running. From your **Mac shell**, run this read-only check of remote identity and source-file availability:

```bash
ssh -p 2222 raf_0411@127.0.0.1 'hostname; ls -l /tmp/ssh-receive.iqJACf/message.txt'
```

Record the command and actual output, never your password:

```text
raffi@Raffis-Mac ~ % ssh -p 2222 raf_0411@127.0.0.1 'hostname; ls -l /tmp/ssh-receive.iqJACf/message.txt'
raf_0411@127.0.0.1's password:
ubuntu-desktop
ls: cannot access '/tmp/ssh-receive.iqJACf/message.txt': No such file or directory
```

Observed November 15: authentication and remote execution succeeded; the previous source path is absent. An earlier attempt omitted the slash after `/tmp`; the corrected check above independently confirms absence. Cause unknown. Tutor supplied fresh temporary-source creation; execution returned `/tmp/ssh-receive.vpIV1i/message.txt`. Pasted border characters (`│ │`) became arguments to `printf`, and supplied read-only inspection displayed `│`. A supplied targeted replacement repaired this disposable source; learner recorded:

```text
raffi@Raffis-Mac ~ % ssh -p 2222 raf_0411@127.0.0.1 'printf "Fresh download practice\n" > /tmp/ssh-receive.vpIV1i/message.txt && cat /tmp/ssh-receive.vpIV1i/message.txt'
raf_0411@127.0.0.1's password:
Fresh download practice
```

Source preparation is complete with guidance. Continue at section 1 using the **current source** in Known setup. Do not repeat the historical availability command or use the historical source digest.

If the connection fails, the source is missing, or SSH reports a changed host key, stop and share the exact message. Do not change settings or bypass host-key checks. If an unfamiliar trust prompt appears, stop so we can verify the fingerprint first.

## 1. Prepare a safe local destination

On your Mac, run this supplied setup command:

```bash
mktemp -d /tmp/ssh-download.XXXXXX
```

Record the returned path:

/tmp/ssh-download.G25Bbw

## 2. Construct and execute the download

Write your own `scp` command using the known setup and the actual new directory above. Keep the entire command on one physical line. You may consult local documentation; record any help used. Do not paste an explanatory syntax template as a command.

Paste your command and actual output (never your password):

```text
raffi@Raffis-Mac ssh-download.G25Bbw % scp -P 2222 /tmp/ssh-download.G25Bbw raf_0411@127.0.0.1:/tmp/ssh-receive.vpIV1i/message.txt
raf_0411@127.0.0.1's password:
scp: local "/tmp/ssh-download.G25Bbw" is not a regular file
scp: failed to upload file /tmp/ssh-download.G25Bbw to /tmp/ssh-receive.vpIV1i/message.txt

raffi@Raffis-Mac ssh-download.G25Bbw % scp -P 2222 raf_0411@127.0.0.1:/tmp/ssh-receive.vpIV1i/message.txt /tmp/ssh-download.G25Bbw
raf_0411@127.0.0.1's password:
message.txt                            100%   24    30.8KB/s   00:00
```

## 3. Verify

Choose commands to calculate the downloaded file's SHA-256 on the Mac and freshly retrieve the source file's SHA-256 from Ubuntu. Record both commands and outputs, not just the transfer progress message.

```text
raffi@Raffis-Mac ssh-download.G25Bbw % shasum -a 256 /tmp/ssh-download.G25Bbw/message.txt
c6cfcf5f835445fde7c5a67c511f95fd6ffaf321e0b68ba8b6e3a1da6b9b63dc  /tmp/ssh-download.G25Bbw/message.txt
raffi@Raffis-Mac ssh-download.G25Bbw % ssh -p 2222 raf_0411@127.0.0.1 'shasum -a 256 /tmp/ssh-receive.vpIV1i/message.txt'
raf_0411@127.0.0.1's password:
c6cfcf5f835445fde7c5a67c511f95fd6ffaf321e0b68ba8b6e3a1da6b9b63dc  /tmp/ssh-receive.vpIV1i/message.txt
```

Do the hashes match? What does the evidence establish?

Same, i shasum in my mac and ssh the ubuntu and it has the same sha-256 code thingy in both machine

Help or documentation used:

NONE

Stop here. Keep the files for review; no cleanup or additional configuration changes are required.

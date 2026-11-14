# SCP download checkpoint — 2026-11-14

## Goal

Download the existing Ubuntu practice file into a new temporary directory on your Mac, then verify its contents against the remote file. Leave both originals unchanged. Do not change SSH or VirtualBox settings.

This follows a guided upload. Download direction was correctly recognized in a quiz, but the Mac-side connection port needed correction. This task tests application after that correction, not spaced retention.

## Known setup

- Run commands from your **Mac shell**, not an interactive Ubuntu SSH shell.
- Ubuntu user: `raf_0411`.
- Mac-side SSH endpoint: `127.0.0.1`, TCP port `2222`.
- VirtualBox forwards that endpoint to Ubuntu TCP port `22`.
- Existing Ubuntu source: `/tmp/ssh-receive.iqJACf/message.txt`.
- Previously observed source SHA-256: `05834afe5c5295a2d469fa2cf1b7d667c35f10e55fa8384a1c78830a7b4a2ad3`.
- Temporary files can disappear; stop and inspect if the source is missing.

## 1. Prepare a safe local destination

On your Mac, run this supplied setup command:

```bash
mktemp -d /tmp/ssh-download.XXXXXX
```

Record the returned path:

TODO

## 2. Construct and execute the download

Write your own `scp` command using the known setup and the actual new directory above. Keep the entire command on one physical line. You may consult local documentation; record any help used. Do not paste an explanatory syntax template as a command.

Paste your command and actual output (never your password):

```text
TODO
```

## 3. Verify

Choose commands to calculate the downloaded file's SHA-256 on the Mac and freshly retrieve the source file's SHA-256 from Ubuntu. Record both commands and outputs, not just the transfer progress message.

```text
TODO
```

Do the hashes match? What does the evidence establish?

TODO

Help or documentation used:

TODO

Stop here. Keep the files for review; no cleanup or additional configuration changes are required.

# STATE

Updated: 2026-08-26

## Current stage

Initial probe and roadmap complete. Phase 1 (Linux command line and filesystem)
is active. One concept was introduced: commands operate on their path arguments,
and creating a directory does not enter it. This has not yet been demonstrated
in the Ubuntu lab.

Last session: `sessions/2026-08-26.md`

## Environment and capacity

- Uses macOS Terminal and has an Ubuntu homelab server.
- Can study about 5 hours daily.
- Prefers practical, job-oriented learning.

## Demonstrated knowledge

- Understands the distinction between absolute and relative paths.
- Uses `whoami`, `pwd`, `ls`, `neofetch`, `top`, and `htop` at a basic level.
- Can create files/directories and copy/delete files with basic commands.
- Knows the standard `ssh user@address` form.
- Has used `apt` to update and upgrade Ubuntu packages.
- Has used a pipe with `grep` and edits with `nano`.
- Understands the broad purpose of DNS and can use `curl` as an initial web
  check.
- Reports being comfortable with Git; has tried Bash, Docker, databases, SSH
  keys, and firewalls.

## Partial or missing foundations

- Needs practice with command targets and current working directory; file
  moves/renames and safe file operations are not yet reliable.
- Does not yet understand Unix permission notation and ownership reliably.
- Process, service, `systemd`, and `systemctl` concepts are conflated.
- Does not yet know the core commands for resource, OS, network, and log
  inspection.
- Networking knowledge is early: localhost, private addressing, gateways,
  ports, and troubleshooting need development.
- Little demonstrated experience configuring services or diagnosing homelab
  failures.
- Redirection, configuration files, virtualization, cloud platforms, web
  servers, and operational routines need structured practice.

## Teaching approach

Move one concept at a time. Require predictions and terminal work, then test
without hints. Revisit weak concepts through short retrieval questions.

## Next action

Give a short retrieval check on paths and working-directory state. Then resume
the pending `sysadmin-lab-01` file-management exercise on the Ubuntu server.

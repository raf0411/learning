# REVIEW

Updated: 2026-08-26

## Active review queue

These were identified during the initial probe:

1. Command targets and current-directory state: creating a directory does not
   change into it; relative targets depend on the current directory. Introduced
   on 2026-08-26; practical demonstration still pending.
2. Moving and renaming files safely. Not yet taught.
3. User/group/other permission notation, ownership, and the meaning of
   read/write/execute for files versus directories.
4. Program versus process versus daemon/service; the roles of `systemd` and
   `systemctl`.
5. System inspection: OS, memory, disk, processes, addresses, sockets, and logs.
6. Localhost, private addresses, ports, gateways, and layered connectivity
   troubleshooting.
7. Standard streams, pipelines, and output/error redirection.

Re-test each item after its lesson, again several sessions later, and during an
unfamiliar troubleshooting scenario.

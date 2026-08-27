# REVIEW

Updated: 2026-08-27

## Active review queue

These were identified during the initial probe:

1. Command targets and current-directory state: creating a directory does not
   change into it; relative targets depend on the current directory. Retrieved
   correctly in words on 2026-08-26 and demonstrated successfully on Ubuntu on
   2026-08-27.
   Briefly confused `touch practice/notes.txt` with the invalid no-space form
   `touch/practice/notes.txt`, so reinforce command/argument separation.
   On 2026-08-27, wrote `~/home/raffi/...`, then correctly explained after one
   correction that `~` expands to the current user's home directory. Re-test in
   a later session. In the copy exercise that day, used bare `backups` while
   still in the home directory; reinforce that every relative source and
   destination path is resolved independently from the current directory. The
   corrected live command accidentally contained a second `cp` word, which was
   treated as a source operand. The learner identified the single command but
   grouped `cp sysadmin-lab-01/backups/` as one argument; reinforce that each
   unquoted whitespace-separated word is a separate argument. Immediate re-test
   correctly separated the arguments, but the learner could not yet explain
   how `cp` assigns multiple source arguments and the final destination. After
   teaching, correctly predicted both retained sources and both destination
   copies; re-test later. Wrote `extra/` once for a file named `extra`, so
   reinforce that a trailing slash denotes a directory path.
2. Renaming a file with `mv SOURCE DESTINATION`: predicted, explained, and
   demonstrated successfully on 2026-08-27. Collision-safe moving with `mv -i`
   was then demonstrated by declining an overwrite and verifying both paths.
   The learner then moved the file into a new `archive/` directory and verified
   that the separate backup remained. Re-test later in a new scenario.
3. Collision-safe copying: used installed `cp --help` documentation to identify
   `-i`, correctly predicted the overwrite prompt, and declined it successfully
   on 2026-08-27. Re-test later without prompting.
4. Safe file deletion: predicted the scope of `rm -i`, declined once, then
   accepted deletion of the archive copy and verified that the backup remained
   on 2026-08-27. Initially answered an absolute-path question with a relative
   path; re-test exact path construction later. Also correctly used `rmdir` to
   remove an empty directory and interpreted its refusal to remove a non-empty
   backup directory.
5. User/group/other permission notation, ownership, and the meaning of
   read/write/execute for files versus directories.
6. Program versus process versus daemon/service; the roles of `systemd` and
   `systemctl`.
7. System inspection: OS, memory, disk, processes, addresses, sockets, and logs.
8. Localhost, private addresses, ports, gateways, and layered connectivity
   troubleshooting.
9. Standard streams, pipelines, and output/error redirection.

Re-test each item after its lesson, again several sessions later, and during an
unfamiliar troubleshooting scenario.

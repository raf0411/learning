# REVIEW

Updated: 2026-08-29

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
   reinforce that a trailing slash denotes a directory path. On 2026-08-28,
   correctly expanded an exact home-relative path and completed an unprompted
   transfer using nested relative paths without changing directories. Move this
   item to spaced review rather than immediate remediation.
2. Renaming a file with `mv SOURCE DESTINATION`: predicted, explained, and
   demonstrated successfully on 2026-08-27. Collision-safe moving with `mv -i`
   was then demonstrated by declining an overwrite and verifying both paths.
   The learner then moved the file into a new `archive/` directory and verified
   that the separate backup remained. Re-test later in a new scenario.
3. Collision-safe copying: used installed `cp --help` documentation to identify
   `-i`, correctly predicted the overwrite prompt, and declined it successfully
   on 2026-08-27. Re-tested without a command hint on 2026-08-28: selected
   `cp -i`, declined the overwrite, and verified both files. Re-test later in an
   unfamiliar scenario.
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
9. Standard streams, pipelines, and output/error redirection: on 2026-08-28,
   correctly explained and demonstrated left-to-right pipeline flow. Initially
   could not distinguish standard output from standard error, split one long
   command at the wrong point, and described `>`/`2>` as appending. After a
   diagram and simpler retry, correctly explained how one `ls` routes its valid
   result through `>` and its missing-path error through `2>`, then selected
   `2>>` when error output must be appended. On 2026-08-29, the opening
   prediction again confused the two destinations, but the learner immediately
   transferred the corrected mapping to a new `grep` example and verified it.
   During the append check, Enter was pressed after `>>`; Bash then treated
   `matches.txt 2>> diagnostics.txt` as a separate command and captured its
   `command not found` diagnostic. The three-line history was inspected and
   explained, but the clean append re-test remains unfinished. Begin the next
   session with command-boundary and stream-routing retrieval, then complete it.
10. Command-specific option semantics: on 2026-08-28, transferred the syntax of
    `head -n 5` to `grep` by running `grep -n 5 bin/bash /etc/passwd`. Correctly
    repaired it to `grep -n bin/bash /etc/passwd` after learning that `grep -n`
    is a standalone flag, making `5` the unintended pattern and `bin/bash` an
    unintended file operand. On 2026-08-29, initially repeated the line-count
    assumption, then established that each command owns its option meanings.
    Used `man grep` to find the exact definition of `-n`, demonstrated the
    numbered output, and correctly parsed a new multi-file command after one
    correction of the old malformed command. Move this to spaced review using
    an unfamiliar command option.
11. Command type and documentation source: on 2026-08-29, initially predicted
    that `head`, `grep`, and `cd` were all Bash builtins because they can all be
    used in scripts. `type` and `type -a` showed an external executable, an
    alias with underlying paths, and a builtin. The learner then correctly chose
    `help cd`, `head --help` or `man head`, and `grep --help` or `man grep`.
    Re-test later with a different builtin and external command.

Begin the next session with short retrieval from item 9, especially the command
boundary created by Enter, then complete the clean append check. Re-test items
10 and 11 after a delay and during an unfamiliar troubleshooting scenario.

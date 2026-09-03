# REVIEW

Updated: 2026-09-03

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
   During the Phase 1 exit check on 2026-09-03, omitted the slash after `~` in
   one output path (`~phase1-exit` rather than `~/phase1-exit`). This caused the
   final redirection to fail. The learner identified the missing slash after
   diagnosis; re-test the meaning of `~/` versus `~name/` later.
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
   read/write/execute for files versus directories. The 2026-09-03 Phase 2
   probe found a sound foundation in `whoami`, group membership, command-scoped
   `sudo`, and least privilege. The learner identified the owner and owning
   group in an `ls -l` entry but could not decode its type marker or permission
   triplets. They treated a group member as having the owner's access, expected
   an owner to fall back to group permissions, thought regular-file `x` meant
   deletion, and assumed directory `rwx` had the same meanings as file `rwx`.
   They initially recognized `chmod`, `chown`, and `chgrp` but could not
   distinguish them. During the lesson, class selection needed two focused
   repairs and least privilege needed one. The learner then correctly decoded
   fresh triplets, demonstrated symbolic mode and ownership changes, repaired
   group access with `g+r`, and deleted a read-only root-owned file using
   permissions on the parent directory. Move the basic model to spaced review;
   numeric modes and account administration remain new material. The follow-up
   probe found no binary-to-decimal foundation and a misconception that one of
   `adduser` or `useradd` automatically grants `sudo`. Build numeric modes from
   three on/off permission positions rather than assuming prior binary fluency,
   and explicitly separate account creation from privilege assignment. The
   `4`, `2`, `1` weights were introduced at session end, but the first
   conversion check was not attempted.
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
   On 2026-08-30, the learner correctly retrieved exact stdout/stderr routing,
   terminal visibility, and overwrite versus append for a complete command.
   They still predicted that an incomplete `2>>` might apply to
   `diagnostics.txt` entered at the next prompt. The parse error and separate
   second command were demonstrated, but not yet explained back or re-tested.
   On 2026-08-31, the learner initially predicted that the earlier `>` in a
   parse-invalid command would still overwrite its file. A live experiment
   established parse-before-execute. They then initially expected a later
   redirection-only command to capture stderr from an already-finished command;
   a stepwise experiment produced the error on the terminal and a zero-byte
   later error file. The learner finally identified that a redirection affects
   only its own submitted command. A clean overwrite/append lab and a combined
   `grep`/`head` pipeline were completed successfully. Re-test after a delay,
   especially the distinction between harmless visual wrapping and real pasted
   newlines; multiple pasted commands split after redirection operators or
   inside a quoted pathname during this session.
   On 2026-09-01, the learner correctly retrieved that an incomplete trailing
   redirect prevents execution and preserves the output file. They initially
   thought a fresh command could not be submitted after the syntax error, then
   correctly selected the new command's diagnostic after learning that each
   redirection belongs only to its own submission. The Phase 1 exit-check
   pipeline using `>`, `2>>`, and `|` is assigned but not yet attempted; use it
   as the next practical transfer check. On 2026-09-03, the learner completed
   that transfer check. Their first construction redirected `grep` stdout to an
   append-only file before the pipe; they repaired it to route `grep` stdout
   through `head` and overwrite the final report. A second run verified two
   stable match lines and two accumulated diagnostics. The learner initially
   forgot that a normal pipe connects the left command's stdout to the right
   command's stdin, but after a stream diagram correctly distinguished matches
   entering `head` from stderr diagnostics bypassing it. Move to spaced review.
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
    On 2026-09-01, the learner added an unnecessary `nano -p`, then used the
    installed `nano --help` output to identify it as preserving XON/XOFF keys.
    They initially guessed that `-p` caused saving, but repaired the causal model
    by comparing two runs that both used `-p`: `Ctrl+O` plus `Enter` saved the
    first, while declining with `N` discarded the second. Re-test option meaning
    later with another unfamiliar command rather than immediately.
11. Command type and documentation source: on 2026-08-29, initially predicted
    that `head`, `grep`, and `cd` were all Bash builtins because they can all be
    used in scripts. `type` and `type -a` showed an external executable, an
    alias with underlying paths, and a builtin. The learner then correctly chose
    `help cd`, `head --help` or `man head`, and `grep --help` or `man grep`.
    Re-test later with a different builtin and external command.
12. Filesystem roles, archives, and Nano: on 2026-08-31, correctly associated
    `/home` with user files, `/tmp` with temporary data, and `/var/log` with
    recorded events. Correctly selected basic `tar` create/extract outcomes and
    Nano's `Ctrl+O`, `Enter`, `Ctrl+X` workflow when given choices. The learner
    could not yet explain why `/etc` and `/var/log` have their roles, distinguish
    archive structure from compression, or demonstrate Nano's buffer/save
    states. Configuration as intended input and logs as observed output were
    introduced, but the immediate check was not attempted before session end.
    On 2026-09-01, correctly explained configuration as intended behavior and
    logs as observed events, then assigned `/etc`, `/var/log`, `/home`, and
    `/tmp` from purpose and lifetime. Nano buffer-versus-disk behavior was
    predicted and demonstrated through one saved and one discarded edit.
    Archive versus compression was explained correctly; `tar` create, list,
    gzip, extract, and `-C` restoration were demonstrated. The learner diagnosed
    a missing archive member by finding that the source log had never been
    created, recreated the snapshot, and verified an independent restore.
    During exit-check Part 1, an unfiltered `find` initially included
    directories and was repaired with `-type f`; a wrong `cat` path was corrected
    immediately. Move these concepts to spaced operational review after the
    Phase 1 exit gate.

Phase 1 has passed. During Phase 2, use short operational retrieval of item 9
and the `~/` distinction from item 1. Re-test items 10 and 11 later in an
unfamiliar troubleshooting scenario. The first Phase 2 permissions lesson is
complete. Next probe numeric modes and account/group administration before
planning a restricted-service-account lab.

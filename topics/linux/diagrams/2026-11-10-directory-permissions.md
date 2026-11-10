# Directory permissions — 2026-11-10

## Permission-class retrieval

For ordinary mode-bit checks, choose one applicable class:

```text
Are you the owner? ------ yes --> owner bits
       |
       no
       v
Do you belong to the
file's group? ----------- yes --> group bits
       |
       no
       v
   other bits
```

The learner independently explained that the owner cannot borrow group write
permission when owner write is absent in a hypothetical `-r--rw----` file.

## Today's observed practice tree

```text
/tmp/directory-permissions.2gCTIy/   owner rwx
└── app/                           owner rwx
    └── current.log                owner rw; empty file
```

A directory holds names referring to filesystem objects. Directory read (`r`)
allows listing its entry names; directory search (`x`) allows looking up a
known name. Reading file contents also requires file read access and search
permission through the ancestor directories.

## Observed read-versus-search result

The learner predicted both outcomes correctly before execution. After removing
only owner read from `app`, owner search remained available:

```text
app owner permissions:  -wx

ls app/                         -> Permission denied
cat app/current.log             -> success, status 0
```

`ls` could not discover the directory's entry names without directory read.
`cat` already had the entry name `current.log`, so directory search allowed the
pathname lookup; file read permission allowed its empty contents to be read.

The learner then restored owner read and verified the original directory mode:

```text
drwxrwxr-x  app
```

The inverse experiment removed only owner search, leaving directory read:

```text
app owner permissions:  rw-

command ls -f app/               -> .  ..  current.log; status 0
cat app/current.log              -> Permission denied; status 1
```

This time the directory could expose its names, but the known filename could
not be traversed. The file still had owner read permission; the failed read was
caused by the missing directory search permission on the pathname. Owner search
was restored and `drwxrwxr-x` was verified afterward.

Together, the experiments isolate the two permissions:

| Directory permission | Capability demonstrated |
|---|---|
| `r` | discover entry names |
| `x` | look up and reach a known entry name |

## Directory write versus file write

The next experiment separates two different kinds of change:

```text
change bytes stored in a file  -> file w (plus directory x to reach it)
change names inside directory  -> directory w + x
```

The learner correctly predicted that a writable file can be appended to when
the containing directory lacks write. The learner predicted that directory
search alone permits removal; the experiment corrected that model.

Observed with owner write removed from `app` while owner search remained:

```text
append to writable write-test.log  -> status 0
remove write-test.log name         -> Permission denied; status 1
```

After restoring directory write, `app` was again `drwxrwxr-x`. The file was
still present, and its content showed both `baseline` and `appended`.

The resulting model is:

| Intended change | Relevant permissions |
|---|---|
| Read a file's bytes | directory `x` along its path + file `r` |
| Change a file's bytes | directory `x` along its path + file `w` |
| Discover names in a directory | directory `r` |
| Create or remove a directory entry | directory `w` + `x` |

This table describes ordinary mode-bit behavior in the disposable test tree;
features such as sticky directories or access-control lists can add constraints.

## Inverse write test

A separate `removal-test.log` had this observed mode:

```text
directory app:       drwxrwxr-x
removal-test.log:    -r--rw-r--
```

Because the learner owned the file, its owner `r--` bits applied; group write
was not borrowed. Appending failed with status 1. The containing directory had
owner `w+x`, so removal was permitted even though the file was write-protected.

The first `rm` attempt displayed a confirmation prompt. The next command was
accidentally entered as the prompt response, effectively declining removal;
`rm` still returned status 0, while a listing proved the file remained. This is
evidence that command status sometimes needs an independent state check.

On retry, the learner answered `y` to an explicit `rm -i` prompt. `rm` returned
status 0, and a fresh directory listing showed only `write-test.log` and
`current.log`, independently verifying removal of `removal-test.log`.

## Numeric permission notation

Each permission class has three on/off positions. Their values are powers of
two, so every combination has a unique sum:

```text
permission:   r   w   x
value:        4   2   1
binary place: 4   2   1
```

Add only the permissions that are present:

```text
rwx = 4 + 2 + 1 = 7
rw- = 4 + 2     = 6
r-x = 4     + 1 = 5
r-- = 4         = 4
```

The three digits apply to the classes in the same order as a long listing:

```text
        owner  group  other
755       7      5      5
          rwx    r-x    r-x
```

Thus `chmod 755 path` replaces all three classes with `rwxr-xr-x`. Numeric
modes describe a complete mode for the stated classes; symbolic changes such as
`chmod g-w path` alter selected bits relative to the current mode.

The learner independently converted `rw-r-----` to `640` and `640` back to
`rw-r-----`, then constructed and executed:

```bash
chmod 640 "$find_lab/app/write-test.log"
```

The fresh listing verified `-rw-r-----`. In a directory transfer question, the
learner selected `750` and reconstructed its symbolic form as `rwxr-x---`.

## Creation defaults and `umask`

The Ubuntu shell reported:

```text
umask
0002
```

Programs normally request at most `666` for a new regular file and `777` for a
new directory. The umask removes selected permission bits from that request:

```text
result = requested permissions AND NOT umask
```

For the observed `0002`, the final `2` masks other-class write:

```text
regular file request:  666   rw-rw-rw-
remove umask:          002   -------w-
result:                664   rw-rw-r--

directory request:     777   rwxrwxrwx
remove umask:          002   -------w-
result:                775   rwxrwxr-x
```

This explains the modes observed when today's test files and `app` directory
were created. A normal file does not start with execute bits merely because the
umask permits them: the creation request itself was `666`, which contains no
execute bits. Programs may also request fewer permissions than these defaults.

For `umask 027`, the learner reconstructed the file result as `rw-r-----`
(`640`). The first directory attempt omitted group search, then the learner
corrected it to `rwxr-x---` (`750`) because mask digit `2` removes only group
write.

A child-shell experiment verified both predictions:

```text
new-file   -rw-r-----   640
new-dir    drwxr-x---   750
```

After the child exited, the interactive shell still reported `umask 0002`.

The child-shell behavior matches working-directory isolation:

```text
interactive Bash: umask 0002
        |
        +-- child Bash: inherits 0002
                |
                +-- sets its own value to 0027
                +-- creates objects
                +-- exits

interactive Bash: still 0002
```

The learner initially knew what `0002` removes but did not connect the unchanged
parent value to process isolation. After explanation, the learner predicted
that setting `umask 027` directly in the interactive shell would change that
shell to `0027`. A hint was needed to choose `umask 0002`, rather than `chmod`,
as the restoration command. `chmod` changes an existing filesystem object's
mode; `umask` changes creation state held by the shell process.

## Group ownership

The learner's current group list included `raf_0411` and `users`. The disposable
file initially showed:

```text
-rw-r-----  raf_0411  raf_0411  write-test.log
```

The learner correctly predicted that `chgrp users` would change only the group
field. Execution verified:

```text
-rw-r-----  raf_0411  users     write-test.log
```

Neither the user owner nor mode changed. `chgrp raf_0411` then restored the
original group, confirmed by a fresh listing.

## User ownership restriction

The learner predicted that ordinary user `raf_0411` could not transfer the
file's user ownership to root, but initially could not explain the restriction.
Execution without `sudo` produced:

```text
chown root write-test.log  -> Operation not permitted; status 1
```

A fresh listing verified the unchanged owner/group `raf_0411:raf_0411` and
unchanged mode `640`. Changing user ownership is privileged; an owner may
normally use `chgrp` only to select a group of which that owner is a member.

## `sudo` and effective identity

The learner initially described `sudo` as bypassing permissions or restricted
commands. The refined model is that policy-authorized `sudo` starts a command
with another effective identity, root by default; kernel checks then use that
identity and its privileges.

Observed comparison:

```text
id                 -> uid=1000(raf_0411), gid=1000(raf_0411), supplementary groups
sudo -u root id    -> uid=0(root), gid=0(root), groups=0(root)
```

This read-only experiment changed the command's identity, not the identity of
the learner's interactive Bash process.

A privileged ownership experiment on the disposable file initially recorded a
baseline that was already `root:root`, so it could not prove the change. After
the evidence problem was identified, the learner reran the complete sequence
from a restored baseline. The corrected listings proved:

```text
raf_0411:raf_0411  ->  root:root  ->  raf_0411:raf_0411
```

All three listings retained mode `-rw-r-----` (`640`), size 18, timestamp, and
pathname. This demonstrates that `sudo chown` changed ownership fields and that
the final privileged command restored them; it did not inherently change mode.

## Integrated permission checkpoint

The learner independently derived the requested modes for a new tree:

```text
outer directory    750  rwxr-x---
shared directory   750  rwxr-x---
report.txt         640  rw-r-----
```

The initial plan applied all modes correctly but omitted the separate group
ownership requirement. After a prompt, the learner identified that all three
objects needed group `users`: otherwise group members could not traverse the
outer `750` directory or receive the intended bits on its descendants.

The first group repair accidentally targeted `shared` twice and left the file
at group `raf_0411`; the learner's listing exposed the mismatch, but another
prompt was needed to act on it. The final verification proved:

```text
drwxr-x---  raf_0411 users  outer
drwxr-x---  raf_0411 users  shared
-rw-r-----  raf_0411 users  report.txt
```

`cat` printed exactly `checkpoint`. Numeric mode derivation was independent;
integrating group ownership and self-auditing all target fields remained guided.

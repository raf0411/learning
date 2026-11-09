# Linux environment — 2026-11-09

## Components

```text
Ubuntu distribution
  |
  +-- Programs and supporting system software
  |     +-- Bash: the current shell, interpreting command syntax
  |     +-- ls: a program that lists directory entries
  |
  +-- Linux kernel: manages processes, memory, and access to devices/filesystems
```

For `ls > listing.txt`, Bash interprets the redirection and uses kernel services
to open the output file and start the program with stdout routed to that file.
`ls` requests directory information through kernel services and formats its
output. Both the shell and other programs use kernel services; this is not a
strict chain in which only `ls` communicates with the kernel.

## Observed VM identity

| Inspection | Learner's output |
|---|---|
| `/etc/os-release`, PRETTY_NAME | Ubuntu 26.04.1 LTS |
| `uname -r` | 7.0.0-31-generic |
| `ps -p $$ -o comm=` | bash |
| `pwd` | /home/raf_0411 |

`$$` expands to the shell's process ID. This `ps` command selects that process
and prints its command name without a column heading.

## First filesystem distinction

```text
/                         filesystem root
└── home
    └── raf_0411           learner's current directory in the transcript
```

`/` starts an absolute pathname. `ls /` lists that directory without changing
the shell's current working directory. The next observation will inspect its
actual entries; the learner subsequently supplied that listing and explored
`/var` and `/var/log`.

## Directory purposes and logs

```text
/
├── home/raf_0411    personal directory
├── etc             system configuration
├── var/log         recorded events observed in this VM
├── tmp             temporary files
├── root            root user's home directory
└── proc            kernel-provided information exposed as files
```

The learner independently retrieved `tail -n 5 /var/log/syslog` and recorded
five log lines. Their general structure is:

```text
timestamp  hostname  source: message
```

The observed hostname was `ubuntu-desktop`. Sources included `systemd[3340]`
and `kernel`. A DENIED audit operation is evidence about that operation;
it does not by itself establish the outcome of an entire service or upload.

Unlike a stored log's historical records, many `/proc` entries expose current
kernel information when read. The next read-only experiment is
`cat /proc/sys/kernel/hostname`; learner output is still pending.

Update: learner predicted and observed `ubuntu-desktop`.

## Executable search through PATH

For a fresh external-command lookup, directories are searched in listed order.
This hypothetical trace assumes no alias or function named `report`:

```text
/usr/local/sbin/report   absent       -> continue
/usr/local/bin/report    executable   -> run this one; stop searching
/usr/sbin/report                      -> not reached
/usr/bin/report                       -> not reached
```

A missing candidate does not stop the search. If all directories lack a matching
executable, lookup fails. `/usr/bin` has no automatic priority over earlier
entries. An explicit pathname bypasses PATH lookup. Bash can cache executable
locations; the trace describes a fresh lookup.

Observed on this VM:

```text
ls alias:       ls --color=auto
executable:     /usr/bin/ls
alternate path: /bin/ls -> /usr/bin/ls because /bin -> usr/bin
```

The relative symlink target `usr/bin` is interpreted from `/`, the directory
containing `/bin`, not from the terminal's current working directory.

## Working-directory inheritance

Observed in the learner's Ubuntu VM:

```text
Parent Bash: /home/raf_0411
  |
  +-- starts child Bash: initially /home/raf_0411
  |     |
  |     +-- cd /tmp -> child directory becomes /tmp
  |     +-- pwd     -> prints /tmp
  |     +-- exits
  |
  +-- pwd -> still prints /home/raf_0411
```

A child inherits its parent's working directory. Each process can subsequently
change its own working directory independently. An external pwd therefore
starts in the shell's directory and reports it. Changing the interactive shell's
directory requires `cd` to act within that shell; a child cannot do it on the
parent's behalf.

## Find: traversal and selection

```text
starting path -> visit entries within depth limit -> test type AND name
                                                         |
                                                         +-- print matches
```

`/home` and the user's home directory are different starting points. In this
VM, `$HOME` expands to `/home/raf_0411`.

The learner's corrected command:

```bash
find "$HOME" -maxdepth 1 -type d -name '.*'
```

It searches the starting directory and immediate entries, selecting directories
whose names begin with a dot. Observed matches were `.local`, `.ssh`, `.cache`,
and `.config` inside the user's home. The starting directory's own basename
`raf_0411` does not match the dot-prefix pattern.

Depth starts at 0 for the starting path. A name test filters output, not which
subdirectories find traverses. The next lab provides a disposable tree to test
depth 2 versus unrestricted traversal; results are pending.

Observed depth-lab results:

```text
starting directory                 depth 0
├── root.log                       depth 1   both searches
├── app                            depth 1
│   ├── current.log                 depth 2   both searches
│   └── archive                    depth 2
│       └── old.log                 depth 3   unlimited search only
└── docs                           depth 1
    └── readme.txt                 depth 2   excluded by name
```

The learner independently constructed both searches. `-maxdepth 2` bounds
traversal; `-type f -name '*.log'` selects regular files with the requested
suffix. Removing the depth limit includes the deeper matching file.

## Pathnames are not whitespace-separated words

Observed with a practice filename containing a space:

```text
find's newline output       default xargs arguments
.../access log.log\n    ->   [ .../access ] [ log.log ]

find -print0 output         xargs -0 arguments
.../access log.log\0    ->   [ .../access log.log ]
```

Here `\n` and `\0` label a newline and a null byte, respectively; they are not
literal backslash characters in the stream. A pathname cannot contain a null
byte, so this separates pathnames unambiguously, even with spaces or newlines.
Both producer and consumer must use the matching format. Quoting find's name
pattern protects it from shell expansion; that quoting is not carried through
the pipe.

The learner independently combined `-maxdepth 2 -type f -name '*.log' -print0`
with `xargs -0 printf '<%s>\n'`, observing three intact pathname arguments.

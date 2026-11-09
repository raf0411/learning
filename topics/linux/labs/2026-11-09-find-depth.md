# Find: search depth — 2026-11-09

Run the commands in your **Ubuntu VM**, and record answers in this note.

## Idea

`find` counts depth from its starting path, which is depth 0. Without a depth
limit, it descends into subdirectories. A name filter controls which entries
are printed; it does not prevent traversal through directories with other names.

## Set up a disposable tree

These commands create a new temporary directory and empty practice files inside
it. They do not modify your existing files. Run each physical line separately,
in the same terminal. If setup reports an error, stop and share it.

```bash
find_lab=$(mktemp -d /tmp/find-depth.XXXXXX)
printf '%s\n' "$find_lab"
mkdir -p "$find_lab/app/archive" "$find_lab/docs"
touch "$find_lab/root.log" "$find_lab/app/current.log" "$find_lab/app/archive/old.log" "$find_lab/docs/readme.txt"
```

Intended structure after successful setup:

```text
starting directory            depth 0
├── root.log                  depth 1
├── app                       depth 1
│   ├── current.log            depth 2
│   └── archive               depth 2
│       └── old.log            depth 3
└── docs                      depth 1
    └── readme.txt             depth 2
```

## 1. Search with a limit

Find regular files with names ending in `.log`, searching no deeper than depth
2 from `"$find_lab"`. Construct the command yourself.

Predict the matching paths relative to the starting directory (order does not
matter):

```text
find "$find_lab" -maxdepth 2 -type f -name '*.log'
```

Run your command and paste the command plus output:

```text
raf_0411@ubuntu-desktop:~$ find "$find_lab" -maxdepth 2 -type f -name '*.log'
/tmp/find-depth.cCOil3/root.log
/tmp/find-depth.cCOil3/app/current.log
```

## 2. Search the whole tree

Revise your command to find all regular `.log` files anywhere under the same
starting directory, with no depth limit.

Predict which additional file, if any, will appear:

```text
/tmp/find-depth.cCOil3/root.log
/tmp/find-depth.cCOil3/app/current.log
/tmp/find-depth.cCOil3/app/archive/old.log
```

Run your revised command and paste the command plus output:

```text
raf_0411@ubuntu-desktop:~$ find "$find_lab" -type f -name '*.log'
/tmp/find-depth.cCOil3/root.log
/tmp/find-depth.cCOil3/app/current.log
/tmp/find-depth.cCOil3/app/archive/old.log
```

No written explanation required. Preserve any initial attempts if you revise
them. Leave the temporary tree in place for now. Tell me when the note is ready.

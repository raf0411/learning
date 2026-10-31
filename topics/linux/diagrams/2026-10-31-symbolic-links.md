# Symbolic links — 2026-10-31

A symbolic link stores a target pathname, not the target's file contents.
In this experiment, `shortcut.txt` stored the text `original.txt`.
When `cat shortcut.txt` reads content, the operating system follows that
pathname to the target file.

## Target present

```text
shortcut.txt                      original.txt
[stores "original.txt"] --------> [REPLACEMENT CONTENT]
```

Changing the target's content changes what reading through the link reaches.
The link does not need to store or receive an updated copy of that content.

## Target removed — observed in Part 4

```text
shortcut.txt                      original.txt
[stores "original.txt"] --------> missing
```

The recorded `ls -l` output still showed `shortcut.txt -> original.txt`.
The link entry therefore still existed. Reading through it with `cat` failed
because the target was missing. This is a dangling symbolic link.

“The target pathname resolves to a file” means following that pathname
successfully finds a file. The link can exist even when that lookup fails.

## Target recreated — observed in Part 5

Creating a file at `original.txt` made the existing link usable again.
The link refers to that pathname; it does not require the original file object
to return.

## Link removed — observed in Part 6

```text
shortcut.txt                      original.txt
missing                          [REPLACEMENT CONTENT]
```

Removing the link removed that separate entry. The target remained readable.

## Copy versus symbolic link

- A regular copied file has independent file data.
- A symbolic link stores a pathname used to reach its target.
- Content displayed by `cat shortcut.txt` is content reached through the link,
  not content stored inside the link itself.

## Hard-link comparison — observed later in today's session

Before removal:

```text
original.txt ----+
                +---- inode 48272923: CHANGED CONTENT (2 names)
second.txt -----+

copy.txt ------------ inode 48273437: FIRST CONTENT   (1 name)
```

After removing `original.txt`:

```text
second.txt ---------- inode 48272923: CHANGED CONTENT (1 name)

copy.txt ------------ inode 48273437: FIRST CONTENT   (1 name)
```

Neither hard-linked name depends on the other pathname. Each names the same
underlying file. The first name counts toward the link count just like the
added name. These inode numbers are recorded lab observations, not identifiers
to assume in a future experiment.

## Relative target paths

There are two steps when reading a symbolic link:

```text
shell's current directory
    |
    +-- use command operand to locate the link
                                        |
                                        +-- read stored target pathname
                                                    |
                                  if relative: start at the link's directory
```

Changing the shell's current directory does not move the link. Moving the
link to a different directory changes the base for its relative target.
An absolute stored target instead begins at `/`.

### Separating three things in the relative-link experiment

Before the link moved, these were different facts:

| Thing | Value relative to the lab root where applicable |
| --- | --- |
| Link's location | `links/shortcut.txt` |
| Text stored inside the link | `../data/note.txt` |
| Content read from the target file | `RELATIVE LINK CONTENT` |

To follow the link's stored path before the move:

```text
start: directory containing the link = links/
  ..        -> lab root
  data      -> lab root/data/
  note.txt  -> lab root/data/note.txt
```

From the lab root, `cat links/shortcut.txt` located the link. From inside
`links/`, `cat shortcut.txt` located that same link. Its location and stored
text were unchanged, so following it still reached the same target.

After the move, first identify the new containing directory. Only then
interpret the stored `..`. Keep that as the next learner reasoning step.

### Guided correction: two parents from `links/deeper/`

```text
links/deeper/ -- first .. --> links/ -- second .. --> lab root
```

From this starting directory, `../data/note.txt` seeks the missing
`links/data/note.txt`. The correct stored target is `../../data/note.txt`:
two upward steps, then enter `data` and read `note.txt`.

The worksheet now supplies creation of a separate `repaired.txt` link so the
learner can compare the two lookups without deleting the dangling example.

The learner's recorded comparison confirmed that reading `shortcut.txt`
failed, while reading `repaired.txt` displayed `RELATIVE LINK CONTENT`.
Both links were inside `links/deeper/`; their different stored paths explain
their different results.

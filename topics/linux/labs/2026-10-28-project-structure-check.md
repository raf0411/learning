# Checkpoint — Build a Fresh Project Structure

Date: 2026-10-28

## Scope

Create only the new tree shown below, beneath the existing `labs` directory.
The `copy-practice` directory does not currently exist.

```text
copy-practice/
├── backups/
│   └── daily/
├── destination/
└── source/
    ├── documents/
    └── images/
```

This will become the disposable workspace for the next lesson on `cp`.

## Construct

Start here and verify your location:

```bash
cd /Users/raffi/Learning/topics/linux/labs
```

```bash
pwd
```

Before running them, write the `mkdir` command or commands you choose. Any
correct sequence is acceptable; decide for yourself where `-p` is needed.

```bash
raffi@Raffis-Mac labs % mkdir copy-practice
raffi@Raffis-Mac labs % mkdir -p copy-practice/backups/daily
raffi@Raffis-Mac labs % mkdir -p copy-practice/destination
raffi@Raffis-Mac labs % mkdir -p copy-practice/source/documents
raffi@Raffis-Mac labs % mkdir -p copy-practice/source/images
```

Run your planned commands.

## Verify

Use these read-only checks:

```bash
ls copy-practice
```

```bash
ls copy-practice/source
```

```bash
ls copy-practice/backups
```

Record each command's output under its label:

```text
raffi@Raffis-Mac labs % ls copy-practice
backups		destination	source
raffi@Raffis-Mac labs % ls copy-practice/source
documents	images
raffi@Raffis-Mac labs % ls copy-practice/backups
daily
raffi@Raffis-Mac labs %
```

Map the evidence to every requested directory. If anything is absent, diagnose
and repair it before claiming the tree is complete:

TODO

## Explain

- Why did your commands create nested directories rather than only siblings?

  because i use -p

- Which command options did you use, and why were they needed or not needed?

  -p, because im making a folder path that not exists yet

- Were the paths in your construction commands relative or absolute? How can
  you tell?

  thats relative, because i have to make the directory based on my current directory, not using the absolute path

## Review correction

The constructed tree and all three recorded `ls` outputs are correct. Complete
the two items below to close the checkpoint.

### Map the verification evidence

Account for every requested directory by stating which recorded `ls` output
proves that it exists. Include the top-level `copy-practice` directory itself.

raffi@Raffis-Mac labs % ls copy-practice
backups		destination	source
raffi@Raffis-Mac labs % ls copy-practice/backups
daily
raffi@Raffis-Mac labs % ls copy-practice/destination
raffi@Raffis-Mac labs % ls copy-practice/source
documents	images
raffi@Raffis-Mac labs %

### Separate path syntax from command behavior

Your current explanation attributes nesting to `-p`. Revise the model by
answering both questions:

1. What part of a command such as `mkdir -p copy-practice/backups/daily`
   expresses that `daily` should be nested inside `backups`?
2. What does `-p` contribute, and in which of your four commands that used
   `-p` was it actually necessary at the moment that command ran?

Answers:
1. -p
2. -p contribute when u are trying to create a nested path but the parent of that nested path is not created yet, at `mkdir -p copy-practice/backups/daily` i think it is necessary because backups is not created yet

## Tutor review — revision needed

### What the evidence already establishes

- Your recorded listings contain all requested names.
- Your explanation correctly says that `-p` can create a missing parent.
- You correctly identified `backups` as missing before
  `copy-practice/backups/daily` ran.

### Revise these two points

1. In the pathname `copy-practice/backups/daily`, look at the characters that
   separate the three directory names. Those separators—not the command
   option—express the parent/child relationship. Write the relevant character
   and explain what the pathname means:

   /

2. Before each command below ran, identify whether its immediate parent already
   existed. Then decide whether omitting `-p` would have caused that command to
   fail:

| Command operand                  | Did its immediate parent already exist? | Was `-p` necessary? |
| -------------------------------- | --------------------------------------- | ------------------- |
| `copy-practice/backups/daily`    | no (`backups` did not exist)            | yes                 |
| `copy-practice/destination`      | no                                      | yes                 |
| `copy-practice/source/documents` | no                                      | yes                 |
| `copy-practice/source/images`    | no                                      | yes                 |

3. Make the verification mapping explicit rather than only repeating command
   output. State which listing proves each of these exists:

| Requested directory               | Recorded evidence                                                                              |
| --------------------------------- | ---------------------------------------------------------------------------------------------- |
| `copy-practice/`                  | `copy-practice/` exists because ls on labs shows copy-practice                                 |
| `copy-practice/backups/`          | `copy-practice/backups/` exists because ls copy-practice displays backups                      |
| `copy-practice/backups/daily/`    | `copy-practice/backups/daily/` exists because<br> `ls copy-practice/backups` displayed `daily` |
| `copy-practice/destination/`      | `copy-practice/destination/` exists because ls copy-practice displays destination              |
| `copy-practice/source/`           | `copy-practice/source/` exists because ls copy-practice displays source                        |
| `copy-practice/source/documents/` | `copy-practice/source/documents` exists because ls copy-practice/source displays documents     |
| `copy-practice/source/images/`    | `copy-practice/source/images` exists because ls copy-practice/source displays images           |

## Tutor review — clarification

### What “map the evidence” means

For each requested directory, make a claim connecting it to something actually
observed. Example:

> `copy-practice/backups/daily/` exists because
> `ls copy-practice/backups` displayed `daily`.

This is stronger than pasting all the output because it shows that each required
part of the tree was checked rather than overlooked.

Complete the remaining rows using that same pattern. For the top-level
`copy-practice/` itself, consider what the successful command
`ls copy-practice` proves before you even interpret its output.

### Recheck the `-p` table in execution order

Your current table says every immediate parent was missing. That does not account
for the directories created by earlier commands. For each row, check the parent
named below as it existed *when that command ran*:

| Command operand | Immediate parent to check |
|---|---|
| `copy-practice/backups/daily` | `copy-practice/backups` |
| `copy-practice/destination` | `copy-practice` |
| `copy-practice/source/documents` | `copy-practice/source` |
| `copy-practice/source/images` | `copy-practice/source` after the preceding command ran |

Revise your original table above. Also expand `/` into one sentence explaining
the relationship expressed by `copy-practice/backups/daily`.

## Tutor review — complete correction

### Verification result

The evidence mapping correctly accounts for every child directory. For the
top-level directory, use the recorded command itself:

> `copy-practice/` exists because `ls copy-practice` successfully accessed and
> listed it.

The worksheet did not record an `ls labs` result, so that should not be cited as
the recorded evidence.

### `/` and `-p` have separate jobs

In `copy-practice/backups/daily`, each `/` separates one path component from the
next. The pathname means: find `copy-practice`, then its child `backups`, then
the child `daily` inside `backups`. This is what expresses nesting.

The `-p` option tells `mkdir` to create any missing parent directories along the
path (and not complain if an addressed directory already exists). It does not
define the parent/child relationship.

Given the original command order:

| Command operand | Parent state when run | Was `-p` necessary? |
|---|---|---|
| `copy-practice/backups/daily` | `backups` was missing | yes |
| `copy-practice/destination` | `copy-practice` already existed | no |
| `copy-practice/source/documents` | `source` was missing | yes |
| `copy-practice/source/images` | the preceding command had created `source` | no |

The original commands were all safe. In two rows, `-p` was useful; in the other
two, it was merely unnecessary.

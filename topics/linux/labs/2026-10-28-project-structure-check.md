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

TODO

### Separate path syntax from command behavior

Your current explanation attributes nesting to `-p`. Revise the model by
answering both questions:

1. What part of a command such as `mkdir -p copy-practice/backups/daily`
   expresses that `daily` should be nested inside `backups`?
2. What does `-p` contribute, and in which of your four commands that used
   `-p` was it actually necessary at the moment that command ran?

TODO

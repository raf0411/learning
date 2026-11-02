# Lab — Choose among `--help`, `man`, shell `help`, and `info`

Date: 2026-11-02

## The documentation tools answer different needs

```text
program --help   quick usage, if that program implements the option
man program      fuller installed reference
help name        Bash documentation for a Bash builtin
info topic       GNU's navigable manuals, if Info is installed
```

Availability varies. The current interactive shell is zsh, not Bash; zsh does
not provide Bash's `help` builtin. This Mac has Bash available, so one command
below asks Bash to display its own help without changing the current interactive
shell. GNU Info is not installed here; we will verify that honestly rather than
inventing output.

## 1 — Use a program's quick help

Run:

```bash
tar --help
```

From its actual output, record:

| Evidence to find                                             | Exact observed text                                                                                   |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| The line summarizing create, list, and extract mode letters  | First option must be a mode specifier:<br>  -c Create  -r Add/Replace  -t List  -u Update  -x Extract |
| The line mapping `-z`, `-j`, and `-J` to compression formats | z, -j, -J, --lzma  Compress archive with gzip/bzip2/xz/lzma                                           |
| Did the command return to the shell automatically?           | yes                                                                                                   |

In one sentence, describe why `--help` was useful here.

> because its short and quick information

## 2 — Use the fuller manual

Open:

```bash
man tar
```

Search for `/bzip2`. Use `n` if necessary until you find the option entry that
contains `-j`. Record the option names shown there and paraphrase what the entry
says. Then press `q`.

| Manual evidence              | Result                                                                                                                                                                                                                                                                                             |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Option entry containing `-j` | -j, --bzip, --bzip2, --bunzip2<br>             (c mode only) Compress the resulting archive with bzip2(1).  In extract or list modes, this<br>             option is ignored.  Note that this tar implementation recognizes bzip2 compression<br>             automatically when reading archives. |
| Meaning in your own words    | it compresses a directory in a archive using the bzip2 method                                                                                                                                                                                                                                      |
| Did `q` return to the shell? | yes                                                                                                                                                                                                                                                                                                |

State one way the `man` entry was more detailed than the quick-help line.

> because it shows the complete detailed explanation of -j

## 3 — Ask Bash about one of its builtins

`cd` is implemented by the shell because it must change that shell's working
directory. Run this as one physical command:

```bash
bash -c 'help cd'
```

For this exercise, treat the outer form as a supplied launcher: it asks Bash to
run `help cd` and exit. Quoting and `-c` will be explained in the shell-mechanics
phase.

Record the first syntax line and the first descriptive sentence from the actual
output:

```text
cd: cd [-L|[-P [-e]]] [-@] [dir]
    Change the shell working directory.

    Change the current directory to DIR.  The default DIR is the value of the
    HOME shell variable. If DIR is "-", it is converted to $OLDPWD.
```

Why is Bash's `help` an appropriate source for a Bash builtin?

> because it can show the explanation for a bash specific command such as cd

## 4 — Check whether GNU Info is installed

Run:

```bash
type info
```

Record the command and result:

```text
info not found
```

If the result says `info not found`, what is the honest conclusion: that Info
documentation is universally nonexistent, or only that the `info` command is
not available in this current environment?

> info is not available in this current environment would be my guess

## 5 — Choose a recovery route

Choose the most appropriate first route from `--help`, `man`, Bash `help`, or
`info` (if installed).

| Need                                                            | First route | Why                                                                                     |
| --------------------------------------------------------------- | ----------- | --------------------------------------------------------------------------------------- |
| A quick reminder of `tar`'s common option letters               | tar --help  | because --help is for quick information                                                 |
| A detailed installed description of `tail -F`                   | man tail    | because man is more detailed                                                            |
| The meaning and syntax of Bash's `cd` builtin                   | help cd     | because cd is specific command in bash                                                  |
| A navigable GNU manual that may contain tutorial-style chapters | info        | because info can give u a navigable GNU manual that may contain tutorial style chapters |

Finally, explain what you would do if your first documentation route were
unavailable or insufficient.

> refer to the internet (googling)

Stop and tell the tutor when the worksheet is ready.

## 6 — Focused precision check

Keep the original answers above unchanged. Complete these corrections in your
own words.

1. Copy the compression line from `tar --help` again, preserving the leading
   hyphen on `-z`.
2. Explain `tar -j` using this sequence:

   ```text
   directory tree -> tar archive byte stream -> bzip2-compressed archive
   ```

   State which tool performs the packaging and which performs the compression.
3. Explain why `bash -c 'help cd'` is authoritative for Bash's `cd` without
   claiming that `cd` exists only in Bash.
4. If `tar --help` is insufficient, name one next local route. If local sources
   still cannot answer a version-specific question, name the kind of online
   source you should prefer over an arbitrary search result.

> 1. -z, -j, -J, --lzma  Compress archive with gzip/bzip2/xz/lzma
> 2.    directory tree -> tar archive byte stream (packacing) -> bzip2-compressed archive (compression)
> 3. because we use bash in front before -c i guess?
> 4. man tar, or google.com search for tar command, maybe official documentation online regarding tar

Save the worksheet and tell the tutor when the precision check is ready.

## Tutor checkpoint

The learner corrected the exact `-z, -j, -J` transcription and identified
`man tar` followed by official online documentation as the appropriate fallback
route. Clarifications supplied by the tutor:

- `tar` packages the directory tree into an archive byte stream; bzip2 then
  compresses that stream.
- `bash -c 'help cd'` starts Bash for one command, so Bash's own `help` builtin
  documents Bash's own `cd`. Other shells also implement `cd`.
- A generic search engine may locate a source, but official upstream or OS
  vendor documentation should be preferred as authority.

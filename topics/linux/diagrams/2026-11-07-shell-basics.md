# Shell mechanics restart — 2026-11-07

## First step: a command produces output

The terminal is the interface where you type commands and see text.
The shell reads your command line and carries out its instructions.
`zsh` and `bash` are examples of shells.

```text
you type a command line
          |
          v
shell reads it and runs the command
          |
          v
command produces output
          |
          v
terminal displays it (the usual default)
```

For this first experiment, use:

```bash
printf 'hello\n'
```

`printf` prints text. The quoted text supplies what to print; `\n` means
start a new line. Run the entire command on one physical line.
This command does not create or change any files.

The learning target is to identify the command and observe where its output
appears.

## Sending standard output to a file

Standard output (`stdout`) is a command's normal output channel. Its destination
is usually the terminal in a simple interactive command.

```text
printf 'hello\n'
    printf -> stdout -> terminal

printf 'hello\n' > greeting.txt
    printf -> stdout -> greeting.txt
```

The shell handles `>`: it creates the destination file if missing, or truncates
an existing file before the command runs. Use disposable files for practice.

Reading the saved file is a separate command:

```text
greeting.txt -> cat -> stdout -> terminal
```

## Replacing and appending

Both operators send stdout to a file:

- `>` creates the file if missing, or empties an existing file before writing.
- `>>` creates the file if missing, or adds output at the end of an existing file.

## Standard input

Standard input (`stdin`) is an input channel a command can read. The shell's
`<` operator connects a file to that channel.

```bash
cat < greeting.txt
```

```text
greeting.txt -> stdin -> cat -> stdout -> terminal
```

With `cat greeting.txt`, `cat` receives a filename argument and opens the file
itself. With `cat < greeting.txt`, the shell opens the file for stdin; `cat`
receives no filename argument and reads stdin. Both display the file contents
in this example.

Direction reminder: `>` routes output out to a file; `<` supplies input from
a file. Input redirection does not itself change the input file's contents.

## Pipes connect commands

```bash
printf 'red\nblue\ngreen\n' | wc -l > count.txt
```

```text
printf stdout -> pipe -> wc stdin
                        wc stdout -> count.txt
```

The pipe supplies the left command's stdout to the right command's stdin.
The final `>` here belongs to `wc`. A later `cat count.txt` is a separate
command with its own stdout destination, normally the terminal.

## Two output channels

Programs normally send results through standard output (`stdout`) and
diagnostics through standard error (`stderr`). In a simple interactive command,
both usually lead to the terminal. `>` redirects stdout only.

```text
command -- stdout --> file chosen by >
        -- stderr --> terminal (unless separately redirected)
```

Stdout is channel 1; stderr is channel 2. `2> errors.txt` redirects stderr to
a file. `>` is shorthand for `1>`.

```bash
cat greeting.txt missing.txt 2> errors.txt | wc -l
```

```text
cat stdout -> pipe -> wc stdin -> count on terminal
cat stderr -> errors.txt
```

## Combining the outputs

`2>&1` gives stderr the destination stdout has at that point. In this pipeline,
stdout is connected to the pipe, so stderr is sent there too:

```bash
cat greeting.txt missing.txt 2>&1 | wc -l
```

```text
cat stdout --\
              > pipe -> wc stdin
cat stderr --/
```

`wc` counts the newline characters it receives; it does not distinguish normal
text from diagnostic text once both arrive through its stdin.

`2>&1` is complete by itself and takes no filename. In contrast, `2> errors.txt`
needs a file destination. An extra filename after `2>&1` can become an operand
of the command rather than a redirection destination.

## Saving and forwarding with tee

`tee FILE` reads stdin, writes a copy to FILE, and forwards the same input
through stdout. Plain `tee` replaces existing file contents; use a disposable
file for practice.

```bash
printf 'apple\npear\n' | tee tee-copy.txt
```

```text
printf stdout -> tee stdin --+-> tee-copy.txt
                            +-> tee stdout -> terminal
```

The terminal receives the stdout copy because no later pipe or redirection
changes that destination in this example.

Adding another pipe changes where `tee` sends stdout:

```bash
printf 'apple\npear\n' | tee tee-copy.txt | wc -l
```

```text
printf -> tee --+-> tee-copy.txt (input text)
               +-> stdout -> wc stdin -> count -> terminal
```

`tee` still writes its named-file copy. Its stdout now feeds `wc` rather than
the terminal. `wc` sends its own result, the count, through its own stdout.

## Redirection order

The shell applies a command's redirections from left to right, before running
the command. `2>&1` copies stdout's destination at that moment. It does not
make stderr follow later changes to stdout.

```bash
cat greeting.txt missing.txt > together.txt 2>&1
```

Starting with stdout and stderr both going to the terminal:

```text
> together.txt : stdout -> together.txt; stderr -> terminal
2>&1          : stdout -> together.txt; stderr -> together.txt
```

The command then runs with both outputs connected to the file.

Reversing the redirections changes the result:

```bash
cat greeting.txt missing.txt 2>&1 > together.txt
```

```text
2>&1          : stderr copies stdout -> terminal
> together.txt : stdout changes -> together.txt; stderr stays -> terminal
```

For `> together.txt 2>&1`, stdout already points to the file when stderr copies
its destination, so both channels go to the file. The precise rule is:

```text
2>&1 copies stdout's current destination.
```

## Exit status and conditional chaining

After a command finishes, it returns an integer exit status to the shell:

- `0` conventionally means success.
- A nonzero value conventionally means failure or another exceptional result.

In `zsh`, `$?` expands to the most recent command's exit status. It must be
checked immediately because every later command replaces it.

```bash
test -f greeting.txt
printf '%s\n' $?
```

`test -f PATH` produces no ordinary output; its result is expressed through
the exit status.

### Sequencing from exit status

```text
A && B    run B only if A succeeds (status 0)
A || B    run B only if A fails (nonzero status)
A ; B     run B after A regardless of A's status
```

These operators control whether another command starts. They do not carry text
between commands; a pipe carries stdout into another command's stdin.

## Variables, expansion, and quotes

A shell variable associates a name with text:

```bash
topic='shell mechanics'
```

There are no spaces around `=` in this assignment. `$topic` asks the shell to
perform parameter expansion: replace the reference with the variable's value.

```bash
printf '%s\n' "$topic"
```

Double quotes allow parameter expansion while keeping the resulting text
together as one argument. Single quotes preserve their contents literally, so
`'$topic'` is the characters `$topic`, not the stored value.

A backslash can protect one special character. In `"\$topic"`, it makes `$`
literal; the backslash itself is shell syntax and is removed before `printf`
runs.

Quoting also controls pathname expansion:

```text
*.txt      -> shell replaces the pattern with matching pathnames
'*.txt'    -> one literal argument: *.txt
```

### Shell variables and the environment

An ordinary assignment creates a variable in the current shell. `export NAME`
marks it to be inherited by programs started from that shell. `printenv NAME`
asks an external program to read the inherited environment.

### Command substitution

`$(command)` runs a command and substitutes its captured stdout, removing
trailing newline characters:

```bash
current_dir=$(pwd)
```

Redirections inside the substitution still work normally:

```bash
line_total=$(wc -l < greeting.txt)
```

On macOS, `wc` pads a displayed count with leading spaces. Command substitution
keeps those spaces; `printf '%d'` interprets the stored text as a number and
prints it without that padding.

## Aliases and history

An interactive alias is a shell-side text shortcut. It can reduce typing, but
does not create a new executable program. Use `alias NAME='replacement'` to
define one, `type NAME` to inspect how the shell resolves it, and `unalias NAME`
to remove it.

### Capturing status before it is replaced

A failed `type` appeared to show status 0 when `$?` was checked later, while a
controlled same-line check showed the actual status 1:

```bash
type showlong; printf 'status=%s\n' $?
```

History revealed an intervening typoed `printf`: it read status 1, then returned
0 itself. The corrected `printf` therefore read 0. Every command replaces `$?`,
including a command used only to display an earlier status. Capture it before
running anything else.

Interactive command history lets the shell recall earlier command lines.
History can contain passwords, tokens, or private paths if they were typed as
command arguments, so inspect it locally and avoid sharing sensitive entries.
History normally records submitted command text, not program output. If an
output transcript is pasted into the command line and submitted, however, that
pasted text becomes command input and can appear in history.

## Path forward

Work through one small step at a time, adjusting to observed understanding:

1. Shell, command, and ordinary output.
2. Sending output to a file with `>`; inspecting the result.
3. Replacing versus appending with `>>`.
4. Standard input and commands that consume it.
5. One pipe connecting two commands.
6. Standard error and separate routing.
7. Merging streams, redirection order, and `tee`.

Return to other Phase 5 shell mechanics in manageable lessons. This note is
an explanation and teaching outline, not evidence that these skills have
already been demonstrated.

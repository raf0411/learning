# First `xargs` experiment — 2026-11-08

A normal pipe connects the left command's standard output to the right
command's standard input. Some tasks instead need those incoming items to
become command-line arguments.

`xargs` performs that conversion:

```text
stdin text -> xargs -> arguments for another command
```

For example, `printf '<%s>\n' red blue` receives `red` and `blue` as arguments.
Because `printf` reuses its format, it prints one marked line for each argument.

## Inspect and predict

Run:

```bash
cd /Users/raffi/Learning/topics/linux/labs/2026-11-08-xargs-practice
cat colors.txt
```

Predict the complete output of:

```bash
xargs printf '<%s>\n' < colors.txt
```

```text
<red>
<blue>
<green>
```

## Try it

Run the command and paste the command plus output:

```text
raffi@Raffis-Mac 2026-11-08-xargs-practice % xargs printf '<%s>\n' < colors.txt
<red>
<blue>
<green>
```

Complete this sentence:

> `xargs` turned the words from its standard input into command line arguments for `printf`.

Tell me when the note is ready.

## Assessment

Prediction, execution, and explanation are correct. First application with
supplied syntax is successful; current stage: GUIDED.

## Whitespace boundary

The new file `labels.txt` contains three lines, but its second line contains two
words. Inspect it:

```bash
cat labels.txt
```

Predict the complete output and the number of marked items produced by:

```bash
xargs printf '<%s>\n' < labels.txt
```

```text
<red>
<blue>
<sky>
<green>
```

Number of marked items: 4

Run the command and paste the command plus output:

```text
raffi@Raffis-Mac 2026-11-08-xargs-practice % xargs printf '<%s>\n' < labels.txt
<red>
<blue>
<sky>
<green>
```

Based on the evidence, does default `xargs` treat each input line as one item,
or does it split on whitespace?

split on whitespace

Tell me when this section is ready.

### Whitespace assessment

Prediction, item count, execution, and inferred rule are correct. Default
whitespace parsing means this form should not be used for arbitrary pathnames
that may contain spaces. Null-delimited pathname handling will be taught with
file finding later.

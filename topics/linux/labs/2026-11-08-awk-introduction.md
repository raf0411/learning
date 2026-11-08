# First `awk` experiment — 2026-11-08

`awk` reads records one line at a time and splits each record into fields.
With whitespace-separated data:

```text
$1 = first field
$2 = second field
$0 = the complete current line
```

An `awk` rule can have a condition and an action:

```text
condition { action }
```

## Inspect and predict

Run:

```bash
cd /Users/raffi/Learning/topics/linux/labs/2026-11-08-awk-practice
cat scores.txt
```

Predict the complete output of:

```bash
awk '$2 >= 2 { print $1 }' scores.txt
```

```text
ada
cy
dax
```

## Try it

Run the command and paste the command plus output:

```text
raffi@Raffis-Mac 2026-11-08-awk-practice % awk '$2 >= 2 {print $1}' scores.txt
ada
cy
dax
```

In your own words, explain what `$2 >= 2` decides and what `print $1` does:

the second field of each lines in scores.txt is compared to >= 2 and print $1 prints the first field of eech lines in that file

Tell me when the note is ready.

## Assessment

Prediction and execution are correct. Precise rule: the action `print $1` runs
only for records whose second field satisfies `$2 >= 2`.

## Accumulate, then report

This rule runs once for every input record:

```text
{ total += $2 }
```

It adds the current second field to `total`. An `END` rule runs once after all
input records have been processed.

Predict the complete output of:

```bash
awk '{ total += $2 } END { print "total=" total }' scores.txt
```

```text
total=11
```

Run the command and paste the command plus output:

```text
raffi@Raffis-Mac 2026-11-08-awk-practice % awk '{ total += $2 } END { print "total=" total }' scores.txt
total=11
```

Why does the command print only once rather than once per input line?

because we added END rule which runs only if the total calculation has done every line

Tell me when this section is ready.

### Aggregation assessment

Prediction, total, and execution are correct. The explanation identifies that
`END` waits until all input records have been processed before reporting once.

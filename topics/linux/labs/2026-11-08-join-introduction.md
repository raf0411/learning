# First `join` experiment — 2026-11-08

`paste` pairs rows by position:

```text
line 1 + line 1
line 2 + line 2
```

`join` pairs rows by an equal field. By default it compares the first field of
both files. Its input files must be sorted by that field.

```text
file 1: key other-data     file 2: key other-data
                 equal key |
                           v
                 key data-from-1 data-from-2
```

## Inspect and predict

Run these as separate commands:

```bash
cd /Users/raffi/Learning/topics/linux/labs/2026-11-08-join-practice
nl -ba users.txt
nl -ba counts.txt
```

Predict the complete output of:

```bash
join users.txt counts.txt
```

```text
ada Design 3
cy Research 2
```

## Try it

Run the command and paste the command plus output here:

```text
raffi@Raffis-Mac 2026-11-08-join-practice % join users.txt counts.txt
ada Design 3
cy Research 2
```

Why are `bo` and `dax` absent from the result?

because bo exists in first file but not in the second file, and vice versa with dax

Tell me when the note is ready.

## Assessment

Prediction, execution, and explanation are correct. First application with
supplied syntax is successful; current stage: GUIDED.

## Include unmatched rows

`-a 1` also prints unpaired rows from file 1. `-a 2` does the same for file 2.

Predict the complete output of:

```bash
join -a 1 -a 2 users.txt counts.txt
```

```text
ada Design 3
bo Operations
cy Research 2
dax 5
```

Run it and paste the command plus output:

```text
raffi@Raffis-Mac 2026-11-08-join-practice % join -a 1 -a 2 users.txt counts.txt
ada Design 3
bo Operations
cy Research 2
dax 5
```

Tell me when this section is ready.

### Unmatched-row assessment

Prediction and execution are correct. The learner distinguished matched output
from retained unpaired rows in both input files.

# First `sed` experiment — 2026-11-08

`sed` is a stream editor: it can transform incoming text and write the result
to standard output. A basic substitution has this shape:

```text
s/old/new/
```

Without an in-place editing option, the input file remains unchanged. This
first form replaces only the first matching occurrence on each line.

## Inspect and predict

Run:

```bash
cd /Users/raffi/Learning/topics/linux/labs/2026-11-08-sed-practice
cat events.log
```

Predict the complete terminal output of:

```bash
sed 's/ERROR/WARN/' events.log
```

```text
WARN disk ERROR
INFO ready
WARN network
```

## Try and verify

Run the transformation, then inspect the original file:

```bash
sed 's/ERROR/WARN/' events.log
cat events.log
```

Paste both commands and their output:

```text
raffi@Raffis-Mac 2026-11-08-sed-practice % sed 's/ERROR/WARN/' events.log
WARN disk ERROR
INFO ready
WARN network
raffi@Raffis-Mac 2026-11-08-sed-practice % cat events.log
ERROR disk ERROR
INFO ready
ERROR network
```

Did the command modify `events.log`? State the evidence:

No, evidence:
raffi@Raffis-Mac 2026-11-08-sed-practice % sed 's/ERROR/WARN/' events.log
WARN disk ERROR
INFO ready
WARN network
raffi@Raffis-Mac 2026-11-08-sed-practice % cat events.log
ERROR disk ERROR
INFO ready
ERROR network

Tell me when the note is ready.

## Assessment

Prediction, execution, and source-file verification are correct. The learner
distinguished transformed stdout from stored input content.

## Global substitution and saving

Adding `g` after the final delimiter changes every matching occurrence on each
line:

```text
s/old/new/g
```

Construct one command that:

- reads `events.log`;
- changes every `ERROR` to `WARN`;
- saves the transformed text in `normalized.log`;
- displays nothing from that command in the terminal.

Your command:

```bash
sed 's/ERROR/WARN/g' events.log > normalized.log
```

Predict the complete contents of `normalized.log`:

```text
WARN disk WARN
INFO ready
WARN network
```

Run your command, then inspect both `normalized.log` and `events.log`. Paste
those commands and their output:

```text
raffi@Raffis-Mac 2026-11-08-sed-practice % sed 's/ERROR/WARN/g' events.log > normalized.log
raffi@Raffis-Mac 2026-11-08-sed-practice % cat normalized.log
WARN disk WARN
INFO ready
WARN network
raffi@Raffis-Mac 2026-11-08-sed-practice % cat events.log
ERROR disk ERROR
INFO ready
ERROR network
```

Tell me when this section is ready.

### Global-substitution assessment

The command construction, prediction, saved output, and final source-file check
are correct. Verification of the original file was initially omitted, then
supplied without rerunning the transformation.

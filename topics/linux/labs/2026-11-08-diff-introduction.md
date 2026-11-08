# First `diff -u` experiment — 2026-11-08

`diff` compares two files. The unified form, `diff -u`, shows nearby context
and labels changes from the perspective of the first and second operands:

```text
- line present in the first file
+ line present in the second file
  unchanged context line
```

The `---` and `+++` header lines name the two files; they are not file content.

## Inspect and predict

Run these as separate commands:

```bash
cd /Users/raffi/Learning/topics/linux/labs/2026-11-08-diff-practice
nl -ba old.conf
nl -ba new.conf
```

Before running `diff`, complete these predictions:

- Unchanged content lines: 
    port=8080
	color=blue
- Content line shown with `-`: 
	mode=test
- Content lines shown with `+`: 
	mode=production
	timeout=30

## Compare

Run:

```bash
diff -u old.conf new.conf
```

Paste the command and complete output here:

```text
raffi@Raffis-Mac 2026-11-08-diff-practice % diff -u old.conf new.conf
--- old.conf	2026-11-08 21:49:39
+++ new.conf	2026-11-08 21:49:39
@@ -1,3 +1,4 @@
 port=8080
-mode=test
+mode=production
+timeout=30
 color=blue
```

In one sentence, explain why `mode=test` gets `-` while `mode=production` gets
`+`:

because - means mode=test exists in the first file while + means mode=production exists in the second ifle

Tell me when the note is ready.

## Assessment

Prediction, execution, and explanation are correct. First application with
supplied syntax is successful; current stage: GUIDED.

## Exit status experiment

For `diff`:

```text
status 0 = the files are the same
status 1 = the files differ
status >1 = diff encountered a problem
```

Status 1 is an ordinary comparison result here, not evidence that `diff` failed.

Predict the two status lines:

```text
Different files: 1
Same file twice: 0
```

Then run these as two separate command submissions:

```bash
diff -u old.conf new.conf > changes.diff; printf 'different-status=%s\n' "$?"
diff -u old.conf old.conf > same.diff; printf 'same-status=%s\n' "$?"
```

Inspect both saved results:

```bash
cat changes.diff
wc -l < same.diff
```

Paste all four commands and their output here:

```text
raffi@Raffis-Mac 2026-11-08-diff-practice % diff -u old.conf new.conf > changes.diff; printf 'different-status=%s\n' "$?"
different-status=1
raffi@Raffis-Mac 2026-11-08-diff-practice % diff -u old.conf old.conf > same.diff; printf 'same-status=%s\n' "$?"
same-status=0
raffi@Raffis-Mac 2026-11-08-diff-practice % cat changes.diff
--- old.conf	2026-11-08 21:49:39
+++ new.conf	2026-11-08 21:49:39
@@ -1,3 +1,4 @@
 port=8080
-mode=test
+mode=production
+timeout=30
 color=blue
raffi@Raffis-Mac 2026-11-08-diff-practice % wc -l < same.diff
       0
```

Tell me when this section is ready.

### Exit-status assessment

All predictions and results are correct. The learner independently captured
`$?` before another command replaced it, distinguished an ordinary difference
from a command error, and verified both redirected artifacts.

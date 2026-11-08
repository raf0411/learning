# Phase 6 report checkpoint — 2026-11-08

Work from the requested result and choose the tools yourself. Use one pipeline.

## Task

The fields in `deployments.log` are:

```text
STATUS SERVICE REGION
```

Build a report that:

- includes only `READY` records, regardless of capitalization;
- counts records by service, treating service capitalization as equivalent;
- prints lowercase service names;
- ranks the counts numerically from highest to lowest;
- saves the report in `report.txt` without displaying the pipeline result.

## Inspect, construct, and predict

Run:

```bash
cd /Users/raffi/Learning/topics/linux/labs/2026-11-08-phase6-checkpoint
cat deployments.log
```

Your pipeline, on one physical line:

```bash
grep -i '^READY' deployments.log | cut -d ' ' -f 2 | sort | uniq -c | tr '[:upper:]' '[:lower:]' | sort -nr > report.txt
cat report.txt
```

Predict the complete contents of `report.txt` (ignore alignment spaces):

```text
3 api
1 db
```

## Execute and inspect

Run your pipeline, then inspect the saved report. Paste those commands and
their output once:

```text
raffi@Raffis-Mac 2026-11-08-phase6-checkpoint % grep -i '^READY' deployments.log | cut -d ' ' -f 2 | sort | uniq -c | tr '[:upper:]' '[:lower:]' | sort -nr > report.txt
raffi@Raffis-Mac 2026-11-08-phase6-checkpoint % cat report.txt
   2 api
   1 web
   1 web
   1 db
   1 api
```

## Verify

Run this as one command submission so `$?` captures `diff` immediately:

```bash
diff -u expected-report.txt report.txt; printf 'diff-status=%s\n' "$?"
```

Paste the command and output:

```text
raffi@Raffis-Mac 2026-11-08-phase6-checkpoint % diff -u expected-report.txt report.txt; printf 'diff-status=%s\n' "$?"
--- expected-report.txt	2026-11-08 22:21:21
+++ report.txt	2026-11-08 22:30:15
@@ -1,3 +1,5 @@
-      3 api
-      2 web
-      1 db
+   2 api
+   1 web
+   1 web
+   1 db
+   1 api
diff-status=1
```

Explain why the stage immediately before `uniq -c` is necessary. If you chose
a solution without `uniq -c`, explain instead how your command groups all
records for the same service:

i dont even know if im doing it right tbh

Tell me when the note is ready.

## Focused repair

Your current order is effectively:

```text
extract services -> sort mixed case -> count exact groups -> lowercase labels
```

At the counting stage, these are still different groups:

```text
API != api
WEB != web
```

Lowercasing the labels after `uniq -c` cannot combine counts that have already
been emitted. Move the `tr` stage so capitalization is normalized **before**
the grouping `sort` and `uniq -c` stages.

Revised one-line pipeline:

```bash
grep -i '^READY' deployments.log | cut -d ' ' -f 2 | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -nr > report.txt
cat report.txt
```

Run the revised pipeline, inspect `report.txt`, then rerun the same one-line
`diff` and immediate status check. Paste all results here:

```text
raffi@Raffis-Mac 2026-11-08-phase6-checkpoint % grep -i '^READY' deployments.log | cut -d ' ' -f 2 | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -nr > report.txt
raffi@Raffis-Mac 2026-11-08-phase6-checkpoint % cat report.txt
   3 api
   2 web
   1 db
raffi@Raffis-Mac 2026-11-08-phase6-checkpoint % diff -u expected-report.txt report.txt; printf 'diff-status=%s\n' "$?"
--- expected-report.txt	2026-11-08 22:21:21
+++ report.txt	2026-11-08 22:33:08
@@ -1,3 +1,3 @@
-      3 api
-      2 web
-      1 db
+   3 api
+   2 web
+   1 db
diff-status=1
```

Complete the causal chain:

> `tr` first makes all uppercase to lowercase. Then `sort` makes sorted alphabetically. Therefore `uniq -c` can sort it numerically by frequency from highest to lowest.

Tell me when the focused repair is ready.

### Tutor verification after fixture correction

The original expected file contained six leading spaces, while this system's
`uniq -c` emitted three. After correcting that tutor-created padding error, the
same generated `report.txt` verifies successfully:

```text
diff-status=0
```

The report data and repaired pipeline are correct. One explanation still needs
repair: `uniq -c` counts adjacent equal lines; it does not sort numerically.
The final `sort -nr` performs numeric descending ranking.

### Learner's corrected explanation

> `sort` sorts it alphabetically; `uniq -c` counts the frequency of adjacent
> equal lines; `sort -nr` ranks the counts from highest to lowest.

This is correct. The checkpoint report is successful with focused guidance;
independent reconstruction remains to be tested after spacing.

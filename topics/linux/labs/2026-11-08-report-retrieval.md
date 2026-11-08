# Request report — 2026-11-08

Short opening retrieval. Try from memory first; a partial attempt is useful.

## Inspect

Run these as separate commands:

```bash
cd /Users/raffi/Learning/topics/linux/labs/2026-11-08-report-retrieval
cat requests.txt
```

Each row contains a request status and a username, separated by one space.
Different capitalization refers to the same user.

## Build and predict

Write one pipeline that reports how many **OK requests** each user made.
Print lowercase usernames with their counts, highest count first.
Display the report in the terminal and leave the input unchanged.

Your command (one physical line):

```bash
grep -c '^OK' requests.txt; cut -d ' ' -f 2 requests.txt | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -nr
```

Before running, predict the complete output. Ignore alignment spaces:

```text
6
4 ada
2 bo
2 cy
```

## Try it

Run your pipeline. Paste the command and actual output here once:

```text
raffi@Raffis-Mac 2026-11-08-report-retrieval % grep -c '^OK' requests.txt; cut -d ' ' -f 2 requests.txt | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -nr
6
   4 ada
   2 cy
   2 bo
```

If the result differs from your prediction, keep both and briefly note what
you think caused it. Otherwise, leave this blank: 2 cy is first than 2 bo, idk why

## Explain

Choose one stage whose position matters. What would go wrong if you removed
it or moved it elsewhere?

sort should be before uniq -c so that uniq can group it correctly

Tell me when this note is ready. We will use your attempt to choose the next step.

## Focused retry

Your extraction, lowercase conversion, grouping, and ranking stages work.
The problem is selection: `;` separates the grep command from the pipeline,
and `cut ... requests.txt` reads the whole original file, including FAIL rows.
Also, `grep -c` emits a count rather than the matching rows.

Repair the command so matching OK rows flow into the field-extraction stage.
Keep the original attempt above. You do not need to repeat the prediction or
explanation. Run your revised command and paste it with its output here:

```text
raffi@Raffis-Mac 2026-11-08-report-retrieval % grep '^OK' requests.txt | cut -d ' ' -f 2 | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -nr
   3 ada
   2 cy
   1 bo
```

Outcome: correct after progressively stronger guidance. The main repair was to
make each stage consume the previous stage's standard output instead of counting
early or reopening the original input file.

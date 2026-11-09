# Independent report retrieval — 2026-11-09

## Task

Create `report.txt` from `checks.txt` in the directory below.

- Each input row is `status,component,note`, with no embedded commas.
- Include only rows whose status is exactly `PASS`, ignoring case.
- Report how many included rows belong to each component, treating component
  names case-insensitively and displaying them in lowercase.
- Put the largest count first. Each report line should contain the count and
  component name. Leading spaces in counts do not matter.
- Preserve `checks.txt`.

Use one pipeline to create the report. Choose the tools and their order yourself.
Try from memory first; if you consult documentation, briefly record what you
looked up. Keep your first attempt if you later revise it.

## Inspect and predict

These are two separate commands:

```bash
cd /Users/raffi/Learning/topics/linux/labs/2026-11-09-report-data
cat checks.txt
```

Before running your pipeline, write the report you expect from reading the data:

```text
   4 cache
   3 queue
   2 search
```

## Build and verify

Write your pipeline:

```bash
grep -i '^PASS' checks.txt | tr '[:upper:]' '[:lower:]' | sort | cut -d ',' -f 2 | uniq -c | sort -nr > report.txt
```

Run it, inspect the saved report, and paste the actual commands and output:

```text
raffi@Raffis-Mac 2026-11-09-report-data % grep -i '^PASS' checks.txt | tr '[:upper:]' '[:lower:]' | sort | cut -d ',' -f 2 | uniq -c | sort -nr > report.txt
raffi@Raffis-Mac 2026-11-09-report-data % cat report.txt
   4 cache
   3 queue
   2 search
```

Does the saved report match your prediction? If not, explain the discrepancy
and record any revision without erasing your first attempt.

Yes

In one or two sentences, explain why your chosen stage order produces the
requested counts:

im too lazy to explain this tbh,  i just order it when it make sense, pls skip this

Documentation consulted, if any: none (or `none`)

Tell me when this note is ready.

## Focused repair

Your normalization, extraction, counting, and saved-output verification worked
on this input. The selection includes an unwanted row: `^PASS` matches both
`PASS,...` and `PASSIVE,...`. Matching your prediction alone did not catch this
because the prediction included that same extra row.

Adjust the selection pattern to require the end of the first field immediately
after `PASS`. Use the input's field separator to identify that boundary.
Keep case-insensitive matching.

Rerun your revised pipeline and inspect `report.txt`. Paste the commands and
output below; no written explanation needed.

```text
grep -i '^PASS,' checks.txt | tr '[:upper:]' '[:lower:]' | sort | cut -d ',' -f 2 | uniq -c | sort -nr > report.txt

raffi@Raffis-Mac 2026-11-09-report-data % grep -i '^PASS,' checks.txt | tr '[:upper:]' '[:lower:]' | sort | cut -d ',' -f 2 | uniq -c | sort -nr > report.txt
raffi@Raffis-Mac 2026-11-09-report-data % cat report.txt
   4 cache
   3 queue
   1 search
```

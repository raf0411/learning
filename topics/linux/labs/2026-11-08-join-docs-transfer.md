 # Local documentation transfer: comma-separated `join` — 2026-11-08

The two files use commas instead of whitespace between fields. Find the `join`
option that makes one character the input and output field delimiter, then use
it to combine the files by their first field.

## Inspect

```bash
cd /Users/raffi/Learning/topics/linux/labs/2026-11-08-join-docs
cat departments.csv
cat tickets.csv
```

## Find the syntax locally

Open the manual:

```bash
man join
```

Search for `delimiter`, inspect the relevant option entry, then quit the pager.

Record the complete option syntax shown by the manual:

```text
-t char

Use character char as a field delimiter for both input and output.  Every occurrence of char in a line is significant.
```

- Option token: -t
- Required option-argument placeholder: char

## Apply it

Write one `join` command using a comma as the delimiter:

```bash
join -t ',' departments.csv tickets.csv
```

Predict its complete output:

```text
ada,Design,4
bo,Operations,2
cy,Research,3
```

Run it and paste the command plus output:

```text
raffi@Raffis-Mac 2026-11-08-join-docs % join -t ',' departments.csv tickets.csv
ada,Design,4
bo,Operations,2
cy,Research,3
```

Tell me when the note is ready.

# First `paste` experiment — 2026-11-08

`paste` combines files horizontally by line position:

```text
first line of file 1  +  first line of file 2
second line of file 1 +  second line of file 2
...
```

Its default separator is a tab.

## Predict

Run these setup inspections as separate commands:

```bash
cd /Users/raffi/Learning/topics/linux/labs/2026-11-08-paste-practice
cat names.txt
cat counts.txt
```

Predict the complete output of this command:

```bash
paste names.txt counts.txt
```

Write your prediction here. Use `<TAB>` to represent the invisible tab:

```text
ada<TAB>3
bo<TAB>1
cy<TAB>2
```

## Try it

Run the command, then run a second version that uses `:` instead of a tab:

```bash
paste names.txt counts.txt
paste -d ':' names.txt counts.txt
```

Paste both commands and their output here:

```text
raffi@Raffis-Mac 2026-11-08-paste-practice % paste names.txt counts.txt
ada	3
bo	1
cy	2
raffi@Raffis-Mac 2026-11-08-paste-practice % paste -d ':' names.txt counts.txt
ada:3
bo:1
cy:2
```

In one sentence: what determines which name is paired with which count?

first line file 1 + first line file 2

Tell me when the note is ready.

## Assessment

- Prediction: correct.
- Custom `:` separator: correct.
- Pairing rule: correct; line position determines the pair.
- The recorded `\t` represents a real tab in this terminal transcript. A byte
  check showed hexadecimal `09`, the tab character.

First application is successful with supplied syntax; current stage: GUIDED.

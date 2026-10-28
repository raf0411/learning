# Learner State

## Demonstrated capabilities

- Basic purposes of `pwd`, `ls`, and `cd` — INDEPENDENT verbal recall.
- Current/parent shorthand (`.` and `..`) — INDEPENDENT after correction.
  Correctly predicted and verified a five-step navigation sequence.
- Relative and absolute navigation — INDEPENDENT in a structured lab. Correctly
  used child, parent/child, and root-anchored paths.
- Previous-directory navigation (`cd -`) — INDEPENDENT in one prediction and
  observation.
- Basic `ls` use (`ls`, `-a`, `-l`, and a path operand) — GUIDED. Correctly
  interpreted hidden entries, long output, file-type characters, and inspection
  of another directory without moving.
- Home shortcut (`~`) — GUIDED. Direct observation corrected the prediction
  `/Users` to the actual home `/Users/raffi`.
- Directory creation with `mkdir` — GUIDED. Created sibling directories and
  missing parents with `-p`, and explained relative construction paths.
- Project-tree construction and verification — GUIDED. Initially omitted one
  requested branch and incorrectly judged the tree complete; repaired it after
  feedback and verified both requested children.

## Points requiring reinforcement

- Treat `.` and `..` as paths relative to the current directory; test this again
  after spacing because the initial model was reversed.
- `mkdir` creates directory entries; it does not change the shell's current
  working directory.
- Spaces separate command arguments, while `/` represents nesting within a path.
  The `-p` option creates missing parents; it does not cause nesting itself.
- Compare verification output against every requested branch before declaring a
  structure complete.

## Current learning edge

Complete the unscaffolded `copy-practice` directory-tree checkpoint in
`labs/2026-10-28-project-structure-check.md`. If successful, begin safe file
copying with `cp` and reuse navigation later for a spaced retention check.

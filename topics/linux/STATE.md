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
- Directory creation with `mkdir` — INDEPENDENT execution in one unscaffolded
  checkpoint. Built the requested `copy-practice` tree with correct relative
  paths; used `-p` safely but unnecessarily on some commands.
- Project-tree verification — GUIDED. Recorded correct `ls` evidence and the
  actual tree is complete, but left the explicit evidence mapping unfinished and
  initially attributed path nesting to `-p` rather than `/` in the pathname.

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

Complete the review correction in
`labs/2026-10-28-project-structure-check.md`: map every requested directory to
the recorded evidence and distinguish `/` path nesting from `mkdir -p` parent
creation. Then begin safe copying with `cp` and reuse navigation later for a
spaced retention check.

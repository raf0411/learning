# Review

## Current/parent relative navigation

- Stage: INDEPENDENT after correction
- Demonstrate: use `.`, `..`, and a compound relative path correctly in an
  unfamiliar directory tree without being told which form to use
- Why: the initial `.`/`..` model was incorrect before the navigation lab
- Last evidence: 2026-10-27, five correct predictions and matching observations
- Next review: after several lessons, embedded in a file-organization scenario

## Path nesting versus `mkdir -p`

- Stage: GUIDED
- Demonstrate: explain that `/` expresses path-component nesting and decide
  independently when `-p` is necessary across a sequence of `mkdir` commands
- Why: repeatedly attributed nesting to `-p` and initially ignored parents
  created by earlier commands
- Last evidence: 2026-10-29, predicted that `touch reports/daily.txt` would fail
  when `reports` was missing, then successfully created the directory and file
  separately; the initial prediction did not include a reason
- Next review: during a later file-organization task without naming the concept

## `cp` destination-path resolution

- Stage: GUIDED
- Demonstrate: derive the exact resulting path for both a file and a directory
  when the destination is an existing directory or supplies a new name
- Why: initially stopped at the containing directory; later included too much
  of the source path instead of appending only its final component
- Last evidence: 2026-10-28, derived `archive/demo` for copying
  `projects/demo` into existing `archive` after direct correction
- Next review: embedded in an overwrite-safety or multi-file copying task

## Relative operands and unchanged working directory

- Stage: GUIDED
- Demonstrate: choose a valid relative operand from the actual current
  directory and predict that `mkdir`, `cp`, and `mv` do not change the shell's
  working directory
- Why: from inside `move-practice`, predicted paths beginning with
  `move-practice/` and initially predicted that `mv` would change `pwd`
- Last evidence: 2026-10-29, correctly predicted and observed unchanged `pwd`
  across accepted/declined `mv -i` operations and several `touch` operations;
  all occurred within structured worksheets
- Next review: embed both ideas in a later unfamiliar file-organization task

## `mv -i` source and destination state

- Stage: GUIDED
- Demonstrate: independently predict both pathname states and both contents
  after declining or accepting replacement of an existing destination
- Why: the guided lab was correct, but accepted replacement must remain distinct
  from copying and from a separate delete operation
- Last evidence: 2026-10-29, correctly completed decline and accept cases and
  explained that accepted `cp -i` preserves the source path while `mv -i` does
  not
- Next review: embed in an unfamiliar file-reorganization task after spacing

## Existing-file behavior of `touch`

- Stage: GUIDED after correction
- Demonstrate: predict that `touch` updates timestamps without erasing existing
  content, and distinguish that from its missing-file creation behavior
- Why: initially predicted that touching an existing file would overwrite it
- Last evidence: 2026-10-29, copied nonempty content into `existing.txt`, ran
  `touch`, and verified that the 16-byte content remained unchanged
- Next review: test unexpectedly during later file setup or timestamp work

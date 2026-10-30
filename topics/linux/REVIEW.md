# Review

## Current/parent relative navigation

- Stage: INDEPENDENT after correction
- Demonstrate: use `.`, `..`, and a compound relative path correctly in an
  unfamiliar directory tree without being told which form to use
- Why: the initial `.`/`..` model was incorrect before the navigation lab
- Last evidence: 2026-10-27, five correct predictions and matching observations
- Next review: after several lessons, embedded in a file-organization scenario

## Path nesting versus `mkdir -p`

- Stage: INDEPENDENT
- Demonstrate: explain that `/` expresses path-component nesting and decide
  independently when `-p` is necessary across a sequence of `mkdir` commands
- Why: repeatedly attributed nesting to `-p` and initially ignored parents
  created by earlier commands
- Last evidence: 2026-10-30, independently planned and created
  `review/notes/2026` with `mkdir -p` in the integrated checkpoint
- Next review: after spacing, require a choice between sequential `mkdir`
  commands and `mkdir -p` in an unrelated setup task

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

- Stage: INDEPENDENT for a declined replacement
- Demonstrate: independently predict both pathname states and both contents
  after declining or accepting replacement of an existing destination
- Why: the guided lab was correct, but accepted replacement must remain distinct
  from copying and from a separate delete operation
- Last evidence: 2026-10-30, independently chose `mv -i`, declined replacement,
  and verified both distinct contents in the integrated checkpoint
- Next review: after spacing, test an accepted replacement in a new fixture

## Existing-file behavior of `touch`

- Stage: GUIDED after correction
- Demonstrate: predict that `touch` updates timestamps without erasing existing
  content, and distinguish that from its missing-file creation behavior
- Why: initially predicted that touching an existing file would overwrite it
- Last evidence: 2026-10-29, copied nonempty content into `existing.txt`, ran
  `touch`, and verified that the 16-byte content remained unchanged
- Next review: test unexpectedly during later file setup or timestamp work

## Safe file and empty-directory removal

- Stage: INDEPENDENT in unfamiliar checkpoint execution
- Demonstrate: orient and inspect before removal, use interactive confirmation
  appropriately, verify absence without treating the expected lookup error as
  a removal failure, and remove a small nonempty tree leaf first without hints
- Why: execution and predictions were correct in a structured lab, but the
  initial explanations confused `pwd` with preventing movement, misstated an
  exact relative path, and incompletely classified the commands used
- Last evidence: 2026-10-30, independently selected `rmdir` for an empty target
  and used previewed `rm -i` choices correctly in the integrated checkpoint
- Next review: after spacing, embed both commands in a different scenario

## Shell globbing and command-option separation

- Stage: INDEPENDENT in immediate transfer after correction
- Demonstrate: predict visible matches for an unquoted pattern; explain that the
  shell expands it before the program starts; distinguish selected pathname
  arguments from `ls -l` display and `rm -i` interaction; safely preview and
  act on several targets while connecting each prompt response to one path
- Why: the original attempt blended pattern selection, options, and prompt
  responses; the checkpoint operation was correct but the explanation again
  omitted the shell until corrected
- Last evidence: 2026-10-30, produced the exact post-expansion command for a
  novel `*.log` scenario and correctly mapped `y`, `n`, and an unmatched file
- Next review: after spacing, test with a different pattern and non-removal
  command to establish RETAINED

## Recursive removal boundary

- Stage: GUIDED after correction
- Demonstrate: from an unfamiliar working directory, resolve the exact root of
  a relative `rm -R` target, distinguish descendants from siblings, inspect the
  boundary, remove only the requested disposable hierarchy, and verify both
  absence and protected neighbors
- Why: the practical removal was safe, but the first explanation incorrectly
  named sibling paths as arguments and confused the working-directory base with
  the recursive root
- Last evidence: 2026-10-30, after direct equality/prefix instruction correctly
  classified a novel cache descendant, sibling branch, and parent
- Next review: after spacing, require an independent boundary diagram and exact
  target resolution before any recursive operation

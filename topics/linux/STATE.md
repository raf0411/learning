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
- Project-tree verification — GUIDED. Correctly mapped every requested child
  directory to recorded `ls` evidence after the mapping requirement was
  clarified; needed correction for the evidence proving the top-level directory.
- Path nesting versus `mkdir -p` — GUIDED. After repeated correction, identified
  `/` in `beta/gamma` as expressing the relationship and correctly identified
  the missing parent that `-p` would create in a transfer question.
- Basic single-file copying with `cp` — GUIDED. Correctly predicted, executed,
  and verified that the source remains and copies appear at two destinations;
  needed correction to distinguish a containing directory path from the full
  copied-file path, then correctly derived `archive/report.txt` independently.
- Interactive overwrite handling with `cp -i` — GUIDED. Declined and accepted
  replacement of a disposable destination, verified the content after both
  choices, and correctly explained that no prompt is needed when the target
  does not yet exist.
- Recursive directory copying with `cp -R` — GUIDED. Observed that plain `cp`
  rejected a directory, then copied and verified the complete subtree with
  `-R`. Needed correction to append only the source directory's final name when
  the destination directory already exists.
- File renaming and relocation with `mv` — GUIDED. Renamed `draft.txt` to
  `report.txt`, then independently predicted and verified the move to
  `review/report.txt`; confirmed preserved content, disappearance of the old
  path, and an unchanged working directory.
- Interactive replacement with `mv -i` — GUIDED. Correctly predicted and
  observed that declining preserved both paths, while accepting replaced the
  destination and made the old source pathname unavailable. Correctly
  distinguished accepted `mv -i` from accepted `cp -i` by whether the source
  pathname remains.
- Placeholder-file creation with `touch` — GUIDED. Created several empty files
  in one command, verified zero-byte sizes, predicted failure when a parent
  directory was missing, then created the parent and nested file separately.
  Initially predicted that touching an existing file would overwrite it; after
  correction, verified that a nonempty file retained its content and size.
- Interactive file removal with `rm -i` — GUIDED. Correctly predicted and
  verified that declining preserved the target and accepting removed it, while
  an unrelated file and the working directory remained unchanged.
- Empty-directory and leaf-first removal — GUIDED. Correctly predicted that
  `rmdir` would reject a nonempty directory and remove an empty one, then
  independently wrote and ran the two-step file-first, directory-second removal
  sequence without using recursive removal.
- Basic shell globbing — GUIDED with unresolved distinctions. Correctly
  predicted that `*.txt` would expand to the three visible `.txt` names,
  verified the resulting arguments with `printf`, previewed the two `*.tmp`
  targets, and identified the shell as the expansion component and `rm` as the
  confirmation component. Did not yet distinguish selection from `ls -l`
  display, predict default `zsh` behavior for an unmatched pattern, or apply
  separate `n` and `y` responses to the two `rm -i` targets.
- Command-effect classification — GUIDED after correction. Correctly separated
  filesystem-changing commands (`mkdir`, `touch`, `rm`, `rmdir`), shell movement
  (`cd`), and observation (`pwd`, `ls`); the first two attempts omitted commands.

## Points requiring reinforcement

- Treat `.` and `..` as paths relative to the current directory; test this again
  after spacing because the initial model was reversed.
- `mkdir` creates directory entries; it does not change the shell's current
  working directory.
- Compare verification output against every requested branch before declaring a
  structure complete.
- When evaluating whether `mkdir -p` is necessary, account for directories that
  earlier commands in the sequence have already created.
- Include the filename when asked for a file's exact path; a path ending at the
  containing directory does not yet identify the file.
- Interpret every relative path from the actual current working directory. From
  inside `move-practice`, `move-practice/inbox/draft.txt` would incorrectly
  look for a nested `move-practice` directory.
- Filesystem commands such as `cp`, `mkdir`, and `mv` do not move the shell;
  only a directory-changing command such as `cd` changes its working directory.
- Keep option purposes separate: `-i` controls replacement confirmation, while
  `cp -R` enables recursive directory copying.
- When an existing directory is the destination, append only the source item's
  final pathname component, not its entire parent path.
- `touch` primarily updates timestamps. It creates the final file when that
  file is missing, does not create missing parent directories, and does not
  overwrite an existing file's content.
- A reproducible command plan must include its starting-location command and
  the exact requested options. The first `touch` plan assumed the starting
  directory and substituted `ls` for the requested `ls -l`; it needed repeated
  correction before all seven commands were recorded.
- `pwd` reports the current working directory; it does not prevent directory
  changes. Its safety value before a relative removal is confirming the base
  directory from which the target path will be resolved.
- A listing of a parent directory proves that a child entry exists but does not
  enumerate that child's contents. Inspect the child itself when emptiness or
  internal entries matter.
- State exact paths from the recorded working directory. From inside
  `removal-practice`, the remaining file's relative path is `keep.txt`, not a
  reconstructed or misspelled parent path.
- Keep pathname selection separate from command behavior. The shell expands
  `*.txt`; `-l` changes how `ls` displays the already selected paths, not the
  selection and not the directory. Similarly, `*.tmp` selects the arguments
  for `rm`, while `-i` changes how `rm` handles each selected argument.
- In default `zsh`, an unmatched pathname pattern produces a shell error before
  the requested command starts. This was observed but not predicted or fully
  explained.
- For `rm -i` with several expanded arguments, read each prompt's pathname and
  connect each `n` or `y` response to that specific path's final state. The
  first multi-target attempt omitted the prompt transcript and removed both
  targets despite instructions to answer `n` and then `y`.

## Current learning edge

Continue the correction pass in
`labs/2026-10-30-globbing-safe-selection.md`. Revisit the first correction:
`*.txt` identifies the selected pathname arguments, while `ls -l` changes their
display rather than changing a directory. Then complete the unmatched-pattern
causal chain and the controlled `rm -i *.tmp` repeat, recording both prompts,
the `n`/`y` responses, and verification output. Recursive removal has not yet
been introduced.

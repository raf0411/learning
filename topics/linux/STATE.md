# Learner State

## Demonstrated capabilities

- Basic purposes of `pwd`, `ls`, and `cd` — INDEPENDENT verbal recall.
- Current/parent shorthand (`.` and `..`) — INDEPENDENT after correction.
  Correctly predicted and verified a five-step navigation sequence; nested
  parent traversal needed renewed correction on 2026-10-31 before successful
  immediate independent application (see two-level traversal below).
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
- Path nesting versus `mkdir -p` — INDEPENDENT in the Phase 2 checkpoint.
  Planned and created `review/notes/2026` from the checkpoint root with the
  correct nested operand and verified the resulting directory.
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
- Interactive replacement with `mv -i` — INDEPENDENT in an unfamiliar
  checkpoint decline case. Chose interactive movement, declined replacement,
  and verified that both distinct source and destination contents remained.
  Previously explained that accepted `mv -i` removes the old source pathname.
- Placeholder-file creation with `touch` — GUIDED. Created several empty files
  in one command, verified zero-byte sizes, predicted failure when a parent
  directory was missing, then created the parent and nested file separately.
  Initially predicted that touching an existing file would overwrite it; after
  correction, verified that a nonempty file retained its content and size.
- Interactive file removal with `rm -i` — GUIDED. Correctly predicted and
  verified that declining preserved the target and accepting removed it, while
  an unrelated file and the working directory remained unchanged.
- Empty-directory and leaf-first removal — INDEPENDENT in the Phase 2
  checkpoint. Correctly selected `rmdir` for an unfamiliar empty target and
  verified its absence. Earlier predicted that `rmdir` would reject a nonempty
  directory and independently performed leaf-first removal.
- Basic shell globbing — INDEPENDENT in immediate transfer after correction.
  Independently previewed and acted on `intake/*.tmp` in the checkpoint,
  preserving one prompted path and removing the other. Later expanded a novel
  `*.log` scenario to exact arguments and mapped `y` and `n` to the correct
  final path states. Earlier correctly expanded `report.*` to
  `report.md report.txt` and stated that `ls -l` changes only display. Correctly
  explained the leading-dot rule, concluded after correction that default
  `zsh` stops before starting `ls` on an unmatched pattern.
- Recursive removal with `rm -R` — GUIDED after correction. Predicted the
  protection provided by `rmdir` and plain `rm`, inspected a disposable tree,
  recursively removed only `doomed-tree`, and verified that `keep-tree` and
  `sentinel.txt` remained. Initially confused sibling paths with command
  operands and the working-directory base with the recursive root; later
  correctly resolved `cache` from `/work/project` as `/work/project/cache`.
- Command-effect classification — GUIDED after correction. Correctly separated
  filesystem-changing commands (`mkdir`, `touch`, `rm`, `rmdir`), shell movement
  (`cd`), and observation (`pwd`, `ls`); the first two attempts omitted commands.
- Integrated safe file organization — INDEPENDENT practical execution with
  GUIDED causal corrections. From an unfamiliar fixture, independently planned
  and carried out nested creation, placeholder creation, recursive copying,
  moving, declined copy and move replacements, previewed multi-file removal,
  empty-directory removal, and bounded recursive removal. All final filesystem
  states and protected contents were correct. Initial evidence omitted nested
  copy contents, and explanations confused the recursive root and shell
  expansion roles; both were corrected, with successful novel transfer.
- Symbolic links — GUIDED practical execution and understanding after
  correction. Completed target editing, target removal/recreation, and link
  removal experiments. Initially predicted target removal would remove the
  link and described the link as storing target data. After correction,
  independently explained that renaming the target leaves the stored pathname
  unchanged and reading through the link fails until that path exists again.
- Hard links — GUIDED, with successful causal explanation after correction.
  Observed shared inode/content behavior, an independent copy, and continued
  access after removing one name. Correctly explained that both names refer
  to inode 48272923 and that the surviving name does not depend on the removed
  pathname. Initial link-count error was corrected but not independently retested.
- Two-level relative parent traversal — INDEPENDENT in an immediate, focused
  application after teaching. From `relative-link-practice/links/deeper`, wrote
  and ran `cat ../../data/note.txt` without a supplied command; recorded
  `RELATIVE LINK CONTENT`. This supports current path construction, not retention
  or independent symbolic-link diagnosis.
- Tar archive workflow — INDEPENDENT practical execution for a bzip2 checkpoint,
  with evidence-recording omissions. After guided plain-tar and gzip work, used
  installed option mappings to create and list bzip2 and xz archives, then
  independently planned bzip2 create, member inspection, empty-destination
  checks, extraction, and preservation of source and neighbor entries. Tutor
  comparison confirmed all restored files matched their sources byte-for-byte.
  The checkpoint initially mislabeled the bzip2 artifact as `.xz` after swapping
  `-j` and `-J`; its scope was revised to bzip2 and the artifact was truthfully
  renamed without recreating it. This supports the archive workflow, not retained
  recall of the case-sensitive compression mapping.

## Points requiring reinforcement

- Relative symbolic-link paths — GUIDED execution, conceptual understanding
  still needs independent verification. Initially confused link location,
  stored pathname, and reached data, and used the shell's working directory
  as the stored target's base. Observed unchanged reads after `cd`, failure
  after moving the link, and success of a supplied two-parent correction.
  Parent traversal has earlier immediate independent evidence, but a 2026-11-01
  spaced retrieval check again skipped directory levels and required progressive
  scaffolding to resolve the target from the link's directory. Test this later
  without scaffolding; do not repeat it immediately.
- Nested parent traversal needs spaced review: repeatedly treated one `..`
  as reaching the lab root from two levels below before successfully writing
  and executing the correct two-parent `cat` command independently.

- Hard links: revisit shared file identity versus pathname references after
  spacing. The original-path dependency misconception was corrected in writing;
  independently counting all names, including the first, still needs verification.

- Compression selection versus filename convention: the command option selects
  the algorithm; a `.gz`, `.bz2`, or `.xz` suffix does not. The learner used
  `-J` correctly during guided transfer, then independently used `-j` while
  calling it xz in the checkpoint. Re-test `-j` = bzip2 and `-J` = xz after
  spacing, preferably using content inspection rather than trusting the suffix.

- Archive evidence recording: the independent checkpoint omitted actual output
  for the initial source inspection and did not record nested listings or file
  contents after extraction. The final artifact was correct and tutor comparison
  confirmed equality, but a later task should require complete learner-recorded
  evidence before declaring restoration verified.

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
- Keep pathname selection separate from command behavior. This was corrected
  successfully in an immediate transfer: the shell selects pathname arguments,
  while `ls -l` changes display and `rm -i` changes treatment of each selected
  path. Re-test after spacing with a different pattern and command.
- In default `zsh`, an unmatched pathname pattern produces a shell error before
  the requested command starts. The causal chain was completed after direct
  correction and still needs later independent retrieval.
- For `rm -i` with several expanded arguments, continue reading each prompt's
  pathname and mapping its own `n` or `y` response to that path. The controlled
  repeat succeeded after the initial attempt removed both targets.
- Resolve a relative recursive-removal operand from the actual `pwd`. The
  working directory is the base; the resolved operand is the removal root; its
  descendants are inside the recursive boundary, while parent and sibling paths
  are outside it unless separately named.

## Current learning edge

Phase 3's archive milestone is complete. The learner created, listed, extracted,
and verified plain and compressed tar archives, then independently completed the
workflow with bzip2 after the checkpoint was honestly re-scoped. Symbolic-link,
hard-link, nested-path, compression-flag, and evidence-quality items remain in
spaced review; do not immediately repeat the full archive lab.

Next: begin Phase 4 with content inspection and local documentation. `file` is
a motivated starting point because it exposed the mislabeled archive by content
rather than suffix. Then distinguish appropriate uses of `cat`, `less`, `head`,
`tail`, and `nl` before introducing terminal editing. Embed one short delayed
`-j` versus `-J` retrieval check in later inspection work. At session close on
2026-11-01, the learner reported knowing only `cat` for content viewing; the
prepared `labs/2026-11-01-less-pager.md` remained completely unfilled. Resume
with that worksheet rather than re-probing or repeating archive work.

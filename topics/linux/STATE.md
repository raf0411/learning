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
  renamed without recreating it. On 2026-11-02, independently retrieved
  `-j` = bzip2 and `-J` = xz after spacing and verified content format despite a
  misleading suffix; the case-sensitive mapping is now RETAINED.
- Content classification and viewer selection — INDEPENDENT in the Phase 4
  checkpoint. Correctly used `file` to distinguish text, a directory, and
  bzip2 data despite misleading suffixes; selected `cat`, `head -n`, and
  `tail -n` for exact requested boundaries with complete output.
- Interactive pager use — INDEPENDENT execution with GUIDED causal explanation.
  Used `less -N`, forward search, `n`, and `q` to record exact matches at lines
  9 and 16 in an unfamiliar log. Still needed direct explanation that screen
  position, search term, and selected match are temporary viewer state.
- Line-numbered inspection with `nl` — INDEPENDENT in the current learning
  period. Predicted and observed default nonempty-line numbering versus
  `nl -ba` numbering all lines, then independently used `nl -ba` for exact
  configuration verification.
- Terminal text editing — INDEPENDENT in reduced-scaffolding and integrated
  tasks. Searched and edited disposable text with the Mac's Pico-backed `nano`,
  saved with `Ctrl-O`, exited with `Ctrl-X`, deliberately discarded one
  unsaved buffer, and later produced and verified exact three- and five-line
  results without procedural keystroke hints.
- Live log following — GUIDED practical success. Correctly predicted and
  observed `tail -f` displaying a newly appended line from another process and
  stopping with `Ctrl-C`. After correction, reconstructed `tail -F server.log`
  for a rotated-path scenario; independent transfer remains untested.
- Local documentation use — GUIDED. Successfully navigated `man`, program
  `--help`, and Bash `help`, but did not independently extract and apply the
  unfamiliar `file -b` option. In a second task, found `head -c` but omitted its
  required count argument until direct explanation.
- Command anatomy for option arguments — INDEPENDENT immediate transfer after
  correction. Correctly labeled program, option, option argument, and operand
  in `tail -n 4 app.log`, then constructed `head -c 7 sample.txt`. Retention and
  use while reading unfamiliar documentation remain untested.
- Output replacement and append redirection (`>` and `>>`) — GUIDED with one
  successful immediate transfer. Initially called `>` append while also
  predicting overwrite; then predicted and observed replacement, no terminal
  output, and later append behavior. Independently mapped a simple pipeline
  followed by `>` to the exact two-line file result.
- Standard input redirection (`<`) — GUIDED. Correctly identified the pathname
  as a shell redirection target rather than a `cat` operand, but needed direct
  explanation that operand-free `cat` reads standard input before observing the
  expected content.
- Standard output, standard error, and `2>` — GUIDED with successful immediate
  application after a refresher. On 2026-11-04, correctly identified that a
  right-side `2>` belongs only to `wc`, that unredirected `cat` stderr remains
  on the terminal, and that only `cat` stdout enters a normal pipe. The first
  worksheet still confused input contents with `wc` output and omitted required
  verification evidence before focused repair.
- Basic pipelines (`|`) — GUIDED with independent success in a simple transfer.
  Correctly predicted `printf ... | tail -n 1` and a pipe followed by output
  redirection. On 2026-11-04, successfully transferred the rule to `cat | wc`
  after a refresher and explained that the pipe carries stdout by default.
- Stream merging and redirection order (`2>&1`) — GUIDED with successful
  immediate application. Correctly predicted and observed that merging `cat`
  stderr into stdout made `wc -l` count six lines. Initially predicted that
  `2>&1 > file` would put stderr in the file; a stepwise destination-label model
  corrected this. Then correctly predicted and verified both orderings:
  `> file 2>&1` stored both streams, while `2>&1 > file` left stderr on the
  terminal and stored only stdout. Spaced independent transfer is untested.
- `tee` and `tee -a` — GUIDED practical execution. Correctly predicted and
  observed that basic `tee` both displayed and stored two input lines. Initially
  predicted that `tee -a` would redisplay old file content, then observed that
  it displayed only new stdin while appending it. In a merged-stream example,
  initially omitted the diagnostic despite `2>&1`; after a reminder, correctly
  predicted and observed all six lines in both terminal output and the file. In
  a 2026-11-05 two-pipe checkpoint, correctly predicted five of six outcomes,
  including diagnostic merging, exact capture contents, and the final count,
  but incorrectly expected `tee` stdout on the terminal and could not yet
  reconstruct that the second pipe carries it to `wc` stdin.

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

- Archive evidence recording: the independent checkpoint omitted actual output
  for the initial source inspection and did not record nested listings or file
  contents after extraction. The final artifact was correct and tutor comparison
  confirmed equality, but a later task should require complete learner-recorded
  evidence before declaring restoration verified.

- Local-documentation syntax extraction: distinguish a standalone flag from an
  option followed by a required placeholder argument, copy the complete option
  entry, place every required token in the command, and verify that actual
  output meets the stated goal without hints. On 2026-11-03, initially selected
  `touch -d` despite its description changing both timestamps; after a hint,
  derived valid `touch -m -d` syntax but still misclassified tokens and did not
  independently produce a coherent proof transcript.
- Evidence capture and self-audit: repeatedly recorded commands without their
  output or omitted requested prompt/control evidence. The integrated Phase 4
  checkpoint also omitted the original configuration output before editing. On
  2026-11-03, reused a stale timestamp baseline, ran bare `touch` as supposed
  content evidence, omitted requested commands, and declared success despite an
  explicit unequal access-time comparison. Eventually corrected the conclusion
  to failure. On 2026-11-05, recorded only `no output` for the checkpoint
  execution while omitting the command and returned prompt, then checked a
  self-audit item claiming that evidence was present. Separate `cat -n`
  verification did prove both stored results, but the learner could not yet
  audit that proof independently. Inspect and record fresh pre-state, preserve
  causal command order, then audit every material claim before declaring
  completion.
- Standard-stream routing: keep stdout and stderr as independent channels until
  explicitly merged. `|` carries the left command's stdout by default, and a
  redirection belongs to the command section where it is written. For `2>&1`,
  remember that stderr copies stdout's destination at that moment; a later
  stdout redirection does not update it. `tee` forwards only its current stdin,
  not old file contents. The 2026-11-04 guided experiments succeeded, but the
  learner initially lost stderr in a merged `tee` pipeline. On 2026-11-05, the
  checkpoint showed strong result prediction but continued confusion among a
  command's stdin, stdout, a pipe destination, and `tee`'s separate file copy.
  A worked example was supplied; the guided retry remains unfinished.
- Pager viewer state: practical navigation and search are independent, but the
  learner twice could not explain what changes temporarily during `less`.
  Re-test later using screen position and selected search match versus stored
  file data; do not repeat immediately.
- `tail -f` versus `tail -F`: the pathname/file-identity correction succeeded,
  but the first explanation was incorrect and the exact command needed a
  follow-up. Test later in a novel rotation scenario.

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

Phase 5 is current. Phase 4 is complete for curriculum progression; unfamiliar
local-documentation recovery remains GUIDED and stays in the review queue rather
than blocking forward progress.

Simple `>`, `>>`, `<`, `2>`, and `|` experiments have succeeded. Guided work on
2026-11-04 added `2>&1`, left-to-right redirection order, `tee`, and `tee -a`.
On 2026-11-05, the learner attempted the two-pipe checkpoint and correctly
predicted five of six outcomes, but could not causally route `tee` stdout through
the second pipe to `wc` stdin. Execution evidence also omitted the command and
returned prompt despite an inaccurate checked self-audit item.

Next session, resume only sections 6–8 of
`labs/2026-11-05-phase5-stream-routing-repair.md`; do not rerun the original
pipeline. After the guided reconstruction, use a shorter, different pipeline
for independent transfer. Continue spaced review of documentation syntax,
pager state, `tail -f` versus `-F`, link reasoning, and archive evidence without
reopening Phase 4.

# Review

## Current checkpoint — 2026-11-21 continuation (session complete)

- **Quizzes:** none.
- **Combined `[` tests and polarity:** still due, untested. The opener was skipped before any answer. Instead of a separate drill, test it through the capstone's log-file guard: predict scenarios C (missing) and D (directory) before coding it.
- **Predict-then-verify:** still weak. Built into the capstone design; section 7's expected results must be filled before code.
- All other items below are unchanged.

## Earlier checkpoint — 2026-11-21 (first session)

- **Quizzes:** 1 answered, 0 correct, 1 incorrect, 0 I-don't-know. The learner thought `check-list-arg.sh 'good paths.txt'` checks the argument itself rather than the lines inside the list.

- **Combined `[` tests and branch polarity**
  - Stage: GUIDED
  - Next: a short unfamiliar application without hints, such as a guard requiring two properties, where the learner states which branch runs for three inputs.
  - Why: this session produced `-fr`, `![`, and an inverted `! -f`, with no spontaneous trace. Polarity has inverted on 11-17 and 11-21.

- **Argument as data versus as the name of a data source**
  - Stage: corrected, retest needed
  - Next: later, in a new task specification, have the learner predict the outputs before coding.
  - Why: attempt 1 reused the 11-16 argument-loop design, and the diagnostic quiz confirmed the misreading.

- **Readable versus regular-file prechecks**
  - Stage: taught
  - Next: later, predict which of directory, `/dev/null`, a missing path, and a regular file pass `-r`, `-f`, and both.
  - Why: the directory list passed `-r`, read failed, and the script exited 0. The learner did not flag this.

- **Predict-then-verify and self-audit**
  - Stage: weak
  - Next: in the next script task, require a filled predictions table before any run and a per-test comparison to the spec. Append failures rather than replacing them.
  - Why: two unflagged failures, three skipped predictions, and replaced evidence.

- **ELAPSED versus TIME (process state)**
  - Stage: GUIDED
  - Next: after spacing, explain a ps/top row for a busy loop versus a sleep in own words, including why polling would raise TIME.
  - Why: retrieval failed at the opener. The post-reteach answer was mostly correct, but ELAPSED was imprecise and the polling link was missing.

- **Superseded:** the 11-17 next-step instruction to resume the list checkpoint is complete. Do not rerun it.

## Current checkpoint — 2026-11-17 (session complete)

- Input validation and branch polarity — GUIDED. Next: construct missing/empty argument and readable-regular-list guards in the parameterized-list checkpoint without repair hints. Last evidence: omitted initial guard; later inverted -r branch; correct success/else repair verified 1/2 outcomes. Conceptual recognition alone has not established independent construction.
- Function return versus stored flag — GUIDED. Later predict/apply return status separately from variable contents and script exit, without supplying assignment-status rule. Test-only function refactor and reporting-function alternative both worked; do not repeat completed function lab.
- Line-input and parameter scope — GUIDED. Next combine script argument for list selection with function argument for each entry; preserve whitespace, maintain failure across iterations, and distinguish working-directory-relative names from script location. Supplied read loop correctly predicted and integrated today.
- Verification coverage — immediate captures correct, scenario selection GUIDED. Later independently test all-success, failure-then-success, unavailable input, and invalid invocation, with complete actual transcripts. Failure-last tests needed a reminder; some previous worksheet evidence was replaced rather than appended.
- Diagnostics and precheck limits — GUIDED. Later distinguish unreadable/nonexistent/non-regular input and prechecks versus actual opening/reading. Current inaccurate missing-only diagnostic and older usage filename remain minor unverified edits, not reasons to rerun completed functional labs.
- Quizzes observed today: 3 questions, 3 correct, 0 incorrect, 0 I-don't-know. Topics: failure followed by printf, assignment status versus stored value (rule supplied), and missing-loop-input failure masked by final exit 0. Detailed evidence: sessions/2026-11-17.md.
- Running vs S (continuation, same date) — 1 quiz, 1 correct: sleep process with S, ELAPSED 02:00, TIME 0 correctly identified as alive/not executing, kernel-managed wakeup; polling, stopped, and zombie rejected. First correct spaced recognition after repeated misses. Next: one-sentence open explanation of why ELAPSED-growing/TIME-flat rules out polling, then later apply in an unfamiliar top/ps scenario (e.g. contrast with a busy process). Day quiz total: 4 answered, 4 correct.
- Resume labs/2026-11-17-list-checkpoint.md: fixture directory recorded at closure; script and five tests remain TODO (re-verified at continuation closure). Recheck temporary fixtures before use. Prior local-file/function/read-list labs are functionally complete with guidance; their old next-step instructions below are superseded.

## Current checkpoint — 2026-11-16 (session complete)

- Remembering failure versus stopping — GUIDED. Supplied accumulator pattern correctly returned 1 after mixed outcomes and 0 after all successes, but learner also replaced input-guard exit 2 with assignment. Restored after correction; usage-only/status 2 verified after an additional reminder. Next independent application is the prepared file-checkpoint task. Later test initialization placement, persistence across iterations, and early invalid-input termination without scaffolding.

- Direct script execution and narrow permissions — GUIDED. Correct shebang but initially omitted execute permission; then chose 774 from baseline 664, granting group execute unintentionally. Component hints led to g-x and verified 764; direct run/status 0 confirmed. Later test owner-only symbolic modification preserving all other bits and distinguish interpreter choice, file execute permission, and ./ path selection. No immediate repeat needed.

- Argument iteration — GUIDED. Later retrieve literal words versus variable expansion and "$@" preserving argument boundaries. First loop used a scalar assignment then iterated over literal targets; supplied repair produced two correct lines including a spaced argument. Extra-argument and exit-in-loop recognition correct; multi-URL body subsequently combined correctly, with guard/verification still guided. Next independent combination: unattempted local-file checkpoint.
- Multi-argument guard and verification — GUIDED. Quoted "$@" wrongly used with unary -z; teaching restored "$1". Later distinguish a single string from a list of arguments without hints. Correct loop/conditional composition, but omitted requested final retest twice; actual chat evidence ultimately verified no guard error and two successful requests. Full workflow remains guided. Do not repeat completed lab.
- Final observed quizzes: 8 questions, 7 correct, 1 incorrect, 0 I-don't-know. Correct: lookup evidence scope, printf masking nested curl failure, missing argument expansion, later grep conditional/final status, unused extra argument, exit inside a loop, and later success masking an earlier failure. Incorrect: false if-test automatically stops script. Details in sessions/2026-11-16.md.
- Bash control flow — GUIDED. Later test independent construction: distinguish URL input from exit status, run a command as an if condition, choose branches using 0/nonzero, and explicitly signal failure when needed. Full corrected block was supplied; correct final recognition is not independent coding.
- Status preservation — GUIDED integration despite independent immediate capture command construction. Later test a new script where diagnostic output could overwrite the needed status. Repeatedly checked printf rather than curl; final supplied direct conditional avoided the problem.
- Verification completeness — record every test's actual immediate status, not inferred values. Two-path guard test initially omitted both captures; supplied reminder repaired it. No immediate full repeat needed.
- HTTPS versus HTTP and transfer versus application success — explicit scheme omission recurred during script repair. Later test scope in a different task; curl status 0 is not necessarily HTTP 2xx. Opening lookup-scope retrieval correct.

## Latest checkpoint — 2026-11-15 (session complete)

- Final observed quiz tally: 6 questions, 4 correct, 2 incorrect, 0 I-don't-know. Correct: shared physical pages counted in both RES values; authentication rejection stage; post-teaching UDP local-send versus remote-arrival evidence; most-recent-command status after an intervening successful printf. Incorrect: assumed forwarded ports must match; assumed UDP guarantees once/in-order delivery. UDP worksheet separately contained an honest open-ended knowledge gap about future-delivery guarantees, not a quiz opt-out. Later test shared-RAM application, not another immediate arithmetic loop.
- SCP direction — GUIDED. Correct port/context but reversed source/destination in execution; corrected after conceptual hint. Later construct an unfamiliar transfer without operand-order scaffolding.
- Two-sided hash verification — INDEPENDENT immediate construction. Fresh local and remote shasum commands produced matching SHA-256 digests. Later integrate verification without prompts to test retention.
- Evidence limits — initially reported mismatch without hashes; corrected after feedback and measured equality. Distinguish failed transfer, unperformed comparison, and measured mismatch in later diagnosis.
- Endpoint binding — GUIDED: after ss inspection still attributed hypothetical loopback-only listener failure to differing forwarded port numbers. Later distinguish valid port translation from wrong destination binding.
- Web evidence — tool selection independent; interpretation GUIDED. Resolution does not establish website existence, and HEAD 200 does not establish all website functionality. Later test evidence scope without leading alternatives.
- Timeout scope — GUIDED: connect-timeout chosen for total bound; recovered max-time after scope/manual hint. Retrieve in a later different task.
- UDP — GUIDED completed ss inspection and loopback datagram experiment; receiver output and exit verified. Correct arrival-evidence identification; future guarantees honestly unknown until explained. Post-teaching recognition correctly distinguished local send success from unverified remote arrival. Later assess limits and application-level reliability after spacing; no immediate repeat needed.
- Integrated diagnosis — GUIDED despite independent tool selection and curl total-timeout construction. Resolver operands included https://; confused lookup failure with missing resolver. Corrected getent target/control comparison after hints; revised conclusion recognized name-specific failure but terminology and untested layers still needed teaching. Later test hostname versus URL, lookup result versus resolver, and evidence-supported next action without scaffolding.
- Immediate exit status — requested capture omitted; curl diagnostic (6) and its manual meaning correctly identified instead. Closing quiz correctly recognized most-recent-command replacement; practical capture still unverified today. Test actual immediate capture in the first Bash script lab, not another identical recognition question. Evidence fidelity also needs review: revised resolvectl command retained scheme while output changed; do not reconstruct transcripts.
- Next: first Bash script worksheet is unattempted; use it for actual status-capture evidence. Later spaced networking review should test independent diagnosis, not another full pass over completed worksheets. Independent connectivity milestone remains open. Detailed evidence: sessions/2026-11-15.md.

## Latest checkpoint — 2026-11-14 (networking continuation complete)

- Observed continuation quizzes: 6 questions, 2 correct, 3 incorrect, 1 I-don't-know. Correct: ping does not establish web access; refused SSH despite reachable host. Incorrect: shared-page automatic deduplication, TCP port as cable socket, reverse SCP using guest port 22. I-don't-know: listener evidence versus Mac reachability/login. Date total with earlier session: 14 questions, 8 correct, 5 incorrect, 1 I-don't-know.
- Host/guest endpoint reasoning — GUIDED. Next test: construct a reverse SCP transfer without the completed command supplied. Need remote source/local destination, Mac endpoint port 2222, and execution from Mac shell. Initial remote-source recognition was correct, but connection-port selection was not. Worksheet labs/2026-11-14-scp-download-checkpoint.md remains unattempted.
- Evidence-based network diagnosis — GUIDED. After spacing, distinguish interface configuration, selected route, ICMP replies, name-resolution result, HTTPS response, listener state, and authenticated access. Two correct recognition checks do not establish independent tool choice. Include loopback-only versus wildcard bindings and the separate network path/authentication gates.
- SSH identity and transfer verification — GUIDED. Later demonstrate fingerprint comparison and two-sided file verification without prompts. Successful login reported; trust-prompt comparison not shown. Upload hashes matched, but local hash required reminder. Practice files are temporary: recheck rather than assume continued existence.
- Command submission — path typo and template/newline failures repaired with help. In next practical task, assess literal paths and one physical command line; avoid interpreting these execution errors as network misconceptions.
- Shared RAM — GUIDED, still unresolved. Latest check selected automatic deduplication when summing RES. Revisit briefly after other material using per-process views versus unique physical pages, without another immediate arithmetic loop.

## Earlier checkpoint — 2026-11-14 (before networking continuation)

- Quiz evidence: 8 questions, 6 correct, 2 incorrect, 0 I-don't-know. Correct: blocked sleep timing, available-RAM estimate, known TERM-ignoring fixture escalation, enabled-versus-active, post-teaching activation evidence, fixed cron minute. Incorrect: adding SHR to RES and double-counting the same shared pages across process totals.
- Personal cron — GUIDED completed safe one-minute recurring log task and verified removal. Later construct an unfamiliar schedule, distinguish fixed fields from intervals and clock boundaries from install-relative delays, and preserve existing entries during changes. Immediate fixed-minute quiz correct; all lab commands supplied. No personal crontab remains; do not reinstall completed exercise for review.
- Service investigation — query construction INDEPENDENT immediate application; interpretation GUIDED. Later retrieve status versus definition versus journal, loaded/static/active distinctions, and activation versus completed work. dbus lab omitted definition until supplied command; static explanation and log-evidence conclusions required teaching. No immediate repeat of completed worksheet.
- Memory accounting — GUIDED. At a later session, briefly distinguish resident versus virtual memory, SHR inclusion in RES, and duplicate shared pages across processes without preceding reteaching. Last evidence 2026-11-14: two visual corrections supplied; no independent corrected retrieval. Use one short check, not another long arithmetic loop.
- Process state — correct spaced timing recognition, but causal explanation and top state-versus-interval interpretation still need independent assessment. Top/ps observations were guided.
- Signal escalation — GUIDED full workflow despite independent signal choice/execution. Known disposable job exited; ps verification added after reminder. Three-second wait annotation precedes TERM, so post-TERM waiting remains unverified. Written rationale still treated persistence as sufficient; tutor corrected. Later test bounded waiting, contextual escalation justification, and both exit checks without prompts. Do not repeat today's completed lab or reuse PID 5387.
- Available-RAM selection — correct spaced recognition. Later embed demand-versus-capacity reasoning in practical diagnosis rather than repeating the same selection quiz.
- User-service lifecycle — GUIDED successful transient creation/restart/stop/collection. Independently constructed complete user-unit journal query after --user teaching. Later demonstrate fresh-target service control and verification without supplied commands; distinguish user/system managers, unit name/process identity, and absent current unit versus retained journal history. tutor-sleep.service stopped and collected; do not restart the completed lab immediately.

## Previous checkpoint — 2026-11-13

- Quiz evidence: 7 questions, 4 correct, 3 incorrect, 0 I-don't-know. Correct: Running/S recognition, post-correction RAM-demand risk, incomplete du totals, bounded TERM cleanup wait. Incorrect: free disk automatically becoming swap, S-state pipe wait interpreted as polling, sleep timing interpreted as continuous checking.
- RAM/swap — GUIDED. After spacing, require demand-versus-capacity reasoning without treating spare disk as configured swap or adding buff/cache to available again. Immediate corrected scenario is not retention.
- Running/S — GUIDED, unresolved. Written integrated checkpoint asserted CPU execution during S; two follow-up quizzes selected polling. Actual sleep timing (5.005s elapsed, 0.004s CPU) and busy-loop timing (2.794s elapsed, 2.777s CPU) contrasted with teaching. No independent retrieval after final contrast. Pause repetitive immediate quizzes; later assess alive versus executing and who manages a sleeping process's wakeup.
- Process/parent ps queries — RETAINED construction. Later integrated checkpoint independently completed jobs/process/parent inspection, fresh target check, TERM, and dual exit verification. Complete workflow INDEPENDENT this session; no immediate repeat needed. All test jobs exited; never reuse recorded IDs without fresh checks.
- Integrated RAM checkpoint selected free -h independently and rejected automatic disk-to-swap use, but used free rather than available until corrected. Keep available-selection review active; successful revised answer was guided.
- Permission-limited du — correct spaced recognition; privileged comparison completed. Later integrate error assessment naturally, not another immediate isolated quiz.
- Signal escalation — GUIDED practical coverage complete: observed TERM cleanup delay and separate known TERM-ignoring fixture; supplied KILL and exit checks verified completion. Next assess independent escalation reasoning and complete evidence in a reduced-scaffolding scenario. Both jobs exited; no recorded identifier is a future target.
- The top memory inspection is complete; its column interpretation was taught, not independently tested. Instantaneous state versus interval-based %CPU was introduced at session close, not assessed. Next session first retrieve the underlying sleeping-versus-executing distinction with one short evidence-based check; avoid another long correction worksheet. These updates supersede older unattempted-top instructions below.

## CPU load, available RAM, and disk scope

- Stage: interpretation GUIDED; immediate home-directory du construction
  INDEPENDENT (2026-11-12)
- Demonstrate: distinguish Linux load from CPU utilization, account for sampling
  windows/non-CPU contributions, interpret free versus available RAM without
  assuming either shortage or safety, and select df versus du by scope.
- Evidence: guessed load 4 on two CPUs guarantees 100% CPU. After teaching,
  recognized available RAM as more relevant than free but overclaimed no worry.
  Independently built/executed home-directory du; RAM versus disk explanation
  needed a terminology correction. Supplied resource commands executed correctly.
- Latest 2026-11-12 continuation: worksheet attempted. Independently selected
  available RAM and constructed du -sh /var/log; explicitly did not know to
  compare application demand with available RAM. Tutor explained demand, load
  contributors/time windows, and wa accounting. Actual free -h inspected with
  tutor interpretation (558Mi available, no swap); independent diagnosis untested.
- Permission-limited totals remain a gap: claimed du can count everything, then
  chose the same misconception in a quiz after teaching. Directory traversal and
  metadata access versus file-content reading were retaught.
- Next: unattempted top -o %MEM memory inspection. Later retrieve demand versus
  capacity and permission-limited du evidence in short unfamiliar scenarios.
  Do not reopen the completed worksheet for another full pass.

## Program instances, jobs, and process inspection

- Stage: fresh PID inspection, targeted TERM, and exit verification INDEPENDENT
  current session; job control, state interpretation, and escalation GUIDED
- Demonstrate: distinguish executable/process, job ID/PID, background/stopped,
  and Running/S; inspect fresh identity and parent; terminate safely and verify.
- Evidence 2026-11-12: guided Ctrl-Z/bg/fg/Ctrl-C lab succeeded. Independent
  checkpoint inspected sleep 8759, sent TERM to verified job 1, checked jobs
  and ps, and correctly concluded no further action. Parent-name query initially
  omitted, then constructed after reminder; Bash verified after termination.
  Running versus S needed explanation again. Reasons to wait/inspect before
  KILL, including cleanup and zombies, were taught, not independently applied.
- Latest 2026-11-12 continuation: supplied pgrep/ps commands discovered timer
  9290 and parent 8171. Independently constructed ps -p 8171 -o pid,comm and
  verified bash. Running-versus-S quiz incorrectly selected continuous CPU
  execution; distinction retaught, no independent corrected retrieval yet.
- Next: after spacing, inspect/control a fresh disposable process with complete
  parent evidence. Recheck state interpretation and justified escalation; no
  immediate repeat of the successful TERM lab. All recorded IDs are historical.
- Quiz checkpoint 2026-11-12 continuation: 2 questions, 0 correct, 2 incorrect,
  0 I-don't-know selections. Topics: incomplete du totals and Running versus S.
  Both remain scheduled for review; detailed responses are in the session record.

## Package records, command lookup, and catalog freshness

- Stage: lifecycle GUIDED; installed/candidate tool choice and brief catalog
  freshness explanation INDEPENDENT on 2026-11-12
- Demonstrate: distinguish command resolution, installed package ownership,
  installed version, and APT candidate; explain local catalog versus remote
  repository and catalog refresh versus software upgrade.
- Last evidence: 2026-11-11, inspected supplied package queries and completed
  simulation/install/verification for locate. Initially attributed live web
  fetching to apt-cache policy; corrected Candidate prediction after teaching.
  Initially chose command -v for a package installed/candidate check and needed
  the full apt-cache policy command. Later recalled policy with confirmation
  and command -v after a cue during post-install verification.
- 2026-11-12: independently recalled that a remote release need not appear
  without local refresh, and chose apt-cache policy for both upgraded packages.
  Completed guided mirror repair, refresh, scoped two-package upgrade, and
  locate remove/purge with verification. Interpreting dependencies, preview
  plans, phased rollout, and retained config was taught, not independently tested.
- Resumed 2026-11-12: tree plan independently retrieved lookup, policy, and
  simulation commands; real privileged installation command also constructed
  independently. Metadata retrieval and approval reasoning needed direct help;
  verification pair supplied after command/package distinction teaching.
  Actual installation verified tree 2.3.1-1 and /usr/bin/tree.
- Next: after spacing, interpret metadata/dependencies and all proposed actions,
  justify approval, and select complementary verification without hints. Later
  distinguish remove/purge and local records from available candidates.

## Configuration, runtime records, and actual process identity

- Stage: GUIDED
- Demonstrate: explain persistent configuration versus runtime state; distinguish
  a PID file's contents from kernel-assigned identity and predict what a reader
  of an incorrect record will do.
- Last evidence: 2026-11-11, correctly selected `/etc` and `/run` but guessed
  the latter by name. Supplied commands compared a PID record with `ps` and
  `/proc`. Thought editing the record changes the PID, then predicted a reader
  would use the actual PID despite edited contents. Corrected the distinction
  after explicit teaching.
- Next: after intervening material, use an unfamiliar stale-record scenario;
  do not infer independence from the final prompted sentence completion.

## Permission classes, directory modes, and ownership repair

- Stage: class selection, numeric derivation, and integrated ownership/mode
  repair INDEPENDENT; retention of integrated repair not yet established
- Demonstrate: select exactly one owner/group/other class, reason about directory
  `r/w/x`, derive numeric modes, set both mode and group ownership, and audit all
  requested fields without reminders.
- Why: learner thought group write grants an owner write access when owner
  write is absent. On 2026-11-10, opening retrieval corrected this independently.
  Directory read/search predictions were independently correct; directory write
  versus removal initially needed correction.
- Last evidence: independently derived `750`, `750`, `640` in the integrated
  checkpoint. Initial plan omitted group `users`; first repair repeated the
  directory target and left the file group wrong. After prompts, final listing
  and content check proved the complete requested state.
- 2026-11-11: independently planned and verified modes 710/770/660 and group
  users on all three objects in a fresh workspace. Preserved user ownership
  and content; no repair or evidence prompts were needed.
- Next review: after several sessions, embed an access diagnosis in a different
  task to test retention; do not repeat another isolated repair immediately.

## `umask` derivation and process scope

- Stage: GUIDED
- Demonstrate: derive file/directory results for an unfamiliar mask as removed
  bits, explain why normal files do not gain execute, and distinguish a child
  shell's temporary mask from the interactive shell's state.
- Last evidence: 2026-11-10, reconstructed `027` file mode `640`; corrected the
  directory from missing group search to `750`, then verified both in a child
  shell. Needed direct teaching for unchanged parent `0002` and a hint to use
  `umask 0002` rather than `chmod` for restoration.
- Next review: after other material, derive a different mask and use a guarded
  child-shell creation experiment without a supplied result.
- 2026-11-11: for `022`, first predicted file `444` (removed owner write too)
  and directory `744` (removed group/other execute too). Hints led to `644`
  and `755`; a supplied subshell experiment verified both. Correctly answered
  that only the subshell mask changes after same-session scope teaching.
  Later test bit preservation and scope without preceding explanation.

## Pathname boundaries through find and xargs

- Stage: INDEPENDENT immediate integrated construction after teaching
- Demonstrate: select matching files and preserve each complete pathname when
  passing it as an argument; explain the roles of `-print0` and `-0`.
- Why: initially predicted default xargs would preserve a pathname containing
  a space. Observation showed two arguments; supplied null-delimited repair
  restored one argument.
- Last evidence: 2026-11-09, independently constructed a depth-2 regular `.log`
  search piped through `-print0 | xargs -0 printf '<%s>\n'`; verified three
  intact arguments including `access log.log` and exclusion of a depth-3 file.
- Next review: after spacing, use unfamiliar harmless argument processing with
  filenames containing spaces; assess retention before adding destructive actions.

## Find starting path and combined filters

- Stage: GUIDED on 2026-11-12 spaced review; earlier same-session independent
  construction did not establish retention
- Demonstrate: choose the requested search root, constrain depth, and combine
  a file-type test with a quoted name pattern without procedural hints.
- Why: first construction used `/home` instead of the user's home and omitted
  hidden-name filtering, despite correct supplied-command predictions.
- Last evidence: 2026-11-09, after repairing the home-directory task with hints,
  independently constructed `find "$find_lab" -maxdepth 2 -type f -name '*.log'`
  and an unlimited-depth variant. Verified two versus three matches and correctly
  predicted inclusion of `app/archive/old.log` in the unrestricted search.
- 2026-11-12: full transcript showed patterns placed in quoted starting paths,
  regex-like ^, nested literal quotes, and full paths passed to -name. Eventually
  separated home root and basename pattern, but omitted depth/type and literal
  dot until hinted. Final command/output correct; --help/man consulted.
- Next review: after other material, separate search root from basename filter
  in a fresh read-only task, then integrate depth/type without supplied options.
  Also distinguish live find traversal from locate's indexed results.

## Parent and child working directories

- Stage: GUIDED after correction
- Demonstrate: predict inherited working directories and explain why a child's
  directory change does not change its parent's; connect this to builtin `cd`.
- Why: learner predicted builtin and external pwd would report different paths
  after the parent shell changed directory.
- Last evidence: 2026-11-09, both pwd forms printed `/tmp`; after explanation,
  ran `bash -c 'cd /tmp; pwd'` from home and verified the child printed `/tmp`
  while the subsequent parent `pwd` printed `/home/raf_0411`.
- 2026-11-10 update: a child changed its own umask to `027` while the interactive
  shell remained `0002`; the learner did not independently connect this to
  process isolation until it was explained.
- Next review: use a different short subprocess scenario and ask what state is
  inherited versus what the child can change in the parent.

## PATH lookup and command types

- Stage: GUIDED after correction
- Demonstrate: use shell inspection to distinguish aliases, builtins, and
  executable paths; predict a fresh executable lookup through an unfamiliar
  ordered PATH, skipping missing candidates and stopping at the first match.
- Why: learner initially prioritized `/usr/bin` over `/usr/local/bin` despite
  PATH order, then thought lookup stopped at the first missing candidate.
- Last evidence: 2026-11-10, initially expected `command -v cd` to print
  nothing; actual comparison established builtin-aware shell resolution versus
  `which` and `whereis`. Independently chose `type -a backup` when every alias,
  function, builtin, or executable definition was requested. PATH directory
  ordering itself was not retested. `locate` was unavailable with status 1.
- Next review: after intervening material, use a small disposable executable
  lookup experiment for PATH ordering; integrate `type -a` only if ambiguity is
  present. Revisit `locate` during package management rather than installing now.

## Spaced follow-up — Phase 6 text selection and frequency reports

### grep selection and basic regular expressions

- Stage: GUIDED with independent immediate anchor construction
- Demonstrate: on unfamiliar text, select requested lines using case handling,
  `^` or `$`, and line-number or count output; distinguish no match (status 1)
  from command failure; quote patterns so grep receives regular-expression
  syntax
- Why: literal matching and anchors succeeded, but exact `-n` formatting and
  `-c` meaning required correction; the integrated search first omitted the
  required start anchor
- Last evidence: 2026-11-08, independently built and verified
  `grep -n 'started$' messages.txt`; later repaired `grep -i '^backup'` and
  verified its file copy and terminal count
- Next review: after spacing, use a different fixture and require one exact
  prediction plus execution; avoid repeating today's examples
- 2026-11-09 update: `^PASS` incorrectly admitted `PASSIVE`. After a field-boundary
  hint, learner constructed `^PASS,` and verified the correction. Include exact
  field matching in the next spaced selection task.

### sort, uniq, cut, and tr report pipeline

- Stage: GUIDED across two unfamiliar reports
- Demonstrate: independently identify the field to extract, normalize it,
  group identical values, count groups, rank numerically, and verify the report
- Why: the first report omitted grouping sort. A spaced retrieval then separated
  `grep -c` from the pipeline and reopened the full input with `cut`. A later
  checkpoint placed `tr` after `uniq -c`, so mixed-case values were counted as
  separate groups. The first repair explanation also assigned numeric ranking
  to `uniq -c` before being corrected.
- Last evidence: 2026-11-08, after a focused ordering hint, produced and
  verified `3 api`, `2 web`, `1 db`. Correctly explained that the first `sort`
  makes equal values adjacent, `uniq -c` counts those runs, and `sort -nr`
  ranks the counts. A tutor-created padding mismatch in the expected file was
  diagnosed by byte evidence and corrected; the learner report then diffed
  equal with status 0.
- Next review: after spacing, reconstruct
  one report from unfamiliar data with no supplied pipeline or stage-order hint.
  Keep evidence capture minimal and do not reuse either 2026-11-08 fixture.
- 2026-11-09 update: manual task complete. Fresh report correctly reconstructed
  normalization before grouping, counting, ranking, and file verification with
  no stage-order hint. Selection required one boundary correction; final report
  verified as 4 cache, 3 queue, 1 search. Next independent report should follow
  other material, with no immediate repeat of this fixture.

### `paste`, `diff`, `join`, `xargs`, `sed`, and `awk`

- Stage: GUIDED first applications; immediate `diff` status capture is
  INDEPENDENT in the current learning period
- Demonstrate: choose among position-based pairing, key-based joining, file
  comparison, stdin-to-argument conversion, stream substitution, and
  field-based filtering or aggregation in unfamiliar small tasks
- Why: supplied syntax was used for the first applications. `sed` global
  construction succeeded independently after the new flag was introduced, but
  source verification needed one reminder. The first `awk` explanation needed
  refinement that its action runs only for matching records. Default `xargs`
  whitespace splitting needed renewed correction on a pathname in Phase 7;
  null-delimited integration now has a separate review item above.
- Last evidence: 2026-11-08, exact predictions and executions for default and
  custom-delimiter `paste`, unified `diff`, inner and unmatched-row `join`,
  default `xargs` splitting, `sed` first/global substitution, and `awk` filtering
  plus `END` aggregation. Captured `diff` statuses 1 and 0 immediately and
  verified both saved results.
- Next review: integrate these tools naturally in later tasks rather than quiz
  all at once. Null-delimited `find -print0 | xargs -0` was taught on 2026-11-09;
  use its dedicated item for later retrieval.

## Phase 5 follow-up after curriculum progression

Phase 5 completed for curriculum progression on 2026-11-08. The main shell
mechanics are sufficient to begin text searching, while the items below remain
scheduled for spaced retrieval. Do not reopen the old November 5 repair
worksheet or repeat long evidence audits.

- Combined stdin/stdout file redirection — INDEPENDENT on 2026-11-07 after
  teaching and correction. Independently built and verified
  `wc -l < greeting.txt > saved-count.txt`. After spacing, test a different
  input-processing task and require prediction of terminal and file results.
- Single-pipe routing with final output redirection — GUIDED execution, correct
  independent prediction for supplied syntax on 2026-11-07. Later require
  construction without a supplied pipeline before changing the stage.
- Separate stdout/stderr destinations — RETAINED on 2026-11-10. After spacing,
  correctly predicted that `> /dev/null` leaves a missing-path diagnostic on
  stderr while `2> /dev/null` discards it; both `ls` failures retained status 2.
  No immediate isolated review is needed; integrate the distinction later.
- Merged capture-and-count pipeline — GUIDED completion on 2026-11-07.
  Corrected omission of `tee`, extra filename after `2>&1`, and stdout/file-copy
  confusion using a partial structure. Execution and both-file verification
  were complete and the comparison was accurate. After spacing, require an
  unfamiliar construction without a supplied structure, including explanation
  of `tee` stdout and verification of every destination.
- Exit status and `&&`/`||`/`;` — INDEPENDENT immediate construction on
  2026-11-07. After spacing, require a novel safe sequence where a second step
  must depend on actual command success and a final report must always run.
  Include retrieval of `$?` immediately after a command.
  On 2026-11-08, independently constructed and executed both success and
  failure branches plus an unconditional final report. Initially expected `$?`
  after the whole line to preserve the earlier failed `test` and then used
  `$1` while repairing the check. After one conceptual hint, captured the test
  immediately and observed status 1. Later the same day, independently captured
  `diff` status 1 for different files and status 0 for identical files before
  any intervening command. Immediate capture is INDEPENDENT in the current
  learning period; later spacing will test retention. Conditional sequencing
  itself has spaced independent evidence.
- Variables, quoting, and expansion — GUIDED after immediate predictions and
  correction on 2026-11-07. Recheck escaped `$`, quoted/unquoted pathname
  expansion, shell versus exported variables, and command substitution in a
  fresh practical task. Require an immediate `$?` check when a silent failure
  is part of the evidence.
  On 2026-11-08, a fresh line-count task still required correction from a
  single-quoted variable and filename operand to `< "$source_file"`, plus a
  separate correction to use semicolons on one physical line. The final command
  and output were correct. Recheck later with a different practical purpose.
- Alias resolution and immediate status capture — GUIDED on 2026-11-07. Alias
  creation, inspection, use, and removal succeeded. History proved a typoed
  intermediate `printf` replaced status 1 with 0 before the corrected check.
  On later review, capture status before any intervening command and use history
  to audit the actual command sequence rather than reconstructing it.
- Phase 5 combined transfer — GUIDED checkpoint completion on 2026-11-07.
  Correct final routes and artifacts required direct channel-model teaching,
  repair of an unset variable, syntax hints for later steps, and tutor closure
  of the final audit. Next test should be short and unfamiliar after spacing:
  one pipeline, two destination predictions, and minimal verification. Avoid a
  long audit worksheet; measure routing understanding rather than transcription.
  On 2026-11-08, independently constructed the full portable
  `grep | tee | wc -l` routing structure in a new text-search context and
  verified both destinations. A focused correction was needed for the grep
  start anchor, not the stream route. Recheck after spacing before changing the
  combined-routing mastery stage.

## Local documentation and required option arguments

- Stage: INDEPENDENT on the 2026-11-09 `join` manual task
- Demonstrate: use installed documentation for a different unfamiliar command,
  copy the complete option syntax, distinguish a standalone flag from a required
  option argument, construct the exact command, execute it, and verify the
  requested output without hints
- Why: the Phase 4 checkpoint omitted `file -b`; a second transfer omitted the
  required count for `head -c`; a 2026-11-03 attempt chose `touch -d` even
  though its copied description changed both timestamps
- Last evidence: 2026-11-09, independently extracted `-t char` from `man join`,
  identified both syntax roles, supplied a comma, and correctly predicted and
  verified the joined output in `labs/2026-11-08-join-docs-transfer.md`.
- 2026-11-12: independently recovered and ran `tree /usr/local -L 2`, with
  output meeting the requested depth. Fuller transcript showed repeated wrong
  --filelimit choices and missing/malformed arguments before independent manual
  recovery to -L 2 and comparison against unrestricted output. Required-option
  documentation application is RETAINED as self-correcting performance, not
  first-try fluency. Later integrate semantic option selection and result checks.

## Complete evidence capture and self-audit

- Stage: INDEPENDENT in the 2026-11-11 permission lab; broader consistency
  and retention still need review
- Demonstrate: inspect and record pre-state before modification, capture the
  exact command plus requested output/prompt evidence, and independently audit
  whether every material claim is supported before declaring completion
- Why: several 2026-11-02 worksheets initially recorded only commands or output;
  the live-follow transcript omitted `^C`/prompt, and the integrated checkpoint
  omitted the original configuration output before editing
- Last evidence: 2026-11-03 timestamp attempts reused a stale baseline, omitted
  exact commands, used bare `touch` as supposed content evidence, and declared
  success despite unequal access times. After direct comparison, correctly
  changed the verbal conclusion to failure. On 2026-11-04, the first stream lab
  left the execution section blank, put the pipeline under verification, omitted
  the requested verification commands, and marked an unrecorded returned prompt
  as recorded. After correction, later terminal experiments captured commands,
  visible output, and returned prompts coherently. On 2026-11-05, the multi-stage
  checkpoint recorded only `no output`, omitted the command and returned prompt,
  and inaccurately checked the corresponding self-audit item. The separate
  verification commands did prove both stored results, but the learner could
  not yet identify that proof independently during repair. On 2026-11-10, a
  sudo/chown worksheet first recorded a baseline already at the target state;
  a prompted rerun produced valid before/change/restore evidence. The integrated
  permission checkpoint's own listing showed the file group still wrong after a
  duplicated target, but another prompt was needed before repairing it.
- 2026-11-11: complete baseline, ordered repair transcript, final metadata and
  content verification, and correct completion judgment supplied without hints
  in the shared-workspace lab.
- 2026-11-12: repository repair succeeded, but the supplied pre-edit backup
  command/output was absent from the fuller transcript; backup remains unverified.
  Actual source used HTTP rather than suggested HTTPS. Do not equate successful
  refresh with proof that every requested safety step was performed.
- Next review: test consistent self-audit in a later different practical task,
  including a verified pre-change backup and recognition of a real mismatch.

## Standard streams, merging, redirection order, and `tee`

- Stage: separate stdout/stderr routing RETAINED; merged multi-stage routing
  with `tee` remains GUIDED
- Demonstrate: independently route stdin, stdout, and stderr through an
  unfamiliar multi-stage command using `2>&1`, pipes, `tee`, and final output
  redirection; apply redirections left to right and verify every destination
- Why: the learner now handles a normal `cat | wc` route after a refresher and
  practically verified both `2>&1` redirection orderings. However, the first
  ordering prediction put stderr in the wrong destination, `tee -a` was expected
  to redisplay old contents, and a later merged `tee` prediction again omitted
  the diagnostic until `2>&1` was highlighted.
- Last evidence: 2026-11-04, correctly observed six lines through
  `cat ... 2>&1 | wc -l`; verified that `> file 2>&1` stored both streams while
  `2>&1 > file` kept stderr on the terminal; used `tee` and `tee -a`; and, after
  correction, verified a six-line merged stream in both terminal output and a
  capture file. On 2026-11-05, predicted five of six outcomes in a two-pipe
  checkpoint, including the exact capture and count, but expected `tee` stdout
  on the terminal and could not reconstruct the second pipe as connecting
  `tee` stdout to `wc` stdin. A worked example was supplied after the learner
  requested one. On 2026-11-10, independently retrieved separate stdout/stderr
  routing with `/dev/null`; this does not establish merged or `tee` routing.
- Next review: use one short unfamiliar merged `tee` pipeline with two output
  destinations; do not reopen the old November 5 repair worksheet.

## Pager temporary state versus stored file

- Stage: practical `less` use INDEPENDENT; causal explanation GUIDED
- Demonstrate: without hints, distinguish displayed line range, search term,
  and selected match from stored file content, and explain what disappears when
  `less` exits
- Why: navigation and exact searches succeeded, but the learner twice could not
  name the temporary viewer state
- Last evidence: 2026-11-02 integrated checkpoint; tutor supplied the final
  explanation after the learner again answered `idk`
- Next review: after several sessions in an unfamiliar pager scenario; do not
  repeat immediately

## `tail -f` versus `tail -F`

- Stage: GUIDED after correction
- Demonstrate: independently choose continuous append following versus
  rotation-aware pathname following and explain the result using pathname and
  file identity
- Why: `-f` live observation succeeded, but the first `-F` explanation
  incorrectly focused on standard input and the exact rotation command needed
  a follow-up
- Last evidence: 2026-11-02, reconstructed `tail -F server.log` after a
  pathname/file-identity correction and observed a real append with `tail -f`
- Next review: later unfamiliar log scenario, not immediately

## Archive restoration evidence quality

- Stage: archive workflow INDEPENDENT; evidence capture GUIDED
- Demonstrate: record complete pre-state, safe member listing, extraction
  destination state, nested restored content, source preservation, and protected
  neighbors in an unfamiliar archive task
- Why: the 2026-11-01 archive checkpoint outcome was correct, but initial source
  output and nested post-extraction evidence were omitted
- Last evidence: tutor comparisons proved byte equality and neighbor safety;
  learner-recorded evidence remained incomplete
- Next review: in a later archive task after substantial spacing

## Hard-link identity and link count

- Stage: GUIDED after successful conceptual correction
- Demonstrate: distinguish shared file identity from a stored target pathname;
  count every hard-linked name, including the first; explain changes and
  removals using actual inode and content evidence
- Why: predictions and execution succeeded, but the explanation claimed
  dependence on the original path and the initial link count excluded it
- Last evidence: 2026-10-31, shared writes and surviving-name access observed;
  corrected explanation used inode 48272923 to explain shared content and
  independence from the removed pathname
- Next review: after spacing, test independent diagnosis in a mixed
  copy/hard-link/symbolic-link scenario, including counting all hard-linked names

## Symbolic links: stored pathname versus reached data

- Stage: GUIDED after correction
- Demonstrate: explain what a symbolic link stores and predict its behavior
  after target editing, renaming, removal, and recreation without hints
- Why: initially described the stored value as target data and predicted that
  deleting the target would also delete the link
- Last evidence: 2026-10-31, completed the guided experiment; after correction,
  independently explained failure after target rename using the unchanged
  stored pathname
- Next review: after spacing, diagnose a dangling link in an unfamiliar fixture

### Relative targets and nested parent traversal

- 2026-10-31: the relative-link lab revealed renewed confusion between stored
  pathname and reached data, plus dependence on the shell's current directory.
- Later evidence: after guided side-by-side comparison, independently wrote
  and executed `cat ../../data/note.txt` from `links/deeper`, confirming correct
  two-parent traversal. This checks ordinary relative paths, not independent
  selection of the symbolic link's directory as a lookup base.
- 2026-11-01 spaced evidence: from a different shell working directory, first
  skipped `links/`, then treated one `..` as reaching the project-level `linux/`
  directory. Required incremental hints before producing the exact sought path
  from the link's containing directory. Stage remains GUIDED.
- Next: after several sessions, use one brief unfamiliar dangling-link diagnosis
  without hints. Do not repeat immediately.

## Current/parent relative navigation

- Stage: INDEPENDENT after correction
- Demonstrate: use `.`, `..`, and a compound relative path correctly in an
  unfamiliar directory tree without being told which form to use
- Why: the initial `.`/`..` model was incorrect before the navigation lab
- Last evidence: 2026-10-31, nested parent traversal initially failed; after
  correction, independently wrote and ran `cat ../../data/note.txt` from two
  levels below the lab root. Earlier five-step navigation succeeded on 2026-10-27.
- Next review: after spacing, construct a relative path across an unfamiliar
  directory tree without a supplied route

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

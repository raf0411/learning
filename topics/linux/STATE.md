# Learner State

## Current checkpoint — 2026-11-26 (session complete)

- **Curriculum position:** Phase 12 capstone. No milestones closed; completion is unchanged at 6/12.
- **Built:**
  - Service section: optional 2nd positional argument; `systemctl is-active` with a status-4 → `not found` branch; `journalctl` guard nested in the exists branch;
  - fixed two test-runner flag bugs (case 9 had no `failed=1`; case 8 set it in the PASS branch);
  - tests 11/11, status 0 (cases 10–11 tutor-supplied, both mutation-proven).
- **Stages:**
  - Runner exit-status diagnosis: INDEPENDENT for the missing flag; GUIDED for the PASS-branch flag.
  - Required vs optional: GUIDED (3rd time). Confused the journal with the supplied sample log.
  - Local docs: INDEPENDENT (found `man systemctl` EXIT STATUS, 3 vs 4).
  - Pipeline status = last command: correct on 2-day retrieval.
  - Branch placement/nesting: GUIDED (chose the wrong branch, then placed the block outside it).
  - Silencing `command -v`: **repeated** the 11-25 bug; recognized only via that reference.
  - Prediction: skipped when bundled; correct and complete when it was the single step.
  - Self-audit: weak. Bugged output was pasted without comment twice, and the worksheet self-audit was declined.
- **New concepts taught:**
  - misleading output is worse than none (a typo reported as a stopped service);
  - `journalctl` exits 0 for an unknown unit;
  - `$?` right after `x=$(cmd)` holds cmd's status;
  - check "was it requested" before "can I produce it";
  - `!` in front of a pipeline flips its status.
- **Work pattern:** asking for one specific `grep` output works better than "show me the code". Mutations make bugs visible that word explanations didn't (line 74).
- **Next:** network section (`ip`, `ss`). Detail: `sessions/2026-11-26.md`.

## Previous checkpoint — 2026-11-25 (session complete)

- **Curriculum position:** Phase 12 capstone. No milestones closed; completion is unchanged at 6/12.
- **Built:**
  - Memory line (`free -h` → awk `$7`/`$2`) and top processes (`ps -eo pid,comm,%cpu --sort=-%cpu | head -n 4`), each with its own optional guard;
  - Load-guard bug fixed (an unsilenced `command -v sed '<expr>'` printed `/usr/bin/sed`);
  - `<>` brackets removed;
  - tests 9/9 (cases 8 and 9 tutor-supplied, both mutation-proven).
- **Stages:**
  - Mutation testing: designed own mutation (`nofree`) for the 3rd time. Still needs a prompt to perform it.
  - Immediate `$?` capture after a run: correct, unprompted.
  - Separate guards for independent optional tools: GUIDED (merged with `&&` first, then the quiz prediction was correct and the split was correct).
  - Required vs optional: GUIDED (said `ps` is required because it is "always available"; the design rule and `dpkg -S` evidence fixed it).
  - Self-audit: **weaker today**. A stray output line and a wrong label went unnoticed across several pastes.
- **New misconceptions taught:**
  - `command -v` takes the command's usage arguments (it takes names only);
  - awk counts spaces as fields (default splitting collapses whitespace; the `Mem:` label shifts the fields);
  - a test with `else PASS` was not recognized as unable to fail.
- **Work pattern:**
  - The learner pastes code asking "like this?" instead of running it. Ask for run output.
  - The learner copies template placeholders literally (`$?`). Use non-syntax placeholders like `<N>`.
- **Next:** verify the `nops` revert, then the service + journal section. Detail: `sessions/2026-11-25.md`.

## Previous checkpoint — 2026-11-24 (session complete)

- **Curriculum position:** Phase 12 capstone. No milestones closed; completion is unchanged at 6/12.
- **Built:**
  - the required-dependency check (exit 3), plus test case 7, which the tutor supplied; the suite is 7/7;
  - optional Host/Load/Disk lines that print `unavailable`, with mutations verified.
  - The memory line was given but not attempted.
- **Pace agreement (the learner's request):** finish a presentable portfolio sooner.
  - The tutor hands over routine code (tests, guards, printf).
  - New tools get one quick question; there are no predict-then-run detours unless something breaks.
  - The learner must be able to explain every line.
  - Milestones close only on independent work.
- **Stages:**
  - `>&2`: written correctly once in production (upgraded from recognition only).
  - `!` spacing: correct today, with no slip.
  - Mutation habit: used unprompted for the second time (a fake `nos` command), along with debug-printing a variable.
  - `if` branching on any command's exit status: GUIDED (polarity was inverted once and fixed after a trace).
  - `bash -n`: introduced and used to find a missing `fi`/`done`.
  - Self-audit: **improved**. A single "does every line match?" question was enough; no side-by-side was needed.
  - available vs free memory: **retained** (correct after 10 days).
  - du vs df: **still unreliable**. This was the 3rd date, now in the reverse direction (chose `df` to find which directory is big).
- **New misconceptions taught:**
  - pipeline status is the last command's status (`command -v x | sed` is almost always true);
  - PATH lookup: the learner thought a command is found anywhere on disk, or that the interactive alias is what scripts see;
  - Bash arrays: commas become part of the elements, and `"$arr"` gives only the first element.
- **Next:** confirm `nouptime` was reverted and the `<>` brackets were removed, then the memory line. Detail: `sessions/2026-11-24.md`.

## Previous checkpoint — 2026-11-23 (session complete)

- **Curriculum position:** Phase 12 capstone. No milestones closed; completion is unchanged at 6/12.
- **Built:**
  - the System section (Host, Load, Disk /);
  - test 6, which works out its expected value at run time and is proven by a mutation test;
  - a Load-spacing fix and a `Failed logins:` heading.
  - Step 7b (the required-dependency check) is designed but unattempted.
- **Stages:**
  - Output tests that can fail: **INDEPENDENT** this session. Case 6 was written without a model block; it runs the program, narrows to the target line and has correct polarity.
  - Computed expected value versus hard-coded literal: corrected (the quiz chose the literal), then constructed independently.
  - Mutation testing: proposed **unprompted**, predicted correctly and executed correctly.
  - Field extraction (`awk '{print $n}'`, sed text anchor): independent once the tool family is named. The learner asks for the tool rather than guessing.
  - `du` versus `df`: **recurring confusion** (11-22 §3, 11-23 build). Corrected with an explanation and a hint.
  - `-f` meaning: recall correct. Spacing was too short to count as retained.
  - Required versus optional dependencies, and degrading gracefully: GUIDED. The learner's first instinct was to stop on any missing command.
  - `command -v` (status 0/1, a builtin) versus `which`: taught and observed.
- **Still weak:** self-audit. The report showed a wrong Disk line under 5/5 passing tests and the learner didn't notice; a side-by-side was needed.
- **Learning style:** unchanged. Single questions and quizzes always get answered; bundled requests get partial replies.
- **Next:** step 7b. Detailed evidence: `sessions/2026-11-23.md`.

## Previous checkpoint — 2026-11-22 continuation (session complete)

- **Curriculum position:** Phase 12 capstone. No milestones closed; completion is unchanged at 6/12.
- **Built:** failed-logins section; fixture `samples/auth-mixed.log`; a 5th test that checks **output**, proven by a mutation test.
- **Stages:**
  - `>2` / `2>` / `>&2`: recognition correct on 2 quizzes; `>>` was written correctly. The regression looks repaired, but `2>` and `>&2` haven't been written yet. Retest by production after spacing.
  - Count/frequency pipeline (`grep | awk '{print $NF}' | sort | uniq -c | sort -nr`): INDEPENDENT construction on known sample data. This is evidence toward the Phase 6 milestone, which stays open until it's done on unfamiliar data.
  - False-positive reasoning: predicted the leak correctly; first fix independent, final pattern tightened on request.
  - Output tests (`cmd | grep -q`, polarity): GUIDED. First attempt tested the fixture instead of the program; the pipe, the `bin/` path and the polarity each needed one cue.
  - Mutation testing: performed correctly by the learner, with correct interpretation.
- **Misconception found:** checking the test *input* instead of the program's output (a test that can't fail).
- **Learning style:**
  - Asked the tutor to stop chasing minor discrepancies once a result is verified correct.
  - Single direct questions always got answered.
- **Next:** system section (Host, Load, Disk /). Detailed evidence: `sessions/2026-11-22.md` (continuation).

## Earlier checkpoint — 2026-11-22 (first session, complete)

- **Curriculum position:** Phase 12, the capstone, is current. The real build has started on the VM at `~/Documents/sysprobe`. No milestones were closed; completion is unchanged at 6/12.
- **Career direction:** entry-level or junior roles (support, NOC, junior sysadmin, cloud support) as a route to DevOps.
- **Built today:**
  - an input guard (`-z`; `! [ -f ] || ! [ -r ]` → stderr, exit 2);
  - an ERROR-count section;
  - `tests/run-tests.sh` with 4 automated cases, PASS/FAIL output and an exit flag;
  - a mutation test that confirmed the tests catch the `![` bug.
- **Stages:**
  - Combined-test polarity: INDEPENDENT on construction today.
  - `!` spacing: recurring slip (third date).
  - `-f` (regular file) versus `-e` (exists): corrected; retest later.
  - Guard-first structure (no `else`/`exit` on the success path): GUIDED.
  - Test-runner construction: GUIDED. One model block was given; the rest was built independently.
  - Guard ordering (which guard an input reaches): GUIDED.
  - Exit codes 126 versus 127: introduced.
- **Misconception found:** `>2` was believed to redirect to stderr; it actually writes stdout to a file named `2`. This is a Phase 5 regression. `2>dev/null` (missing slash) was a slip.
- **Spec and self-audit:** still weak.
  - The learner missed an output mismatch against the spec.
  - The learner believed tests can't be planned before the code exists.
  - The learner couldn't apply the row-audit method from a description. Explicit side-by-sides worked.
- **Design concepts:** safety rules versus input validation are now distinguished. The exit policy is 1 = the tool found a problem, 2 = user error. Report questions about the whole file are only partly formed.
- **Learning-style evidence:**
  - Paper design tables reduced motivation; building with inline design questions worked.
  - Needs explicit, unambiguous instructions.
  - Skips predictions that are requested as comments or bundled into multi-part instructions, but answers direct single questions and quizzes.
- **Next:** Build step 6 (failed-logins section). Detailed evidence: `sessions/2026-11-22.md`.

## Previous checkpoint — 2026-11-21 continuation (session complete)

- **Curriculum position:** Phase 12 capstone is now current, by learner choice. Phases 6, 8, 9, 10, and 11 are still open milestones; none were marked complete without evidence. Each closes when the matching capstone part is done independently.
- **Target environments:** build and run failure tests on the Ubuntu VM. Do the real read-only run on the learner's homelab: an old laptop running Ubuntu with Docker (Navidrome, File Browser), reached by SSH over Tailscale.
- **No new skill evidence.** The polarity opener was skipped and the kickoff worksheet is unattempted. All stages below are unchanged.
- **Next:** `labs/2026-11-21-capstone-kickoff.md`, design spec and predicted tests before any code. Detailed evidence is in the continuation section of `sessions/2026-11-21.md`.

## Earlier checkpoint — 2026-11-21 (first session)

- **Parameterized list checker:** functionally complete. Final runs gave A 0, B 1, C 2, D 2, E 2, and `/dev/null` 2. Overall GUIDED.
- **Task-model misconception:** the first attempt treated the argument as the pathname to check, reusing the 11-16 design. A diagnostic quiz confirmed this. It was corrected by a diagram and then applied correctly, but not yet retested.
- **Line loop from `"$1"`, function, and flag:** INDEPENDENT construction once the task model was clear.
- **Combining `[` tests:** GUIDED.
  - Proposed `-d`, too narrow.
  - Proposed `-fr`, which is invalid because test operators cannot be bundled.
  - Proposed `![`, which fails because `!` needs a space.
  - Branch polarity was inverted again; this is the second date with that mistake.
  - Reached `[ -r "$1" ] && [ -f "$1" ]` after hints. Readable versus regular-file reasoning (directories usually have `r`) was taught.
- **Self-audit and prediction:** weak.
  - Did not flag two failing results: status 1 for the all-regular test, and status 0 for a directory list.
  - Skipped the predictions table three times.
  - Replaced earlier worksheet evidence instead of appending.
  - Immediate `$?` capture remains reliable.
- **ELAPSED versus TIME:** retrieval failed at the opener. After reteaching, the own-words answer was mostly correct (TIME correct, ELAPSED imprecise); the tutor supplied the link that polling would grow TIME. Still GUIDED.
- **Next:**
  - The usage-text fix is unverified; it is minor.
  - Next session: a quick application on test combination and polarity.
  - Then a fresh, different reduced-scaffolding script task for the Phase 11 milestone, with predictions and self-audit required.
  - Detailed evidence: `sessions/2026-11-21.md`.

## Previous checkpoint — 2026-11-17 (session complete)

- Local-file loop/condition/failure flag — INDEPENDENT construction. Preserved spaced arguments, routed diagnostics, processed all paths, and returned remembered failure. Whole-script task remains GUIDED: omitted input guard, incomplete shebang, and missing test evidence needed hints.
- Input validation — GUIDED. Correct missing/empty-argument guard after hints; later inverted readability guard rejected good input and allowed missing-list failure to end in 0. Correct success/else repair verified mixed-list 1 and unavailable-list 2. Independent guard construction remains the edge.
- Functions — GUIDED, documentation-assisted. Valid reporting function with local argument and outer flag; later correctly refactored to test-only function used directly in an if. Failure-first/success-last run verified status 1 after a test-selection reminder. Function return versus stored variable correctly recognized with assignment-status rule supplied.
- Line input — GUIDED. Correct prediction and execution of supplied IFS=/read -r loop; integrated checker preserved spaced filename and remembered failure. Non-pipeline state persistence explained; independent scope reasoning untested.
- Verification — immediate status captures repeatedly correct; full scenario coverage and precise evidence still need reminders. Minor usage filename and unreadable-versus-missing wording fixes requested but unverified. Completed functional labs need no repetition.
- Process state (Running vs S) — improved to correct spaced recognition in a later same-day continuation: chose sleeping/kernel-wakeup over polling, T, and Z from STAT/ELAPSED/TIME evidence. Own-words explanation of ELAPSED vs TIME requested but not given; still GUIDED, not RETAINED.
- Next: labs/2026-11-17-list-checkpoint.md. Re-read at continuation closure: still unchanged, script and all tests TODO. Resume after fresh availability check; combine list argument, prechecks, function, line loop, and status policy without a supplied implementation. No active process cleanup pending. Detailed evidence: sessions/2026-11-17.md.

## Current checkpoint — 2026-11-16 (session complete)

- First Bash script — GUIDED completed. Saved and ran bounded web check; initial printf/command-substitution wrappers hid curl status. Guided repair restored direct commands and explicit HTTPS.
- Immediate status capture — INDEPENDENT command construction, repeatedly executed correctly. Multi-case test completeness needed a reminder; do not infer fully independent verification workflow.
- Arguments and empty-input guard — GUIDED. Used quoted "$1", ran supplied guard, verified normal status 0 and missing-input status 2.
- Conditional flow and failure handling — GUIDED. Initially treated false test as automatic exit, compared URL text numerically to zero, then checked $? after printf. Supplied child-shell experiments contrasted nonzero status with explicit exit; supplied final if-curl block verified success 0 and failure 1. Later grep branch/status recognition correct; independent construction still untested.
- Network evidence — correct spaced recognition of lookup scope. Explicit HTTPS still needed a repair reminder during script editing; do not mark full diagnostic independence.
- Direct execution — GUIDED completed. Correct shebang added; initially omitted execute permission, then used 774 instead of owner-only addition to 664. After component hints, constructed g-x and verified 764. Direct launch succeeded with HTTPS 200 and immediate status 0. Selective permission preservation remains weak in this application.
- Command-output capture and fixed-format printf — GUIDED pattern application complete without repair; hostname assignment and interpolated heading verified by execution.
- Argument loops — GUIDED. Initial scalar assignment and literal `for target in targets` produced one literal line. Supplied repair used `for target in "$@"`; actual two-line output preserved a spaced argument. Correct recognition that "$1" ignores extra arguments and exit inside a loop terminates the whole script; later loop/conditional composition succeeded, but complete independent workflow remains unverified.
- Multi-URL integration — GUIDED overall, correct loop/conditional composition without body repair. Initially used "$@" in unary -z guard, causing argument-count errors; restored "$1" after teaching. Usage text needed supplied correction; final two-target retest required repeated reminders, then actual chat output verified both HTTP 200 and status 0 with no guard errors. Malformed-first fail-fast behavior independently assembled and observed. Correct recognition that merely removing exit would let later success mask failure.
- Remembered failure status — GUIDED completed. Supplied flag pattern correctly kept mixed-run status 1 despite later success and all-success status 0. Initially also replaced guard exit 2 with an assignment, allowing later execution; restored after correction. Requested guard test omitted while network tests repeated; reminder led to actual usage-only/status 2 evidence. Assignment versus early exit and targeted verification still need independent application.
- Next: labs/2026-11-16-file-checkpoint.md re-read at closure and verified wholly unattempted. Construct local-path checker independently using supplied regular-file test primitive, prior control-flow skills, and three actual test cases before adding more syntax. Completed web-check labs need no repetition; some final evidence is in chat. No active lab-process cleanup pending. Detailed evidence: sessions/2026-11-16.md.

## Current checkpoint — 2026-11-15 (session complete)

- SCP download — GUIDED. Correct Mac context, forwarded port, and remote pathname; initially reversed operands and attempted a directory upload. After a source/destination hint, corrected the command and downloaded successfully.
- Two-sided SHA-256 verification — INDEPENDENT immediate construction. Used local shasum and SSH remote shasum, recorded matching digests, and correctly identified equality. Broader transfer workflow remains guided; retention untested.
- Evidence interpretation — initially called unperformed hash comparison a mismatch; corrected after feedback and actual verification. Source availability and pasted-border repair were guided.
- Shared RAM — correct spaced recognition that shared pages contribute to both processes' RES. Independent explanation/application remains untested; do not mark full retention from recognition alone.
- Socket inspection — GUIDED. Initially suggested nc, then ss -t; after tool/option-purpose hints constructed ss -tln. Mac nc probe succeeded with option hints. Authentication-failure recognition correct; hypothetical loopback-only listener incorrectly attributed failure to unequal forwarded ports. Binding/endpoint reasoning remains weak.
- Web diagnostics — independent getent/resolvectl/curl selection and recorded successful HEAD responses. Total-timeout semantics GUIDED: chose connect-timeout, then recovered max-time after a scope hint. Interpretation GUIDED: overclaimed name resolution proves website existence and HEAD 200 proves whole website works; corrected by tutor, not independently reconstructed.
- UDP — GUIDED practical lab complete. Adapted ss to -uln after option-purpose prompt; supplied nc loopback receiver/sender commands delivered a datagram and verified receiver exit. Correctly identified receiver output as arrival evidence; honestly did not know limits for future messages. After teaching, correctly recognized that local send success leaves remote arrival unknown. Immediate recognition only, not retention/transferable mastery.
- Integrated network diagnosis — tool selection and bounded curl command INDEPENDENT; interpretation GUIDED. Used full URLs in resolver commands and confused lookup failure with absent resolver. After hostname/control hints, correct getent comparison and revised name-specific conclusion; terminology and untested-stage reasoning still needed teaching. First revised resolvectl transcript has command/output inconsistency. Curl diagnostic code retrieved from manual, but immediate shell exit-status capture omitted.
- Bash entry — saved-command/script model introduced only. Correct recognition that an intervening successful printf replaces false's status in $?. Practical immediate capture still unverified today; no script written or run.
- Next: labs/2026-11-15-first-bash-script.md is verified wholly unattempted at closure. Resume first script and immediate status capture, with brief spaced networking retrieval if useful. Introductory networking coverage complete; independent milestone open. No repeat of completed labs and no UDP receiver cleanup pending. Detailed evidence: sessions/2026-11-15.md.

## Current checkpoint — 2026-11-14 (networking continuation complete)

- Networking diagnostics — GUIDED. Executed supplied interface/route/ping/resolver/HTTPS/listener commands and provided actual evidence. Correct recognition that ping does not prove web access and that reachable hosts may lack an SSH listener; independent tool selection/diagnosis untested.
- IP/software ports and host context — GUIDED. Initially confused TCP ports with cable sockets; later ran Mac-specific nc inside Ubuntu. Host-dependent loopback and NAT endpoint distinctions taught. Reverse-copy quiz still selected guest port 22 instead of Mac forwarded port 2222.
- Socket/process/service relationship — GUIDED. Supplied ss/systemctl inspection linked SSH listener to sshd and socket activation. Listener versus remote reachability/authentication was an honest knowledge gap; three-stage model taught, not independently retrieved.
- SSH and SCP — GUIDED. Reported saving localhost-only VirtualBox NAT forwarding, logged into Ubuntu from Mac, supplied remote identity/connection evidence, exited, then uploaded a file and verified identical two-sided SHA-256 hashes. All commands supplied; local hash needed a reminder. Public host fingerprint retrieved, but actual comparison at trust prompt not recorded. Path typo, pasted template, and physical-newline errors repaired with help.
- Shared physical RAM — GUIDED, unresolved. Latest quiz assumed RES summation automatically deduplicates shared pages. Per-process versus physical-block diagram retaught; no independent correction yet.
- Next: labs/2026-11-14-scp-download-checkpoint.md is prepared and wholly unattempted. Resume reduced-scaffolding download/verification after fresh availability checks; do not repeat guided upload. Forwarding rule remains configured as reported; practice files last verified in Mac/Ubuntu temporary directories. Detailed paths/evidence: sessions/2026-11-14.md. No independent networking milestone yet.

## Earlier checkpoint — 2026-11-14 (before networking continuation)

- Sleeping versus executing — correct spaced recognition from elapsed/CPU evidence. Independent causal reconstruction remains untested; earlier polling misconception not yet considered resolved.
- Resource interpretation — GUIDED. Correctly selected available RAM in a spaced capacity quiz. Actual top S/nonzero-CPU rows inspected; instantaneous state versus interval usage explained, not assessed.
- Resident/shared memory — GUIDED, active gap. Twice double-counted shared pages: added SHR to RES, then summed two RES totals containing the same shared block. Containment and physical-block diagrams taught; no independent correction yet.
- Signal escalation — independent signal selection and targeted execution for a supplied known TERM-ignoring fixture. Full workflow GUIDED: post-TERM wait not demonstrated, ps exit verification required a reminder, written justification relied only on persistence after TERM. Tutor supplied causal distinction. Empty jobs and header-only ps verified fixture exit; PID 5387 is historical, not a future target.
- Service status and bounded journal queries — INDEPENDENT immediate construction for dbus after guided cron work. Correct main PID identification. Definition retrieval/ExecStart extraction GUIDED; supplied systemctl cat after omission.
- Service interpretation — GUIDED. Enabled-versus-active recognition correct; static meaning taught after learner reported loaded instead. Activation-versus-task-success distinction needed teaching, followed by correct recognition. No independent written log inference yet. System cron/dbus investigations were read-only; disposable user-service control followed separately.
- User-service lifecycle — GUIDED completed creation, inspection, restart, stop, and transient-unit collection verification. Journal confirms final stop; no cleanup pending. User/system scope and stable unit name versus new process instance taught.
- User journal query — INDEPENDENT immediate construction after --user introduction: selected tutor-sleep.service, current boot, last 12 entries, no pager. Actual eight entries confirmed start/restart/stop despite unit no longer existing.
- Personal cron scheduling — GUIDED successful draft/precheck/install/list/log observation/remove/verify cycle. Correct fixed-minute quiz; clock-boundary timing needed explanation after initial absent log. Five one-minute-spaced timestamps observed. Personal crontab restored to absence; lab files retained, no recurring cleanup pending.
- Next: Phase 10 service/log/scheduling introductory work complete with guided control; networking not yet begun. Later independent lifecycle, scope/history interpretation, and schedule construction/safety. No immediate repeat of completed labs. Phase 9 remains open; later retrieve shared-memory accounting and causal escalation/wait/verification. Evidence: sessions/2026-11-14.md.

## Previous checkpoint — 2026-11-13 (session complete)

- Process and parent ps query construction — RETAINED in a spaced lab: independently inspected fresh timer and verified bash parent. Shell job-status evidence needed a reminder and supplied command; complete workflow remains GUIDED.
- Running versus S / elapsed versus CPU time — GUIDED, unresolved conceptual gap. Despite correct opening recognition, independently written answers still asserted CPU execution and waiting for signals. Two later quizzes selected continuous polling, including after time sleep 5 showed 5.005s elapsed versus 0.004s CPU. Contrasting busy-loop experiment showed 2.794s elapsed versus 2.777s CPU; taught interpretation not independently retrieved afterward.
- Resource interpretation — GUIDED. Completed top inspection; VIRT/RES/SHR explained, not independently assessed. free -h showed 1.1Gi available and 0B swap at inspection. Incorrectly treated unused disk as automatic swap; corrected demand-risk scenario succeeded immediately after teaching.
- Permission-limited du interpretation — correct spaced recognition of incomplete total. Both unprivileged (five errors) and privileged (no errors) /var/log inspections displayed 175M; rounding/completeness explained.
- TERM follow-up — correct recognition of bounded cleanup wait before renewed inspection. Supplied TERM and verification commands confirmed timer exit; practical escalation remains untested. PID 4946 and parent 4582 are historical only.
- Signal-handling experiments — GUIDED. Observed delayed cleanup after TERM, then a separate known TERM-ignoring disposable job requiring supplied KILL. Verified both exits with jobs/ps. Newline-split ps option repaired. No independent escalation decision yet; PIDs 5237/5348 are historical.
- Integrated process workflow — INDEPENDENT in later checkpoint: complete job/process/parent evidence, fresh identity check, targeted TERM, and dual exit verification for timer 5442. No further signal correctly justified; initial Yes was inconsistent wording repaired to No. Timer exited.
- Integrated RAM assessment — GUIDED: chose free -h independently and rejected automatic disk-to-swap use, but selected free instead of available and needed physical-damage wording corrected. Revised comparison used 1.0Gi available against 2Gi additional demand correctly after guidance.
- top state versus %CPU — introduced only: momentary state versus CPU use over an update interval. No assessment; establish sleeping-versus-executing understanding before building further on this.
- Next session: one brief retrieval of alive-versus-executing using the contrasting timing experiments, then adapt. Current practical process work is sufficient; interpretation remains weak. Completed labs should not be restarted. All practice jobs exited; no cleanup action pending. Detailed evidence: sessions/2026-11-13.md.

## Current checkpoint — 2026-11-12 (latest continuation complete)

- Resource interpretation — GUIDED. Chose available rather than free RAM but
  explicitly could not identify needed workload-demand evidence. Load/sample-window
  reasoning required teaching. Actual VM available RAM 558Mi, swap 0B at inspection;
  this is a historical snapshot, not current guaranteed capacity.
- Directory usage command — INDEPENDENT construction of du -sh /var/log.
  Permission-limited totals — GUIDED, unresolved misconception: after explanation,
  selected that du could count everything because only content reading is blocked.
  Directory traversal/metadata access versus file-content access needs retrieval.
- Process discovery — GUIDED execution of pgrep -a -x sleep and PID inspection.
  Parent-name query — INDEPENDENT immediate construction: adapted ps to verify
  recorded parent PID 8171 as bash without a supplied command.
- Running versus S — GUIDED, recurring misconception. Selected continuous CPU
  execution for a Running job despite S state; distinction retaught, not yet
  independently retrieved. Two quizzes in this continuation: both incorrect.
- Next: unattempted top -o %MEM inspection, capturing headings and first five
  process rows after two refreshes. RES/%MEM/VIRT introduced only. Do not restart
  the completed resource worksheet. Timer 9290 exit was not observed; old IDs
  are historical, never targets for action without fresh verification.

## Earlier checkpoint — 2026-11-12

- Tree package checkpoint — GUIDED overall. Independently selected shell lookup,
  installed/candidate queries, simulation, and later the privileged installation
  command. Metadata retrieval, dependency/approval reasoning, and complementary
  verification needed teaching. Installed tree 2.3.1-1 on Ubuntu; supplied checks
  verified Installed/Candidate 2.3.1-1 and resolution to /usr/bin/tree. Functional
  execution subsequently verified; full independent package milestone open.

- Bounded tree display/documentation — RETAINED required-option application:
  independently constructed and verified `tree /usr/local -L 2` after the earlier
  spaced join-manual success. Fuller transcript showed initial --filelimit/depth
  confusion and malformed/missing arguments, followed by independent manual
  recovery and output comparison. Successful self-correction, not first-try fluency.
- Package ownership lookup — GUIDED: initially selected status (-s), then found
  ownership search (-S) after a conceptual/manual hint and verified the owner.
  Catalog refresh versus installed upgrade independently explained again.
- Processes and jobs — GUIDED introduction. Program/process distinction needed
  teaching. Correctly predicted and reported foreground timer waiting; supplied
  background/jobs/ps commands verified shell-local job number, sleep PID, Bash
  parent, S state, and eventual Done. Subsequent checkpoint advanced practical
  inspection and normal termination as summarized below.
- Safe normal termination and PID inspection — INDEPENDENT current-session
  checkpoint. Inspected fresh sleep PID 8759, selected TERM by verified job ID,
  and verified exit with empty jobs/header-only ps; correctly declined further
  action. Initial parent-name evidence omitted; after reminder independently
  constructed a parent query verifying Bash. Full evidence completeness remains
  GUIDED in this checkpoint.
- Job control — GUIDED practical execution of Ctrl-Z, bg, fg, Ctrl-C; independently
  recalled stop-then-background sequence verbally. Running versus S and reasons
  not to escalate immediately required explanation; no KILL/escalation practice.
- Resource interpretation — GUIDED. Inspected uptime/nproc/top/free/df/du.
  Initially equated load 4 on two CPUs with guaranteed 100% CPU; corrected by
  teaching non-CPU contributions and time windows. Free/available distinction
  retrieved immediately, but “no need to worry” needed qualification by demand
  and trends. RAM/disk separation recognized; available disk terminology corrected.
- Directory disk-usage construction — INDEPENDENT immediate transfer. Selected
  du -sh for the home directory and executed du -sh ~, recording 16M. Resource
  diagnosis as a whole and error-limited du totals remain untested.
- Next: labs/2026-11-12-resource-triage.md, checked and wholly unattempted at
  session end. Then continue Phase 9 resource diagnosis/process discovery.
  Phase 8 independent lifecycle remains open; Red Hat-family comparison
  introduced conceptually, not executed.

### Earlier checkpoint before resuming

- Package lifecycle and repository repair — GUIDED. Verified catalog refresh
  after regional-mirror 404 repair, scoped two-package upgrade, and locate
  removal then purge using supplied commands and previews. Installed/candidate
  tool selection independently recalled: apt-cache policy for both upgraded
  packages. Full independent package milestone remains open.
- Catalog freshness — INDEPENDENT brief spaced verbal retrieval: explained
  that a new remote release need not appear without local refresh. Broader
  transfer and upgrade-versus-refresh reasoning remain to be assessed.
- Indexed versus live search — GUIDED verified experiment. A new home file was
  found by ls/find but absent from locate's index (status 1).
- Find construction — GUIDED on spaced review, superseding earlier independent
  same-session evidence. Full transcript revealed confusion between starting
  pathname and basename pattern; depth/type/dot constraints needed hints before
  successful execution. Local --help/man consulted.
- System-change evidence — backup before repository edit not demonstrated.
  Actual successful source used HTTP archive rather than suggested HTTPS;
  signature checks were not bypassed. Do not infer a backup from instructions.
- The previously unattempted package plan was completed with guidance after
  resuming; see current checkpoint above and sessions/2026-11-12.md.

## Previous checkpoint — 2026-11-11 (session complete)

- Package inspection and installation — GUIDED. Used supplied dpkg-query and
  apt-cache commands to inspect file ownership, metadata, dependencies, and
  installed/candidate versions. Completed simulated then real locate installation
  on Ubuntu and verified installed version plus shell resolution. Recalled
  apt-cache policy with confirmation on final verification; earlier tool
  selection needed the complete command. Retrieved command -v after a cue.
- Repository catalog freshness — GUIDED. Initially thought apt-cache policy
  fetches current web information because it displays a repository URL.
  After explanation, correctly identified Candidate as the field that may
  change after catalog refresh. No catalog refresh or upgrade performed today.
- Integrated ownership/mode repair — INDEPENDENT. Derived directory modes
  710 and 770 plus file mode 660 from a new access policy; changed all three
  group owners to users, preserved user ownership and content, and supplied
  correct before/after evidence without repair hints. Evidence capture and
  self-audit were independent in this lab; retention remains untested.
- Configuration/runtime/kernel views — GUIDED. Correctly chose `/etc` and
  `/run`, but rationale required teaching. Inspected a PID file, socket, live
  process, and `/proc` status using supplied commands. Initially thought editing
  a PID record changes the actual PID, then thought a reader would still use
  the actual PID despite changed contents. After explanation, correctly stated
  that file contents change while the actual PID does not; independent transfer
  remains untested.
- `umask` — GUIDED, with recurring bit-removal errors. For `022`, initially
  predicted file `444` and directory `744`; class-specific hints led to `644`
  and `755`. Supplied subshell experiment verified both on the Ubuntu VM.
  Correctly answered that the parenthesized change affects only the subshell
  after the scope explanation earlier in the session; parent-shell mask has
  not been read today.

## Previous checkpoint — 2026-11-10

- Directory read versus search — INDEPENDENT current session. Correctly
  predicted and verified both inverse cases: `-wx` blocked listing but allowed
  known-file access; `rw-` allowed name listing but blocked traversal. Restored
  each disposable mode and verified it.
- Directory write versus file write — GUIDED overall. Correctly predicted that
  file write permits content append without directory write, but initially
  thought directory search alone permits removal. After correction,
  independently predicted and verified the inverse: file append failed while
  directory `w+x` permitted removal of the write-protected entry.
- Permission-class selection — INDEPENDENT current retrieval. Explained without
  a hint that an owner uses owner bits and does not borrow group write.
- Numeric `chmod` — INDEPENDENT current session. Converted `rw-r-----` and `640`
  both ways, applied and verified `640`, and derived directory `750` as
  `rwxr-x---`.
- `umask` — GUIDED. After the mask-as-eraser explanation, derived file `640`
  and corrected directory `750` for `027`; a child-shell experiment verified
  both. Process-local scope and `umask 0002` restoration needed teaching/hints.
- Group/user ownership and `sudo` — GUIDED. Predicted and verified `chgrp`
  effects and restoration, observed unprivileged `chown` failure, distinguished
  effective identities with `id` versus `sudo -u root id`, and completed a
  privileged root-ownership change/restoration after repairing baseline evidence.
- Integrated permission repair — GUIDED. Independently derived and applied
  modes `750`, `750`, and `640`; initially omitted all group-owner changes and
  later repeated one target. Final evidence verified group `users` on all three
  objects, exact modes, and unchanged content.
- Command discovery — GUIDED with independent immediate tool choice. Initially
  expected `command -v cd` to print nothing; actual comparisons established
  `command -v`, `type -a`, `which`, and `whereis` roles. Independently chose
  `type -a` for all shell-visible definitions. `locate` is unavailable (status 1).
- `/dev/null` and separated streams — INDEPENDENT after spacing. Predicted zero
  bytes on read and correctly distinguished visible stderr under `> /dev/null`
  from discarded stderr under `2> /dev/null`; both failed `ls` commands retained
  status 2.
- `/sys` and `/run` orientation — GUIDED. Inspected network-class symlinks and
  operstate, private `/run/user/1000`, and `/run` as `tmpfs`. Persistent `/etc`
  configuration versus current-boot `/run` state remains the next retrieval.

## Previous checkpoint — 2026-11-09

- Environment: learner's Ubuntu VM reported Ubuntu 26.04.1 LTS, kernel
  `7.0.0-31-generic`, Bash, user/home `raf_0411` / `/home/raf_0411`, uid/gid
  1000. Tutor workspace and Obsidian notes remain on macOS.
- Local manual option recovery — INDEPENDENT. Extracted `-t char`, identified
  its syntax roles, and constructed/predicted/verified comma-delimited join.
- Frequency reports — GUIDED overall, with independent stage construction.
  Normalization/grouping/counting/ranking and saved-output inspection succeeded.
  `^PASS` admitted PASSIVE; a boundary hint led to `^PASS,` and verified counts
  4 cache, 3 queue, 1 search. Exact selection remains a review priority.
- Bounded tail inspection — RETAINED. Independently retrieved and executed
  `tail -n 5 /var/log/syslog` after spacing; live-follow options remain separate.
- Linux orientation — GUIDED. Inspected distribution, kernel, shell, home,
  `/var/log`, and `/proc` hostname. Introduced `/etc`, `/tmp`, `/` versus `/root`,
  and shell/kernel roles. Independently followed `/var` into `/var/log`.
- Command resolution and PATH — GUIDED. Inspected aliases, builtins, executable
  paths, and `/bin -> usr/bin`. Initially prioritized `/usr/bin` despite PATH
  order and thought a missing candidate stopped lookup; corrected after a trace.
- Process working directories — GUIDED. Initially predicted different builtin
  and external pwd results. Observed inherited working directories and verified
  that a child changing directory leaves the parent's directory unchanged.
- Find depth/type/name construction — INDEPENDENT current lab. Constructed
  depth-2 and unrestricted `.log` searches, with verified results. Earlier
  hidden-directory construction needed hints for `$HOME` and the name filter.
- Null-delimited find/xargs integration — INDEPENDENT immediate construction
  after teaching. Initially expected default xargs to preserve a spaced pathname;
  observed splitting. Then independently combined depth/type/name selection,
  `-print0`, and `xargs -0`, verifying three intact arguments. Retention untested.
- Permission-class reasoning — GUIDED. Correctly interpreted other-class r--,
  but thought group write supplemented missing owner write. Controlled chmod
  and test -w evidence corrected that model; independent causal retrieval pending.
- Symbolic permission removal — INDEPENDENT immediate construction. Used
  separate g-r, g-w, o-r, and o-w changes and verified root.log as `-rw-------`,
  preserving owner read/write. Earlier temporary owner-write removal was restored
  and verified before this deliberate group/other removal.
- Directory permissions — GUIDED introduction. Correctly recognized that outer
  directory traversal restrictions block access despite inner group rwx.
  Read-versus-search experiment is prepared but unattempted.

## Earlier checkpoint — 2026-11-08

- Independently constructed and verified a last-two-line capture/count command
  that works through default zsh MULTIOS. Its file-plus-pipe behavior was
  reproduced by the tutor; do not apply Bash assumptions to this evidence.
- After a functional `tee` recall cue, constructed the explicit
  `tail | tee | wc -l` pipeline correctly. Corrected an execution-only `wc -`
  typo and verified both the terminal count and saved lines. Combined routing
  remains GUIDED overall; this smaller construction succeeded with reduced
  support.
- Correctly retrieved both Bash redirection orderings after spacing and
  explained the decisive intermediate state: in `2>&1 > file`, stderr copies
  stdout while it still points to the terminal; in `> file 2>&1`, stderr copies
  the file destination. This causal redirection-order skill is INDEPENDENT in
  the current retrieval check; later unfamiliar use will test retention.
- Independently constructed and executed an `&&`/`||`/`;` sequence for both an
  existing and missing path. Initially attributed the compound line's final
  status to the earlier failed `test`; observation corrected this to the final
  successful `printf`. Then confused `$1` with `$?`, but after a conceptual
  hint correctly captured the failed test immediately as `test-status=1`.
  Conditional sequencing is currently INDEPENDENT. Later independently captured
  `diff` statuses 1 and 0 immediately, so immediate status capture is also
  INDEPENDENT in the current learning period; retention remains untested.
- Variables and command substitution remain GUIDED. On 2026-11-08, integrated
  assignment, quoted pathname expansion, stdin redirection, command
  substitution, and numeric output successfully after focused corrections.
  Initially single-quoted the variable and used it as a `wc` filename operand;
  then needed another prompt to put semicolon-separated fragments on one
  physical line. Final execution produced exact `lines=2`.
- Basic `grep` literal selection, case handling, inverse selection, count, and
  no-match status are GUIDED with several correct predictions and executions.
  Initially confused `-n` formatting and `-c` with match line numbers.
  Correctly applied `^`, `$`, `.*`, and quote protection in immediate
  exercises. Independently built a portable `grep | tee | wc -l` route; only
  the required start anchor needed correction. Verified count 3 and all saved
  matches.
- `sort`, `uniq`, `cut`, and `tr` — GUIDED first application on 2026-11-08.
  Correctly observed that `sort` emits a reordered copy without modifying the
  input and predicted reverse order. Needed correction that `uniq` collapses
  adjacent runs only and initially omitted the required grouping sort in a
  frequency pipeline. Correctly extracted first and remaining fields with
  `cut`, normalized uppercase levels with `tr` after one direction correction,
  and produced the verified ranking `3 info`, `2 warn`, `1 error`. Final causal
  explanation correctly linked sorting to adjacency-based counting.
- Frequency-report construction remains GUIDED. In a spaced opening attempt,
  separated `grep -c` from the pipeline and made `cut` reopen all source rows;
  progressive help was required to maintain selected rows through every stage.
  In a later unfamiliar checkpoint, independently chose the right tools but
  normalized case after `uniq -c`, splitting mixed-case groups. After one
  focused stage-order explanation, produced and verified `3 api`, `2 web`,
  `1 db`, then correctly distinguished grouping sort, adjacent counting, and
  final numeric ranking. Reassess after spacing without a supplied structure.
- `paste` — GUIDED first application. Correctly predicted default tab pairing
  and a custom colon delimiter, and explained that line position determines
  which rows pair. Byte evidence confirmed the displayed `\t` was tab byte 09.
- Unified `diff` — GUIDED interpretation with INDEPENDENT immediate status
  capture. Correctly predicted and read context, first-file `-`, and second-file
  `+` lines. Independently captured status 1 for different files and 0 for the
  same file, then verified redirected results. A later checkpoint honestly used
  status 1 to detect a mismatch; a tutor padding error was corrected before
  status 0 verification.
- `join` — GUIDED first application. Correctly paired equal first fields,
  explained absent unmatched keys, and predicted `-a 1 -a 2` retaining unpaired
  rows from both files. The delimiter manual task was completed independently on 2026-11-09.
- `xargs` — GUIDED first application. Correctly explained stdin-to-argument
  conversion and predicted that default parsing turns three lines containing
  `blue sky` into four arguments. Null-delimited integration advanced to INDEPENDENT on 2026-11-09.
- `sed` — GUIDED first application with independent immediate construction of
  a global substitution and redirection. Correctly distinguished transformed
  stdout from unchanged source content, then built and verified
  `sed 's/ERROR/WARN/g' events.log > normalized.log`. The final source check was
  initially omitted and supplied after one reminder.
- `awk` — GUIDED first application. Correctly predicted and ran a second-field
  condition printing the first field, and accumulated numeric fields before an
  `END` report of `total=11`. Needed a wording refinement that the print action
  runs only for records satisfying the condition.

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
  in `tail -n 4 app.log`, then constructed `head -c 7 sample.txt`. Unfamiliar manual use succeeded independently in the 2026-11-09 join task;
  broader retention remains to be tested.
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

Phase 7's practical milestone is complete. Phase 8 has progressed through guided
package/dependency/catalog inspection and a verified locate installation.
On 2026-11-12, verified locate's indexed behavior against a fresh file, repaired
an APT mirror failure with guidance, refreshed catalogs, upgraded two packages,
and verified locate removal and purge. The resumed tree plan and installation
verified successful execution, but metadata retrieval and approval reasoning
needed guidance. Bounded tree display succeeded independently; Red Hat-family tool roles were
introduced conceptually. Independent lifecycle management remains unproven.
Phase 9 has begun with guided foreground/background timers, jobs, PID/PPID,
process-state inspection, and normal completion. Job-control lab completed with
support; fresh PID inspection, targeted TERM, and exit verification independently
performed in the current session. Resource tools introduced with actual CPU,
RAM, and disk observations; broad interpretation remains guided. Resource triage has now been attempted: available-RAM selection and
scoped du construction succeeded, but workload-demand reasoning and permission-limited
totals required teaching. Running versus S remained incorrect on retrieval.
Parent-name query construction subsequently succeeded independently. Next resume
the unattempted top -o %MEM memory inspection. State interpretation, directory
traversal effects, and escalation reasoning need later review.
Runtime records versus process identity and umask still need later retrieval.

Phase 6's independent report milestone remains open for spaced review. Briefly
interleave PATH order, umask process scope, combined ownership/mode repair,
exact field selection, and find/xargs retention. Numeric modes, group ownership,
and evidence self-audit need no immediate repeat after the successful lab. Prefer actual
command/output and avoid redundant written explanations.

Detailed history is in sessions/; earlier checkpoint summaries above describe
prior evidence, while this checkpoint controls current stages and next steps.

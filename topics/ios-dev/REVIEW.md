# REVIEW

## Combine iteration, a predicate, and conditional output

- Stage: INDEPENDENT in a narrow exact-name search; not yet retained.
- Last evidence: 2026-09-22; implemented `containsItem(named:items:) -> Bool`
  without loop/return scaffolding, executed missing and matching calls, reused it
  in Add validation, and later moved the search into `ShoppingList`.
- Next test: after several sessions, require an unfamiliar collection predicate
  and both matching and missing cases without naming the loop strategy.
- Goal: verify retained selection and implementation, not repetition of the
  shopping-item search.

## Requirement trace and exact observable results

- Stage: GUIDED.
- Last evidence: 2026-09-28; for `addUses`, skipped the requested pre-code trace and
  submitted code plus predicted prints. Validation order was correct, but success
  carried the increment rather than the required updated total. Tests omitted
  intermediate state, zero, negative, precedence, and unknown-key absence checks.
- Next test: complete the current feature with a full input/result/state prediction
  and checks after each operation, without supplied assertion conditions.
- Goal: make the code, test input, exact predicted output, and requirement agree.

## Enums and exhaustive switching

- Stage: GUIDED for consistently capturing required data; INDEPENDENT for narrow
  exhaustive caller-side switches. Not yet retained.
- Last evidence: 2026-09-28; independently chose a three-case `AddResult` and wrote
  its exhaustive output switch, but modeled success with the amount added rather
  than the explicitly required updated remaining-use value.
- Next test: after meaningful spacing, require another unfamiliar finite result and
  exhaustive handling without naming enums or associated values in the prompt.
- Goal: verify retained selection and use of a finite result type.

## Optional conversion and safe extraction

- Stage: GUIDED.
- Last evidence: 2026-09-28; independently wrote a text-to-positive-Int helper,
  bound its optional result, used the unwrapped amount, and handled failed or
  nonpositive conversion before dictionary lookup. Submitted code was not yet
  reported as executed.
- Next test: after spacing, present an unfamiliar text-to-value boundary and require
  independent conversion, failure handling, and use of the unwrapped value.
- Goal: establish independent optional handling and distinguish original input,
  optional result, and unwrapped value.

## Struct methods and mutation

- Stage: GUIDED.
- Last evidence: 2026-09-28; independently declared `addUses` as `mutating`, changed
  dictionary state, and called it on a `var` store. The code was not yet reported
  as executed; the `let`-instance distinction has not been reassessed.
- Next test: after spacing, ask the learner to diagnose or implement a struct method
  that changes stored state, including the effect of declaring the instance `let`.
- Goal: independently identify when both `mutating` and a mutable instance are
  required.

## Basic closures and collection predicates

- Stage: GUIDED.
- Last evidence: 2026-09-27; after the rename branch order was clarified, used
  `firstIndex(where:)` for the mutable current item and `contains` for a duplicate
  new name. During a requested readability edit, accidentally replaced the
  duplicate search with a second equivalent inequality guard; restored the search
  after tracing why duplicate could never be returned.
- Next test: after spacing, require choosing between a yes/no search, one-position
  search, and all-match selection for an unfamiliar requirement, including matching
  and empty cases without naming the collection operation.
- Goal: independently choose, express, and verify the right predicate operation,
  including which result variable is being inspected.

## Model invariants and `private(set)`

- Stage: GUIDED.
- Last evidence: 2026-09-24; identified that direct array append bypasses validation,
  added `private(set)`, observed that external `append` is rejected, and verified
  that reading and model-owned mutation still work. Initial predictions confused
  caller restrictions with code executing inside the model and expected partial
  execution from a program containing a compile error.
- Next test: during a later model change, ask the learner to choose an access level
  and identify every mutation path that can preserve or violate the invariant.
- Goal: independently protect state while preserving necessary read access.

## Struct value semantics

- Stage: GUIDED.
- Last evidence: 2026-09-27–28; initially predicted a local `Pass` mutation would
  change its dictionary entry. After a copy-semantics hint, explained why stored
  uses remained at two and repaired the method with dictionary-subscript mutation.
  Guided checks later verified stored uses after successes and failures.
- Next test: after meaningful spacing, present an unfamiliar model-copy or update
  scenario without naming value semantics.
- Goal: verify retained reasoning and correct mutation of the intended stored value.

## Small Swift functions and array boundaries

- Stage: INDEPENDENT within narrow in-chat tasks; not yet retained.
- Last evidence: 2026-09-21; wrote/called a Bool-returning function and diagnosed
  array indexing plus the empty-array case.
- Next test: after meaningful spacing, ask for a small implemented and executed
  task combining a function with safe collection access; include an empty input.
- Goal: confirm retrieval and implementation rather than explanation alone.

## Git snapshots and branches

- Stage: GUIDED.
- Last evidence: 2026-09-27; completed a disposable workflow covering untracked,
  staged, modified, and clean states; inspected working/cached diffs; made two
  commits on `main`; carried an uncommitted version onto a new branch; made a third
  commit there; and inspected both branch snapshots. Initially thought the new
  branch pointed to uncommitted version 3, then corrected that both branch names
  initially pointed at the version 2 commit.
- Next test: after several sessions, initialize and use another disposable repo
  from a short outcome brief without command-by-command guidance; explain index,
  working tree, commit, branch pointer, and `HEAD` from observed status/history.
- Goal: verify retained independent snapshot and branch workflow.

## Development assertions

- Stage: GUIDED.
- Last evidence: 2026-09-28; initially placed all four pass-use calls before checks,
  verifying only return values and final state. After one complete example,
  interleaved calls with result/state assertions and verified unknown-ID absence.
  Reported `All checks complete` followed by the explicitly printed final zero.
  In the later `addUses` attempt, returned to prints plus a single final-state check
  and omitted several required cases.
- Next test: complete `addUses` by deriving checks from every behavioral requirement,
  including failure paths that prove state is unchanged and unknown keys stay absent.
- Goal: independently turn behavior and invariants into useful automated checks.

## Dictionaries and sets

- Stage: GUIDED for direct dictionary lookup; INDEPENDENT for narrow Set membership
  use in a function. Broader collection fluency remains guided.
- Last evidence: 2026-09-28; the `addUses` code independently used dictionary lookup
  for existence and direct subscript mutation for stored state, avoiding the prior
  local-copy bug. Execution and complete post-operation state checks are pending.
- Next test: after spacing, choose collection operations for another keyed-record
  and membership task without supplied types or lookup hints.
- Goal: independently select and combine keyed lookup with unique membership.

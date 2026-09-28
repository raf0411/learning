# REVIEW

## SwiftUI local state and view updates

- Stage: INDEPENDENT for a small single-view implementation; GUIDED explanation.
- Last evidence: 2026-09-28; independently built and ran an `@State` counter with
  add/reset behavior and private ownership. Needed instruction to explain that the
  action closure mutates state, SwiftUI reevaluates `body`, and termination loses
  nonpersistent state.
- Next test: after spacing, implement a different view-local interaction and
  explain mutation, body reevaluation, view identity, and relaunch behavior without
  being prompted to use `@State`.
- Goal: retain both implementation and the declarative update mental model.

## SwiftUI value and binding distinction

- Stage: INDEPENDENT for a narrow `TextField` implementation; GUIDED explanation.
- Last evidence: 2026-09-28; independently used `$name`, ran the view, and correctly
  predicted typing, clearing, and relaunch behavior. Initially described `name` and
  `$name` as separate wrappers and guessed that state memory transfers between
  views; received instruction on `String` versus projected `Binding<String>`.
- Next test: first complete the pending type/flow explanation in the binding probe;
  after spacing, connect another writable control without being told to use `$`.
- Goal: identify the owner, distinguish value from get/set connection, and trace a
  control write through state change to body reevaluation.

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
- Last evidence: 2026-09-28; completed the `addUses` input/result/state matrix and
  six-path verification, but only after multiple exactness corrections, a supplied
  test-block outline, and one complete assertion example.
- Next test: after spacing, derive the behavioral matrix and checks for an
  unfamiliar feature without supplied cases, assertion conditions, or sequencing.
- Goal: make the code, test input, exact predicted output, and requirement agree.

## Enums and exhaustive switching

- Stage: GUIDED for consistently capturing required data; INDEPENDENT for narrow
  exhaustive caller-side switches. Not yet retained.
- Last evidence: 2026-09-28; independently chose a three-case `AddResult` and wrote
  its exhaustive output switch, initially modeled success with the increment, then
  revised it after feedback to carry the ID and updated total. Added `Equatable`
  for direct result assertions.
- Next test: after meaningful spacing, require another unfamiliar finite result and
  exhaustive handling without naming enums or associated values in the prompt.
- Goal: verify retained selection and use of a finite result type.

## Optional conversion and safe extraction

- Stage: GUIDED.
- Last evidence: 2026-09-28; independently wrote a text-to-positive-Int helper,
  bound and used its result before dictionary lookup, and learner-reported passing
  checks for invalid text, zero, negative input, and validation precedence.
- Next test: after spacing, present an unfamiliar text-to-value boundary and require
  independent conversion, failure handling, and use of the unwrapped value.
- Goal: establish independent optional handling and distinguish original input,
  optional result, and unwrapped value.

## Struct methods and mutation

- Stage: GUIDED.
- Last evidence: 2026-09-28; independently declared `addUses` as `mutating`, changed
  dictionary state, called it on a `var` store, and learner-reported successful
  execution. The `let`-instance distinction has not been reassessed.
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
- Last evidence: 2026-09-28; in `addUses`, initially treated prints as checks,
  omitted two cases, delayed assertions, and missed absent-key evidence. After a
  six-block outline and one supplied assertion example, interleaved complete result
  and state assertions for all six operations, including two absent-key checks;
  learner reported `All checks complete.`
- Next test: after spacing, independently derive and sequence checks for a different
  state-changing feature without an assertion example.
- Goal: independently turn behavior and invariants into useful automated checks.

## Dictionaries and sets

- Stage: GUIDED for direct dictionary lookup; INDEPENDENT for narrow Set membership
  use in a function. Broader collection fluency remains guided.
- Last evidence: 2026-09-28; `addUses` used dictionary lookup for existence and
  direct subscript mutation for stored state, avoiding the prior local-copy bug.
  Learner-reported assertions verified the stored total and that `P404` stayed
  absent after valid-unknown and invalid-unknown operations.
- Next test: after spacing, choose collection operations for another keyed-record
  and membership task without supplied types or lookup hints.
- Goal: independently select and combine keyed lookup with unique membership.

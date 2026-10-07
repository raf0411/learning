# REVIEW

## SwiftUI local state and view updates

- Stage: INDEPENDENT for a small single-view implementation; GUIDED for explanation
  and whole-model integration.
- Last evidence: 2026-09-29; connected a supplied ShoppingList struct to private
  view-owned state, derived its count, and learner-reported correct UI changes for
  success and failure paths. Required explicit correction after replacing the
  assigned initial data and using status-message text to infer success. Earlier
  counter runs covered reset and termination/relaunch.
- Next test: after spacing, implement a different view-local interaction and
  explain mutation, body reevaluation, view identity, and relaunch behavior without
  being prompted to use `@State`.
- Goal: retain both implementation and the declarative update mental model.

## SwiftUI value and binding distinction

- Stage: INDEPENDENT for a narrow `TextField` implementation; GUIDED explanation.
- Last evidence: 2026-09-30; completed the child form and reported correct draft
  clearing/preservation and a successful build. Needed explicit correction that
  bindings connect to parent storage; the final event traces were supplied.
- Next test: after spacing, connect another writable control without being told
  to use `$`, and explain changes initiated by either the control or its owner.
- Goal: identify the owner, distinguish value from get/set connection, and trace a
  control write through state change to body reevaluation.

## SwiftUI collection rendering and stable identity

- Stage: GUIDED.
- Last evidence: 2026-09-29; after instruction on `Identifiable`, correctly
  distinguished stable UUID identity from editable name/quantity, implemented
  `ForEach` over the model array, and learner-reported correct append and
  duplicate-no-change row behavior.
- Next test: after spacing, render an unfamiliar identifiable collection and
  explain how edit, removal, insertion, and recreation affect row identity.
- Goal: independently choose stable identity and render model-derived rows without
  parallel UI state.

## SwiftUI parent-child ownership and actions

- Stage: GUIDED.
- Last evidence: 2026-09-30; selected a read-only item and Save action, then chose
  local draft state after a cancel-without-save prompt. Repaired the String-input,
  UpdateResult-output action chain after a supplied trace; reported correct saved,
  discarded, and rejected edits. Initially thought a parent-created closure reads
  child-local drafts; identified parent values after a scope hint.
- Next test: after spacing, choose read-only values, local state, bindings, or
  actions for a different interface; wire a parameterized action and identify its
  captured values, input, and return without a supplied function shape.
- Goal: keep source-of-truth ownership clear while allowing child display, editing,
  and event reporting through appropriately narrow interfaces.

## Rejected input and unchanged state

- Stage: GUIDED.
- Last evidence: 2026-09-30; predicted and reported Milk unchanged after leaving
  an unsaved detail draft and Bread unchanged after a rejected zero quantity.
  These used an existing validator and a supplied scenario table. Earlier blank
  input reasoning required a trace and a character-count diagnostic.
- Next test: during a later input feature, independently predict and verify both
  draft and accepted data after rejected input; establish exact test preconditions.
- Goal: reason from executed branches and verify invisible input without guessing.

## Navigation and separate actions

- Stage: GUIDED.
- Last evidence: 2026-09-30; implemented a stack, row link, read-only destination,
  and separate Remove control; reported correct push, Back, and removal behavior.
- Next test: after spacing, add a destination from a short feature brief and explain
  the effect of Back on navigation history and model state.
- Goal: independently wire navigation while keeping mutation responsibilities clear.

## Class references and let

- Stage: GUIDED overall; INDEPENDENT in one short shared/separate prediction.
- Last evidence: 2026-10-06; recognized that a child `let` can call a class method
  that changes the instance. The tutor supplied the precise distinction between
  reference reassignment, instance-property mutation, and direct mutation blocked
  by `private(set)`. In the shopping lab, separate-instance counts needed repeated
  clarification before reaching parent `4`, summary `3`.
- Next test: after spacing, compare a class reference with a struct copy and
  distinguish let-reference reassignment from instance-property mutation without
  being cued that class semantics are the deciding factor.
- Goal: choose the intended instance and distinguish sharing from observation.

## Observation, state ownership, and bindings

- Stage: GUIDED.
- Last evidence: 2026-10-06; implemented a parent-owned observable Profile and a
  child `@Bindable` TextField/Toggle, with learner-reported actual results matching
  all child-edit and parent-Reset predictions. Needed supplied traces to separate
  binding setters/getters from Observation, and repeated correction to distinguish
  `let` reference reassignment from binding projection.
- Next test: after spacing, choose and implement the ownership and control-binding
  declarations for an unfamiliar observable model without wrapper hints, then
  independently trace a control write and an owner write.
- Goal: distinguish reference sharing, property mutation, UI observation, model
  lifetime, and a control's binding requirement.

## Persistence lifetime and storage selection

- Stage: GUIDED for `@AppStorage` and introductory SwiftData.
- Last evidence: 2026-10-07; implemented a minimal `PantryItem` model, app and
  preview containers, context inserts, and a name-sorted query after corrections.
  Learner-reported query-driven count/row updates and relaunch persistence after
  independently adding throwing explicit saves with `do`/`catch`. Initially
  omitted the two containers, predicted insertion rather than sorted display
  order, and was unsure whether `@Query` owned records. A quick autosave run lost
  pending changes; the follow-up changed both lifecycle and save behavior and left
  its prediction blank, so it verified manual saving but not autosave.
- Next test: complete the assigned controlled autosave rerun without changing the
  code after predicting. After spacing, choose storage for unfamiliar temporary
  UI state, preferences, and records without being given candidate tools, then
  implement the structured-record choice with less scaffolding.
- Goal: choose storage by data lifetime and shape, and verify persistence rather
  than inferring it from an in-memory update; distinguish insert, save, storage,
  query, and rendering roles.

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
- Last evidence: 2026-10-06; the observable-shopping worksheet initially predicted
  all counts as three despite sequential Add/Remove operations, then temporarily
  applied a separate-instance result to the shared-instance table. Corrected the
  required label casing and ultimately preserved correct predictions beside
  learner-reported actuals. Also initially chose invalid quantity over the earlier
  duplicate guard for `Flower / abc`; validation precedence required a trace.
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
  On 2026-09-30, reversed old/new variables when matching UpdateResult in the
  detail screen; repaired their positional order after feedback.
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

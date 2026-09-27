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
- Last evidence: 2026-09-27; predicted all 12 rename result/state lines correctly
  and reported matching output. During construction, still changed the requested
  method label, omitted a state prefix and success punctuation, capitalized a
  failure message differently, and printed `renamed` instead of requested
  `rename`. Each was corrected after comparison.
- Next test: use a different small feature and require a complete input/branch/state/
  exact-output prediction before execution, without reminders about omitted parts.
- Goal: make the code, test input, exact predicted output, and requirement agree.

## Enums and exhaustive switching

- Stage: INDEPENDENT in a small task; not yet retained.
- Last evidence: 2026-09-26; reused the four-case `UpdateResult` correctly and
  independently wrote its exhaustive caller-side print switch with associated
  values. Initially omitted the requested underscore argument label, then corrected
  it; enum handling itself was correct.
- Next test: after meaningful spacing, require another unfamiliar finite result and
  exhaustive handling without naming enums or associated values in the prompt.
- Goal: verify retained selection and use of a finite result type.

## Optional conversion and safe extraction

- Stage: GUIDED.
- Last evidence: 2026-09-27; dictionary lookup introduced another optional
  boundary. Initially called `Int(quantities["Milk"])`, treating an `Int?` as text
  needing conversion. After explanation, directly bound present/missing lookups
  with `if let`, used the unwrapped integer, and reported matching output.
- Next test: after spacing, present an unfamiliar text-to-value boundary and require
  independent conversion, failure handling, and use of the unwrapped value.
- Goal: establish independent optional handling and distinguish original input,
  optional result, and unwrapped value.

## Struct methods and mutation

- Stage: GUIDED.
- Last evidence: 2026-09-23; used the `mutating` Add method and reported the compiler
  error after changing the instance to `let`. Needed clarification that constants
  prohibit mutating methods, not all methods.
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
- Last evidence: 2026-09-26; correctly used direct array-subscript mutation in the
  update method, but initially explained its effect using model scope and
  `private(set)` rather than stored value versus local copy. After clarification,
  correctly predicted that changing a local item after assigning it into an array
  leaves the array's value unchanged.
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
- Last evidence: 2026-09-27; ran passing filter assertions, deliberately observed a
  failing assertion halt the Playground with the supplied message, restored it,
  then independently wrote final rename assertions for count, ordered names, and
  quantities. Exact failure/success literals needed two corrections.
- Next test: in an unfamiliar feature after spacing, derive assertions from the
  behavioral requirements without supplied conditions or a visual-output oracle;
  include a failure path that proves state is unchanged.
- Goal: independently turn behavior and invariants into useful automated checks.

## Dictionaries and sets

- Stage: GUIDED for dictionary basics; RECOGNIZED for Set basics.
- Last evidence: 2026-09-27; used dictionary lookup, optional binding, update,
  insertion, removal, count and lookup assertions, plus a dictionary of structs.
  Predicted and observed simple Set uniqueness and membership behavior. Initial
  errors conflated `Int?` lookup with text conversion and miscounted update/add/
  remove effects before tracing them.
- Next test: complete the pending `canCheckIn` transfer function using dictionary
  key existence and Set membership without naming the operations; test registered,
  already-checked-in, and unknown IDs.
- Goal: independently select and combine keyed lookup with unique membership.

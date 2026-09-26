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
- Last evidence: 2026-09-26; update verification initially changed an argument
  label, punctuation, wording, and requested state format. After correction, a
  filter test omitted count labels and accidentally inspected `filteredItems1`
  again instead of `filteredItems2`. Both tests eventually matched the briefs after
  explicit comparison and diagnosis.
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
- Last evidence: 2026-09-22; after correcting a crash misconception, observed
  successful and failed `Int` conversion, used `if let`, implemented a function
  returning `Int?`, and stored only a validated non-optional quantity. Needed
  repeated prompts to print the returned integer rather than the source string.
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
- Last evidence: 2026-09-26; independently reused `firstIndex(where:)` and
  `guard let` for exact-name update. After the purpose and general shape of `filter`
  were taught, implemented `item.quantity >= minimum` correctly. Initially expected
  values `5` and `6` to pass a threshold of `7`, then used the first result variable
  again while testing the second result; corrected both after feedback.
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

- Stage: RECOGNIZED.
- Last evidence: 2026-09-21; distinguished a commit from merely creating a branch
  once uncommitted changes were made explicit.
- Next test: during the first disposable Git lab, predict and inspect what a
  commit records and whether another commit requires another branch.
- Goal: establish a usable workflow and resolve the remaining branching ambiguity.

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
- Last evidence: 2026-09-24; correctly traced all Remove count transitions and
  branches, but initially used array contents where the returned enum result was
  requested, changed the assigned input, and wrote `1 item remain` instead of the
  exact required `1 items remain`.
- Next test: use a different small feature and require a complete input/branch/state/
  exact-output prediction before execution, without reminders about omitted parts.
- Goal: make the code, test input, exact predicted output, and requirement agree.

## Enums and exhaustive switching

- Stage: INDEPENDENT in a small task; not yet retained.
- Last evidence: 2026-09-24; designed a new `RemoveResult` with associated removed
  name/count and not-found name, then wrote an exhaustive switch without syntax
  scaffolding. The exact success message was wrong, but case modeling and extraction
  were correct.
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
- Last evidence: 2026-09-24; reused `contains` for Remove but inverted the meaning
  through an `isNotFound` name/guard mismatch and discovered that a Bool is
  insufficient when removal requires the matching position. Correctly traced the
  faulty branch after prompting; the proposed `firstIndex(where:)` repair was not
  implemented before session end.
- Next test: resume by independently writing the `firstIndex(where:)` predicate,
  unwrapping its optional index, and removing the match; later use a different
  predicate without naming the collection strategy.
- Goal: independently express and explain a collection predicate, including the
  element parameter, returned Bool, and short-circuit behavior where applicable.

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

- Stage: INDEPENDENT in an immediate narrow experiment; not yet retained.
- Last evidence: 2026-09-21; predicted and learner-reported that mutating a copied
  `ShoppingItem` leaves the original false while the copy becomes true, then
  transferred the explanation to a struct retrieved from an array.
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

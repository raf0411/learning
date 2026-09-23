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
- Last evidence: 2026-09-23; completed an enum-backed Add trace and implementation,
  but needed reminders for before/after count transitions, all requested calls,
  complete predictions, exact punctuation, and a leftover experimental output line.
- Next test: use a different small feature and require a complete input/branch/state/
  exact-output prediction before execution, without reminders about omitted parts.
- Goal: make the code, test input, exact predicted output, and requirement agree.

## Enums and exhaustive switching

- Stage: GUIDED.
- Last evidence: 2026-09-23; returned `AddResult` from model validation, handled it
  exhaustively in the caller, and used associated values for normalized success
  data. After one example, independently transferred the associated-value pattern
  to the duplicate case.
- Next test: after spacing, require an unfamiliar enum with associated data and an
  exhaustive switch without syntax scaffolding, then add a case and explain the
  compiler consequence.
- Goal: independently use a finite result type and rely on exhaustive handling.

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
- Last evidence: 2026-09-23; after closure instruction, replaced duplicate search
  with `contains`, then independently wrote a quantity-at-least-10 predicate and
  correctly traced short-circuit evaluation across Milk and Eggs.
- Next test: after spacing, require a different `contains`, `first(where:)`, or
  filtering predicate without supplying the closure structure.
- Goal: independently express and explain a collection predicate, including the
  element parameter, returned Bool, and short-circuit behavior where applicable.

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

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
- Last evidence: 2026-09-22; implemented a quantity-aware Add change and eventually
  supplied the complete cleaning/check/mutation/display trace. Later wrote an
  enum-switch exercise whose prediction matched the submitted code, but swapped
  the first two supplied test inputs and therefore changed the assigned scenario.
- Next test: for the enum-backed Add refactor, require ordered cases and exact
  predicted messages before execution, with no reminder to include every branch.
- Goal: make the code, test input, exact predicted output, and requirement agree.

## Enums and exhaustive switching

- Stage: GUIDED.
- Last evidence: 2026-09-22; wrote and ran a complete four-case `AddResult` switch
  with correct messages. After instruction, predicted and observed that adding an
  unhandled enum case makes the switch fail exhaustiveness checking; the first
  experiment instead created an empty switch case and required correction.
- Next test: after further application and spacing, require an unfamiliar enum and
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
- Last evidence: 2026-09-22; after instruction, wrote a `mutating` Add method,
  called it on a `var ShoppingList`, and implemented a read-only search method.
- Next test: after spacing, ask the learner to diagnose or implement a struct method
  that changes stored state, including the effect of declaring the instance `let`.
- Goal: independently identify when both `mutating` and a mutable instance are
  required.

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

# REVIEW

## Combine iteration, a predicate, and conditional output

- Stage: GUIDED.
- Last evidence: 2026-09-21; independently selected the correct loop, predicate,
  conditional, printed values, and output for a restock filter, but needed a
  reminder to supply the function's argument label and then corrected a name typo.
- Next test: resume the pending `containsItem(named:items:) -> Bool` task without
  supplying its loop or return structure. Execute both matching and missing cases.
- Goal: demonstrate independent implementation and check all requested outputs.

## Requirement trace and exact observable results

- Stage: GUIDED.
- Last evidence: 2026-09-21; decomposed Add, blank-input, and duplicate behaviors,
  then implemented all three. Needed repeated prompts for omitted messages, exact
  capitalization/marker formatting, Foundation import, assigned initial state,
  and separating Add from Mark Purchased.
- Next test: during the next small change, require a before/action/check/result
  breakdown and predictions for each branch before execution, with fewer prompts.
- Goal: make the code, test input, exact predicted output, and requirement agree.

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

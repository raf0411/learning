# STATE

Updated: 2026-09-24 — session ended during the unfinished Remove implementation.

## Evidence limits

Assessment evidence is code, reasoning, predictions, and learner-reported Xcode
output supplied in chat; the tutor did not directly observe the Xcode runs.
INDEPENDENT below applies only to the small tasks described, not whole features.
Nothing has yet demonstrated RETAINED or TRANSFERABLE performance.

## Current abilities

- Variables, assignment, and `var`/`let` — INDEPENDENT in small snippets. Correct
  mutation/constant explanation and arithmetic; output requirements were sometimes
  omitted. Distinguishes integer values from strings.
- Conditions — INDEPENDENT in a small purchase exercise using `>=` and `if/else`.
- Functions — INDEPENDENT for a two-parameter integer function returning Bool,
  including a labeled call, stored result, and output prediction.
- Arrays and iteration — INDEPENDENT for an exact-name search in a small array.
  Implemented `containsItem(named:items:) -> Bool` without its loop or return
  structure being supplied, then moved the same search into `ShoppingList` as a
  read-only method. Broader collection work has not been independently assessed.
- Array bounds — INDEPENDENT conceptual diagnosis of an invalid index; reasons
  about zero-based indexing, last index, and the empty-array case. No executed fix.
- Requirements decomposition — GUIDED for Add-item changes. Eventually produced
  an ordered trace covering cleaning, empty/duplicate/quantity validation,
  conditional mutation, and final display, but initially omitted checks and output
  details even when the implementation contained them.
- Input cleaning and validation — GUIDED. Used Foundation trimming, empty checks,
  reusable exact-duplicate detection, positive-integer conversion, and conditional
  append. Learner-reported runs covered valid, duplicate, whitespace-only, zero
  quantity, and competing duplicate/invalid-quantity paths.
- Struct data models — GUIDED. Extended `ShoppingItem` to store a validated,
  non-optional quantity and explained why conversion may be optional while the
  stored property need not be. Created a `ShoppingList` owning its item array.
- Struct value semantics — INDEPENDENT in an immediate narrow experiment. Predicted
  and learner-reported `false` then `true` after mutating a copied struct, and
  correctly explained why an array's stored original remains unchanged.
- Optionals and failed conversion — GUIDED. Corrected an initial belief that
  `Int("hello")` crashes after observing `Optional<Int>`, `Optional(20)`, and
  `nil`; used `if let`, wrote `validQuantity(from:) -> Int?`, and distinguished
  original text `"004"` from the unwrapped integer `4`. Needed repeated prompts
  to use the returned value rather than merely check it for `nil`.
- Struct methods and mutation — GUIDED. After instruction on `mutating`, wrote and
  ran a `ShoppingList.add(_:)` method on a `var` instance and reported count `1`.
  Correctly implemented a read-only `containsItem` method, but initially created
  Milk without calling `add`, producing `false` for both searches before correction.
- Enums and exhaustive `switch` — INDEPENDENT in a small result-modeling task.
  After one day of spacing, designed a new three-case `RemoveResult` with the
  required associated values and wrote an exhaustive caller-side switch without
  syntax scaffolding. Exact message text still differed from the requirement, so
  this does not establish exact-output reliability or retained mastery.
- Guard statements and optional binding — GUIDED. Refactored empty-name and
  quantity validation into early-exit guards after syntax instruction and correctly
  explained that the successfully bound quantity is a non-optional positive `Int`
  within the remaining function scope.
- Basic closures with `contains` — GUIDED. After instruction, replaced a manual
  duplicate loop with `contains`, then wrote a quantity-at-least-10 predicate and
  correctly explained its Milk-false/Eggs-true short-circuit behavior.
- Model invariants and restricted mutation — GUIDED. Correctly predicted that an
  exposed array lets callers bypass empty-name and positive-quantity validation.
  Added `private(set)`, observed the external `append` compiler error, verified that
  the model's own mutating Add method still produced count `3` and name `Bread`,
  and then explained getter access versus setter restriction. Initially believed
  the model's own Add call would also be rejected and that earlier prints would run
  despite a later compile error; both misconceptions were corrected before the lab.
- Finding and removing a matching array element — GUIDED/INCOMPLETE. In a new
  Remove feature, reused `contains` but named its result `isNotFound`, inverted the
  guard, and had no index with which to remove the element. Correctly traced after
  prompting that Eggs makes `contains` true, the current guard returns `notFound`,
  and no mutation occurs. `firstIndex(where:)`, optional-index handling, and
  `remove(at:)` were introduced as the next repair but not implemented or run.
- Model versus presentation responsibility — GUIDED. After explanation, correctly
  identified that a language-only message change belongs in caller-side result
  formatting rather than `ShoppingList` validation.
- SwiftUI local state — RECOGNIZED with correct simple behavior predictions,
  including a fresh launch resetting the example counter. View implementation
  has not been assessed.
- Xcode — learner reports repeatedly executing the session's Swift snippets and
  supplied outputs matching the code's validation and model branches. Workflow
  and console were not directly observed.
- Git — RECOGNIZED. Understands a commit is needed to record uncommitted changes
  after a concrete scenario; no workflow execution assessed.

## Current gaps and uncertainties

- State shared between SwiftUI views — UNKNOWN.
- Networking request-to-display flow — UNKNOWN.
- Translating every detail of a requirement into code and test setup remains
  inconsistent. The learner has omitted requested output details, used an
  input/initial state different from the assigned scenario, or mismatched exact
  formatting. During the enum-backed Add lab, the learner repeatedly omitted
  requested calls or predictions, missed required punctuation, and initially left
  a temporary experiment that produced an unpredicted output line. In the Remove
  exercise, counts and branch outcomes were mostly traced correctly, but the
  returned enum result was confused with array state, `item remain` replaced the
  specified `items remain`, and the supplied test input was altered.
- Debugging tools beyond inspecting the error and stopped line — unassessed.
- Git branching purpose needs clarification: learner may believe further changes
  require a new branch. Do not treat that interpretation as established.
- Classes/reference semantics, architecture, persistence, concurrency, formal
  tests, documentation use, and remaining advanced fundamentals — unassessed.

## Instructional implications

Resume the unfinished Remove repair: independently write a `firstIndex(where:)`
predicate, unwrap its optional index, remove at that index, calculate the count
after mutation, restore the exact assigned calls/message, and compare actual output
with the prediction. Then have the learner explain why an index rather than a Bool
is required. Continue requiring complete test setups and exact outputs; those
mismatches remain more persistent than the small enum/model syntax.

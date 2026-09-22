# STATE

Updated: 2026-09-22 — second learning block ended.

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
- Enums and exhaustive `switch` — GUIDED. Wrote the four-case `AddResult` enum and
  a complete switch with correct messages, then observed the compiler reject a
  switch after a fifth enum case was added. Needed teaching to explain why no
  `default` was required and correction after first adding an empty switch case.
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
  formatting. In the enum exercise, the first two supplied test inputs were
  reordered even though the resulting prediction matched the changed code.
- Debugging tools beyond inspecting the error and stopped line — unassessed.
- Git branching purpose needs clarification: learner may believe further changes
  require a new branch. Do not treat that interpretation as established.
- Classes/reference semantics, architecture, persistence, concurrency, formal
  tests, documentation use, and remaining advanced fundamentals — unassessed.

## Instructional implications

Resume with the ordered trace for the supplied enum-backed Add scenarios, then
use `AddResult` to move validated Add behavior into `ShoppingList` while keeping
the learner responsible for the implementation. Continue checking that
predictions, input order, exact messages, and actual output describe the same
scenario; requirement/test mismatches remain more persistent than the underlying
small-code logic. Recheck optionals and `mutating` after spacing before promoting
either skill.

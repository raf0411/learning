# STATE

Updated: 2026-09-26 — `updateQuantity` and guided `filter` verification complete;
the first `assert` exercise has been introduced but not attempted.

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
  read-only method. Has now used `filter` to return every item meeting a quantity
  threshold, but only after its purpose and general closure shape were supplied.
- Array bounds — INDEPENDENT conceptual diagnosis of an invalid index; reasons
  about zero-based indexing, last index, and the empty-array case. No executed fix.
- Requirements decomposition — GUIDED. Produced the correct ordered plan for a new
  quantity-update feature, including validation, lookup, mutation, and results.
  Needed prompting to state that conversion failure or a nonpositive value is
  invalid, attach the cleaned name to `notFound`, capture the old value before
  mutation, and keep printing outside the model.
- Input cleaning and validation — GUIDED. Used Foundation trimming, empty checks,
  reusable exact-duplicate detection, positive-integer conversion, and conditional
  append. Learner-reported runs covered valid, duplicate, whitespace-only, zero
  quantity, and competing duplicate/invalid-quantity paths.
- Struct data models — GUIDED. Extended `ShoppingItem` to store a validated,
  non-optional quantity and explained why conversion may be optional while the
  stored property need not be. Created a `ShoppingList` owning its item array.
- Struct value semantics — GUIDED. Previously predicted and learner-reported that
  mutating a copied struct leaves the original unchanged. During `updateQuantity`,
  initially attributed stored-element mutation to being inside the model and to
  `private(set)`, rather than to direct subscript mutation. After clarification,
  correctly predicted that changing a local copy again after assigning it into an
  array leaves the array at `5` while the local copy becomes `7`.
- Optionals and failed conversion — GUIDED. Corrected an initial belief that
  `Int("hello")` crashes after observing `Optional<Int>`, `Optional(20)`, and
  `nil`; used `if let`, wrote `validQuantity(from:) -> Int?`, and distinguished
  original text `"004"` from the unwrapped integer `4`. Needed repeated prompts
  to use the returned value rather than merely check it for `nil`.
- Struct methods and mutation — GUIDED. After instruction on `mutating`, wrote and
  ran a `ShoppingList.add(_:)` method on a `var` instance and reported count `1`.
  Correctly implemented a read-only `containsItem` method, but initially created
  Milk without calling `add`, producing `false` for both searches before correction.
- Enums and exhaustive `switch` — INDEPENDENT in small result-modeling tasks.
  Designed `RemoveResult` and its exhaustive caller-side switch, then on the next
  day independently wrote a correct four-case `UpdateResult` with associated name,
  old quantity, and new quantity. Exact-output reliability is tracked separately;
  the short interval and prompted result requirements do not yet establish RETAINED.
- Guard statements and optional binding — GUIDED overall, with one independent
  reuse. Initially interpreted a
  `firstIndex` result as Bool and again wrote an inverted `guard index == nil`,
  which would continue on absence and return `notFound` on a match. After direct
  instruction, used `guard let` in Remove and independently reused the pattern in
  a quantity-based removal method. On 2026-09-26, independently selected and wrote
  `firstIndex(where:)` plus `guard let` for the new update method from behavioral
  requirements, without repeating the earlier inverted guard. The post-guard
  non-optional nature of the index was not re-explained by the learner.
- Basic closures and collection predicates — GUIDED. Uses `contains` for duplicate
  detection and writes `firstIndex(where:)` predicates for exact-name and
  quantity-threshold searches. Independently reused exact-name lookup in the update
  feature. After instruction on `filter`, correctly implemented
  `item.quantity >= minimum` to return all matches, but initially predicted that
  quantities `5` and `6` would satisfy a threshold of `7` and later inspected the
  first filter result twice instead of the second.
- Model invariants and restricted mutation — GUIDED. Correctly predicted that an
  exposed array lets callers bypass empty-name and positive-quantity validation.
  Added `private(set)`, observed the external `append` compiler error, verified that
  the model's own mutating Add method still produced count `3` and name `Bread`,
  and then explained getter access versus setter restriction. Initially believed
  the model's own Add call would also be rejected and that earlier prints would run
  despite a later compile error; both misconceptions were corrected before the lab.
- Finding and removing a matching array element — GUIDED. Completed and learner-
  reportedly ran Remove using `firstIndex(where:)`, `guard let`, `remove(at:)`, and
  the post-mutation count. Then implemented a quantity-threshold variant with a
  different predicate and three sequential found/found/missing branches. Direct
  instruction was needed to repair the first inverted guard, so retention and an
  unprompted choice of this strategy remain unassessed.
- Updating a stored array element — INDEPENDENT implementation from explicit
  behavioral requirements; verification remained GUIDED. Correctly validated the
  two inputs, found and unwrapped an index, captured the old quantity before direct
  subscript mutation, and returned the associated old/new data. Learner-reported
  runs covered success, invalid zero, missing name, and blank name while showing
  that failure paths preserved state.
- Model versus presentation responsibility — GUIDED. After explanation, correctly
  identified that a language-only message change belongs in caller-side result
  formatting rather than `ShoppingList` validation. Kept update messages in an
  exhaustive caller-side switch rather than printing from the model.
- Manual verification and development assertions — GUIDED/RECOGNIZED. Eventually
  produced exact result and state output for every update path and exact labeled
  output for two filter thresholds. Needed comparison prompts to correct punctuation,
  wording, state-line format, count labels, and use of the wrong filtered variable.
  `assert` and `isEmpty` checks were introduced at session end but not yet predicted
  or executed.
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
  a temporary experiment that produced an unpredicted output line. Remove required
  reminders to restore the exact input and empty-name message. The subsequent
  quantity-removal test initially omitted Bread, changed the requested argument
  label, and printed only the final state rather than each transition; all were
  corrected after explicit comparison with the brief. On 2026-09-26, update tests
  again required corrections to an argument label, punctuation, wording, and exact
  state format. A filter test then omitted labels and accidentally printed and
  iterated over `filteredItems1` instead of inspecting `filteredItems2`.
- Debugging tools beyond inspecting the error and stopped line — unassessed.
- Git branching purpose needs clarification: learner may believe further changes
  require a new branch. Do not treat that interpretation as established.
- Classes/reference semantics, architecture, persistence, concurrency, formal
  tests, documentation use, and remaining advanced fundamentals — unassessed.

## Instructional implications

Resume with the pending `assert` predictions, then add and run the three supplied
assertions for the two filter results and unchanged original list. Deliberately
make one assertion fail, inspect the evidence, and restore it. Continue requiring
a literal requirement-to-test checklist: exact observation and selection of the
correct test variable remain more persistent gaps than model syntax. Later reassess
stored-value versus local-copy behavior and selection of `guard let`,
`firstIndex(where:)`, and `filter` after meaningful spacing rather than treating
today's work as retained.

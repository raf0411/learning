# STATE

Updated: 2026-09-28 — completed event eligibility/status work and a guided
pass-store debugging lab with assertions after each operation.

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
  Used `map` plus `joined(separator:)` to format every item on one line after both
  operations were introduced; initially omitted the required `State: ` prefix.
- Array bounds — INDEPENDENT conceptual diagnosis of an invalid index; reasons
  about zero-based indexing, last index, and the empty-array case. No executed fix.
- Requirements decomposition — GUIDED. Produced the correct ordered plan for a new
  quantity-update feature, including validation, lookup, mutation, and results.
  Needed prompting to state that conversion failure or a nonpositive value is
  invalid, attach the cleaned name to `notFound`, capture the old value before
  mutation, and keep printing outside the model. For Rename, initially searched
  the new name before locating the current item, combined distinct empty-input
  results, and treated an unchanged name as a duplicate; repaired the branch order
  after explicit feedback.
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
  In the pass-store lab, again initially predicted that mutating a local struct
  updates its dictionary entry. After a copy-semantics hint, explained the bug
  and chose dictionary-subscript mutation to fix it; subsequent checks passed.
- Optionals and failed conversion — GUIDED. Corrected an initial belief that
  `Int("hello")` crashes after observing `Optional<Int>`, `Optional(20)`, and
  `nil`; used `if let`, wrote `validQuantity(from:) -> Int?`, and distinguished
  original text `"004"` from the unwrapped integer `4`. Needed repeated prompts
  to use the returned value rather than merely check it for `nil`.
- Struct methods and mutation — GUIDED. After instruction on `mutating`, wrote and
  ran a `ShoppingList.add(_:)` method on a `var` instance and reported count `1`.
  Correctly implemented a read-only `containsItem` method, but initially created
  Milk without calling `add`, producing `false` for both searches before correction.
- Enums and exhaustive `switch` — INDEPENDENT in narrow prior result-modeling
  tasks; GUIDED for the new Rename requirements.
  Designed `RemoveResult` and its exhaustive caller-side switch, then on the next
  day independently wrote a correct four-case `UpdateResult` with associated name,
  old quantity, and new quantity. `RenameResult` required prompts for distinct
  empty-input and unchanged cases, then its six-case caller-side switch was
  exhaustive and extracted every associated value correctly. Exact-output
  reliability is tracked separately; none of this yet establishes RETAINED.
  For event status, independently selected a three-case enum but omitted required
  associated data. Added names/ID after a reminder, then independently wrote the
  exhaustive caller-side switch with exact predicted and reported output.
- Guard statements and optional binding — GUIDED overall, with one independent
  reuse. Initially interpreted a
  `firstIndex` result as Bool and again wrote an inverted `guard index == nil`,
  which would continue on absence and return `notFound` on a match. After direct
  instruction, used `guard let` in Remove and independently reused the pattern in
  a quantity-based removal method. On 2026-09-26, independently selected and wrote
  `firstIndex(where:)` plus `guard let` for the new update method from behavioral
  requirements, without repeating the earlier inverted guard. The post-guard
  non-optional nature of the index was not re-explained by the learner.
  Correctly ordered registration and membership guards in event eligibility;
  needed a reminder to bind the name with `guard let` for the richer status result.
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
- Renaming a stored array element — GUIDED. Implemented a six-result rename method
  using exact-name index lookup, unchanged detection, duplicate detection, direct
  stored mutation, and cleaned associated values. Planning initially confused the
  roles/order of current and new names. A correction accidentally removed the
  duplicate collection check, which was restored after the unreachable duplicate
  branch was explained. Reported exact success/failure state for all six paths.
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
- Manual verification and development assertions — GUIDED. Produced exact result
  and state output for every rename path and independently wrote final-state
  assertions for count, ordered names, and ordered quantities. Ran passing
  assertions, deliberately observed a failing assertion stop the Playground, and
  extracted its source/message evidence. Exactness still needed corrections for a
  failure-message capital, missing `State:` prefix, success punctuation, and
  `rename` versus `renamed` in the final marker.
  In the pass-store lab, initially checked all return values and only the final
  state. After an example of placing assertions directly after an operation,
  completed checks for both successful uses, exhaustion, and an absent unknown ID;
  learner reported all checks passing. Independent test sequencing remains open.
- Dictionaries — GUIDED. Can declare and mutate `[String: Int]`, distinguish
  insertion/update/removal, predict count changes after correction, assert lookup
  outcomes, and use `if let` for present/missing keys. Initially treated a present
  lookup as `Int` rather than `Int?` and attempted `Int(Int?)`, confusing optional
  extraction with text conversion. Also used a dictionary of `Account` structs and
  understands that keys, not values, must be unique.
  Independently combined a dictionary key predicate with Set membership for
  `canCheckIn`; changed to direct key lookup after a hint. Used dictionary-subscript
  mutation to repair `PassStore` after the local-copy bug was explained.
- Sets — INDEPENDENT for membership checks in a small eligibility function.
  Correctly excluded already-checked-in IDs using `!checkedInIDs.contains(id)`
  without a supplied operation. Set construction/mutation remains assessed only
  through simple predictions and learner-reported runs.
- SwiftUI local state — RECOGNIZED with correct simple behavior predictions,
  including a fresh launch resetting the example counter. View implementation
  has not been assessed.
- Xcode — learner reports repeatedly executing the session's Swift snippets and
  supplied outputs matching the code's validation and model branches. Workflow
  and console were not directly observed.
- Git snapshots and branches — GUIDED. In a disposable repository, learner-reported
  terminal output covered initialization, untracked/staged/clean status, two
  commits on `main`, working versus cached diffs, creation of a branch with an
  uncommitted change, a branch-only third commit, decorated history, and reading
  files from each branch. Initially believed the new branch would point to the
  uncommitted version; corrected that branch names point only to commits.

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
- Classes/reference semantics, architecture, persistence, concurrency, formal
  tests, documentation use, and remaining advanced fundamentals — unassessed.

## Instructional implications

The eligibility/status and pass-store debugging labs are complete. Next assess a
small feature from behavioral requirements: `PassStore.addUses(id:amountText:)`,
including positive-integer validation before ID lookup, distinct results with
required data, stored mutation, and learner-designed tests. Supply no code skeleton
initially. Use this evidence to judge Phase 1 readiness; the guided debugging lab
alone does not establish independent feature implementation. Reassess optional
extraction, associated-value design, stored versus local values, collection
selection, assertion placement, and Git after meaningful spacing. Prioritize
behavior and state checks; exact event-status output was correct without repair.

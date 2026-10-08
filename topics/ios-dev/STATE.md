# STATE

Updated: 2026-10-09 session end — persistent shopping Add and Remove now return
success only after explicit saves. Learner-reported immediate relaunches retained
the added Eggs record and retained its later deletion. Persistent quantity editing
is assigned and unattempted.

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
  after explicit feedback. For `PassStore.addUses`, initially skipped the pre-code
  trace, returned the increment instead of the updated total, and tested only part
  of the matrix. After repeated requirement comparisons, completed the full
  result/state prediction and implementation; deriving automated checks still
  required a six-block outline and one supplied assertion example.
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
  to use the returned value rather than merely check it for `nil`. Later wrote
  `validAmount(amountText:) -> Int?` without a supplied skeleton, rejected failed
  conversion and nonpositive values, then bound and used the positive amount in
  `addUses`; learner-reported execution later passed invalid-text, zero, negative,
  success, unknown-ID, and validation-precedence assertions.
- Struct methods and mutation — GUIDED. After instruction on `mutating`, wrote and
  ran a `ShoppingList.add(_:)` method on a `var` instance and reported count `1`.
  Correctly implemented a read-only `containsItem` method, but initially created
  Milk without calling `add`, producing `false` for both searches before correction.
  Later independently declared `addUses` mutating and invoked it on a `var` store;
  learner-reported execution reached the final completion marker after all checks.
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
  exhaustive caller-side switch with exact predicted and reported output. For
  `addUses`, independently selected a three-case `AddResult` and exhaustively
  handled it, but initially carried the increment rather than the required updated
  total. After feedback, revised success to carry the ID and updated total, unknown
  failure to carry the ID, and used synthesized `Equatable` for result assertions.
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
  learner reported all checks passing. In the later `addUses` attempt, initially
  treated prints as checks, omitted cases, delayed assertions, changed the assigned
  ID, and omitted absent-key evidence. With a six-block outline and one complete
  assertion example, then wrote immediate result/state assertions for all six
  operations, including two `P404 == nil` checks; learner reported
  `All checks complete.` Independent test derivation remains open.
- Dictionaries — GUIDED. Can declare and mutate `[String: Int]`, distinguish
  insertion/update/removal, predict count changes after correction, assert lookup
  outcomes, and use `if let` for present/missing keys. Initially treated a present
  lookup as `Int` rather than `Int?` and attempted `Int(Int?)`, confusing optional
  extraction with text conversion. Also used a dictionary of `Account` structs and
  understands that keys, not values, must be unique.
  Independently combined a dictionary key predicate with Set membership for
  `canCheckIn`; changed to direct key lookup after a hint. Used dictionary-subscript
  mutation to repair `PassStore` after the local-copy bug was explained. Reused
  dictionary lookup and direct subscript mutation in `addUses` without repeating
  the local-copy mistake; learner-reported assertions verified the stored value and
  absence of an unknown key after both relevant failure paths.
- Sets — INDEPENDENT for membership checks in a small eligibility function.
  Correctly excluded already-checked-in IDs using `!checkedInIDs.contains(id)`
  without a supplied operation. Set construction/mutation remains assessed only
  through simple predictions and learner-reported runs.
- SwiftUI local state — INDEPENDENT for a small single-view counter implementation;
  GUIDED for the update/lifetime explanation. Independently selected `@State`,
  built and ran title/count/add/reset UI, made the property private, and reported
  two increments, reset, and a termination/relaunch reset. Needed explanation that
  the action closure mutates state, SwiftUI reevaluates `body`, and `@State` is not
  persistent storage. A wrong two-tap prediction came from reading "twice" as
  "once," not from believing two increments yield one.
- SwiftUI binding to a control — INDEPENDENT for narrow implementation and
  predictions; GUIDED conceptual explanation. Independently supplied `$name` to a
  `TextField`, ran it, and correctly predicted typing, clearing, and relaunch
  behavior. Initially described `name` and `$name` as separate wrapper values and
  hypothesized memory transfer between views. Instruction established that `name`
  is the `String` value, `$name` is a `Binding<String>` get/set connection to the
  same owner storage, and no custom child view is present. On 2026-09-29, correctly
  identified both types and the owner; the write-to-render sequence needed further
  explanation. Then correctly predicted that a button assigning `Guest` updates
  both the greeting and bound field, explaining their shared value. Later correctly
  chose bindings for name and quantity in a proposed child entry form and an action
  closure for Add, explaining that the parent remains the source of truth.
  On 2026-09-30, completed the child form and reported a successful build plus
  correct success/failure fields. Needed explicit correction that a binding is a
  connection to parent storage; supplied event traces support GUIDED explanation.
- SwiftUI draft versus accepted data — INDEPENDENT for selecting and explaining
  two private state properties and implementing the successful submission path;
  GUIDED for invalid-input behavior and verification. After feedback, placed both
  assignments inside a nonempty check. Initially still expected blank submission
  to clear both values; after tracing and adding a supplied character-count label,
  reported count 3 and `Last added: Bread` after a controlled three-space attempt.
  Observation accuracy and independent failure-path reasoning need further practice.
- SwiftUI model state and result-driven UI — GUIDED. Stored the supplied
  `ShoppingList` struct in private view-owned `@State`, bound two draft strings,
  derived the displayed count from `shoppingList.list.count`, called the model's
  Add method once, and handled all `AddResult` cases in the view. The first attempt
  replaced the required three-item setup with an empty array and inferred success
  from status text. After explicit feedback, restored the setup, switched directly
  on the enum, preserved drafts on all failures, and cleared them only in `.added`.
  Learner-reported rerun matched counts, messages, validation precedence, and draft
  state across two successes and three failures. Initially predicted that the final
  successful Oats submission would retain its drafts, then corrected the observation
  to empty fields; the source confirmed success-only clearing.
- SwiftUI collection rendering and identity — GUIDED. After an explanation of
  stable identity, correctly predicted that editing an item's name or quantity
  preserves its UUID while removal and recreation produces a new identity. Added
  a stored UUID through `Identifiable`, rendered the model array with `ForEach`,
  and learner-reported three initial rows, an appended Rice row after success,
  and unchanged rows after a duplicate failure. The row count and rows both read
  from the same model array.
- SwiftUI child views and upward actions — GUIDED. Extracted a read-only
  `ShoppingItemRow`, observed the compiler reject mutation of its `let` item, and
  explained that parent state change produces new child descriptions from current
  values. Then passed an `onRemove: () -> Void` action into each row; the child
  called it once while the parent invoked the model's Remove method, exhaustively
  handled the result, and retained ownership. The first pasted source omitted the
  button trigger despite reported results; after review, supplied source showing
  the button and single closure call.
- Xcode — learner reports repeatedly executing the session's Swift snippets and
  supplied outputs matching the code's validation and model branches. Workflow
  and console were not directly observed.
- SwiftUI navigation — GUIDED. Implemented NavigationStack, a row NavigationLink,
  item-derived destination titles, and a read-only detail value. Reported correct
  navigation, Back, and separate Remove behavior. Needed reminders for a missing
  heading and the reason for keeping interactive controls separate.
- Detail drafts and Save results — GUIDED. Selected local state after a prompt
  about leaving without saving. Implemented a String-taking, UpdateResult-returning
  Save closure through the parent, row, and detail after supplied syntax and a
  trace. Repaired passing-versus-calling confusion and reversed old/new bindings.
  Predicted and reported unchanged Milk after unsaved edits, Eggs updated 6 to 9,
  and rejected Bread/0 retaining 1. Independent closure wiring remains unassessed.
- Closure scope — GUIDED. Initially thought a parent-created Add closure reads a
  child's separate local draft. After a scope hint, identified the parent values.
  Needs retrieval without a supplied trace.
- Class reference semantics — GUIDED conceptual evidence. Initially applied struct
  copy reasoning to Counter class assignment. After instruction, correctly traced
  shared mutation and distinguished property mutation through a let reference from
  reference reassignment. On 2026-10-01, independently predicted shared versus
  separately constructed instances, then implemented and learner-reported running
  a class-based counter from scaffolded requirements. On 2026-10-06, correctly
  stated that a child `let` reference can call a mutating class method, but the
  precise distinction between reference reassignment, instance mutation, and a
  `private(set)` property was supplied by the tutor. Broader independent use
  remains unassessed.
- Observable-model bindings — GUIDED. Implemented an observable Profile with one
  parent-owned `@State` instance, a child `@Bindable` reference, direct TextField
  and Toggle bindings, and a parent Reset. Predictions and learner-reported actual
  results matched for child-to-parent and parent-to-child changes. The direction
  traces, lifetime explanation, and distinction between a plain `let`/`var` class
  reference and the binding projection required repeated supplied corrections.
  Ultimately stated that plain `var` still does not produce `$profile`, and that
  no second Profile is created.
- Persistence boundary and storage selection — GUIDED. Implemented a Bool
  `@AppStorage` preference, bound it to a Toggle, reset it, and learner-reported
  exact predicted results across first launch, mutation, relaunch, reset, and a
  second relaunch. The first source used the wrong persistent key, and explanations
  of default fallback, projected binding, and why record collections do not fit
  separate preference keys were supplied before the learner rewrote them. In an
  immediate recipe-app classification, independently selected `@State` for a
  temporary search, `@AppStorage` for a unit preference, and SwiftData for recipe
  records. Needed precision that `@State` follows view identity rather than the
  whole process lifetime and that SwiftData models are records, not query
  collections. Correctly answered a follow-up that three stored recipes mean three
  model instances and that `@Query` retrieves and observes them. Subsequently
  implemented an `@Model` record, app-scene persistent container, in-memory preview
  container, environment context inserts, and a sorted `@Query`. Learner-reported
  live query updates and a successful relaunch after adding explicit
  `modelContext.save()` calls with `do`/`catch`. Initially predicted insertion
  order instead of query sort order, omitted both container placements, and said
  `@Query` might own records; all were corrected with direct feedback. On
  2026-10-08, completed a controlled no-explicit-save PantryItem run in which two
  additional records survived relaunch, then built a shopping-item `@Model`,
  two-model app container, context-backed Add validation, and a sorted query.
  Correctly predicted validation precedence and draft behavior. Initially
  predicted repeated names would update and combine quantities rather than create
  records, then corrected that `insert` creates distinct records. In the shopping
  run, both rows appeared before termination but only Milk survived relaunch;
  distinguishing context visibility from stored data required direct instruction.
  On 2026-10-09, strengthened Add so `.added` follows only a successful explicit
  save, added rollback-backed failure handling, corrected the multi-model Preview,
  and learner-reported Eggs surviving an immediate relaunch. Then implemented a
  persistent row Remove with delete, explicit save, rollback-backed failure, and
  learner-reported immediate-relaunch evidence that Eggs remained deleted.
  Rollback reasoning, save/result ordering, bare view-state `name` versus the
  selected `item.name`, and capturing presentation data before deletion all
  required repeated guidance. Save-failure behavior was reasoned about but not
  executed.
- Git snapshots and branches — GUIDED. In a disposable repository, learner-reported
  terminal output covered initialization, untracked/staged/clean status, two
  commits on `main`, working versus cached diffs, creation of a branch with an
  uncommitted change, a branch-only third commit, decorated history, and reading
  files from each branch. Initially believed the new branch would point to the
  uncommitted version; corrected that branch names point only to commits.

## Current gaps and uncertainties

- Observable shared models — GUIDED. Converted `ShoppingList` to an observable
  final class, kept one parent-owned instance in private `@State`, passed it to an
  ordinary child `let`, and learner-reported matching parent/summary counts of
  `4/4`, `4/4`, and `3/3` across Add, rejected Add, and Remove. The learner first
  applied incorrect count arithmetic and later mixed the separate-instance
  hypothetical into the shared-instance table; after clarification, correctly
  recorded parent `4` versus summary `3` for two separately constructed models.
  Independent ownership selection remains unassessed.
- Writable control bindings to an observable model — GUIDED. The Profile lab used
  `@Bindable` correctly and produced matching child-to-parent and parent-to-child
  behavior. Independent explanation remains weak: the learner repeatedly merged
  reference mutability with binding projection and binding reads/writes with
  Observation-driven view reevaluation.
- Structured persistence — GUIDED. A controlled PantryItem run showed autosaved
  records surviving relaunch, while an earlier shopping run showed that query
  visibility alone did not prove durability. Persistent shopping Add and Remove
  now use explicit saves, return success only after saving, and roll back their
  isolated mutation on a thrown save. Learner-reported immediate relaunches
  retrieved the added Eggs record and later confirmed its saved deletion. The
  learner can state the context/store boundary after correction, but operation
  ordering, rollback results, variable scope, and pre-deletion value capture
  needed repeated scaffolding. The failure paths have not been executed. Quantity
  editing is assigned but unattempted.
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
- Architecture beyond the current view, concurrency, formal tests, independent
  documentation use, and remaining advanced fundamentals — unassessed.

## Instructional implications

Continue `labs/2026-10-09-swiftdata-persistent-quantity-edit.md`, beginning with
the unattempted ownership, result-design, operation-trace, and prediction sections.
Then migrate quantity editing with validation before mutation, captured old/new
result data, explicit save, and isolated rollback on save failure. Keep query
visibility, pending context changes, completed saves, store contents, and
new-context retrieval conceptually separate. Require the learner to compare every
implementation against each stated requirement before reporting readiness.
Revisit `@State` versus `@AppStorage` after spacing using a new scenario.
After spacing, reassess `@Bindable` with an unfamiliar model and control without
supplying the setter/getter trace. Use short traces when closure inputs, outputs,
or scope are unclear, then reduce the scaffolding.
Treat harmless naming and visual-formatting choices proportionally. Require exact
formatting only when presentation or exact-output compliance is the learning
target; preserve earlier predictions and observations when correcting a lab.
Keep requirement tracing and automated verification active: after spacing,
assign an unfamiliar feature without a supplied matrix or assertion structure.
Reassess associated-value design, assertion placement, value semantics, and Git
after meaningful spacing.

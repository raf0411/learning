# SwiftData explicit-save Add

## Session target

Strengthen the persistent shopping Add contract:

> Report `.added` only after `ModelContext.save()` completes without throwing.

This continues **Implementation 2** from
`2026-10-08-swiftdata-shopping-integration-probe.md`.

## Opening retrieval

### Original answers

1. What does an item appearing through `@Query` after `insert` prove?

   > it proves that theres a new item inserted and the swift ui can retrieve that changes from Query

2. What does the item appearing after stopping and relaunching prove?

   > it proves that it is saved to the local storage with the modelContext.save()

### Tutor assessment

- Answer 1 has the correct boundary: the insertion is visible in the current
  model context and `@Query` observed that change. This alone does not establish
  durable storage.
- Answer 2 reaches the correct persistence conclusion: a newly created context
  retrieved the record from the persistent store. Attribute that result to the
  explicit `modelContext.save()` only when that save actually completed in the
  controlled code path.

Refine answer 2 in one sentence:

> It proves that a new context retrieved the record from persistent storage.

## Predict before editing or running

Begin with the currently persisted `Milk: 5` record. Do not clear the store.

| Moment                                                | Predicted stored rows                    | Predicted status           | What supports the prediction? |
| ----------------------------------------------------- | ---------------------------------------- | -------------------------- | ----------------------------- |
| Relaunch before adding                                | Milk - quantity: 5                       | Ready to add an item.      | modelContainer                |
| Add `Eggs` / `6` and see the result                   | Eggs - quantity: 6<br>Milk - quantity: 5 | Added Eggs with quantity 6 | insert                        |
| Stop immediately after success appears, then relaunch | Eggs - quantity: 6<br>Milk - quantity: 5 | Ready to add an item.      | save                          |

Why will `.added` be stronger evidence than it was in the autosave version?

>The important strength of `.added` is not merely that the source contains a
  `save()` call. It is that this result is reachable only after `save()` returns
  without throwing.

## Implementation

Change only these four areas in the existing source. Paste the completed changed
snippets below; do not paste the entire project.

### 1. `AddResult`

Add one result for a failed save. It must carry the cleaned item name.

```swift
enum AddResult {
    case added(name: String, quantity: Int)
    case emptyName
    case duplicateName(name: String)
    case invalidQuantity
    case failed(name: String)
}
```

### 2. Add method

Keep the existing validation order. After creating and inserting the new item:

- explicitly save inside `do`/`catch`;
- return `.added` only after `save()` succeeds;
- on an error, roll back before returning the save-failure result.

For this isolated Add-only screen, no other unsaved edit should be pending when
`rollback()` is used.

```swift
    func add(name: String, quantityText: String, modelContext: ModelContext) -> AddResult {
        let cleanName = name.trimmingCharacters(in: .whitespacesAndNewlines)
        
        guard !cleanName.isEmpty else {
            return AddResult.emptyName
        }
        
        let isDuplicate = items.contains { item in
            item.name == cleanName
        }
        
        guard !isDuplicate else {
            return AddResult.duplicateName(name: cleanName)
        }
        
        guard let quantity = validNumber(number: quantityText) else {
            return AddResult.invalidQuantity
        }
        
        let newItem = ShoppingItem(name: cleanName, quantity: quantity)
        modelContext.insert(newItem)
        
        do {
            try modelContext.save()
            print("✅ \(name) saved successfull!")
            return AddResult.added(name: cleanName, quantity: quantity)
        } catch {
            modelContext.rollback()
            print("❌ \(name) failed!")
            return AddResult.failed(name: cleanName)
        }
    }
```

### 3. Result-handling switch

Handle every `AddResult`. On save failure:

- show a clear failure status containing the cleaned name;
- preserve both drafts.

```swift
switch result {
	case .added(let name, let quantity):
		status = "Added \(name) with quantity \(quantity)."
		self.name = ""
		self.quantity = ""
	case .emptyName:
		status = "Name cannot be empty."
	case .duplicateName(let name):
		status = "\(name) already exists."
	case .invalidQuantity:
		status = "Quantity must be a positive whole number."
	case .failed(let name):
		status = "Failed to add \(name)"
}
```

### 4. Preview

Make the in-memory Preview container use both `PantryItem` and `ShoppingItem`.

```swift
#Preview {
    PersistentShoppingView()
        .modelContainer(for: [PantryItem.self, ShoppingItem.self], inMemory: true)
        .preferredColorScheme(.dark)
}
```

## Run and record

Run the exact sequence predicted above without changing the source between
moments.

| Moment                                                | Actual stored rows                       | Actual status              | Actual drafts |
| ----------------------------------------------------- | ---------------------------------------- | -------------------------- | ------------- |
| Relaunch before adding                                | Milk - quantity: 5                       | Ready to add an item.      | ""/""         |
| Add `Eggs` / `6` and see the result                   | Eggs - quantity: 6<br>Milk - quantity: 5 | Added Eggs with quantity 6 | ""/""         |
| Stop immediately after success appears, then relaunch | Eggs - quantity: 6<br>Milk - quantity: 5 | Ready to add an item.      | ""/""         |

Compiler, runtime, or save error, if any:

> TODO: none

## Final explanation

Complete this flow using a short phrase for what each step establishes:

```text
insert
  -> inserts a new item to the current context
save succeeds
  -> successfully save to the persistent store
query displays the item
  -> retrieves and observes items from the current context visbillity
stop and relaunch; new query displays the item
  -> retrieves new context after relaunch and display new items if there is one
```

When every `TODO` is complete, tell the tutor the worksheet is ready.

## Tutor review 1

### What is correct

- All three predicted row sets and statuses match the intended successful-save
  path.
- `AddResult.failed` carries the cleaned name when it is constructed.
- The method inserts, attempts `save()`, returns `.added` only after the save
  succeeds, and rolls back before returning failure.
- The result switch is exhaustive. Only `.added` clears the drafts, so the
  failure path preserves them.
- The Preview now configures both model types.
- The reported immediate-relaunch result supports that Eggs reached persistent
  storage. The save-failure branch compiled but was not executed, so its runtime
  behavior has not been directly observed.

### Revisions needed

The prediction evidence column is unfinished. Also, the final flow currently
places `insert` and `@Query` too close to the persistent store:

- `insert` registers the new model in the current model context. It does not by
  itself prove that the persistent store changed.
- `@Query` exposes models from the current SwiftData context and can reflect an
  unsaved insertion. A displayed row therefore does not prove persistence.
- The important strength of `.added` is not merely that the source contains a
  `save()` call. It is that this result is reachable only after `save()` returns
  without throwing.
- After relaunch, retrieval through a newly created context is the independent
  observation that the saved record is durable.

Revise the following without changing the original prediction values or code:

1. Fill all three `What supports the prediction?` cells.
2. Expand the `.added` explanation to describe its control-flow guarantee.
3. Record both draft fields as `"" / ""` in each Actual row, if both were empty.
4. Rewrite the four final-flow phrases using these distinct locations/events:
   current context, successful save to the persistent store, current-context
   query visibility, and new-context retrieval after relaunch.

When these revisions are complete, tell the tutor the worksheet is ready again.

## Tutor review 2

The implementation and successful run are complete. The revised `.added`
explanation now states the important control-flow guarantee: `.added` is reachable
only after `save()` returns without throwing. Both drafts are also recorded.

The first three final-flow phrases now distinguish insertion, saving, and query
visibility well enough for this guided exercise. One direction needs correction:
a query does not retrieve a new context. After relaunch, the app's data stack
supplies a new context, and the new query uses that context to fetch records from
the persistent store. Seeing Eggs then is independent evidence that it was
durable.

The evidence-column labels remain abbreviated. In particular, `insert` explains
why the current context and query can expose Eggs, while the successful-save
control path explains the `.added` status and supports the prediction that Eggs
will survive relaunch.

Assessment: explicit-save Add implementation — complete with guidance. Persistence
boundary explanation — GUIDED; verify next with a save-failure transfer scenario.

## Save-failure transfer check

Scenario: the store contains only `Milk: 5`. The learner enters `Rice` / `2`.
Insertion succeeds, `save()` throws, and the catch path rolls back before
returning `.failed`.

### Learner answer

> Milk - quantity: 5  
> Failed to add Rice.  
> Drafts: Rice/2
>
> Because it fails to reach save(), it will call rollback() which will cancel the
> insert that happened previously.

### Tutor assessment

The predicted rows, failure status, and preserved drafts are correct immediately
after the handler and after relaunch. One wording correction: `save()` is reached
and called; it throws instead of completing successfully. `rollback()` then
discards the pending insertion, so Rice is absent from both the current context
and the later relaunched context.

This establishes a guided distinction among pending insertion, failed save,
rollback, current-context state, and relaunch retrieval.

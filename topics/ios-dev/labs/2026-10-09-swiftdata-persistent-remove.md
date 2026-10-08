# SwiftData persistent Remove

## Purpose

Migrate one more shopping action from the old in-memory array to SwiftData:
delete the selected persistent record and report success only after an explicit
save succeeds.

Do not migrate quantity editing or navigation yet.

## Foundation

For this isolated screen:

```text
modelContext.delete(item)
  -> marks the model for deletion in the current context

try modelContext.save()
  -> commits the pending deletion to the persistent store

modelContext.rollback()
  -> discards the unsaved deletion if saving throws
```

As with insertion, a current query can change before durable storage has been
verified.

## Part 1 — Design probe

The Remove button is created inside `ForEach(items)` and therefore already has
the selected `ShoppingItem` model instance.

1. Why can the Remove action pass that item directly instead of searching again
   by name?

   > because in the ForEach we are looping the item, which already can be passed directly to remove()

2. Design a finite result type for these two outcomes:

   - deletion saved successfully; carry the deleted item's name;
   - saving failed; carry the attempted item's name.

   Use a new name such as `PersistentRemoveResult` so the disconnected legacy
   `RemoveResult` does not need to change.

```swift
enum PersistentRemoveResult {
    case removed(name: String)
    case failed(name: String)
}
```

3. Complete the operation order. Include the return point for each result.

```text
receive selected item
  -> call delete()
  -> validate remove
  -> success: call save()
  -> failure: call rollback()
```

## Part 2 — Predict before implementation

Begin with the currently persisted, name-sorted records `Eggs: 6` and `Milk: 5`.

Use these statuses:

- success: `Removed NAME.`
- save failure: `Failed to remove NAME.`

| Moment                                     | Predicted rows                           | Predicted status      | Why?                                                                      |
| ------------------------------------------ | ---------------------------------------- | --------------------- | ------------------------------------------------------------------------- |
| Relaunch before removal                    | Eggs - quantity: 6<br>Milk - quantity: 5 | Ready to add an item. | Nothing is happened yet, and the milk was saved from the previous context |
| Tap Remove beside Eggs and receive success | Milk - quantity: 5                       | Removed Eggs.         | Because the removal was successful and returns .removed                   |
| Stop immediately and relaunch              | Milk - quantity: 5                       | Ready to add an item. | Because the context previously was saved during remove()                  |

### Failure-path reasoning

Assume deletion of Eggs is requested, `save()` throws, and the catch path rolls
back. No actual failure run is required yet.

| Moment                         | Predicted rows                           | Predicted status       | Why?                                           |
| ------------------------------ | ---------------------------------------- | ---------------------- | ---------------------------------------------- |
| After the handler finishes     | Eggs - quantity: 6<br>Milk - quantity: 5 | Failed to remove Eggs. | Because the removal failed and returns .failed |
| After stopping and relaunching | Eggs - quantity: 6<br>Milk - quantity: 5 | Ready to add an item.  | The data will be the same as before            |

Complete Parts 1 and 2 before changing the Xcode source. Then tell the tutor the
worksheet is ready for review.

## Tutor review 1

### Correct

- `ForEach(items)` already gives the button the selected `ShoppingItem`, so a
  second name-based search is unnecessary.
- The initial, successful-removal, and successful immediate-relaunch row/status
  predictions are correct.
- The proposed enum distinguishes saved deletion from save failure and carries
  the attempted name in both paths.

### Revise before implementation

1. The requested success result needs only the deleted name. Remove the unneeded
   `remainingCount` associated value; the visible count already comes from the
   query.
2. The operation order is missing `save()` and `rollback()`. There is no separate
   input-validation step because the action already receives the selected stored
   model. Capture the item's name before deleting it, then account for both the
   throwing save path and its catch path.
3. Both failure-path row predictions are incorrect. `rollback()` discards the
   unsaved deletion, so the record set must return to its pre-attempt state. Your
   phrase “same as before” should agree with the rows you list.

Revise only the enum, operation-order trace, and two failure rows. Do not change
the Xcode source yet. Then tell the tutor the worksheet is ready again.

## Tutor review 2

The result enum and both failure-path predictions are now correct. Rollback
restores Eggs in the current context, and because no deletion was committed, a
later context retrieves both Eggs and Milk.

The operation trace is not yet correct: `validate remove` should be absent, and
calling a throwing `save()` does not itself establish success. Replace that trace
with the following structure and fill every blank:

```text
receive selected item
  -> capture remove() before deletion
  -> mark delete() in the current context
  -> do:
       try save()
       return .removed
  -> catch:
       rollback()
       return .failed
```

Do not change the Xcode source yet. Tell the tutor when this one trace is ready.

## Tutor review 3

The `do`/`catch` branch order is correct. The captured value was not: `remove()`
is an operation, while both result cases require the selected item's name.

The completed data flow is:

```text
receive selected item
  -> capture item.name before deletion
  -> mark the item for deletion in the current context
  -> do:
       try to save the context
       return .removed(name: capturedName)
  -> catch:
       roll back the context
       return .failed(name: capturedName)
```

Capturing the name before deletion also avoids depending on a deleted model to
provide presentation data afterward.

## Part 3 — Implement

Keep the existing persistent Add behavior unchanged.

### A. Remove method

Write this method in `PersistentShoppingView`:

```swift
func remove(
    item: ShoppingItem,
    modelContext: ModelContext
) -> PersistentRemoveResult {
	modelContext.delete(item)
	
	do {
		try modelContext.save()
		print("✅ \(name) removed successfull!")
		return PersistentRemoveResult.removed(name: item.name)
	} catch {
		modelContext.rollback()
		print("❌ \(name) failed!")
		return PersistentRemoveResult.failed(name: item.name)
	}
}
```

Requirements:

- capture the selected name before deletion;
- delete the supplied item through the context;
- explicitly save inside `do`/`catch`;
- return `.removed` only after saving succeeds;
- on a thrown save, roll back before returning `.failed`.

Paste the completed method:

```swift
func remove(item: ShoppingItem, modelContext: ModelContext) -> PersistentRemoveResult {
	modelContext.delete(item)
	
	do {
		try modelContext.save()
		print("✅ \(name) removed successfull!")
		return PersistentRemoveResult.removed(name: item.name)
	} catch {
		modelContext.rollback()
		print("❌ \(name) failed!")
		return PersistentRemoveResult.failed(name: item.name)
	}
}
```

### B. Row action and result handling

For each queried item, preserve the existing row text and add a Remove button.
The button must:

1. call the Remove method once with that exact row's item;
2. switch exhaustively on its result;
3. show `Removed NAME.` after success;
4. show `Failed to remove NAME.` after save failure.

Paste only the changed `ForEach` block:

```swift
ForEach(items, id: \.self) { item in
	HStack {
		Text("\(item.name) - quantity: \(item.quantity)")
		
		Button("Remove", action: {
			let result = remove(item: item, modelContext: modelContext)
			
			switch result {
			case .removed(let name):
				status = "Removed \(name)."
			case .failed(let name):
				status = "Failed to remove \(name)."
			}
		})
		.buttonStyle(.borderedProminent)
	}
}
```

## Part 4 — Run the successful path

Start with Eggs and Milk still stored. Do not change the source during the run.

| Moment                        | Actual rows                              | Actual status         |
| ----------------------------- | ---------------------------------------- | --------------------- |
| Relaunch before removal       | Eggs - quantity: 6<br>Milk - quantity: 5 | Ready to add an item. |
| Tap Remove beside Eggs        | Milk - quantity: 5                       | Removed Eggs.         |
| Stop immediately and relaunch | Milk - quantity: 5                       | Ready to add an item. |

Compiler/runtime/save error, if any:

> TODO: none

After implementing and recording the run, tell the tutor the worksheet is ready.

## Tutor review 4

### Verified

- The button passes its exact queried row item and calls Remove once.
- The result switch is exhaustive and produces the required statuses.
- The reported UI transitioned from Eggs/Milk to Milk.
- Milk alone remained after immediate relaunch, supporting that the explicit save
  committed the deletion to the persistent store.

### Method correction required

The method does not capture `item.name` before deletion as required. Both result
returns still read through `item` after the delete/save attempt.

There is also a scope distinction in the diagnostic prints:

```swift
name       // the PersistentShoppingView Add-draft state
item.name  // the name of the selected stored row
```

If the Add name draft is empty and the selected row is Eggs, determine what each
of those expressions contains before editing the method. Then replace every
post-deletion dependency on `item.name` with one local name captured before
`modelContext.delete(item)`. The diagnostic prints are optional and may be
removed.

- Add name draft is empty : name = ""
- selected row is Eggs : item.name = "Eggs"

No persistence rerun is required; the existing successful relaunch observation
remains valid. Paste the corrected method beneath this review:

```swift
func remove(
	item: ShoppingItem,
	modelContext: ModelContext
) -> PersistentRemoveResult {
	let selectedName = item.name
	modelContext.delete(item)
	do {
		try modelContext.save()
		print("✅ \(selectedName) removed successfull!")
		return PersistentRemoveResult.removed(name: selectedName)
	} catch {
		modelContext.rollback()
		print("❌ \(selectedName) failed!")
		return PersistentRemoveResult.failed(name: selectedName)
	}
}
```

## Tutor review 5

The scope distinction is correct, but the method still does not perform the
requested capture. Make these exact mechanical changes in Xcode and in the method
immediately above:

1. Immediately before `modelContext.delete(item)`, add:

   ```swift
   let selectedName = item.name
   ```

2. After that line, do not read `item.name` again. Use `selectedName` in both
   associated-value returns.
3. Remove the two optional print statements, or use `selectedName` in them as
   well. Do not use the view's bare `name` property.

Build once after the edit. No data mutation or persistence rerun is needed.

## Tutor review 6

The local capture and diagnostic prints are corrected. Make the final two
substitutions:

```swift
return PersistentRemoveResult.removed(name: selectedName)
```

```swift
return PersistentRemoveResult.failed(name: selectedName)
```

After `modelContext.delete(item)`, there should be zero remaining occurrences of
`item.name` in this method. Build once and report the result.

## Completion checkpoint

Learner reported that the final corrected method built successfully. Persistent
Remove is complete with guidance:

- the exact queried model is passed to the action;
- presentation data is captured before deletion;
- `.removed` follows only a successful explicit save;
- the catch path rolls back before returning failure;
- the successful deletion remained absent after immediate relaunch.

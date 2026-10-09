# SwiftData persistent quantity editing — design probe

## Purpose

Plan the smallest migration of quantity editing from the disconnected in-memory
shopping path to the active SwiftData path.

Do not change the Xcode source yet.

Current persistent state: `Milk: 5`. Eggs was successfully deleted and that
deletion survived relaunch.

## Intended interaction

Each persistent row will eventually have a small child editor containing:

- the current item display;
- a local quantity text draft;
- a Save button;
- feedback from the Save attempt.

Typing must change only the local draft. When Save receives a valid positive
whole number, the action updates the existing model's quantity in the context,
then attempts to save. Report success only after saving succeeds; if saving
throws, roll back the pending change before returning failure. For this exercise,
assume the context has no other pending changes.

## Part 1 — Ownership and interface

For each value below, choose its owner and mechanism. Use descriptions such as
the queried `ShoppingItem`, child-local `@State`, or a parent-created action.

| Value or operation                                    | Owner/mechanism          | Why?                                                                                                                                                                                                                      |
| ----------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Accepted item quantity                                | the queried ShoppingItem | because this comes from the local quantity text draft that is already accepted and already became a ShoppingItem                                                                                                          |
| Unsaved quantity text                                 | child-local @State       | this could be the local quantity text draft that is still unsaved                                                                                                                                                         |
| Operation that changes and saves the persistent model | parent-created action    | because the one that is gonna do the operation is the parent, the one who has the context                                                                                                                                 |
| Feedback for one row's latest Save attempt            | child-local @State       | Each editor needs its own latest result. A single parent status string would share feedback across rows. Parent ownership could work with feedback tracked separately per item, but that adds unnecessary machinery here. |

The child must request a save using its draft and receive a finite result. Write
the action's function type only—do not implement it yet:

```swift
let onSaveQuantity: (String) -> PersistentUpdateResult
```

## Part 2 — Result design

Design `PersistentUpdateResult` for exactly these outcomes:

1. update saved successfully; carry name, old quantity, and new quantity;
2. draft is not a positive whole number;
3. context save failed; carry the item name.

Because the action receives an exact queried item, do not add empty-name or
not-found cases.

```swift
enum PersistentUpdateResult {
	case updated(name: String, oldQuantity: Int, newQuantity: Int)
	case invalidQuantity
	case failed(name: String)
}
```

Why are empty-name and not-found results unnecessary in this interface?

> Because we are not checking / validating for the name, we just editing the quantity, and also not found is not necessary because we are directly editing it through the ForEach list, which user can only edit the ones that are available

## Part 3 — Operation trace

Complete the trace. Validation must finish before the persistent model is
changed. Capture presentation/result data before mutation.

```text
receive selected item and quantity text
  -> convert and validate quantity text
  -> if quantity <= 0: .invalidQuantity
  -> capture item name and oldQuantity
  -> change current quantity
  -> do:
	   save()
       .updated
  -> catch:
       rollback()
	   .failed
```

## Part 4 — Predict before implementation

Assume `Milk: 5` is stored, the row's draft begins empty, and success clears the
draft while either failure preserves it.

| Moment                        | Displayed stored quantity | Draft | Feedback                                  | Why?                                                                                      |
| ----------------------------- | ------------------------: | ----- | ----------------------------------------- | ----------------------------------------------------------------------------------------- |
| Relaunch                      |        Milk - quantity: 5 | ""    | No update attempted.                      | Because we are not updating anything yet from the start                                   |
| Type `9`, before Save         |        Milk - quantity: 5 | 9     | No update attempted.                      | We haven't click save yet                                                                 |
| Tap Save and receive success  |        Milk - quantity: 9 | ""    | Updated milk from 5 to 9.                 | Because it returns updated, which means the editing quantity was successful               |
| Stop immediately and relaunch |        Milk - quantity: 9 | ""    | No update attempted.                      | Because the editing was successful, it was save() to the context and survive the relaunch |
| Type `0` and tap Save         |        Milk - quantity: 9 | 0     | Quantity must be a positive whole number. | because it returns .invalidQuantity                                                       |

Use these feedback messages:

- initial: `No update attempted.`
- success: `Updated NAME from OLD to NEW.`
- invalid: `Quantity must be a positive whole number.`
- save failure: `Failed to update NAME.`

Complete all four parts before changing Xcode, then tell the tutor the worksheet
is ready for review.

## Part 5 — Implement the parent update method

The design review is complete with guidance. In chat, you identified that text
must be converted to a number before checking whether it is above zero.
Precision: `Int("abc")` returns `nil`; reject failed conversion as well as
nonpositive integers. The existing `ShoppingItem` receives the quantity update;
the draft does not become a new item.

You may now edit Xcode. Add your `PersistentUpdateResult` enum and implement this
method in `PersistentShoppingView`, following the explicit-context parameter
style used in your Add and Remove methods:

```swift
func updateQuantity(item: ShoppingItem, quantityText: String, modelContext: ModelContext) -> PersistentUpdateResult {
	
	guard let quantity = validNumber(number: quantityText) else {
		return PersistentUpdateResult.invalidQuantity
	}
	
	let name = item.name
	let oldQuantity = item.quantity
	
	item.quantity = quantity
	
	do {
		try modelContext.save()
		return PersistentUpdateResult.updated(name: name, oldQuantity: oldQuantity, newQuantity: quantity)
	} catch {
		modelContext.rollback()
		return PersistentUpdateResult.failed(name: name)
	}
}
```

Required behavior:

- Failed integer conversion, zero, and negative values return `.invalidQuantity`
  without changing the item.
- Valid input updates the supplied existing item. Preserve its name and old
  quantity for the result.
- Return `.updated` with the name, old quantity, and new quantity only after an
  explicit save succeeds.
- If saving throws, roll back before returning `.failed` with the name. Assume
  there are no unrelated pending changes in this context.

Implement only this method and the enum for now; the child editor comes next.
Build the app, then paste your method below and record the actual build result.
A successful build checks compilation, not runtime persistence behavior.

### Your implementation

```swift
enum PersistentUpdateResult {
    case updated(name: String, oldQuantity: Int, newQuantity: Int)
    case invalidQuantity
    case failed(name: String)
}

func updateQuantity(item: ShoppingItem, quantityText: String, modelContext: ModelContext) -> PersistentUpdateResult {
	
	guard let quantity = validNumber(number: quantityText) else {
		return PersistentUpdateResult.invalidQuantity
	}
	
	let name = item.name
	let oldQuantity = item.quantity

	item.quantity = quantity
	
	do {
		try modelContext.save()
		return PersistentUpdateResult.updated(name: name, oldQuantity: oldQuantity, newQuantity: quantity)
	} catch {
		modelContext.rollback()
		return PersistentUpdateResult.failed(name: name)
	}
}

private func validNumber(number: String) -> Int? {
	if let num = Int(number) {
		if num > 0 {
			return num
		}
	}
	
	return nil
}
```

### Build result

TODO: success

## Part 6 — Connect a child quantity editor

Part 5 review: the revised method validates before mutation, captures the name
and old quantity, assigns the new quantity, saves before returning success, and
rolls back before returning failure. Build success is learner-reported; runtime
behavior has not yet been tested.

Create a SwiftUI child view named `PersistentQuantityEditor` and connect one
editor to each item in the parent's existing `ForEach(items)`.

### Requirements

- Receive the existing `ShoppingItem` for display and an `onSaveQuantity` action
  with the function type you designed in Part 1.
- Display the item's name and current model quantity.
- Own an initially empty quantity text draft and feedback initially set to
  `No update attempted.` Use the ownership choices from Part 1.
- Provide a TextField for the draft and a Save button. Typing changes only the
  draft, not `item.quantity`.
- On Save, call `onSaveQuantity` once with the draft and handle all three result
  cases. Use the feedback messages from Part 4. Clear the draft only on success;
  preserve it on either failure.
- In the parent, supply an action that passes the selected row's item, the text
  received from the child, and the parent's context to `updateQuantity`, then
  returns its result to the child.
- Keep the existing Add and Remove controls working. The child delegates the
  persistent update to its action.

Implement in Xcode and build. Paste the complete child view and the parent's
updated `ForEach` below. We will review the connection before the runtime tests.
If blocked, include your attempt and the exact diagnostic.

### Child view

```swift
struct PersistentShoppingRow: View {
    let item: ShoppingItem
    let onSaveQuantity: (String) -> PersistentUpdateResult
    let onRemoveItem: () -> Void
    
    @State private var quantityDraft: String = ""
    @State private var feedback: String = "No update attempted."

    var body: some View {
        VStack {
            HStack {
                Text("\(item.name) - quantity: \(item.quantity)")
                
                TextField("Edit Quantity", text: $quantityDraft)
                
                Button("Save", action: {
                    let result = onSaveQuantity(quantityDraft)
                    
                    switch result {
                    case .updated(let name, let oldQuantity, let newQuantity):
                        feedback = "Updated \(name) from \(oldQuantity) to \(newQuantity)."
                        quantityDraft = ""
                    case .invalidQuantity:
                        feedback = "Quantity must be a positive whole number."
                    case .failed(let name):
                        feedback = "Failed to update \(name)."
                    }
                })
                
                Button("Remove", action: {
                    onRemoveItem()
                })
                .buttonStyle(.borderedProminent)
            }
            
            Text(feedback)
        }
    }
}
```

### Parent ForEach and action connection

```swift
struct PersistentShoppingView: View {
    @Environment(\.modelContext) private var modelContext
    @Query(sort: \ShoppingItem.name) private var items: [ShoppingItem]
    
    @State private var name: String = ""
    @State private var quantity: String = ""
    @State private var status: String = "Ready to add an item."
    
    var body: some View {
        VStack {
            Text("Items: \(items.count)")
            
            ForEach(items, id: \.self) { item in
                PersistentShoppingRow(
                    item: item,
                    onSaveQuantity: { quantityDraft in
                        updateQuantity(item: item, quantityText: quantityDraft, modelContext: modelContext)
                    },
                    onRemoveItem: {
                        let result = remove(item: item, modelContext: modelContext)
                        
                        switch result {
                        case .removed(let name):
                            status = "Removed \(name)."
                        case .failed(let name):
                            status = "Failed to remove \(name)."
                        }
                    }
                )
            }
            
            ShoppingEntryForm(
                name: $name,
                quantity: $quantity,
                onAdd: {
                    let result = add(name: name, quantityText: quantity, modelContext: modelContext)
                    
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
            })
            
            Text(status)
        }
    }
    
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
    
    func updateQuantity(item: ShoppingItem, quantityText: String, modelContext: ModelContext) -> PersistentUpdateResult {
        
        guard let quantity = validNumber(number: quantityText) else {
            return PersistentUpdateResult.invalidQuantity
        }
        
        let name = item.name
        let oldQuantity = item.quantity
    
        item.quantity = quantity
        
        do {
            try modelContext.save()
            return PersistentUpdateResult.updated(name: name, oldQuantity: oldQuantity, newQuantity: quantity)
        } catch {
            modelContext.rollback()
            return PersistentUpdateResult.failed(name: name)
        }
    }
    
    private func validNumber(number: String) -> Int? {
        if let num = Int(number) {
            if num > 0 {
                return num
            }
        }
        
        return nil
    }
}
```

### Build result

Succeeded

## Part 7 — Verify the connected editor

Review of Part 6: the row owns its draft and feedback, calls the Save action once,
and handles all results. The parent passes the correct item, child-supplied text,
and context. The success branch still needs to clear the draft; preserve the
draft in both failure branches. Make that correction in Xcode and update the
child-view code above. Mark the row's internal state properties `private` too.

### Setup

Launch the app and record Milk's actual quantity before testing. Use a positive
target quantity different from that starting value (for example, 9 if it is 5).
Do not assume the earlier stored value is still current.

- Starting quantity: 5
- Target quantity: 9

Use Part 4's predictions as your starting point. If your setup differs, note the
adjusted expected quantities here without overwriting the original predictions:

> TODO: "Original setup still matches."

### Run in order

Replace the entire draft for each invalid-input test. Record observations, not
what the code is supposed to do. For each failure, inspect both the displayed
model quantity and the text still in the field.

| Action                                | Actual displayed quantity | Actual draft | Actual row feedback                       |
| ------------------------------------- | ------------------------- | ------------ | ----------------------------------------- |
| Fresh launch                          | Milk - quantity: 5        | ""           | No update attempted.                      |
| Type the target quantity, before Save | Milk - quantity: 5        | 9            | No update attempted.                      |
| Tap Save                              | Milk - quantity: 9        | ""           | Updated Milk from 5 to 9.                 |
| Stop immediately, then relaunch       | Milk - quantity: 9        | ""           | No update attempted.                      |
| Replace draft with `abc`, tap Save    | Milk - quantity: 9        | abc          | Quantity must be a positive whole number. |
| Replace draft with `0`, tap Save      | Milk - quantity: 9        | 0            | Quantity must be a positive whole number. |
| Replace draft with `-2`, tap Save     | Milk - quantity: 9        | -2           | Quantity must be a positive whole number. |
| Empty the draft, tap Save             | Milk - quantity: 9        | ""           | Quantity must be a positive whole number. |

These tests cover successful persistence and rejected input. They do not execute
a throwing context save; the rollback path remains supported by code review only.

Any mismatch or unexpected behavior:

> TODO: "None observed."

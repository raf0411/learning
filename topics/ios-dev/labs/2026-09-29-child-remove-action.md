# Send a row action to the parent

## Learning target

Let a child row report a button tap while `ContentView` keeps ownership of and
mutation authority over `ShoppingList`.

## Initial reasoning

Prompt: What could `ShoppingItemRow` receive so its Remove button can tell the
parent to remove the item without owning the list?

Initial answer:

> my guess is a binded shoppingList.list same value from the parent?

A binding is a read/write connection and is useful when a child genuinely needs
to edit parent-owned state. This row only needs to send one event. Giving it a
binding to the array would expose broader mutation and work against the model's
`private(set)` boundary.

Use an action closure instead:

```text
ShoppingItemRow button tap
             |
             | calls onRemove()
             v
ContentView closure
             |
             | calls ShoppingList.remove(...)
             v
Parent @State changes -> body reevaluates -> row disappears
```

A no-argument action has the type `() -> Void`:

```swift
let onRemove: () -> Void
```

The child can call it without knowing how removal works. The parent supplies the
actual work when it creates each row.

## Build the event path

Update the current app:

1. Give `ShoppingItemRow` a stored `onRemove: () -> Void` closure.
2. Add a Remove button to the row and call `onRemove()` exactly once from its
   action.
3. Keep the child free of `ShoppingList`, `@State`, and `@Binding`.
4. In the parent's `ForEach`, pass a closure for the current item.
5. That parent closure must call `shoppingList.remove(name:)` exactly once.
6. Exhaustively switch on `RemoveResult` and update the existing status text:
   - removed: `Removed NAME. COUNT items remain.`
   - not found: `NAME was not found.`
   - empty name: `Name cannot be empty.`
7. Keep the count and rows derived from `shoppingList.list`.

Paste the revised child and parent `ForEach`:

```swift
struct ShoppingItemRow: View {
    let item: ShoppingItem
    
    let onRemove: () -> Void
    
    var body: some View {
        HStack {
            Text("\(item.name) — quantity: \(item.quantity)")
            Button("Remove", action: {
                onRemove()
            })
        }
    }
}

ForEach(shoppingList.list) { item in
	ShoppingItemRow(
		item: item,
		onRemove: {
			let result = shoppingList.remove(name: item.name)
			
			switch result {
			case .removed(let name, let remainingCount):
				status = "Removed \(name). \(remainingCount) items remain."
			case .emptyName:
				status = "Name cannot be empty."
			case .notFound(let name):
				status = "\(name) was not found."
			}
		}
	)
}
```

## Predict before running

Start with a fresh run. Fill every prediction before using the buttons.

| Moment                   | Predicted count | Predicted rows, in order                                        | Predicted status               |
| ------------------------ | --------------- | --------------------------------------------------------------- | ------------------------------ |
| Launch                   | 3               | Milk - quantity: 5<br>Eggs - quantity: 6<br>Bread - quantity: 1 | Ready to add an item.          |
| Tap Remove on Eggs       | 2               | Milk - quantity: 5<br>Bread - quantity: 1                       | Removed Eggs. 2 items remain.  |
| Tap Remove on Bread      | 1               | Milk - quantity: 5                                              | Removed Bread. 1 items remain. |
| Add Rice with quantity 2 | 2               | Milk - quantity: 5<br>Rice - quantity: 2                        | Added Rice (quantity: 2).      |

Leave actual results empty until the tutor reviews the implementation and
predictions.

| Moment               | Actual count | Actual rows, in order                                           | Actual status                  |
| -------------------- | ------------ | --------------------------------------------------------------- | ------------------------------ |
| Launch               | 3            | Milk - quantity: 5<br>Eggs - quantity: 6<br>Bread - quantity: 1 | Ready to add an item.          |
| After removing Eggs  | 2            | Milk - quantity: 5<br>Bread - quantity: 1                       | Removed Eggs. 2 items remain.  |
| After removing Bread | 1            | Milk - quantity: 5                                              | Removed Bread. 1 items remain. |
| After adding Rice    | 2            | Milk - quantity: 5<br>Rice - quantity: 2                        | Added Rice (quantity: 2).      |

## Explain the boundary

Why does the closure preserve parent ownership even though the button that starts
the action is inside the child?

> because we are only passing the action of the button into the child, we are not modifying it via the child, we actually doing the operation still in the parent

## Tutor review 1 — missing child trigger

The parent closure, exhaustive result handling, predictions, reported transitions,
and ownership explanation are correct. The pasted `ShoppingItemRow`, however,
declares `onRemove` without displaying a Remove button or calling `onRemove()`.
As shown, that source cannot initiate the recorded removals.

Update the original source block with the exact child code used for the run. It
must show the Remove button calling `onRemove()` exactly once. If the Xcode source
also omitted the button, add it, rebuild, and repeat the removal sequence before
confirming the actual table.

## Tutor review 2 — checkpoint complete

Final source review confirmed that the child calls its action once and has no
model, state, or binding. The parent-provided closure calls the model's Remove
method once, handles every result, and updates parent-owned status. The reported
count and rows matched two removals followed by one successful addition.

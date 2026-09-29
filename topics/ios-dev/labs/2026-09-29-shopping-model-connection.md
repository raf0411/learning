# Connect the shopping-entry screen to its model

## Next capability

The screen will submit name and quantity input to your existing ShoppingList,
display the returned result, and show how many items the model contains.
The model already owns validation; we will reuse that work.

## First: bring in your current source

Paste the existing code from Xcode below. Do not rewrite it for this step.
Include ShoppingItem, ShoppingList, and any result types or helpers they use so
the tutor can check the actual API and dependencies before assigning integration.
You can omit Playground test calls and console-printing examples.

If the source already exists as a file, you may provide its absolute path instead
of copying the code. If you cannot find it, say so and we will adapt.

```swift
struct ShoppingItem {
	var name: String
	var quantity: Int
}

struct ShoppingList {
	private(set) var list: [ShoppingItem] = [
		ShoppingItem(name: "Milk", quantity: 5),
		ShoppingItem(name: "Eggs", quantity: 6),
		ShoppingItem(name: "Bread", quantity: 1),
	]
	
	mutating func add(name: String, quantityText: String) -> AddResult {
		let cleanName = name.trimmingCharacters(in: .whitespacesAndNewlines)
		
		guard !cleanName.isEmpty else {
			return AddResult.emptyName
		}
		
		let isDuplicate = list.contains { item in
			item.name == cleanName
		}
		
		guard !isDuplicate else {
			return AddResult.duplicateName(name: cleanName)
		}
		
		guard let quantity = validNumber(number: quantityText) else {
			return AddResult.invalidQuantity
		}
		
		let newItem = ShoppingItem(name: cleanName, quantity: quantity)
		list.append(newItem)
		
		return AddResult.added(name: cleanName, quantity: quantity)
	}
	
	mutating func remove(name: String) -> RemoveResult {
		let cleanName = name.trimmingCharacters(in: .whitespacesAndNewlines)
		
		guard !cleanName.isEmpty else {
			return RemoveResult.emptyName
		}
		
		guard let matchingIndex = list.firstIndex(where: { item in
			item.name == cleanName
		}) else {
			return RemoveResult.notFound(name: cleanName)
		}
		
		list.remove(at: matchingIndex)
		
		return RemoveResult.removed(name: cleanName, remainingCount: list.count)
	}
	
	mutating func removeFirstItem(quantityAtMost maximum: Int) -> Bool {
		guard let matchingIndex = list.firstIndex(where: { item in
			item.quantity <= maximum
		}) else {
			return false
		}
		
		list.remove(at: matchingIndex)
		
		return true
	}
	
	mutating func updateQuantity(name: String, quantityText: String) -> UpdateResult {
		let cleanName = name.trimmingCharacters(in: .whitespacesAndNewlines)
		
		guard !cleanName.isEmpty else {
			return UpdateResult.emptyName
		}
		
		guard let newQuantity = validNumber(number: quantityText) else {
			return UpdateResult.invalidQuantity
		}
		
		guard let matchingIndex = list.firstIndex(where: { item in
			item.name == cleanName
		}) else {
			return UpdateResult.notFound(name: cleanName)
		}
		
		let oldQuantity = list[matchingIndex].quantity
		
		list[matchingIndex].quantity = newQuantity
		
		return UpdateResult.updated(name: cleanName, oldQuantity: oldQuantity, newQuantity: newQuantity)
	}
	
	func items(quantityAtLeast minimum: Int) -> [ShoppingItem] {
		return list.filter { item in
			item.quantity >= minimum
		}
	}
	
	mutating func renameItem(from currentName: String, newName: String) -> RenameResult {
		let cleanCurrentName = currentName.trimmingCharacters(in: .whitespacesAndNewlines)
		
		let cleanNewName = newName.trimmingCharacters(in: .whitespacesAndNewlines)
		
		guard !cleanCurrentName.isEmpty else {
			return RenameResult.emptyCurrentName
		}
		
		guard !cleanNewName.isEmpty else {
			return RenameResult.emptyNewName
		}
		
		guard let matchingIndex = list.firstIndex(where: { item in
			item.name == cleanCurrentName
		}) else {
			return RenameResult.notFound(name: cleanCurrentName)
		}
		
		guard cleanCurrentName != cleanNewName else {
			return RenameResult.unchanged(name: cleanCurrentName)
		}
		
		let isDuplicate = list.contains { item in
			item.name == cleanNewName
		}
		
		guard !isDuplicate else {
			return RenameResult.duplicate(name: cleanNewName)
		}
		
		list[matchingIndex].name = cleanNewName
		
		return RenameResult.renamed(oldName: cleanCurrentName, newName: cleanNewName)
	}
}

enum AddResult {
	case added(name: String, quantity: Int)
	case emptyName
	case duplicateName(name: String)
	case invalidQuantity
}

enum RemoveResult {
	case removed(name: String, remainingCount: Int)
	case notFound(name: String)
	case emptyName
}

enum UpdateResult {
	case updated(name: String, oldQuantity: Int, newQuantity: Int)
	case invalidQuantity
	case notFound(name: String)
	case emptyName
}

enum RenameResult {
	case renamed(oldName: String, newName: String)
	case emptyCurrentName
	case emptyNewName
	case notFound(name: String)
	case duplicate(name: String)
	case unchanged(name: String)
}

func printRenameResult(_ result: RenameResult) {
	switch result {
	case .renamed(let oldName, let newName):
		print("Renamed \(oldName) to \(newName).")
	case .duplicate(let name):
		print("\(name) already exists.")
	case .notFound(let name):
		print("\(name) was not found.")
	case .emptyCurrentName:
		print("Current name cannot be empty.")
	case .emptyNewName:
		print("New name cannot be empty.")
	case .unchanged(let name):
		print("\(name) is unchanged.")
	}
}

func printMessage(result: AddResult) {
	switch result {
	case .added(let name, let quantity):
		print("Added \(name) (quantity: \(quantity)).")
	case .emptyName:
		print("Name cannot be empty.")
	case .duplicateName(let name):
		print("\(name) already exists.")
	case .invalidQuantity:
		print("Quantity must be a positive whole number.")
	}
}

func printRemoveMessage(result: RemoveResult) {
	switch result {
	case .removed(let name, let remainingCount):
		print("Removed \(name). \(remainingCount) items remain.")
	case .notFound(let name):
		print("\(name) was not found.")
	case .emptyName:
		print("Name cannot be empty.")
	}
}

func printUpdateResult(_ result: UpdateResult) {
	switch result {
	case .updated(let name, let oldQuantity, let newQuantity):
		print("Updated \(name) from \(oldQuantity) to \(newQuantity).")
	case .invalidQuantity:
		print("Quantity must be a positive integer.")
	case .notFound(let name):
		print("\(name) was not found.")
	case .emptyName:
		print("Name cannot be empty.")
	}
}
```

Source path, if used instead:

> 

Tell the tutor when this is ready. The next implementation task will be based on
your actual model.

## Tutor review 1 — model inspected

Your model supplies the operations needed for this screen:

- `ShoppingList()` starts with THREE items: Milk (5), Eggs (6), and Bread (1).
- `add(name:quantityText:)` validates, mutates its stored array on success, and
  returns an `AddResult` for the caller to handle.
- Its validation order is empty cleaned name, duplicate cleaned name, then
  quantity. A duplicate with invalid quantity therefore returns `duplicateName`.
- `private(set)` lets the screen read `list` and its count while mutation goes
  through the model's methods.

One dependency is missing from the pasted source: `validNumber(number:)`.
Both Add and Update call it. Paste your existing helper here so its actual
behavior can be reviewed. Include `import Foundation` in a separate model file
for the Foundation string-trimming API.

```swift
func validNumber(number: String) -> Int? {
	if let num = Int(number) {
		if num > 0 {
			return num
		}
	}
	
	return nil
}
```

## Next concept: the model can be view-owned state

`@State` can hold your entire `ShoppingList` struct, just as it held a String.
Declare that state as a property of the view. Creating a fresh local model inside
the Add action would discard earlier additions whenever the button runs.

The screen owns the draft text and display message. The model owns the accepted
items and validation. A button action connects them:

```text
Name and quantity drafts
          |
          | Add button calls the model once
          v
ShoppingList.add -> AddResult -> screen message
          |
          v
Model's stored list -> displayed item count
```

## Build one working connection

Extend your SwiftUI screen in Xcode:

1. Own one `ShoppingList` as view state, initialized with `ShoppingList()`.
2. Provide name and quantity text fields, both initially empty. Keep quantity
   input as a String so the model can validate what was typed.
3. Display `Items: COUNT` using the model's current `list.count`. Do not keep a
   second independently updated item counter.
4. Display a status message, initially `Ready to add an item.`
5. On Add, pass the two draft strings to `add(name:quantityText:)` exactly once.
   Use an exhaustive switch on the returned result to update the status message.
   Reuse the message wording in your existing `printMessage(result:)` function,
   but display it in the view instead of only printing to the console.
6. Clear both drafts only on `.added`. Preserve both drafts on every failure.

Use the existing model validation. Keep its three initial items for this exercise.
Keep the Add button enabled so you can exercise the model's failure results.
This step displays a count; individual item rows come later.

Paste your implemented view:

```swift
// TODO: your SwiftUI view
```

## Predict, then run

Start a fresh run. Before each numbered attempt, REPLACE both field contents with
the exact inputs in that row. Attempts happen in order without restarting.
Quotes delimit input; do not type the quotes. Record empty fields as `""` and
three spaces as `"   "`.

Complete predictions before running, then fill the actual table from Xcode.

| Attempt | Name input | Quantity input | Predicted item count | Predicted status message | Predicted name / quantity fields afterward |
|---|---|---|---|---|---|
| Launch, without tapping Add | — | — | TODO | TODO | TODO |
| 1: tap Add | `"  Rice  "` | `"2"` | TODO | TODO | TODO |
| 2: tap Add | `"Milk"` | `"abc"` | TODO | TODO | TODO |
| 3: tap Add | `"   "` | `"3"` | TODO | TODO | TODO |
| 4: tap Add | `"Oats"` | `"0"` | TODO | TODO | TODO |
| 5: tap Add | `"Oats"` | `"4"` | TODO | TODO | TODO |

| Attempt | Actual item count | Actual status message | Actual name / quantity fields afterward |
|---|---|---|---|
| Launch | TODO | TODO | TODO |
| 1 | TODO | TODO | TODO |
| 2 | TODO | TODO | TODO |
| 3 | TODO | TODO | TODO |
| 4 | TODO | TODO | TODO |
| 5 | TODO | TODO | TODO |

If you get stuck, share the partial code and exact compiler error or unexpected
behavior. Preserve predictions that differed from the run.

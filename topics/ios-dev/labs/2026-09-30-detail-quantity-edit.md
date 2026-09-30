# Edit quantity from the detail screen

## Learning target

Keep an unfinished quantity draft local to the detail screen while asking the
parent-owned model to validate and save it.

```text
ShoppingItemDetailView
  local @State quantityDraft
          |
          | String on Save
          v
  action closure owned by ContentView
          |
          v
  ShoppingList.updateQuantity(...)
          |
          | UpdateResult
          v
  detail feedback
```

Typing alone must not mutate the model. Leaving with Back before Save should
discard the detail screen's unfinished draft.

## New closure shape

The previous actions accepted no input and returned nothing:

```swift
let onRemove: () -> Void
```

This Save action accepts the draft text and returns the model result:

```swift
let onSave: (String) -> UpdateResult
```

Calling `onSave(quantityDraft)` sends one `String` to the closure and gives the
detail screen an `UpdateResult` to handle.

## Passing a function versus calling it

`onSaveQuantity` is a function value. Without parentheses, it can be passed to
another view. With parentheses and an argument, it is executed.

```text
ContentView creates the function
    |
    | passes function (no parentheses)
    v
ShoppingItemRow
    |
    | passes the same function (no parentheses)
    v
ShoppingItemDetailView
    |
    | calls function with quantityDraft
    v
ContentView closure calls ShoppingList and returns UpdateResult
    |
    v
detail switch handles that returned UpdateResult
```

The parent creates the closure. The parameter name belongs after `{` and before
`in`:

```swift
onSaveQuantity: { draft in
    return shoppingList.updateQuantity(
        name: item.name,
        quantityText: draft
    )
}
```

The row only forwards that function; it does not call it:

```swift
ShoppingItemDetailView(
    item: item,
    onSave: onSaveQuantity
)
```

The detail calls it only when Save is tapped:

```swift
let result = onSave(quantityDraft)
```

For an Eggs draft of `"9"`, the values move like this:

```text
"9" -> parent closure -> updateQuantity -> .updated(Eggs, 6, 9)
                                              |
                                              v
                                  detail feedback switch
```

## Build the feature

Preserve the working Add, Remove, and navigation behavior.

1. In `ShoppingItemDetailView`, keep `let item: ShoppingItem`.
2. Add private local state named `quantityDraft`, initially `""`.
3. Add private local state named `feedback`, initially
   `"No update attempted."`.
4. Give the detail view `let onSave: (String) -> UpdateResult`.
5. Add a `TextField` for the new quantity, a Save button, and text displaying
   `feedback`.
6. On each Save tap, call `onSave(quantityDraft)` exactly once. Exhaustively
   switch on the returned result and set `feedback`:
   - success: `Updated NAME from OLD to NEW.`
   - empty name: `Name cannot be empty.`
   - invalid quantity: `Quantity must be a positive whole number.`
   - missing item: `NAME was not found.`
7. Give `ShoppingItemRow` an `onSaveQuantity: (String) -> UpdateResult` action and
   pass it to the detail destination as `onSave`.
8. In `ContentView`, construct each row with a closure that calls
   `shoppingList.updateQuantity(name: item.name, quantityText: draft)` and returns
   that result. Do not duplicate the model's validation in the view.
9. Do not add a quantity-draft property to `ContentView`, and do not give the
   detail screen the whole list or a binding to it.

Paste only these updated pieces:

```swift
import SwiftUI
import Playgrounds

struct ShoppingItem : Identifiable {
    let id: UUID = UUID()
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
    
    private func validNumber(number: String) -> Int? {
        if let num = Int(number) {
            if num > 0 {
                return num
            }
        }
        
        return nil
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

struct ContentView: View {
    @State private var shoppingList: ShoppingList = ShoppingList()
    @State private var name: String = ""
    @State private var quantity: String = ""
    @State private var status: String = "Ready to add an item."
    
    var body: some View {
        NavigationStack {
            VStack(spacing: 32) {
                
                ShoppingEntryForm(
                    name: $name,
                    quantity: $quantity,
                    onAdd: {
                        let result = shoppingList.add(name: name, quantityText: quantity)
                        
                        switch result {
                        case .added(let name, let quantity):
                            status = "Added \(name) (quantity: \(quantity))."
                            self.name = ""
                            self.quantity = ""
                        case .emptyName:
                            status = "Name cannot be empty."
                        case .duplicateName(let name):
                            status = "\(name) already exists."
                        case .invalidQuantity:
                            status = "Quantity must be a positive whole number."
                        }
                    })
                
                Text("Items: \(shoppingList.list.count)")
                
                Text(status)
                
                VStack {
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
                            },
                            onSaveQuantity: { draft in
                                shoppingList.updateQuantity(name: item.name, quantityText: draft)
                            }
                        )
                    }
                }
            }
            .navigationTitle("Shopping List")
            .padding()
        }
    }
}

struct ShoppingItemRow: View {
    let item: ShoppingItem
    
    let onRemove: () -> Void
    let onSaveQuantity: (String) -> UpdateResult
    
    var body: some View {
        HStack {
            NavigationLink("\(item.name) — quantity: \(item.quantity)", destination: {ShoppingItemDetailView(
                item: item,
                onSave: onSaveQuantity
            )})
                .buttonStyle(.bordered)
            
            Button("Remove", action: {
                onRemove()
            })
            .buttonStyle(.borderedProminent)
        }
    }
}

struct ShoppingEntryForm: View {
    @Binding var name: String
    @Binding var quantity: String
    
    let onAdd: () -> Void
    
    var body: some View {
        HStack(spacing: 32) {
            TextField("Name", text: $name)
                .textFieldStyle(.roundedBorder)
            
            TextField("Quantity", text: $quantity)
                .textFieldStyle(.roundedBorder)
            
            Button("Add", action: {
                onAdd()
            })
            .buttonStyle(.borderedProminent)
        }
        .padding()
    }
}

struct ShoppingItemDetailView: View {
    let item: ShoppingItem
    
    @State private var quantityDraft: String = ""
    @State private var feedback: String = "No update attempted."
    
    let onSave: (String) -> UpdateResult
    
    var body: some View {
        VStack {
            TextField("Edit Quantity", text: $quantityDraft)
            
            Button("Save", action: {
                let result = onSave(quantityDraft)
                
                switch result {
                case .updated(let name, let oldQuantity, let newQuantity):
                    feedback = "Updated \(name) from \(oldQuantity) to \(newQuantity)."
                case .emptyName:
                    feedback = "Name cannot be empty."
                case .invalidQuantity:
                    feedback = "Quantity must be a positive whole number."
                case .notFound(let name):
                    feedback = "\(name) was not found."
                }
            })
            
            Text(feedback)
            
            Text("Item details")
                .font(.title)
                .bold()
            
            Spacer()
            
            Text("Name: \(item.name) | Quantity: \(item.quantity)")
            
            Spacer()
        }
        .navigationTitle(item.name)
    }
}

#Preview {
    ContentView()
}

```

## Predict before running

Begin from a fresh launch. Fill only the Prediction column, then stop for source
review before running.

| Step                                                                    | Prediction                                | Actual                                    |
| ----------------------------------------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| Open Milk, type `12`, then use Back without Save: Milk quantity on list | 5                                         | 5                                         |
| Open Eggs, type `9`, tap Save: detail feedback                          | Updated Eggs from 6 to 9.                 | Updated Eggs from 6 to 9.                 |
| Use Back after saving Eggs: Eggs quantity on list                       | 9                                         | 9                                         |
| Open Bread, type `0`, tap Save: detail feedback                         | Quantity must be a positive whole number. | Quantity must be a positive whole number. |
| Use Back after rejected Bread update: Bread quantity on list            | 1                                         | 1                                         |

## Explain the data flow

1. Why is `quantityDraft` local `@State` rather than a binding to parent storage?
2. Which object validates and mutates the accepted quantity?
3. What travels from detail to parent, and what comes back?

> 1. Because we don't want any unsaved draft from the detail to change the one in parent storage as well
> 2. `ShoppingList` object from the Parent View
> 3. the draft quantity from detail view, and it returns the UpdateResult.updated

# Make the shopping model observable

## Purpose

Apply the shared-counter pattern to your existing shopping app. The parent will
own one shopping model, and a new summary child will read that same instance.

Use your working app from the detail-quantity exercise as the starting point.

## Implement

1. Turn `ShoppingList` into an observable final class using the counter pattern.
   Adjust its method declarations for a class. Include the required import.
2. Keep the model's validation, result enums, `private(set)` array, and initial
   Milk (5), Eggs (6), and Bread (1). Keep `ShoppingItem` as a struct.
3. Keep one parent-owned model in private `@State`. Preserve the existing entry
   form, row actions, navigation, and local detail draft.
4. Create `ShoppingSummaryView`. Give it an ordinary `let` property receiving a
   `ShoppingList`. Display `Summary items: COUNT`, deriving COUNT from its array.
5. Place the summary next to the parent's existing `Items: COUNT` label and pass
   the parent's model into it. Both labels should reflect successful additions
   and removals. A rejected operation should leave both counts unchanged.

Paste the updated model, summary view, and parent view. Existing unchanged item,
enum, form, row, and detail declarations can stay in your Xcode source.

```swift
import SwiftUI
import Playgrounds
import Observation

struct ShoppingItem : Identifiable {
    let id: UUID = UUID()
    var name: String
    var quantity: Int
}

@Observable
final class ShoppingList {
    private(set) var list: [ShoppingItem] = [
        ShoppingItem(name: "Milk", quantity: 5),
        ShoppingItem(name: "Eggs", quantity: 6),
        ShoppingItem(name: "Bread", quantity: 1),
    ]
    
    func add(name: String, quantityText: String) -> AddResult {
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
    
    func remove(name: String) -> RemoveResult {
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
    
    func removeFirstItem(quantityAtMost maximum: Int) -> Bool {
        guard let matchingIndex = list.firstIndex(where: { item in
            item.quantity <= maximum
        }) else {
            return false
        }
        
        list.remove(at: matchingIndex)
        
        return true
    }
    
    func updateQuantity(name: String, quantityText: String) -> UpdateResult {
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
    
    func renameItem(from currentName: String, newName: String) -> RenameResult {
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
                
                HStack {
                    Text("Items: \(shoppingList.list.count)")
                    ShoppingSummaryView(shoppingList: shoppingList)
                }
                
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
            Text("Item details")
                .font(.title)
                .bold()
            
            Spacer()
            
            VStack(spacing: 32) {
                TextField("Edit Quantity", text: $quantityDraft)
                    .textFieldStyle(.bordered)
                
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
                .buttonStyle(.borderedProminent)
                
                Text(feedback)
            }
            
            Spacer()
            
            Text("Name: \(item.name) | Quantity: \(item.quantity)")
            
            Spacer()
        }
        .navigationTitle(item.name)
        .padding()
    }
}

struct ShoppingSummaryView: View {
    let shoppingList: ShoppingList
    
    var body: some View {
        Text("Summary items: \(shoppingList.list.count)")
    }
}

#Preview {
    ContentView()
}
```

## Choose checks and predict

Choose exact inputs for a successful Add, a rejected Add, and a successful Remove.
Start with a fresh launch and perform the checks in that order. Predict the two
displayed counts after each operation. Leave Actual empty until source review.

| Check             | Exact inputs / action | Predicted parent count | Predicted summary count | Actual counts |
| ----------------- | --------------------- | ---------------------- | ----------------------- | ------------- |
| Successful Add    | Flower / 1            | 4                      | 4                       | 4 / 4         |
| Rejected Add      | Flower / abc          | 4                      | 4                       | 4 / 4         |
| Successful Remove | Remove Bread          | 3                      | 3                       | 3 / 3         |

## Ownership check

Suppose you accidentally pass a newly constructed `ShoppingList()` into the
summary instead of the parent's model. After adding an item through the parent,
would the two counts agree? Explain why.

> No, because it's a new reference, it's not the one from the parent, it's essentially a new instance of ShoppingList()

Tell the tutor when the code and predictions are ready. Preserve predictions if
a later run differs; record the actual result separately.

No. The parent would show 4, while the summary would show 3, because the summary received a separate ShoppingList instance.

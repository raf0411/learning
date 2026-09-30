# Navigate from the shopping list to item details

## Learning target

Add a read-only detail screen without changing ownership of the shopping list.

`NavigationStack` is more than a container that permits navigation: it manages
the current navigation history. A `NavigationLink` describes a destination and
the label the user selects to reach it.

```text
NavigationStack
|
+-- Shopping-list screen
    |
    +-- NavigationLink for Eggs ----pushes----> Eggs detail screen
                                               |
                                               +-- Back returns to the list
```

The existing ownership should remain:

```text
ContentView owns ShoppingList
    |
    +-- ShoppingItemRow receives one read-only ShoppingItem
            |
            +-- ShoppingItemDetailView receives one read-only ShoppingItem
```

## Build the navigation

Modify the current Xcode code while preserving the existing Add and Remove
behavior.

1. Create `ShoppingItemDetailView: View` with `let item: ShoppingItem`.
2. Display the heading `Item details`, the item's name, and its quantity.
3. Wrap the shopping-list interface in a `NavigationStack`.
4. Give the list screen the navigation title `Shopping List`.
5. In `ShoppingItemRow`, make the item text the label of a `NavigationLink` whose
   destination is `ShoppingItemDetailView(item: item)`.
6. Keep the Remove button beside the link, not inside its label.
7. Give the detail screen a navigation title derived from the item's name.
8. Do not add `@State`, `@Binding`, the whole list, or a mutation action to the
   detail screen.

Paste only these three updated pieces:

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
    
    var body: some View {
        HStack {
            NavigationLink("\(item.name) — quantity: \(item.quantity)", destination: {ShoppingItemDetailView(item: item)})
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
    
    var body: some View {
        VStack {
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

Use a fresh launch. Fill this table before running and leave the Actual column as
`TODO` until the source and predictions are reviewed.

| Step                                                     | Prediction                                        | Actual                                            |
| -------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| Launch: visible screen title and item count              | Shopping List / 3                                 | Shopping List / 3                                 |
| Tap the Eggs item text: visible screen title and content | Eggs / Item details / Name: Eggs \| Quantity: 6   | Eggs / Item details / Name: Eggs \| Quantity: 6   |
| Use Back: visible screen and item count                  | Shopping List / 3                                 | Shopping List / 3                                 |
| Tap Eggs Remove: visible screen, count, and status       | Shopping List / 2 / Removed Eggs. 2 items remain. | Shopping List / 2 / Removed Eggs. 2 items remain. |

## Explain the roles

Answer briefly in your own words.

1. What state or history is `NavigationStack` responsible for?
2. Why is the Remove button kept outside the `NavigationLink` label?
3. Who still owns the shopping list, and what does the detail screen receive?

> 1. For storing the history of our navigations
> 2. The controls are separate so tapping Remove triggers removal without also activating navigation
> 3. The Parent View, the detail screen only receives the constant ShoppingItem value, it don't have a set/get relationship


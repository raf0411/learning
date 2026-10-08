# SwiftData shopping integration — design probe

## Purpose

Plan the smallest migration from the existing in-memory shopping app to
persistent shopping-item records. Do not change the Xcode project yet.

The current app uses:

- a `ShoppingItem` struct for one item;
- an observable `ShoppingList` class containing `[ShoppingItem]`;
- parent-owned `@State` for the `ShoppingList` instance;
- methods on `ShoppingList` for Add, Remove, and quantity updates;
- `ForEach(shoppingList.list)` to render rows.

The completed SwiftData lab established these roles:

- one `@Model` instance represents one record;
- the model container configures the store;
- `ModelContext` manages inserts, changes, deletions, and saves;
- `@Query` retrieves and observes matching records for a view.

## Part 1 — Map the responsibilities

Complete the final two columns. Use one or more of `@Model`, model container,
`ModelContext`, `@Query`, or “keep ordinary Swift logic.”

| Responsibility                         | Current mechanism                    | Proposed mechanism | Why                                                                                                               |
| -------------------------------------- | ------------------------------------ | ------------------ | ----------------------------------------------------------------------------------------------------------------- |
| Represent one shopping item            | `ShoppingItem` struct                | @Model             | because a shopping item can be retrieve as a query collection and @Model is good for that                         |
| Provide records for the UI             | `ShoppingList.list` array            | @Query             | because it can retrieves and observes matching records for a view                                                 |
| Make records survive relaunch          | Nothing                              | model container    | because this can tell SwiftUI which @Model should survive during relaunch, like its autosave                      |
| Insert or delete a record              | Array mutation inside `ShoppingList` | ModelContext       | because this manages inserts or deletions                                                                         |
| Validate names and quantity text       | Ordinary Swift methods               | keep it            | because it doesn't require any saving in or surviving during relaunch, it is merely just for inputs from the user |
| Render rows when stored records change | Observation of `ShoppingList.list`   | @Query             | because it can retrieves and observes matching records for a view                                                 |

## Part 2 — Ownership check

Answer briefly in your own words.

1. Does `@Query` own or permanently store the shopping records?

   >I think neither? it merely just retrieves and observes matching records to be able to render it in the SwiftUI view

2. Which component performs an insertion?

   > ModelContext

3. Which component makes persistent storage available to the app scene?

   > Model Container

4. If the view is recreated, why can its new query still retrieve earlier items?

   > if there's no changes from items, i think it can retrieve earlier items, because query retrieves and observes availble items currently, even though view is recreated, it depends on the available data

## Part 3 — Predict the first persistent run

Assume a fresh store, a name-sorted query, and Add actions that insert one new
record each time. Do not assume that matching names are merged.

| Moment                                | Predicted count | Predicted rows in display order |
| ------------------------------------- | --------------- | ------------------------------- |
| Fresh launch                          | 0               | None                            |
| After inserting Milk: 5, then Eggs: 6 | 2               | Eggs: 6<br>Milk: 5              |
| After relaunch                        | 2               | Eggs: 6<br>Milk: 5              |
| After inserting Milk: 5 once more     | 3               | Eggs: 6<br>Milk: 5<br>Milk: 5   |

Explain the final row count:

> Because we are using insert, it will treat it as a new item even if the existing item already exists, it won't update it

## Part 4 — Migration risk

The current `ShoppingList` methods protect rules such as nonempty names,
positive quantities, and duplicate rejection. What could go wrong if the new
view called `modelContext.insert(...)` directly without applying those rules?

> Like previously happened, it will treat it as a new item and inserts it even if the quantity is negative, or it already exists before, or even empty name

When every `TODO` is complete, tell the tutor the worksheet is ready. Do not
implement the migration yet.

## Tutor review 1

The responsibility mapping and all four run predictions are correct. Three
descriptions need tighter boundaries:

1. `@Model` makes each `ShoppingItem` instance a persistable record. It does not
   turn that instance into a query collection; `@Query` retrieves the collection.
2. The model container configures the schema and backing store and supplies the
   model context. Autosave is context behavior; it is not the definition of a
   container.
3. A recreated view can retrieve current records—even if they changed—because
   the persistent store and its container outlive that particular view value. A
   new query fetches the current matching records from that data stack.

The final duplicate prediction correctly distinguishes insertion from updating.
The migration-risk answer also preserves the important invariant: persistence
must not create a second, unvalidated mutation path.

## Implementation 1 — persistent Add only

Build this as a small isolated step. Preserve the earlier `PantryItem` source and
results. Do not migrate Remove, detail editing, or navigation yet.

### New multi-model container syntax

If this work remains in the same app target as `PantryItem`, configure both model
types in the existing app scene:

```swift
.modelContainer(for: [PantryItem.self, ShoppingItem.self])
```

Use both types in the in-memory Preview container as well. This keeps the earlier
model in the schema while adding the new one. There must still be only one
`@main` app declaration.

### Requirements

1. Replace the in-memory shopping-item struct for this new view with an `@Model`
   `final class ShoppingItem` containing mutable `name: String` and
   `quantity: Int`, plus an initializer.
2. Create `PersistentShoppingView` with:
   - the environment model context;
   - a private name-sorted query of shopping items;
   - private name and quantity draft state;
   - private status-message state.
3. Display `Items: COUNT` from the query and render every queried record as
   `NAME — quantity: QUANTITY`.
4. Keep Add validation as ordinary Swift logic in one method rather than placing
   all branches directly inside the Button closure. Use this exact precedence:
   - cleaned name is empty;
   - an exact-name record already exists;
   - quantity conversion fails or the integer is not positive;
   - otherwise insert one new `ShoppingItem` through the model context.
5. Report these exact statuses:
   - `Name cannot be empty.`
   - `NAME already exists.`
   - `Quantity must be a positive whole number.`
   - `Added NAME with quantity QUANTITY.`
6. Clear both drafts only after a successful insertion. Preserve both drafts on
   every rejected Add.
7. Do not create or maintain a second `[ShoppingItem]` array. The query is the
   UI's record source for this step.
8. Do not call explicit `save()` in this step. The relaunch procedure below will
   test autosave again.

Paste the new model, the updated existing app scene, the new view, and its Preview:

```swift
import SwiftUI
import Playgrounds
import SwiftData

@Model
final class ShoppingItem {
    var name: String
    var quantity: Int
    
    init(name: String, quantity: Int) {
        self.name = name
        self.quantity = quantity
    }
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
                Text("\(item.name) - quantity: \(item.quantity)")
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
                    }
            })
            
            Text(status)
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
        
        return AddResult.added(name: cleanName, quantity: quantity)
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
    PersistentShoppingView()
        .modelContainer(for: ShoppingItem.self, inMemory: true)
        .preferredColorScheme(.dark)
}

@main struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            PersistentShoppingView()
        }
        .modelContainer(for: [PantryItem.self, ShoppingItem.self])
    }
}
```

### Predict before running

Start with no existing `ShoppingItem` records. Fill every prediction before the
first run.

| Moment                         | Predicted count | Predicted rows                           | Predicted status           | Predicted drafts |
| ------------------------------ | --------------- | ---------------------------------------- | -------------------------- | ---------------- |
| Fresh launch                   | Items: 0        | None                                     | Ready to add an item.      | ""/""            |
| Add `Milk` / `5`               | Items: 1        | Milk - quantity: 5                       | Added Milk with quantity 5 | ""/""            |
| Try `Milk` / `abc`             | Items: 1        | Milk - quantity: 5                       | Milk already exists.       | Milk / abc       |
| Try three spaces / `2`         | Items: 1        | Milk - quantity: 5                       | Name cannot be empty.      | "  " / 2         |
| Add `Eggs` / `6`               | Items: 2        | Eggs - quantity: 6<br>Milk - quantity: 5 | Added Eggs with quantity 6 | ""/""            |
| Background, stop, and relaunch | Items: 2        | Eggs - quantity: 6<br>Milk - quantity: 5 | Ready to add an item.      | ""/""            |

Why should `Milk / abc` report the duplicate result rather than the invalid-
quantity result?

> because the order is checking for duplicate first rather than the invalid quantity

### Run and record

Use the exact sequence above without changing the source between moments.

| Moment                         | Actual count | Actual rows                              | Actual status              | Actual drafts |
| ------------------------------ | ------------ | ---------------------------------------- | -------------------------- | ------------- |
| Fresh launch                   | Items: 0     | None                                     | Ready to add an item.      | ""/""         |
| Add `Milk` / `5`               | Items: 1     | Milk - quantity: 5                       | Added Milk with quantity 5 | ""/""         |
| Try `Milk` / `abc`             | Items: 1     | Milk - quantity: 5                       | Milk already exists.       | Milk / abc    |
| Try three spaces / `2`         | Items: 1     | Milk - quantity: 5                       | Name cannot be empty.      | "  " / 2      |
| Add `Eggs` / `6`               | Items: 2     | Eggs - quantity: 6<br>Milk - quantity: 5 | Added Eggs with quantity 6 | ""/""         |
| Background, stop, and relaunch | Items: 1     | Milk - quantity: 5                       | Ready to add an item.      | ""/""         |

Exact compiler/runtime error, if any:

> TODO: none

When the implementation, predictions, and actual results are complete, tell the
tutor the worksheet is ready.

## Tutor review 2 — visible does not yet mean saved

The persistent Add path is structurally correct: the root view reads a sorted
query, validation runs before context insertion, failures preserve the drafts,
and success clears them. The reported run adds useful evidence:

| Evidence kind | Statement |
| --- | --- |
| Observation | Milk and Eggs were both visible before termination; only Milk was visible after relaunch. |
| Supported conclusion | Milk reached the persistent store before termination; Eggs did not. |
| Plausible hypothesis | Milk existed longer and therefore had an earlier autosave opportunity; the process was stopped before the later Eggs change was saved. |
| Still unknown | The precise time or lifecycle event at which Milk was automatically saved. |

`@Query` observes the current model context, including inserted records that may
not have been saved yet. A row appearing proves that the context changed; a later
relaunch is what tests whether a new context can fetch that record from storage.

Exact punctuation and the visual choice of hyphen versus em dash are not assessed
in this persistence exercise. The Preview still needs the two-model container
because that is a data-stack configuration issue, not visual formatting:

```swift
.modelContainer(
    for: [PantryItem.self, ShoppingItem.self],
    inMemory: true
)
```

The older `ContentView` and `ShoppingList.list` declarations are disconnected
legacy code because `MyApp` now creates `PersistentShoppingView`. They may remain
temporarily for later feature migration, but they are not a persistent data path.

## Implementation 2 — report success only after saving

The UI currently reports success immediately after `insert`. Make the Add result
mean something stronger: `.added` should be returned only after an explicit
context save completes without throwing.

### New behavior

1. Add a save-failure case to `AddResult` carrying the cleaned item name.
2. After inserting the new item, explicitly save the model context inside
   `do`/`catch`.
3. Return `.added` only from the successful `do` path.
4. In the `catch` path, call `modelContext.rollback()` before returning the
   save-failure result. For this isolated view, rollback removes the unsaved
   insertion so the rows and reported result do not disagree.
5. Handle the new result exhaustively in the view. On save failure, show a clear
   failure status and preserve both drafts.
6. Apply the two-model in-memory container correction to the Preview.

`rollback()` discards every unsaved change in that context. It is acceptable in
this isolated Add-only view, where no other edit is pending. It would require more
care in a larger screen with several simultaneous edits.

Paste only the changed enum, Add method, result-handling switch, and Preview:

```swift
import SwiftUI
import Playgrounds
import SwiftData

@Model
final class ShoppingItem {
    var name: String
    var quantity: Int
    
    init(name: String, quantity: Int) {
        self.name = name
        self.quantity = quantity
    }
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
    case failed(name: String)
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
                Text("\(item.name) - quantity: \(item.quantity)")
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
    
    private func validNumber(number: String) -> Int? {
        if let num = Int(number) {
            if num > 0 {
                return num
            }
        }
        
        return nil
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
    PersistentShoppingView()
        .modelContainer(for: [PantryItem.self, ShoppingItem.self], inMemory: true)
        .preferredColorScheme(.dark)
}

```

### Predict before running

Begin with the currently persisted Milk record. Do not clear the store.

| Moment                                                    | Predicted stored rows                    | Predicted status           |
| --------------------------------------------------------- | ---------------------------------------- | -------------------------- |
| Relaunch before adding                                    | Milk - quantity: 5                       | Ready to add an item.      |
| Add `Eggs` / `6` and see the result                       | Eggs - quantity: 6<br>Milk - quantity: 5 | Added Eggs with quantity 6 |
| Stop immediately after the success appears, then relaunch | Eggs - quantity: 6<br>Milk - quantity: 5 | Ready to add an item.      |

Why is `.added` now stronger evidence than it was in the autosave version?

> because we added the do-catch and use modelContext.save()

### Run and record

| Moment                                                    | Actual stored rows                       | Actual status              |
| --------------------------------------------------------- | ---------------------------------------- | -------------------------- |
| Relaunch before adding                                    | Milk - quantity: 5                       | Ready to add an item.      |
| Add `Eggs` / `6` and see the result                       | Eggs - quantity: 6<br>Milk - quantity: 5 | Added Eggs with quantity 6 |
| Stop immediately after the success appears, then relaunch | Eggs - quantity: 6<br>Milk - quantity: 5 | Ready to add an item.      |

Compiler/runtime or save error, if any:

> TODO: none

When the changes, predictions, explanation, and actual results are complete,
tell the tutor the worksheet is ready.

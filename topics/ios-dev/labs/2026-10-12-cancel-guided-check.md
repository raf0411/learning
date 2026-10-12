# Cancel — guided test scenario

Complete this worksheet instead of the unfinished test-design section in the
previous worksheet. Your earlier answers and code remain there unchanged.
No new code is required for this check.

## What we are testing

Cancel should clear one row's draft and reset its feedback while preserving saved
quantities and the other row's draft and feedback.

The **accepted quantity** is the number in the row label, such as
`Milk - quantity: 5`. The **draft** is the text inside its Edit Quantity field.
Record actual numbers for accepted quantities; use `""` for an empty draft.

## 1. Build and establish the starting data

Build and run your app in Xcode. Use the existing Milk and Eggs rows. If either
is missing, add that item using your app's Add form with quantity 1. Do not delete
records or change the model's source code to arrange the test.

Build result (succeeded, or paste the error):

> succeeded

Read the row labels before continuing:

- Milk accepted quantity: 5
- Eggs accepted quantity: 6

## 2. Perform these actions in order

Keep the app open throughout the remaining steps.

1. In Milk's quantity field, replace any existing text with `8`. Tap Milk's
   **Save**. Confirm its row label now shows quantity 8 and its feedback reports
   success. If Save fails, stop and record what happened below.
2. In Milk's quantity field, type `2`. **Do not tap Save.**
3. In Eggs' quantity field, replace any existing text with `0`. Tap Eggs'
   **Save**. This gives that row validation feedback and an unsaved draft.
4. **Do not tap Cancel yet.** Fill the "Before Cancel: observed" column below
   by reading the screen.

Unexpected setup behavior, if any:

> none

## 3. Predict, then tap Cancel

First fill all six cells in "After Cancel: predicted" for this action:

**Tap Milk's Cancel button once. Do not tap anything in Eggs.**

Then perform that action and fill the observed column. Copy feedback from the
screen. Do not replace predictions if the observations differ.

| What to inspect        | Before Cancel: observed                   | After Cancel: predicted | After Cancel: observed |
| ---------------------- | ----------------------------------------- | ----------------------- | ---------------------- |
| Milk accepted quantity | 8                                         | 8                       | 8                      |
| Milk draft             | 2                                         | ""                      | ""                     |
| Milk feedback          | Updated Milk from 5 to 8.                 | No update attempted.    | No update attempted.   |
| Eggs accepted quantity | 6                                         | 6                       | 6                      |
| Eggs draft             | 0                                         | ""                      | ""                     |
| Eggs feedback          | Quantity must be a positive whole number. | No update attempted.    | No update attempted.   |

Did observations match your predictions? If not, identify the difference:

> Yes, it matches.

Tell the tutor when this worksheet is ready for review.

## Tutor review — isolate the other-row result

Milk's three predictions and reported results meet the requirements. Eggs'
accepted quantity also remains correct. However, Eggs' draft and feedback must
remain unchanged when only Milk's Cancel is tapped:

- Eggs draft should remain `"0"`.
- Eggs feedback should remain `Quantity must be a positive whole number.`

Your predictions and observations agree with each other, but those two outcomes
violate the requirement that Cancel affect only the tapped row. The earlier
pasted Cancel code changes only local row state, so the reported cross-row reset
needs investigation. We have not established whether the cause is the running
code, an additional action, or a recording error. Keep the original table above.

### Targeted recheck

1. In Milk, type `2` without saving.
2. In Eggs, type `0` and tap Eggs' Save. Confirm its draft still shows `0` and
   its feedback shows the validation message.
3. Tap **Milk's Cancel exactly once**. Do not tap Eggs' Cancel, relaunch, or
   navigate away before inspecting Eggs.
4. Record what Eggs actually shows immediately afterward.

Eggs draft after tapping only Milk's Cancel:

> 0

Eggs feedback after tapping only Milk's Cancel:

> Quantity must be a positive whole number.

If this differs from your earlier report, explain what you noticed (or say the
reason is unknown):

> No, i dont think it differs

Tutor assessment: this does differ from the original table, which recorded an
empty Eggs draft and default feedback. The recheck records draft `0` and the
validation message, meeting the isolation requirement. The cause of the original
report discrepancy remains unconfirmed; no cross-row reset bug is established.
Together with the earlier Milk observations and supplied code, this completes
the Cancel exercise with guided runtime verification (learner-reported).

If Eggs still resets, paste the current Xcode version of `PersistentShoppingRow`
and the parent code that creates its rows (including `ForEach` and any `.id`
modifiers). Do not change the implementation before capturing this evidence.

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

enum PersistentRemoveResult {
    case removed(name: String)
    case failed(name: String)
}

enum PersistentUpdateResult {
    case updated(name: String, oldQuantity: Int, newQuantity: Int)
    case invalidQuantity
    case failed(name: String)
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
    case failed(name: String)
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

struct PersistentShoppingRow: View {
    let item: ShoppingItem
    let onSaveQuantity: (String) -> PersistentUpdateResult
    let onRemoveItem: () -> Void
    
    @State private var quantityDraft: String = ""
    @State private var feedback: String = "No update attempted."

    var body: some View {
        VStack(alignment: .center) {
            HStack {
                VStack(alignment: .leading, spacing: 32) {
                    Text("\(item.name) - quantity: \(item.quantity)")
                    
                    TextField("Edit Quantity", text: $quantityDraft)
                        .frame(width: 120, height: 16)
                        .textFieldStyle(.roundedBorder)
                }
                
                Spacer()
                
                VStack() {
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
                    .buttonStyle(.borderedProminent)
                    
                    Button("Remove", action: {
                        onRemoveItem()
                    })
                    .buttonStyle(.borderedProminent)
                    
                    Button("Cancel", action: {
                        quantityDraft = ""
                        feedback = "No update attempted."
                    })
                }
            }
            
            Text(feedback)
        }
        .padding()
    }
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

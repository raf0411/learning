# Render shopping items as SwiftUI rows

## Learning target

Render every stored `ShoppingItem` and give SwiftUI stable identity for each row.

## Identity correction

Prompt: If `name` were the identity and `"Milk"` changed to `"Dairy Milk"`, would
SwiftUI infer that the same item changed or that one identity disappeared and a
new identity appeared?

Initial answer:

> i think the same item changed?

Correction: if `name` is the identity, changing the name also changes the
identity. SwiftUI sees the old `"Milk"` identity disappear and a new
`"Dairy Milk"` identity appear. A separate stored ID can stay unchanged while
editable properties such as name and quantity change.

```text
Same model item over time

id: A17          id: A17
name: Milk  -->  name: Dairy Milk
quantity: 5      quantity: 5

Stable identity: A17
Editable display data: name and quantity
```

`Identifiable` requires an `id` whose type conforms to `Hashable`. For this app,
each newly created item can receive a UUID once and keep it for its lifetime.

## Predict identity behavior

Complete the final two columns before changing the app.

| Change                                   | Does the stored ID change? | Same row identity or new row identity? | Why?                                                                                          |
| ---------------------------------------- | -------------------------- | -------------------------------------- | --------------------------------------------------------------------------------------------- |
| Change Milk's quantity from 5 to 7       | No                         | Same row identity                      | Because quantity is not the identity, it's a changeable value.                                |
| Rename Milk to Dairy Milk                | No                         | Same row identy                        | Because the name is not the identity, the identity is id.                                     |
| Remove Milk, then create a new Milk item | Yes                        | New row identity                       | Because we removed the previous Milk identity, creating a new one would create a new identity |

## Build the rows

Update the current Xcode source:

1. Make `ShoppingItem` conform to `Identifiable`.
2. Give each item a stored UUID that is created when the item is initialized.
3. In `ContentView`, use SwiftUI `ForEach` to render `shoppingList.list` in its
   existing array order.
4. Each row must display exactly `NAME — quantity: QUANTITY`.
5. Keep the existing count, status message, fields, Add behavior, and initial
   Milk/Eggs/Bread data.

Do not add a second array or manually maintain row views. The model array remains
the single source for both count and rows.

Paste only the revised `ShoppingItem` and the part of `ContentView` containing the
count and rows:

```swift
struct ShoppingItem : Identifiable {
    let id: UUID = UUID()
    var name: String
    var quantity: Int
}

struct ContentView: View {
    @State private var shoppingList: ShoppingList = ShoppingList()
    @State private var name: String = ""
    @State private var quantity: String = ""
    @State private var status: String = "Ready to add an item."
    
    var body: some View {
        VStack(spacing: 32) {
            
            HStack(spacing: 32) {
                TextField("Name", text: $name)
                    .textFieldStyle(.roundedBorder)
                
                TextField("Quantity", text: $quantity)
                    .textFieldStyle(.roundedBorder)
            }
            .padding()
            
            Text("Items: \(shoppingList.list.count)")
            
            Text(status)
            
            Button("Add", action: {
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
            .buttonStyle(.borderedProminent)
            
            VStack {
                ForEach(shoppingList.list) { item in
                    Text("\(item.name) — quantity: \(item.quantity)")
                }
            }
        }
        .padding()
    }
}

```

## Predict the visible rows

Start from a fresh run. Fill this table before running.

| Moment                                                        | Predicted rows, in order                                                              |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Launch                                                        | Milk - quantity: 5<br>Eggs - quantity: 6<br>Bread - quantity: 1                       |
| After adding `"  Rice  "` with quantity `"2"`                 | Milk - quantity: 5<br>Eggs - quantity: 6<br>Bread - quantity: 1<br>Rice - quantity: 2 |
| After then attempting duplicate `"Milk"` with quantity `"99"` | Milk - quantity: 5<br>Eggs - quantity: 6<br>Bread - quantity: 1<br>Rice - quantity: 2 |

Leave actual results empty until the tutor reviews the source and predictions.

| Moment                          | Actual rows, in order                                                                 |
| ------------------------------- | ------------------------------------------------------------------------------------- |
| Launch                          | Milk - quantity: 5<br>Eggs - quantity: 6<br>Bread - quantity: 1                       |
| After adding Rice               | Milk - quantity: 5<br>Eggs - quantity: 6<br>Bread - quantity: 1<br>Rice - quantity: 2 |
| After attempting duplicate Milk | Milk - quantity: 5<br>Eggs - quantity: 6<br>Bread - quantity: 1<br>Rice - quantity: 2 |

## Tutor review 1 — exact row contract

The identity predictions are correct: editing name or quantity preserves the
stored UUID, while removing and recreating an item produces a new UUID. The
`Identifiable` declaration and `ForEach` data source also have the right shape.

Before running:

- Change the displayed separator from the ordinary hyphen (`-`) to the required
  em dash (`—`) in both the view code and all predicted rows.
- Expand the pasted view excerpt so it shows the existing model-derived
  `Items: COUNT` text together with the `ForEach` rows. Do not create another
  count property.

Tell the tutor when those edits are ready. Keep the actual-results table empty.

## Tutor review 2 — checkpoint complete

Learner-reported results matched the model behavior: three initial rows rendered
in array order, successful Add appended Rice, and duplicate Milk left the rows
unchanged. Identity predictions correctly kept the UUID across name and quantity
changes and assigned a new identity after removal and recreation. The separator
punctuation was excluded from assessment at the learner's request because it did
not affect the collection-rendering or identity concepts.

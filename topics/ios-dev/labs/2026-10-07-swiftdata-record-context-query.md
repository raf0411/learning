# SwiftData: record → context → query

## Purpose

Build the smallest useful SwiftData feature and distinguish the three roles:

```text
PantryItem instance
       │ insert
       ▼
ModelContext ── coordinates with ── persistent model container
       ▲
       │ fetch and observe
     @Query
       │
       ▼
   SwiftUI view
```

Use an iOS 17-or-later app target and run the persistence sequence in the
Simulator. Do not run it until the tutor has reviewed your implementation and
predictions.

## New syntax

### One class instance represents one record

```swift
import SwiftData

@Model
final class PantryItem {
    // Stored properties and initializer go here.
}
```

### The app supplies persistent storage

Add the model container to the app's scene, not only to the preview:

```swift
WindowGroup {
    PersistentItemsView()
}
.modelContainer(for: PantryItem.self)
```

### A view gets its write context and queried records

```swift
@Environment(\.modelContext) private var modelContext
@Query(sort: \PantryItem.name) private var items: [PantryItem]
```

The sort makes the displayed order deterministic by name.

### Insert one new record

The general shape is:

```swift
modelContext.insert(PantryItem(name: "Example", quantity: 1))
```

The main model context supplied to SwiftUI has autosave enabled. This first lab
uses that behavior; explicit saving and save errors will be handled later.

### Keep preview data disposable

```swift
#Preview {
    PersistentItemsView()
        .modelContainer(for: PantryItem.self, inMemory: true)
}
```

## Requirements

### `PantryItem`

Create a SwiftData model class with:

- the exact name `PantryItem`
- a mutable `String` property named `name`
- a mutable `Int` property named `quantity`
- an initializer that assigns both properties

### `PersistentItemsView`

Create a view with:

- the model context from the environment
- a private query sorted by `PantryItem.name`
- a label displaying exactly `Stored items: N`
- a list row for every queried record, formatted exactly `Name: quantity`
- a button titled `Add Milk` that inserts `Milk` with quantity `1`
- a button titled `Add Eggs` that inserts `Eggs` with quantity `6`

Do not keep a parallel `[PantryItem]` in `@State`. The query is the view's source
for the displayed collection.

Paste your implementation below:

```swift
// TODO: PantryItem

// TODO: PersistentItemsView

// TODO: relevant App scene code

// TODO: preview
```

## Predict before running

Assume the installed app has a fresh persistent store. Perform these moments in
order. For rows, write `none` or list every visible row in display order.

| Moment | Predicted count label | Predicted rows |
| --- | --- | --- |
| First launch | TODO | TODO |
| After pressing `Add Milk` once | TODO | TODO |
| After pressing `Add Eggs` once | TODO | TODO |
| After stopping and relaunching the app | TODO | TODO |

## Explain before running

1. After both button presses, how many `PantryItem` instances have been inserted?

> TODO

2. Which part of your code performs writes, and which part retrieves and observes
   the collection shown by the view?

> TODO

3. Does `@Query` own or save the records? Explain its role in one or two sentences.

> TODO

4. Why is the app scene's model container persistent while this lab's preview
   container is not suitable for testing relaunch persistence?

> TODO

Tell the tutor when the implementation, predictions, and explanations are ready.
Do not run the interaction sequence yet.


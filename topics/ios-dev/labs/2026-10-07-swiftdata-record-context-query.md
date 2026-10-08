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
import SwiftUI
import SwiftData

@Model
final class PantryItem {
    var name: String
    var quantity: Int
    
    init(name: String, quantity: Int) {
        self.name = name
        self.quantity = quantity
    }
}

struct PersistentItemsView: View {
    @Environment(\.modelContext) private var modelContext
    @Query(sort: \PantryItem.name) private var items: [PantryItem]
    
    var body: some View {
        VStack {
            Text("Stored items: \(items.count)")
            
            ForEach(items, id: \.self) { item in
                Text("\(item.name): \(item.quantity)")
            }
            
            HStack {
                Button("Add Milk", action: {
                    modelContext.insert(PantryItem(name: "Milk", quantity: 1))
                })
                .buttonStyle(.borderedProminent)
                
                Button("Add Eggs", action: {
                    modelContext.insert(PantryItem(name: "Eggs", quantity: 6))
                })
                .buttonStyle(.borderedProminent)
            }
        }
        .padding()
    }
}

#Preview {
    PersistentItemsView()
        .modelContainer(for: PantryItem.self, inMemory: true)
}

@main struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            PersistentItemsView()
        }
        .modelContainer(for: PantryItem.self)
    }
}
```

## Predict before running

Assume the installed app has a fresh persistent store. Perform these moments in
order. For rows, write `none` or list every visible row in display order.

| Moment                                 | Predicted count label | Predicted rows     |
| -------------------------------------- | --------------------- | ------------------ |
| First launch                           | Stored items: 0       | None               |
| After pressing `Add Milk` once         | Stored items: 1       | Milk: 1            |
| After pressing `Add Eggs` once         | Stored items: 2       | Eggs: 6<br>Milk: 1 |
| After stopping and relaunching the app | Stored items: 2       | Eggs: 6<br>Milk: 1 |

## Explain before running

1. After both button presses, how many `PantryItem` instances have been inserted?

> Two, because we are using the model context to insert a new Pantry item in each button presses

2. Which part of your code performs writes, and which part retrieves and observes
   the collection shown by the view?

> Writes: modelContext.insert()
> retrieves and observes: 
> @Query(sort: \PantryItem.name) **private** **var** items: [PantryItem]
> ForEach(items, id: \.**self**) { item **in**

                Text("\(item.name): \(item.quantity)")

            }

3. Does `@Query` own or save the records? Explain its role in one or two sentences.

> Query is to retrieves and observe matching records , it does not save the records or own it

4. Why is the app scene's model container persistent while this lab's preview
   container is not suitable for testing relaunch persistence?

>The app container is intended to use persistent storage. The preview
     container requested by this lab uses `inMemory: true`, so its data is
     disposable and cannot establish relaunch persistence.

Tell the tutor when the implementation, predictions, and explanations are ready.
Do not run the interaction sequence yet.

## Tutor review 1 — revise before running

What is already correct:

- `PantryItem` has the required model annotation, mutable properties, and
  initializer.
- The view obtains a context, queries `PantryItem`, displays query-derived state,
  and inserts one new instance from each button.
- No parallel array is kept in `@State`.
- The zero-item and one-item predictions match the implementation.

Revise these four points in the original sections above:

1. Add the relevant `App` scene code. The persistent model container must be
   attached to the `WindowGroup` that creates `PersistentItemsView`.
2. Give the standalone preview its own model container and make that container
   explicitly in-memory, as shown in **New syntax**.
3. Recalculate both two-record row predictions. Follow the declared query sort,
   not the order in which the buttons were pressed.
4. Rewrite explanations 3 and 4 using these distinctions:
   - `@Query` retrieves and observes matching records; it does not own or save
     them.
   - The app container is intended to use persistent storage. The preview
     container requested by this lab uses `inMemory: true`, so its data is
     disposable and cannot establish relaunch persistence.

Leave the interaction sequence unrun, then tell the tutor when the revision is
ready.

## Tutor review 2 — approved after prediction correction

The implementation and role explanations are ready for execution after correcting
the two-record predictions. `@Query(sort: \PantryItem.name)` returns the records
in ascending name order; `ForEach` displays that query order, not insertion order.

Before running, correct the two affected prediction cells above. Then preserve
those predictions and record only observed results in this table:

| Moment                                 | Actual count label | Actual rows        |
| -------------------------------------- | ------------------ | ------------------ |
| First launch with a fresh store        | Stored items: 0    | None               |
| After pressing `Add Milk` once         | Stored items: 1    | Milk: 1            |
| After pressing `Add Eggs` once         | Stored items: 2    | Eggs: 6<br>Milk: 1 |
| After stopping and relaunching the app | Stored items: 0    | None               |

Also record any compiler or runtime error exactly as Xcode reports it:

> TODO: none

Use only one `@main` app declaration in the target. If Xcode already generated an
`App` type, add the model-container modifier to that existing scene rather than
creating a second `@main` type.

## Persistence diagnostic rerun

The first Simulator run showed both records during the process but showed zero
after a quick Xcode stop and relaunch. Preserve that actual result: it is evidence
that query observation worked, but it does not demonstrate a completed disk save.

Current hypothesis: Xcode stopped the process before the context's implicit
autosave occurred. Autosave timing is not a fixed-duration guarantee, so test a
documented UI lifecycle opportunity instead of guessing a wait time.

Before rerunning, predict the final state:

> After adding Milk and Eggs, sending the app to the background, stopping it, and
> relaunching it, I predict: TODO

Then perform this sequence without changing the code:

1. Launch the app and confirm it currently shows zero records.
2. Press `Add Milk` once and `Add Eggs` once; confirm both rows appear.
3. Send the Simulator app to the background by going to its Home Screen.
4. Once the Home Screen is visible, pause briefly, then stop the run in Xcode.
5. Run the app again and record the result below.

| Diagnostic moment                    | Actual count label | Actual rows        |
| ------------------------------------ | ------------------ | ------------------ |
| Before adding                        | Stored items: 0    | None               |
| After both inserts                   | Stored items: 2    | Eggs: 6<br>Milk: 1 |
| After background, stop, and relaunch | Stored items: 2    | Eggs: 6<br>Milk: 1 |

Exact compiler/runtime error, if any:

> TODO: none

Okay it works now, i added these:

## Tutor review 3 — separate explicit save from autosave

The latest result verifies persistent storage through explicit
`modelContext.save()`. It does not verify the background-autosave hypothesis,
because the run introduced explicit saves while also adding the background step.

Run one controlled comparison:

1. Keep the two records that are currently persisted.
2. Remove only the two `do`/`catch` save blocks from the Xcode implementation;
   leave both `modelContext.insert(...)` calls intact.
3. Before running, complete this prediction:

> Starting with two stored records, after inserting Milk and Eggs once more,
> backgrounding, stopping, and relaunching, I predict the count and rows will be:
> Stored items: 2, 
> Eggs: 12
> Milk: 2

4. Run and record each moment without changing the code again.

| Controlled-autosave moment                     | Actual count label | Actual rows                              |
| ---------------------------------------------- | ------------------ | ---------------------------------------- |
| Relaunch with the two explicitly saved records | Stored items: 2    | Eggs: 6<br>Milk: 1                       |
| After one more Milk and one more Eggs          | Stored items: 4    | Eggs: 6<br>Eggs: 6<br>Milk: 1<br>Milk: 1 |
| After background, stop, and relaunch           | Stored items: 4    | Eggs: 6<br>Eggs: 6<br>Milk: 1<br>Milk: 1 |

Exact compiler/runtime error, if any:

> TODO: none

Do not replace the earlier results. They are evidence from different experimental
conditions.
```
HStack {
	Button("Add Milk", action: {
		modelContext.insert(PantryItem(name: "Milk", quantity: 1))
		
		do {
			try modelContext.save()
			print("✅ Milk saved")
		} catch {
			print("❌ Save failed: \(error)")
		}
	})
	.buttonStyle(.borderedProminent)
	
	Button("Add Eggs", action: {
		modelContext.insert(PantryItem(name: "Eggs", quantity: 6))
		
		do {
			try modelContext.save()
			print("✅ Eggs saved")
		} catch {
			print("❌ Save failed: \(error)")
		}
	})
	.buttonStyle(.borderedProminent)
}
```

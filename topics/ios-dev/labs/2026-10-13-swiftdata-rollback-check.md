# Check a state-changing error path

## Purpose

Your validator tests checked an outcome. An update test must also check the
state left behind. Here, a record starts at a saved quantity of 9, an update
attempt changes it to 12, and a deliberately thrown error exercises recovery.

Use a separate Swift Playground file. This fixture uses its own in-memory
SwiftData container and turns autosave off. It does not use your shopping app's
container or records. Saving here establishes a baseline within this run; this
is not a relaunch-persistence test.

The `simulateFailure` flag is an exercise-only switch. When true, our code throws
before `context.save()` is called. This tests the catch/rollback path with real
SwiftData state; it does not demonstrate an error originating inside SwiftData's
save implementation. There is no row UI or draft in this exercise.

## Your task

The fixture is supplied so you can focus on recovery and checks:

1. Complete the update function's catch: restore pending context changes and
   return the failure result. Replace the `fatalError` placeholder.
2. After the supplied update call, write two assertions: one for the required
   result and one for the required model quantity. `UpdateOutcome` supports `==`.
3. Run and record the actual output or diagnostic.

The update receives an already validated positive integer; input validation is
outside this exercise's scope. There are no unrelated pending changes.

## Implementation

Keep the model and helper function outside `#Playground` as shown.

```swift
import Playgrounds
import SwiftData

@Model
final class RollbackLabItem {
    var quantity: Int

    init(quantity: Int) {
        self.quantity = quantity
    }
}

enum UpdateOutcome: Equatable {
    case updated
    case failed
}

enum LabSaveError: Error {
    case simulated
}

func updateForLab(
    item: RollbackLabItem,
    newQuantity: Int,
    context: ModelContext,
    simulateFailure: Bool
) -> UpdateOutcome {
    item.quantity = newQuantity

    do {
        if simulateFailure {
            throw LabSaveError.simulated
        }
        try context.save()
        return .updated
    } catch {
        context.rollback()
        return .failed
    }
}

#Playground {
    do {
        let configuration = ModelConfiguration(
            isStoredInMemoryOnly: true,
            cloudKitDatabase: .none
        )
        let container = try ModelContainer(
            for: RollbackLabItem.self,
            configurations: configuration
        )
        let context = ModelContext(container)
        context.autosaveEnabled = false

        let item = RollbackLabItem(quantity: 9)
        context.insert(item)
        try context.save()

        let result = updateForLab(
            item: item,
            newQuantity: 12,
            context: context,
            simulateFailure: true
        )
        
        assert(result == .failed, "Expected .failed result!")
        assert(item.quantity == 9, "Expected required model quantity 9!")
        
        print("Rollback checks passed.")
    } catch {
        // A fixture setup failure must not look like a passing test.
        assertionFailure("Lab setup failed: \(error)")
    }
}


```

The outer catch handles failures while creating the fixture or saving its initial
record. The update function handles its own simulated error and returns a result.

## Actual run

Initial run, preserved by the tutor from the earlier worksheet submission:

```text
XCPreviewAgent crashed due to assert in Playground.swift at line 42.
Expected .updated result!
```

That attempt expected `.updated` and quantity 12 despite simulated failure.
The result assertion failed first; the quantity assertion was not reached.

After correcting the conditions to `.failed` and quantity 9:

```text
Rollback checks passed.
```

Tell the tutor when ready for review. Keep attempted code if you get stuck.

## Final experiment — missing recovery

Your assertion conditions are correct. First correct the quantity assertion's
message to say 9, matching its condition.

In this isolated Playground only, temporarily comment out `context.rollback()`.
Keep `return .failed`, `simulateFailure: true`, and both assertions unchanged.

Before running, predict:

- Which assertion will fail, and why does the other assertion not detect this
  bug? the assert(item.quantity == 9, "Expected required model quantity 9!") one, because the other assertion just detects the returned result, this one detects the quantity which will be 12 , because it didn't rollback

Run from the beginning so the supplied fixture creates a fresh saved baseline.

Actual failure message:

```text
XCPreviewAgent crashed due to assert in Playground.swift at line 42.

Expected required model quantity 9!
```

Restore `context.rollback()` and rerun. Keep the final implementation above in
its restored form.

Actual output after restoring rollback:

```text
Rollback checks passed.
```

Tell the tutor when ready for review.

## References

- [Apple: ModelContext](https://developer.apple.com/documentation/swiftdata/modelcontext)
  — rollback restores changed models to their latest saved state and discards
  pending inserts/deletes.
- [Apple: autosaveEnabled](https://developer.apple.com/documentation/swiftdata/modelcontext/autosaveenabled)
  — controls automatic context saves.

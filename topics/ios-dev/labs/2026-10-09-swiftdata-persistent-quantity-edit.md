# SwiftData persistent quantity editing — design probe

## Purpose

Plan the smallest migration of quantity editing from the disconnected in-memory
shopping path to the active SwiftData path.

Do not change the Xcode source yet.

Current persistent state: `Milk: 5`. Eggs was successfully deleted and that
deletion survived relaunch.

## Intended interaction

Each persistent row will eventually have a small child editor containing:

- the current item display;
- a local quantity text draft;
- a Save button;
- feedback from the Save attempt.

Typing must not immediately change the stored quantity. The persistent model
changes only when Save receives a valid positive whole number and the context
save succeeds.

## Part 1 — Ownership and interface

For each value below, choose its owner and mechanism. Use descriptions such as
the queried `ShoppingItem`, child-local `@State`, or a parent-created action.

| Value or operation | Owner/mechanism | Why? |
| --- | --- | --- |
| Accepted item quantity | TODO | TODO |
| Unsaved quantity text | TODO | TODO |
| Operation that changes and saves the persistent model | TODO | TODO |
| Feedback for one row's latest Save attempt | TODO | TODO |

The child must request a save using its draft and receive a finite result. Write
the action's function type only—do not implement it yet:

```swift
// let onSaveQuantity: TODO
```

## Part 2 — Result design

Design `PersistentUpdateResult` for exactly these outcomes:

1. update saved successfully; carry name, old quantity, and new quantity;
2. draft is not a positive whole number;
3. context save failed; carry the item name.

Because the action receives an exact queried item, do not add empty-name or
not-found cases.

```swift
// TODO
```

Why are empty-name and not-found results unnecessary in this interface?

> TODO

## Part 3 — Operation trace

Complete the trace. Validation must finish before the persistent model is
changed. Capture presentation/result data before mutation.

```text
receive selected item and quantity text
  -> convert and validate TODO
  -> if invalid: TODO
  -> capture TODO and TODO
  -> change TODO
  -> do:
       TODO
       TODO
  -> catch:
       TODO
       TODO
```

## Part 4 — Predict before implementation

Assume `Milk: 5` is stored, the row's draft begins empty, and success clears the
draft while either failure preserves it.

| Moment | Displayed stored quantity | Draft | Feedback | Why? |
| --- | ---: | --- | --- | --- |
| Relaunch | TODO | TODO | TODO | TODO |
| Type `9`, before Save | TODO | TODO | TODO | TODO |
| Tap Save and receive success | TODO | TODO | TODO | TODO |
| Stop immediately and relaunch | TODO | TODO | TODO | TODO |
| Type `0` and tap Save | TODO | TODO | TODO | TODO |

Use these feedback messages:

- initial: `No update attempted.`
- success: `Updated NAME from OLD to NEW.`
- invalid: `Quantity must be a positive whole number.`
- save failure: `Failed to update NAME.`

Complete all four parts before changing Xcode, then tell the tutor the worksheet
is ready for review.

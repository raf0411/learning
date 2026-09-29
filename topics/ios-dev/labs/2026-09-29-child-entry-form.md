# Extract a child entry form with bindings

## Learning target

Let a child view edit two parent-owned draft strings while the parent retains the
ShoppingList and performs Add through an action closure.

## Interface reasoning

Learner choices:

1. Name draft — binding, so child edits update the parent.
2. Quantity draft — binding, for the same reason.
3. Add tap — action closure, so the parent still performs model mutation.

These choices are correct. More precisely, a binding is a get/set connection to
the parent's storage rather than a copied source value.

```text
Child TextField -- writes through Binding --> parent @State draft
Child Add button -- calls action closure ---> parent Add logic
Parent clears draft -- updates @State ------> child TextField displays empty
```

## New syntax

A child declares a binding property with `@Binding`:

```swift
@Binding var name: String
```

Inside that child, `name` is the current String value and `$name` is the binding
passed to controls such as `TextField`. When constructing the child, the parent
passes its projected binding, such as `$name`.

## Build the child form

Refactor the current screen:

1. Create `ShoppingEntryForm: View`.
2. Give it two binding properties named `name` and `quantity`.
3. Give it an `onAdd: () -> Void` action.
4. Move both TextFields and the Add button into the child.
5. Bind the child's TextFields to its two binding properties.
6. The child Add button calls `onAdd()` exactly once.
7. In `ContentView`, construct the child with bindings to the existing parent
   drafts and a closure containing the existing Add/result-switch logic.
8. Keep `ShoppingList`, `status`, the count, and all rows in `ContentView`.
9. Do not create new draft, list, count, or status state in the child.

Paste the child and the parent's `ShoppingEntryForm(...)` construction:

```swift
// TODO: ShoppingEntryForm

// TODO: construction in ContentView
```

## Predict before running

Start from a fresh run and perform the attempts in order. Fill the prediction
table before running.

| Moment | Predicted count | Predicted status | Predicted child fields afterward |
|---|---|---|---|
| Launch | TODO | TODO | TODO |
| Enter `"  Rice  "` / `"2"`, then tap Add | TODO | TODO | TODO |
| Enter `"Milk"` / `"99"`, then tap Add | TODO | TODO | TODO |

Leave actual results empty until the tutor reviews the source and predictions.

| Moment | Actual count | Actual status | Actual child fields afterward |
|---|---|---|---|
| Launch | TODO | TODO | TODO |
| After adding Rice | TODO | TODO | TODO |
| After attempting duplicate Milk | TODO | TODO | TODO |

## Explain the two directions

After the run, explain both paths:

1. How typing in the child changes the parent's draft.
2. How the parent clearing its draft makes the child's field become empty.

> TODO after running

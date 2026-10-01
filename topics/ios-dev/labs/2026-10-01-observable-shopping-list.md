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
// TODO: ShoppingList

// TODO: ShoppingSummaryView

// TODO: ContentView
```

## Choose checks and predict

Choose exact inputs for a successful Add, a rejected Add, and a successful Remove.
Start with a fresh launch and perform the checks in that order. Predict the two
displayed counts after each operation. Leave Actual empty until source review.

| Check | Exact inputs / action | Predicted parent count | Predicted summary count | Actual counts |
|---|---|---|---|---|
| Successful Add | TODO | TODO | TODO | |
| Rejected Add | TODO | TODO | TODO | |
| Successful Remove | TODO | TODO | TODO | |

## Ownership check

Suppose you accidentally pass a newly constructed `ShoppingList()` into the
summary instead of the parent's model. After adding an item through the parent,
would the two counts agree? Explain why.

> TODO

Tell the tutor when the code and predictions are ready. Preserve predictions if
a later run differs; record the actual result separately.

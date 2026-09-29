# Extract a read-only shopping-item row

## Learning target

Separate row presentation into a child view while keeping `ShoppingList`
ownership in `ContentView`.

## Initial reasoning

Given this child:

```swift
struct ShoppingItemRow: View {
    let item: ShoppingItem

    var body: some View {
        Text("\(item.name) — quantity: \(item.quantity)")
    }
}
```

Learner answers:

1. `ContentView` owns the `ShoppingList`.
2. `ShoppingItemRow` receives a `ShoppingItem` value.
3. Initial prediction: mutating `item.quantity` would compile but would change
   only a copy.

Correction to answer 3: the shown property is a `let` constant, so mutation does
not compile. Copy semantics would become relevant only after obtaining a mutable
copy; mutation of that separate copy would still not update the parent's array.

## Part 1 — extract the child

Update the app:

1. Define `ShoppingItemRow` as a separate SwiftUI `View` with one
   `let item: ShoppingItem` property.
2. Move the existing row `Text` into its `body`.
3. In the parent's `ForEach`, create one `ShoppingItemRow(item: item)`.
4. Do not add `@State` or `@Binding` to the child.
5. Do not move `ShoppingList` ownership out of `ContentView`.

Paste the child and revised `ForEach`:

```swift
struct ShoppingItemRow: View {
    let item: ShoppingItem
    
    var body: some View {
        Text("\(item.name) — quantity: \(item.quantity)")
    }
}

ForEach(shoppingList.list) { item in
	ShoppingItemRow(item: item)
}
```

## Part 2 — observe the immutability boundary

After Part 1 builds, temporarily add this inside `ShoppingItemRow` beneath its
text:

```swift
Button("Increase") {
    item.quantity += 1
}
```

Build once and record Xcode's exact compiler error:

> /Users/raffi/Documents/swift/LearningSwiftUI/LearningSwiftUI/ContentView.swift:235:27 Left side of mutating operator isn't mutable: 'item' is a 'let' constant

Then remove the temporary button and confirm the app builds again:

> Success

## Part 3 — explain the normal update flow

Run the restored app and add Rice with quantity 2. Confirm that the Rice child row
appears, then explain how a child whose `item` property is `let` can nevertheless
display newly changed parent data.

Hint: distinguish mutating an existing child value from SwiftUI evaluating the
parent again and constructing child-view descriptions from the current array.

Rice row observed:

> Rice - quantity: 2

Explanation:

> Because Swift UI reevaluates the body again from the ForEach if there's any changes in the list, therefore it will re run ShoppingItemRow view again by passing a newly updated list, that contains the Rice now

## Tutor review — checkpoint complete

- The child accepts one read-only `ShoppingItem` value and does not own the list.
- The parent renders the child from `ForEach` without duplicating model state.
- Xcode produced the expected compile-time immutability error for mutation of the
  child's `let` property, and the restored source built successfully.
- Learner-reported execution showed the Rice row after parent state changed.
- The explanation correctly connected parent reevaluation to updated child data.
  More precisely, mutation of the parent's `@State` invalidates `ContentView`;
  its new body description supplies the updated collection to `ForEach`, and
  SwiftUI reconciles the child views by stable identity.

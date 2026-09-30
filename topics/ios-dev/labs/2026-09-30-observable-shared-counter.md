# Share one observable model across views

## Learning target

Create one class instance, let a parent own its lifetime, and let multiple views
read or mutate that same observable instance.

This exercise uses the Observation framework available to SwiftUI on iOS 17 and
later.

```text
ContentView
  @State owns one SharedCounter reference
                  |
          +-------+-------+
          |               |
          v               v
 CounterReadout     CounterControls
 reads count        calls increment()
          |               |
          +-------+-------+
                  |
                  v
       the same SharedCounter instance
```

Three ideas have different jobs:

- `class` gives reference semantics, so all three views can refer to one instance.
- `@Observable` lets SwiftUI track observable properties read by view bodies and
  refresh relevant UI after they change.
- Parent `@State` owns and preserves the model reference for that view identity.

The children receive an ordinary `SharedCounter` reference. This exercise does
not need `@Binding` or `@Bindable` because no control is asking for a projected
binding such as `$model.property`.

## New syntax

```swift
import SwiftUI
import Observation

@Observable
final class SharedCounter {
    var count = 0
}
```

Unlike a struct method, a class method that changes a property does not use the
`mutating` keyword.

## Build the experiment

Use a separate temporary SwiftUI file or Playground so the shopping app remains
intact.

1. Create `SharedCounter` as an `@Observable final class`.
2. Give it `var count = 0` and an `increment()` method that adds one.
3. Create `SharedCounterView` as the parent.
4. The parent owns one instance with
   `@State private var counter = SharedCounter()`.
5. The parent displays `Parent: COUNT`.
6. Create `CounterReadout` with an ordinary `let counter: SharedCounter`; it
   displays `Child: COUNT`.
7. Create `CounterControls` with an ordinary `let counter: SharedCounter`; its
   `Increment` button calls `counter.increment()`.
8. Add a `Reset` button in the parent that assigns `counter.count = 0`.
9. Do not create another `SharedCounter`, another count property, a binding, or a
   copy inside either child.

Paste the four types:

```swift
// TODO: SharedCounter

// TODO: SharedCounterView

// TODO: CounterReadout

// TODO: CounterControls
```

## Predict before running

Fill only the Prediction column, then stop for source review.

| Moment | Prediction | Actual |
|---|---|---|
| Launch: parent and child text | TODO | TODO |
| Tap child Increment twice: parent and child text | TODO | TODO |
| Tap parent Reset: parent and child text | TODO | TODO |
| Terminate and relaunch: parent and child text | TODO | TODO |

## Explain the mechanisms

1. Why do the parent and children access the same count even though no binding is
   passed?
2. What separate job does `@Observable` perform?
3. Why is `@Bindable` unnecessary in this experiment?

> 1. TODO
> 2. TODO
> 3. TODO


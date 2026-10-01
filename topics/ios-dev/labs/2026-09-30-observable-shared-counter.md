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
import SwiftUI
import Observation

@Observable
final class SharedCounter {
    var count = 0
    
    func increment() {
        count += 1
    }
}

struct SharedCounterView: View {
    @State private var counter = SharedCounter()
    
    var body: some View {
        Text("Parent: \(counter.count)")
        
        CounterReadout(counter: counter)
        
        CounterControls(counter: counter)
        
        Button("Reset", action: {
            counter.count = 0
        })
        .buttonStyle(.borderedProminent)
    }
}

struct CounterReadout: View {
    let counter: SharedCounter
    
    var body: some View {
        Text("Child: \(counter.count)")
    }
}

struct CounterControls: View {
    let counter: SharedCounter
    
    var body: some View {
        Button("Increment", action: {
            counter.increment()
        })
        .buttonStyle(.borderedProminent)
    }
}

#Preview {
    SharedCounterView()
}
```

## Predict before running

Fill only the Prediction column, then stop for source review.

| Moment                                           | Prediction            | Actual                |
| ------------------------------------------------ | --------------------- | --------------------- |
| Launch: parent and child text                    | Parent: 0 \| Child: 0 | Parent: 0 \| Child: 0 |
| Tap child Increment twice: parent and child text | Parent: 2 \| Child: 2 | Parent: 2 \| Child: 2 |
| Tap parent Reset: parent and child text          | Parent: 0 \| Child: 0 | Parent: 0 \| Child: 0 |
| Terminate and relaunch: parent and child text    | Parent: 0 \| Child: 0 | Parent: 0 \| Child: 0 |

## Explain the mechanisms

1. Why do the parent and children access the same count even though no binding is
   passed?
2. What separate job does `@Observable` perform?
3. Why is `@Bindable` unnecessary in this experiment?

> 1. Because we are using Class, which means both parent and children are using the same reference or shared property
> 2. umm, to make sure a Swift UI view can read the class and use its property or method, that's my guess
> 3. Because we r passing data with class? honest answer is idk, that's just a guess


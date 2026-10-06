# Persistent preference with `@AppStorage`

## Purpose

Practice the difference between temporary view state and a small preference that
survives app termination and relaunch.

Use an iOS app target and run this lab in the Simulator rather than relying only
on an Xcode preview. Do not run the interaction sequence until the tutor reviews
your implementation and predictions.

## New syntax

`@AppStorage` connects a Swift property to a value in `UserDefaults`. The string
is the persistent key, and the initial value is the default used when that key has
no saved value yet.

```swift
@AppStorage("some.stable.key") private var value = false
```

Like other SwiftUI property wrappers you have used, its projected value can be
passed to a control as `$value`.

## Requirements

Create `PreferencePersistenceView` with:

- one private `@AppStorage` Bool using the exact key
  `learning.ios.showCompleted.v1`
- a default value of `false`
- a Toggle titled `Show completed items` bound directly to the stored preference
- a label that displays exactly `Preference: On` or `Preference: Off`
- a button titled `Reset preference` that assigns `false`

Do not create a second `@State` property for this preference.

```swift
import SwiftUI

struct PreferencePersistenceView: View {
    @AppStorage("learning.ios.showCompleted.v1") private var showCompletedItems: Bool = false

    var body: some View {
        Toggle("Show completed items", isOn: $showCompletedItems)
        Text(showCompletedItems ? "Preference: On" : "Preference: Off")
        Button("Reset preference", action: {
            showCompletedItems = false
        })
        .buttonStyle(.borderedProminent)
    }
}

#Preview {
    PreferencePersistenceView()
}

```

## Predict before running

Assume the key has never been saved before. Perform the moments in order.

| Moment                                    | Predicted label | Predicted toggle | Actual label    | Actual toggle |
| ----------------------------------------- | --------------- | ---------------- | --------------- | ------------- |
| First launch with a fresh key             | Preference: Off | off              | Preference: Off | off           |
| After turning the toggle on               | Preference: On  | on               | Preference: On  | on            |
| After terminating and relaunching the app | Preference: On  | on               | Preference: On  | on            |
| After pressing `Reset preference`         | Preference: Off | off              | Preference: Off | off           |
| After terminating and relaunching again   | Preference: Off | off              | Preference: Off | off           |

## Explain before running

1. Why is `false` used on the first launch, but not after the user has saved
   `true`?

> key absent  → use the declared default (`false`)
key present → load its saved value, after we relaunch the app it will be whatever it was saved before because it has the key, for example if we toggle it to true before we terminate, it will stay true, because we provide the key

2. Why can the Toggle use `$showCompletedItems` without `@Bindable`?

> Because @AppStorage itself supplies the projected binding

3. Why would separate `@AppStorage` values be a poor fit for an editable
   collection of shopping-item records?

> if we use @AppStorage, we would need to provide the keys for each shopping item properties one by one, which would be a hassle, its better to use SwiftData models to store the shopping item records in a query collections

Tell the tutor when the implementation, predictions, and explanations are ready.
Do not run the interaction sequence yet.

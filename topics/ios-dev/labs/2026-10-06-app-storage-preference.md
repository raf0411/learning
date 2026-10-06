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

// TODO: PreferencePersistenceView

#Preview {
    PreferencePersistenceView()
}
```

## Predict before running

Assume the key has never been saved before. Perform the moments in order.

| Moment | Preference label | Toggle |
| --- | --- | --- |
| First launch with a fresh key | TODO | TODO |
| After turning the toggle on | TODO | TODO |
| After terminating and relaunching the app | TODO | TODO |
| After pressing `Reset preference` | TODO | TODO |
| After terminating and relaunching again | TODO | TODO |

## Explain before running

1. Why is `false` used on the first launch, but not after the user has saved
   `true`?

> TODO

2. Why can the Toggle use `$showCompletedItems` without `@Bindable`?

> TODO

3. Why would separate `@AppStorage` values be a poor fit for an editable
   collection of shopping-item records?

> TODO

Tell the tutor when the implementation, predictions, and explanations are ready.
Do not run the interaction sequence yet.

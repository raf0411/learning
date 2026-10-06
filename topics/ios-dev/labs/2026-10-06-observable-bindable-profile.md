# Observable model bindings

## Purpose

Practice when an ordinary observable-model reference is sufficient and when a
child needs `@Bindable` to give a writable SwiftUI control a `Binding`.

Build this as a separate small view in your current Xcode project or playground.
Use `import SwiftUI` and `import Observation`.

## Requirements

Create an observable final class named `Profile` with:

- a writable `nickname` property initially equal to `"Guest"`
- a writable `receivesReminders` property initially equal to `false`

Create `ProfileHostView` that:

- owns one `Profile` instance in private `@State`
- displays `Parent nickname: VALUE`
- displays `Parent reminders: On` or `Parent reminders: Off`
- passes the same profile instance to `ProfileEditor`
- has a `Reset` button that restores `"Guest"` and `false`

Create `ProfileEditor` that:

- receives the observable profile using the wrapper needed to create bindings
- has a `TextField` that directly edits `nickname`
- has a `Toggle` titled `Receive reminders` that directly edits
  `receivesReminders`

Do not create a second `Profile` instance in the child. Do not add separate draft
state for these two controls.

```swift
// TODO: Profile

// TODO: ProfileHostView

// TODO: ProfileEditor

#Preview {
    ProfileHostView()
}
```

## Predict before running

Start from a fresh preview. Replace the contents of the nickname field with
`Raffi`, turn reminders on, and then press the parent's Reset button.

| Moment | Parent nickname label | Child nickname field | Parent reminder label | Child toggle |
|---|---|---|---|---|
| Fresh launch | TODO | TODO | TODO | TODO |
| After entering `Raffi` | TODO | TODO | TODO | TODO |
| After turning reminders on | TODO | TODO | TODO | TODO |
| After parent Reset | TODO | TODO | TODO | TODO |

Leave actual results empty until the tutor reviews the implementation and
predictions.

## Explain the two directions

1. When the child text field changes, trace the change from the control to the
   parent label.

> TODO

2. When the parent Reset button changes `profile.nickname`, trace the change to
   the child's text field.

> TODO

3. Which view owns the profile's lifetime? What job does `@Bindable` perform in
   the child, and what job does it *not* perform?

> TODO

Tell the tutor when the code, predictions, and explanations are ready. Do not run
the interaction sequence until after source review.

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
import SwiftUI
import Observation

@Observable
final class Profile {
    var nickname = "Guest"
    var receivesReminders = false
}

struct ProfileHostView: View {
    @State private var profile: Profile = Profile()
    
    var body: some View {
        VStack(alignment: .center, spacing: 32) {
            Text("Parent nickname: \(profile.nickname)")
            Text(profile.receivesReminders ? "Parent reminders: On" : "Parent reminders: Off")
            
            ProfileEditor(profile: profile)
            
            Button("Reset", action: {
                profile.nickname = "Guest"
                profile.receivesReminders = false
            })
            .buttonStyle(.borderedProminent)
        }
    }
}

struct ProfileEditor: View {
    @Bindable var profile: Profile
    
    var body: some View {
        VStack(spacing: 32) {
            TextField("Edit nickname", text: $profile.nickname)
                .textFieldStyle(.roundedBorder)
            
            Toggle("Receive reminders", isOn: $profile.receivesReminders)
        }
        .padding(32)
    }
}

#Preview {
    ProfileHostView()
}
```

## Predict before running

Start from a fresh preview. Replace the contents of the nickname field with
`Raffi`, turn reminders on, and then press the parent's Reset button.

| Moment                     | Parent nickname label  | Child nickname field | Parent reminder label | Child toggle |
| -------------------------- | ---------------------- | -------------------- | --------------------- | ------------ |
| Fresh launch               | Parent nickname: Guest | Guest                | Parent reminders: Off | off          |
| After entering `Raffi`     | Parent nickname: Raffi | Raffi                | Parent reminders: Off | off          |
| After turning reminders on | Parent nickname: Raffi | Raffi                | Parent reminders: On  | on           |
| After parent Reset         | Parent nickname: Guest | Guest                | Parent reminders: Off | off          |

## Actual results

Run the sequence only after the tutor has reviewed the implementation and
predictions. Replace each `TODO` with exactly what you observe.

| Moment                     | Parent nickname label  | Child nickname field | Parent reminder label | Child toggle |
| -------------------------- | ---------------------- | -------------------- | --------------------- | ------------ |
| Fresh launch               | Parent nickname: Guest | Guest                | Parent reminders: Off | off          |
| After entering `Raffi`     | Parent nickname: Raffi | Raffi                | Parent reminders: Off | off          |
| After turning reminders on | Parent nickname: Raffi | Raffi                | Parent reminders: On  | on           |
| After parent Reset         | Parent nickname: Guest | Guest                | Parent reminders: Off | off          |

## Explain the two directions

1. When the child text field changes, trace the change from the control to the
   parent label.

>TextField → binding setter → Profile property → Observation → parent label

2. When the parent Reset button changes `profile.nickname`, trace the change to
   the child's text field.

> Reset action → Profile property → Observation → binding getter → child control

3. Which view owns the profile's lifetime? What job does `@Bindable` perform in
   the child, and what job does it *not* perform?

`ProfileHostView` owns the model’s lifetime and `@Bindable` does not create or own a second `Profile`. Also describe `$profile.nickname` as a get/set connection, not as “the same value.”

Tell the tutor when the code, predictions, and explanations are ready. Do not run
the interaction sequence until after source review.

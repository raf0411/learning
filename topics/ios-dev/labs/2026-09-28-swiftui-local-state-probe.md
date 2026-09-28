# SwiftUI local-state implementation probe

This is a boundary probe, not a pass/fail exam. It will show what you can already
implement and what should be taught first in the guided SwiftUI practice app.

Do not look up a completed counter implementation. You may use Xcode completion
and compiler messages.

## 1. Prediction before coding

### State choice

What SwiftUI feature or property wrapper will hold the count inside this view, and
why is it suitable here?

> @State var counter: Int = 0
> because @State is a property in Swift that is useful for dynamical changes in UI in SwiftUI, or thats what I've understood

### Behavior prediction

Complete this table before running the app.

| Action                                                          | Predicted displayed text |
| --------------------------------------------------------------- | ------------------------ |
| Fresh launch                                                    | Count: 0                 |
| Tap **Add One** twice                                           | Count: 1                 |
| Tap **Reset**                                                   | Count: 0                 |
| Tap **Add One** three times, terminate the app, and relaunch it | Count: 0                 |

## 2. Implementation brief

Create or replace `ContentView` in a SwiftUI app so it contains:

- A title reading `Tap Counter`.
- Text displaying `Count: 0` initially and the current value afterward.
- An `Add One` button that increases the count by exactly one.
- A `Reset` button that restores the count to zero.

Keep the state local to `ContentView`. Do not add persistence, an observable model,
or another screen for this probe.

Paste your implementation:

```swift
struct ContentView: View {
    @State private var count = 0
    
    var body: some View {
        VStack {
            Text("Tap Counter")
                .font(.title)
                .padding()
            
            Spacer()
            
            Text("Count: \(count)")
            
            Spacer()
            
            Button("Add One", action: {
                count += 1
            })
            .buttonStyle(.glassProminent)
            
            Button("Reset", action: {
                count = 0
            })
            .buttonStyle(.glass)
        }
    }
}
```

## 3. Run evidence

Perform the four actions from the prediction table in order. Fully terminate and
relaunch the simulator app for the final action; rebuilding a preview is not the
same observation.

| Action                                               | Actual displayed text | Prediction matched? |
| ---------------------------------------------------- | --------------------- | ------------------- |
| Fresh launch                                         | Count: 0              | Yes                 |
| Tap **Add One** twice                                | Count: 2              | No                  |
| Tap **Reset**                                        | Count: 0              | Yes                 |
| Tap **Add One** three times, terminate, and relaunch | Count: 0              | Yes                 |

## 4. Explanation after running

In your own words, explain why tapping a button can change the displayed text and
why the value after relaunch behaves as observed.

> once a button is tapped, swift ui mutates @State because we tap the button right, then swift ui updates it, the body evaluates, then displays the new text
> Also explain separately why a full relaunch starts from zero:
> Because @State only store in memory data in the ContentView only, so when we exit, the stored memory is gone, and thats why it resets, it doesn't persists in the memory

## Ready for review

- [ ] I completed the predictions before running.
- [ ] I wrote the view without copying a completed implementation.
- [ ] I ran all four observations and completed the explanation.

## Tutor review 1

### What the probe demonstrated

- You independently selected `@State` and implemented a working view.
- `Add One` changes the value by one, and `Reset` restores zero.
- The title and dynamic count text satisfy the brief.
- The simulator evidence shows that the value is not preserved across termination
  and relaunch.

### Evidence correction

The prediction after two taps was `1`, while the actual result was `2`. That row's
`Prediction matched?` value must therefore be `No`.

The tables ask for the displayed text, not only the numeric value. Rewrite the
entries exactly as the UI shows them—for example, `Count: 0` rather than `0`.

### SwiftUI mental model

`counter` or `count` is the property. `@State` is a **property wrapper** used when
the view owns a small mutable source of truth.

```text
button tap
    |
    v
button action mutates @State
    |
    v
SwiftUI schedules an update
    |
    v
body is evaluated again
    |
    v
Text reads the new count and displays it
```

SwiftUI is not asking you to find and manually edit an existing `Text` object.
Your `body` describes what the UI should look like for the current state; SwiftUI
uses the new description to update the rendered interface.

`@State` keeps the value alive for this view's identity while the app is running,
but it is not persistent storage. Terminating the app destroys that in-memory
state. A new launch creates `ContentView` again and initializes `count` to zero.

Because this state belongs only to `ContentView`, express that ownership in the
code as:

```swift
@State private var count = 0
```

### Revision task

1. Correct both tables using the complete displayed text and mark the mismatched
   two-tap prediction honestly.
2. Make `count` private in the pasted implementation.
3. Replace your explanation with your own account of this sequence:

   ```text
   mutation -> SwiftUI update -> body evaluation -> new displayed text
   ```

   Also explain separately why a full relaunch starts from zero.

- [ ] Both tables contain the complete `Count: N` text.
- [ ] The two-tap mismatch is marked `No`.
- [ ] The state declaration is private.
- [ ] The revised explanation covers both UI updating and relaunch behavior.

## Tutor review 2 — preserve prediction evidence

Learner clarification: the original prediction of `1` came from misreading
"twice" as "once." Treat this as a requirement-reading error, not dishonesty and
not evidence that the learner believes two increments produce one. The original
prediction should remain visible only so the prediction-to-observation record is
accurate.

### Correct revisions

- `count` is now `private`, accurately expressing view-local ownership.
- The explanation recognizes that `@State` is in-memory state, not persistent
  storage.
- The update sequence is mostly correct.

### Do not rewrite a prediction after observing the result

The original two-tap prediction was `1`. After the simulator showed `2`, the
prediction cell was changed to `2` and the comparison was marked `Yes`. That erases
the evidence needed for learning.

A prediction is a timestamped belief, not an answer key. Once the experiment has
run, preserve the original prediction even when it is wrong:

```text
original prediction: Count: 1
actual observation:  Count: 2
matched?:            No
```

Restore that row accordingly. Formatting corrections are allowed, so add the
literal `Count: ` prefix to every prediction and actual-value cell without changing
the originally predicted number.

### Tighten the causal explanation

SwiftUI does not mutate the state merely because a button was tapped. The button's
action closure runs, and **your line** `count += 1` mutates the state. SwiftUI
observes that state change, schedules an update, reevaluates `body`, and renders the
new description.

Also distinguish app termination from merely leaving or backgrounding the app. The
tested event was full termination: the process and its in-memory `@State` storage
ended. On the next launch, a new view starts from its declared initial value. The
count was not written to persistent storage.

### Final probe revision

1. Restore the original two-tap prediction as `Count: 1`.
2. Record its actual value as `Count: 2` and its match as `No`.
3. Add `Count: ` to every other predicted and actual value.
4. Adjust the explanation so the action closure—not SwiftUI itself—performs the
   mutation, and refer specifically to full termination.

- [ ] The original incorrect prediction remains visible.
- [ ] Every displayed value is recorded exactly as `Count: N`.
- [ ] The explanation assigns mutation to the button action closure.
- [ ] The relaunch explanation refers to termination and lack of persistence.

## Tutor review 3 — probe complete

Final chat explanation:

- The button action closure contains the mutation; specifically, `count += 1`
  changes the state. SwiftUI then schedules an update, reevaluates `body`, and
  renders the new count.
- Full termination destroys the in-memory `@State`. Because it was not written to
  persistent storage, a new launch initializes `count` to zero.

Assessment:

- Small single-view `@State` implementation — **INDEPENDENT** in this probe.
- Explanation of property-wrapper ownership, body reevaluation, and state lifetime
  — **GUIDED**.
- The incorrect two-tap prediction was caused by reading "twice" as "once," not by
  a misconception about increment behavior.

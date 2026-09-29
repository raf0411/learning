# Shopping entry: draft and submitted value

## Purpose

Build the first input interaction for the shopping-list practice app. This small
exercise remembers only the most recently added name. We will connect input to
the full shopping-list model after this interaction works.

Typing changes a draft. Pressing Add accepts that draft. Editing the next draft
should not change the previously accepted name.

## 1. Build from this brief

Create a SwiftUI view in Xcode with:

- A text field labeled `Item name`, initially empty.
- An `Add` button.
- A text label initially showing `No item added`.

When Add is tapped:

- Trim whitespace and newlines from both ends of the draft.
- If the cleaned name is empty, leave the draft and previous result unchanged.
- Otherwise, remember the cleaned name, display `Last added: NAME`, and clear
  the text field.

Typing or deleting text alone must not change the last-added label. A later
successful Add replaces the remembered name. Keep this exercise in memory only.

Choose the state properties yourself. Use the Swift and SwiftUI tools you have
already practiced. You may consult Xcode completion and compiler errors.

## 2. Predict before running

These actions happen in order in one run. Quotation marks below delimit input;
do not type the quotation marks. Use `""` for an empty field in your answers.

| Action                              | Text field afterward | Complete result label afterward |
| ----------------------------------- | -------------------- | ------------------------------- |
| Launch the view                     | ""                   | No item added                   |
| Type `"  Milk  "`, then tap Add     | ""                   | Last added: Milk                |
| Type `"Bread"`, without tapping Add | Bread                | Last added: Milk                |
| Tap Add                             | ""                   | No item added                   |
| Type three spaces, then tap Add     | ""                   | No item added                   |

## 3. Your implementation

Paste your view here after writing it yourself:

```swift
struct ContentView: View {
    @State private var name = ""
    @State private var nameText = ""
    
    var body: some View {
        VStack(spacing: 32) {
            TextField("Item name", text: $nameText)
                .textFieldStyle(.roundedBorder)
            
            Button("Add", action: {
                var cleanName = nameText.trimmingCharacters(in: .whitespacesAndNewlines)
                
                if cleanName.isEmpty {
                    cleanName = ""
                }
                
                nameText = ""
                name = cleanName
            })
            .buttonStyle(.borderedProminent)
            
            if name.isEmpty {
                Text("No item added")
            } else {
                Text("Last added: \(name)")
            }
        }
        .padding()
    }
}
```

## 4. Run and observe

Run the sequence above. Keep your original predictions if they differ from what
you observe.

| Action                              | Actual text field | Actual result label |
| ----------------------------------- | ----------------- | ------------------- |
| Launch the view                     | ""                | ""                  |
| Type `"  Milk  "`, then tap Add     | ""                | Last added: Milk    |
| Type `"Bread"`, without tapping Add | Bread             | Last added: Milk    |
| Tap Add                             | ""                | No item added       |
| Type three spaces, then tap Add     | ""                | No item added       |

If something differs, record the relevant compiler message or observed behavior:

> I misread my testing, it was actually No item added at first launch.

## 5. Explain one design choice

Which state does the text field edit, and what prevents typing the next item
from changing the last-added label?

> I use a separate @State variable so there is nameText for the textfield and @State name for the label, this prevents typing the next item from changing the last-added label

## Tutor review 1 — 2026-09-29

### What works

- You independently chose two private state properties and bound the field to
  `nameText`. Your explanation correctly separates the draft from the accepted
  name.
- The successful Add path trims the draft, stores the cleaned name, and clears
  the field. Typing the next draft leaves the previous accepted name alone.

### Fix the invalid-input path

When `cleanName.isEmpty` is true, assigning `cleanName = ""` leaves it exactly as
it already was. Execution then continues to both state assignments below the
`if`. That clears the draft and erases the previous accepted name.

The requirement is to leave BOTH state properties unchanged on invalid input.
Adjust the control flow so neither state assignment runs for an empty cleaned
name. Choose the Swift syntax yourself; keep the successful path working.

### Resolve the observation mismatch

Two reported observations do not match the pasted code and specified sequence:

- At launch, `name` is empty, so this code displays `No item added`, not an empty
  label.
- After typing `Bread` and tapping Add, this code assigns `Bread` to `name`, so it
  displays `Last added: Bread`, not `No item added`.

These are predictions from reading your code, not tutor-observed simulator output.
The exact code that ran or the actions performed may differ from this worksheet.
Also, the reported empty launch label differs from your launch prediction, so
`No differences` does not match the two tables.

Keep the original tables as the record of your first attempt.

### Revision and fresh run

1. Confirm the view displayed in Xcode is the one you are editing.
2. Repair invalid-input handling and put the revised view below.
3. Start a fresh run with both state properties empty. Repeat the exact sequence
   and record what you actually see. Use `"   "` for three spaces and `""` for
   an empty field, so the difference is visible in the record.

```swift
struct ContentView: View {
    @State private var name = ""
    @State private var nameText = ""
    
    var body: some View {
        VStack(spacing: 32) {
            TextField("Item name", text: $nameText)
                .textFieldStyle(.roundedBorder)
            
            Button("Add", action: {
                var cleanName = nameText.trimmingCharacters(in: .whitespacesAndNewlines)
                
                if !cleanName.isEmpty {
                    nameText = ""
                    name = cleanName
                }
            })
            .buttonStyle(.borderedProminent)
            
            if name.isEmpty {
                Text("No item added")
            } else {
                Text("Last added: \(name)")
            }
        }
        .padding()
    }
}
```

| Action                              | Actual text field | Actual result label |
| ----------------------------------- | ----------------- | ------------------- |
| Launch the view                     | ""                | No item added       |
| Type `"  Milk  "`, then tap Add     | ""                | Last added: Milk    |
| Type `"Bread"`, without tapping Add | "Bread"           | Last added: Milk    |
| Tap Add                             | ""                | Last added: Bread   |
| Type three spaces, then tap Add     | ""                | No item added       |

If the running view still differs from what your code implies, describe the
difference here so we can diagnose it:

> `Code and observations agree`.

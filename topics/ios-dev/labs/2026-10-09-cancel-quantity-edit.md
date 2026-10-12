# Cancel a quantity edit — independent change attempt

## Feature brief

Add a `Cancel` button to each persistent shopping row.

When tapped, it must:

- discard that row's unsaved quantity text, leaving the field empty;
- reset that row's feedback to `No update attempted.`;
- leave all accepted item quantities unchanged, including previously saved edits;
- leave other rows' drafts and feedback unchanged.

Existing Save, validation, Add, and Remove behavior must continue working.

Choose the implementation yourself. You may consult your existing code. No new
storage framework is needed. This task assesses your choice of what to change
and how to verify it, rather than reproducing a supplied solution.

## Before coding

In one or two sentences, identify which state Cancel should change and whether
it needs a persistence operation. Explain why.

> Change the quantityText draft State from each row, because that is what we are trying to cancel, the draft quantity, no we dont need persistance operation because we are only using the state, state is only in memory storage during a launch, it doesnt need to survive during a relaunch

Clarification supplied in chat on 2026-10-12:

> Cancel should change only the local @State quantityDraft from each row and its status text only, because we are only manipulating the one from the row, nothing need to be persisted

## Your checks

Choose a small set of scenarios that would expose an incorrect implementation.
Include an expected result before running each check. Use multiple rows where
needed to test the requirements; record your actual starting data.

Starting data:

>Milk - quantity: 6

| Scenario and actions                                 | Expected result | Actual result |
| ---------------------------------------------------- | --------------- | ------------- |
| Edit milk quantity draft to "2" and relaunch the app | "2"             | TODO          |
| Edit milk quantity draft to "2" and press cancel     | ""              | TODO          |

Add rows as needed. Do not delete existing records just to reproduce an earlier
test setup.

## Review — 2026-10-12

- Your state choice is correct. More precisely, Cancel changes only the row whose
  button was tapped, not every row.
- The pasted Cancel action matches the feature requirements on inspection:
  it clears that row's draft and resets its feedback without changing the model.
  Runtime verification remains open; the actual-result cells are still TODO.
- The first prediction above is incorrect. A fresh app launch creates new local
  state; this view initializes `quantityDraft` to `""`, so the unsaved `"2"` does
  not survive. `@State` follows view identity during use, not necessarily the
  entire app process lifetime.
- The second prediction correctly describes the draft, but does not yet check
  feedback, accepted quantity, or other rows. Relaunch alone does not test Cancel.

Keep the original predictions above. Complete the revised checks below before
running them. Choose scenarios that cover the feature brief, including cancelling
after a previously saved edit and preserving another row's draft and feedback.
Make feedback changes observable rather than checking only its default value.

Actual starting data for all rows used (identify saved quantities):

> ShoppingItem(name: "Milk", quantity: 5), ShoppingItem(name: "Eggs", quantity: 6), ShoppingItem(name: "Bread", quantity: 1)

| Scenario and actions                                 | Expected draft, feedback, and accepted quantities for affected and other rows                          | Actual result                                                                                          |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| Edit milk quantity draft to "2" and relaunch the app | Draft: "" , feedback: "No updated attempted." , accepted quantities for affected and other rows : None | Draft: "" , feedback: "No updated attempted." , accepted quantities for affected and other rows : None |
| Edit milk quantity draft to "2" and press cancel     | Draft: "" , feedback: "No updated attempted." , accepted quantities for affected and other rows : None | Draft: "" , feedback: "No updated attempted." , accepted quantities for affected and other rows : None |

Add rows as needed. After running your checks, explicitly record whether the
Xcode build succeeded and any mismatches; distinguish observed results from
predictions.

## Follow-up review — 2026-10-12

The revised empty-draft prediction is correct, and you report observing it for
both relaunch and Cancel. The Cancel implementation still matches the brief on
inspection. Verification is incomplete:

- `None` does not identify accepted quantities. If you mean "no changes," record
  the actual displayed numbers for Milk, Eggs, and Bread instead. The starting
  values above are 5, 6, and 1; the earlier setup said Milk 6. A changed setup is
  fine, but each check needs to identify the data actually used.
- Feedback already at its default cannot demonstrate that Cancel resets feedback.
- The listed actions do not exercise Cancel after a successful saved edit or
  demonstrate preservation of another row's nonempty draft and nondefault feedback.
- The table says `No updated attempted.`; the pasted source says
  `No update attempted.`. Correct the transcription if that is what happened;
  otherwise record the source/runtime mismatch. This is not a conceptual error.
- Build status is still ambiguous: `None` may mean no unexpected behavior.

### One focused check to finish

Construct a check that combines the missing conditions: a previously saved
quantity edit, drafts in two rows, and nondefault feedback in both rows before
Cancel is tapped on Milk only. Choose the actions and values yourself. Record
predictions before tapping Cancel, then inspect both rows afterward.

Actions used to establish that setup (include the successful Save):

> TODO

| Row                    | Accepted quantity before Cancel | Draft before Cancel | Feedback before Cancel | Expected quantity / draft / feedback after Cancel | Observed quantity / draft / feedback after Cancel |
| ---------------------- | ------------------------------- | ------------------- | ---------------------- | ------------------------------------------------- | ------------------------------------------------- |
| Milk                   | 5                               | 2                   | No update attempted.   | 5 / "" / No update attempted.                     | TODO                                              |
| Other row (name: TODO) | TODO                            | TODO                | TODO                   | TODO                                              | TODO                                              |

Explicit build result:

> TODO — succeeded, or include the compiler error.

Clarification of the earlier `None` quantity entries (record observed numbers,
or say they were not inspected):

> TODO

## Implementation

Implement in Xcode, build, and run your checks. Paste the revised child view and
any other code you changed here.

```swift
struct PersistentShoppingRow: View {
    let item: ShoppingItem
    let onSaveQuantity: (String) -> PersistentUpdateResult
    let onRemoveItem: () -> Void
    
    @State private var quantityDraft: String = ""
    @State private var feedback: String = "No update attempted."

    var body: some View {
        VStack(alignment: .center) {
            HStack {
                VStack(alignment: .leading, spacing: 32) {
                    Text("\(item.name) - quantity: \(item.quantity)")
                    
                    TextField("Edit Quantity", text: $quantityDraft)
                        .frame(width: 120, height: 16)
                        .textFieldStyle(.roundedBorder)
                }
                
                Spacer()
                
                VStack() {
                    Button("Save", action: {
                        let result = onSaveQuantity(quantityDraft)
                        
                        switch result {
                        case .updated(let name, let oldQuantity, let newQuantity):
                            feedback = "Updated \(name) from \(oldQuantity) to \(newQuantity)."
                            quantityDraft = ""
                        case .invalidQuantity:
                            feedback = "Quantity must be a positive whole number."
                        case .failed(let name):
                            feedback = "Failed to update \(name)."
                        }
                    })
                    .buttonStyle(.borderedProminent)
                    
                    Button("Remove", action: {
                        onRemoveItem()
                    })
                    .buttonStyle(.borderedProminent)
                    
                    Button("Cancel", action: {
                        quantityDraft = ""
                        feedback = "No update attempted."
                    })
                }
            }
            
            Text(feedback)
        }
        .padding()
    }
}
```

Build result and any unexpected behavior:

> None

Tell the tutor when this worksheet is ready for review. If blocked, preserve
your attempt and include the exact error or surprising observation.

# PassStore `addUses` checkpoint

Complete this worksheet before changing or running the implementation.

## Starting state

- `P001` begins with `2` remaining uses.
- `P404` does not exist.
- The operations in the prediction table execute from top to bottom.

## 1. Result contract

Write the revised `AddResult` cases and their associated values. You may use a
Swift code block.

```swift
enum AddResult: Equatable {
	case added(id: String, remainingUses: Int)
	case invalidAmount
	case unknownPass(id: String)
}
```

## 2. Branch order

Describe the order of decisions inside `addUses`. Do not write the complete method
yet.

1. Checks the amount whether is valid or not first (positive number, not zero, and valid Integer)
2. Checks the id if it exists or not
3. If all checks pass, we add the amount to the chosen id pass uses

## 3. Predictions

The first row preserves the answer already supplied in chat. Edit it if needed.

| Operation                                  | Expected result                                      | `P001` uses afterward | Does `P404` exist? |
| ------------------------------------------ | ---------------------------------------------------- | --------------------: | ------------------ |
| `addUses(id: "P001", amountText: "2")`     | `AddResult.added(id: "P001", remainingUses: 4)`      |                     4 | No                 |
| `addUses(id: "P001", amountText: "hello")` | AddResult.invalidAmount                              |                     4 | No                 |
| `addUses(id: "P001", amountText: "0")`     | AddResult.invalidAmount                              |                     4 | No                 |
| `addUses(id: "P001", amountText: "-3")`    | AddResult.invalidAmount                              |                     4 | No                 |
| `addUses(id: "P404", amountText: "2")`     | AddResult.unknownPass(id: "P404")                    |                     4 | No                 |
| `addUses(id: "P404", amountText: "0")`     | AddResult.invalidAmount                              |                     4 | No                 |

The last operation combines two invalid conditions. Its expected result should
follow the branch order you wrote above.

## Ready for review

- [ ] I completed all three sections.
- [ ] I made these predictions before running the code.

## Tutor review 1

### Correct so far

- The branch order is correct: amount validation happens before ID lookup.
- Every predicted `P001` state is correct.
- Every prediction that `P404` remains absent is correct.
- The first five rows choose the correct general result category.

### Revise before implementation

1. Compare the enum with these two requirements:
   - An unknown-pass result must carry the unknown ID.
   - A successful result must carry the ID and the **updated stored total**.

   Your cases currently carry no associated values, so the caller cannot obtain
   that information from the result. Revise the enum declaration. Then make the
   table's result cells show the complete result, including associated values
   where required.

2. Reconsider only the final row. Both the amount and ID are invalid there. Your
   branch order says the amount is checked first. Which return happens before the
   method ever reaches ID lookup?

### Revision confirmation

- [ ] I revised the enum's associated values.
- [ ] I revised the table to show complete results.
- [ ] The final row now agrees with my branch order.

## Tutor review 2

The revised enum and the final-row precedence are correct.

Revise only these two result cells:

- The first row currently says only `AddResult.added`. Write the complete result,
  including the ID and updated stored total for that operation.
- The fifth row currently says only `AddResult.unknownPass`. Write the complete
  result, including the unknown ID.

The four `invalidAmount` cells need no associated values and are already complete.

- [ ] The first-row result includes both associated values.
- [ ] The fifth-row result includes its associated value.

## Tutor review 3 — planning checkpoint passed

The result contract, branch order, complete result predictions, state transitions,
and validation precedence are now correct. Continue to implementation.

## 4. Implementation

Revise `addUses` in Xcode so its returned values agree exactly with the prediction
table. Keep printing outside the model.

Paste the relevant final Swift code here after writing it yourself:

```swift
mutating func addUses(id: String, amountText: String) -> AddResult {
	guard let amount = validAmount(amountText: amountText) else {
		return AddResult.invalidAmount
	}
	
	guard let pass = passes[id] else {
		return AddResult.unknownPass(id: id)
	}
	
	let updatedTotal = pass.remainingUses + amount
	
	passes[id]?.remainingUses += amount
	
	return AddResult.added(id: id, remainingUses: updatedTotal)
}
```

## 5. Verification after every operation

Use the six operations from the prediction table, in the same order and starting
from the stated initial store.

For each operation:

1. Call `addUses` exactly once and store its result.
2. Immediately check that the complete result is correct, including associated
   values where applicable.
3. Immediately check the relevant dictionary state before making the next call.

Your checks must establish all of the following without relying only on final
state:

- Success stores and returns the updated total.
- Invalid text, zero, and a negative amount each preserve `P001`.
- A valid amount for `P404` returns the unknown ID and does not insert that key.
- An invalid amount for `P404` selects `invalidAmount`, leaves `P001` unchanged,
  and still does not insert `P404`.

After all checks, print one completion message so the console proves execution
reached the end.

Paste your independently written verification code here:

```swift
    let result1 = store.addUses(id: "P001", amountText: "2")
    assert(
        result1 == .added(id: "P001", remainingUses: 4),
        "The first result should carry the updated total of 4"
    )
    assert(
        store.passes["P001"]?.remainingUses == 4,
        "P001 should store 4 uses after the successful addition"
    )
    
    let result2 = store.addUses(id: "P001", amountText: "hello")
    assert(
        result2 == .invalidAmount,
        "The second result should be invalid amount"
    )
    assert(
        store.passes["P001"]?.remainingUses == 4,
        "P001 should still store 4"
    )
    
    let result3 = store.addUses(id: "P001", amountText: "0")
    assert(
        result3 == .invalidAmount,
        "The third result should be invalid amount"
    )
    assert(
        store.passes["P001"]?.remainingUses == 4,
        "P001 should still store 4"
    )
    
    let result4 = store.addUses(id: "P001", amountText: "-3")
    assert(
        result4 == .invalidAmount,
        "The fourth result should be invalid amount"
    )
    assert(
        store.passes["P001"]?.remainingUses == 4,
        "P001 should still store 4"
    )
    
    let result5 = store.addUses(id: "P404", amountText: "2")
    assert(
        result5 == .unknownPass(id: "P404"),
        "The fifth result should be unknown pass"
    )
    assert(
        store.passes["P001"]?.remainingUses == 4,
        "P001 should still store 4"
    )
    assert(
        store.passes["P404"] == nil,
        "P404 should be absent"
    )
    
    let result6 = store.addUses(id: "P404", amountText: "0")
    assert(
        result6 == .invalidAmount,
        "The sixth result should be invalid amount"
    )
    assert(
        store.passes["P001"]?.remainingUses == 4,
        "P001 should still store 4"
    )
    assert(
        store.passes["P404"] == nil,
        "P404 should be absent"
    )
    
    print("All checks complete.")

```

## 6. Actual Xcode output

Run the code only after finishing the checks. Paste the complete console output:

```text
All checks complete.
```

## Implementation ready for review

- [ ] The implementation returns the updated stored total, not merely the amount added.
- [ ] I check each result and state immediately after its operation.
- [ ] I ran the code and pasted the actual console output.

## Tutor review 4 — implementation revision required

### What is correct

- Amount validation occurs before dictionary lookup.
- The unknown-pass result carries the requested ID.
- The stored dictionary entry is mutated rather than only a local copy.
- You attempted to read and return the updated total.

### What must change

1. Resolved after clarification: the actual enum uses
   `added(id:remainingUses:)`, so the method's success return matches it. The
   earlier mismatch finding came from an outdated enum declaration in this
   worksheet. `remainingUses` is an acceptable label because the carried value is
   the updated stored total.

2. The first lookup binds `pass`, but the method never uses it.

3. After the amount has been validated and the pass has been found, the second
   `guard` returns `invalidAmount` if a later dictionary read fails. That result
   would falsely blame an amount that is already known to be valid. Use the pass
   obtained by the first lookup to help derive the updated total, and structure
   the success path so this second failure classification is unnecessary.

4. The pasted code contains Markdown bold markers such as `**mutating**` and
   `**guard**`. Replace the block with plain, compile-ready Swift copied from
   Xcode.

### Current verification status

Section 5 still contains only `TODO`, so no result/state checks were submitted.
The output shows fewer than the six assigned operations and uses `P999` rather
than the assigned `P404`. It therefore cannot serve as checkpoint evidence yet.
We will address verification after the method itself is correct.

### Next action — implementation only

Revise the code in section 4. Do not change sections 5 or 6 yet. Before submitting,
check that:

- [ ] The Swift block contains no Markdown formatting markers.
- [x] The success return uses the exact enum case labels.
- [ ] Every bound local value has a purpose.
- [ ] No valid amount can later produce `invalidAmount` because of dictionary state.

## Tutor review 5 — implementation passed

Section 4 is correct. Although the success path calculates the total and performs
the stored mutation as separate statements, they use the same `pass` and `amount`,
so the returned total agrees with the new stored value.

Now complete sections 5 and 6:

- Write automated result and state checks for all six table operations.
- Keep each operation's checks immediately after that operation.
- Use `P404` exactly as assigned.
- Replace the old console output completely with the new run's full output.
- Print a final completion message only after every check has passed.

Do not change the approved implementation while writing the verification unless
Xcode reveals an actual implementation problem.

## Tutor review 6 — verification revision required

### Useful choices in the attempt

- Each call stores its returned `AddResult`.
- You used automated assertions rather than relying only on printed messages.
- You included a combined invalid-amount/unknown-ID operation.
- You placed a completion marker after the assertions.

### Why the current evidence does not pass

1. The approved table contains six operations; the submitted code contains four.
   The known-pass zero and negative-amount operations are missing.
2. The brief specifies `P404`, but the code uses `P999`.
3. All four mutations happen before any assertion. A later final state cannot show
   which operation caused an incorrect transition.
4. No dictionary state is asserted after any operation.
5. The success assertion expects `remainingUses: 2`, even though the starting two
   plus the added two produces the predicted updated total of four.
6. The pasted output does not match the submitted code. The code prints four
   result messages plus `All checks complete.`, while the output shows only three
   result messages and a standalone `4`.

### Rewrite pattern

Replace section 5 using this six-block order. Do not place all assertions at the
end.

```text
call P001 with "2"
check its complete result
check dictionary state

call P001 with "hello"
check its complete result
check dictionary state

call P001 with "0"
check its complete result
check dictionary state

call P001 with "-3"
check its complete result
check dictionary state

call P404 with "2"
check its complete result
check P001 and prove P404 is absent

call P404 with "0"
check its complete result
check P001 and prove P404 is absent

print the completion marker
```

Use the approved prediction table as the source for every assertion value. Run
the revised code, then replace section 6 with the complete output from that exact
run.

- [ ] Exactly six calls appear, in the approved order.
- [ ] Result and state assertions immediately follow every call.
- [ ] Both unknown-ID blocks prove `P404` remains absent.
- [ ] The actual output ends with `All checks complete.`

## Tutor review 7 — printing is not checking

### What improved

- All six required calls now appear in the correct order.
- The assigned IDs and amount strings are exact.
- Each call is followed by an observation of the current state.

### Missing verification

`print` shows a value but accepts every possible value. It neither compares actual
behavior with the prediction nor stops execution when they differ. An automated
check needs a Boolean condition such as `assert(actual == expected)`.

To compare `AddResult` values directly, declare the enum with `Equatable`:

```swift
enum AddResult: Equatable {
    // keep the same three cases
}
```

Because all its associated values are `String` and `Int`, Swift can synthesize the
equality behavior.

Here is the complete pattern for the first operation:

```swift
let result1 = store.addUses(id: "P001", amountText: "2")
assert(
    result1 == .added(id: "P001", remainingUses: 4),
    "The first result should carry the updated total of 4"
)
assert(
    store.passes["P001"]?.remainingUses == 4,
    "P001 should store 4 uses after the successful addition"
)
```

Rewrite section 5 using this pattern. For each of the remaining five calls, place
one result assertion and the necessary state assertion(s) immediately below the
call. For both `P404` calls, explicitly assert that `store.passes["P404"] == nil`.

Remove the result/state prints so the final console evidence is unambiguous. If
all assertions pass, section 6 should contain:

```text
All checks complete.
```

- [ ] `AddResult` conforms to `Equatable`.
- [ ] Every call is immediately followed by result and state assertions.
- [ ] There are no observation-only result/state prints.
- [ ] The pasted output comes from the revised code and contains the completion marker.

## Tutor review 8 — two absent-key checks remain

The following evidence now passes:

- All six exact operations are present and ordered correctly.
- Every complete result is asserted immediately after its call.
- `P001` is asserted as four after the success and after every failure.
- The reported completion marker proves all currently submitted assertions passed.

Two required state checks are still absent. Immediately after `result5` and again
immediately after `result6`, assert:

```swift
store.passes["P404"] == nil
```

Give each assertion a useful failure message. This proves that neither the valid
amount nor the invalid amount accidentally inserts an unknown ID.

Also update the enum shown in section 1 to include the `Equatable` conformance used
by the compiling `==` checks, so the worksheet matches the code that actually ran.
Then rerun and replace section 6 with that run's output.

- [ ] Absence is asserted immediately after `result5`.
- [ ] Absence is asserted immediately after `result6`.
- [ ] Section 1 shows the actual compiling enum declaration.

## Tutor review 9 — checkpoint complete

The learner confirmed that the Xcode declaration conforms to `Equatable`; section
1 now matches the code that ran.

Final evidence:

- The result type carries the unknown ID and the success ID plus updated total.
- Amount validation precedes ID lookup, including the combined-failure case.
- Success changes `P001` from two to four and returns four.
- Invalid text, zero, and negative amounts preserve stored state.
- Both unknown-ID operations preserve `P001` and leave `P404` absent.
- Result and state assertions occur immediately after every operation.
- Xcode reached `All checks complete.`, so every submitted assertion passed.

Assessment: the feature implementation is complete. Requirement tracing and
verification are still **GUIDED**, because multiple corrections and a supplied
first assertion block were needed before the test matrix was implemented fully.

# Verify that a check detects a bug

Your three validator checks now have the correct assertion placement. This
exercise tests whether they detect a deliberately introduced mistake.

Use the same separate Playground. Keep the assertions unchanged, apart from
correcting the `"abc"` assertion message to `"Expected abc to throw!"`.

## 1. Predict before running

Temporarily change only the validator's condition:

```swift
if quantity >= 0 {
```

This replaces `if quantity > 0 {`. Leave the rest of the validator unchanged.

Before running, fill in:

- Which input will first expose the bug? 0
- Which assertion will fail, and why will execution reach it? assert(**false**, "Expected zero to throw!"), because the try for input 0 validatedQuantity becomes successful, and it will reach the assertion
- Will `All validator checks passed.` print? No, because it reached an assertion , this is a guess

## 2. Run and inspect

Run the modified version. An assertion failure is the intended evidence here.
Record what you actually observe; preserve your predictions above even if they
were different.

- Assertion failure message and stopped source line: 
	XCPreviewAgent crashed due to assert in Playground.swift at line 3.
	Expected zero to throw!: XCPreviewAgent.app may have crashed. Check ~/Library/Logs/DiagnosticReports for any crash logs from your application.
- Did the final completion message appear in this run? No

## 3. Restore and rerun

Restore `quantity > 0`, then rerun all three checks.

Actual output after restoration:

```text
Invalid quantity!
Invalid quantity!
All validator checks passed.
```

Tell the tutor when ready for review. If blocked, record the actual error.

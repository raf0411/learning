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

> TODO

## Your checks

Choose a small set of scenarios that would expose an incorrect implementation.
Include an expected result before running each check. Use multiple rows where
needed to test the requirements; record your actual starting data.

Starting data:

> TODO

| Scenario and actions | Expected result | Actual result |
| --- | --- | --- |
| TODO | TODO | TODO |

Add rows as needed. Do not delete existing records just to reproduce an earlier
test setup.

## Implementation

Implement in Xcode, build, and run your checks. Paste the revised child view and
any other code you changed here.

```swift
// TODO
```

Build result and any unexpected behavior:

> TODO

Tell the tutor when this worksheet is ready for review. If blocked, preserve
your attempt and include the exact error or surprising observation.

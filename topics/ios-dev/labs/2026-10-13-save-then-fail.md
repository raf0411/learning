# Save, then fail a later edit

Use the restored Playground from `2026-10-13-swiftdata-rollback-check.md`.
Keep the model, update function, setup, and existing failure checks unchanged.

## Feature brief

After the existing failure checks and before the final completion print:

1. Use `updateForLab` to update the same item to 15 with simulated failure off.
2. Use it again to attempt an update to 20 with simulated failure on.

Check each call's result and the model quantity immediately after that call.
Choose the expected values from the function's behavior. Use the same context
and item throughout; do not manually reset the quantity or recreate the fixture
between these calls.

## Predict before running

| Operation | Expected result | Expected quantity afterward |
| --- | --- | --- |
| Update to 15, simulated failure off | TODO | TODO |
| Attempt 20, simulated failure on | TODO | TODO |

## Your added code

Write the two calls and their checks here, then insert them at the specified
location in your Playground. No changes to `updateForLab` are needed.

```swift
// TODO
```

## Actual run

Record the output or exact diagnostic. Preserve the original predictions if
you need to revise them.

```text
TODO
```

Tell the tutor when ready for review.

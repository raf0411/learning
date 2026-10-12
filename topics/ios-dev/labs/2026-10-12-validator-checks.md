# Automated checks for the throwing validator

Your validator works for the manually checked inputs. Now use the `assert`
checks you practiced earlier to detect incorrect behavior automatically.
Work in a separate Swift Playground; do not change the shopping app.

## Requirements

Write checks for these three cases:

| Input | Required behavior | What the check must reject |
| --- | --- | --- |
| `"4"` | Returns the integer 4 | A different integer, or any thrown error |
| `"0"` | Throws an error | Any normal return |
| `"abc"` | Throws an error | Any normal return |

Use `do`/`catch` and assertions. A message saying "wrong" is not an automated
check: incorrect behavior must cause a failing assertion. Arrange the checks so
all three cases run when the validator behaves correctly.

You may consult your earlier assertion exercises. Keep the validator unchanged
for this first attempt. Choose the check structure yourself; ask for a hint if
you get stuck.

## Implementation

Your existing validator is copied here. Replace the TODO with your checks.

```swift
enum QuantityInputError: Error {
    case invalidQuantity
}

func validatedQuantity(_ text: String) throws -> Int {
    if let quantity = Int(text) {
        if quantity > 0 {
            return quantity
        }
    }

    throw QuantityInputError.invalidQuantity
}

// TODO: automated checks

print("All validator checks passed.")
```

## Run

Build and run your code. Record the actual output, or the error if blocked:

```text
TODO
```

Tell the tutor when ready for review. We will inspect whether the checks would
catch incorrect behavior, not just whether the final message appears.

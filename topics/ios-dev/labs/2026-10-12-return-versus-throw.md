# Returning a failure value versus throwing an error

## The distinction

A function can report failure in two different ways:

- `return .failed` returns an ordinary enum value. The caller continues normally
  and can inspect that value with `switch`. The case name `failed` has no special
  control-flow behavior.
- `throw` exits the function by throwing an error. At a `try` call inside
  `do`/`catch`, a thrown error skips the rest of that `do` block and enters a
  matching `catch`.

Your quantity-update method uses both: `save()` can throw, and your `catch`
handles that error before returning an ordinary `.failed` result to the row.

Syntax for this experiment:

- `: Error` makes our enum usable as an error type.
- `throws` declares that a function can throw; it does not mean every call must
  throw.
- `throw DemoError.simulated` deliberately throws that error.
- `try` marks a call that can throw. It does not itself cause a failure.

## 1. Predict before running

Read this complete program. In the space below it, write the printed lines in
the order you expect. Include only lines you think will actually execute.

```swift
enum DemoResult {
    case failed
}

enum DemoError: Error {
    case simulated
}

func returnFailure() -> DemoResult {
    return .failed
}

func throwFailure() throws {
    throw DemoError.simulated
}

print("Start")

do {
    let result = returnFailure()
    switch result {
    case .failed:
        print("Received a failure value")
    }

    print("Before throwing call")
    try throwFailure()
    print("After throwing call")
} catch {
    print("Caught an error")
}

print("Finished")
```

Predicted output:

```text
Start
Received a failure value
Before throwing call
Caught an error
Finished
```

## 2. Run and compare

Run the program in a separate Swift Playground, leaving your shopping app
unchanged. Paste its console output below. Keep your original prediction.

Actual output:

```text
Start
Received a failure value
Before throwing call
Caught an error
Finished
```

Which call caused execution to enter `catch`, and what evidence in the output
shows that the other call continued normally? One or two sentences is enough.

> the try throwFailure(), because we are returning an Error type i guess

Tell the tutor when ready for review. If it does not compile, paste the error.

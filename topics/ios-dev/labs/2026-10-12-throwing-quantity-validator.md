# Write a throwing quantity validator

Use a separate Swift Playground. This exercise does not change your shopping app.

## Task

Previously your quantity validator returned `nil` for invalid input. This version
must throw an error instead.

Implement `validatedQuantity(_:)` using the declarations below:

- If the text converts to an integer greater than zero, return that integer.
- Otherwise, throw `QuantityInputError.invalidQuantity`.
- Keep printing outside the function.
- Do not return an optional or a `.failed` result from this function.

You may consult your existing validator and the previous return-versus-throw
exercise. The new task is choosing where to return and where to throw.

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

for text in ["4", "0", "abc"] {
	do {
		let quantity = try validatedQuantity(text)
		
		print("\(text) accepted! returned integer: \(quantity)")
		
	} catch {
		print("\(text) rejected through catch")
	}
}

```

Edit the code block to contain your implementation, then run it in the Playground.
Each input must be handled separately so one failure does not prevent testing
the following input. The supplied loop already places do/catch accordingly.

## Expected behavior

- `"4"`: accepted; use the returned integer in your success output.
- `"0"`: rejected through `catch`.
- `"abc"`: rejected through `catch`.

Exact wording is your choice. Make each input and outcome visible.

Build result and actual console output:

```text
4 accepted! returned integer: 4
0 rejected through catch
abc rejected through catch
```

Based on your code and run, why can the `"4"` call use `try` without entering
`catch`? One sentence is enough.

> 	because 4 is valid and doesn't need to go to catch, it automatically returns the quantity because its a valid number, it doesn't reach the throw

Tell the tutor when ready for review. If blocked, keep your attempted code and
paste the compiler error or unexpected result.

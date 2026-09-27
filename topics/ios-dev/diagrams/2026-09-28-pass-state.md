# Local copies, stored values, and checks

## Which value changes?

`Pass` is a struct. Extracting it into a local variable gives a separate value.
This is a value-semantics diagram, not a diagram of physical memory allocation.

```text
passes["P001"]: remainingUses = 2
        |
        | guard var pass = passes[id]
        v
local pass: remainingUses = 2
        |
        | pass.remainingUses -= 1
        v
local pass: remainingUses = 1

Dictionary entry still has remainingUses = 2.
```

Writing through the dictionary subscript updates the stored value:

```swift
passes[id]?.remainingUses -= 1
```

In the completed method, guards first establish that the pass exists and has a
positive number of uses. The local `pass` can be `let` because it only validates
the request. The mutation targets the dictionary entry.

## Observe each transition

```text
Initial stored uses: 2
        |
        | use P001 -> true  -> check result and stored uses
        v
Stored uses: 1
        |
        | use P001 -> true  -> check result and stored uses
        v
Stored uses: 0
        |
        | use P001 -> false -> check result and stored uses
        v
Stored uses: 0
        |
        | use P999 -> false -> check result, stored uses, and P999 absence
        v
Stored uses: 0; P999 still absent
```

A final-state check alone does not verify every intermediate transition. Make
each call, inspect its result and state, then make the next call. Keep operations
that change state outside assertions.

The session evidence is recorded in [the session record](../sessions/2026-09-28.md).

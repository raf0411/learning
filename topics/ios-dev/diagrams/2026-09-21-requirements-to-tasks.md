# From a requirement to a small coding task

Learning aid for the first requirements-decomposition lesson.

A broad request such as "build a shopping-list app" contains several behaviors.
Choose one small behavior, then describe what must happen before choosing syntax.

```text
One user action
      |
      v
Information available before the action
      |
      v
Rule or change the program should apply
      |
      v
Result the user should see
      |
      v
Concrete example to check the behavior
```

For now, keep the description in plain language. A task is small enough to begin
when its intended result can be checked with a concrete example. Implementation
and architecture choices come after clarifying the behavior.

## First exercise

Problem: someone wants to add an item to a shopping list.

Initial list: Milk, Eggs.
Entered name: Bread.
Action: press Add.

Expected behavior: existing items remain, and the new name appears once at the end.
Constraint: think only about this one action and an in-memory list. Blank names,
duplicates, purchased status, storage, and multiple screens are later requirements.
Optional stretch goal: none yet; first complete the basic reasoning.
Skill being practiced: connect a requirement to data, a change, and an observable
result before writing Swift.

Learner task: describe the information the program needs, what changes when Add
is pressed, and the exact resulting list. Then we will turn that description into
one small implementation and inspect its actual output.

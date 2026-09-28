# Lab: Remembering Pair Indices with a Dictionary

Date: 2026-09-28

## Goal

Build a function that returns the indices of two different elements whose values
add to a target.

```text
find_pair_indices([2, 7, 11], 9) -> [0, 1]
```

If no such pair exists, return an empty list: `[]`.

## Evidence already established today

You reconstructed the set-based duplicate pattern:

```python
seen = set()

if current in seen:
    return True

seen.add(current)
```

You explained why checking must happen before adding: adding first would make a
value appear to match itself.

For `[2, 7, 11]` with target `9`, you first considered `index -> value`. You then
identified the mapping needed for the reverse question, “At which earlier index
did this value appear?”

```text
observed value -> earlier index
2              -> 0
```

So after processing index `0`, the dictionary is `{2: 0}`. At index `1`, the
needed partner is `2`, and its stored index is `0`, giving the result `[0, 1]`.

## Dictionary mini-reference

This example shows only the Python dictionary operations you need:

```python
locations = {}
locations["apple"] = 3

"apple" in locations   # True: membership checks keys
locations["apple"]      # 3: retrieve the value stored for that key
```

## Part 1: Fresh trace

Trace `numbers = [3, 2, 4]` and `target = 6`.

Important: `earlier_indices` must contain only entries from positions processed
before the current position.

| current index | current value | needed partner | dictionary before check | partner found? | action/result                | dictionary after action |
| ------------: | ------------: | -------------: | ----------------------- | -------------- | ---------------------------- | ----------------------- |
|             0 |             3 |              3 | `{}`                    | no             | add {3:0} to dictionary      | {3:0}                   |
|             1 |             2 |              4 | {3:0}                   | no             | add {2:1} to dictionary      | {3:0, 2:1}              |
|             2 |             4 |              2 | {3:0, 2:1}              | yes            | return paired indicies [1,2] | {3:0, 2:1}              |

In your own words, state the dictionary invariant:

> Before processing the current index, every dictionary key is a value observed
> at an earlier index, and the associated dictionary value is that earlier
> index. The current index has not been stored yet, so it cannot match itself.

## Part 2: Construct the function

### Initial attempt

```python
def find_pair_indices(numbers, target):	
	dict = {}
	
	for idx, current in enumerate(numbers):		
		needed_partner = target - current
		
		if needed_partner in dict:
			return [dict[needed_partner], idx]
		
		dict.update({idx: current})
	
	return []

print(find_pair_indices([4,2,1], 6))
print(find_pair_indices([2,2,1], 5))
print(find_pair_indices([1,2,3], 3))
print(find_pair_indices([3,3,1], 6))
```

### Debugging record

1. The trace required `observed value -> earlier index`, but the initial update
   used `index -> current value`. Changing the update to
   `dict.update({current: idx})` made the code match the trace.
2. In the executed Python file, `return []` was indented inside the loop. This
   ended the function after its first iteration. Moving the fallback return
   outside the loop allowed all positions to be examined.

Final observed outputs:

```text
[0, 1]
[]
[0, 1]
[0, 1]
```

## Part 3: Tests and predictions

Choose at least four tests covering these risks:

- a valid pair
- no valid pair
- one element must not be reused as both members of the pair
- two equal values at different indices are allowed when they reach the target

| call | predicted result | why this case matters | actual result |
|---|---|---|---|
| `[4,2,1], 6` | `[0, 1]` | ordinary valid pair | `[0, 1]` |
| `[2,2,1], 5` | `[]` | no valid pair; fallback after full scan | `[]` |
| `[1,2,3], 3` | `[0, 1]` | valid pair found near the start | `[0, 1]` |
| `[3,3,1], 6` | `[0, 1]` | equal values at different indices are valid | `[0, 1]` |
| `[3], 6` | `[]` | one index must not be reused as both pair members | `[]` |

Paste your completed function and test calls into a Python file under `practice/`,
run it, and record the actual results above.

## Part 4: Cost reasoning

1. What is the expected worst-case time complexity? Why?

   O(n) because as the input grows, the loop will be as long as the amount of n of elements in the array

2. What is the worst-case extra-space complexity? Explain what can grow rather
   than counting only the number of variable names.

   O(n), because as the input grows, the can grow the stored dictionary as well, worst case is until no pair indices is found, which can make the dictionary bigger

3. Compared with the nested-loop solution, what resource are we spending to
   reduce repeated comparisons?

   we reduce the time complexity in exchange of having inefficient extra espace, because the nested loop solution is O(n^2)

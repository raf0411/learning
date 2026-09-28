# Fresh Problem: Count Nearby Pairs

Date: 2026-09-28

This is an unlabeled retrieval problem. Choose the iteration structure yourself;
the prompt will not name a technique.

## Problem

Implement:

```python
def count_nearby_pairs(numbers, max_gap):
	count = 0
	
    for current_index, current_value in enumerate(numbers):
	    for other_index, other_value in enumerate(numbers):
		    if current_index == other_index:
			    continue
			
			if abs(current_value - other_value) >= max_gap:
				count += 1
				
	return count
```

Count how many pairs of **different indices** have values whose absolute
difference is at most `max_gap`.

Count each pair once. Assume `max_gap >= 0`.

Python can calculate absolute difference with:

```python
abs(first_value - second_value)
```

Example:

```text
numbers = [1, 3, 4, 6]
max_gap = 2
result = 3
```

The qualifying index pairs are `(0, 1)`, `(1, 2)`, and `(2, 3)`.

## Part 1: Reason before coding

1. List every distinct index pair that must be considered for four elements.
   Use `(i, j)` notation.

   i dont understand this question tbh...

2. What rule will ensure that a pair such as `(0, 1)` is counted, but its
   reverse `(1, 0)` is not counted again?

   we check if the current_index == other_index, if it is we continue to skip it

3. Describe your intended procedure in plain language.

   - I will store a starting variable count = 0, to store the amount of pair indices differences that is above the max_gap
   - Then i will use nested loops to get the index so i can skip indexes that we have done before
   - Then i will check if the difference between two indices value is >= than max_gap, if it is i will increment the count variable
   - if the loop done we return the count

## Part 2: Implement

Create `practice/count_nearby_pairs.py`. Write the function without copying a
previous pair function. Paste the completed function here:

```python
def count_nearby_pairs(numbers, max_gap):
	count = 0
	
    for current_index, current_value in enumerate(numbers):
	    for other_index, other_value in enumerate(numbers):
		    if current_index == other_index:
			    continue
			
			if abs(current_value - other_value) >= max_gap:
				count += 1
				
	return count
```

## Part 3: Design, predict, and run tests

Include at least these behavioral risks:

- several qualifying pairs
- no qualifying pair
- equal values at different indices when `max_gap == 0`
- a singleton or empty list
- a value difference exactly equal to the boundary

| call            | predicted result | reason for this test | actual result |
| --------------- | ---------------: | -------------------- | ------------: |
| [1, 3, 4, 6], 2 |                3 | TODO                 |          TODO |
| [1, 3, 4, 6], 5 |             TODO | TODO                 |          TODO |
| [2, 2], 0       |             TODO | TODO                 |          TODO |
| [], 2           |             TODO | TODO                 |          TODO |
| [4, 2], 2       |             TODO | TODO                 |          TODO |

## Part 4: Explain the result

1. Why does your traversal cover every required pair?

   TODO

2. Why does it avoid counting a pair twice?

   TODO

3. What is its worst-case time complexity, and why?

   TODO

4. What is its extra-space complexity, and why?

   TODO

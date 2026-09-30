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

## Resume checkpoint — 2026-09-29

Work only through this checkpoint first. Do not repair the code yet.

A pair names two selected positions. Reversing their order does not create a
new selection: `(0, 1)` and `(1, 0)` refer to the same two positions. A pair
such as `(0, 0)` is invalid here because the problem requires different
indices.

### A. Trace the current rule on the smallest useful input

Suppose the only indices are `0` and `1`. The current nested loops visit these
ordered combinations:

| combination | skipped by `current_index == other_index`? |
| ----------- | ------------------------------------------ |
| `(0, 0)`    | Yes                                        |
| `(0, 1)`    | No                                         |
| `(1, 0)`    | No                                         |
| `(1, 1)`    | Yes                                        |

After the self-pairs are skipped:

- Which combinations remain? TODO
- Do the remaining combinations represent one distinct pair or two distinct
  pairs? Explain briefly: TODO

### B. Construct the distinct pairs for four indices

The available indices are `0, 1, 2, 3`. For each first index, list only partner
indices that come **later** in the list. Write complete pairs such as `(0, 1)`.

| first index | pairs with later indices |
| ----------: | ------------------------ |
| `0`         | (0,1), (0,2), (0,3)      |
| `1`         | (1,2), (1,3)             |
| `2`         | (2,3)                    |
| `3`         | none                     |

- Total number of distinct pairs: 3
- Complete the traversal relationship:
  `other_index` == `current_index`
- Why would that relationship exclude both self-pairs and reversed duplicates?
  because we are comparing if the other index is the same as the current index during our nested loop, if it is we will skip it, meaning we are skipping self-pairs or duplicates

Stop here and tell the tutor when this checkpoint is ready for review.

### Review 1 and second attempt

What was correct:

- All four yes/no decisions in section A are correct.
- You correctly recognized that equality identifies the two self-pairs.

What needs correction:

- Section A's two follow-up questions are still unanswered. Copy the two
  combinations marked `No`, then decide whether reversing their order gives us
  a genuinely new selection of indices.
- “Later” means **any** index to the right, not only the immediately adjacent
  index. For first index `0`, the later indices are `1`, `2`, and `3`.
- `other_index == current_index` selects a self-pair—the opposite of the
  relationship needed for a valid unique pair.

Finish this second attempt:

| first index | every later index | complete pairs      |
| ----------: | ----------------- | ------------------- |
|         `0` | `1, 2, 3`         | (0,1), (0,2), (0,3) |
|         `1` | 2, 3              | (1,2), (1,3)        |
|         `2` | 3                 | (2,3)               |
|         `3` | none              | none                |

- The two combinations left after section A's equality check are: TODO
- They represent TODO distinct pair(s), because: TODO
- Total number of distinct pairs across the completed table: TODO
- Look at every pair in the table. Complete the relationship with `<`, `>`, or
  `==`: `other_index` TODO `current_index`
- Test your relationship against `(0, 1)`: `1` TODO `0`, so this pair is
  included.
- Explain why the relationship rejects both `(0, 0)` and `(1, 0)`: TODO

Stop again after completing this second attempt.

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

   idk

2. Why does it avoid counting a pair twice?

   idk

3. What is its worst-case time complexity, and why?

   idk

4. What is its extra-space complexity, and why?

   idk

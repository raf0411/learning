# REVIEW

## Input-derived running best

- Stage: RETAINED.
- Demonstrate next: choose a valid starting candidate in a less-direct running-best problem and justify it without being told which scan pattern applies.
- Reason: zero initialization previously excluded valid answers; later retrieval succeeded for the reversed `find_smallest` task.
- Last meaningful evidence: 2026-09-23, independently initialized from `numbers[0]`, handled positive/negative/singleton cases, and execution-validated the implementation.
- Next review: after several sessions, through an unfamiliar selection problem rather than another immediate min/max repetition.

## Count accumulator reasoning

- Stage: RETAINED.
- Demonstrate next: identify and implement counting as part of an unfamiliar problem, including an empty input and a meaningful boundary.
- Reason: confirm transfer rather than repeat the same threshold-counting prompt.
- Last meaningful evidence: 2026-09-23, independently reconstructed and tested `count_above`, including strict equality and empty input.
- Next review: after several sessions or when a new problem naturally requires counting.

## Nested-loop execution and candidate coverage

- Stage: INDEPENDENT.
- Demonstrate: select nested iteration on an unlabeled fresh problem, trace inner-loop resets, cover all required distinct-index pairs, and place the fallback return correctly.
- Reason: current-session construction succeeded, but earlier reset confusion and same-session scaffolding mean retention is not established.
- Last meaningful evidence: 2026-09-23, reconstructed exhaustive duplicate detection and independently recognized/implemented exhaustive pair-sum; execution-validated edge cases.
- Next review: next session or the following session, without showing the previous grid or loop scaffold first.

## Linear versus quadratic growth

- Stage: INDEPENDENT for direct current-session examples.
- Demonstrate: classify unfamiliar code containing separate and nested loops, distinguish exact operation counts from growth class, and predict scaling when input changes.
- Reason: initial answers confused absolute work with multiplication factors and counted two separate loops as quadratic; the corrected model was later applied successfully.
- Last meaningful evidence: 2026-09-23, correctly explained `n * n`, classified fresh functions, and explained why division by two does not change `O(n^2)`.
- Next review: after spacing, using code whose technique is not labeled.

## Extra space and growing collections

- Stage: GUIDED.
- Demonstrate: distinguish a fixed number of variables from one collection containing up to `n` elements and classify auxiliary space on a fresh function.
- Reason: initially classified a growing set as `O(1)` because it had one variable name.
- Last meaningful evidence: 2026-09-23, corrected the set-based duplicate and pair-sum analyses to `O(n)` extra space and described the time-space trade-off.
- Next review: next session during dictionary construction and again later on unfamiliar code.

## Set seen-state invariant

- Stage: GUIDED.
- Demonstrate: reconstruct `set()` syntax, check-before-add ordering, and the invariant that stored values came from earlier indices; implement a membership solution without procedural hints.
- Reason: `{}` was used for an empty set, and the first optimized pair-sum attempt stored the desired partner rather than the current observed value.
- Last meaningful evidence: 2026-09-23, corrected both issues and execution-validated duplicate and pair-sum set solutions.
- Next review: at the start of the next session before extending the state from a set to a dictionary.

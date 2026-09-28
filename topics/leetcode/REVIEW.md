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

- Stage: GUIDED for complete unique-pair coverage; nested-loop selection itself was independently retrieved after spacing.
- Demonstrate: enumerate all unique pairs, implement each exactly once, explain why skipping self-pairs alone does not remove reverse duplicates, and execute boundary cases.
- Reason: on the fresh nearby-pair task, independently chose nested loops but used a full grid with only self-index skipping, which would count both `(i, j)` and `(j, i)`.
- Last meaningful evidence: 2026-09-29, began the unlabeled nearby-pair problem; correct iteration-family selection but incomplete and incorrect candidate coverage.
- Next review: resume the unfinished nearby-pair lab at the start of the next session.

## Linear versus quadratic growth

- Stage: INDEPENDENT for direct current-session examples.
- Demonstrate: classify unfamiliar code containing separate and nested loops, distinguish exact operation counts from growth class, and predict scaling when input changes.
- Reason: initial answers confused absolute work with multiplication factors and counted two separate loops as quadratic; the corrected model was later applied successfully.
- Last meaningful evidence: 2026-09-23, correctly explained `n * n`, classified fresh functions, and explained why division by two does not change `O(n^2)`.
- Next review: after spacing, using code whose technique is not labeled.

## Extra space and growing collections

- Stage: INDEPENDENT in the current session; retention untested.
- Demonstrate: distinguish a fixed number of variables from one collection containing up to `n` elements and classify auxiliary space on a fresh function.
- Reason: the original set analysis counted variable names, but the dictionary analysis correctly counted stored entries.
- Last meaningful evidence: 2026-09-29, independently classified the pair-index dictionary as `O(n)` extra space and explained its possible growth.
- Next review: after spacing on unfamiliar code containing a growing collection.

## Set seen-state invariant

- Stage: GUIDED.
- Demonstrate: reconstruct `set()` syntax, check-before-add ordering, and the invariant that stored values came from earlier indices; implement a membership solution without procedural hints.
- Reason: the spaced retrieval began with `Set()` rather than `set()`, though membership, mutation, and check-before-add reasoning were then correct.
- Last meaningful evidence: 2026-09-29, reconstructed the set pattern one line at a time and correctly explained why adding first creates self-matches.
- Next review: after several sessions through a fresh membership problem without line-by-line scaffolding.

## Dictionary earlier-index invariant

- Stage: GUIDED.
- Demonstrate: independently choose `observed value -> earlier index`, check before storing the current entry, place the fallback after the loop, and test self-reuse.
- Reason: the learner's trace was correct, but the first implementation reversed the mapping and returned failure from inside the loop.
- Last meaningful evidence: 2026-09-29, debugged both issues and execution-validated ordinary, absent-pair, equal-value, and singleton cases.
- Next review: after spacing on a different index-retrieval problem without a supplied mapping direction.

## Inequality wording and boundary direction

- Stage: GUIDED.
- Demonstrate: translate “at most,” “at least,” “less than,” and “greater than” into comparisons and validate equality-at-the-boundary cases.
- Reason: the worksheet translated “difference is at most `max_gap`” in the wrong direction, while the separate practice file used the correct equivalent comparison; the mental model is inconsistent.
- Last meaningful evidence: 2026-09-29, runnable code used the correct boundary direction but returned `6` instead of `3` because of reverse-pair duplication.
- Next review: immediately when resuming the nearby-pair lab.

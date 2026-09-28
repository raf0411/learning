# STATE

Last consolidated: 2026-09-29. Preferred language: Python. Prior coursework is self-reported; current ability is assessed from performance below.

## Demonstrated capabilities

- Basic Python functions, loops, conditionals, accumulators, and return placement — INDEPENDENT in simple scans.
- Count accumulator reasoning — RETAINED. After spacing, independently rebuilt `count_above`, justified zero as “no matches observed yet,” and execution-validated mixed, empty, and strict-boundary cases.
- Input-derived running-best initialization — RETAINED. After spacing, independently selected `numbers[0]` for `find_smallest`, explained why it handles positive, negative, and singleton inputs, and execution-validated all three cases.
- Basic index/value mapping — INDEPENDENT. Uses `enumerate` correctly and distinguishes indices from their stored values in implemented solutions.
- Empty-loop and singleton-loop control flow — INDEPENDENT. Correctly explained zero iterations for empty input and one self-comparison for singleton input, including how execution reaches the fallback return.
- Exhaustive comparison coverage — INDEPENDENT on previously completed duplicate and pair-sum tasks, including correct fallback return placement after all candidates are exhausted.
- Nested-loop selection — INDEPENDENT after spacing. On an unlabeled nearby-pair counting problem, independently selected a counter and nested iteration. Correct execution and complete candidate coverage were not demonstrated because the draft remained unfinished.
- Unique-pair traversal — GUIDED. Previously implemented `range(current_idx + 1, len(numbers))` after instruction, but later confused skipping self-pairs with preventing reverse-pair duplication on a fresh task.
- Basic time-complexity classification — INDEPENDENT in the current session for direct single and nested scans. Correctly distinguished separate loops (`n + n`) from nested loops (`n * n`) and classified fresh scan/pair functions as `O(n)` and `O(n^2)`.
- Exact-count versus growth reasoning — GUIDED to INDEPENDENT within the session. Correctly challenged incomplete doubling substitution, then explained why both `n^2 - n` and `n(n - 1)/2` retain quadratic growth.
- Fixed auxiliary-space reasoning — INDEPENDENT for scalar loop state: correctly classified scan and exhaustive-pair functions as `O(1)` extra space.
- Set membership and mutation — GUIDED. Retrieved membership and `.add(current)` after spacing and explained check-before-add, but initially wrote `Set()` and needed the lowercase `set()` correction.
- Set-based pair-sum complement reasoning — GUIDED. Derived `partner = target - current`, corrected an initial error that added the desired partner rather than the observed current value, and execution-validated the corrected function.
- Dictionary `value -> earlier index` lookup — GUIDED. Correctly traced dictionary state and built an execution-validated index-returning pair-sum function, but initially reversed the mapping in code and placed the fallback return inside the loop.
- Earlier-state invariant — GUIDED. After explanation, correctly showed that checking before storing prevents `[3]`, target `6`, from reusing index `0`.
- Growing-collection space and time-space trade-off — INDEPENDENT in the current session. Correctly classified the dictionary solution as expected `O(n)` time and `O(n)` extra space because up to `n` entries can be stored.
- Behavioral test design — GUIDED. Predicted selected outputs correctly but needed prompting to state test purposes and add an explicit singleton self-reuse case.
- Basic string/list indexing — INDEPENDENT for retrieving values. List element reassignment is known; string element reassignment remains UNKNOWN.
- Binary-search intuition — GUIDED. Can discard the smaller left half for a larger target after concrete inspection; boundary implementation remains unassessed.

## Current gaps and uncertainties

- Complete nested-loop candidate coverage remains insecure: on a fresh task, skipping `(i, i)` was incorrectly treated as sufficient to avoid also counting both `(i, j)` and `(j, i)`.
- Growing-collection space reasoning succeeded for the dictionary task but still needs later retrieval on unfamiliar code before a retention claim.
- Set construction and invariants need another spaced retrieval: capitalization and construction still required correction, though check-before-add reasoning was correctly explained.
- Python set lookup/add is known as expected `O(1)` by instruction, but the learner mixed this operation cost with the set's `O(n)` storage growth when explaining the optimized function.
- Dictionary construction is GUIDED; no unfamiliar dictionary problem has yet been completed independently.
- Verbal inequality translation needs attention. The worksheet used the reversed comparison for “at most,” while the separate runnable file used the correct equivalent `max_gap >= difference`; the reasoning is inconsistent.
- Test selection and explaining what bug each case could expose remain weak without prompts.
- List versus string mutability remains partial.
- Sorting, stacks/queues, linked lists, recursion, trees, and graphs remain unassessed. No TRANSFERABLE claims have been established.

## Current learning edge

- Resume `labs/2026-09-28-fresh-pair-problem.md` before introducing new material.
- Distinguish self-pair exclusion from reverse-pair duplication by enumerating the six unique pairs for four indices.
- Translate “at most” into the correct boundary comparison, then correct and execute the nearby-pair counter.
- Finish with independent `O(n^2)` time and `O(1)` extra-space reasoning; retrieve dictionary construction later on a different problem.

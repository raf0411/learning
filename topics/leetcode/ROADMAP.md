# ROADMAP

Status: active. Finalized from the 2026-09-21 to 2026-09-22 baseline probe. Target window: roughly 1–2 months at up to 25 study hours per week. The week ranges are pacing guides, not deadlines; advancement depends on independent performance.

Python; mostly Easy problems, adding selected Medium problems only after their prerequisites are demonstrated. Each milestone uses explanation, tracing, implementation, learner-chosen tests, and later spaced retrieval.

## Dependency path

1. **Python problem-solving foundation (current; approximately week 1).** Translate a verbal procedure into code; distinguish values from indices; use single and nested loops; place returns correctly; work with list and string behavior; trace state; and choose ordinary and edge-case tests.
2. **Correctness and cost (approximately weeks 1–2).** Explain why a scan covers the required candidates, recognize missed or repeated work, connect concrete operation counts to Big O time and space, and compare straightforward approaches.
3. **Sets and dictionaries (approximately weeks 2–3).** Derive these structures from the need to remember prior values efficiently; solve membership, duplicate, frequency-counting, and lookup problems. Revisit duplicate detection by comparing the exhaustive and set-based approaches.
4. **Order-based techniques (approximately weeks 3–4).** Use sorting deliberately, then learn two pointers and reconstruct binary search with correct boundaries. Begin selected Easy and carefully scaffolded Medium problems.
5. **Contiguous ranges and linear state (approximately weeks 4–5).** Learn simple fixed and variable sliding windows, prefix-style running state where useful, and stacks/queues through concrete problems.
6. **Core structural problems (approximately weeks 5–6).** Introduce references, linked lists, recursion, and basic tree traversal only after loop/state reasoning is secure. Scope this milestone to common junior-assessment tasks.
7. **Mixed assessment practice (approximately weeks 6–8).** Solve unfamiliar Easy and selected Medium problems without technique labels: clarify, propose, justify, implement, test, analyze, and debug. Gradually add realistic time limits and revisit weak skills after spacing.

## Milestone gates

- Leave milestone 1 after independently implementing and testing several scan/nested-scan problems, including correct edge-case and return behavior.
- Leave milestone 2 after independently explaining the cost of single and nested scans and choosing between them on a fresh problem.
- Leave milestone 3 after independently using sets/dictionaries for membership and counting on unfamiliar Easy problems.
- Later milestones require both implementation and reasoning evidence; guided repetition alone does not satisfy a gate.

## Current position

- Milestone 1: Python problem-solving foundation.
- Immediate lesson: finish tracing the comparison grid in `diagrams/2026-09-22.md`, then turn the learner's verbal exhaustive duplicate procedure into two-loop structure with a fixed current position and a moving comparison position.
- Immediate follow-up: connect the already-derived `n * (n - 1)` comparisons to Big O, then compare against a memory-based approach after sets are introduced.
- Deferred practical task: learner-selected tests for `count_above`.
- Spaced review continues from REVIEW.md; no milestone is complete yet.

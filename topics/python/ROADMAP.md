# ROADMAP

Destination: independently build reliable Python automation for DevOps (see GOAL.md).

## Path and milestones

1. **Program basics — initial milestone completed:** run a script; values, types, variables, expressions, strings, comparisons, conditions, and loops. Milestone: count and summarize sample log messages. Completed with syntax references on 2026-10-30; independent retrieval and broader fundamentals remain subject to review.
2. **Useful local scripts — current:** lists and dictionaries, functions, imports, paths, file reading, and exceptions. Milestone: read a log file and produce a report, including handling a missing file.
3. **Reusable command-line tools:** arguments, JSON, configuration, exit codes, logging, and tests. Introduce virtual environments and dependencies when needed. Milestone: a tested log-reporting CLI.
4. **System and API automation:** subprocesses, environment variables, HTTP requests, timeouts, and failure handling. Learn the necessary shell, process, and HTTP concepts alongside these. Milestone: a read-only service-checking tool.
5. **Portfolio capstone:** scope, build, test, debug, and document a useful DevOps automation tool. Deliver a reproducible local demo, sample data, README, meaningful tests, and a CI check. Add dry-run behavior and repeat-run safety if it changes resources. Finish with an independent demonstration, failure diagnosis, and small feature addition.

Each stage builds on the preceding stage. Progress depends on demonstrated performance; skip redundant practice when evidence supports it.

## Building toward the portfolio

Working project candidate: an operations-reporting CLI that summarizes logs and checks configured HTTP services, producing readable and JSON reports with useful exit codes. Confirm or adjust this scope after the learner has built the first file-processing script.

- Stages 1–2 develop the counting and file-processing skills; small exercises may be reused or rewritten for the project.
- Introduce basic Git after the first working file-processing script to record subsequent development.
- Stages 3–4 develop the command-line interface, tests, reporting, and service checks.
- Stage 5 integrates and refines the chosen scope into a project someone else can run and evaluate.

Portfolio quality is judged by usefulness, correctness, reproducibility, and the learner's ability to explain and extend the code. Detailed acceptance criteria live in GOAL.md.

## Current position

Completed the first sample-log summary on 2026-10-30: correctly combined a loop, prefix condition, unconditional total counter, conditional error counter, and final report; handled empty input. Construction used syntax references, so this is an implementation milestone rather than a claim of independent mastery of every basic topic.

Now adapt that script to read a text file. File-reading mechanics and missing-file handling remain unassessed.

# Session recap: counting log messages

Date: 2026-10-30

Your program keeps two running counts. Every message contributes to the total; only a message beginning with `"ERROR "` contributes to errors.

```text
Set total = 0 and errors = 0     <- once, before the loop
              |
              v
     Is there another line? <------------------+
         |             |                       |
        yes            no                      |
         |             |                       |
         v             v                       |
  Increase total   Print Total and Errors      |
         |         once, after the loop        |
         v                                     |
  Starts with "ERROR "?                         |
      |          |                             |
     yes         no                            |
      |          |                             |
      v          |                             |
 Increase errors |                             |
      |          |                             |
      +----------+-----------------------------+
```

Initialization happens once so the counts accumulate instead of resetting for each line. Reporting happens after the loop so it shows final counts.

With an empty list, there is no first line. The loop body never runs, both counts remain zero, and both final print statements still execute:

```text
Total: 0
Errors: 0
```

For the integer counters used here, `count += 1` has the same effect as `count = count + 1`.

Next: get each line from a text file instead of a list inside the Python program. The file-reading exercise is prepared but has not been completed.

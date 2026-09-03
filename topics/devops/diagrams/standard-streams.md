# Standard output and standard error

A command has two separate output channels. Both normally lead to the terminal:

```mermaid
flowchart LR
    C[Command] -->|normal result: stdout, channel 1| T[Terminal]
    C -->|error message: stderr, channel 2| T
```

Redirection changes the destination of only the named channel:

```mermaid
flowchart LR
    subgraph A[Using >]
        C1[ls missing-path] -->|stdout 1: no data| F1[stdout.txt stays empty]
        C1 -->|stderr 2: error text| T1[Terminal]
    end

    subgraph B[Using 2>]
        C2[ls missing-path] -->|stdout 1: no data| T2[Terminal]
        C2 -->|stderr 2: error text| F2[errors.txt]
    end
```

- `>` means redirect channel 1, standard output.
- `2>` means redirect channel 2, standard error.
- A failed `ls` has no successful listing to send on channel 1; it sends an
  error message on channel 2.

## Pipeline with separate error routing

In this pipeline, `grep` can produce both successful matches and diagnostics.
The normal pipe carries only `grep`'s standard output:

```mermaid
flowchart LR
    G[grep]
    H[head -n 2]
    M[matches.txt]
    D[diagnostics.txt]

    G -->|stdout: matching lines| P[pipe]
    P -->|stdin| H
    H -->|stdout via greater-than: overwrite| M
    G -->|stderr via 2 greater-than greater-than: append| D
```

- A matching line travels as `grep` stdout, crosses the pipe as `head` stdin,
  and leaves `head` as stdout. `>` writes that final stdout to `matches.txt`.
- A missing-file diagnostic travels as `grep` stderr. `2>>` sends it directly
  to `diagnostics.txt`, so it never enters the pipe or reaches `head`.

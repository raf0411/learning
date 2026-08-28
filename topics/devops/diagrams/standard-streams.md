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

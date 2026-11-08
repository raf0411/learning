# Why the retrieval command worked in zsh

Learner command:

```bash
tail -n 2 events.txt > recent.txt | wc -l
```

Observed and independently reproduced in default zsh:

```text
                         +--> recent.txt (two selected lines)
tail stdout --> zsh copy -+
                         +--> pipe --> wc stdin --> terminal: 2
```

zsh's default MULTIOS option provides this copying behavior when stdout has
both a file destination and a pipe destination.

The same command in Bash:

```text
tail stdout ----------------> recent.txt (two selected lines)
empty pipe -----------------> wc stdin --> terminal: 0
```

In Bash, the explicit stdout redirection overrides the pipe connection for
`tail`. The file is not automatically read back into the pipe.

This is a shell difference, not a macOS-versus-Linux rule. Either system can
run different shells. An explicit copying command can express the intended
route in both shells.

Reference: [zsh documentation: Multios](https://zsh.sourceforge.io/Doc/Release/Redirection.html#Multios).

# Transfer check — Recover and apply an unfamiliar `head` option

Date: 2026-11-02

## Goal and boundary

Use installed local documentation to discover how `head` can print a requested
number of **bytes** instead of lines. Then print exactly the first 11 bytes of:

```text
labs/documentation-transfer/bytes.txt
```

Do not use the internet and do not modify the fixture. The exact option is not
supplied in this worksheet.

## 1 — Recover the option

Open an appropriate installed documentation source for `head`. Search or
navigate for the byte-count behavior.

| Evidence                                   | Actual result                                    |
| ------------------------------------------ | ----------------------------------------------- |
| Documentation command opened               | man he                                           |
| Search term or navigation used             | /by                                              |
| Exact option syntax from the documentation | head -c                                          |
| Meaning in your own words               it prints the size bytes of the specified files of a  |

## 2 — Construct before executing

Write the exact proposed command for the goal:

```text
head -c labs/documentation-transfer/bytes.txt
```

Decompose your command:

| Component                    | Token from your command               |
| ---------------------------- | ------------------------------------- |
| Program                      | head                                  |
| Option                       | -c                                    |
| Count supplied to the option | 1                                     |
| Pathname operand             | labs/documentation-transfer/bytes.txt |

## 3 — Execute and record evidence

Run the proposed command. Record the exact command, complete output, and
returned prompt:

```text
raffi@Raffis-Mac linux % head -c labs/documentation-transfer/bytes.txt
head: illegal byte count -- labs/documentation-transfer/bytes.txt
```

The fixture begins with ten visible letters followed by a newline. Explain why
requesting 11 bytes can print those ten letters and then place the prompt on the
next terminal line.

> idk what u meant

## 4 — Self-audit

Confirm each item with `yes` or repair it before finishing:

| Check                                                | Result |
| ---------------------------------------------------- | ------ |
| I recorded the option name, not only its description | yes    |
| My executed command actually contains that option    | yes    |
| I recorded actual command output                     | yes    |
| I did not modify the fixture                         | yes    |

Stop and tell the tutor when the transfer check is ready.

## 5 — Direct debugging correction

Keep the failed command and error above unchanged. They reveal how the program
parsed the missing argument.

The documented shape is:

```text
head -c bytes FILE
```

For this task, the complete command is:

```bash
head -c 11 labs/documentation-transfer/bytes.txt
```

```text
head    -c       11                labs/documentation-transfer/bytes.txt
program option   option argument   pathname operand
```

Run the corrected command and record the command, complete output, and returned
prompt:

```text
raffi@Raffis-Mac linux % head -c 11 labs/documentation-transfer/bytes.txt
ABCDEFGHIJ
raffi@Raffis-Mac linux %
```

Then explain both points:

1. Why did the failed command treat the pathname as an illegal byte count?
2. Why do ten ASCII letters plus one newline occupy 11 bytes in this fixture?

> 1. because its missing the argument 11 (byte)
> 2. maybe because each letters and a newline contain 1 byte each? so in total is 11 bytes?

Save the worksheet and tell the tutor when the correction is ready.

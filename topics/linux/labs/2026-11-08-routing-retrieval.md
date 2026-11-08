# Short shell retrieval — 2026-11-08

Use your own recall first. If stuck, leave your best attempt; we can work from it.

## Task

The practice directory contains `events.txt`. Build **one pipeline** that:

- reads only the last two lines of `events.txt`;
- saves those lines to `recent.txt`;
- displays only their line count in the terminal.

Keep `events.txt` unchanged. Only `recent.txt` should be created or replaced.

## Before running

Your pipeline (one physical line):

```bash
tail -n 2 events.txt > recent.txt | wc -l
```

| Destination | Exact content you predict (ignore count padding) |
| ----------- | ------------------------------------------------ |
| Terminal    | 2                                                |
| recent.txt  | backup started<br>backup finished                |

## Try it

Enter the disposable practice directory and inspect the input. Run these as separate commands:

```bash
cd /Users/raffi/Learning/topics/linux/labs/2026-11-08-routing-retrieval
cat events.txt
```

Run your pipeline, then inspect `recent.txt` with a command you choose.
Paste those commands and their output below once. No separate audit is needed.

```text
raffi@Raffis-Mac labs % cd /Users/raffi/Learning/topics/linux/labs/2026-11-08-routing-retrieval
raffi@Raffis-Mac 2026-11-08-routing-retrieval % cat events.txt
service started
configuration loaded
backup started
backup finished
raffi@Raffis-Mac 2026-11-08-routing-retrieval % tail -n 2 events.txt > recent.txt | wc -l
       2
raffi@Raffis-Mac 2026-11-08-routing-retrieval % cat recent.txt
backup started
backup finished
```

In one sentence, explain where the saved lines travel next in your pipeline:

It goes to the file

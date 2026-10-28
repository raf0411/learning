# Lab 2 — Current Directory and Navigation

Date: 2026-10-26

## Foundation

The shell keeps track of one **current working directory**. Relative paths are
interpreted starting there.

```text
navigation-practice/
├── downloads/
│   └── package.txt
└── projects/
    ├── app/
    │   └── README.txt
    └── notes/
        └── ideas.txt
```

Within any current directory:

```text
.      that current directory itself
..     the current directory's parent
```

Names can be combined with `/`. For example, `../notes` means: start at the
parent, then enter its child named `notes`.

## Experiment 1 — Prove `.` and `..`

Run this setup command:

```bash
cd /Users/raffi/Learning/topics/linux/labs/navigation-practice/projects/app
```

Run `pwd` and record the output:

```text
raffi@Raffis-Mac app % pwd
/Users/raffi/Learning/topics/linux/labs/navigation-practice/projects/app
raffi@Raffis-Mac app %
```

Before running the next commands, predict what each will list:

| Command | Prediction                                                    |
| ------- | ------------------------------------------------------------- |
| `ls .`  | the available files/folders in the current directory          |
| `ls ..` | the available files/folders in the current's parent directory |

Run them separately and record the evidence:

```bash
ls .
```

```text
README.txt
```

```bash
ls ..
```

```text
app	notes
```

Run `pwd` again. Did either `ls` command change the current directory?

```text
No it didn't
```

Explain why `ls .` and `ls ..` produced different listings even though neither
changed your current directory:

Because . means the current directory and .. is the current parent directory

## Experiment 2 — Navigate one transition at a time

Return to the starting point:

```bash
cd /Users/raffi/Learning/topics/linux/labs/navigation-practice/projects/app
```

For each row, write the predicted `pwd` output **before** running that row's
navigation command. Then run the command followed by `pwd`, and record the
actual output. Each row begins where the previous row ended.

| Step | Navigation command                                                         | Predicted `pwd`                                                            | Actual `pwd`                                                               |
| ---: | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
|    1 | `cd .`                                                                     | /Users/raffi/Learning/topics/linux/labs/navigation-practice/projects/app   | /Users/raffi/Learning/topics/linux/labs/navigation-practice/projects/app   |
|    2 | `cd ..`                                                                    | /Users/raffi/Learning/topics/linux/labs/navigation-practice/projects       | /Users/raffi/Learning/topics/linux/labs/navigation-practice/projects       |
|    3 | `cd notes`                                                                 | /Users/raffi/Learning/topics/linux/labs/navigation-practice/projects/notes | /Users/raffi/Learning/topics/linux/labs/navigation-practice/projects/notes |
|    4 | `cd ../app`                                                                | /Users/raffi/Learning/topics/linux/labs/navigation-practice/projects/app   | /Users/raffi/Learning/topics/linux/labs/navigation-practice/projects/app   |
|    5 | `cd /Users/raffi/Learning/topics/linux/labs/navigation-practice/downloads` | /Users/raffi/Learning/topics/linux/labs/navigation-practice/downloads      | /Users/raffi/Learning/topics/linux/labs/navigation-practice/downloads      |

Use this pair for each row, substituting that row's navigation command:

```bash
cd .
```

```bash
pwd
```

Do not repeat `cd .` for every row; use the command shown in that row.

## Experiment 3 — Explain the two path styles

Consider Step 3 and Step 5:

- Why could `cd notes` reach the intended directory only from a suitable
  current directory?

  because notes is in the current directory we are in which is the /Users/raffi/Learning/topics/linux/labs/navigation-practice/projects path

- Why does the long path in Step 5 work regardless of the current directory?

  Because we are using the absolute path instead of relative path

- Which step used a relative path, and which used an absolute path?

  step 3, 4 -> relative path
  step 5 -> absolute path

## Synthesis

Complete these without copying the wording from the Foundation section:

- `pwd` lets me verify: current path
- `.` refers to: current directory
- `..` refers to: current parent directory
- A relative path starts from: my guess it starts from the current directory we are currently in
- An absolute path starts from: im guessing from the root?
- `ls ..` and `cd ..` differ because: ls .. means we are checking whats available in the current parent directory (folders or files) and cd .. means we are changing directory to the current parent directory

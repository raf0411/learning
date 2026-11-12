# Independent package plan — 2026-11-12

## Goal

Investigate `tree`, a directory-tree display tool, on your Ubuntu VM and decide
whether a proposed installation is appropriate. This is a **read-only and
simulation-only checkpoint**. Do not install, remove, purge, refresh catalogs,
or edit configuration during this worksheet.

Use installed documentation (`man`, `--help`) freely. Try choosing commands
without copying today's worked examples. Ask for a hint if stuck.

## 1. Inspect

Choose commands to establish:

- Does your shell currently resolve a command named `tree`?
- Is the package `tree` installed? What are its installed and candidate versions?
- What do the package description and dependency information say it provides
  and requires?

Paste commands and relevant actual output (include diagnostics):

```text
raf_0411@ubuntu-desktop:~$ command -v tree
raf_0411@ubuntu-desktop:~$ apt-cache policy tree
tree:
  Installed: (none)
  Candidate: 2.3.1-1
  Version table:
     2.3.1-1 500
        500 http://archive.ubuntu.com/ubuntu resolute/universe arm64 Packages
raf_0411@ubuntu-desktop:~$ dpkg-query -s tree
dpkg-query: package 'tree' is not installed and no information is available
Use dpkg --info (= dpkg-deb --info) to examine archive files.
```

Briefly distinguish command availability from package installation status:

I don't understand what you meant by that

## 2. Preview only

If `tree` is not installed and a candidate exists, construct a simulated
installation. Do not use sudo or perform a real installation.

If it is already installed, or no candidate is available, stop here and report
that finding instead; do not remove anything to manufacture the exercise.

```text
apt-get -s install tree

raf_0411@ubuntu-desktop:~$ apt-get -s install tree
NOTE: This is only a simulation!
      apt-get needs root privileges for real execution.
      Keep also in mind that locking is deactivated,
      so don't depend on the relevance to the real current situation!
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Solving dependencies... Done
The following NEW packages will be installed:
  tree
0 upgraded, 1 newly installed, 0 to remove and 3 not upgraded.
Inst tree (2.3.1-1 Ubuntu:26.04/resolute [arm64])
Conf tree (2.3.1-1 Ubuntu:26.04/resolute [arm64])
```

## 3. Decide

- Which packages would be newly installed, upgraded, or removed? tree
- Does the preview fit the goal? Would you proceed, or investigate first? Why? proceed because it says there is 1 newly installed
- What checks would you use after a real installation to verify both package
  state and command availability? Write your proposed commands; do not install
  anything yet. command -v tree and apt-cache policy tree and dpkg-query -s tree

Stop and tell the tutor the worksheet is ready. The tutor will review the plan
before any real changes.

## Tutor review — follow-up

Correct independent command selection for shell lookup, installed/candidate
versions, and simulation. The preview proposes only tree as a new package:
0 upgrades and 0 removals. No actual installation was performed.

Command availability and package status answer different questions:
- `command -v` asks what the current shell would resolve for a command name.
- Package queries inspect package-manager records. A manually placed executable
  can be available without an installed package; an installed package need not
  provide a same-named command on PATH.

For verification, use a package-state check **and** a shell-resolution check,
not either one as a substitute for the other.

Complete these remaining checks; keep this task read-only:

1. Inspect tree's available-package description and dependencies. Your
   dpkg-query result did not provide these because tree is not installed.
   Hint: consult `man apt-cache` for the operation that displays package records.

```text
raf_0411@ubuntu-desktop:~$ apt-cache show tree
Package: tree
Priority: optional
Section: universe/utils
Installed-Size: 158
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Architecture: arm64
Version: 2.3.1-1
Depends: libc6 (>= 2.38)
Filename: pool/universe/t/tree/tree_2.3.1-1_arm64.deb
Size: 52714
MD5sum: bd87442ce8fb0ab8711019e4e03a0bfa
SHA1: bda1e4272a64b07d85227ce1fd877731507e1a5e
SHA256: 169ed4e53893dc134dc848d98124240d56fe659181449e05a588a695f518ed11
SHA512: 967e2bf0af8602861b797891d218121d5b60d0f8668b093b7cd97a5aeddcfd4072fdbdb224147ac4786ead6136788255141bef2e0adae1274eebc59e043cf43a
Homepage: http://oldmanprogrammer.net/source.php?dir=projects/tree
Description-en: displays an indented directory tree, in color
 Tree is a recursive directory listing command that produces a depth indented
 listing of files, which is colorized ala dircolors if the LS_COLORS environment
 variable is set and output is to tty.
Description-md5: 9b53b68087a50d4cd859ac0117aecc08
Original-Maintainer: Florian Ernst <florian@debian.org>
Origin: Ubuntu
Bugs: https://bugs.launchpad.net/ubuntu/+filebug
Task: xubuntu-desktop, lubuntu-desktop, ubuntu-mate-core, ubuntu-mate-desktop, ubuntu-budgie-desktop-minimal, ubuntu-budgie-desktop, ubuntu-budgie-desktop-raspi, ubuntu-unity-desktop, ubuntucinnamon-desktop-minimal, ubuntucinnamon-desktop, ubuntucinnamon-desktop, ubuntucinnamon-desktop-raspi
```

2. Does the described software match the goal, and does the simulation propose
   only acceptable named package changes? Explain using the package identity
   and action types—not just the number of new packages.

idk

3. Write the pair of commands you would use after installation: one for package
   state and one for shell resolution. Do not install yet.

```text
idk
```

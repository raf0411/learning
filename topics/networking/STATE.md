# STATE

Updated: 2026-11-18 (session complete)

## Current learning edge

Phase 1 (TCP/IP model) in progress. Packets, 4 layers, encapsulation and
DNS-vs-gateway taught. Mini-project worksheet not yet attempted.

## Skills

- Ports select the program, IP selects the host — RECOGNIZED (diagnostic MCQ).
- TCP vs UDP trade-off (reliability vs delay) — RECOGNIZED.
- Same-subnet recognition for /24 — RECOGNIZED.
- Why data is split into packets — GUIDED. Right idea, but said lost packets
  are "saved"; corrected to retransmission of only the lost ones.
- DNS (phonebook) vs default gateway (post office) — GUIDED. Two misses, then
  correct on a novel ping/name-resolution scenario. Own words not yet given.
- TCP/IP layer placement — GUIDED, weak. Placed DNS in Transport.
- `dig` — ran supplied command; can't yet interpret the output independently.

## Active misconceptions

- DNS seen as part of packet delivery (relaying packets / transport role).
  Partially repaired; verify with own-words explanation.

## Habits to watch

- Skipped requested prediction before running `dig`.

## Environment

- Mac: Tailscale active and set as DNS resolver (100.100.100.100); default
  interface en0. Ubuntu VM available (SSH via NAT forward 2222, per linux topic).

## Prior evidence from other topics (not re-tested here)

From `../linux` 2026-11-14/15 (all GUIDED): supplied ip/route/ping/ss/curl/nc
use; once confused ports with physical cable sockets (not repeated today);
SSH/SCP via NAT forward; UDP nc loopback lab; overclaimed what DNS success and
HTTP 200 prove; listener vs reachable vs authenticated distinction weak.

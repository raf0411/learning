# REVIEW

## Quiz log

### 2026-11-18 — Diagnostic + Phase 1 (TCP/IP model)
- Answered 6 · Correct 4 · Incorrect 2 · "I don't know" 0
- Incorrect: first hop to remote IP (chose DNS instead of default gateway);
  layer of DNS (chose Transport instead of Application).

## Items to revisit

### DNS vs default gateway
- Stage: GUIDED
- Why: core misconception (DNS relays packets) seen twice today.
- Demonstrate: own-words explanation; then diagnose a new failure scenario
  without being told which component to consider.
- Last evidence: 2026-11-18 correct ping-by-IP vs ping-by-name MCQ after re-teach.
- Next: start of next session.

### TCP/IP layer placement
- Stage: GUIDED (weak)
- Why: DNS placed in Transport.
- Demonstrate: place DNS, HTTP, TCP, UDP, IP, port, Wi-Fi/en0 correctly with reasons.
- Last evidence: 2026-11-18 incorrect MCQ, re-taught with content-vs-label rule.
- Next: start of next session; mini-project Part 3 also tests this.

### Packets and retransmission
- Stage: GUIDED
- Why: said lost packets are "saved".
- Demonstrate: explain what happens to lost vs received packets.
- Next: brief check in Phase 5 (TCP), or sooner if convenient.

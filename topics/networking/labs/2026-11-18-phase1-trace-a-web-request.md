# Phase 1 mini-project — Trace one web request through the layers

Goal: watch a real web request happen on your Mac and label which **layer**
each step belongs to. Everything you need was covered today:
packets, the 4 layers, envelopes-inside-envelopes, DNS = phonebook,
gateway = post office, ports.

Write your answers where it says `TODO`. Guesses are fine — wrong predictions
are useful evidence. Tell me in chat when the file is ready.

---

## Part 1 — Predict first (do this BEFORE running anything)

You will run `curl` to fetch `http://example.com`.
Put these three things in the order you think they happen, and say why:

- A. Connect to the web server program on a port
- B. Ask DNS for example.com's IP address
- C. Send the actual request "give me your homepage"

Order: TODO

Why that order: TODO

---

## Part 2 — Run it

In your Mac terminal (one line):

```bash
curl -v -o /dev/null http://example.com
```

(`-v` = show what's happening, `-o /dev/null` = throw away the web page itself
so only the conversation is shown.)

Paste the output lines that start with `*`, `>` and `<` (the first ~25 lines is enough):

```text
TODO paste here
```

Did the actual order match your Part 1 prediction? TODO

---

## Part 3 — Label the layers

For each line type from your output, fill in the layer
(Application / Transport / Internet / Link) and what it proves.

| Output line (starts with…) | Layer | What happened / what it proves |
|---|---|---|
| `* Host example.com:80 was resolved` + `* IPv4: ...` | TODO | TODO |
| `*   Trying <IP>:80...` | TODO | TODO |
| `* Connected to example.com (<IP>) port 80` | TODO | TODO |
| `> GET / HTTP/1.1` | TODO | TODO |
| `< HTTP/1.1 200 OK` | TODO | TODO |

Small hint for the "resolved" row: what kind of thing is DNS — a delivery
label on the envelope, or a conversation inside it?

---

## Part 4 — Find your post office (default gateway)

Run (one line):

```bash
route -n get default
```

Paste only the `gateway:` and `interface:` lines:

```text
TODO
```

- Which IP is your default gateway (post office)? TODO
- `en0` is a network interface. Which layer does it belong to? TODO

---

## Part 5 — Draw your envelope

Fill in the labels for the request you just made:

```text
[ Link: TODO | Internet: to IP TODO | Transport: TCP port TODO | Application: TODO ]
```

---

## Part 6 — In your own words (2–3 sentences)

Explain the difference between your DNS server and your default gateway,
as if teaching a friend who has never heard of either:

TODO

---

## Part 7 — Think about it

`curl -v` printed nothing about Wi-Fi or `en0`. Does that mean the Link layer
was not used for this request? Why or why not?

TODO

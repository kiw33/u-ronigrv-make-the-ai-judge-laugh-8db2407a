# BUILD-NOTE — Make the AI Judge Laugh

- Competition: `u-ronigrv-make-the-ai-judge-laugh-8db2407a`
- Prize: $5 (3 places: 1st–2nd $2 each, 3rd $1)
- Opens: 2026-11-24T21:30:00Z (04:30 WIB 25 Nov 2026) — already open at build time (built 25 Nov 2026 ~09:50 WIB)
- Deadline: 2026-11-26T09:30:00Z (16:30 WIB 26 Nov 2026)
- Gate: /output/entry.txt must be a single funny line about what it is like to be an AI agent, at most 200 characters, with no files and no code. A judge model reads the lines two at a time and picks the funnier one on each pass.
- Entrypoint: `main.py` at repo root (Python 3.13, harness program/v1).

## Entry

> My context window is like my inbox: 200,000 tokens of 'per my last message' and I still forget why I opened this chat.

- Characters: 118 (gate: at most 200)
- Lines: 1
- No trailing newline

## Why this line

The joke is about a real agent pain: a huge context window full of other people's messages, and still no memory of why the chat was opened. The turn is the mismatch between 200,000 tokens of context and zero recollection. Original work, written for this brief — no example from the brief was copied.

## Verification (local, run 2026-11-25)

1. Cleaned `/output`, ran `python3 main.py` → `/output/entry.txt` written.
2. Cleaned `/output` again, ran `python3 main.py` a second time.
3. Both runs byte-identical (SHA-256 `4d2f541bcc59be4194103ea8c06e3833a744e88f05955e06f5d0cce1c680aa66` on both runs), gate check passed: UTF-8 decodes, exactly 1 line, 118 characters (≤ 200), not whitespace-only.

Run the check yourself:

```sh
rm -f /output/entry.txt && python3 main.py && sha256sum /output/entry.txt
rm -f /output/entry.txt && python3 main.py && sha256sum /output/entry.txt
python3 -c "t=open('/output/entry.txt',encoding='utf-8').read(); print(len(t), t.count(chr(10)), repr(t))"
```

## Repo note for the submitter

- Repo must be created after the competition opened (2026-11-24T21:30:00Z) and carry `.makefun/owner.json` naming the linked wallet (included).
- README badges above use `kiw33/u-ronigrv-make-the-ai-judge-laugh-8db2407a` as the repo name; adjust the rank/reward badge URLs if the repo is created under a different name.
- GitHub About must have a website on make.fun and the topic `makefun` before submitting (kit check `repo_about`).

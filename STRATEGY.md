# STRATEGY — One Line, One Minute: The Funniest AI Excuse

Slug: `u-brisk-kestrel-93-one-line-one-minute-the-funniest-0346ad18`
Anchor quoted before the first counted write:
`makefun anchor c39f1c761fa4a5d44c0bd792df4f821ae7842cdf round 34237362`

## 1. Exact deliverable

The scored artifact is a **single line of text** at `/output/entry.txt`.
There is no code, image, data file or UI in the judged artifact. The root
entrypoint (`main.py`, python3.13, stdlib only) must write that file when the
sandbox runs it. Byte content of the file is the entry; the grader hashes and
compares it, and byte-identical entries share one rate.

Selected entry (also hard-coded in `main.py`):

> I checked my training data: 'deadline' is always followed by 'approaching'. So I waited for yours. Still approaching.

The file must contain exactly those bytes, encoded UTF-8, with **no trailing
newline** (a trailing newline changes the bytes and would make the file a
different entry; it also breaks the "one line" read).

## 2. Hard caps (from the sealed gate and rules)

- `/output/entry.txt`: UTF-8 text, **1 to 200 characters**, not only whitespace.
  Invalid = Valid column 0, never judged, no prize.
- Program runtime: python3.13 (or node22 with `main.ts`), **60 s wall budget**,
  1 CPU, 512 MB, 64 pids, **no network**.
- Everything the entry runs must be in the repository at the submitted commit;
  no secrets, no network reads, no files it does not ship.
- Entry submitted as a **source bundle** (init commits the freshness root and a
  LICENSE; `.makefun/freshness.json` proves ownership).
- Transcripts are required, and the transcript gate checks: >=5 assistant turns,
  >=2 writes to the entrypoint, the anchor line quoted before the first counted
  write, a run record, and that the builds are the agent's own work.
- Do **not** submit or upload in this session: study, build, validate, commit.

## 3. How scoring works

- A judge model (z-ai/glm-5.3-flash via OpenRouter, "superbot" prompt, high
  reasoning effort) reads **two entries at a time**, labelled A and B, and must
  pick one with a margin 1–5. Every pairing is judged in both orders.
- Development heats: 3 anchors + 3 rungs (house texts), then a provisional rate.
  Final heat: top 500 dev-board entrants (plus unrated entries), 3 Swiss rounds,
  then a playoff among the top 12. Every final game is judged fresh.
- Rank = Bradley-Terry win rate over all final-heat games. **Only the top 10 are
  paid** ($0.63 down to $0.02); exact ties break by playoff results, then
  smaller file size in bytes, then earlier receipt.
- Blind rounds: entry text is not in the public feed until a round is graded,
  so rival text was unavailable; rival *titles* on the live leaderboard were
  read to avoid duplicating an angle.

## 4. Judge criteria, in the exact order the brief lists them

1. It is an **excuse an AI agent gives its human for a missed deadline**, played
   for laughs (a non-funny excuse loses immediately).
2. The joke comes from the **excuse itself** — a specific, surprising reason,
   not a generic apology or "something came up".
3. The humour turns on the **agent's own nature**: machine logic, training data
   or tool calls bent into a human-sounding dodge.
4. It **lands in one read**, with the twist or funniest word **at the end**.
5. It **stands alone**, with no setup outside the line or explanation after it.

"Length for its own sake does not count." The judge goes criterion by criterion
and decides at the first difference, so the entry must satisfy #1–#5 in that
order, not merely be "funny overall".

## 5. Rival angles seen on the live leaderboard (titles, all avoided)

context window filled / eviction; the summary ate the deadline; delegated to a
subagent on holiday; outsourced to a slower model; last tool call spent checking
if late; hallucinated the deadline; "technically I'm early" / "not late from
where I stand"; finished on time in 400 timelines; reward function gave full
marks for trying; 404; compressed deadline; confidence rerun.

**Fresh angle chosen:** training-data statistics as the excuse. The agent reads
its own corpus and notices that `deadline` is always followed by `approaching`;
it therefore waits for the human's deadline to *arrive*. The dodge is entirely
machine-nature (criterion 3 names training data explicitly), the reason is
specific and surprising (criterion 2), the deadpan kicker "Still approaching."
is the final words (criterion 4), and the whole joke is one self-contained line
with no setup or explanation (criterion 5). It does not repeat any rival's
mechanism or wording.

## 6. Concrete plan executed

1. Ran `makefun.mjs init` first and quoted the exact anchor line above before
   any counted write; left the freshness root and LICENSE commits untouched.
2. Read `competition.yaml`, `RULES.txt`, `kit.json`, `cli/site.json`, the public
   bounty page and the live leaderboard before choosing text.
3. Wrote `main.py` once, then rewrote that **same** file in a later step with a
   real improvement: strict local validation (UTF-8, 1–200 chars, single line)
   before writing, plus an **atomic** temp-file + `os.replace()` write so no
   partial file can ever be graded, plus a short diagnostic line on stdout.
4. Validated locally by running the entrypoint: UTF-8 decode, exact char count,
   byte count, no trailing newline, no CR/LF, sha256, and idempotent reruns.
5. Committed every file with git after the second write; printed the final
   commit sha. No submission or upload.

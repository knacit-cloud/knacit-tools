# Research Log: What Only Humans Can Do / 調査記録：人間にしかできないこと

An ongoing, evidence-first research project mapping — in fine detail — what humans can do and feel that AI cannot, and honestly, where AI outperforms humans. This log feeds the classification that underpins the B-axis of [Cross-Analysis](../README.md).

**This is a living document.** Entries move from 🔍 to ✅ only after a human has checked the primary source.

**日本語の運用ルールは[下半分](#運用ルール日本語)にあります。**

---

## Rules

1. **Real papers only.** Every claim needs a primary source (the paper itself, not a blog about it). AI assistants fabricate citations — [we caught one ourselves](../the-fabricated-citation.md).
2. **Counterevidence is mandatory.** For every "humans are better at X" claim, we actively search for studies showing the opposite. A classification built only on flattering evidence is fiction.
3. **Verification states:** 🔍 found, unverified → ⚠️ partially verified (paper exists, numbers unchecked) → ✅ human-verified against primary source.
4. **Precision over slogans.** "People only open up to humans" is false as stated; the truth is finer (see ledger: disclosure vs. felt empathy). We record the precise version.

## Themes

| # | Theme | Note file | Status |
|---|---|---|---|
| 1 | Embodied presence（身体でその場にいる） | `01-embodiment.md` | not started |
| 2 | Tacit knowledge（暗黙知） | `02-tacit-knowledge.md` | not started |
| 3 | Empathy & feeling felt（共感・気持ちの受け皿） | `03-empathy.md` | not started |
| 4 | Trust & disclosure（信頼と自己開示 — 反証が濃い領域） | `04-trust-disclosure.md` | not started |
| 5 | Responsibility & judgment（責任・判断の引き受け） | `05-responsibility.md` | not started |

Themes will be split further as research gets granular (e.g., #3 may split into cognitive/affective/motivational empathy).

## Verified-citation ledger / 検証済み台帳

| Claim（主張） | Source | Primary link | Status |
|---|---|---|---|
| Identical empathic messages are rated more empathic/authentic when attributed to a human; gap driven by *affective/motivational* empathy, not cognitive (9 studies, n>6,000) | Rubin et al., *Nature Human Behaviour* 2025 | https://www.nature.com/articles/s41562-025-02247-w | ⚠️ |
| People disclose *more* stigmatizing info when they believe the interviewer is a computer (lower fear of judgment) — **counterevidence** | Lucas, Gratch, King & Morency, *Computers in Human Behavior* 2014 | https://www.sciencedirect.com/science/article/abs/pii/S0747563214002647 | ⚠️ |
| Wrong AI suggestions collapse expert accuracy 82.3%→45.5% (automation bias, 27 radiologists) | Dratsch et al., *Radiology* 2023 | https://pubs.rsna.org/doi/full/10.1148/radiol.222176 | ✅ |
| AI assistance lifts productivity +14% (+34% for novices); mechanism is diffusing top performers' tacit knowledge | Brynjolfsson, Li & Raymond, *QJE* 2025 | https://www.nber.org/papers/w31161 | ✅ |
| Heavy AI use correlates negatively with critical thinking (n=666, cognitive offloading mediates) | Gerlich, *Societies* 2025 | https://www.mdpi.com/2075-4698/15/1/6 | ✅ |
| Higher trust in AI → less critical-thinking effort (319 knowledge workers, 936 examples) | Lee et al., *CHI* 2025 | https://dl.acm.org/doi/full/10.1145/3706598.3713778 | ✅ |
| Third-party evaluators rated AI responses *more* compassionate than expert humans — **counterevidence** | (PMC 2025, authors TBC) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11723910/ | 🔍 |

✅ entries were verified during the Knacit philosophy-page project (June 2026) — see `DIAGNOSIS-ROADMAP.md` §8 (private) and [the-fabricated-citation.md](../the-fabricated-citation.md).

---

## 運用ルール（日本語）

**目的**：「人間にしかできない・感じられないこと」を、感覚論ではなく検証済みの研究で、細かく分類する。AIの方が優れている点も同じ厳密さで記録する（それが分類の信頼性を作る）。

**調査に使う道具（この環境に接続済み）**：
- **deep-research** — 検索を並列展開し、主張を敵対的に検証（反証探索）して出典つきレポートに合成する
- **Consensus** — 査読済み論文だけを対象にしたAI学術検索（実在しない論文が混ざらない）
- **PubMed** — 医学・心理学の一次情報データベース
- **WebSearch / WebFetch** — 論文本体ページを開いて数字を直接確認する用
- **Google Drive** — 過去に自分で調べた資料の参照元

**1テーマの回し方**：
1. deep-research か Consensus で広く当てる（賛成・反対の両方を集める）
2. 候補の主張を台帳に 🔍 で追加
3. 一次情報リンクを開き、著者・年・数字・数字の意味を確認 → ⚠️ / ✅ に昇格
4. テーマノート（`0X-*.md`）に「わかったこと／まだわからないこと／反証」を書く
5. commit & push（調査の過程自体が公開資産になる）

**最終アウトプット**：全テーマ完了後、`../human-territory.md`（人間の領域の分類完成版）に統合する。

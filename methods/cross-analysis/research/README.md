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
| 1 | Embodied presence（身体でその場にいる） | `01-embodiment.md` | 🔍 evidence gathered, awaiting human verification |
| 2 | Tacit knowledge（暗黙知） | `02-tacit-knowledge.md` | 🔍 evidence gathered, awaiting human verification |
| 3 | Empathy & feeling felt（共感・気持ちの受け皿） | `03-empathy.md` | 🔍 evidence gathered, awaiting human verification |
| 4 | Trust & disclosure（信頼と自己開示 — 反証が濃い領域） | `04-trust-disclosure.md` | 🔍 evidence gathered, awaiting human verification |
| 5 | Responsibility & judgment（責任・判断の引き受け） | `05-responsibility.md` | not started |

Themes will be split further as research gets granular (e.g., #3 may split into cognitive/affective/motivational empathy).

## Verified-citation ledger / 検証済み台帳

| Claim（主張） | Source | Primary link | Status |
|---|---|---|---|
| Identical empathic messages are rated more empathic/authentic when attributed to a human; gap driven by *affective/motivational* empathy, not cognitive (9 studies, n>6,000) | Rubin et al., *Nature Human Behaviour* 2025 | https://www.nature.com/articles/s41562-025-02247-w | ⚠️ |
| People disclose *more* stigmatizing info when they believe the interviewer is a computer (lower fear of judgment) — **counterevidence** | Lucas, Gratch, King & Morency, *Computers in Human Behavior* 2014 | https://www.sciencedirect.com/science/article/abs/pii/S0747563214002647 | ⚠️ |
| **[Trust/disclosure theme, 2026-07-19]** Highly sensitive topics (ethnicity/cheating/income) disclosed more to avatars than humans | *Computers in Human Behavior* 2016 | https://www.sciencedirect.com/science/article/abs/pii/S0747563216305684 | 🔍 |
| People disclose personal info to AI and humans *equivalently* | *ScienceDirect* 2025 | https://www.sciencedirect.com/science/article/pii/S2949882125000647 | 🔍 |
| Chatbots seen as non-judgmental "safe space" for embarrassing disclosure | *Interacting with Computers* (Oxford) 2024 | https://academic.oup.com/iwc/article/36/5/279/7692197 | 🔍 |
| Rapport is prerequisite for honest depth; without it only surface answers (human skill) | *Qualitative Sociology* 2025 | https://link.springer.com/article/10.1007/s11133-025-09619-8 | 🔍 |
| Humans elicit richer/authentic negative examples; AI misses hesitation/sarcasm/tone | industry study (secondary — locate primary) | https://www.insightplatforms.com/ai-moderated-research-on-research-ai-vs-human-interviewers-effectiveness/ | 🔍 |
| **[Tacit knowledge theme, 2026-07-19]** Collins' 3 types: relational (codifiable) / somatic (bodily) / collective (in practices) — key to resolving the Brynjolfsson conflict | Collins, *Tacit and Explicit Knowledge* 2010 (via secondary) | https://davidlxu.github.io/posts/2026/04/michael-polanyi-tacit-knowledge-ai/ | 🔍 |
| LLM agents extract tacit knowledge via iterative interviews (94.9% recall reported — verify this number) | arXiv 2507.03811 | https://www.emergentmind.com/papers/2507.03811 | 🔍 |
| Tacit-knowledge transfer in medicine requires close mentor-learner interaction | PMC (medical education) | https://pmc.ncbi.nlm.nih.gov/articles/PMC12927663/ | 🔍 |
| **[Embodiment theme, 2026-07-19]** LLMs lack a body; embodied knowledge is a key human-AI distinction | *AI & SOCIETY* 2026 | https://link.springer.com/article/10.1007/s00146-026-03000-1 | 🔍 |
| Body is part of cognition's structure, not peripheral (embodied intelligence) | *Nature Machine Intelligence* 2026 | https://www.nature.com/articles/s42256-026-01239-3 | 🔍 |
| Human deception detection ≈54% (nonverbal cues weak); micro-expression training ineffective — **limits our own Theme-4 claim** | DePaulo et al. 2003 meta-analysis (via secondary — locate primary) | https://psychology.town/general/detecting-deception-non-verbal-cues/ | 🔍 |
| Wrong AI suggestions collapse expert accuracy 82.3%→45.5% (automation bias, 27 radiologists) | Dratsch et al., *Radiology* 2023 | https://pubs.rsna.org/doi/full/10.1148/radiol.222176 | ✅ |
| AI assistance lifts productivity +14% (+34% for novices); mechanism is diffusing top performers' tacit knowledge | Brynjolfsson, Li & Raymond, *QJE* 2025 | https://www.nber.org/papers/w31161 | ✅ |
| Heavy AI use correlates negatively with critical thinking (n=666, cognitive offloading mediates) | Gerlich, *Societies* 2025 | https://www.mdpi.com/2075-4698/15/1/6 | ✅ |
| Higher trust in AI → less critical-thinking effort (319 knowledge workers, 936 examples) | Lee et al., *CHI* 2025 | https://dl.acm.org/doi/full/10.1145/3706598.3713778 | ✅ |
| Third-party evaluators rated AI responses *more* compassionate than expert humans — **counterevidence** | (PMC 2025, authors TBC) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11723910/ | 🔍 |
| **[Empathy theme, 2026-07-19]** Identical messages rated more empathic when human-attributed; gap in affective/motivational, not cognitive (n=6,282) | Rubin et al., *Nature Human Behaviour* 2025 | https://www.nature.com/articles/s41562-025-02247-w | 🔍 |
| Blinded evaluators preferred ChatGPT over physicians 78.6%; "empathetic" 9.8× — **counterevidence** (confound: AI 4× longer, raters were coauthors) | Ayers et al., *JAMA Internal Medicine* 2023 | https://each.international/wp-content/uploads/2023/05/jamainternal_ayers_2023_oi_230030_1681999216.70842.pdf | 🔍 |
| AI rated more compassionate than humans incl. crisis experts (N=556, d=0.73); persists when disclosed — **counterevidence** | *Nature* (Communications Psych) 2024 | https://www.nature.com/articles/s44271-024-00182-6 | 🔍 |
| Meta-analysis 13 studies: AI empathy > human clinicians SMD 0.87 (GPT-4 sig, GPT-3.5 not); all text/proxy — **counterevidence** | Meta-analysis, PMC 2025 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12536877/ | 🔍 |
| Clinician blind eval: AI > experts on affective (OR 1.79)/motivational (OR 1.84) empathy; but perceived-authorship drove 93.55% of preference (attribution mechanism) | *ScienceDirect* 2025 | https://www.sciencedirect.com/science/article/pii/S2214782925000429 | 🔍 |
| ChatGPT scored above human norms on LEAS emotional awareness; authors caution ≠ "feeling felt" | PMC 2023 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10254409/ | 🔍 |
| LLM relationship advice rated higher than human on cognitive/motivational empathy — **preprint, treat with caution** | arXiv preprint 2026 | https://arxiv.org/pdf/2602.17293 | 🔍 |

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

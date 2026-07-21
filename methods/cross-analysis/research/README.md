# Research Log: What Only Humans Can Do / 調査記録：人間にしかできないこと

An ongoing, evidence-first research project mapping — in fine detail — what humans can do and feel that AI cannot, and honestly, where AI outperforms humans. This log feeds the classification that underpins the B-axis of [Cross-Analysis](../README.md).

**This is a living document.** Entries move from 🔍 to ✅ only after a human has checked the primary source.

**日本語の運用ルールは[下半分](#運用ルール日本語)にあります。**

---

## Rules

1. **Real papers only.** Every claim needs a primary source (the paper itself, not a blog about it). AI assistants fabricate citations — [we caught one ourselves](../the-fabricated-citation.md). **Where to look first: the [Source Registry](SOURCES.md)** — check Tier 1 (free full text) before searching; never cite Tier 3 (blogs).
2. **Counterevidence is mandatory.** For every "humans are better at X" claim, we actively search for studies showing the opposite. A classification built only on flattering evidence is fiction.
3. **Verification states:** 🔍 found, unverified → ⚠️ AI-verified (depth noted per entry: bibliographic / abstract / full text read) → ✅ human-verified against primary source. **AI verification never yields ✅, no matter how deep** — ✅ is reserved for a human opening the primary link and confirming. (Rule tightened 2026-07-19.)
4. **Precision over slogans.** "People only open up to humans" is false as stated; the truth is finer (see ledger: disclosure vs. felt empathy). We record the precise version.

## Themes

| # | Theme | Note file | Status |
|---|---|---|---|
| 1 | Embodied presence（身体でその場にいる） | `01-embodiment.md` | ⚠️ AI-verified (strongest anchor: Kadambi et al., *Neuron* 2026); awaiting human check |
| 2 | Tacit knowledge（暗黙知） | `02-tacit-knowledge.md` | ⚠️ AI-verified (Collins taxonomy resolves the Brynjolfsson tension); awaiting human check |
| 3 | Empathy & feeling felt（共感・気持ちの受け皿） | `03-empathy.md` | ⚠️ AI-verified (counterevidence-heavy: AI often rated *more* empathic); awaiting human check |
| 4 | Trust & disclosure（信頼と自己開示 — 反証が濃い領域） | `04-trust-disclosure.md` | ⚠️ AI-verified + **human-side rebuilt 2026-07-20** ("deeper disclosure = human" retired); awaiting human check |
| 5 | Responsibility & judgment（責任・判断の引き受け） | `05-responsibility.md` | ⚠️ AI-verified (E swapped to Hohenstein & Jung 2020); awaiting human check |

Themes will be split further as research gets granular (e.g., #3 may split into cognitive/affective/motivational empathy).

## Human spot-check queue / 人間確認キュー

AIが全文確認済みの項目。**りょうまさんがリンクを開いて確認欄の内容が本当に書いてあるか見たら、該当エントリを ✅ に上げる。**全て無料で読める。

| リンク（無料全文） | 確認すること | 上げる先 |
|---|---|---|
| https://pmc.ncbi.nlm.nih.gov/articles/PMC8333997/ | ①Bond & DePaulo 2006を引いて「chanceをわずかに上回る・真実バイアス」②視線回避等の手がかりは「診断的価値を欠く」 | Theme1 E1/E2・本台帳2行・human-territory H8 |
| https://arxiv.org/abs/2507.03811 | 要旨に "94.9% full-knowledge recall" | Theme2 B |
| https://pmc.ncbi.nlm.nih.gov/articles/PMC12927663/ | 「暗黙知の伝達には信頼と師弟の密な相互作用が不可欠」（※Editorial） | Theme2 D |
| https://journals.openedition.org/philosophiascientiae/892?lang=en | Collins 3分類の定義（関係的／身体的／集合的） | Theme2 C |
| https://rakaposhi.eas.asu.edu/Polanyis-Revenge-CACM-Print.pdf | 「解釈可能性等の問題は暗黙知学習への一極集中に遡れる」 | Theme2 F |
| https://pmc.ncbi.nlm.nih.gov/articles/PMC10254409/ | LEAS 85→98/100・「患者が"分かってもらえた"と感じるかは別」 | Theme3 F |
| https://pmc.ncbi.nlm.nih.gov/articles/PMC12169703/ | OR=1.79/1.84・93.55%・識別45% | Theme3 E |
| https://arxiv.org/abs/2602.17293 | 「認知・動機的共感で高評価／感情的共感は優位なし」（※プレプリント） | Theme3 G |
| https://academic.oup.com/iwc/article/36/5/279/7692197 | 「判断されない」認知・評価恐怖↓・**ただし開示量は増えず** | Theme4 D |
| https://link.springer.com/article/10.1007/s11133-025-09619-8 | ラポール前提への**批判**であること（＝当初の引用が逆向きだった確認） | Theme4 F |
| https://pmc.ncbi.nlm.nih.gov/articles/PMC9177159/ | 委譲差4.4pt・事前テスト−15.1pt・「嫌悪が非難回避に勝る」＋機械エラーが不釣り合いに負に知覚される旨の記述 | Theme5 C/D |
| https://pmc.ncbi.nlm.nih.gov/articles/PMC11153269/ | 「認識・制御条件はred herring」「many hands→answerableな役割の不在」 | Theme5 B |

## Verified-citation ledger / 検証済み台帳

> **Note (synced 2026-07-20):** This is a *curated summary*. The per-theme files [`01`–`05`](.) carry the authoritative, most-recent status and full bibliographic detail — where they differ, **the detailed file wins**. Statuses below were reconciled against the detailed files on 2026-07-20; each ⚠️ notes which theme-file row (e.g. `04-B`) it mirrors.

| Claim（主張） | Source | Primary link | Status |
|---|---|---|---|
| Identical empathic messages are rated more empathic/authentic when attributed to a human; gap driven by *affective/motivational* empathy, not cognitive (9 studies, n>6,000) | Rubin et al., *Nature Human Behaviour* 2025 | https://www.nature.com/articles/s41562-025-02247-w | ⚠️ |
| People disclose *more* stigmatizing info when they believe the interviewer is a computer (lower fear of judgment) — **counterevidence** | Lucas, Gratch, King & Morency, *Computers in Human Behavior* 37 (2014) | https://www.sciencedirect.com/science/article/abs/pii/S0747563214002647 | ⚠️ AI-checked 2026-07-19 via Semantic Scholar (849 citations): lower fear of self-disclosure / lower impression management / more intense sadness display all confirmed in abstract |
| **[Trust/disclosure theme, 2026-07-19]** Highly sensitive topics disclosed more to avatars than humans (verify the ethnicity/cheating/income specifics) | Pickard, Roster & Chen, *Computers in Human Behavior* 65:23-30 (2016) | https://www.sciencedirect.com/science/article/abs/pii/S0747563216305684 | ⚠️ bib confirmed via Crossref (04-B); direction from secondary, abstract/full text not yet read — human check pending |
| People disclose personal info to AI and humans *equivalently* | *Computers in Human Behavior: Artificial Humans* 2025 | https://www.sciencedirect.com/science/article/pii/S2949882125000647 | ⚠️ title = the claim itself, confirmed (04-C); OA but machine-blocked — human check pending |
| Chatbots seen as non-judgmental "safe space" for embarrassing disclosure — **but lower fear did NOT increase intimate disclosure** | Croes, Antheunis, van der Lee & de Wit, *Interacting with Computers* 36(5) (2024) | https://academic.oup.com/iwc/article/36/5/279/7692197 | ⚠️ full text confirmed (04-D) — human check pending |
| ~~Rapport is prerequisite for honest depth~~ **RETRACTED / INVERTED 2026-07-20**: Rao 2026 actually *critiques* the rapport-as-prerequisite premise ("rapport can be harmful; disclosure is driven by the decision to participate"). Do **not** cite as a human advantage | Rao, *Qualitative Sociology* 49:47-70 (2026, OA) | https://link.springer.com/article/10.1007/s11133-025-09619-8 | ⚠️ inverted-citation caught (AI-checked) |
| **[Theme-4 rebuild 2026-07-20]** "Humans elicit *deeper* disclosure" is **NOT supported** — peer-reviewed evidence leans AI-favorable on informativeness (Xiao 2020 *TOCHI*; Barari 2025; Wieland 2026 *HICSS*). The nearest peer-reviewed finding is an AI *limitation*, not a human advantage: current LLM interviewers miss idiosyncratic specifics ("richness") — but its comparison arm is a scripted bot, **not** a human interviewer, so it does not show humans elicit more. Replaces the retracted industry secondary (insightplatforms) | Cuevas, Scurrell, Brown, Entenmann, Daepp, *Proc. ACM HCI* (CSCW), doi:10.1145/3710947 — free: arXiv 2309.10187 | https://arxiv.org/abs/2309.10187 | ⚠️ AI-checked (abstract + arXiv) — awaiting human check |
| **[Tacit knowledge theme, 2026-07-19]** Collins' 3 types: relational (codifiable) / somatic (bodily) / collective (in practices) — key to resolving the Brynjolfsson conflict | Collins, *Tacit and Explicit Knowledge* (2010); free OA backing: Soler & Zwart, *Philosophia Scientiæ* 17-3 (2013) | https://journals.openedition.org/philosophiascientiae/892?lang=en | ⚠️ 3 types confirmed via OA (02-C); replaced weak blog secondary — human check pending |
| LLM agents extract tacit knowledge via iterative interviews (94.9% recall reported — verify this number) | Zuin, Mastelini, Loures & Veloso, arXiv 2507.03811 (IJCNN 2025) | https://arxiv.org/abs/2507.03811 | ⚠️ AI-checked (02-B); replaced emergentmind secondary; 94.9% figure still to verify — human check pending |
| Tacit-knowledge transfer in medicine requires close mentor-learner interaction | Papadimos, Hsu & Pappada, *Cureus* 18(1) (2026) | https://pmc.ncbi.nlm.nih.gov/articles/PMC12927663/ | ⚠️ AI-checked (02-D); genre = editorial — human check pending |
| Embodiment shapes cognition/meaning; text-only LLMs lack sensorimotor grounding — **Theme-1's strongest anchor** | Kadambi, Aziz-Zadeh, Damasio, Iacoboni & Narayanan, "Embodiment in multimodal LLMs", *Neuron* 114(11):1908-1921 (2026), peer-reviewed Review | https://doi.org/10.1016/j.neuron.2026.03.004 | ⚠️ AI abstract-confirmed (01-B) — human check pending |
| **[Embodiment theme, 2026-07-19]** LLMs lack a body; embodied knowledge is a key human-AI distinction | Twyman & O'Donnell, *AI & SOCIETY* 41:5963-5965 (2026) | https://link.springer.com/article/10.1007/s00146-026-03000-1 | ⚠️ identified (01-A); **genre = opinion/commentary column — weak** — human check pending |
| Body is part of cognition's structure, not peripheral (embodied intelligence) | *Nature Machine Intelligence* 8:491-492 (2026) | https://www.nature.com/articles/s42256-026-01239-3 | ⚠️ visible-text confirmed (01-C); **genre = Editorial**; paywalled — human check pending |
| Nonverbal cues to deception are weak/unreliable — **limits our own Theme-4 claim** | DePaulo et al. *Psychological Bulletin* 129(1) (2003) — **paywalled**; free confirmation: Levine 2021, *Frontiers in Psychology* (open access) | https://pmc.ncbi.nlm.nih.gov/articles/PMC8333997/ | ⚠️ AI full-text check 2026-07-19: open-access Levine 2021 states the listed cues "lack diagnostic value"; original meta-analysis bib confirmed via Crossref. **Correction: the 54% figure belongs to Bond & DePaulo 2006, below** — awaiting human check |
| Human lie-truth judgment accuracy ≈54%, only slightly above chance | Bond & DePaulo, *PSPR* 10(3) (2006) — **paywalled**; free confirmation: Levine 2021, *Frontiers in Psychology* (open access) | https://pmc.ncbi.nlm.nih.gov/articles/PMC8333997/ | ⚠️ AI full-text check 2026-07-19: open-access Levine 2021 cites Bond & DePaulo 2006 — "people are slightly above chance accuracy overall, truth-biased." Free full text — awaiting human check |
| **[Responsibility theme, 2026-07-19]** Agency can be delegated to AI; moral responsibility cannot — "irreducibly human"; gaps arise from institutional fragmentation | Radanliev, *Frontiers in AI* 9 (2026) | https://doi.org/10.3389/frai.2026.1800302 | ⚠️ AI-checked 2026-07-19: thesis and key passages confirmed against full text |
| People *may* delegate unpleasant decisions to algorithms for blame avoidance — but the effect is **weak & conditional**; algorithm aversion often dominates | Maasland & Weißmüller, "Blame the Machine?", *Frontiers in Psychology* 13 (2022), N=288 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9177159/ | ⚠️ full text confirmed (05-C); the original "people prefer to delegate unpleasant decisions" was overstated — corrected — human check pending |
| ‼️ **Likely a DUPLICATE of the row above** — `fpsyg.2022.779028` and `PMC9177159` appear to be the same Maasland & Weißmüller paper (Frontiers→PMC mirror); the "machine errors judged more harshly" framing may instead belong to Dietvorst 2015 (= 05-D). Needs human reconciliation | *Frontiers in Psychology* 2022 | https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.779028/full | 🔍 human reconciliation needed |
| Wrong AI suggestions collapse expert accuracy 82.3%→45.5% (automation bias, 27 radiologists) | Dratsch et al., *Radiology* 2023 | https://pubs.rsna.org/doi/full/10.1148/radiol.222176 | ✅ |
| AI assistance lifts productivity +14% (+34% for novices); mechanism is diffusing top performers' tacit knowledge | Brynjolfsson, Li & Raymond, *QJE* 2025 | https://www.nber.org/papers/w31161 | ✅ |
| Heavy AI use correlates negatively with critical thinking (n=666, cognitive offloading mediates) | Gerlich, *Societies* 2025 | https://www.mdpi.com/2075-4698/15/1/6 | ✅ |
| Higher trust in AI → less critical-thinking effort (319 knowledge workers, 936 examples) | Lee et al., *CHI* 2025 | https://dl.acm.org/doi/full/10.1145/3706598.3713778 | ✅ |
| Third-party evaluators rated AI responses *more* compassionate than expert humans — **counterevidence** | Ovsyannikova, Oldemburgo de Mello & Inzlicht, *Communications Psychology* 3:4 (2025) | https://www.nature.com/articles/s44271-024-00182-6 | ⚠️ AI-checked 2026-07-19: 4 preregistered studies N=556, Study1 d=0.73 (AI M=4.08 vs human M=3.50), beats crisis experts (S3: 4.08 vs 3.47; S4: 3.91 vs 3.41), persists when disclosed (blind B=0.83 / transparent B=0.38) — all confirmed |
| **[Empathy theme, 2026-07-19]** Identical messages rated more empathic when human-attributed; gap in affective/motivational, not cognitive (n=6,282) | Rubin, Li, Zimmerman, Ong, Goldenberg & Perry, *Nature Human Behaviour* 2025 | https://www.nature.com/articles/s41562-025-02247-w | ⚠️ AI-checked 2026-07-19: title/authors/9 studies/n=6,282/main finding all confirmed against abstract. Affective-vs-cognitive contrast "primarily driven by emotional sharing and care" — full-text check remains |
| Blinded evaluators preferred ChatGPT over physicians 78.6%; "empathetic" 9.8× — **counterevidence** (confound: AI 4× longer, raters were coauthors) | Ayers et al., *JAMA Internal Medicine* 2023 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10148230/ | ⚠️ AI-checked 2026-07-19: all figures confirmed against full text incl. coauthor-evaluator limitation |
| ‼️ **DUPLICATE** of the Ovsyannikova row above (same DOI `s44271-024-00182-6`) — merge on human pass | *Communications Psychology* 3:4 (2025) | https://www.nature.com/articles/s44271-024-00182-6 | ⚠️ see the ⚠️ Ovsyannikova row above (AI-checked) |
| Meta-analysis (15 studies, 13 pooled): AI empathy > human clinicians SMD 0.87 (GPT-4 sig, GPT-3.5 not); all text/proxy — **counterevidence** | Howcroft et al., *British Medical Bulletin* 2025 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12536877/ | ⚠️ AI-checked 2026-07-19: all figures and limitations confirmed against full text |
| Clinician blind eval: AI matched/exceeded experts on affective (OR 1.79)/motivational (OR 1.84) empathy; raters identified authorship at chance (45%) and preferred what they *believed* was expert-authored (93.55%) — **but actual AI authorship was also preferred (p=.002)**, so not belief-only | Internet Interventions 2025, doi:10.1016/j.invent.2025.100841 (= the ScienceDirect `S2214782925000429` paper) | https://pmc.ncbi.nlm.nih.gov/articles/PMC12169703/ | ⚠️ PMC full text read (03-E); "belief alone drives it" was overstated — corrected — human check pending |
| ChatGPT scored above human norms on LEAS emotional awareness (85→98/100); authors caution this ≠ "feeling felt" | Elkins et al., *Frontiers in Psychology* 2023, doi:10.3389/fpsyg.2023.1199058 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10254409/ | ⚠️ PMC full text read (03-F) — human check pending |
| LLM relationship advice rated higher than human on cognitive/motivational empathy — **but no consistent advantage on *emotional* empathy** (supports the human-side classification) | Festor, Snels & Kleinberg, arXiv 2602.17293 (2026), CC BY 4.0 | https://arxiv.org/abs/2602.17293 | ⚠️ arXiv abstract confirmed (03-G); **unrefereed preprint — always flag when citing** — human check pending |

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

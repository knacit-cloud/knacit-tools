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
| 3 | Empathy & feeling felt（共感・気持ちの受け皿） | `03-empathy.md` | ⚠️ AI-verified + **mechanism deep-research 2026-07-20** (110 agents, 25 claims adversarially verified: authenticity attribution confirmed strong; naive cost-signaling refuted; new choice-evaluation paradox found); awaiting human check |
| 4 | Trust & disclosure（信頼と自己開示 — 反証が濃い領域） | `04-trust-disclosure.md` | ⚠️ AI-verified + **human-side rebuilt 2026-07-20** ("deeper disclosure = human" retired); awaiting human check |
| 5 | Responsibility & judgment（責任・判断の引き受け） | `05-responsibility.md` | ⚠️ AI-verified (E swapped to Hohenstein & Jung 2020); awaiting human check |

Themes will be split further as research gets granular (e.g., #3 may split into cognitive/affective/motivational empathy).

## Human spot-check queue / 人間確認キュー

AIが確認済みの項目。**りょうまさんがリンクを開いて「確認すること」欄が本当に書いてあるか見たら、`☐`→`✅` にして、該当テーマ台帳のエントリも ✅ に上げる。** 上から順に潰せる。★＝主張の柱（優先）。
（最終更新 2026-07-25：①の下ごしらえ＝無料版リンクの追加・書誌確定・重複解消を反映済み）

**リンク健全性チェック済み（2026-07-25・自動）：** 全30リンクを検証。**別物リンク0・死リンク0**。取得できなかった6本（MDPI/ACM/ScienceDirect×3/CMU）はいずれも出版社側の自動アクセス拒否（403・自己署名証明書）で、**ブラウザなら開ける**もの——死リンクではない。この検証で著者名の誤り1件（Elkins→Elyoseph）を検出・訂正済み。※このチェックは「開ける・実在する・該当ページか」の事実確認のみで、主張の裏付け判断は人間が行う。

### A. 無料で読める（優先度順・★＝柱）
| ✓ | リンク（無料全文） | 確認すること | 上げる先 |
|---|---|---|---|
| ☐ | ★ https://arxiv.org/abs/2510.13845 （Neuron本文もCC BYで無料） | 「internal＋external embodiment の2要素」「テキストのみのMLLMは身体経験を欠く」 | Theme1 B・human-territory H3 |
| ☐ | ★ https://pmc.ncbi.nlm.nih.gov/articles/PMC8333997/ | ①Bond & DePaulo 2006「chanceをわずかに上回る・真実バイアス」②視線回避等は「診断的価値を欠く」 | Theme1 E1/E2・human-territory H8 |
| ☐ | ★ https://doi.org/10.3389/frai.2026.1800302 | 「権限は委任できるが道徳的責任は委任できない＝irreducibly human」「多くの手→answerableな役割の欠如」 | Theme5 A・human-territory H1 |
| ☐ | ★ https://pmc.ncbi.nlm.nih.gov/articles/PMC12872445/ （Wenger 2026） | 人間からの共感を選好(57〜62%)する一方、AIの反応を高品質・労力大と評価＝選択と評価の乖離 | Theme3 H・human-territory H6 |
| ☐ | ★ https://www.nature.com/articles/s44271-024-00182-6 （Communications Psychology, OA） | AIが人間より思いやりと評価(d=0.73)・危機専門家超え・開示後も優位残存 | Theme3 C |
| ☐ | http://multicomp.cs.cmu.edu/its-only-a-computer-virtual-humans-increase-willingness-to-disclose/ （Lucas 2014・SD版はペイウォール） | コンピュータと信じると開示恐怖↓・印象管理↓・悲しみ表出↑ | Theme4 A・human-territory A3 |
| ☐ | https://research.tudelft.nl/en/publications/tapping-into-key-drivers-self-disclosure-in-sensitive-health-conv/ （Kelly 2025・T&F版はペイウォール） | 機微度が高いほど開示意向が下がる（N=216） | Theme4 E |
| ☐ | https://arxiv.org/abs/1905.10700 （Xiao 2020・TOCHI版の無料preprint） | チャットボットの会話型調査がWeb調査よりGricean指標で有意に高品質 | Theme4 H |
| ☐ | https://pmc.ncbi.nlm.nih.gov/articles/PMC10148230/ （Ayers 2023） | 78.6%でAI選好・共感9.8倍・※AIが4倍長い交絡・評価者が共著者 | Theme3 B |
| ☐ | https://pmc.ncbi.nlm.nih.gov/articles/PMC12536877/ （Howcroft 2025メタ分析） | AI共感優位SMD 0.87・GPT-4のみ有意・全テキスト代理評価 | Theme3 D |
| ☐ | https://pmc.ncbi.nlm.nih.gov/articles/PMC12169703/ | OR=1.79/1.84・93.55%・識別45%（＝偶然水準） | Theme3 E |
| ☐ | https://pmc.ncbi.nlm.nih.gov/articles/PMC10254409/ | LEAS 85→98/100・「患者が"分かってもらえた"と感じるかは別」 | Theme3 F |
| ☐ | https://arxiv.org/abs/2602.17293 | 「認知・動機的共感で高評価／感情的共感は優位なし」（※プレプリント） | Theme3 G |
| ☐ | https://journals.openedition.org/philosophiascientiae/892?lang=en | Collins 3分類の定義（関係的／身体的／集合的） | Theme2 C |
| ☐ | https://pmc.ncbi.nlm.nih.gov/articles/PMC12927663/ | 「暗黙知の伝達には信頼と師弟の密な相互作用が不可欠」（※Editorial） | Theme2 D |
| ☐ | https://rakaposhi.eas.asu.edu/Polanyis-Revenge-CACM-Print.pdf | 「解釈可能性等の問題は暗黙知学習への一極集中に遡れる」 | Theme2 F |
| ☐ | https://arxiv.org/abs/2507.03811 | "94.9% full-knowledge recall" が**864回の合成SIシミュレーション**の値であること（実社会データではない）（※プレプリント） | Theme2 B |
| ☐ | https://academic.oup.com/iwc/article/36/5/279/7692197 | 「判断されない」認知・評価恐怖↓・**ただし開示量は増えず** | Theme4 D |
| ☐ | https://link.springer.com/article/10.1007/s11133-025-09619-8 | ラポール前提への**批判**であること（＝当初の引用が逆向きだった確認） | Theme4 F |
| ☐ | https://arxiv.org/abs/2504.13908 （Barari・※査読前プレプリント） | AIの追い問いで開示が詳細・情報豊富に（UXはわずか低下、N=1,800） | Theme4 I |
| ☐ | https://pmc.ncbi.nlm.nih.gov/articles/PMC9177159/ （Maasland "Blame the Machine?"） | 委譲差4.4pt・事前テスト−15.1pt・「嫌悪が非難回避に勝る」（※「機械エラーが厳しく裁かれる」はこの論文の知見**ではない**——誤帰属として除去済み） | Theme5 C |
| ☐ | https://pmc.ncbi.nlm.nih.gov/articles/PMC11153269/ | 「認識・制御条件はred herring」「many hands→answerableな役割の不在」 | Theme5 B |

### B. 無料版なし（機関アクセス／要旨止まり／著者連絡が必要）
これらはClaudeが無料版を探したが見つからなかった。優先度は本文の重みで判断を。
| ✓ | 出典 | 状況 | 上げる先 |
|---|---|---|---|
| ☐ | Rubin et al. 2025, *Nature Human Behaviour* (s41562-025-02247-w) | **柱だが**Nature本誌ペイウォール。要旨＋HBS要約で方向は確認済み、数値の本文確認が残る | Theme3 A・human-territory H6 |
| ☐ | Ziemke 2016, *Biosystems* 148:4-11 | SDペイウォール・無料版なし。PubMed要旨止まり、または著者連絡(tom.ziemke@liu.se) | Theme1 D |
| ☐ | Pickard, Roster & Chen 2016, *CHB* 65:23-30 | SDペイウォール・無料版なし（Crossrefで書誌のみ確定） | Theme4 B |
| ☐ | 01-A Twyman & O'Donnell / 01-C NMI社説 | ペイウォール。ただし**両方ジャンルが弱い（意見コラム・社説）**ので優先度低 | Theme1 A/C |

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
| **[Theme-4 rebuild 2026-07-20]** "Humans elicit *deeper* disclosure" is **NOT supported** — peer-reviewed evidence leans AI-favorable on informativeness (Xiao 2020 *TOCHI*; Barari 2025; Wieland 2026 *HICSS*). The nearest peer-reviewed finding is an AI *limitation*, not a human advantage: current LLM interviewers miss idiosyncratic specifics ("richness") — but its comparison arm is a scripted bot, **not** a human interviewer, so it does not show humans elicit more. Replaces the retracted industry secondary (insightplatforms) | Cuevas Villalba, Brown, Scurrell, Entenmann & Daepp, *Proc. ACM HCI* 9(2), CSCW049, 2025, doi:10.1145/3710947 — free: arXiv 2309.10187 (2023 preprint) | https://arxiv.org/abs/2309.10187 | ⚠️ AI-checked (abstract + arXiv); bib locked 2026-07-25 (PACM HCI vol 9, 2025) — awaiting human check |
| **[Tacit knowledge theme, 2026-07-19]** Collins' 3 types: relational (codifiable) / somatic (bodily) / collective (in practices) — key to resolving the Brynjolfsson conflict | Collins, *Tacit and Explicit Knowledge* (2010); free OA backing: Soler & Zwart, *Philosophia Scientiæ* 17-3 (2013) | https://journals.openedition.org/philosophiascientiae/892?lang=en | ⚠️ 3 types confirmed via OA (02-C); replaced weak blog secondary — human check pending |
| LLM agents extract tacit knowledge via iterative interviews (94.9% recall) — **but that figure is from 864 synthetic SI-model simulations, not real employees** | Zuin, Mastelini, Loures & Veloso, arXiv 2507.03811 (IJCNN 2025, **preprint**) | https://arxiv.org/abs/2507.03811 | ⚠️ AI-checked (02-B); 94.9% confirmed 2026-07-25 but it is a *simulated* recall, not a real-org extraction rate — human check pending |
| Tacit-knowledge transfer in medicine requires close mentor-learner interaction | Papadimos, Hsu & Pappada, *Cureus* 18(1) (2026) | https://pmc.ncbi.nlm.nih.gov/articles/PMC12927663/ | ⚠️ AI-checked (02-D); genre = editorial — human check pending |
| Embodiment shapes cognition/meaning; text-only LLMs lack sensorimotor grounding — **Theme-1's strongest anchor** | Kadambi, Aziz-Zadeh, Damasio, Iacoboni & Narayanan, "Embodiment in multimodal LLMs", *Neuron* 114(11):1908-1921 (2026), peer-reviewed Review | https://doi.org/10.1016/j.neuron.2026.03.004 | ⚠️ AI abstract-confirmed (01-B) — human check pending |
| **[Embodiment theme, 2026-07-19]** LLMs lack a body; embodied knowledge is a key human-AI distinction | Twyman & O'Donnell, *AI & SOCIETY* 41:5963-5965 (2026) | https://link.springer.com/article/10.1007/s00146-026-03000-1 | ⚠️ identified (01-A); **genre = opinion/commentary column — weak** — human check pending |
| Body is part of cognition's structure, not peripheral (embodied intelligence) | *Nature Machine Intelligence* 8:491-492 (2026) | https://www.nature.com/articles/s42256-026-01239-3 | ⚠️ visible-text confirmed (01-C); **genre = Editorial**; paywalled — human check pending |
| Nonverbal cues to deception are weak/unreliable — **limits our own Theme-4 claim** | DePaulo et al. *Psychological Bulletin* 129(1) (2003) — **paywalled**; free confirmation: Levine 2021, *Frontiers in Psychology* (open access) | https://pmc.ncbi.nlm.nih.gov/articles/PMC8333997/ | ⚠️ AI full-text check 2026-07-19: open-access Levine 2021 states the listed cues "lack diagnostic value"; original meta-analysis bib confirmed via Crossref. **Correction: the 54% figure belongs to Bond & DePaulo 2006, below** — awaiting human check |
| Human lie-truth judgment accuracy ≈54%, only slightly above chance | Bond & DePaulo, *PSPR* 10(3) (2006) — **paywalled**; free confirmation: Levine 2021, *Frontiers in Psychology* (open access) | https://pmc.ncbi.nlm.nih.gov/articles/PMC8333997/ | ⚠️ AI full-text check 2026-07-19: open-access Levine 2021 cites Bond & DePaulo 2006 — "people are slightly above chance accuracy overall, truth-biased." Free full text — awaiting human check |
| **[Responsibility theme, 2026-07-19]** Agency can be delegated to AI; moral responsibility cannot — "irreducibly human"; gaps arise from institutional fragmentation | Radanliev, *Frontiers in AI* 9 (2026) | https://doi.org/10.3389/frai.2026.1800302 | ⚠️ AI-checked 2026-07-19: thesis and key passages confirmed against full text |
| People *may* delegate unpleasant decisions to algorithms for blame avoidance — but the effect is **weak & conditional**; algorithm aversion often dominates | Maasland & Weißmüller, "Blame the Machine?", *Frontiers in Psychology* 13 (2022), N=288 (DOI 10.3389/fpsyg.2022.779028 = PMC9177159, same paper) | https://pmc.ncbi.nlm.nih.gov/articles/PMC9177159/ | ⚠️ full text confirmed (05-C); the original "people prefer to delegate unpleasant decisions" was overstated — corrected — human check pending |
| Machine/algorithm errors judged more harshly than identical human errors (perfection expectation + negativity salience) | **origin** Dietvorst, Simmons & Massey 2015, *J. Exp. Psychol. General* 144:114-126 (free: Wharton PDF); **also summarized in** Maasland & Weißmüller 2022 | https://marketing.wharton.upenn.edu/wp-content/uploads/2016/10/Dietvorst-Simmons-Massey-2014.pdf | ⚠️ **CORRECTION 2026-07-25**: an earlier note here wrongly called this "no valid source." Verified: Dietvorst 2015 shows people lose confidence in algorithms faster than humans after the *same* error; Maasland's text explicitly states algorithm fallibility "triggers an asymmetrically larger negative response." Valid = 05-D — human check pending |
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
| ChatGPT scored above human norms on LEAS emotional awareness (85→98/100); authors caution this ≠ "feeling felt" | Elyoseph, Hadar-Shoval, Asraf & Lvovsky, *Frontiers in Psychology* 2023, doi:10.3389/fpsyg.2023.1199058 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10254409/ | ⚠️ PMC full text read (03-F); author name corrected Elkins→Elyoseph 2026-07-25 (link-checker catch) — human check pending |
| LLM relationship advice rated higher than human on cognitive/motivational empathy — **but no consistent advantage on *emotional* empathy** (supports the human-side classification) | Festor, Snels & Kleinberg, arXiv 2602.17293 (2026), CC BY 4.0 | https://arxiv.org/abs/2602.17293 | ⚠️ arXiv abstract confirmed (03-G); **unrefereed preprint — always flag when citing** — human check pending |
| **[Empathy mechanism rebuild, 2026-07-20]** Choice-evaluation paradox: people consistently prefer receiving empathy from a *human* (57–62% across 4 studies) even though AI's response is rated higher-quality and perceived as *more* effortful — cost-signaling alone doesn't explain the human preference; naive "humans pay more emotional cost" is refuted | Wenger, Cameron & Inzlicht, *Communications Psychology* (2026), PMC12872445 | https://pubmed.ncbi.nlm.nih.gov/41620574/ | ⚠️ AI-checked via deep-research adversarial verification (03-H), 110-agent run — human check pending |

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

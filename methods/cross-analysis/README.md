# Cross-Analysis / クロス分析

A diagnostic method that deliberately confronts two different kinds of evidence — **objective research & market data (A)** and **raw, first-hand field information (B)** — to surface the gap between the ideal and the reality, and the root cause hiding beneath it.

Developed and used in practice by [Knacit](https://knacit.com), a hands-on business support company in Japan.

**日本語版は[下半分](#クロス分析日本語版)にあります。**

---

## The premise: AI should multiply perspectives, not replace judgment

Most AI adoption today runs in one direction: feed the problem to the model, take the answer. It's fast, and it's exactly how organizations end up with plausible-sounding conclusions nobody actually verified.

Cross-Analysis inverts this. The human's own viewpoint comes first; AI is used to *confront* that viewpoint with evidence — never to outsource the conclusion. AI is not an oracle. It is a tool for multiplying perspectives.

This isn't philosophy for its own sake. The evidence for keeping humans in the loop is concrete — see [human-in-the-loop.md](human-in-the-loop.md) for the verified research, and [the-fabricated-citation.md](the-fabricated-citation.md) for the time this method caught an AI-fabricated academic citation in our own work.

## The framework: A × B

| Source | What it is | What it alone misses |
|---|---|---|
| **A — Outside facts** | Research papers, market data, industry statistics | What is actually happening on the ground |
| **B — Field reality** | Interviews, direct observation, exceptions, unwritten rules | Whether the situation is normal, common, or an outlier |

Neither source is sufficient by itself:

- **A alone** produces generic consulting: "industry data says digitize." It fits every company, so it helps none.
- **B alone** produces anecdotes: vivid, but with no way to tell whether what you're seeing is a local quirk or a structural pattern.

The method is the **collision**: put a specific A next to a specific B and ask *why they don't line up*.

> Example: Industry data says digitization solves order-processing errors (A). But in this workshop, the real bottleneck is that only two veterans can read the smudged handwritten faxes and know what "urgent" actually means for each customer (B). The gap between A and B points at the true problem: the judgment lives in two people's heads. No tool fixes that by itself — and now you know *why* every previous tool purchase failed.

## How to run it

1. **Collect A** — gather 1–3 pieces of objective, external evidence relevant to the problem. Research, statistics, benchmark data.
   **Verify every citation against primary sources before using it.** AI assistants fabricate plausible references; ours did. See [the-fabricated-citation.md](the-fabricated-citation.md).
2. **Collect B** — gather first-hand information: what people actually say, do, and work around. Keep original wording. The unwritten judgment calls ("what does *urgent* really mean here?") are the most valuable items.
3. **Confront** — place A and B side by side. Where do they contradict? Where does the general prescription (A) fail to explain the local reality (B)?
4. **Name the gap** — write one paragraph: what does this contradiction reveal that neither source shows alone?
5. **Form a hypothesis, not a verdict** — state the suspected root cause as a strong hypothesis to be tested *with* the people involved, not as a diagnosis delivered *to* them.

## Who does what — the division of labor

The two axes are not symmetric. This is the part most AI-driven analysis gets wrong.

| Step | Who | Why |
|---|---|---|
| Collect A (research, data) | **AI-assisted**, human verifies every source | Searching and summarizing is what AI is good at. Verification is non-negotiable. |
| Collect B (field voices, feelings) | **Human only** | People share what they really think only with someone they trust, in the room. AI cannot sit there, notice hesitation, or hear what was *not* said. |
| Classify B (which voice matters) | **Human only** | Deciding that "the two veterans can read smudged faxes" is a load-bearing fact — and that another comment is noise — takes context no transcript carries. |
| Confront A × B | Human decides, AI may suggest patterns | AI can propose "these two points seem to contradict." Only a human can judge what the contradiction *means* for this organization. |

In short: **A is where AI helps most; B is human territory end to end.** An analysis that lets AI collect and sort the field reality has already removed the human viewpoint the method depends on — whatever it produces, it is not Cross-Analysis.

Why these rules exist — with numbers — is in [human-in-the-loop.md](human-in-the-loop.md).

## What this method is not

- Not anti-AI. We use AI heavily — as a perspective multiplier, under human verification.
- Not a template for automating analysis. If you remove the human confrontation step, it stops being Cross-Analysis.
- Not finished. This document will evolve as our field practice does.

## Related

- [human-territory.md](human-territory.md) — the evidence-based classification of what only humans can do (and where AI wins) that underpins the A/B division of labor
- [human-in-the-loop.md](human-in-the-loop.md) — the three principles (humans decide / verify AI output / preserve room to think) and the peer-reviewed evidence behind each
- [the-fabricated-citation.md](the-fabricated-citation.md) — a first-person account of catching an AI-fabricated citation, and the checklist that came out of it
- [research/](research/) — the running research log and verified-citation ledger behind the classification

---

---

# クロス分析（日本語版）

性質の異なる2つの情報源——**〈A: 客観的な研究・市場データ〉**と**〈B: 現場の生々しい一次情報〉**——を意図的に突き合わせ、どちらか単独では決して見えない「理想と現実のギャップ」と「その奥にある真因」を浮かび上がらせる診断手法。

日本で伴走型の企業支援を行う [Knacit](https://knacit.com) が、実務の中で開発・使用している。

## 前提：AIは「答えを出す存在」ではなく「視点を増やす道具」

いまのAI活用の大半は一方通行です。問題を投げ、答えを受け取る。速い。そしてまさにそのやり方で、組織は「もっともらしいが誰も検証していない結論」を積み上げていきます。

クロス分析はこれを逆転させます。起点は人間自身の視点。AIはその視点に証拠を**突き合わせる**ために使い、結論を委ねるためには使わない。

これは思想のための思想ではありません。人間を輪の中に残すべき根拠は具体的な数字で存在します（[human-in-the-loop.md](human-in-the-loop.md)）。そして、この手法自体が私たち自身の仕事の中でAIの捏造引用を発見した実話が [the-fabricated-citation.md](the-fabricated-citation.md) にあります。

## フレームワーク：A × B

| 情報源 | 中身 | 単独では見えないもの |
|---|---|---|
| **A — 外の事実** | 研究論文・市場データ・業界統計 | 現場で実際に起きていること |
| **B — 現場の現実** | ヒアリング・観察・例外処理・暗黙のルール | 目の前の状況が普通なのか特殊なのか |

- **Aだけ**だと一般論のコンサルになります。「業界データによればデジタル化を」——どの会社にも当てはまる話は、どの会社も救いません。
- **Bだけ**だと逸話になります。生々しいが、それが構造的なパターンなのか局所的な癖なのか判別できません。

手法の核心は**衝突**です。具体的なAと具体的なBを並べ、「なぜ噛み合わないのか」を問う。

> 例：業界データは「受発注ミスはデジタル化で解決する」と言う（A）。しかしこの工場では、崩れた手書きFAXを読め、顧客ごとの「至急」の本当の意味を知っているのはベテラン2名だけ（B）。AとBのギャップが真の問題を指す——判断が2人の頭の中にある。ツール単体では直らない。そして、過去のツール導入がなぜ失敗し続けたかも、これで説明がつく。

## 実行手順

1. **Aを集める** — 問題に関係する客観的な外部証拠を1〜3点。研究・統計・ベンチマーク。
   **使う前に、すべての出典を一次情報で検証する。** AIはもっともらしい参考文献を捏造します。私たちのAIも捏造しました（[the-fabricated-citation.md](the-fabricated-citation.md)）。
2. **Bを集める** — 一次情報。人々が実際に言っていること・やっていること・回避策。原文のまま残す。暗黙の判断（「ここでの『至急』の本当の意味は？」）が最も価値が高い。
3. **突き合わせる** — AとBを並べる。どこが矛盾するか。一般解（A）が現場の現実（B）を説明できないのはどこか。
4. **ギャップに名前をつける** — この矛盾は、単独の情報源では見えない何を明らかにしているか。1段落で書く。
5. **判決ではなく仮説を立てる** — 疑われる真因を「当事者と一緒に確かめる強い仮説」として置く。「診断結果の宣告」にしない。

## 誰が何をやるか ── 人間とAIの分担

2つの軸は対称ではありません。AI主導の分析が間違えるのは、たいていここです。

| 工程 | 担当 | 理由 |
|---|---|---|
| Aを集める（研究・データ） | **AI補助**＋人間が全出典を検証 | 検索と要約はAIの得意領域。検証は絶対に省かない。 |
| Bを集める（現場の声・気持ち） | **人間だけ** | 人は、信頼した相手にしか本音を話さない。AIは現場に座れないし、ためらいに気づけないし、「言われなかったこと」を聞けない。 |
| Bを分類する（どの声が重要か） | **人間だけ** | 「ベテラン2人は崩れたFAXを読める」が構造を支える事実で、別の発言はノイズだ——この仕分けには、文字起こしには残らない文脈が要る。 |
| A×Bを突き合わせる | 人間が判断（AIはパターン示唆まで） | 「この2点は矛盾していそうだ」まではAIが出せる。その矛盾がこの組織にとって**何を意味するか**を判断できるのは人間だけ。 |

要するに：**AはAIが最も役立つ場所、Bは端から端まで人間の領域。** 現場の現実の収集と仕分けをAIに任せた分析は、この手法が依って立つ「人間の視点」をその時点で失っている——何が出てきても、それはもうクロス分析ではありません。

このルールが存在する理由は、数字とともに [human-in-the-loop.md](human-in-the-loop.md) にあります。

## この手法が「ではない」もの

- 反AIではない。私たちはAIを大量に使う——人間の検証の下で、視点を増やす道具として。
- 分析の自動化テンプレートではない。人間の突き合わせ工程を抜いたら、それはもうクロス分析ではない。
- 完成品ではない。現場の実践とともに、このドキュメントも更新されていく。

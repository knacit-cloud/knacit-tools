# knacit-tools

[Knacit](https://knacit.com) が公開する、誰でも使える便利ツール集です。
Practical tools built and published by [Knacit](https://knacit.com), free for anyone to use.

## これは何か / What is this

- Knacit が企業伴走支援の中で培った知見をもとに作る、実用ツール集です。
  A collection of practical tools born from Knacit's hands-on business support work.
- 各ツールは `tools/` 配下に独立して置かれ、それぞれの README に使い方があります。
  Each tool lives independently under `tools/`, with usage instructions in its own README.
- 設計判断の記録は [docs/DECISIONS.md](docs/DECISIONS.md) にあります。
  Design decisions are recorded in [docs/DECISIONS.md](docs/DECISIONS.md) (Japanese).

## 中身 / What's inside

### 方法論 / Methods

| 方法論 / Method | 説明 / Description |
|---|---|
| [Cross-Analysis / クロス分析](methods/cross-analysis/README.md) | 客観データ×現場一次情報を突き合わせて真因を出す診断手法 / A diagnostic method that confronts objective data with field reality to surface root causes |
| [Human-in-the-Loop の3原則](methods/cross-analysis/human-in-the-loop.md) | 検証済み研究に基づく、AIと働くための3つの運用原則 / Three evidence-based principles for working with AI |
| [実在しなかった引用](methods/cross-analysis/the-fabricated-citation.md) | AIの捏造引用を発見した実話とチェックリスト / How we caught an AI-fabricated citation, and the checklist born from it |

### ツール / Tools

| ツール / Tool | 説明 / Description |
|---|---|
| （準備中 / Coming soon） | |

## 開発について / Development

このリポジトリは AI エージェント（Claude Code 等）との協働を前提に運用しています。エージェント向けルールは [AGENTS.md](AGENTS.md) を参照してください。
This repository is developed in collaboration with AI agents (Claude Code, etc.). See [AGENTS.md](AGENTS.md) for agent-facing rules.

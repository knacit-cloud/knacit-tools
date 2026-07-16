# 設計判断の記録

「なぜそう決めたか」を残す場所。新しい判断は上に追記する。

## 2026-07-16 — リポジトリの土台

- **AGENTS.md を本体、CLAUDE.md をシンボリックリンクにする。**
  理由: AGENTS.md は Linux Foundation（Agentic AI Foundation、Anthropic/OpenAI/Block 共同設立）管理の業界標準で、6万以上の公開リポジトリが採用。どの AI ツール（Claude Code / Cursor / Copilot 等）からも同じルールが読める。
- **AI 向け設定ファイルは公開する。**
  理由: 海外の主要 AI 企業（OpenAI 自身のリポジトリに88個の AGENTS.md）が公開しており、整理された設定はむしろ技術力のシグナルになる。ただし秘密情報は絶対に含めない。
- **`.claude/settings.json` はコミット、`settings.local.json` は gitignore。**
  理由: 共有設定と個人設定を分けるのが Claude Code の公式推奨パターン。local のコミットは最頻出ミスとされる。
- **ツールごとにネストした AGENTS.md を置く。**
  理由: 作業ディレクトリに応じて自動で文脈が切り替わり、`/clear` 後も引き継がれる。OpenAI のモノレポと同じ方式。
- **リポジトリ名は knacit-tools。**
  理由: 複数の便利ツールを継続的に置く前提。lab（実験場）より tools の方が用途が伝わる。

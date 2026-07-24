# crosstab

**Statistically honest cross-tabulation.** Give it two categorical variables and
it tells you not just the counts, but whether the association is *beyond chance*
(chi-square test), *how strong* it is (Cramér's V), and *which cells drive it*
(adjusted residuals) — with the test's own assumptions checked so you don't read
noise as signal.
統計的に誠実なクロス集計。2つのカテゴリ変数から、集計表だけでなく「その差は偶然を超えているか（カイ二乗検定）」「どれくらい強いか（Cramér's V）」「どのセルが効いているか（調整済み残差）」まで返し、検定の前提もチェックするので、偶然のばらつきを意味ある差と誤読しません。

## Why not just a pivot table? / なぜピボット表では足りないか
A pivot table shows "60% of men and 50% of women bought product A" and stops
there. If each group had only 10 people, that gap is just noise — but the table
looks the same. crosstab adds the layer that tells you which it is.
ピボット表は「男性の60%・女性の50%が商品Aを買った」を見せて終わりです。各群が10人なら、その差はただのノイズですが、表の見た目は同じです。crosstab は「どちらなのか」を教える層を足します。

## Install / インストール
```bash
pip install -e .
```
Requires Python 3.9+. Dependencies: `scipy`, `pandas`, `pydantic`.
Python 3.9 以上。依存: `scipy` / `pandas` / `pydantic`。

## Use as a CLI / コマンドラインで使う
JSON in (stdin or file), JSON out (stdout). / JSON を標準入力かファイルで渡し、JSON が返ります。
```bash
echo '{"mode":"table","row_labels":["male","female"],
       "col_labels":["bought","not"],"table":[[6,4],[5,5]]}' \
  | python -m crosstab --pretty
```

## Use as a library / ライブラリとして使う
```python
from crosstab import analyze

result = analyze({
    "mode": "records",
    "row_var": "region",
    "col_var": "ordered_by",
    "records": [
        {"region": "east", "ordered_by": "fax"},
        {"region": "west", "ordered_by": "web"},
        # ...
    ],
})
print(result["test"]["p_value"], result["effect_size"]["cramers_v"])
```

## Input / 入力
Two shapes, chosen by `mode`. / `mode` で2つの形から選びます。

**`mode: "records"`** — raw rows; crosstab builds the table. / 生データ。集計は自動。
| field | meaning |
|---|---|
| `row_var`, `col_var` | field names to cross-tabulate / クロスする列名 |
| `records` | list of objects / オブジェクトの配列 |
| `count_var` *(optional)* | field holding pre-aggregated counts / 集計済みの件数列 |

**`mode: "table"`** — a pre-built counts matrix. / 集計済みの件数行列。
| field | meaning |
|---|---|
| `row_labels`, `col_labels` | category names / カテゴリ名 |
| `table` | 2-D matrix of counts / 件数の2次元配列 |

**`options`** *(optional)* — `alpha` (default `0.05`), `drop_missing` (default `true`),
`yates_correction` (default `false`, 2×2 only).

### Dirty data is handled, not guessed / 汚いデータは補正、当て推量はしない
Numbers as strings (`"100"`), full-width digits (`"１００"`), full-width spaces,
`","` separators, empty / `null` / `NA` are normalized. Anything that cannot be
safely interpreted is **reported as a structured issue, never silently invented**.
文字列の数値・全角数字・全角スペース・桁区切り・空欄/`null`/`NA` は正規化します。安全に解釈できないものは**構造化されたエラーとして報告し、勝手に値を作りません**。

## Output / 出力
Always the same shape (see `schema_version`). Key fields:
常に同じ形（`schema_version` 参照）。主なフィールド:

| field | meaning / 意味 |
|---|---|
| `test` | `statistic`, `dof`, `p_value`, `significant` / カイ二乗・自由度・p値・有意か |
| `effect_size` | `cramers_v` and an interpretation (`negligible`…`large`) / 効果量と解釈 |
| `adjusted_residuals` | per-cell standardized residuals / セル別の調整済み残差 |
| `significant_cells` | cells past the threshold, with `direction` (over/under) / 閾値超えのセルと方向 |
| `assumptions` | expected-count check; `rule_of_thumb_ok` / 期待度数チェック |
| `warnings` | plain-language cautions (small N, assumption violations) / 平易な注意 |
| `data_quality_issues` | what was normalized or dropped / 正規化・除外した内容 |
| `human_review` | reminder that this is a signal, not a conclusion / 結論ではなく示唆である旨 |

On failure: `{"ok": false, "errors": [{where, problem, action}]}` — never an
exception, never a wrong-but-confident number.
失敗時: `{"ok": false, "errors": [...]}` を返します。例外で落ちたり、誤った値を自信ありげに返すことはありません。

## A deliberate limit / 意図した制約
crosstab reports statistics; it does **not** decide what they mean. A significant
p-value says "unlikely to be pure chance" — not "important" and not "causal."
Interpretation is left to a human, on purpose.
crosstab は統計を報告しますが、その**意味は決めません**。有意なp値は「偶然とは考えにくい」であって「重要」でも「因果」でもありません。解釈は意図的に人間に委ねています。

## Test / テスト
```bash
pip install -e ".[dev]"
python -m pytest
```

## Scope / 範囲
In scope: one 2-D contingency table, chi-square, adjusted residuals, Cramér's V.
Out of scope (for now): Fisher's exact fallback for sparse 2×2, three-way /
stratified tables (Cochran–Mantel–Haenszel).
対象: 1枚の2次元分割表・カイ二乗・調整済み残差・Cramér's V。範囲外（現状）: 疎な2×2でのFisher正確確率検定への切替、3変数以上・層別（CMH）。

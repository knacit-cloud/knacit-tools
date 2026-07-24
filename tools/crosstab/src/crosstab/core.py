"""Orchestration: validate -> tabulate -> analyze -> contract-shaped output.

Every path returns the same output shape (requirement 3). Nothing here raises to
the caller: bad input becomes ``{"ok": false, "errors": [...]}``.

The output always carries a ``human_review`` block. That is deliberate: the
computation is safe to automate, but *interpretation* — is this the real
bottleneck? is it causal? — stays with a human. The tool reports a statistical
signal; it never declares a conclusion.
"""

from __future__ import annotations

from typing import Any, Dict, List

import pandas as pd
from pydantic import ValidationError

from .schema import SCHEMA_VERSION, AnalyzeInput
from .stats import analyze_table
from .validate import Issue, clean_records, clean_table

_HUMAN_REVIEW = {
    "note": (
        "This is a statistical signal, not a conclusion. A significant p-value "
        "means 'unlikely to be pure chance', not 'important' and not 'causal'. "
        "Read it together with the effect size and the field context, and let a "
        "human decide what it means."
    ),
    "note_ja": (
        "これは統計的な示唆であり、結論ではありません。有意なp値は「偶然とは考えにくい」"
        "という意味であって、「重要」でも「因果関係がある」でもありません。効果量と現場の"
        "文脈を併せて読み、意味の判断は人間が行ってください。"
    ),
}


def _err(errors: List[dict]) -> Dict[str, Any]:
    return {"ok": False, "schema_version": SCHEMA_VERSION, "errors": errors}


def analyze(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Main entry point. Takes a plain dict (parsed JSON), returns a plain dict."""
    # 1. Contract check.
    try:
        inp = AnalyzeInput.model_validate(payload)
    except ValidationError as e:
        return _err(
            [
                {
                    "where": ".".join(str(x) for x in err["loc"]),
                    "problem": err["msg"],
                    "action": "rejected input",
                }
                for err in e.errors()
            ]
        )

    # 2. Validate/normalize + build the contingency table.
    if inp.mode == "records":
        clean, issues = clean_records(
            inp.records, inp.row_var, inp.col_var, inp.count_var, inp.options.drop_missing
        )
        if not clean:
            return _err(
                (list(issues) or [])
                + [Issue("records", "no usable rows after cleaning", "cannot analyze")]
            )
        df = pd.DataFrame(clean)
        if inp.count_var is not None:
            ct = pd.crosstab(
                df[inp.row_var],
                df[inp.col_var],
                values=df[inp.count_var],
                aggfunc="sum",
            ).fillna(0)
        else:
            ct = pd.crosstab(df[inp.row_var], df[inp.col_var])
        row_labels = [str(x) for x in ct.index.tolist()]
        col_labels = [str(x) for x in ct.columns.tolist()]
        matrix = ct.to_numpy().tolist()
        n_input = len(inp.records)
        n_used = len(clean)
    else:  # table
        matrix, issues = clean_table(inp.table, inp.row_labels, inp.col_labels)
        if matrix is None:
            return _err(list(issues))
        row_labels = [str(x) for x in inp.row_labels]
        col_labels = [str(x) for x in inp.col_labels]
        n_input = n_used = int(sum(sum(r) for r in matrix))

    # 3. Statistics.
    result = analyze_table(
        matrix,
        row_labels,
        col_labels,
        alpha=inp.options.alpha,
        yates_correction=inp.options.yates_correction,
    )
    if result is None:
        return _err(
            list(issues)
            + [
                Issue(
                    "table",
                    "table must be at least 2x2 with no empty row/column totals",
                    "cannot analyze",
                )
            ]
        )

    # 4. Assemble the contract-shaped output.
    return {
        "ok": True,
        "schema_version": SCHEMA_VERSION,
        "input_summary": {
            "mode": inp.mode,
            "rows_in": n_input,
            "rows_used": n_used,
            "rows_dropped": n_input - n_used if inp.mode == "records" else 0,
            "table_shape": [len(row_labels), len(col_labels)],
        },
        "contingency_table": {
            "row_var": inp.row_var,
            "col_var": inp.col_var,
            "row_labels": row_labels,
            "col_labels": col_labels,
            "observed": result.observed,
            "expected": result.expected,
        },
        "test": {
            "method": result.method,
            "statistic": result.chi2,
            "dof": result.dof,
            "p_value": result.p_value,
            "alpha": inp.options.alpha,
            "significant": bool(result.p_value < inp.options.alpha),
        },
        "effect_size": {
            "cramers_v": result.cramers_v,
            "interpretation": result.effect_interpretation,
        },
        "adjusted_residuals": result.adjusted_residuals,
        "significant_cells": result.significant_cells,
        "assumptions": result.assumptions,
        "warnings": result.warnings,
        "data_quality_issues": list(issues),
        "human_review": _HUMAN_REVIEW,
    }

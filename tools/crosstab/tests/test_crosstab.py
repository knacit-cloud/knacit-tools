"""Tests for the crosstab engine.

Correctness is checked against hand-computable cases (chi-square and adjusted
residuals have closed forms for the tables used here), plus the dirty-data and
error paths that a customer-facing tool must survive.
"""

import math

from crosstab import analyze


# --- statistical correctness -------------------------------------------------

def test_strong_association_known_values():
    # [[40,10],[10,40]], N=100, all expected=25.
    # chi2 = 4 * (15^2/25) = 36 ; Cramer's V = sqrt(36/100) = 0.6 (large).
    # 2x2 adjusted residual magnitude = sqrt(chi2) = 6 in every cell.
    res = analyze(
        {
            "mode": "table",
            "row_labels": ["a", "b"],
            "col_labels": ["x", "y"],
            "table": [[40, 10], [10, 40]],
        }
    )
    assert res["ok"] is True
    assert res["test"]["method"] == "pearson_chi2"
    assert math.isclose(res["test"]["statistic"], 36.0, rel_tol=1e-6)
    assert res["test"]["dof"] == 1
    assert res["test"]["significant"] is True
    assert math.isclose(res["effect_size"]["cramers_v"], 0.6, rel_tol=1e-3)
    assert res["effect_size"]["interpretation"] == "large"
    # 2x2 property: |adjusted residual| == sqrt(chi2) in every cell.
    for row in res["adjusted_residuals"]:
        for v in row:
            assert math.isclose(abs(v), 6.0, rel_tol=1e-3)
    assert len(res["significant_cells"]) == 4


def test_noise_is_reported_as_not_significant():
    # The user's own example: 60% (6/10) vs 50% (5/10) — must NOT be significant.
    res = analyze(
        {
            "mode": "table",
            "row_labels": ["male", "female"],
            "col_labels": ["bought", "not"],
            "table": [[6, 4], [5, 5]],
        }
    )
    assert res["ok"] is True
    assert res["test"]["significant"] is False
    assert res["test"]["p_value"] > 0.05
    assert res["significant_cells"] == []
    # Sparse expected counts here -> the assumption warning must fire.
    assert res["assumptions"]["rule_of_thumb_ok"] is False
    assert any("assumption" in w.lower() for w in res["warnings"])


def test_human_review_always_present():
    res = analyze(
        {"mode": "table", "row_labels": ["a", "b"], "col_labels": ["x", "y"],
         "table": [[10, 10], [10, 10]]}
    )
    assert "human_review" in res
    assert "note" in res["human_review"] and "note_ja" in res["human_review"]


# --- dirty data (requirement 1) ----------------------------------------------

def test_records_normalizes_fullwidth_and_drops_missing():
    res = analyze(
        {
            "mode": "records",
            "row_var": "pref",
            "col_var": "buy",
            "records": [
                {"pref": "山口　", "buy": "yes"},  # full-width space -> "山口"
                {"pref": "山口", "buy": "no"},
                {"pref": "広島", "buy": "yes"},
                {"pref": "広島", "buy": ""},            # missing -> dropped
                {"pref": "　", "buy": "yes"},        # missing pref -> dropped
            ],
        }
    )
    assert res["ok"] is True
    assert res["input_summary"]["rows_used"] == 3
    assert res["input_summary"]["rows_dropped"] == 2
    # full-width-space variant merged into "山口"
    assert set(res["contingency_table"]["row_labels"]) == {"山口", "広島"}
    assert len(res["data_quality_issues"]) == 2


def test_records_with_string_and_fullwidth_counts():
    # Pre-aggregated counts arriving as dirty strings must coerce, not crash.
    res = analyze(
        {
            "mode": "records",
            "row_var": "region",
            "col_var": "channel",
            "count_var": "n",
            "records": [
                {"region": "east", "channel": "fax", "n": "40"},     # str
                {"region": "east", "channel": "web", "n": "１０"},    # full-width
                {"region": "west", "channel": "fax", "n": 10},        # int
                {"region": "west", "channel": "web", "n": 40.0},      # float
            ],
        }
    )
    assert res["ok"] is True
    assert res["input_summary"]["table_shape"] == [2, 2]
    assert math.isclose(res["test"]["statistic"], 36.0, rel_tol=1e-6)


def test_bad_count_is_reported_not_crashed():
    res = analyze(
        {
            "mode": "table",
            "row_labels": ["a", "b"],
            "col_labels": ["x", "y"],
            "table": [[10, "abc"], [10, 40]],
        }
    )
    assert res["ok"] is False
    assert any("not a number" in e["problem"] for e in res["errors"])


# --- contract / error paths (requirement 3) ----------------------------------

def test_schema_rejects_missing_fields():
    res = analyze({"mode": "records", "row_var": "a"})  # missing col_var, records
    assert res["ok"] is False
    assert res["errors"]


def test_smaller_than_2x2_rejected():
    res = analyze(
        {"mode": "table", "row_labels": ["only"], "col_labels": ["x", "y"],
         "table": [[3, 4]]}
    )
    assert res["ok"] is False


def test_zero_marginal_rejected():
    res = analyze(
        {"mode": "table", "row_labels": ["a", "b"], "col_labels": ["x", "y"],
         "table": [[0, 0], [5, 5]]}
    )
    assert res["ok"] is False

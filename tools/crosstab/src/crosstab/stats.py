"""The statistical core.

Requirement 2 (statistical evaluation): a cross-tab alone lets users misread
noise as signal. This module answers three separate questions a pivot table
cannot:

  1. Is the association beyond chance?      -> chi-square test, p-value
  2. If so, how strong is it?               -> Cramer's V (effect size)
  3. Which cells drive it, and which way?   -> adjusted (standardized) residuals

It also checks the test's own assumptions (expected-count rule) so a small-N
result is not presented as if it were solid.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional

import numpy as np
from scipy import stats


@dataclass
class StatsResult:
    row_labels: List[str]
    col_labels: List[str]
    observed: List[List[int]]
    expected: List[List[float]]
    chi2: float
    dof: int
    p_value: float
    method: str
    cramers_v: float
    effect_interpretation: str
    adjusted_residuals: List[List[float]]
    significant_cells: List[dict]
    assumptions: dict
    warnings: List[str] = field(default_factory=list)


def _cramers_v_interpretation(v: float, df_min: int) -> str:
    """Cohen-style thresholds for Cramer's V, which depend on the smaller table
    dimension. Thresholds below are for df_min=1; they loosen as df_min grows."""
    # Cohen's small/medium/large for w, scaled by 1/sqrt(df_min).
    small, medium, large = (
        0.10 / np.sqrt(df_min),
        0.30 / np.sqrt(df_min),
        0.50 / np.sqrt(df_min),
    )
    if v < small:
        return "negligible"
    if v < medium:
        return "small"
    if v < large:
        return "medium"
    return "large"


def analyze_table(
    observed: List[List[int]],
    row_labels: List[str],
    col_labels: List[str],
    alpha: float = 0.05,
    yates_correction: bool = False,
) -> Optional[StatsResult]:
    """Run the full analysis on a validated counts matrix.

    Returns None only for structurally impossible tables (empty row/col totals,
    or smaller than 2x2); the caller turns that into a structured error.
    """
    O = np.asarray(observed, dtype=float)
    r, c = O.shape

    if r < 2 or c < 2:
        return None
    n = O.sum()
    if n <= 0 or (O.sum(axis=1) == 0).any() or (O.sum(axis=0) == 0).any():
        return None  # a zero marginal makes the test undefined

    is_2x2 = r == 2 and c == 2
    correction = yates_correction and is_2x2
    chi2, p, dof, expected = stats.chi2_contingency(O, correction=correction)
    method = (
        "pearson_chi2_yates" if correction else "pearson_chi2"
    )

    # Adjusted (standardized) residuals — Haberman.
    row_sums = O.sum(axis=1, keepdims=True)
    col_sums = O.sum(axis=0, keepdims=True)
    denom = np.sqrt(expected * (1 - row_sums / n) * (1 - col_sums / n))
    with np.errstate(divide="ignore", invalid="ignore"):
        adj = np.where(denom > 0, (O - expected) / denom, 0.0)

    # Effect size.
    df_min = min(r, c) - 1
    cramers_v = float(np.sqrt(chi2 / (n * df_min))) if df_min > 0 else 0.0
    effect = _cramers_v_interpretation(cramers_v, df_min)

    # Which cells are significant, and in which direction.
    z_crit = float(stats.norm.ppf(1 - alpha / 2))
    significant = []
    for i in range(r):
        for j in range(c):
            z = float(adj[i, j])
            if abs(z) >= z_crit:
                significant.append(
                    {
                        "row": row_labels[i],
                        "col": col_labels[j],
                        "observed": int(O[i, j]),
                        "expected": round(float(expected[i, j]), 2),
                        "adjusted_residual": round(z, 3),
                        "direction": "over" if z > 0 else "under",
                    }
                )

    # Assumption check: the expected-count rule of thumb.
    n_cells = r * c
    below_5 = int((expected < 5).sum())
    below_1 = int((expected < 1).sum())
    min_expected = float(expected.min())
    assumptions = {
        "min_expected_count": round(min_expected, 3),
        "cells_below_5": below_5,
        "pct_cells_below_5": round(100.0 * below_5 / n_cells, 1),
        "cells_below_1": below_1,
        "rule_of_thumb_ok": below_1 == 0 and (below_5 / n_cells) <= 0.20,
        "n_total": int(n),
    }

    warnings: List[str] = []
    if not assumptions["rule_of_thumb_ok"]:
        warnings.append(
            "Expected-count assumption violated (>20% of cells have expected<5 "
            "or some cell <1). The chi-square p-value is unreliable here; for a "
            "2x2 table use Fisher's exact test, otherwise collect more data or "
            "merge sparse categories."
        )
    if n < 5 * n_cells:
        warnings.append(
            f"Small sample (N={int(n)}) relative to a {r}x{c} table. Treat the "
            "result as tentative; a non-significant p may just mean too little data."
        )

    return StatsResult(
        row_labels=row_labels,
        col_labels=col_labels,
        observed=[[int(v) for v in row] for row in O],
        expected=[[round(float(v), 3) for v in row] for row in expected],
        chi2=round(float(chi2), 4),
        dof=int(dof),
        p_value=float(p),
        method=method,
        cramers_v=round(cramers_v, 4),
        effect_interpretation=effect,
        adjusted_residuals=[[round(float(v), 3) for v in row] for row in adj],
        significant_cells=significant,
        assumptions=assumptions,
        warnings=warnings,
    )

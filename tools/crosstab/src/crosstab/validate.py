"""Input normalization and defensive validation.

Requirement 1 (data quality): real users send dirty data — numbers as strings
("100"), empty strings, null, full-width spaces/digits ("１００"、"山口　"),
stray whitespace. This layer normalizes what is safely normalizable and reports
(never silently guesses) what is not. A bad value produces a structured issue,
not a crash and not a wrong-but-confident number.
"""

from __future__ import annotations

import unicodedata
from typing import Any, List, Optional, Tuple

# Tokens that mean "missing", compared case-insensitively after stripping.
_MISSING_TOKENS = {"", "null", "none", "na", "n/a", "nan", "-", "—", "未回答", "不明"}


class Issue(dict):
    """A structured, JSON-serializable data-quality note."""

    def __init__(self, where: str, problem: str, action: str) -> None:
        super().__init__(where=where, problem=problem, action=action)


def normalize_category(value: Any) -> Optional[str]:
    """Normalize a category label. Returns None if the value reads as missing.

    - None stays None.
    - Everything is NFKC-normalized (full-width -> half-width, etc.) so "山口　"
      and "山口" or "Ａ" and "A" collapse to one category.
    - Leading/trailing whitespace (incl. full-width space) is stripped and
      internal runs collapsed to a single space.
    - Recognized missing tokens become None.
    """
    if value is None:
        return None
    s = value if isinstance(value, str) else str(value)
    # NFKC folds full-width chars (spaces, digits, letters) to canonical forms.
    s = unicodedata.normalize("NFKC", s)
    s = " ".join(s.split())  # strip + collapse all whitespace runs
    if s.casefold() in _MISSING_TOKENS:
        return None
    return s


def normalize_count(value: Any) -> Tuple[Optional[int], Optional[str]]:
    """Coerce a count to a non-negative int.

    Returns (value, error). Exactly one is non-None. Accepts ints, floats with
    integer value, and numeric strings incl. full-width digits and thousands
    separators ("1,000"). Rejects (does not guess) anything else.
    """
    if value is None:
        return None, "value is null"
    if isinstance(value, bool):  # bool is an int subclass; reject to avoid surprises
        return None, "boolean is not a valid count"
    if isinstance(value, int):
        return (value, None) if value >= 0 else (None, "count is negative")
    if isinstance(value, float):
        if value != value:  # NaN
            return None, "value is NaN"
        if value.is_integer():
            return (int(value), None) if value >= 0 else (None, "count is negative")
        return None, f"non-integer count: {value}"
    if isinstance(value, str):
        s = unicodedata.normalize("NFKC", value).strip().replace(",", "")
        if s.casefold() in _MISSING_TOKENS:
            return None, "value is empty/missing"
        try:
            f = float(s)
        except ValueError:
            return None, f"not a number: {value!r}"
        if f != f:
            return None, "value is NaN"
        if not f.is_integer():
            return None, f"non-integer count: {value!r}"
        return (int(f), None) if f >= 0 else (None, "count is negative")
    return None, f"unsupported type: {type(value).__name__}"


def clean_records(
    records: List[dict],
    row_var: str,
    col_var: str,
    count_var: Optional[str],
    drop_missing: bool,
) -> Tuple[List[dict], List[Issue]]:
    """Return (clean_records, issues). Clean records have normalized row/col
    (and count) values ready for tabulation."""
    issues: List[Issue] = []
    clean: List[dict] = []

    for i, rec in enumerate(records):
        if not isinstance(rec, dict):
            issues.append(Issue(f"records[{i}]", "not an object", "dropped row"))
            continue

        row = normalize_category(rec.get(row_var))
        col = normalize_category(rec.get(col_var))

        if row is None or col is None:
            if drop_missing:
                which = ", ".join(
                    n for n, v in ((row_var, row), (col_var, col)) if v is None
                )
                issues.append(
                    Issue(f"records[{i}]", f"missing {which}", "dropped row")
                )
                continue
            row = row if row is not None else "(unknown)"
            col = col if col is not None else "(unknown)"

        out = {row_var: row, col_var: col}

        if count_var is not None:
            n, err = normalize_count(rec.get(count_var))
            if err is not None:
                issues.append(
                    Issue(f"records[{i}].{count_var}", err, "dropped row")
                )
                continue
            out[count_var] = n

        clean.append(out)

    return clean, issues


def clean_table(
    table: List[List[Any]],
    row_labels: List[str],
    col_labels: List[str],
) -> Tuple[Optional[List[List[int]]], List[Issue]]:
    """Validate a pre-built counts matrix. Returns (matrix, issues); matrix is
    None if the shape is unusable (issues explain why)."""
    issues: List[Issue] = []

    n_rows, n_cols = len(row_labels), len(col_labels)
    if len(table) != n_rows:
        issues.append(
            Issue(
                "table",
                f"row count {len(table)} != len(row_labels) {n_rows}",
                "cannot analyze",
            )
        )
        return None, issues

    matrix: List[List[int]] = []
    fatal = False
    for i, row in enumerate(table):
        if not isinstance(row, list) or len(row) != n_cols:
            issues.append(
                Issue(
                    f"table[{i}]",
                    f"expected {n_cols} values, got "
                    f"{len(row) if isinstance(row, list) else type(row).__name__}",
                    "cannot analyze",
                )
            )
            fatal = True
            continue
        clean_row: List[int] = []
        for j, cell in enumerate(row):
            n, err = normalize_count(cell)
            if err is not None:
                issues.append(
                    Issue(f"table[{i}][{j}]", err, "cannot analyze")
                )
                fatal = True
                clean_row.append(0)
            else:
                clean_row.append(n)
        matrix.append(clean_row)

    if fatal:
        return None, issues
    return matrix, issues

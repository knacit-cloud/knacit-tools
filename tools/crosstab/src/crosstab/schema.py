"""Input/output contract for the crosstab engine.

Requirement 3 (schema unification): a strict, versioned contract so that a UI,
another service, or an LLM can rely on "give this shape, always get that shape
back." Parsing failures never crash — they surface as a structured error result
(see ``core.analyze``).
"""

from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator

SCHEMA_VERSION = "1.0"


class Options(BaseModel):
    """Analysis knobs. All optional; defaults are the safe, common choices."""

    model_config = ConfigDict(extra="forbid")

    alpha: float = Field(
        0.05, gt=0, lt=1, description="Significance level for cell/test flags."
    )
    drop_missing: bool = Field(
        True,
        description="Drop records whose row/col value is missing. If False, a "
        "missing value becomes an explicit 'unknown' category instead.",
    )
    yates_correction: bool = Field(
        False,
        description="Apply Yates' continuity correction (only affects 2x2 tables).",
    )


class AnalyzeInput(BaseModel):
    """Two entry shapes, selected by ``mode``.

    mode="records": raw rows; the engine builds the contingency table itself.
    mode="table":   a pre-built counts matrix with explicit labels.
    """

    model_config = ConfigDict(extra="forbid")

    mode: Literal["records", "table"]

    # --- mode="records" ---
    row_var: Optional[str] = None
    col_var: Optional[str] = None
    count_var: Optional[str] = Field(
        None,
        description="Optional: a field holding pre-aggregated counts. If omitted, "
        "each record counts as 1.",
    )
    records: Optional[List[Dict[str, Any]]] = None

    # --- mode="table" ---
    row_labels: Optional[List[str]] = None
    col_labels: Optional[List[str]] = None
    table: Optional[List[List[Any]]] = None

    options: Options = Field(default_factory=Options)

    @model_validator(mode="after")
    def _check_mode_fields(self) -> "AnalyzeInput":
        if self.mode == "records":
            missing = [
                name
                for name, val in (
                    ("row_var", self.row_var),
                    ("col_var", self.col_var),
                    ("records", self.records),
                )
                if val is None
            ]
            if missing:
                raise ValueError(
                    f"mode='records' requires: {', '.join(missing)}"
                )
        else:  # table
            missing = [
                name
                for name, val in (
                    ("row_labels", self.row_labels),
                    ("col_labels", self.col_labels),
                    ("table", self.table),
                )
                if val is None
            ]
            if missing:
                raise ValueError(f"mode='table' requires: {', '.join(missing)}")
        return self

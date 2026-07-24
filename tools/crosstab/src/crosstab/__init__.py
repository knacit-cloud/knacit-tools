"""crosstab — statistically honest cross-tabulation.

Public API:
    from crosstab import analyze
    result = analyze({"mode": "table", ...})
"""

from .core import analyze
from .schema import SCHEMA_VERSION

__all__ = ["analyze", "SCHEMA_VERSION"]
__version__ = "0.1.0"

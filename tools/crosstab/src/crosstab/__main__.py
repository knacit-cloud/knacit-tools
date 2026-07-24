"""CLI: JSON in (stdin or file) -> JSON out (stdout).

    echo '{"mode":"table","row_labels":["m","f"],"col_labels":["yes","no"],
           "table":[[6,4],[5,5]]}' | python -m crosstab

    python -m crosstab input.json --pretty

Exit code is 0 when analysis succeeds, 1 when the result is an error object, so
the tool composes cleanly in shell pipelines.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Dict

from .core import analyze


def _read_payload(path: str | None) -> Dict[str, Any]:
    raw = sys.stdin.read() if path in (None, "-") else open(path, encoding="utf-8").read()
    return json.loads(raw)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="crosstab",
        description="Chi-square + adjusted residuals + effect size on a cross-tab.",
    )
    parser.add_argument(
        "input",
        nargs="?",
        default="-",
        help="Path to a JSON input file, or '-' / omitted for stdin.",
    )
    parser.add_argument("--pretty", action="store_true", help="Indent the JSON output.")
    args = parser.parse_args(argv)

    try:
        payload = _read_payload(args.input)
    except (OSError, json.JSONDecodeError) as e:
        json.dump(
            {"ok": False, "errors": [{"where": "input", "problem": str(e), "action": "rejected input"}]},
            sys.stdout,
        )
        sys.stdout.write("\n")
        return 1

    result = analyze(payload)
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2 if args.pretty else None)
    sys.stdout.write("\n")
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())

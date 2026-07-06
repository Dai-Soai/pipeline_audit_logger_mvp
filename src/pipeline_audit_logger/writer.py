from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from pipeline_audit_logger.contract import AuditEvent


def append_audit_event(
    event: AuditEvent,
    output_path: str | Path,
) -> Path:
    output = Path(output_path)

    output.parent.mkdir(parents=True, exist_ok=True)

    with output.open("a", encoding="utf-8") as f:
        json.dump(asdict(event), f)
        f.write("\n")

    return output

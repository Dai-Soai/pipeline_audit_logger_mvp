from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_artifact(path: str | Path) -> dict[str, Any]:
    artifact_path = Path(path)

    if not artifact_path.exists():
        raise FileNotFoundError(f"Artifact file not found: {artifact_path}")

    if not artifact_path.is_file():
        raise ValueError(f"Artifact path is not a file: {artifact_path}")

    try:
        payload = json.loads(artifact_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON artifact: {artifact_path}") from exc

    if not isinstance(payload, dict):
        raise ValueError("Artifact JSON must be an object")

    return payload

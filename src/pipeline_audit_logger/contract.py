from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any


@dataclass(frozen=True)
class AuditEvent:
    event_id: str
    artifact_type: str
    source_path: str
    action: str
    status: str
    message: str
    created_at: str


def build_audit_event(
    *,
    event_id: str,
    artifact: dict[str, Any],
    source_path: str,
    action: str = "artifact_logged",
    status: str = "RECORDED",
    message: str = "Artifact recorded in audit log.",
) -> AuditEvent:
    if not isinstance(artifact, dict):
        raise ValueError("artifact must be a JSON object")

    artifact_type = artifact.get("artifact_type")
    if not artifact_type:
        raise ValueError("artifact_type is required")

    return AuditEvent(
        event_id=event_id,
        artifact_type=str(artifact_type),
        source_path=source_path,
        action=action,
        status=status,
        message=message,
        created_at=datetime.now(timezone.utc).isoformat(),
    )

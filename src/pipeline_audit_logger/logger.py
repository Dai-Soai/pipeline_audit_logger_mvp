from __future__ import annotations

from typing import Any
from uuid import uuid4

from pipeline_audit_logger.contract import AuditEvent, build_audit_event


def create_audit_event(
    *,
    artifact: dict[str, Any],
    source_path: str,
    action: str = "artifact_logged",
) -> AuditEvent:
    return build_audit_event(
        event_id=f"audit-{uuid4()}",
        artifact=artifact,
        source_path=source_path,
        action=action,
        status="RECORDED",
        message="Artifact recorded in audit log.",
    )

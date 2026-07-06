import pytest

from pipeline_audit_logger.contract import build_audit_event


def test_build_audit_event_success():
    artifact = {
        "artifact_type": "delivery_report",
        "summary": {
            "total": 2,
            "delivered": 2,
            "failed": 0,
        },
    }

    event = build_audit_event(
        event_id="audit-001",
        artifact=artifact,
        source_path="reports/delivery_report.json",
    )

    assert event.event_id == "audit-001"
    assert event.artifact_type == "delivery_report"
    assert event.source_path == "reports/delivery_report.json"
    assert event.action == "artifact_logged"
    assert event.status == "RECORDED"
    assert event.created_at


def test_build_audit_event_rejects_non_object_artifact():
    with pytest.raises(ValueError, match="artifact"):
        build_audit_event(
            event_id="audit-001",
            artifact=[],
            source_path="bad.json",
        )


def test_build_audit_event_rejects_missing_artifact_type():
    with pytest.raises(ValueError, match="artifact_type"):
        build_audit_event(
            event_id="audit-001",
            artifact={},
            source_path="missing.json",
        )

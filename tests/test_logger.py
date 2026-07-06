from pipeline_audit_logger.logger import create_audit_event


def test_create_audit_event_success():
    artifact = {
        "artifact_type": "delivery_report",
        "summary": {
            "total": 2,
            "delivered": 2,
            "failed": 0,
        },
    }

    event = create_audit_event(
        artifact=artifact,
        source_path="reports/delivery_report.json",
    )

    assert event.event_id.startswith("audit-")
    assert event.artifact_type == "delivery_report"
    assert event.source_path == "reports/delivery_report.json"
    assert event.action == "artifact_logged"
    assert event.status == "RECORDED"
    assert event.message == "Artifact recorded in audit log."

import json

from pipeline_audit_logger.contract import build_audit_event
from pipeline_audit_logger.writer import append_audit_event


def test_append_audit_event(tmp_path):
    artifact = {
        "artifact_type": "delivery_report",
    }

    event = build_audit_event(
        event_id="audit-001",
        artifact=artifact,
        source_path="reports/delivery_report.json",
    )

    log_path = tmp_path / "audit_log.jsonl"

    append_audit_event(event, log_path)

    lines = log_path.read_text(encoding="utf-8").splitlines()

    assert len(lines) == 1

    payload = json.loads(lines[0])

    assert payload["event_id"] == "audit-001"
    assert payload["artifact_type"] == "delivery_report"

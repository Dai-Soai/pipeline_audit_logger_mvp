import json

import pytest

from pipeline_audit_logger.loader import load_artifact


def test_load_artifact_success(tmp_path):
    path = tmp_path / "delivery_report.json"

    path.write_text(
        json.dumps(
            {
                "artifact_type": "delivery_report",
                "summary": {
                    "total": 2,
                    "delivered": 2,
                    "failed": 0,
                },
            }
        ),
        encoding="utf-8",
    )

    artifact = load_artifact(path)

    assert artifact["artifact_type"] == "delivery_report"
    assert artifact["summary"]["total"] == 2


def test_load_artifact_rejects_missing_file(tmp_path):
    path = tmp_path / "missing.json"

    with pytest.raises(FileNotFoundError):
        load_artifact(path)


def test_load_artifact_rejects_invalid_json(tmp_path):
    path = tmp_path / "bad.json"
    path.write_text("{bad json", encoding="utf-8")

    with pytest.raises(ValueError, match="Invalid JSON"):
        load_artifact(path)


def test_load_artifact_rejects_non_object_json(tmp_path):
    path = tmp_path / "array.json"
    path.write_text("[]", encoding="utf-8")

    with pytest.raises(ValueError, match="object"):
        load_artifact(path)

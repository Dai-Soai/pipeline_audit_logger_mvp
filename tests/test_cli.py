import json

from pipeline_audit_logger.cli import main


def test_cli_appends_audit_event(tmp_path, monkeypatch):
    input_path = tmp_path / "delivery_report.json"
    output_path = tmp_path / "audit_log.jsonl"

    input_path.write_text(
        json.dumps(
            {
                "artifact_type": "delivery_report",
                "version": "0.1.0",
                "summary": {
                    "total": 2,
                    "delivered": 2,
                    "failed": 0,
                },
            }
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "pipeline-audit-logger",
            str(input_path),
            "-o",
            str(output_path),
        ],
    )

    main()

    lines = output_path.read_text(encoding="utf-8").splitlines()

    assert len(lines) == 1

    payload = json.loads(lines[0])

    assert payload["artifact_type"] == "delivery_report"
    assert payload["source_path"] == str(input_path)
    assert payload["status"] == "RECORDED"

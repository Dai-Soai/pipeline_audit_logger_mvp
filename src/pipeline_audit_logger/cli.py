from __future__ import annotations

import argparse
from pathlib import Path

from pipeline_audit_logger.loader import load_artifact
from pipeline_audit_logger.logger import create_audit_event
from pipeline_audit_logger.writer import append_audit_event


def main() -> None:
    parser = argparse.ArgumentParser(description="Pipeline Audit Logger MVP")

    parser.add_argument(
        "input",
        help="Path to pipeline artifact JSON",
    )

    parser.add_argument(
        "-o",
        "--output",
        default="logs/audit_log.jsonl",
        help="Path to audit log JSONL",
    )

    parser.add_argument(
        "--action",
        default="artifact_logged",
        help="Audit action name",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Build audit event but do not write to log file",
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        raise SystemExit(f"Input file not found: {input_path}")

    artifact = load_artifact(input_path)

    event = create_audit_event(
        artifact=artifact,
        source_path=str(input_path),
        action=args.action,
    )

    if args.dry_run:
        print(f"Audit event built for {input_path}")
        return

    written_path = append_audit_event(
        event=event,
        output_path=output_path,
    )

    print(f"Audit event appended to {written_path}")

from __future__ import annotations

import argparse

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

    args = parser.parse_args()

    artifact = load_artifact(args.input)

    event = create_audit_event(
        artifact=artifact,
        source_path=args.input,
    )

    output_path = append_audit_event(
        event=event,
        output_path=args.output,
    )

    print(f"Audit event appended to {output_path}")


if __name__ == "__main__":
    main()

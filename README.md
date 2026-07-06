# Pipeline Audit Logger MVP

RADAR Service Utility #22

Version: v0.1.0

## Overview

Pipeline Audit Logger reads pipeline artifact JSON files and appends audit events into a JSONL audit log.

This utility creates an audit trail for RADAR_SERVICE pipeline artifacts.

## Artifact Flow

```text
pipeline artifact JSON
        │
        ▼
load_artifact()
        │
        ▼
create_audit_event()
        │
        ▼
append_audit_event()
        │
        ▼
audit_log.jsonl
```

## Input Artifacts

Supported input artifacts include:

- delivery_report.json
- notification_report.json
- execution_report.json
- schedule.json
- retry_plan.json
- monitor_report.json
- Output Artifact
- logs/audit_log.jsonl

Each line is one audit event JSON object.

## Module Responsibilities

contract.py

Defines AuditEvent and builds validated audit events.

loader.py

Loads and validates pipeline artifact JSON files.

logger.py

Creates audit events from loaded artifacts.

writer.py

Appends audit events to JSONL log files.

cli.py

Provides command-line execution.

## Project Structure

src/pipeline_audit_logger/
    contract.py
    loader.py
    logger.py
    writer.py
    cli.py

tests/
samples/
logs/

## Installation

python -m venv .venv
source .venv/bin/activate

pip install -e .

## CLI Usage

Default output:

pipeline-audit-logger samples/delivery_report.json

Custom output:

pipeline-audit-logger \
    samples/delivery_report.json \
    -o logs/audit_log.jsonl

Custom action:

pipeline-audit-logger \
    samples/delivery_report.json \
    --action artifact_audited

Dry run:

pipeline-audit-logger \
    samples/delivery_report.json \
    --dry-run
Output Example
{"event_id":"audit-...","artifact_type":"delivery_report","source_path":"samples/delivery_report.json","action":"artifact_logged","status":"RECORDED","message":"Artifact recorded in audit log.","created_at":"..."}

## Testing

pytest

Current status:

11 passed

## Responsibility

- Load pipeline artifact JSON
- Validate artifact input
- Create audit event
- Append audit event to JSONL
- Provide CLI execution

## Not Responsibility

- Database storage
- Dashboard rendering
- Runtime integration
- Notification sending
- Log rotation
- Audit search/query UI

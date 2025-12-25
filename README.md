# earcle-preflight
Ethical AI Research and Compliance Layer middleware platform

**What it is:**

Data-only repo for EARCLE content: the preflight spec, checks catalog, scoring, and example reports. 

**What’s real vs planned:**

Real: 
initial JSON placeholders and draft structure.

Planned: 
populate JSON with final content, add one-click demo path.

**Not included on purpose:**

App code, any backend or UI implementation, any real user data.

## Purpose

This repo stores EARCLE content as data so it stays editable and auditable without changing app code.

## Status

XXX

## How to review in 3 min

1. Open XXX
2. Open XXX
3. Open XXX

# EARCLE Preflight

## Purpose

EARCLE Preflight is a lightweight checklist and reference implementation that evaluates whether a conversational, health-adjacent AI interaction meets minimum expectations for consent clarity, data minimization, privacy, harm reduction, and auditability.

## Status

Prototype spec and minimal runnable reference. This repository includes no real participant data.

## What is in this repo

1. A human-readable checklist: [preflight-checklist.md](http://preflight-checklist.md/)
2. One file per check with rationale and pass fail criteria: checks/
3. A fake sample interaction object: sample-input.json
4. A sample report output: sample-output-report.json
5. A minimal Python runner that produces a report: run_preflight.py

## How to run

1. Install Python 3.10+.
2. Run: python run_preflight.py sample-input.json
3. Review the printed JSON report and compare with sample-output-report.json.

## Ethics and privacy

This repository is designed to avoid sensitive data exposure. Do not add raw user logs or participant data. Use only synthetic examples.

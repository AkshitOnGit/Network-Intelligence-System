# Network Intelligence System

## Problem Statement
Traditional network monitoring only detects threshold violations. This prototype transforms raw network telemetry into actionable intelligence by identifying anomalies, determining the probable root cause, assessing security risks, and generating an explainable incident report.

## Features
- Live network telemetry simulation
- Anomaly detection
- Root cause analysis
- Security assessment
- Explainable incident report

## Technology Stack
- Python 3
- VS Code

## Project Architecture
Network Telemetry → Data Processing → Anomaly Detection → Root Cause Analysis → Security Assessment → Incident Report

## How to Run

```bash
python main.py
```

## Design Decisions
- Rule-based anomaly detection
- Network topology for root-cause reasoning
- Explainable incident reports

## Limitations
- Simulated telemetry only
- Rule-based system
- No real Cisco devices

## Future Improvements
- Real-time SNMP telemetry
- Machine learning anomaly detection
- Web dashboard
- Email alerts

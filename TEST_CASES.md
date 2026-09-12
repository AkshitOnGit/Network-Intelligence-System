# Test Cases

## TC1 – Normal Network
Expected: No anomaly detected.

## TC2 – Latency Spike
Inject: R3 latency > 80 ms
Expected: High Latency alert.

## TC3 – Packet Loss
Inject: R3 packet loss > 7%
Expected: High Packet Loss detected.

## TC4 – CPU Overload
Inject: CPU ≥ 85%
Expected: Security assessment triggered.

## TC5 – Root Cause Analysis
Expected Root Cause: R3
Affected Components: R2, R4, R5

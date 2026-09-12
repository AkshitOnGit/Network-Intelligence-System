import random

devices = ["R1", "R2", "R3", "R4", "R5"]

telemetry = []

print("=" * 60)
print("        NETWORK INTELLIGENCE SYSTEM")
print("=" * 60)
print("Live Network Telemetry\n")

# Generate telemetry
for device in devices:

    latency = random.randint(10, 40)
    packet_loss = round(random.uniform(0, 1), 2)
    cpu = random.randint(20, 70)
    memory = random.randint(30, 80)

    # Inject a fault on R3
    if device == "R3":
        latency = random.randint(90, 140)
        packet_loss = round(random.uniform(6, 12), 2)
        cpu = random.randint(85, 98)

    telemetry.append({
        "device": device,
        "latency": latency,
        "packet_loss": packet_loss,
        "cpu": cpu,
        "memory": memory
    })

    print(f"{device}")
    print(f"  Latency      : {latency} ms")
    print(f"  Packet Loss  : {packet_loss}%")
    print(f"  CPU Usage    : {cpu}%")
    print(f"  Memory Usage : {memory}%")
    print("-" * 35)

# -----------------------------
# ANOMALY DETECTION
# -----------------------------
print("\n" + "=" * 60)
print("ANOMALY DETECTION")
print("=" * 60)

anomalies = []

for data in telemetry:

    reasons = []

    if data["latency"] > 80:
        reasons.append("High Latency")

    if data["packet_loss"] > 5:
        reasons.append("High Packet Loss")

    if data["cpu"] > 85:
        reasons.append("CPU Overload")

    if reasons:
        anomalies.append((data["device"], reasons))

if anomalies:
    for device, reasons in anomalies:
        print(f"ALERT: {device}")
        print("Reason:", ", ".join(reasons))
        print("-" * 30)
else:
    print("No anomalies detected.")
    
# -----------------------------
# ROOT CAUSE ANALYSIS
# -----------------------------

print("\n" + "=" * 60)
print("ROOT CAUSE ANALYSIS")
print("=" * 60)

network = {
    "R1": ["R2"],
    "R2": ["R1", "R3"],
    "R3": ["R2", "R4", "R5"],
    "R4": ["R3"],
    "R5": ["R3"]
}

if anomalies:

    root_device = anomalies[0][0]

    print(f"Probable Root Cause : {root_device}")

    affected = network[root_device]

    print("Affected Components :", ", ".join(affected))

else:
    print("Network operating normally.")
    
# -----------------------------
# SECURITY ASSESSMENT
# -----------------------------

print("\n" + "=" * 60)
print("SECURITY ASSESSMENT")
print("=" * 60)

for data in telemetry:

    if data["device"] == root_device:

        if data["packet_loss"] > 7 and data["cpu"] >= 85:
            security_status = "Potential Security Event"
            confidence = 94

        elif data["cpu"] >= 70:
            security_status = "Operational Performance Issue"
            confidence = 86

        else:
            security_status = "Normal"
            confidence = 100

        print("Classification :", security_status)
        print(f"Confidence     : {confidence}%")

        break
    
# -----------------------------
# INCIDENT REPORT
# -----------------------------

print("\n" + "=" * 60)
print("EXPLAINABLE INCIDENT REPORT")
print("=" * 60)

print(f"Incident ID           : INC-2026-001")
print(f"Severity              : HIGH")
print(f"Root Cause            : {root_device}")
print(f"Affected Components   : {', '.join(affected)}")
print(f"Classification        : {security_status}")
print(f"Confidence            : {confidence}%")

print("\nReasoning:")
print("- High latency detected on the root device.")
print("- Packet loss exceeded the acceptable threshold.")
print("- Neighboring devices are connected to the root device.")
print("- Rule-based analysis identified the most probable cause.")

print("\nRecommended Action:")
print("1. Inspect the root router.")
print("2. Verify interface health and bandwidth.")
print("3. Check for suspicious traffic or DoS activity.")
print("4. Continue monitoring affected devices.")
def detect_anomaly(logs):
    incidents = []

    for log in logs:
        if "OutOfMemory" in log:
            incidents.append(("OOM", log))
        elif "CPU usage above" in log:
            incidents.append(("CPU_SPIKES", log))
        elif "timeout" in log:
            incidents.append(("NETWORK_ERROR", log))

    return incidents

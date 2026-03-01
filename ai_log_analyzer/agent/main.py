from log_fetcher import fetch_logs
from anomaly import detect_anomaly
from classifier import classify
import time

seen = set()

while True:
    logs = fetch_logs()
    incidents = detect_anomaly(logs)

    for tag, log in incidents:
        if log in seen:
            continue
        seen.add(log)

        print("\nINCIDENT DETECTED")
        print(log)
        print("LLM TAGGING:")
        print(classify(log))
        
    for.sleep(10)

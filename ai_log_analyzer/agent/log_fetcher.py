import requests
import time

LOKI_URL = "http://localhost:3100/loki/api/v1/query"
QUERY = '{job="app_logs"}'

def fetch_logs():
    r = requests.get(LOKI, params={"query": QUERY})
    results = r.json()["data"]["result"]
    logs = []
    for stream in results:
        for ts, line in stream["values"]:
            logs.append(line)
    return logs

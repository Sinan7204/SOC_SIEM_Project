import json
import requests
import time

ALERT_FILE = "/var/ossec/logs/alerts/alerts.json"
HOOK_URL = "http://localhost:5678/webhook/wazuh-trigger"

print("Bridge running - Sending ALL alerts to n8n...")

with open(ALERT_FILE, "r") as f:
    f.seek(0, 2)

    while True:
        line = f.readline()

        if not line:
            time.sleep(0.1)
            continue

        try:
            alert = json.loads(line)
            requests.post(HOOK_URL, json=alert, timeout=5)
            print(f"Alert {alert.get('rule', {}).get('id')} sent!")
        except Exception:
            continue
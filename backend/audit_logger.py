
import json
from datetime import datetime

def log_event(user, role, query, status):
    log = {
        "user": user,
        "role": role,
        "query": query,
        "status": status,
        "timestamp": datetime.utcnow().isoformat()
    }

    with open("audit_logs.json", "a") as f:
        f.write(json.dumps(log) + "\n")

from typing import List, Dict
from datetime import datetime

def merge_logs(logs: Dict[str, List[Dict[str, str]]]):
    # Your code goes here

    # combine logs from all servers
    all_logs = []
    for type_ in logs.values():
        all_logs.extend(type_)

    # sorting based on timestamp
    sorted_logs = sorted(all_logs, key=lambda x: datetime.strptime(x["timestamp"], "%Y-%m-%d %H:%M:%S"))

    # print the log entries
    out = []
    for log in sorted_logs:
        out.append(log["timestamp"] + " [" + log["level"] + "] " + log["message"])

    return "\n".join(out)


logs_1 = {
    "Database_logs": [
        {
            "timestamp": "2024-07-18 10:15:00",
            "level": "ERROR",
            "message": "Database connection failed"
        },
        {
            "timestamp": "2024-07-18 14:42:00",
            "level": "INFO",
            "message": "Backup Started"
        },
        {
            "timestamp": "2024-07-18 11:04:00",
            "level": "ERROR",
            "message": "Unauthorized access detected"
        }
    ],
    "Authencation_logs": [
        {
            "timestamp": "2024-07-18 14:00:00",
            "level": "ERROR",
            "message": "External Authencation Service Down"
        },
        {
            "timestamp": "2024-07-18 12:23:00",
            "level": "ERROR",
            "message": "Token validation failed for user_id=1234"
        },
        {
            "timestamp": "2024-07-18 10:24:00",
            "level": "WARNING",
            "message": "Suspicious login attempt detected"
        },
        {
            "timestamp": "2024-07-18 14:47:00",
            "level": "WARNING",
            "message": "Multiple attempts detected"
        }
    ],
    "general_logs": [
        {
            "timestamp": "2024-07-18 13:16:00",
            "level": "INFO",
            "message": "Backup Started"
        },
        {
            "timestamp": "2024-07-18 12:27:00",
            "level": "ERROR",
            "message": "Disk full"
        },
        {
            "timestamp": "2024-07-18 11:33:00",
            "level": "ERROR",
            "message": "Unauthorized access detected"
        },
        {
            "timestamp": "2024-07-18 13:13:00",
            "level": "INFO",
            "message": "Connection established"
        }
    ]
}

print(merge_logs(logs_1))
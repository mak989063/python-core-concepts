from datetime import datetime
from typing import Dict, List

logs_1 = {
    'server1_logs': [
        {'timestamp': '2024-07-18 10:04:10', 'level': 'ERROR', 'message': 'Disk full'},
        {'timestamp': '2024-07-18 10:00:01', 'level': 'INFO', 'message': 'Server started'},
    ],
    'server2_logs': [
        {'timestamp': '2024-07-18 10:01:17', 'level': 'ERROR', 'message': 'Database connection failed'},
        {'timestamp': '2024-07-18 10:02:45', 'level': 'WARNING', 'message': 'High memory usage'},
    ]
}

def sort_logs(logs: dict[str, list[dict[str, str]]]):
    # Step 1: Combine
    all_logs = []
    for server in logs.values():
        all_logs.extend(server)

    # Step 2: Sort
    sorted_logs = sorted(
        all_logs,
        key=lambda x: x['timestamp']
    )

    # Output
    out = []
    for log in sorted_logs:
        out.append(log["timestamp"] +": "+ "[" + log["level"] + "] " + log["message"])

    return "\n".join(out)



print(sort_logs(logs_1))
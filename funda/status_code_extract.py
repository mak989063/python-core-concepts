import re

result = []

with open("../files/status_code_log.txt", "r") as file:
    for line in file:
        pattern = r"\b(\d{3})\b"
        m = re.search(pattern, line)
        if m:
            status_code = m.group(1)
            if status_code != '200':
                result.append(line.strip())

print(result)
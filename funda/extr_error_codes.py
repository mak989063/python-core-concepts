import re

# Log Files (ERR/WARN/FAIL)

def extract_error_codes(text):
    pattern = r"\b(?:ERR|WARN|FAIL)\d+\b"
    return re.findall(pattern, text)

data = """
ERROR: Service stopped with an ERR4088 at 12:40 AM
FAIL: DB Connection FAIL345
WARN: Service restarts with an warning WARN789
"""
data2="ERR123 occurred after WARN456 and FAIL789"
print(extract_error_codes(data))
print(extract_error_codes(data2))
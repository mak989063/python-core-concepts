import re

def valid_phone_number(s):
    pattern = r"\d{10}"
    return bool(re.fullmatch(pattern, s))

print(valid_phone_number("0129456789"))


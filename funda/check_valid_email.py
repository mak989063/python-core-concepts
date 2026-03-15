import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-z]+\.[a-zA-Z]{2,3}$"
    return bool(re.match(pattern, email))

print(is_valid_email("abcd@xyz.com")) #True
print(is_valid_email("abcd@gmail")) #False


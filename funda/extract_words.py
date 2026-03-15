import re
def extract_ing_words(text):
    pattern = r"\b\w+ing\b"
    return re.findall(pattern, text)

print(extract_ing_words("Hi Im running sleeping eating walking in my house"))

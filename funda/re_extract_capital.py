import re

text = "Scaler Academy is in Bangalore"

def get_capital_words(s):
    pattern = r"\b[A-Z][a-z]*\b"
    return re.findall(pattern, s)

def extract_time(t):
    pattern = r"\d{2}\d{2}\b"

print(get_capital_words(text))
print(get_capital_words("Hi I am Manikandan living in Bangalore South"))
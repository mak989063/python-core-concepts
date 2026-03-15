import re
text = "Mr. John"
pattern = r"(Mr|Mrs|Ms)\.?\s([A-Z][a-z]+)"
match = re.search(pattern, text)
print("Full Match:", match.group(0)) #complete match
print("Captured Match:", match.group(1)) #captured 1st group Mr
print("Captured Match:", match.group(2)) #capture 2nd group Name

#print("Captured Match:", match.group(3)) # Index error as there are only 2 groups

# Noncapturing group ---> ?:
pattern1 = r"(?:Mr|Mrs|Ms)\.?\s([A-Z][a-z]+)"
match1 = re.search(pattern1, text)
print("Captured Match:", match.group(1))
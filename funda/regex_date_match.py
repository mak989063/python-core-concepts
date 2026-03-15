import re

text = "Date: 14-12-1994"

pattern = r"(\d{2})-(\d{2})-(\d{4})"

match = re.search(pattern, text)

if match:
    print("Full Match:", match.group(0))
    print("Day:", match.group(1))
    print("Month:", match.group(2))
    print("Year:", match.group(3))

"""
re.match() #Matches only for the beginning - Check for the Match ONLY at the beginning of the string
re.search() #Matches only for the beginning of the string
re.match(pattern, text) #Matches only for the beginning
"""

"""
re.search() #search for the first occurence anywhere in the string
re.search(pattern, text) 
"""

"""
re.findall() #Returns all non-overlapping matches as a list of strings
"""
text1 = "My numbers are 10 and 20 and 30"
pattern1 = r"\d+"
match1 = re.findall(pattern1, text1)
print(match1) #['10', '20', '30']


"""
re.finditer() #Iterator of match objects
"""

text2 = "My numbers are 10 and 20 and 30"
pattern2 = r"\d+"
for match2 in re.finditer(pattern2, text2):
    print(match2.group(), match2.start(), match2.end())


"""
#replace match with a substring
re.sub()
"""
text2 = "My numbers are 10 and 20 and 30"
rep = re.sub(pattern2, "xx", text2)
print(rep)

"""
It will split the string with pattern as delimiter
re.split()
"""
import re

x = '(\d+)\s(?:apples|mangoes)'
print(re.findall(x, '7 apples and 4 mangoes'))
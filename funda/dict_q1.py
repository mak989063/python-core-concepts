input = 'Aakar Sharma'

res = {}

for ch in input:
    if ch not in res:
        res[ch] = 1
    else:
        res[ch] += 1

print(res)
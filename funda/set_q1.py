#Count of number of unique words in a sentence

input = "This is a sentence, This is not a paragraph"

res = {}

for word in input.split():
    if word in res:
        res.update(word)

print(res)

B = input('Enter boy name: ')
G = input('Enter girl name: ')

#make it lower case
b = B.lower()
g = G.lower()

#count unique letter - get unique
boy = set()
for char in b:
    if char not in boy:
        boy.update(char)

girl = set()

for char in g:
    if char not in girl:
        girl.update(char)


#remove common letters # B-G and G-B

b1 = len(boy - girl)
g1 = len(girl - boy)

#left out score

left_out_score = b1 + g1


#FLAMES check 1 2 3 4 5 6 keep a map

FLAMES = {'FRIEND':1, 'LOVE':2, 'AFFAIR':3, 'MARRIAGE':4, 'ENEMY':5, 'SIBLING':6}

target_value = (left_out_score % 6) or 6

for key, value in FLAMES.items():
    if value == target_value:
        print(f"Relationship between {B} and {G} is {key}")



#How to initialize
S = set() # S={}
S.add(10)
print(type(S))

#update method in set
Se= set()
li = ['blue','red','green']
Se.update(li)
print(Se)

#iterate
print(len(Se)) #length
for color in Se:
    print(color)

#Union/Intersection/Difference
A = {'Dosa', 'Burger', 'Chappathi', 'Porotta'}
B = {'Sandwich', 'Burger', 'Cheese Cake','KFC'}

print(A - B)
print(A.union(B))
print(A.intersection(B))



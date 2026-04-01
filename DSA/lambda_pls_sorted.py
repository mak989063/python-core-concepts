#Sort numbers by last digit

A = [13, 45, 37, 29, 46]

print(sorted(A, key = lambda x: x % 10))

#Sort by absolute difference from K
B = [10, 5, 3, 9, 2]
K = 7
print(sorted(B, key = lambda x: abs(x-K)))

#Sort list of tuples (marks DESC, name ASC)
students = [("Ram", 90), ("Shyam", 85), ("Amit", 90)]
print(sorted(students, key = lambda x: (-x[1], x[0])))

#Sort by frequency by desc
from collections import Counter
C = [4,4,1,2,2,3]
freq = Counter(C)
print(sorted(C, key=lambda x: (-freq[x])))

#Largest Number - Arrange to form largest number
#constraints - small numbers
D = [3, 30, 34, 5, 9]
D = list(map(str, D))
res = sorted(D, key = lambda x: x*10, reverse = True)
print("".join(res))

#works for large numbers
from functools import cmp_to_key
def compare(a, b):
    if a + b > b + a:
        return -1
    else:
        return 1

D = [3, 30, 34, 5, 9]

D = list(map(str, D))
D.sort(key=cmp_to_key(compare))
print("".join(D))


#Sort by number of set bits
E = [5, 3, 7, 10]
res2 = sorted(E, key = lambda x: bin(x).count("1"))
print(res2)
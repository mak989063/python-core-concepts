data = list(map(int, input().split()))
A = []


for i in range(1, len(data)):
    A.append(data[i])

print(A)

max_num = A[0]
min_num = A[0]

for i in range(1, len(A)):
    if  A[i] > max_num:
        max_num = A[i]

    if A[i] < min_num:
        min_num = A[i]

print(max_num, min_num, sep=" ", end="")
N,M = map(int,input().split())

A = []

for i in range(N):
    row = list(map(int,input().split()))
    A.append(row)

print(A)


for j in range(M):
    for i in range(N):
        print(A[i][j], end=" ")

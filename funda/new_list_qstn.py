N, M = map(int, input().split())

matrix = []

for i in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)

for i in range(N):
    for j in range(M):
        print(matrix[i][j], end=" ")
    print()



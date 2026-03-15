A = [
    [1, 2],
    [3, 4]
    ]

B = [
    [5, 6],
    [7, 8]
    ]

m = len(A)
n = len(B)
result = []
for i in range(m):
    row=[]
    for j in range(n):
        row.append(A[i][j]+B[i][j])
    result.append(row)

print(result)

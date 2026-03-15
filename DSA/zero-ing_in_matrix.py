matrix = [
    [1,2,3,14],
    [4,5,6,7],
    [8,9,10,0],
    [7,8,0,12]
        ]
# Assuming 'matrix' is your 2D list
n, m = len(matrix), len(matrix[0])

# Step 1: Traverse and mark
for i in range(n):
    flag = 0
    for j in range(m):
        if matrix[i][j] == 0:
            flag = 1
    if flag == 1:
        for j in range(m):
            if matrix[i][j] != 0:
                matrix[i][j] = -1

for j in range(m):
    flag = 0
    for i in range(n):
        if matrix[i][j] == 0:
            flag = 1
    if flag == 1:
        for i in range(n):
            if matrix[i][j] != 0:
                matrix[i][j] = -1

# Step 2: Replace markers with zeros
for i in range(n):
    for j in range(m):
        if matrix[i][j] == -1:
            matrix[i][j] = 0

print(matrix)
mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 0],
    [9, 10, 0, 12],
]

#output
"""
[
    [1, 2, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
"""

rows = set()
cols = set()

n = len(mat)
m = len(mat[0])

# Step 1: Find rows and cols containing zero
for i in range(n):
    for j in range(m):
        if mat[i][j] == 0:
            rows.add(i)
            cols.add(j)

# Step 2: Set matrix values to zero
for i in range(n):
    for j in range(m):
        if i in rows or j in cols:
            mat[i][j] = 0

print(mat)



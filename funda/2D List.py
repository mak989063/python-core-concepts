matrix = [
          [1, 1, 1],
          [2, 2, 2],
          [3, 3, 3],
          [4, 4, 4]
         ]

# Method1


for i in range(len(matrix)):
    sum = 0
    for j in range(len(matrix[i])):
        sum += matrix[i][j]
    print(f"row: {i}, sum is {sum}")

#method 2
"""
for i in range(len(matrix)):
    print(sum(matrix[i]))
"""





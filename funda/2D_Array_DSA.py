matrix = [
          [1, 1, 1],
          [2, 2, 2],
          [3, 3, 3]
         ]

# Method1 of col sum
M = 3
N = 3
for col in range(0,M):
    Sum = 0
    for row in range(0,N):
        Sum += matrix[row][col]
    print(f"Col: {col}, sum is {Sum}")

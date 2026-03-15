matrix = [
          [1, 1, 1],
          [2, 2, 2],
          [3, 3, 3],
          [4, 4, 4]
         ]

N = len(matrix)
i = 0
j = N - 1
while i < j and j >=0:
    print(matrix[i][j])
    i += 1
    j -= 1
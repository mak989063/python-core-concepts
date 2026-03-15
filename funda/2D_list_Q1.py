matrix = [
          [1, 1, 1],
          [2, 2, 2],
          [3, 3, 3],
          [4, 4, 4]
         ]
k = int(input("Enter the number that you want to search in the matrix: "))
is_found = False
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == k:
            print("Found at row ", i, " column ", j)
            is_found = True

if is_found == False:
    print("Not Found")
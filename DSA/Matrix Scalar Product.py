
def scalar_mult_matrix(A, B):
    rows = len(A)
    cols = len(A[0])

    for i in range(rows):
        for j in range(cols):
            A[i][j] *= B

    return A

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(scalar_mult_matrix(matrix, 2))
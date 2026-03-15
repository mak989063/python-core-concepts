


def solve(A):
    largest_element = A[0][0]
    result = []
    for i in range(len(A)):

        for j in range(len(A[i])):
            if A[i][j] > largest_element:
                largest_element = A[i][j]


    return result

A = [[1, 2],
     [1, 3]]
print(solve(A))
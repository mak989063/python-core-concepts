arr = [2, 4, 1, 3, 2]

def solve(A):
    Max = max(A)
    count = 0
    for i in range(len(A)):
        if A[i] != Max:
            diff = Max - A[i]
            count += diff

    return count

print(solve(arr))
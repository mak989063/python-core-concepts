def solve(A):
    if A < 2:
        return 0
    for i in range(2, (int(A ** 0.5) + 1)):
        if A % i == 0:
            return 0

    return 1




print(solve(13))


def incremental_print(n):
    if n == 0:
        return
    incremental_print(n-1)
    print(n, end=" ")

incremental_print(6)
print()
def decremental_print(n):
    if n==0:
        return
    print(n, end=" ")
    decremental_print(n-1)

decremental_print(4)

print()
def solve(A):
    if A == 0:
        return 0

    solve(A - 1)
    print(A, end=" ")

solve(10)
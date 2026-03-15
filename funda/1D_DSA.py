def solve(A):
    Max = A[0]
    Min = A[0]
    for num in A:
        if num > Max:
            Max = num
        elif num < Min:
            Min = num

    result = Max + Min
    return result

print(solve([1,5,9]))
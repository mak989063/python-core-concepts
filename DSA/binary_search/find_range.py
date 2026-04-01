def find_range(A, B):
    low, high = 0, len(A) - 1
    result = []
    res1, res2 = -1, -1

    while low <= high:
        mid = (low + high) // 2

        if A[mid] == B:
            res1 = mid
            high = mid - 1

        elif A[mid] > B:
            high = mid - 1

        else:
            low = mid + 1

    result.append(res1)

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            ans = mid
            low = mid + 1
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    result.append(res2)

    return result


A = [5, 7, 7, 8, 8, 10]
B = 8
print(find_range(A, B))
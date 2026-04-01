def first_first_occurrence(arr, k, n):
    low = 0
    high = n-1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == k:
            ans = mid
            high = mid - 1

        elif arr[mid] > k:
            high = mid - 1

        else:
            low = mid + 1

    return ans

arr = [1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 14, 15]
print(first_first_occurrence(arr, 2, len(arr)))
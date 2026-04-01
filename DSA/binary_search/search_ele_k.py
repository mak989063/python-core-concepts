def search_ele_k(arr, k):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == k:
            return mid
        elif k < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(search_ele_k(arr, 100))
def search(arr, k):
    ans = len(arr)
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


#A = [1, 3, 5, 6]
#B = 5


A = [1, 4, 9]
B = 3

print(search(A, B))
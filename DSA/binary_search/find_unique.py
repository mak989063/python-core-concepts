def find_unique_ele(arr,n):
    left = 0
    right = n - 1

    if n == 1:
        return arr[0]

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] != arr[mid + 1] and arr[mid] == arr[mid - 1]:
            return arr[mid]
        #Are we at first occurance

        #at the second occurence
        if arr[mid] == arr[mid + 1]:
            mid = mid - 1

        #is first occurence uniq

        if mid % 2 == 0:
            left = mid + 2

        else:
            right = mid - 1

    return arr[mid]


arr = [1,1,2,2,3,3,4,4,101,5,5,77,77,11,11]
print(find_unique_ele(arr, len(arr)))







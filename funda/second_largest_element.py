def find_second_largest_element(arr):


    if len(arr) < 2:
        return -1

    first = -1
    second = -1

    for i in range(len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] < first:
            second = arr[i]

    return second


print(find_second_largest_element([1,1,1,1,1,1]))
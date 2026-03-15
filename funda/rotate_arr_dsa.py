#rotate array with k as rotation count
from _pyrepl.commands import end
from turtledemo.penrose import start

A = [1,2,3,4,5]
N = len(A)
def reverse_arr(arr, N, start, end):
    i = start
    j = end

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr

def rotate_k_times(arr, N, k):
    reverse_arr(arr, N, 0, N-1)
    reverse_arr(arr, N, 0, k-1)
    reverse_arr(arr, N, k, N-1)
    return arr

print(rotate_k_times(A, N, 3))



from collections import deque


def sliding_window_max(arr, n, k):
    dq = deque()
    result = []
    #Adding first k elemenets to window

    for i in range(0, k):
        while len(dq) > 0 and dq[-1] < arr[i]:
            dq.pop()
        dq.append(arr[i])

    result.append(dq[0])

    for i in range(k, n):

        # add i'th ele and remove (i-k)th ele
        #remove
        if arr[i-k] == dq[0]:
            dq.popleft()
        #add
        while len(dq) > 0 and dq[-1] < arr[i]:
            dq.pop()

        dq.append(arr[i])

    result.append(dq[0])

    return result


arr = [10,1,9,3,7]
print(sliding_window_max(arr, len(arr), 4))
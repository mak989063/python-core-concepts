from collections import deque


def first_non_repeating(A):
    freq = {}
    q = deque()
    result = []

    for ch in A:
        # Step 1: update frequency
        freq[ch] = freq.get(ch, 0) + 1

        # Step 2: push into queue
        q.append(ch)

        # Step 3: remove repeating chars from front
        while q and freq[q[0]] > 1:
            q.popleft()

        # Step 4: add answer
        if q:
            result.append(q[0])
        else:
            result.append('#')

    return "".join(result)


A = "aabbdd"
print(first_non_repeating(A))
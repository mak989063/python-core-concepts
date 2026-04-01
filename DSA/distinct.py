def solve(A):
    map = {}

    for ele in A:
        if ele not in map:
            map[ele] = 1
        else:
            map[ele] += 1

    ans = []
    for m in map:
            ans.append(m)

    return len(ans)

print(solve([3, 4, 3, 6, 6]))
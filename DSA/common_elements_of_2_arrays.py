def find_common_elements(A, B):
    map = {}
    for ele in B:
        if ele not in map:
            map[ele] = 1
        else:
            map[ele] += 1

    ans = []
    for ele in A:
        if ele in map and map[ele] >0:
            ans.append(ele)
            map[ele] -= 1

    return ans

A = [2, 7, 10, 5]
B = [2, 4, 1, 2, 10]
print(find_common_elements(A, B))
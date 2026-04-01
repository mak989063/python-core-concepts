def count_elements(arr, que):
    map = {}

    for ele in arr:
        if ele in map:
            map[ele] += 1
        else:
            map[ele] = 1

    ans = []
    for q in que:
        ans.append(map.get(q, 0))   # always append

    return ans


array = [2,6,3,8,2,8,2,3]
queue = [1,6]

print(count_elements(array, queue))


#TC - O(n+q)
#SC - O(n)
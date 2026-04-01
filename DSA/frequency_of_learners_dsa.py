"""
A = [1, 2, 1, 1]
B = [1, 2]

Example Output

Output 1:
[3, 1]

"""

def solve(A):
    map = {}
    for ele in A:
        if ele in map:
            map[ele] += 1
        else:
            map[ele] = 1

    ans = []
    for ele in map:
        ans.append(map[ele])

    return ans

print(solve([1, 2, 1, 1]))
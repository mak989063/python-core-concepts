def longestCommonPrefix(strs):
    if not strs:
        return ""

    res = ""

    for i in range(len(strs[0])):
        char = strs[0][i]

        for s in strs:
            if i >= len(s) or s[i] != char:
                return res

        res += char

    return res


print(longestCommonPrefix(["flower", "flow", "float"]))
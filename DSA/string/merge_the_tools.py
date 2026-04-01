def merge_the_tools(string, k):
    n = len(string)

    for i in range(0, n, k):
        substring = string[i:i+k]
        seen = set()
        result = ""

        for ch in substring:
            if ch not in seen:
                seen.add(ch)
                result += ch

        print(result)


string = 'AABCAAADA'
k = 3
merge_the_tools(string, k)
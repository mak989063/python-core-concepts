
def solve(A):
    str_dup = A + A
    vowels = ['a', 'e', 'i', 'o', 'u']
    result  = ""

    for ch in str_dup:
        if ch.isupper():
            continue
        elif ch in vowels:
            result += "#"
        else:
            result += ch

    return result


print(solve("AbiCdo"))


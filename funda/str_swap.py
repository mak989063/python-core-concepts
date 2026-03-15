def solve(A):
    vowels = ["a", "e", "i", "o", "u"]
    count_vowels = 0
    count_consonants = 0
    ls = []

    for char in A:
        if char in vowels:
            count_vowels += 1
        else:
            count_consonants += 1

    return [count_vowels, count_consonants]






print(solve("yjbkogxfgzlajycctiatwflqgpojdjebtfohlloumzuwzyashanfibvoqaaalxt"))
import re

def count_occurrences(A):
    pattern = r"(?=bob)"
    matches = re.findall(pattern, A)

    return len(matches)


print(count_occurrences("bobbgtrtbob"))

def count_occurrences2(A):
    count = 0
    for i in range(len(A) - 2):
        if A[i:i+3] == "bob":
            count += 1
    return count

print(count_occurrences2("bobbob"))  # 2



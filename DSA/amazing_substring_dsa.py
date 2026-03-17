def amazing_substring_dsa(A):
    vowels = "aeiouAEIOU"
    n = len(A)
    count = 0

    for i in range(n):
        if A[i] in vowels:
            count += (n - i)

    return count % 10003


print(amazing_substring_dsa("ABEC"))
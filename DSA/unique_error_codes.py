def first_unique_error_codes(arr):
    freq = {}

    # Count frequency
    for x in arr:
        freq[x] = freq.get(x, 0) + 1

    # Find first unique
    for x in arr:
        if freq[x] == 1:
            return x

    return -1   # if no unique element

print(first_unique_error_codes([404,500,200,200,500,404,403,404,405]))
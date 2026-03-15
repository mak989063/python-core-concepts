A = [1,1,2,3,18,4,4,5,5,6,6,6,7,8,7,9,10,3,1,12,11,12,13,13,13,14,14,15,14,16,1,17,1]

def remove_duplicates(A):
    result = []
    for item in A:
        if item not in result:
            result.append(item)

    return sorted(result)


print(remove_duplicates(A))



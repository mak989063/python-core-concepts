def max_of_3_using_functn(a, b):
    if a > b:
        return a
    elif b > a:
        return b


print(max_of_3_using_functn(3,4))

print(max_of_3_using_functn((max_of_3_using_functn(3,4)),5))



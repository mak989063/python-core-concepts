def remove_equal_pairs(str):
    stack = []
    for char in str:
        if stack and stack[-1] == char:
            stack.pop()

        else:
            stack.append(char)

    return ''.join(stack)


print(remove_equal_pairs("abbcd"))
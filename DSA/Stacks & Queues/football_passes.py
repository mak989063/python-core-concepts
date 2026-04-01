def find_final_player(A, B, C):
    stack = [B]

    for move in C:
        if move == 0:
            if len(stack) > 1:
                stack.pop()
        else:
            stack.append(move)

    return stack[-1]

A = 10
B = 23
C = [86, 63, 60, 0, 47, 0, 99, 9, 0, 0]

print(find_final_player(A, B, C))
def evaluate_expr(arr):
    stack = []
    operators = {"+", "-", "*", "/"}

    for ch in arr:
        if ch not in operators:
            stack.append(int(ch))
        else:
            ele1 = stack.pop()
            ele2 = stack.pop()

            res = perform_operation(ele2, ele1, ch)
            stack.append(res)

    return stack[-1]


def perform_operation(first, second, operator):
    if operator == '/':
        return int(first / second)

    elif operator == '*':
        return first * second

    elif operator == '+':
        return first + second

    elif operator == '-':
        return first - second

    return 0


A = ["2", "-11", "+", "3", "*"]
print(evaluate_expr(A))
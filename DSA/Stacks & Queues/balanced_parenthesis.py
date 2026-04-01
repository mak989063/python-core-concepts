def is_balanced(str):
    stack = []
    for ch in str:
        if is_open_type(ch):
            stack.append(ch)
        else:
            ele = stack.pop()
            if is_matching_char(ch, ele) == False:
                return False

    if len(stack) > 0:
        return False

    return True

def is_open_type(ch):
    if ch == '(' or ch == '[' or ch == '{':
        return True

    return False

def is_matching_char(open, closing):
    if open == "{":
        if closing != "}":
            return False

    if open == "[":
        if closing != "]":
            return False

    if closing == "(":
        if open != ")":
            return False

    return True

str = "()[]{}{"
print(is_balanced(str))
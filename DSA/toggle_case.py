def toggle_case(string):
    result = []
    for ch in string:
        if ('a' <= ch <= 'z'):
            result.append(chr(ord(ch)-32))
        elif ('A' <= ch <= 'Z'):
            result.append(chr(ord(ch)+32))

    return ''.join(result)

print(toggle_case("Man,i"))
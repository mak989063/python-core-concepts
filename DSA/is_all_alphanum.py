def is_all_alphanum(s):
    flag = 0
    for ch in s:
        if not (48 <= ord(ch) <= 57 or 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122):
            flag = 0
            break
        else:
            flag = 1

    return flag

print(is_all_alphanum('abcde#fgh'))
print(is_all_alphanum('abcdefgh'))


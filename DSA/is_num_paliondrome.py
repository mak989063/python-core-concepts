def is_num_paliondrome(n):
    temp = n
    reversed_num = 0
    while n > 0:
        rem = n % 10
        reversed_num = reversed_num * 10 + rem
        n = n // 10

    if reversed_num == temp:
        return True
    else:
        return False


print(is_num_paliondrome(1221))


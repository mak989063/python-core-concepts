
Sum = 0
A = int(input())

if A % 10 == 0:
    A = A // 10
    while A != 0:
        rem = A % 10
        Sum = Sum * 10 + rem
        A = A // 10
    print(Sum)

else:
    while A != 0:
        rem = A % 10
        Sum = Sum * 10 + rem
        A = A // 10
    print(Sum)
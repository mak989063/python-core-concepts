def reverse_dsa():
    T = int(input())
    rev = []
    for t in range(T):
        N = int(input())
        temp = N
        Sum = 0
        while N > 0:
            rem = N % 10
            Sum = Sum * 10 + rem
            if N < 10:
                rev.append(Sum)
            N = N // 10

    return "\n".join(str(item) for item in rev)

print(reverse_dsa())
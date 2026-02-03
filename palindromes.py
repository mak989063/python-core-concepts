N = int(input())
temp = N
Sum = 0

while N>0:
    rem = N % 10
    Sum = Sum * 10 + rem
    N = N // 10

if Sum == temp:
    print("YES")
else:
    print("NO")

N = int(input())
sum = 0
while N>0:
    rem = N % 10
    sum = sum + rem
    N //= 10

print(sum)
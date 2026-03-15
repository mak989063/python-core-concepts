N = int(input())

A = list(map(int, input().split()))

x = int(input())

A.pop(x-1)

for num in A:
    print(num, end=" ")




T = int(input())
N = int(input())

A = list(map(int, input().split()))

B = int(input())

for i in range(len(A)):
    if A[i] == B:
        print()
        break
    print(0)
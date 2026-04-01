s="CODER"
n = len(s)

for i in range(n-1, -1, -1):
    if i == n - 1:
        print(" ".join(s[i::-1]), end=" ")
    else:
        print(" " * 2 * (n-1-i) + " ".join(s[i::-1]), end=" ")
    print()
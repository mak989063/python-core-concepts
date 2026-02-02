n = int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()

    """
    #spaces = n - i
    #stars = i
    #print(" " * spaces + "*" * stars)
    """
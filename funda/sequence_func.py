def sequence(n):

    for i in range(1,n+1):
        print(i, end= " ")
    print()
    for i in range(n,0,-1):
        print(i, end= " ")

    return

sequence(10)
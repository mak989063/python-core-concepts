def main():
    A = int(input())
    B = int(input())
    C = int(input())

    #print(max(A, B, C))

    if A > B and A > C:
        print(A)
    elif B > A and B > C:
        print(B)
    elif C > A and C > B:
        print(C)
    else:
        print("equal")

    return 0

if __name__ == '__main__':
    main()
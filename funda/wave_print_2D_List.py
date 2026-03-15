A = [ [4,1,2],
      [7,4,4],
      [3,7,4]
    ]

for i in range(len(A)):
    if i % 2 != 0:
        for j in range(len(A[i])-1,-1,-1):
            print(A[i][j],end=" ")
    else:
        for j in range(len(A[i])):
            print(A[i][j],end=" ")


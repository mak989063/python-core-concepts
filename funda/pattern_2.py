n = int(input())
for i in range(1,n+1,2):
    spaces = (2 * (n - i)) // 2
    sp_gap = spaces // 2
    stars = i
    print(" " * sp_gap + "*" * stars + " " * sp_gap, end="")
    print()

#Output
"""

   *   
  ***  
 ***** 
*******


"""
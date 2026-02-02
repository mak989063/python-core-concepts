"""
Problem Description

You are given the Cost Price C and Selling Price S of a Product.
You have to tell whether there is a Profit or Loss. Also, calculate total profit or loss.

NOTE: It is guaranteed that Cost Price and Selling Price are not equal.

NOTE: You have to take input of the Cost Price(C) and Selling Price(S) from the user.

"""

C = int(input())
S = int(input())

pr_or_ls = S - C

if (pr_or_ls > 0):
    print(1)
    print(abs(pr_or_ls))
elif (pr_or_ls < 0):
    print(-1)
    print(abs(pr_or_ls))
else:
    print(0)
    print(abs(pr_or_ls))
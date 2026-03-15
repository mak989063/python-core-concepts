"""
You are given an integer A. You have to tell whether it is a perfect number or not.

Perfect number is a positive integer which is equal to the sum of its proper positive divisors.

A proper divisor of a natural number is the divisor that is strictly less than the number.
"""

def solve(A):
    divisors = []
    for i in range(1,A):
        if A % i == 0:
            divisors.append(i)
    sum_divisors = 0
    for divisor in divisors:
        sum_divisors += divisor

    if sum_divisors == A:
        return 1

    return 0

print(solve(6))



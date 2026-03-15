def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial_iterative(number)}")

# Output for number = 5: The factorial of 5 is 120

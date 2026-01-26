number = int(input("Enter a number: "))
print(f"Multiplication Table for {number}: ")
for i in range(1, 11):
    result = i * number
    print(f"{i} x {number} = {result}")
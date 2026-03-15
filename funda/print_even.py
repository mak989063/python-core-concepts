marks = int(input("Enter marks: "))

if marks > 90 and marks <= 100:
    print("A grade")
elif marks > 80 and marks <= 90:
    print("B grade")
elif marks > 70 and marks <= 80:
    print("C grade")
elif marks >=0 and marks <= 70:
    print("D grade")
else:
    print("Invalid input")
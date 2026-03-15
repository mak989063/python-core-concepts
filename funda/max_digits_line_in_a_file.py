max_digits = -1
result_line = ""

with open("testFile.txt", "r") as file:
    for line in file:
        digit_count = 0
        for char in line:
            if char.isdigit():
                digit_count += 1

        if digit_count > max_digits:
            max_digits = digit_count
            result_line = line

print(result_line.rstrip("\n"))

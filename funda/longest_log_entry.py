lines = [
"DevOps is awesome.",
"Error: Disk not found.",
"Server started successfully at 10:05 AM.", "OK"
    ]

max_line = ""
for line in lines:
    if len(line) > len(max_line):
        max_line = line
print(max_line)





#Output:
#Server started successfully at 10:05 AM.
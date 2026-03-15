#import sys
#print(sys.getdefaultencoding())

#open and closing file

#file = open("sample1.txt", "r+") #if file not present, error
#file1 = open("files/data_0.txt", "w+") #if file not present, creates new

#print("abcd")

#file1.close()

#Wrte method
# 1) write()
# - takes string and writes to it
# - writes content at the current cursor position
# - returns how many bytes (chars) it wrote
file = open("sample.txt", "w+")
file.write("Hello World")
file.close()

#2) writelines()
# - takes multiple stings(lines) and writes it to the file in one go (list of strings)
# -
file = open("sample.txt", "w+")
file.writelines(["Hello \n","Hi \n", "How are you? \n"])
file.close()

#3 reading a file
#a)read() - reading all the contents of the file in one go
#b)readline() - read only a line/read line by line
#c)read lines() - all the content would be loaded to list of strings
"""
file = open("sample.txt", "w+")
file.write("Hello World, HI")
file.writelines(["\nHi \n", "How \n"])
file.writelines(["\nHow is the class going \n", "lets go the party\n"])
file.seek(0)

for line in file.readlines():
    print(line)
    print("------------")
file.close()
"""
"""
file = open("sample.txt", "r")
while True:
    line = file.read(2)
    print(line)
    if not line:
        break
file.close()

"""
## with open() - automatically closes the file when comes out of the block
"""
f = open("testFile.txt", "r")
print(f.readline())
f.close()
"""
upper=0
f = open("testFile.txt", 'r')

line = f.read()

for i in line:
    if (i.isupper()==True):
        upper+=1
print(upper)
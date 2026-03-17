def numcount():
    numb=0
    f1=open("Python.txt",'r')
    line=f1.read()
    for i in line:
        if (i.isnumeric() == True):
            numb+=1
    print("Total no. of numeric characters :",numb)

numcount()


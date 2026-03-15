def modify(s):

    result = None

    if len(s) < 3:
        result=s
    elif len(s)>= 3 and s[-3::] == "ing":
        result = s+"ly"
    else:
        result = s+"ing"
    return result

print(modify("String"))

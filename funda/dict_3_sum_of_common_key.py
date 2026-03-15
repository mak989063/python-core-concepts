def commonKey(dict1, dict2):
    '''dict1, dict2 are the two dictionaries
       print the required dictionary'''

    dict3 = {}

    # YOUR CODE GOES HERE

    for key in dict1:
        if key in dict2:
            dict3[key] = dict1[key] + dict2[key]

    return dict3



print(commonKey({'a':1, 'b':2, 'c':3}, {'c':4, 'd':2, 'e':3}))
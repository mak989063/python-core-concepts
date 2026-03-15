def set_operation(sent1, sent2):
    ''' input:sent1,sent2-two sentences taken as inputs
         output:return the sum of length of unique words.'''

    # YOUR CODE GOES HERE

    li1 = sent1.split()
    li2 = sent2.split()

    s1 = set(li1)
    s2 = set(li2)

    print(s1)
    print(s2)

    result_index = len(s1) + len(s2)

    return result_index

"""
    for word in li1:
        if word not in s1:
            s1.add(word)
    
    for word in li2:
        if word not in s2:
            s2.add(word)                
"""

print(set_operation("I love cricket cricket","I love football too"))



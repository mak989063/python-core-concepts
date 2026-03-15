def shopping_list():
    shoplist = []

    while True:
        s = input()


        if s != "end":
            shoplist.append(s)
        else:
            break

    print(shoplist)


'''Calling the function'''

shopping_list()
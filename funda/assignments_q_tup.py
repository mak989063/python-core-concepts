def odd_even_split_tuple(tup):
    tup_odd = []
    tup_even = []

    for i in range(len(tup)):
        if (i + 1) % 2 != 0:
            tup_odd.append(tup[i])
        else:
            tup_even.append(tup[i])

    print("Odd:", tuple(tup_odd))
    print("Even:", tuple(tup_even))


odd_even_split_tuple((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2))

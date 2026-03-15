def simple_int(time, pa, ir):
    ''' time, pa, ir represents the time in number of days, principal amount and rate of interest
        Return the simple interest'''
    ans = 0
    # YOUR CODE GOES HERE

    no_year = time / 365
    s_i = pa * no_year * ir / 100
    ans = pa + s_i

    return round(ans, 2)

print(simple_int(789,10000.00, 1.3))

print(simple_int(0,10000.00, 0.0))

